#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import markdown
from bs4 import BeautifulSoup


REPO_ROOT = Path("/home/qwen/Authority-Building")
PACKAGE_ROOT = REPO_ROOT / "Coinlineup"
ARTICLES_DIR = PACKAGE_ROOT / "articles"
HTML_DIR = PACKAGE_ROOT / "html"
PAYLOADS_DIR = PACKAGE_ROOT / "payloads"
GITHUB_RAW_BASE = (
    "https://raw.githubusercontent.com/ThanaLamth/Authority-Building/main/Coinlineup/media"
)


@dataclass
class ArticleMetadata:
    title: str
    meta_title: str
    meta_description: str
    slug: str
    primary_keyword: str
    category: str
    schema_label: str
    last_updated: str


def strip_ticks(value: str) -> str:
    value = value.strip()
    if value.startswith("`") and value.endswith("`"):
        return value[1:-1]
    return value


def parse_metadata(lines: list[str]) -> tuple[ArticleMetadata, int]:
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Missing H1 title")

    title = lines[0][2:].strip()
    raw: dict[str, str] = {}
    index = 1

    while index < len(lines) and not lines[index].strip():
        index += 1

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            break
        if not line.startswith("- "):
            break
        key, value = line[2:].split(":", 1)
        raw[key.strip().lower()] = strip_ticks(value)
        index += 1

    metadata = ArticleMetadata(
        title=title,
        meta_title=raw["meta title"],
        meta_description=raw["meta description"],
        slug=raw["slug"],
        primary_keyword=raw["primary keyword"],
        category=raw["category"],
        schema_label=raw["schema"],
        last_updated=raw["last updated"],
    )
    return metadata, index


def extract_section(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else None


def parse_internal_links(section: str | None) -> list[dict[str, str]]:
    if not section:
        return []
    items: list[dict[str, str]] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        match = re.match(
            r"- \[([^\]]+)\]\(([^)]+)\)\s+Suggested anchor:\s+`([^`]+)`",
            line,
        )
        if match:
            items.append(
                {
                    "label": match.group(1),
                    "url": match.group(2),
                    "suggested_anchor": match.group(3),
                }
            )
    return items


def parse_external_links(section: str | None) -> list[dict[str, str]]:
    if not section:
        return []
    items: list[dict[str, str]] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        match = re.match(r"- \[([^\]]+)\]\(([^)]+)\)", line)
        if match:
            items.append({"label": match.group(1), "url": match.group(2)})
    return items


def media_path_to_raw_url(media_path: str) -> str:
    filename = Path(strip_ticks(media_path)).name
    return f"{GITHUB_RAW_BASE}/{filename}"


def parse_media(section: str | None) -> list[dict[str, str]]:
    if not section:
        return []
    items: list[dict[str, str]] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        match = re.match(r"- `([^`]+)`\s+Caption:\s+`([^`]+)`", line)
        if match:
            local_path = match.group(1)
            items.append(
                {
                    "local_path": local_path,
                    "raw_url": media_path_to_raw_url(local_path),
                    "caption": match.group(2),
                }
            )
    return items


def parse_source_set(section: str | None) -> list[str]:
    if not section:
        return []
    items: list[str] = []
    for line in section.splitlines():
        line = line.strip()
        if line.startswith("- "):
            items.append(line[2:].strip())
    return items


def remove_editorial_blocks(body: str) -> str:
    filtered_lines: list[str] = []
    skipping_captions = False

    for line in body.splitlines():
        stripped = line.strip()
        if stripped == "Recommended captions:":
            skipping_captions = True
            continue
        if skipping_captions:
            if not stripped or stripped.startswith("- "):
                continue
            skipping_captions = False
        filtered_lines.append(line)

    body = "\n".join(filtered_lines)
    body = re.sub(
        r"\n## Suggested internal links.*\Z",
        "",
        body,
        flags=re.MULTILINE | re.DOTALL,
    )
    return body.strip()


def normalize_list_labels(body: str) -> str:
    lines = body.splitlines()
    normalized: list[str] = []

    for index, line in enumerate(lines):
        normalized.append(line)
        next_line = lines[index + 1] if index + 1 < len(lines) else ""
        if re.match(r"^[A-Z][A-Za-z0-9 /&()'-]{1,40}:$", line.strip()) and next_line.startswith("- "):
            normalized.append("")

    return "\n".join(normalized)


def replace_media_blocks(body: str) -> str:
    pattern = re.compile(
        r"!\[([^\]]*)\]\(([^)]+)\)\n\*([^*]+)\*",
        flags=re.MULTILINE,
    )

    def repl(match: re.Match[str]) -> str:
        alt = match.group(1).strip()
        src = media_path_to_raw_url(match.group(2).strip())
        caption = match.group(3).strip()
        return (
            f'\n<figure class="wp-block-image size-large">'
            f'<img src="{src}" alt="{alt}" loading="lazy" decoding="async" />'
            f"<figcaption>{caption}</figcaption>"
            f"</figure>\n"
        )

    return pattern.sub(repl, body)


def markdown_to_html(body: str) -> str:
    converted = markdown.markdown(
        body,
        extensions=["tables", "fenced_code", "sane_lists", "smarty"],
    )
    soup = BeautifulSoup(converted, "html.parser")

    for table in list(soup.find_all("table")):
        figure = soup.new_tag("figure", attrs={"class": "wp-block-table"})
        table["class"] = table.get("class", []) + ["coinlineup-table"]
        table.wrap(figure)

    for blockquote in soup.find_all("blockquote"):
        blockquote["class"] = blockquote.get("class", []) + ["wp-block-quote"]

    for figure in soup.find_all("figure"):
        figure["class"] = figure.get("class", []) + ["coinlineup-figure"]

    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.startswith("http://") or href.startswith("https://"):
            link["target"] = "_blank"
            link["rel"] = "noopener nofollow"

    return str(soup).strip()


def build_article_schema(metadata: ArticleMetadata, featured_image: str | None) -> dict[str, Any]:
    article_url = f"{{{{SITE_URL}}}}{metadata.slug}"
    schema: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": metadata.meta_title,
        "description": metadata.meta_description,
        "dateModified": metadata.last_updated,
        "datePublished": metadata.last_updated,
        "mainEntityOfPage": article_url,
        "url": article_url,
        "keywords": [metadata.primary_keyword],
        "articleSection": metadata.category,
    }
    if featured_image:
        schema["image"] = featured_image
    return schema


