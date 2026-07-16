---
name: nft-review-hands-on
description: >
  End-to-end workflow for hands-on review of NFT minting platforms. Use when the user wants to
  review one or more NFT minting/infrastructure platforms by actually logging in, capturing
  authenticated screenshots, and updating a markdown article with verified evidence. Covers
  browser automation via CloakBrowser (headless or headed), email OTP login (Thirdweb-style),
  Google OAuth login (Alchemy-style), Gmail API for OTP retrieval, deep dashboard navigation,
  verified/not-verified table updates, article patching, and git push. Also applies when
  updating an existing nftenex/Authority-Building article with new platform captures.
---

# NFT Review Hands-On

Workflow for authenticated, evidence-based review of NFT minting platforms. Captures real screenshots, patches the article's verified table, and pushes to GitHub.

## Repo layout

`
nftenex/articles/01-best-nft-minting-tools-2026.md   # article to update
nftenex/media/                                         # all screenshots land here
`

Repo cloned at: C:\Users\admin\AppData\Local\Temp\authority-building-check

## Platform login map

| Platform | Login method | Headless? | Notes |
|---|---|---|---|
| Thirdweb | Email OTP | Yes | OTP via Gmail API; field input[maxlength="6"]; auto-submits |
| Alchemy | Google OAuth | No (headed) | Google blocks headless; wait for stable URL after OAuth |
| Manifold | Email + reCAPTCHA | Skip | reCAPTCHA blocks automation |
| Crossmint | — | Skip | Geo-blocked from Vietnam |
| Zora / Rarible / Sequence | Wallet-only | Skip | No email path |

## Core credentials

- Email: 	hanalamth@gmail.com / Nam13121999@
- Gmail token: C:\Users\admin\AppData\Local\Temp\gmail-token.json
- Gmail credentials: C:\Users\admin\AppData\Local\Temp\gmail-credentials.json

## Execution order

1. Launch CloakBrowser (headless=True for Thirdweb, headless=False for Alchemy/Google OAuth).
2. Login to platform -- see 
eferences/login-flows.md for per-platform detail.
3. Navigate authenticated routes and take screenshots -- see 
eferences/dashboard-routes.md.
4. Name screenshots as <platform>-<surface>.png and save to 
ftenex/media/.
5. Patch the article -- see 
eferences/article-patch-guide.md.
6. git add only the article + new media files; commit with a descriptive message; push.

## Browser automation

Use scripts/browser_session.py as the base for any new browser session. It handles CloakBrowser launch, screenshot save path, and graceful close.

Read 
eferences/login-flows.md before writing any login automation.

## Article patching

- Use Python string replacement (not PowerShell here-strings -- they break on Windows with embedded newlines).
- Patch one concern at a time, saving after each step.
- Read 
eferences/article-patch-guide.md for the exact table format and section anchors.

## Git

`ash
cd C:\Users\admin\AppData\Local\Temp\authority-building-check
git add nftenex/articles/01-best-nft-minting-tools-2026.md nftenex/media/<new-files>
git commit -m "nftenex: <platform> authenticated captures <date>"
git push origin main
`

Only stage article + new media. Do not stage scratch/intermediate screenshots.

## Skip rules

- If a platform requires reCAPTCHA and omocaptcha REST API is unavailable: skip, note in article.
- If geo-blocked at CDN: skip, note in article.
- If wallet-only login with no email fallback: capture wallet modal only, note as "Not verified (wallet-only)".
- Go deeper on platforms where login succeeded rather than widening to more platforms.

---

## Screenshot validation (run before every git add)

After capturing any batch of screenshots, run this check BEFORE staging to git.
A screenshot showing a 404, Cloudflare challenge, or blank page is worse than no screenshot.

### Detection criteria

| Signal | Threshold | Action |
|---|---|---|
| File size | < 30KB | Suspect -- inspect |
| Center brightness | > 230 AND size < 40KB | Almost certainly blank/error |
| Page title at capture | "Just a moment", "Attention Required", "Deployment Paused", "404" | Re-capture with fallback |

### Inline validation script (run after every capture loop)

```python
from PIL import Image
import os

MEDIA = r"C:\Users\admin\AppData\Local\Temp\authority-building-check\nftenex\media"
new_files = ["replace_with_actual_filenames.png"]

for fname in new_files:
    path = os.path.join(MEDIA, fname)
    im = Image.open(path).convert("RGB")
    w, h = im.size
    kb = os.path.getsize(path) // 1024
    pts = [(w//4,h//4),(w//2,h//2),(3*w//4,h//2)]
    avg_b = sum(sum(p)/3 for p in [im.getpixel(pt) for pt in pts]) / 3
    flag = " <<< SUSPECT" if (kb < 40 or avg_b > 230) else ""
    print(f"  {kb:4d}KB  avg_brightness={avg_b:.0f}  {fname}{flag}")
```

