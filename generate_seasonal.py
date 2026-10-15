"""
Authority-Building Distribution Script
Generates Halloween + Christmas seasonal articles for 13 sites based on Kanalcoin master articles.
Run from: C:/Users/admin/Authority-Building/
"""
import os, re

BASE = r"C:\Users\admin\Authority-Building"

# Master article definitions: (filename, slug_base, article_type)
MASTERS = [
    ("14-best-crypto-casinos-halloween-2026.md",      "best-crypto-casinos-halloween-2026",       "halloween_casino"),
    ("15-best-halloween-crypto-casino-bonuses-2026.md","best-halloween-crypto-casino-bonuses-2026","halloween_bonus"),
    ("16-best-halloween-crypto-slots-2026.md",        "best-halloween-crypto-slots-2026",         "halloween_slots"),
    ("17-best-crypto-swap-aggregators-christmas-2026.md","best-crypto-swap-aggregators-christmas-2026","xmas_swap"),
    ("18-best-no-kyc-crypto-swaps-christmas-casino-deposits-2026.md","best-no-kyc-crypto-swaps-christmas-casino-deposits-2026","xmas_nokyc"),
    ("19-best-last-minute-crypto-gift-swap-christmas-2026.md","best-last-minute-crypto-gift-swap-christmas-2026","xmas_gift"),
]

