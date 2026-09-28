import json, re, os

# Load data
with open(r"C:\Users\admin\Authority-Building\tp_casino.json", encoding="utf-8") as f:
    tp = json.load(f)

with open(r"C:\Users\admin\Authority-Building\reddit_casino.json", encoding="utf-8") as f:
    reddit = json.load(f)

# Print summary per platform
for platform in tp:
    reviews = tp[platform]
    pos = [r for r in reviews if r["rating"] >= 4 and len(r["text"]) > 60]
    neg = [r for r in reviews if r["rating"] <= 2 and len(r["text"]) > 60]
    total = len(reviews)
    avg = sum(r["rating"] for r in reviews) / total if total else 0
    print(f"\n=== {platform} === ({total} reviews, avg {avg:.1f})")
    print(f"  Positive ({len(pos)}), Negative ({len(neg)})")
    if pos:
        r = pos[0]
        print(f"  [POS] {r['rating']}★ {r['author']}: {r['text'][:120]}")
    if neg:
        r = neg[0]
        print(f"  [NEG] {r['rating']}★ {r['author']}: {r['text'][:120]}")

print("\n=== REDDIT ===")
for platform in reddit:
    items = reddit[platform]
    print(f"\n{platform}: {len(items)} items")
    for item in items[:2]:
        txt = item.get("text") or item.get("title","")
        print(f"  [{item.get('score',0)}] u/{item.get('author','')} r/{item.get('subreddit','')}: {txt[:100]}")
