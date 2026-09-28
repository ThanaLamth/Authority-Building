import json

data = json.load(open("scraped_reviews.json", encoding="utf-8"))
rd = json.load(open("reddit_reviews.json", encoding="utf-8"))

# Get all reviews per platform
platforms = {
    "swapzone": ("tp_swapzone.io", "reddit_swapzone"),
    "stealthex": ("tp_stealthex.io", "reddit_stealthex"),
    "changenow": ("tp_changenow.io", "reddit_changenow"),
    "simpleswap": ("tp_simpleswap.io", "reddit_simpleswap"),
    "exolix": ("tp_exolix.com", "reddit_exolix"),
    "swapspace": ("tp_swapspace.co", "reddit_swapspace"),
    "changelly": ("tp_changelly.com", None),
    "nexo": ("tp_nexo.com", "reddit_nexo_platform"),
}

for name, (tp_key, rd_key) in platforms.items():
    print(f"\n{'='*60}")
    print(f"PLATFORM: {name}")
    print(f"{'='*60}")
    tp_items = data.get(tp_key, [])
    pos = [r for r in tp_items if r.get("stars",0) >= 4 and 60 < len(r.get("text","")) < 500]
    neg = [r for r in tp_items if r.get("stars",0) <= 2 and 60 < len(r.get("text","")) < 500]
    pos.sort(key=lambda x: len(x.get("text","")), reverse=True)
    neg.sort(key=lambda x: len(x.get("text","")), reverse=True)
    
    print(f"\n--- BEST POS (TP) ---")
    for r in pos[:2]:
        print(f"({r['stars']}*) {r['author']}: {r['text']}")
        print(f"URL: {r.get('url','')}")
        print()
    
    print(f"--- BEST NEG (TP) ---")
    for r in neg[:2]:
        print(f"({r['stars']}*) {r['author']}: {r['text']}")
        print(f"URL: {r.get('url','')}")
        print()
    
    if rd_key:
        rd_items = [r for r in rd.get(rd_key, []) if r.get("score",0) >= 3 and 60 < len(r.get("text","")) < 400
                    and r.get("author","") not in ("AutoModerator","[deleted]","")]
        rd_items.sort(key=lambda x: x.get("score",0), reverse=True)
        print(f"--- BEST REDDIT ---")
        for r in rd_items[:2]:
            print(f"(score={r['score']}) u/{r['author']} [{r.get('sub','')}]: {r['text'][:200]}")
            print(f"URL: {r.get('url','')}")
            print()
