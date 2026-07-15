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

## Autonomous article pipeline

When the user says "continue" or "run the pipeline", execute the full loop below for each article in the series, in order, without waiting for user confirmation between steps.

### Series status (as of 2026-07-15)

| # | Article file | imgs | captions | long_para | banned | community_signals | xlinks | Status |
|---|---|---|---|---|---|---|---|---|
| 01 | 01-best-nft-minting-tools-2026.md | 22 | 22 | 0 | 0 | 4 | 9 | DONE |
| 02 | 02-best-nft-analytics-tools-2026.md | 11 | 11 | 10 | 0 | 0 | 4 | needs long_para fix + community signals |
| 03 | 03-best-nft-tracking-tools-2026.md | 12 | 12 | 9 | 0 | 0 | 3 | needs long_para fix + community signals |
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