# Site configurations: name -> {next_num, author, slug_cat_gambling, slug_cat_swap, category_gambling, category_swap, internal_casino, internal_swap, frontmatter_style}
# frontmatter_style: 'yaml' (standard YAML front matter), 'markdown' (no front matter, just H1), 'inline' (markdown with inline meta comment)
SITES = {
    "coinwy": {
        "next_num": 14,
        "author": "Coinwy Editorial Team",
        "slug_gambling": "/gambling/",
        "slug_swap": "/swap/",
        "category_gambling": "gambling/halloween",
        "category_swap": "swap/defi",
        "internal_casino": ["/gambling/best-no-kyc-crypto-casinos-2026", "/crypto/best-crypto-exchanges-2026"],
        "internal_swap": ["/swap/swapspace-review-2026", "/crypto/best-crypto-exchanges-2026"],
        "style": "yaml",
        "site_name": "Coinwy",
    },
    "DeFiLiban": {
        "next_num": None,  # uses descriptive names
        "author": "DeFiLiban Research Team",
        "slug_gambling": "/gambling/",
        "slug_swap": "/defi/",
        "category_gambling": "gambling",
        "category_swap": "defi/swaps",
        "internal_casino": [],
        "internal_swap": [],
        "style": "markdown",
        "site_name": "DeFiLiban",
    },
    "MarketBit": {
        "next_num": 11,
        "author": "MarketBit Research Team",
        "slug_gambling": "/markets/",
        "slug_swap": "/markets/",
        "category_gambling": "markets/gambling",
        "category_swap": "markets/defi",
        "internal_casino": [],
        "internal_swap": [],
        "style": "markdown",
        "site_name": "MarketBit",
    },
    "CCpress": {
        "next_num": 28,
        "author": "CCpress Editorial Team",
        "slug_gambling": "/",
        "slug_swap": "/",
        "category_gambling": "crypto-casinos",
        "category_swap": "crypto-defi",
        "internal_casino": ["/best-crypto-casinos-october-2026", "/is-crypto-casino-safe-red-flags-2026"],
        "internal_swap": ["/top-crypto-exchange-aggregators-2026", "/best-crypto-exchanges-for-beginners-2026"],
        "style": "yaml",
        "site_name": "CCpress",
    },
    "Coincu": {
        "next_num": 20,
        "author": "Coincu Editorial Team",
        "slug_gambling": "/gambling/",
        "slug_swap": "/defi/",
        "category_gambling": "gambling",
        "category_swap": "defi",
        "internal_casino": [],
        "internal_swap": [],
        "style": "yaml",
        "site_name": "Coincu",
    },
    "TrustsCrypto": {
        "next_num": 21,
        "author": "TrustsCrypto Editorial Team",
        "slug_gambling": "best-crypto-casinos-halloween-2026",
        "slug_swap": "best-crypto-swap-aggregators-christmas-2026",
        "category_gambling": "/gambling/",
        "category_swap": "/defi/",
        "internal_casino": ["/top-crypto-exchanges-2026", "/top-10-crypto-by-market-cap-2026"],
        "internal_swap": ["/top-crypto-exchanges-2026"],
        "style": "trusts",
        "site_name": "TrustsCrypto",
    },
    "Coinlive": {
        "next_num": 20,
        "author": "Coinlive Editorial Team",
        "slug_gambling": "/markets/",
        "slug_swap": "/markets/",
        "category_gambling": "Markets > Gambling",
        "category_swap": "Markets > DeFi",
        "internal_casino": ["/markets/best-telegram-casino-apps-2026", "/markets/best-crypto-sports-betting-october-2026"],
        "internal_swap": [],
        "style": "yaml_coinlive",
        "site_name": "Coinlive",
    },
    "nftenex": {
        "next_num": 11,
        "author": "nftenex Editorial Team",
        "slug_gambling": "/gambling/",
        "slug_swap": "/defi/",
        "category_gambling": "gambling/halloween",
        "category_swap": "defi/swaps",
        "internal_casino": ["/gaming-nft/games/best-nft-games-2026"],
        "internal_swap": [],
        "style": "yaml",
        "site_name": "nftenex",
    },
    "topkentopnews": {
        "next_num": 15,
        "author": "topkentopnews Editorial Team",
        "slug_gambling": "/insights/gambling/",
        "slug_swap": "/insights/defi/",
        "category_gambling": "/insights/gambling",
        "category_swap": "/insights/defi",
        "internal_casino": ["/insights/gambling/gamblefi-presales-bull-run-2026"],
        "internal_swap": [],
        "style": "topken",
        "site_name": "topkentopnews",
    },
    "BitcoinMaximalist": {
        "next_num": 13,
        "author": "BitcoinMaximalist Editorial Team",
        "slug_gambling": "/bitcoin-guides/gambling/",
        "slug_swap": "/bitcoin-guides/exchanges/",
        "category_gambling": "/bitcoin-guides/gambling/",
        "category_swap": "/bitcoin-guides/exchanges/",
        "internal_casino": ["/bitcoin-guides/exchanges/best-crypto-exchange-aggregators-2026/"],
        "internal_swap": ["/bitcoin-guides/exchanges/best-crypto-exchange-aggregators-2026/"],
        "style": "yaml",
        "site_name": "BitcoinMaximalist",
    },
    "aicrypto": {
        "next_num": 11,
        "author": "aicrypto Editorial Team",
        "slug_gambling": "/gambling/",
        "slug_swap": "/defi/",
        "category_gambling": "/gambling/halloween/",
        "category_swap": "/defi/swaps/",
        "internal_casino": [],
        "internal_swap": ["/ai-agents/economy/top-virtuals-protocol-ecosystem-coins-2026/"],
        "style": "inline",
        "site_name": "aicrypto",
    },
    "Coinlineup": {
        "next_num": 11,
        "author": "Coinlineup Editorial Team",
        "slug_gambling": "/guides/gambling/",
        "slug_swap": "/guides/defi/",
        "category_gambling": "Guides > Gambling",
        "category_swap": "Guides > DeFi",
        "internal_casino": ["/guides/crypto-trading/best-crypto-exchanges-for-beginners-2026/"],
        "internal_swap": ["/guides/crypto-trading/best-crypto-exchanges-for-beginners-2026/"],
        "style": "yaml",
        "site_name": "Coinlineup",
    },
    "CryptoDailyAlert": {
        "next_num": 16,
        "author": "CryptoDailyAlert Editorial Team",
        "slug_gambling": "/briefs/gambling/",
        "slug_swap": "/briefs/defi/",
        "category_gambling": "Briefs > Gambling",
        "category_swap": "Briefs > DeFi",
        "internal_casino": [],
        "internal_swap": ["/briefs/regulation/best-crypto-regulatory-news-sources"],
        "style": "yaml",
        "site_name": "CryptoDailyAlert",
    },
}

ARTICLE_SLUGS = {
    "halloween_casino":  ("best-crypto-casinos-halloween-2026",       "gambling"),
    "halloween_bonus":   ("best-halloween-crypto-casino-bonuses-2026","gambling"),
    "halloween_slots":   ("best-halloween-crypto-slots-2026",         "gambling"),
    "xmas_swap":         ("best-crypto-swap-aggregators-christmas-2026","swap"),
    "xmas_nokyc":        ("best-no-kyc-crypto-swaps-christmas-casino-deposits-2026","swap"),
    "xmas_gift":         ("best-last-minute-crypto-gift-swap-christmas-2026","swap"),
}

def read_master(filename):
    path = os.path.join(BASE, "Kanalcoin", "articles", filename)
    with open(path, encoding="utf-8") as f:
        return f.read()