def build_itemlist_schema(title: str, ranking_rows: list[dict[str, str]]) -> dict[str, Any]:
    return {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": title,
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": int(row["rank"]),
                "name": row["name"],
                "description": row.get("why_it_made_the_list", ""),
            }
            for row in ranking_rows
        ],
    }


def extract_ranking_rows(html: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    heading = soup.find(["h2", "h3"], string=re.compile(r"The full list", re.I))
    if not heading:
        return []
    table = heading.find_next("table")
    if not table:
        return []

    rows: list[dict[str, str]] = []
    body = table.find("tbody")
    if not body:
        return []

    for tr in body.find_all("tr", recursive=False):
        cells = [cell.get_text(" ", strip=True) for cell in tr.find_all(["td", "th"])]
        if len(cells) < 4:
            continue
        rows.append(
            {
                "rank": cells[0],
                "name": cells[1],
                "best_for": cells[2],
                "why_it_made_the_list": cells[3],
                "watchout": cells[4] if len(cells) > 4 else "",
            }
        )
    return rows


def slug_to_filename(slug: str) -> str:
    return slug.strip("/").split("/")[-1]


def export_article(path: Path) -> dict[str, Any]:
    lines = path.read_text(encoding="utf-8").splitlines()
    metadata, body_start = parse_metadata(lines)
    raw_body = "\n".join(lines[body_start:]).strip()

    internal_section = extract_section(
        r"^## Suggested internal links\n(.*?)(?=^## |\Z)", raw_body
    )
    external_section = extract_section(
        r"^## Suggested external references\n(.*?)(?=^## |\Z)", raw_body
    )
    media_section = extract_section(r"^## Captured media\n(.*?)(?=^## |\Z)", raw_body)
    source_set = extract_section(
        r"^## Source set checked[^\n]*\n(.*?)(?=^## |\Z)",
        raw_body,
    )

    public_body = remove_editorial_blocks(raw_body)
    public_body = normalize_list_labels(public_body)
    public_body = replace_media_blocks(public_body)
    content_html = markdown_to_html(public_body)

    ranking_rows = extract_ranking_rows(content_html)
    internal_links = parse_internal_links(internal_section)
    external_links = parse_external_links(external_section)
    media_assets = parse_media(media_section)
    source_items = parse_source_set(source_set)

    featured_image = next(
        (item["raw_url"] for item in media_assets if item["raw_url"].lower().endswith(".png")),
        media_assets[0]["raw_url"] if media_assets else None,
    )

    schema = [build_article_schema(metadata, featured_image)]
    if ranking_rows:
        schema.append(build_itemlist_schema(metadata.title, ranking_rows))

    slug_name = slug_to_filename(metadata.slug)
    html_path = HTML_DIR / f"{slug_name}.html"
    payload_path = PAYLOADS_DIR / f"{slug_name}.json"

    payload = {
        "title": metadata.title,
        "meta_title": metadata.meta_title,
        "slug": metadata.slug,
        "slug_name": slug_name,
        "meta_description": metadata.meta_description,
        "excerpt": metadata.meta_description,
        "primary_keyword": metadata.primary_keyword,
        "category": metadata.category,
        "schema_label": metadata.schema_label,
        "last_updated": metadata.last_updated,
        "featured_image": featured_image,
        "content_html_path": str(html_path.relative_to(PACKAGE_ROOT)),
        "content_html": content_html,
        "schema_jsonld": schema,
        "internal_link_targets": internal_links,
        "external_references": external_links,
        "captured_media": media_assets,
        "source_set_checked": source_items,
        "ranking_snapshot": ranking_rows,
    }

    html_path.write_text(content_html + "\n", encoding="utf-8")
    payload_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return {
        "title": metadata.title,
        "slug": metadata.slug,
        "html_path": str(html_path.relative_to(PACKAGE_ROOT)),
        "payload_path": str(payload_path.relative_to(PACKAGE_ROOT)),
    }


def main() -> None:
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    PAYLOADS_DIR.mkdir(parents=True, exist_ok=True)

    manifest = [export_article(path) for path in sorted(ARTICLES_DIR.glob("*.md"))]
    (PAYLOADS_DIR / "index.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Exported {len(manifest)} Coinlineup articles to HTML and JSON payloads.")


if __name__ == "__main__":
    main()
