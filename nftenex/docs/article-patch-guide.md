# Article Patch Guide

Article path:
  C:\Users\admin\AppData\Local\Temp\authority-building-check\nftenex\articles\01-best-nft-minting-tools-2026.md

Always use Python string replacement for patching. PowerShell here-strings break on Windows with embedded newlines in multiline replacements.

Pattern:
    with open(file, "r", encoding="utf-8") as f: content = f.read()
    content = content.replace(old, new)
    with open(file, "w", encoding="utf-8") as f: f.write(content)

For non-ASCII characters (stars, unicode) NEVER pass them through PowerShell here-strings -- they corrupt silently.
Write the patch script to a .py file using [System.IO.File]::WriteAllText(..., [System.Text.Encoding]::UTF8), then call python on it.

---

## Verified table location

The table sits in the section "## What this review verified and what it did not"

Row format:
    | <claim text> | Verified |
    | <claim text> | Not verified |
    | <claim text> | Verified (<platform> -- <detail>) |

When adding new verified rows for a platform, insert them ABOVE the "Live contract deployment tested" row (that row stays Not verified unless a real deploy is done).

---

## Adding screenshots to a platform section

Find the anchor -- the last existing screenshot caption in the platform section:
    *<last caption text>*

Append the new block immediately after that anchor paragraph. Format:

    **<Section heading>**

    <Experience paragraph -- see "Experience writing standard" below>

    ![<alt text>](../media/<filename>.png)

    *<Caption -- see "Caption standard (SEO + AIO)" below>*

Do NOT use the old plain-factual format. Every screenshot block must include an experience paragraph above the image and an SEO+AIO caption below it.

---

## Caption standard (SEO + AIO)

Every image caption (the italic line directly below the image) must follow this structure:

    *[Platform] [feature/surface type] [product category keyword], [Month YYYY] -- [extractable fact or confirmed detail]. [Personal judgment sentence -- optional but preferred for authenticated surfaces.]*

### Rules

1. Lead with the entity: platform name + surface + keyword. Never start with a verb or vague opener like "Screenshot of..." or "Captured during...".
   - Good: "Thirdweb contract deploy interface, authenticated dashboard, July 2026 --"
   - Bad: "Thirdweb contract deployment interface, captured July 2026 from inside the authenticated dashboard."

2. Include a product-category keyword naturally in the first clause. Use one of: "NFT minting platform", "NFT minting tool", "NFT infrastructure", "NFT API dashboard", "smart wallet platform", "creator publishing platform", "blockchain developer platform".

3. The fact clause (after the --) must be specific and extractable. It should directly answer a question someone might search for.
   - Good: "500+ supported networks confirmed directly in the live product, not just in public documentation."
   - Good: "No wallet required -- email and Google OAuth sign-in only, confirming a SaaS-style developer onboarding model."
   - Bad: "Confirms what the platform exposes post-authentication."

4. End with a personal judgment sentence where it adds signal (especially for authenticated surfaces). One sentence max.
   - Good: "The most complete NFT API surface of any platform reviewed."
   - Good: "Broader chain coverage than the public homepage communicates."

5. Length: 2 sentences maximum. Keep the first sentence under 30 words.

6. Do not repeat the alt text. Caption adds context; alt text describes the image literally.

### Caption formula by surface type

| Surface | Formula |
|---|---|
| Homepage | [Platform] NFT minting platform homepage, [Month YYYY] -- [what the positioning signals about its intended audience]. [Personal verdict.] |
| Login / wallet modal | [Platform] [login/wallet modal], [Month YYYY] -- [what options are shown, how many clicks to reach it]. [Friction or speed judgment.] |
| Authenticated dashboard | [Platform] [surface name], authenticated [dashboard/], [Month YYYY] -- [what was confirmed directly in the live product]. [What this means for teams evaluating it.] |
| API / developer surface | [Platform] [surface name], authenticated, [Month YYYY] -- [specific endpoints or capabilities confirmed]. [Who this is built for.] |
| Signup / account creation | [Platform] [signup/account form], [Month YYYY] -- [fields present, auth methods available, wallet required or not]. [Comparative judgment.] |

---

## Experience writing standard

