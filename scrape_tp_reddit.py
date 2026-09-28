import httpx, json, re, time, random

TP_COOKIES = {
    "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcklkIjoiNmE2YjE3OGQ3YjA1MDIwN2ZhYmZhOWE5IiwiaGFzQWNjZXB0ZWRUZXJtcyI6dHJ1ZSwiaXNCbG9ja2VkRm9yUmVwb3J0aW5nIjpmYWxzZSwiYWNjZXNzVG9rZW4iOiJtbXEzUGR6aDZNRTU1WnhQRUJyWGx6VmptS3VEIiwiYXV0aGVudGljYXRpb25Tb3VyY2UiOiJnb29nbGUiLCJpYXQiOjE3ODU0MDMyODIsImV4cCI6MTc5MzE3OTI4Mn0.ehJWip9l1xFTsiGX9_MnjXQEJYyuCGl7VpAaI29m7bc",
    "tp-consumer-id": "6a6b178d7b050207fabfa9a9",
    "TP.uuid": "bb1e72da-d08e-4a3f-a643-1e0bdf641f5d",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Tue+Aug+18+2026&version=202607.1.0&groups=C0001:1,C0002:1,C0003:1,C0004:1",
}

RD_COOKIES = {
    "reddit_session": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpsVFdYNlFVUEloWktaRG1rR0pVd1gvdWNFK01BSjBYRE12RU1kNzVxTXQ4IiwidHlwIjoiSldUIn0.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDI3MDMxNDAuMjkwODA4LCJpYXQiOjE3ODcwNjQ3NDAuMjkwODA4LCJqdGkiOiJiTjJxaEppeWRmamdCazl4ZWktcW1Fa21YYTBiVlEiLCJhdCI6MSwiY2lkIjoiY29va2llIiwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnlLamdVRUFBRF9fd0VWQUxrIiwiZmxvIjozLCJhbXIiOlsic3NvIl19.pGlpIlMl41p3KyZ6084QBkrMpX4RIOBq58ZyWtiVUT06buVRZ1NfYqSPHFanlU0sZ4QBAmzuFPaGzmuLw0JW2fgfD6Ut6yDph5drP9VccH5AAXvxNdvxb9K6t-4zSM9IdMLjVAjc7fO6uAQfqj5qU86nxgWxPm_aCkQxb-QQIFvv7Y4MwZFlhS_Oqfzz0hDUx106ECXIbD7dFgFPbRCjvqd3Rdu0P5_Osf1ci9wJNUdFYi1rgLcOWx0WyRxF-3D0dx_ItW4Ypycqg62XVdVbq5hjFyYqK6kd2wKcnne6PCmqU5bC6snO3YgN-kTG_8Uw8RKytcr-o9nQMOxQkbym6g",
    "token_v2": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzg3MTUxMTQwLjg4NTUwNCwiaWF0IjoxNzg3MDY0NzQwLjg4NTUwNCwianRpIjoiM2NLVDFUUzAwVENPUF95QlBtaHdwTFJuV2hvTHZRIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhdCI6MSwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5ieldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJyY2lkIjoiRjhjM0J0QURjLUVhVFZNWGdoSEFCOF9FQ1ZuUExyUnBqMVVhQUNFUW1CZyIsImZsbyI6Mn0.BXJg3W8D0Ulrqnq-T6tAvLZWjbzvNgMl9nkf86HASuR4zPqKNTn_vAkDwsY6x1HcU_OnfFgGuA7hLhqMAr12hk7GdlUOrIhPTYX4mk9hC2nqBUPy_SjtE6SlUtXzOqPrAqLwfP1_oQ30Jy_halMA7HtY7wH1irQ_8__d8RJYo9feXc9r9y0XQRMbmZT4nwr-VUdQQJaCfTRMonbM0m8KRGDZl-yD_GfF-nn5rrYs3jpIT7MR73U9Cp5lK51dNFfjRXHC3w5XDscJQVTJ-30Tilq24BS0tBzMzvGDjB846g_EPEsOjqCMP7NHRbWW2Hzo9d0VBBEBmfO5NDfv0feqyg",
    "loid": "000000000ij2vemib0.2.1693221624613.Z0FBQUFBQnFjZWZSODFCNWhuZmRWY1plV3hhZ0Nzdm0xNHh3eEZ4QzZROXZ1eHdVXzFfYjRxdjMtZFBqM0QwMU1tWUxiWEhXTUF1R0dzdm1QMlpmVk5Tdy1UVjdEaVh5Vmw5ZlJsQXRJREYwRzFGZEp4WGVMbk95aDd1V0FSU05tTDNLb21aSXIyWDc",
}