Any SUSPECT file must be re-captured or swapped before commit.

### Fallback URL list

| Original site | Issue | Fallback | Update in article |
|---|---|---|---|
| nftgo.io | Cloudflare (headless blocked) | https://icy.tools/ | alt + caption only |
| traitsniper.com | Deployment paused (down) | https://www.nftnerds.ai/ | alt + caption only |
| bitscrunch.com | Cloudflare (headless blocked) | https://medium.com/bitscrunch | alt + caption only |
| app.zerion.io/explore/nfts | Cloudflare gated deep route | https://zerion.io/ | alt + caption only |
| coingecko.com | Cloudflare intermittent | https://coinmarketcap.com/ | alt + caption only |
| dune.com | Cloudflare on search pages | Use specific public dashboard URL | confirm public access |

### Re-capture steps

1. Run validation script -- identify all SUSPECT files
2. Pick fallback from table (or find equivalent accessible page)
3. Re-capture: `headless=False`, `wait=8s`, remove webdriver flag
4. Re-run validation -- confirm new file > 50KB and avg_brightness < 200
5. Update **alt text and caption** in article to match what is actually shown
6. Prose body tool name can stay -- only image context must be honest about what was captured



---

## Autonomous article pipeline

When the user says "continue" or "run the pipeline", execute the full loop below for each article in the series, in order, without waiting for user confirmation between steps.

### Series status (as of 2026-07-15)

| # | Article file | imgs | captions | long_para | banned | community_signals | xlinks | Status |
|---|---|---|---|---|---|---|---|---|
| 01 | 01-best-nft-minting-tools-2026.md | 22 | 22 | 0 | 0 | 4 | 9 | DONE |
| 02 | 02-best-nft-analytics-tools-2026.md | 11 | 11 | 0 | 0 | 1 | 4 | DONE |
| 03 | 03-best-nft-tracking-tools-2026.md | 12 | 12 | 0 | 0 | 0 | 3 | DONE (no qualifying community signals) |
| 04 | 04-best-nft-marketplaces-for-creator-royalties-2026.md | 7 | 7 | 9 | 0 | 0 | 3 | needs long_para fix + community signals |
| 05 | 05-best-nft-storage-tools-2026.md | 10 | 10 | 6 | 0 | 0 | 3 | needs long_para fix + community signals |
| 06 | 06-best-nft-communities-2026.md | 8 | 8 | 3 | 0 | 0 | 2 | needs long_para fix + community signals |
| 07 | 07-best-nft-apis-2026.md | 11 | 11 | 6 | 0 | 0 | 4 | needs long_para fix + community signals |
| 08 | 08-best-nft-marketplaces-for-artists-2026.md | 8 | 8 | 6 | 0 | 0 | 3 | needs long_para fix + community signals |
| 09 | 09-best-nft-marketplaces-2026.md | 7 | 7 | 6 | 0 | 0 | 3 | needs long_para fix + community signals |
| 10 | 10-best-nft-games-2026.md | 9 | 9 | 3 | 0 | 0 | 3 | needs long_para fix + community signals |

Update this table after completing each article -- replace the Status cell with "DONE" and update counts.

---

### Autonomous execution loop (per article)

For each article that is NOT "DONE", execute these steps in sequence:

#### Step 1 -- git pull
    cd C:\Users\admin\AppData\Local\Temp\authority-building-check
    git pull --no-edit origin main

#### Step 2 -- audit gaps
Run the audit script to get current gap counts:

    python C:\Users\admin\AppData\Local\Temp\audit_articles.py

Or inline scan for just the target article to confirm which steps are needed.