Every screenshot block must include an experience paragraph placed ABOVE the image. This is not a caption -- it is a first-person prose paragraph describing what it felt like to navigate that surface.

### Structure

    **<Section heading>**

    <Experience paragraph>

    ![alt text](../media/filename.png)

    *<SEO+AIO caption>*

### Rules for the experience paragraph

1. Write in first person ("I", "we"). Use "I" for singular personal reactions, "we" for actions taken during the review session.

2. Lead with a sensory or emotional reaction to the surface -- what it felt like to land on it, not a neutral description of what you saw.
   - Good: "The login page was the first moment I felt Thirdweb really understand its users."
   - Good: "Landing inside the Alchemy dashboard post-login was calming in a way I did not expect."
   - Bad: "After logging in, the Alchemy dashboard showed an apps overview."

3. Describe the experience along at least two of these dimensions:
   - Speed / friction: how fast or slow it was to reach the surface
   - Expectation vs reality: what surprised you vs what you expected
   - Audience fit: who this product is clearly built for, based on what you saw
   - Contrast with other platforms: only when the contrast is sharp and useful

4. End the paragraph with a direct judgment. One sentence. State clearly what the experience means for a team evaluating the platform.
   - Good: "That restraint felt earned."
   - Good: "For a platform serving teams with mixed wallet setups, this breadth is not a flex; it is just the right default."
   - Bad: "Overall, it was a good experience."

5. Length: 3-5 sentences. No lists inside the experience paragraph. Prose only.

6. Tone: calm, direct, slightly opinionated. Match the voice of a senior NFT operator who has seen many platforms and is not easily impressed. Avoid superlatives ("amazing", "incredible", "best ever") but do not be artificially neutral.

7. For authenticated surfaces (post-login), the experience paragraph is mandatory. For public-surface-only captures (homepage, wallet modal), it is strongly preferred but may be shorter (2-3 sentences).

### Experience paragraph by surface type

| Surface | What to focus on |
|---|---|
| Homepage | First impression of positioning, who it feels built for, one thing that stands out |
| Login page / modal | How fast to reach, what options appeared, what the login design signals about the product's audience |
| Team / project dashboard (post-login) | What loaded first, presence or absence of onboarding gates, how the session design makes you feel |
| Contract / deploy interface | Decision points the interface forces, who it rewards vs who it slows down |
| API / developer surface | Whether the capability matched the docs, what the dashboard reveals that the public homepage does not |
| Wallet connect modal | Number of clicks, options shown, what wallet-only gating means for non-crypto-native users |

---

## Sections to update after adding new authenticated captures

1. Verified table -- add rows above "Live contract deployment tested"
2. Platform section -- append screenshot block (experience paragraph + image + SEO caption) after last existing media anchor
3. "Why you can trust this guide" -- mention new authenticated login
4. "Methodology" -- add sentence: "Authenticated <Platform> dashboard surfaces were navigated and captured directly on <date>."
5. "Limitations" -- update to reflect which platforms were authenticated vs not
6. "What we checked ourselves" -- update last paragraph
7. "Review type" in footer metadata -- update if still says "Public-surface and login-layer only"

---

## Git commit format

    git add nftenex/articles/01-best-nft-minting-tools-2026.md nftenex/media/<new-files>
    git commit -m "nftenex: <platform> authenticated captures <YYYY-MM-DD>"
    git push origin main

Stage only: article file + new media files. Do not stage intermediate/scratch screenshots.

---

## WordPress publishing

### Overview

Publishing flow for one article from GitHub repo to WordPress via REST API:

1. Read markdown article from local repo clone
2. Parse all image blocks: extract alt text, src path, and caption
3. Upload each image to WP media library -- set alt_text and caption at upload time
4. Replace ../media/filename.png in content with the returned WP source_url
5. Convert image+caption Markdown blocks to Gutenberg figure HTML
6. Convert remaining Markdown to HTML (python-markdown library)
7. POST article to /wp-json/wp/v2/posts

Script: scripts/publish_to_wp.py

---

### WordPress credentials