def strip_frontmatter(content):
    """Remove YAML front matter block, return body only."""
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            return content[end+4:].lstrip("\n")
    return content

def make_yaml_frontmatter(site_cfg, article_type, slug_val, title, meta_title, meta_description, primary_kw, category, internal_links, style):
    """Generate YAML front matter for a given site style."""
    il_str = "\n".join(f'  - "{l}"' for l in internal_links) if internal_links else '  []'
    
    if style == "trusts":
        return f"""---
title: "{title}"
slug: {slug_val}
site: {site_cfg["site_name"]}
category: {category}
author: {site_cfg["author"]}
published: 2026-10-15
last_modified: 2026-10-15
schema: Article, ItemList, FAQPage
disclaimer: true
---"""
    
    elif style == "topken":
        return f"""---
title: "{title}"
slug: {slug_val}
category: {category}
primary_keyword: {primary_kw}
meta_description: "{meta_description}"
last_updated: 2026-10-15
---"""
    
    elif style == "yaml_coinlive":
        return f"""---
title: "{title}"
meta_title: "{meta_title}"
meta_description: "{meta_description}"
slug: "{slug_val}"
primary_keyword: "{primary_kw}"
category: "{category}"
last_reviewed: "2026-10-15"
---"""
    
    elif style == "inline":
        return f"""# {title}

- Primary keyword: `{primary_kw}`
- Slug: `{slug_val}`
- Meta title: `{meta_title}`
- Meta description: `{meta_description}`
"""
    
    elif style == "markdown":
        return f"""# {title}

**Published:** October 15, 2026 | **Site:** {site_cfg["site_name"]} | **Category:** {category}
"""
    
    else:  # yaml standard
        return f"""---
title: "{title}"
slug: "{slug_val}"
meta_title: "{meta_title}"
meta_description: "{meta_description}"
search_intent: "Commercial investigation"
primary_keyword: "{primary_kw}"
category: "{category}"
author: "{site_cfg["author"]}"
last_reviewed: "2026-10-15"
schema:
  - "Article"
  - "ItemList"
  - "FAQPage"
internal_links:
{il_str}
---"""

def get_article_meta(article_type, site_cfg):
    site_name = site_cfg["site_name"]
    
    metas = {
        "halloween_casino": {
            "title": f"Best Crypto Casinos for Halloween 2026: Live Events, Spooky Slots, and Real Bonuses",
            "meta_title": f"Best Crypto Casinos Halloween 2026: Live $40K–$50K Tournaments and Slots | {site_name}",
            "meta_description": f"Best crypto casinos for Halloween 2026 — BC.Game $20K, Gamdom $50K, Rollbit $40K, Shuffle $20K. Live event dates, no-KYC options, and Halloween slots reviewed.",
            "primary_kw": "best crypto casinos Halloween 2026",
        },
        "halloween_bonus": {
            "title": f"Best Halloween Crypto Casino Bonuses 2026: Tournament Prizes, Cash Drops, and What's Actually Worth Claiming",
            "meta_title": f"Best Halloween Crypto Casino Bonuses 2026: $50K Tournaments and $40K Races | {site_name}",
            "meta_description": f"Best Halloween crypto casino bonuses 2026 — Gamdom $50K Spooky Hill, Rollbit $40K Race, BC.Game $20K Cash Drop. Bonus mechanics and value analysis.",
            "primary_kw": "best halloween crypto casino bonuses 2026",
        },
        "halloween_slots": {
            "title": f"Best Halloween Crypto Slots 2026: RTP, Max Win, and Which Games Are Worth Playing",
            "meta_title": f"Best Halloween Crypto Slots 2026: RTP Data, Max Wins, and Provider Rankings | {site_name}",
            "meta_description": f"Best Halloween crypto slots 2026: Mental 2 (99,999x), Blood Suckers (98% RTP), Big Bass Halloween Splash 1000 (new Oct 12, 2026). RTP data and provider rankings.",
            "primary_kw": "best halloween crypto slots 2026",
        },
        "xmas_swap": {
            "title": f"Best Crypto Swap Aggregators for Christmas 2026: Gift Crypto Fast, No KYC, Best Rates",
            "meta_title": f"Best Crypto Swap Aggregators Christmas 2026: Gift, Convert, Send Fast | {site_name}",
            "meta_description": f"Best crypto swap aggregators for Christmas 2026 — ChangeNOW, 1inch, Jupiter, LlamaSwap, CoW Swap. No-KYC, best rates, fast settlement for holiday gifting.",
            "primary_kw": "best crypto swap aggregators Christmas 2026",
        },
        "xmas_nokyc": {
            "title": f"Best No-KYC Crypto Swaps for Christmas Casino Deposits 2026",
            "meta_title": f"Best No-KYC Crypto Swaps for Christmas Casino Deposits 2026 | {site_name}",
            "meta_description": f"Best no-KYC crypto swap platforms for Christmas casino deposits 2026 — ChangeNOW, RocketX, 1inch, CoW Swap. Fast, no-KYC, USDT TRC20 output.",
            "primary_kw": "best no kyc crypto swap christmas casino deposits 2026",
        },
        "xmas_gift": {
            "title": f"Best Last-Minute Crypto Gift Swaps 2026: Fast, No-KYC, Christmas Eve Ready",
            "meta_title": f"Best Last-Minute Crypto Gift Swaps Christmas 2026: Fast No-KYC Options | {site_name}",
            "meta_description": f"Best last-minute crypto gift swaps for Christmas 2026 — ChangeNOW, Jupiter, 1inch Base. Under 5 minutes, no KYC, step-by-step gifting guide.",
            "primary_kw": "best last minute crypto gift swap christmas 2026",
        },
    }
    return metas[article_type]

