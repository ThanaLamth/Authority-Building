#!/usr/bin/env python3
"""
publish_to_wp.py
Publishes one NFTEnex article from the local repo clone to a WordPress site via REST API.

Usage:
    python scripts/publish_to_wp.py \
        --article nftenex/articles/01-best-nft-minting-tools-2026.md \
        --media-dir nftenex/media \
        --wp-url https://yoursite.com \
        --wp-user admin \
        --wp-pass "xxxx xxxx xxxx xxxx xxxx xxxx" \
        --status draft

Dependencies: pip install requests markdown PyYAML
"""

import argparse
import base64
import os
import re
import sys

import markdown
import requests
import yaml


# ── CLI ──────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--article",   required=True, help="Path to .md article file")
    p.add_argument("--media-dir", required=True, help="Directory containing PNG files")
    p.add_argument("--wp-url",    required=True, help="WordPress site root URL (no trailing slash)")
    p.add_argument("--wp-user",   required=True, help="WordPress username")
    p.add_argument("--wp-pass",   required=True, help="Application Password")
    p.add_argument("--status",    default="draft", choices=["draft", "publish", "future"])
    return p.parse_args()


# ── Auth ─────────────────────────────────────────────────────────────────────

def auth_header(user, app_pass):
    token = base64.b64encode(f"{user}:{app_pass}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


# ── Frontmatter ───────────────────────────────────────────────────────────────

def parse_frontmatter(content):
    m = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not m:
        raise ValueError("No YAML frontmatter found")
    fm = yaml.safe_load(m.group(1))
    body = content[m.end():]
    return fm, body


# ── Image parsing ─────────────────────────────────────────────────────────────

# Matches: ![alt](../media/file.png)\n\n*caption*
# Also handles cases where caption line is directly after image with single newline
IMG_BLOCK = re.compile(
    r"!\[([^\]]*)\]\(\.\.\/media\/([\w\-\.]+\.png)\)"   # ![alt](../media/file.png)
    r"\s*\n\s*\n?"
    r"\*([^*\n][^\n]*)\*",                               # *caption*
    re.MULTILINE,
)

# Matches bare image with no following caption
IMG_BARE = re.compile(
    r"!\[([^\]]*)\]\(\.\.\/media\/([\w\-\.]+\.png)\)",
    re.MULTILINE,
)


def collect_image_filenames(body):
    """Return ordered list of unique image filenames referenced in the article."""
    seen = []
    seen_set = set()
    for m in IMG_BARE.finditer(body):
        fname = m.group(2)
        if fname not in seen_set:
            seen.append(fname)
            seen_set.add(fname)
    return seen


# ── Media upload ──────────────────────────────────────────────────────────────

def upload_image(wp_url, headers, media_dir, filename, alt_text, caption):
    """Upload one image. Returns (media_id, source_url) or None on failure."""
    path = os.path.join(media_dir, filename)
    if not os.path.exists(path):
        print(f"  [SKIP] File not found: {path}")
        return None

    with open(path, "rb") as f:
        data = f.read()

    upload_headers = {
        **headers,
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Content-Type": "image/png",
    }
    r = requests.post(f"{wp_url}/wp-json/wp/v2/media", headers=upload_headers, data=data)
    if r.status_code not in (200, 201):
        print(f"  [FAIL] Upload {filename}: {r.status_code} {r.text[:200]}")
        return None

    media_id  = r.json()["id"]
    source_url = r.json()["source_url"]

    # Set alt_text and caption via PATCH
    patch = {"alt_text": alt_text, "caption": caption}
    pr = requests.post(
        f"{wp_url}/wp-json/wp/v2/media/{media_id}",
        headers={**headers, "Content-Type": "application/json"},
        json=patch,
    )
    if pr.status_code not in (200, 201):
        print(f"  [WARN] Could not set alt/caption for {filename}: {pr.status_code}")

    print(f"  [OK] {filename} -> id={media_id}")
    return media_id, source_url


# ── Content conversion ────────────────────────────────────────────────────────

PLACEHOLDER = "___FIGURE_{i}___"

def build_figure_html(src_url, alt, caption, media_id):
    return (
        f'<!-- wp:image {{"id":{media_id}}} -->\n'
        f'<figure class="wp-block-image">'
        f'<img src="{src_url}" alt="{alt}" class="wp-image-{media_id}"/>'
        f'<figcaption class="wp-element-caption">{caption}</figcaption>'
        f'</figure>\n'
        f'<!-- /wp:image -->'
    )


def convert_content(body, media_map, alt_map, caption_map):
    """
    media_map:   filename -> (media_id, source_url)
    alt_map:     filename -> alt text
    caption_map: filename -> caption text
    """
    figures = {}  # placeholder_key -> figure HTML

    def replace_block(m):
        alt, fname, cap = m.group(1), m.group(2), m.group(3)
        if fname not in media_map:
            return m.group(0)  # leave unchanged if upload failed
        mid, url = media_map[fname]
        key = PLACEHOLDER.format(i=len(figures))
        figures[key] = build_figure_html(url, alt, cap, mid)
        return key

    # Replace full image+caption blocks first
    body = IMG_BLOCK.sub(replace_block, body)

    # Replace any remaining bare image references (no caption)
    def replace_bare(m):
        alt, fname = m.group(1), m.group(2)
        if fname not in media_map:
            return m.group(0)
        mid, url = media_map[fname]
        cap = caption_map.get(fname, alt)
        key = PLACEHOLDER.format(i=len(figures))
        figures[key] = build_figure_html(url, alt, cap, mid)
        return key

    body = IMG_BARE.sub(replace_bare, body)

    # Strip H1 (first # line) -- WP stores title separately
    body = re.sub(r"^#[^\n]+\n", "", body, count=1)

    # Convert remaining Markdown to HTML
    html = markdown.markdown(
        body,
        extensions=["tables", "fenced_code", "nl2br"],
    )

    # Restore figure placeholders (they must not be inside <p> tags)
    for key, fig in figures.items():
        # markdown() may wrap the placeholder in <p>...</p>
        html = html.replace(f"<p>{key}</p>", fig)
        html = html.replace(key, fig)

    return html


# ── Post creation ─────────────────────────────────────────────────────────────

def create_post(wp_url, headers, title, slug, html, excerpt, status,
                featured_media_id, primary_keyword):
    payload = {
        "title":          title,
        "slug":           slug.lstrip("/"),
        "content":        html,
        "excerpt":        excerpt,
        "status":         status,
        "featured_media": featured_media_id,
    }
    # RankMath meta (ignored silently if plugin not active)
    payload["meta"] = {
        "rank_math_focus_kw":    primary_keyword,
        "rank_math_description": excerpt,
    }

    r = requests.post(
        f"{wp_url}/wp-json/wp/v2/posts",
        headers={**headers, "Content-Type": "application/json"},
        json=payload,
    )
    return r


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    args = parse_args()

    with open(args.article, encoding="utf-8") as f:
        raw = f.read()

    fm, body = parse_frontmatter(raw)

    title           = fm.get("title", "Untitled")
    slug            = fm.get("slug", "")
    meta_desc       = fm.get("meta_description", "")
    primary_keyword = fm.get("primary_keyword", "")

    print(f"\nArticle : {title}")
    print(f"Slug    : {slug}")
    print(f"Target  : {args.wp_url}\n")

    headers = auth_header(args.wp_user, args.wp_pass)

    # Build alt + caption maps from image blocks in body
    alt_map     = {}
    caption_map = {}
    for m in IMG_BLOCK.finditer(body):
        alt, fname, cap = m.group(1), m.group(2), m.group(3)
        alt_map[fname]     = alt
        caption_map[fname] = cap
    # Bare images (no caption) -- alt only
    for m in IMG_BARE.finditer(body):
        fname = m.group(2)
        if fname not in alt_map:
            alt_map[fname] = m.group(1)

    filenames = collect_image_filenames(body)
    print(f"Images to upload: {len(filenames)}")

    media_map = {}          # fname -> (id, url)
    featured_media_id = 0

    for fname in filenames:
        alt  = alt_map.get(fname, fname)
        cap  = caption_map.get(fname, alt)
        result = upload_image(args.wp_url, headers, args.media_dir, fname, alt, cap)
        if result:
            media_map[fname] = result
            if featured_media_id == 0:
                featured_media_id = result[0]

    print(f"\nUploaded {len(media_map)}/{len(filenames)} images")
    print(f"Featured media ID: {featured_media_id}\n")

    html = convert_content(body, media_map, alt_map, caption_map)

    print("Creating post...")
    r = create_post(
        args.wp_url, headers,
        title, slug, html, meta_desc, args.status,
        featured_media_id, primary_keyword,
    )

    if r.status_code in (200, 201):
        data = r.json()
        print(f"\n[SUCCESS]")
        print(f"  Post ID  : {data['id']}")
        print(f"  Status   : {data['status']}")
        print(f"  URL      : {data.get('link', '(draft -- no public URL yet)')}")
    else:
        print(f"\n[FAIL] {r.status_code}")
        print(r.text[:500])
        sys.exit(1)


if __name__ == "__main__":
    main()