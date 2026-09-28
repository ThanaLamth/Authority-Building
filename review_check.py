import json
data = json.load(open("scraped_reviews.json", encoding="utf-8"))

def show_reviews(key):
    items = data.get(key, [])
    pos = [r for r in items if r.get("stars", 0) >= 4 and len(r.get("text","")) > 60]
    neg = [r for r in items if r.get("stars", 0) <= 2 and len(r.get("text","")) > 60]
    print(f"--- {key} | pos={len(pos)} neg={len(neg)} ---")
    if pos:
        r = pos[0]
        stars = r["stars"]
        author = r["author"]
        text = r["text"][:120]
        url = r.get("url","no-url")
        print(f"  POS ({stars}*) {author}: {text}")
        print(f"  URL: {url}")
    if neg:
        r = neg[0]
        stars = r["stars"]
        author = r["author"]
        text = r["text"][:120]
        url = r.get("url","no-url")
        print(f"  NEG ({stars}*) {author}: {text}")
        print(f"  URL: {url}")
    print()

for k in ["tp_swapzone.io","tp_stealthex.io","tp_changenow.io","tp_simpleswap.io","tp_exolix.com","tp_swapspace.co","tp_changelly.com","tp_nexo.com"]:
    show_reviews(k)

# Reddit samples
rd = json.load(open("reddit_reviews.json", encoding="utf-8"))
print("=== REDDIT ===")
for k in list(rd.keys())[:4]:
    items = [r for r in rd[k] if r.get("score",0) >= 3 and len(r.get("text","")) > 60]
    print(f"{k}: {len(items)} usable comments")
    if items:
        r = items[0]
        author = r.get("author","")
        text = r.get("text","")[:100]
        url = r.get("url","")
        score = r.get("score",0)
        print(f"  ({score} pts) u/{author}: {text}")
        print(f"  URL: {url}")
    print()
