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

---

## Reddit community signal research

Add one "Community signal" paragraph per platform section, placed immediately after the Pros and cons block.
This is deep research: linking real community discussions adds EEAT signal, enables AIO extraction, and builds reader trust beyond official sources.

### When to add a community signal

Add if -- and only if -- a Reddit thread meets ALL of these criteria:
1. Thread is clearly about the platform being reviewed (not just a coincidental keyword match)
2. Thread contains substantive user opinion or real-world experience (not just a question with no answers)
3. Thread is from a relevant subreddit (r/NFT, r/ethdev, r/web3, r/CryptoCurrency, r/NFTGaming, r/ethereum, r/web3gaming, or the platform's own subreddit)
4. Thread is within the last 2 years (use &t=year or &t=all but verify post date)

Do NOT add a community signal if no qualifying thread exists. A missing signal is better than a weak or irrelevant link.

---

### Search method

Use Playwright (headless=True) to search Reddit directly. Do NOT use Google scraping (blocked) or Reddit JSON API (403).

Search pattern per platform:
    url = f'https://www.reddit.com/r/{subreddit}/search/?q={platform_name}&sort=top&t=year'

Subreddits to search (in order):
    r/NFT, r/ethdev, r/web3, r/CryptoCurrency, r/ethereum, r/NFTGaming, r/web3gaming

Then fetch the top 3-4 result URLs, load each thread, read the first 1200 chars of body text, and evaluate manually.

Script: scripts/search_reddit.py (see below)

---

### Sentiment evaluation

After fetching thread content, classify as:

| Sentiment | What it looks like | How to use |
|---|---|---|
| Positive | Users recommending, praising specific feature, sharing success | Mention the positive signal, quote the key claim |
| Mixed | Positive overall but with a specific valid criticism | Lead with positive, surface the criticism honestly |
| Negative | Bug reports, failures, frustration with a real feature | Use as a "worth noting" signal in Cons section |
| Neutral/Irrelevant | Question with no answers, coincidental keyword match | Skip entirely |

---

### Placement and format

Place immediately after the "- Cons: ..." line in the platform section:

    - Cons: <cons text>

    **Community signal:** <one sentence describing what the thread found, with hyperlink on the key claim>. <One sentence on what this means for teams evaluating the platform.>

Format rules:
- Bold the label: **Community signal:**
- Hyperlink the key claim or thread title using descriptive anchor text (not "click here" or "this thread")
- Max 2 sentences total
- Do not quote Reddit usernames
- Do not say "Reddit users say" -- say "r/NFT community", "r/ethdev discussion", "r/CryptoCurrency thread"

Example (positive):
    **Community signal:** Developers on r/web3 consistently name Thirdweb as the [best free option for wallet authentication](URL) -- though the same thread flags that the SDK ships heavy node_modules, worth factoring in if bundle size matters to your stack.

Example (negative):
    **Community signal:** A [recent r/NFT thread reports Rarible profile settings disabled on the new site](URL) -- avatar upload and X account linking both failing. Small bug, but worth verifying before committing to it as a primary platform.

Example (enterprise validation):
    **Community signal:** Crossmint was among the firms [selected by Mastercard as a crypto infrastructure partner](URL) -- a signal the r/CryptoCurrency community noted as meaningful enterprise validation for a payments-first NFT platform.

---

### Reddit search script (Playwright)

Save as scripts/search_reddit.py and run from repo root.

    import asyncio, json, re
    from playwright.async_api import async_playwright

    SEARCHES = {
        'Thirdweb':  [('web3', 'thirdweb'), ('NFT', 'thirdweb'), ('ethdev', 'thirdweb deploy')],
        'Crossmint': [('NFT', 'crossmint'), ('CryptoCurrency', 'crossmint')],
        'Manifold':  [('NFT', 'manifold studio'), ('ethereum', 'manifold nft')],
        'Zora':      [('NFT', 'zora nft'), ('CryptoCurrency', 'zora protocol')],
        'Sequence':  [('NFTGaming', 'sequence xyz'), ('web3gaming', 'sequence wallet')],
        'Alchemy':   [('ethdev', 'alchemy nft'), ('web3', 'alchemy api')],
        'Rarible':   [('NFT', 'rarible'), ('CryptoCurrency', 'rarible review')],
    }

    async def search_subreddit(page, sub, q):
        url = f'https://www.reddit.com/r/{sub}/search/?q={q.replace(" ","+")}&sort=top&t=year'
        await page.goto(url, wait_until='domcontentloaded', timeout=20000)
        await page.wait_for_timeout(2500)
        html = await page.content()
        permas = re.findall(r'href="(/r/[a-zA-Z0-9_]+/comments/[a-zA-Z0-9_]+/[^"?#]+)', html)
        seen, clean = set(), []
        for u in permas:
            base = 'https://www.reddit.com' + u.rstrip('/')
            if base not in seen:
                clean.append(base); seen.add(base)
        return clean[:4]

    async def fetch_text(page, url):
        await page.goto(url, wait_until='domcontentloaded', timeout=20000)
        await page.wait_for_timeout(2500)
        title = await page.title()
        text = await page.evaluate('() => document.body.innerText')
        return title, text[:1500]

    async def main():
        results = {}
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            ctx = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124')
            page = await ctx.new_page()
            for platform, searches in SEARCHES.items():
                all_urls = []
                for sub, q in searches:
                    urls = await search_subreddit(page, sub, q)
                    for u in urls:
                        if u not in all_urls: all_urls.append(u)
                    await asyncio.sleep(1.5)
                results[platform] = all_urls[:5]
                print(f'{platform}: {len(all_urls)} candidate URLs')
                for u in all_urls[:5]: print(f'  {u}')
            with open('reddit_candidates.json', 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            await browser.close()
        print('Saved reddit_candidates.json -- manually review each URL before adding to article')

    asyncio.run(main())

After running: open reddit_candidates.json, visit each URL, read the thread, apply the sentiment evaluation criteria above, then patch the article.

---

### Paragraph structure and word count

All prose paragraphs (outside headings, lists, images, captions) must stay under 45 words.
Split at natural sentence boundaries (. ! ?) if a paragraph exceeds this limit.

Do not split:
- Bold section headers (**text**)
- Italic caption lines (*text*)
- Image tags (![...](...))
- List items (- text)
- Table rows (| text |)
- Headings (# text)

Script for automated splitting: patch_readability.py in repo root.

---

### Hyperlink rules for article body

Link platform names and key terms ONLY in the review body -- NOT in intro paragraphs (the factual project description).

Targets to link:
- Platform official site: link 1-2 times in review body (not in intro, not in headings)
- Key wallet names (MetaMask, Rabby, Zerion): first mention in body
- Key chain names (Ethereum, Polygon, Arbitrum): first mention in body
- Reddit threads: as Community signal paragraphs (see above)
- Internal cross-links (storage, APIs, royalties): wherever they appear in body

Do NOT link:
- Social media accounts (Twitter/X, Discord) -- not stable, not useful for SEO
- Intro paragraphs -- keep them plain text
- Terms that are too generic to link safely (Base, Optimism, Rainbow when used as common words)