def get_slug(site_cfg, article_type):
    slug_name, article_cat = ARTICLE_SLUGS[article_type]
    if article_cat == "gambling":
        return site_cfg["slug_gambling"] + slug_name
    else:
        return site_cfg["slug_swap"] + slug_name

def get_category(site_cfg, article_type):
    _, article_cat = ARTICLE_SLUGS[article_type]
    if article_cat == "gambling":
        return site_cfg["category_gambling"]
    else:
        return site_cfg["category_swap"]

def get_internal_links(site_cfg, article_type):
    _, article_cat = ARTICLE_SLUGS[article_type]
    if article_cat == "gambling":
        return site_cfg["internal_casino"]
    else:
        return site_cfg["internal_swap"]

def get_output_filename(site_name, site_cfg, article_type, i):
    slug_name, _ = ARTICLE_SLUGS[article_type]
    if site_cfg["next_num"] is None:
        return slug_name + ".md"
    num = site_cfg["next_num"] + i
    return f"{num:02d}-{slug_name}.md"

def replace_site_references(body, site_name):
    """Replace 'Kanalcoin' with the target site name in the article body."""
    return body.replace("Kanalcoin Editorial", f"{site_name} Editorial").replace(
        "| Kanalcoin", f"| {site_name}").replace(
        "Nakamura Haruto, Kanalcoin", f"Editorial Team, {site_name}").replace(
        "— Nakamura Haruto,", f"— {site_name} Editorial Team,")

def generate_articles():
    total = 0
    for site_name, site_cfg in SITES.items():
        site_dir = os.path.join(BASE, site_name, "articles")
        os.makedirs(site_dir, exist_ok=True)
        
        for i, (master_file, _, article_type) in enumerate(MASTERS):
            master_content = read_master(master_file)
            body = strip_frontmatter(master_content)
            body = replace_site_references(body, site_cfg["site_name"])
            
            meta = get_article_meta(article_type, site_cfg)
            slug = get_slug(site_cfg, article_type)
            category = get_category(site_cfg, article_type)
            internal_links = get_internal_links(site_cfg, article_type)
            
            frontmatter = make_yaml_frontmatter(
                site_cfg, article_type, slug,
                meta["title"], meta["meta_title"], meta["meta_description"],
                meta["primary_kw"], category, internal_links,
                site_cfg["style"]
            )
            
            # For inline/markdown styles, body already starts with H1 from strip
            # For markdown style, frontmatter IS the H1, so don't double H1
            if site_cfg["style"] in ("markdown", "inline"):
                # Strip the H1 from body since frontmatter has one
                body_lines = body.lstrip("\n").split("\n")
                if body_lines and body_lines[0].startswith("# "):
                    body = "\n".join(body_lines[1:]).lstrip("\n")
                full_content = frontmatter + "\n\n" + body
            else:
                full_content = frontmatter + "\n\n" + body
            
            outfile = get_output_filename(site_name, site_cfg, article_type, i)
            outpath = os.path.join(site_dir, outfile)
            
            with open(outpath, "w", encoding="utf-8") as f:
                f.write(full_content)
            
            print(f"  OK {site_name}/{outfile} ({len(full_content):,} chars)")
            total += 1
    
    print(f"\nTotal articles generated: {total}")

if __name__ == "__main__":
    generate_articles()