#### Step 3 -- fix long paragraphs (if long_para > 0)
Read the article. For each prose paragraph > 45 words, split at the nearest sentence boundary.
Rules:
- Skip: headings (#), list items (-), captions (*italic*), image lines (![), tables (|), HTML blocks (<)
- Split into exactly 2 paragraphs separated by a blank line
- Do NOT alter the meaning or word choice -- only add a line break
- Use Python string.replace() -- assert old text exists before replacing
- Write with encoding='utf-8'

After fixing: re-scan to confirm long_para = 0.

#### Step 4 -- Reddit community signals (if community_signals = 0)
For each platform section in the article, run the Reddit search from references/article-patch-guide.md.
Subreddits: r/NFT, r/ethdev, r/web3, r/CryptoCurrency, r/ethereum, r/NFTGaming, r/web3gaming
Evaluate each result per the qualifying criteria. Add signal only if thread is:
  1. Clearly about THIS platform (not a keyword coincidence)
  2. Has real user opinion/experience (not just a question)
  3. Within 2 years
  4. From a relevant subreddit

If no qualifying thread: leave blank. Missing > weak.

Format:
    **Community signal:** [descriptive anchor text](URL). [One sentence on what this means for teams.]

Place immediately after the Cons line for each platform.

#### Step 5 -- word filter scan
Run the banned word scan from references/article-patch-guide.md.
Fix any hits. Confirm 0 hits before continuing.

#### Step 6 -- verify captions (if captions < imgs)
Check that every image block has an italic caption line directly below it.
Missing captions: add using the SEO+AIO formula from references/article-patch-guide.md.
Alt text: literal image description. Caption: platform + surface + keyword + fact + judgment.

#### Step 7 -- internal cross-links (if xlinks < 3)
Scan body for trigger terms: storage, IPFS, Arweave, pinning, royalt, marketplace, analytics, floor price, tracking.
For each hit, check if a matching article exists in nftenex/articles/. If yes, add cross-link (max 3 total per article).
Use relative paths: ../XX-slug.md -- NOT absolute URLs.

#### Step 8 -- final verification scan
Run:
    imgs count, captions count, long_para count, banned count, community count, xlinks count
All must pass:
    - long_para = 0
    - banned = 0
    - captions == imgs
    - community_signals >= 1 (or documented as "no qualifying thread found")

#### Step 9 -- git commit and push
    git add nftenex/articles/<filename>.md
    git commit -m "nftenex: editorial pass bài XX <YYYY-MM-DD>"
    git pull --no-edit origin main
    git push origin main

#### Step 10 -- update series status table
After pushing, update the Status column in the series status table above (in this SKILL.md).
Also update the local copy at:
    C:\Users\admin\AppData\Local\Temp\authority-building-check\nftenex\docs\article-patch-guide.md

Then move to the next article (increment XX) and repeat from Step 1.

---

### Completion criteria

The full series is done when ALL 10 articles have Status = "DONE" in the series status table:
- long_para = 0
- banned = 0
- captions == imgs
- community_signals documented per platform (present or "no qualifying thread")
- xlinks >= 2 (3 preferred where opportunities exist)

---

### Notes on autonomous execution

- Never rewrite whole article sections -- patch surgically with string.replace(), asserting old text first.
- Never ask for confirmation between articles -- keep moving until all 10 are done or a genuine blocker appears.
- A genuine blocker is: file not found, git conflict that cannot be auto-resolved, Reddit search returning 0 URLs for every platform in an article.
- After a genuine blocker: note it, mark the article "BLOCKED (reason)", skip to next article, continue.
- Update the series status table in this SKILL.md and in the repo copy after each article.
- Always git pull --no-edit before any push (multiple Codex sessions may run concurrently).

---


---

## AiCryptoCore series status

Repo: Authority-Building/aicrypto/articles/
Local clone: C:\Users\admin\AppData\Local\Temp\authority-building-check

| # | Article file | Status |
|---|---|---|
| 01 | 01-best-ai-crypto-projects-2026.md | **DONE** (commit 70284aa) |
| 02 | 02-best-ai-agent-crypto-coins-2026.md | **DONE** (commit 7d2e1f5) |
| 03 | 03-ai-infrastructure-crypto-coins-2026.md | **DONE** (commit 41655f8) |
| 04 | 04-best-decentralized-ai-crypto-projects-2026.md | not started |
| 05 | 05-best-ai-trading-crypto-coins-2026.md | not started |
| 06 | 06-best-defai-projects-2026.md | not started |
| 07 | 07-best-ai-crypto-signals-2026.md | not started |
| 08 | 08-best-onchain-ai-agents-2026.md | not started |
| 09 | 09-top-virtuals-protocol-ecosystem-coins-2026.md | not started |
| 10 | 10-best-ai-nft-projects-2026.md | not started |

Update Status to **DONE (commit <hash>)** after each article is pushed.

---

## AiCryptoCore article pipeline (autonomous loop)

When the user says "continue" or names a bài number for aicrypto, execute the full loop below.

### Per-article execution (aicrypto)

#### Step 1 -- git pull
    cd C:\Users\admin\AppData\Local\Temp\authority-building-check
    git pull --no-edit origin main

#### Step 2 -- read existing article
Read the target file in aicrypto/articles/. Identify what is a skeleton vs what is already prose.

#### Step 3 -- screenshots (10 per article)
- One screenshot per project section -- navigate to the most informative public surface
- Save to aicrypto/media/<project>-<surface>-YYYY-MM-DD.png
- Run screenshot validation script immediately after capture batch
- Apply fallback URLs for any SUSPECT files

#### Step 4 -- Reddit research (per project)
Subreddits: r/CryptoCurrency, r/bittensor_, r/Chainlink, r/RenderNetwork, r/cosmosnetwork,
            r/VeniceAI, r/Grass_io, r/OriginTrail, r/filecoin, r/AixbtByVirtuals, plus project-specific subs
Qualifying criteria (same as NFTEnex):
  1. Clearly about this project (not keyword coincidence)
  2. Real user opinion or experience, not just a question
  3. Within 2 years
  4. From a relevant subreddit
If no qualifying thread: note "no qualifying signal" -- do not force a weak one.

#### Step 5 -- write / rewrite in AiCryptoCore voice
Apply all rules from the AiCryptoCore writing rules section below:
- Prose flow, no rigid label blocks
- Max 70 words per paragraph
- Community signal embedded where it adds narrative weight
- Failure scenario woven into prose (not a labeled section)
- "Real vs narrative" judgment in every project section
- Banned word scan before finalizing

#### Step 6 -- audit
    imgs == 10, captions == 10, all paras <= 70w, banned == 0, community signals documented

#### Step 7 -- copy to repo + git push
    shutil.copy2(temp_file, repo/aicrypto/articles/NN-slug.md)
    git add aicrypto/articles/NN-slug.md aicrypto/media/<new-files>
    git commit -m "aicrypto: bai NN complete prose rewrite -- 10 imgs, N community signals YYYY-MM-DD"
    git pull --no-edit origin main
    git push origin main

#### Step 8 -- update series status table above
Mark the article DONE with commit hash.

## AiCryptoCore writing rules (apply when writing or rewriting aicrypto articles)

### Voice
Technical but not academic. Write like a developer who also reads venture memos.
Skeptical of pure narrative plays. Genuinely interested in real infrastructure work.
The contrast "this is real infrastructure / this is not" is the site's signature move.

### Prose style -- NOT template style
Do NOT use rigid per-project label blocks (Stack position:, What it actually does:, etc.).
Write in flowing prose. The analysis arrives through sentences, not through form-filling.

Each project section should:
1. Open with the most surprising or structurally important thing about the project -- not the most obvious
2. Weave token utility and ecosystem evidence into the narrative -- not in separate labeled blocks
3. Surface the tension (risk / real vs narrative) early, not at the end as a disclaimer
4. End with a verdict that follows naturally from what was written -- not a boilerplate close
5. Blend first-person observations into technical analysis -- not in a separate "experience" block

### Para length for AiCryptoCore
Analytical prose paragraphs: max 70 words (not 45w -- that rule is for NFTEnex first-person experience style).
Flag and split any paragraph exceeding 70 words.
Short sentences for verdicts, skepticism, and key contrasts.

### Structure per project (prose, not labels)
- Opening: the most interesting/surprising thing -- one strong sentence
- Mechanism: how it actually works at the stack level -- 2-3 sentences
- Token utility: woven into the mechanism description -- not a separate block
- Evidence: what is verifiably live vs what is still documentation-only
- Tension: risk or "real vs narrative" -- introduced early, not saved for last
- Community signal: placed where it adds to the argument, not appended
- Verdict: one short paragraph, follows naturally

### Community signal placement
Place the community signal where it adds the most narrative weight -- usually:
- After the tension/risk observation (it reinforces or complicates the point)
- Not at the end as an afterthought
- Not at the beginning before the mechanism is established
Format: **Community signal:** [descriptive anchor](URL). One sentence on implication.

### "Real vs narrative" per project (required)
Every project must be classified somewhere in its section. Use direct language:
- "The mechanism is real." / "This is not yet proven at scale."
- "X did not rebrand as an AI project -- the use case accrues to it."
- "Treat it as a coalition with live parts, not a single production system."
Do NOT use the header "Real vs narrative:" -- embed the judgment in the prose.

### Failure scenario (required, per project)
Every project must have a failure scenario. Write it as a conditional:
"For X to fail at a fundamental level, [condition 1] and [condition 2] would both have to be true."
Or: "The version of this that struggles is one where..."
Do NOT use the header "What would have to be true for this to fail:" -- embed it.

### Word filter (same as network-wide)
Banned: headless, programmatic, automation (in process context), automated, leveraging, utilize,
seamlessly, cutting-edge, streamline, robust, delve into, it is worth noting, in conclusion, in summary.
Exception: product names that contain banned words (e.g. "Chainlink Automation" as a proper noun)
-- replace with descriptive alternative (e.g. "Chainlink Scheduled Triggers").


