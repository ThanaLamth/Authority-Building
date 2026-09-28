import httpx, json, time, re

QUERIES = [
    ("swapzone", None),
    ("stealthex", None),
    ("changenow", None),
    ("simpleswap", None),
    ("exolix", None),
    ("swapspace", None),
    ("nexo crypto", None),
    ("lido staking ethereum", None),
]

results = {}
headers = {"User-Agent": "Mozilla/5.0 research/1.0"}

def clean(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:380]

def search_pullpush(query):
    posts = []
    url = f"https://api.pullpush.io/reddit/search/comment/?q={query}&size=15&sort=desc&sort_type=score"
    try:
        r = httpx.get(url, headers=headers, timeout=15)
        print(f"  Pullpush comment q={query}: {r.status_code}")
        if r.status_code == 200:
            data = r.json().get("data", [])
            q_word = query.split()[0].lower()
            for item in data:
                body = item.get("body","")
                score = item.get("score",0)
                sub = item.get("subreddit","")
                author = item.get("author","")
                permalink = item.get("permalink","")
                link_id = item.get("link_id","")
                if (body and len(body) > 60 and score >= 2 
                    and q_word in body.lower() 
                    and "[deleted]" not in body 
                    and "[removed]" not in body
                    and author not in ("AutoModerator","[deleted]")):
                    posts.append({
                        "text": clean(body), "score": score, "author": author,
                        "sub": sub, "url": f"https://reddit.com{permalink}" if permalink else "",
                        "source": "pullpush_comment"
                    })
    except Exception as e:
        print(f"  Pullpush err: {e}")
    
    # Also search submissions
    url2 = f"https://api.pullpush.io/reddit/search/submission/?q={query}&size=10&sort=desc&sort_type=score"
    try:
        r2 = httpx.get(url2, headers=headers, timeout=15)
        print(f"  Pullpush submission q={query}: {r2.status_code}")
        if r2.status_code == 200:
            data2 = r2.json().get("data", [])
            q_word = query.split()[0].lower()
            for item in data2:
                selftext = item.get("selftext","")
                title = item.get("title","")
                score = item.get("score",0)
                sub = item.get("subreddit","")
                author = item.get("author","")
                permalink = item.get("permalink","")
                text = selftext or title
                if (text and len(text) > 60 and score >= 3
                    and q_word in (selftext+title).lower()
                    and "[deleted]" not in selftext
                    and "[removed]" not in selftext):
                    posts.append({
                        "text": clean(selftext or title), "score": score, "author": author,
                        "sub": sub, "url": f"https://reddit.com{permalink}" if permalink else "",
                        "title": title, "source": "pullpush_submission"
                    })
    except Exception as e:
        print(f"  Pullpush sub err: {e}")
    
    return posts

for query, _ in QUERIES:
    print(f"\n=== {query} ===")
    posts = search_pullpush(query)
    results[f"reddit_{query.replace(' ','_')}"] = posts
    print(f"  Total: {len(posts)} items")
    time.sleep(1)

with open("C:/Users/admin/Authority-Building/reddit_reviews.json","w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("\nSaved.")
