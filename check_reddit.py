import json

rd = json.load(open("reddit_reviews.json", encoding="utf-8"))

for key in rd.keys():
    items = rd[key]
    good = [r for r in items if r.get("score",0) >= 5 
            and 80 < len(r.get("text","")) < 350
            and r.get("author","") not in ("AutoModerator","[deleted]","")
            and "reddit.com" not in r.get("text","")
            and not r.get("text","").startswith("http")]
    good.sort(key=lambda x: x.get("score",0), reverse=True)
    print(f"\n{key}: {len(good)} good comments")
    for r in good[:2]:
        print(f"  score={r['score']} u/{r['author']} [{r.get('sub','')}]")
        print(f"  {r['text'][:200]}")
        print(f"  {r.get('url','')}")
