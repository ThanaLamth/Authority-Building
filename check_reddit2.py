import json
rd = json.load(open("reddit_reviews.json", encoding="utf-8"))
# xmrtrader changenow comment
for r in rd.get("reddit_changenow", []):
    if "MoneroFox" in r.get("author",""):
        print(repr(r["text"]))
        print(r["url"])
        break