PLATFORMS = ["swapzone.io","stealthex.io","changenow.io","simpleswap.io","exolix.com","swapspace.co","changelly.com","nexo.com"]

REDDIT_QUERIES = [
    ("swapzone", ["CryptoCurrency","Bitcoin"]),
    ("stealthex swap", ["CryptoCurrency","Monero"]),
    ("changenow exchange", ["CryptoCurrency","Bitcoin"]),
    ("simpleswap exchange", ["CryptoCurrency"]),
    ("exolix exchange", ["CryptoCurrency"]),
    ("swapspace aggregator", ["CryptoCurrency"]),
    ("nexo lending crypto", ["CryptoCurrency","defi"]),
    ("lido staking eth", ["ethfinance","ethereum"]),
]

results = {}
headers_tp = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36","Accept":"text/html","Accept-Language":"en-US,en;q=0.9"}
headers_rd = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36","Accept":"application/json"}

def scrape_tp(domain):
    revs = []
    for stars_filter in ["5","1"]:
        url = f"https://www.trustpilot.com/review/{domain}?sort=recency&stars={stars_filter}"
        try:
            r = httpx.get(url, cookies=TP_COOKIES, headers=headers_tp, timeout=20, follow_redirects=True)
            print(f"  TP {domain} stars={stars_filter}: {r.status_code} {len(r.text)}c")
            nd = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', r.text, re.DOTALL)
            if nd:
                data = json.loads(nd.group(1))
                page_reviews = (data.get("props",{}).get("pageProps",{}).get("reviews") or
                                data.get("props",{}).get("pageProps",{}).get("businessUnitReviews",{}).get("reviews") or [])
                for rv in page_reviews[:10]:
                    text = ""
                    if isinstance(rv.get("text"), str): text = rv["text"]
                    elif isinstance(rv.get("body"), str): text = rv["body"]
                    elif isinstance(rv.get("content"), dict): text = rv["content"].get("original","")
                    
                    rating = rv.get("rating",{})
                    stars = rating.get("stars",0) if isinstance(rating,dict) else rating
                    rid = rv.get("id","") or rv.get("reviewId","")
                    author = ""
                    if isinstance(rv.get("consumer"),dict): author = rv["consumer"].get("displayName","")
                    date = ""
                    if isinstance(rv.get("dates"),dict): date = rv["dates"].get("publishedDate","")[:10]
                    
                    if text and len(text) > 60 and not any(x in text.lower() for x in ["referral","ref link","click here to earn"]):
                        revs.append({"text":text[:380],"stars":stars,"author":author,"id":rid,"date":date,
                                     "url":f"https://www.trustpilot.com/reviews/{rid}" if rid else f"https://www.trustpilot.com/review/{domain}"})
        except Exception as e:
            print(f"  TP err: {e}")
        time.sleep(random.uniform(1.5,2.5))
    return revs

def scrape_reddit(query, subs):
    comments = []
    for sub in subs[:2]:
        url = f"https://www.reddit.com/r/{sub}/search.json?q={query}&sort=top&t=year&limit=15&type=link"
        try:
            r = httpx.get(url, cookies=RD_COOKIES, headers=headers_rd, timeout=15, follow_redirects=True)
            print(f"  Reddit r/{sub} q={query}: {r.status_code}")
            if r.status_code == 200:
                posts = r.json().get("data",{}).get("children",[])
                for p in posts[:8]:
                    pd = p.get("data",{})
                    text = pd.get("selftext","")
                    title = pd.get("title","")
                    score = pd.get("score",0)
                    q_word = query.split()[0].lower()
                    if text and len(text) > 60 and score >= 2 and q_word in (text+title).lower() and "[deleted]" not in text and "[removed]" not in text:
                        comments.append({"text":text[:380],"score":score,"author":pd.get("author",""),
                                         "sub":sub,"url":"https://reddit.com"+pd.get("permalink",""),"title":title})
        except Exception as e:
            print(f"  Reddit err: {e}")
        time.sleep(random.uniform(1,2))
    return comments

print("=== Trustpilot ===")
for p in PLATFORMS:
    print(f"\n{p}:")
    revs = scrape_tp(p)
    results[f"tp_{p}"] = revs
    pos = [r for r in revs if r.get("stars",0) >= 4]
    neg = [r for r in revs if r.get("stars",0) <= 2]
    print(f"  {len(revs)} reviews: {len(pos)} pos, {len(neg)} neg")

print("\n=== Reddit ===")
for q, subs in REDDIT_QUERIES:
    print(f"\n{q}:")
    coms = scrape_reddit(q, subs)
    results[f"reddit_{q.replace(' ','_')}"] = coms
    print(f"  {len(coms)} posts")

with open("C:/Users/admin/Authority-Building/scraped_reviews.json","w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("\nSaved.")
