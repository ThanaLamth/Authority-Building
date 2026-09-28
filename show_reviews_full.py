import json

data = json.load(open("scraped_reviews.json", encoding="utf-8"))
rd = json.load(open("reddit_reviews.json", encoding="utf-8"))

def best_reviews(key, tp_or_rd="tp"):
    if tp_or_rd == "tp":
        items = data.get(key, [])
        pos = [r for r in items if r.get("stars", 0) >= 4 and 60 < len(r.get("text","")) < 400
               and "referral" not in r.get("text","").lower()]
        neg = [r for r in items if r.get("stars", 0) <= 2 and 60 < len(r.get("text","")) < 400]
        # sort pos by length desc (more specific), neg too
        pos.sort(key=lambda x: len(x.get("text","")), reverse=True)
        neg.sort(key=lambda x: len(x.get("text","")), reverse=True)
        return pos[:3], neg[:3]
    else:
        items = [r for r in rd.get(key, []) if r.get("score",0) >= 3 and 60 < len(r.get("text","")) < 400]
        items.sort(key=lambda x: x.get("score",0), reverse=True)
        return items[:3], []

print("=== TRUSTPILOT BEST REVIEWS ===\n")
for platform, key in [
    ("Swapzone", "tp_swapzone.io"),
    ("StealthEX", "tp_stealthex.io"),
    ("ChangeNOW", "tp_changenow.io"),
    ("SimpleSwap", "tp_simpleswap.io"),
    ("Exolix", "tp_exolix.com"),
    ("SwapSpace", "tp_swapspace.co"),
    ("Changelly", "tp_changelly.com"),
    ("Nexo", "tp_nexo.com"),
]:
    pos, neg = best_reviews(key)
    print(f"=== {platform} ===")
    if pos:
        r = pos[0]
        print(f"BEST POS ({r['stars']}*) {r['author']}:")
        print(f"  {r['text']}")
        print(f"  URL: {r.get('url','')}")
    if neg:
        r = neg[0]
        print(f"BEST NEG ({r['stars']}*) {r['author']}:")
        print(f"  {r['text']}")
        print(f"  URL: {r.get('url','')}")
    print()