Store per-site in a dict or config. Never hardcode in the article.
Required fields per site:

    WP_URL      = "https://yoursite.com"
    WP_USER     = "admin_username"
    WP_APP_PASS = "xxxx xxxx xxxx xxxx xxxx xxxx"   # Application Password from WP Admin > Users > Profile

Application Password: WP Admin -> Users -> Profile -> scroll to Application Passwords -> Generate.
Use Basic auth: base64(WP_USER + ":" + WP_APP_PASS)

---

### Media upload -- alt text and caption rules

POST /wp-json/wp/v2/media with:

    Headers:
        Authorization: Basic <base64>
        Content-Disposition: attachment; filename="thirdweb-home.png"
        Content-Type: image/png

    After upload, PATCH /wp-json/wp/v2/media/<id> with JSON:
        {
            "alt_text": "<alt text from Markdown ![alt]()>",
            "caption":  "<caption text from italic *...* line below the image>"
        }

Key rules:
- alt_text  = literal image description (what is IN the image) -- from the Markdown alt attribute
- caption   = SEO+AIO sentence with keyword + extractable fact + judgment -- from the *italic* line
- They must be DIFFERENT. Duplicate alt/caption gets flagged by Yoast/RankMath and weakens AIO extraction.
- If caption is missing in Markdown, use alt_text as fallback for caption but truncate to first clause only.

---

### Image block conversion: Markdown -> Gutenberg HTML

Pattern to find in Markdown content (after converting ../media/ to WP URLs):

    ![alt text](WP_URL/filename.png)

    *caption text*

Convert to:

    <!-- wp:image {"id":MEDIA_ID} -->
    <figure class="wp-block-image">
      <img src="WP_URL/filename.png" alt="alt text" class="wp-image-MEDIA_ID"/>
      <figcaption class="wp-element-caption">caption text</figcaption>
    </figure>
    <!-- /wp:image -->

Do this replacement BEFORE passing content to python-markdown, otherwise markdown() will wrap the figure in a <p> tag.

---

### Post fields for /wp-json/wp/v2/posts

    {
        "title":          "<from article H1>",
        "slug":           "<from frontmatter slug field, strip leading slash>",
        "content":        "<full HTML after image conversion + markdown()>",
        "excerpt":        "<meta_description from frontmatter>",
        "status":         "draft",          # always draft first; manually publish after review
        "featured_media": <id of first image uploaded>,
        "meta": {
            "rank_math_focus_kw":       "<primary_keyword from frontmatter>",
            "rank_math_description":    "<meta_description from frontmatter>"
        }
    }

Use status "draft" by default. Only set "publish" when explicitly instructed.
featured_media = media ID of the first image in the article (usually the platform homepage image).

---

### Frontmatter parsing

The article has YAML frontmatter between --- delimiters. Parse with PyYAML:

    import yaml, re
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    fm = yaml.safe_load(match.group(1))
    body = content[match.end():]  # everything after closing ---

Fields to use:
    fm["title"]               -> post title
    fm["slug"]                -> post slug (strip leading /)
    fm["meta_description"]    -> excerpt + rank_math_description
    fm["primary_keyword"]     -> rank_math_focus_kw

---

### H1 stripping

The markdown body starts with # Title. WordPress stores title separately.
Strip the H1 line from body before converting to HTML to avoid duplicate title.

    body = re.sub(r'^#[^\n]+\n', '', body, count=1)

---

### Full conversion order

1. Parse frontmatter -> extract title, slug, meta_description, primary_keyword
2. Strip H1 from body
3. Upload all images (collect filename -> {id, url} map)
4. Replace all ../media/filename.png in body with WP source_url
5. Find all image+caption blocks, replace with Gutenberg figure HTML (store as placeholders)
6. Run markdown(body) to convert remaining Markdown to HTML
7. Restore figure block placeholders into final HTML
8. POST to /wp-json/wp/v2/posts

---

### Dependencies

    pip install requests markdown PyYAML

No other dependencies needed. Do not use pandoc or wordpress-xmlrpc.

---

### Error handling

- If image upload fails: skip that image, log filename, continue. Do not abort full publish.
- If post creation returns 4xx: print full response body for diagnosis.
- Always print final post URL and ID after successful creation.
- After publishing, print: post_id, post_url, status, featured_media_id.