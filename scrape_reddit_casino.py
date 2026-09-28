import requests, json, time, sys

PLATFORMS = {
    "stake.com":   ["stake", "OnlineCasinos", "CryptoCasinos"],
    "bc.game":     ["bcgame", "OnlineCasinos", "CryptoCasinos"],
    "1win.com":    ["1win", "OnlineCasinos", "sportsbook"],
    "jack.com":    ["jackbit", "OnlineCasinos", "CryptoCasinos"],
    "winna.com":   ["winna", "OnlineCasinos", "CryptoCasinos"],
    "rollblock.io":["rollblock", "OnlineCasinos", "CryptoCasinos"],
}

SEARCH_TERMS = {
    "stake.com":   ["stake.com casino", "stake casino review", "stake crypto casino"],
    "bc.game":     ["bc.game review", "bc game casino", "bcgame crypto"],
    "1win.com":    ["1win casino review", "1win crypto betting", "1win sportsbook"],
    "jack.com":    ["jack.com casino", "jackbit casino", "jackbit review"],
    "winna.com":   ["winna casino review", "winna.com crypto"],
    "rollblock.io":["rollblock casino", "rollblock rblk", "rollblock review"],
}

results = {}

for platform, search_terms in SEARCH_TERMS.items():
    posts = []
    for term in search_terms[:2]:
        url = f"https://api.pullpush.io/reddit/search/submission/?q={requests.utils.quote(term)}&size=10&sort=score&sort_type=score&after=1717200000"
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                data = r.json()
                for item in data.get("data", []):
                    if item.get("score", 0) >= 2:
                        posts.append({
                            "title": item.get("title",""),
                            "text": item.get("selftext","")[:500],
                            "author": item.get("author",""),
                            "subreddit": item.get("subreddit",""),
                            "score": item.get("score",0),
                            "url": "https://reddit.com" + item.get("permalink",""),
                            "created": item.get("created_utc",0),
                        })
        except Exception as e:
            sys.stdout.write(f"Error {platform}/{term}: {e}\n")
        time.sleep(1)
    
    # Also search comments
    for term in search_terms[:1]:
        url = f"https://api.pullpush.io/reddit/search/comment/?q={requests.utils.quote(term)}&size=15&sort=score&sort_type=score&after=1717200000"
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                data = r.json()
                for item in data.get("data", []):
                    if item.get("score", 0) >= 3 and len(item.get("body","")) > 30:
                        posts.append({
                            "type": "comment",
                            "text": item.get("body","")[:500],
                            "author": item.get("author",""),
                            "subreddit": item.get("subreddit",""),
                            "score": item.get("score",0),
                            "url": "https://reddit.com" + item.get("permalink",""),
                            "link_id": item.get("link_id",""),
                        })
        except Exception as e:
            sys.stdout.write(f"Error comment {platform}/{term}: {e}\n")
        time.sleep(1)
    
    results[platform] = posts
    sys.stdout.write(f"{platform}: {len(posts)} items\n")
    sys.stdout.flush()

with open(r"C:\Users\admin\Authority-Building\reddit_casino.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

sys.stdout.write("Done: reddit_casino.json\n")
