import asyncio, json, re
from playwright.async_api import async_playwright

TP_COOKIES = [
    {"name":"jwt","value":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcklkIjoiNmE2YjE3OGQ3YjA1MDIwN2ZhYmZhOWE5IiwiaGFzQWNjZXB0ZWRUZXJtcyI6dHJ1ZSwiaXNCbG9ja2VkRm9yUmVwb3J0aW5nIjpmYWxzZSwiYWNjZXNzVG9rZW4iOiJtbXEzUGR6aDZNRTU1WnhQRUJyWGx6VmptS3VEIiwiYXV0aGVudGljYXRpb25Tb3VyY2UiOiJnb29nbGUiLCJpYXQiOjE3ODU0MDMyODIsImV4cCI6MTc5MzE3OTI4Mn0.ehJWip9l1xFTsiGX9_MnjXQEJYyuCGl7VpAaI29m7bc","domain":".trustpilot.com","path":"/"},
    {"name":"tp-consumer-id","value":"6a6b178d7b050207fabfa9a9","domain":".trustpilot.com","path":"/"},
    {"name":"TP.uuid","value":"bb1e72da-d08e-4a3f-a643-1e0bdf641f5d","domain":".trustpilot.com","path":"/"},
    {"name":"OptanonConsent","value":"isGpcEnabled=0&groups=C0001:1,C0002:1,C0003:1,C0004:1","domain":".trustpilot.com","path":"/"},
]

RD_COOKIES = [
    {"name":"reddit_session","value":"eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpsVFdYNlFVUEloWktaRG1rR0pVd1gvdWNFK01BSjBYRE12RU1kNzVxTXQ4IiwidHlwIjoiSldUIn0.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDI3MDMxNDAuMjkwODA4LCJpYXQiOjE3ODcwNjQ3NDAuMjkwODA4LCJqdGkiOiJiTjJxaEppeWRmamdCazl4ZWktcW1Fa21YYTBiVlEiLCJhdCI6MSwiY2lkIjoiY29va2llIiwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnlLamdVRUFBRF9fd0VWQUxrIiwiZmxvIjozLCJhbXIiOlsic3NvIl19.pGlpIlMl41p3KyZ6084QBkrMpX4RIOBq58ZyWtiVUT06buVRZ1NfYqSPHFanlU0sZ4QBAmzuFPaGzmuLw0JW2fgfD6Ut6yDph5drP9VccH5AAXvxNdvxb9K6t-4zSM9IdMLjVAjc7fO6uAQfqj5qU86nxgWxPm_aCkQxb-QQIFvv7Y4MwZFlhS_Oqfzz0hDUx106ECXIbD7dFgFPbRCjvqd3Rdu0P5_Osf1ci9wJNUdFYi1rgLcOWx0WyRxF-3D0dx_ItW4Ypycqg62XVdVbq5hjFyYqK6kd2wKcnne6PCmqU5bC6snO3YgN-kTG_8Uw8RKytcr-o9nQMOxQkbym6g","domain":".reddit.com","path":"/"},
    {"name":"token_v2","value":"eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzg3MTUxMTQwLjg4NTUwNCwiaWF0IjoxNzg3MDY0NzQwLjg4NTUwNCwianRpIjoiM2NLVDFUUzAwVENPUF95QlBtaHdwTFJuV2hvTHZRIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhdCI6MSwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5ieldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJyY2lkIjoiRjhjM0J0QURjLUVhVFZNWGdoSEFCOF9FQ1ZuUExyUnBqMVVhQUNFUW1CZyIsImZsbyI6Mn0.BXJg3W8D0Ulrqnq-T6tAvLZWjbzvNgMl9nkf86HASuR4zPqKNTn_vAkDwsY6x1HcU_OnfFgGuA7hLhqMAr12hk7GdlUOrIhPTYX4mk9hC2nqBUPy_SjtE6SlUtXzOqPrAqLwfP1_oQ30Jy_halMA7HtY7wH1irQ_8__d8RJYo9feXc9r9y0XQRMbmZT4nwr-VUdQQJaCfTRMonbM0m8KRGDZl-yD_GfF-nn5rrYs3jpIT7MR73U9Cp5lK51dNFfjRXHC3w5XDscJQVTJ-30Tilq24BS0tBzMzvGDjB846g_EPEsOjqCMP7NHRbWW2Hzo9d0VBBEBmfO5NDfv0feqyg","domain":".reddit.com","path":"/"},
    {"name":"loid","value":"000000000ij2vemib0.2.1693221624613.Z0FBQUFBQnFjZWZSODFCNWhuZmRWY1plV3hhZ0Nzdm0xNHh3eEZ4QzZROXZ1eHdVXzFfYjRxdjMtZFBqM0QwMU1tWUxiWEhXTUF1R0dzdm1QMlpmVk5Tdy1UVjdEaVh5Vmw5ZlJsQXRJREYwRzFGZEp4WGVMbk95aDd1V0FSU05tTDNLb21aSXIyWDc","domain":".reddit.com","path":"/"},
]

PLATFORMS = [
    ("swapzone.io", "Swapzone"),
    ("stealthex.io", "StealthEX"),
    ("changenow.io", "ChangeNOW"),
    ("simpleswap.io", "SimpleSwap"),
    ("exolix.com", "Exolix"),
    ("swapspace.co", "SwapSpace"),
    ("changelly.com", "Changelly"),
    ("nexo.com", "Nexo"),
]

REDDIT_QUERIES = [
    ("swapzone", "CryptoCurrency"),
    ("stealthex", "CryptoCurrency"),
    ("changenow", "CryptoCurrency"),
    ("simpleswap", "CryptoCurrency"),
    ("exolix", "CryptoCurrency"),
    ("swapspace", "CryptoCurrency"),
    ("nexo platform", "CryptoCurrency"),
    ("lido staking", "ethfinance"),
]

results = {}

async def scrape_tp_page(context, domain, stars):
    page = await context.new_page()
    revs = []
    try:
        url = f"https://www.trustpilot.com/review/{domain}?sort=recency&stars={stars}"
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(3000)
        content = await page.content()
        nd = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', content, re.DOTALL)
        if nd:
            data = json.loads(nd.group(1))
            pp = data.get("props",{}).get("pageProps",{})
            page_reviews = pp.get("reviews") or pp.get("businessUnitReviews",{}).get("reviews") or []
            for rv in page_reviews[:8]:
                text = rv.get("text","") or rv.get("body","") or (rv.get("content",{}) or {}).get("original","")
                rating = rv.get("rating",{})
                star_val = rating.get("stars",0) if isinstance(rating,dict) else (rating or 0)
                rid = rv.get("id","") or rv.get("reviewId","")
                consumer = rv.get("consumer",{}) or {}
                author = consumer.get("displayName","") if isinstance(consumer,dict) else ""
                dates = rv.get("dates",{}) or {}
                date = dates.get("publishedDate","")[:10] if isinstance(dates,dict) else ""
                if text and len(text) > 60:
                    revs.append({
                        "text": text[:380], "stars": star_val, "author": author,
                        "id": rid, "date": date,
                        "url": f"https://www.trustpilot.com/reviews/{rid}" if rid else f"https://www.trustpilot.com/review/{domain}"
                    })
        print(f"  TP {domain} stars={stars}: {len(revs)} reviews")
    except Exception as e:
        print(f"  TP {domain} stars={stars} err: {e}")
    finally:
        await page.close()
    return revs

async def scrape_reddit_page(context, query, sub):
    page = await context.new_page()
    posts = []
    try:
        url = f"https://www.reddit.com/r/{sub}/search/?q={query}&sort=top&t=year"
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(3000)
        content = await page.content()
        # find post links and text
        nd = re.search(r'window\.__r = ({.*?});</script>', content, re.DOTALL)
        # fallback: extract from JSON API
        api_url = f"https://www.reddit.com/r/{sub}/search.json?q={query}&sort=top&t=year&limit=10"
        await page.goto(api_url, wait_until="domcontentloaded", timeout=20000)
        await page.wait_for_timeout(2000)
        json_text = await page.evaluate("() => document.body.innerText")
        try:
            data = json.loads(json_text)
            children = data.get("data",{}).get("children",[])
            for p in children[:8]:
                pd = p.get("data",{})
                text = pd.get("selftext","")
                title = pd.get("title","")
                score = pd.get("score",0)
                q_word = query.split()[0].lower()
                if score >= 2 and q_word in (text+title).lower() and text and len(text) > 60 and "[deleted]" not in text:
                    posts.append({
                        "text": text[:380], "score": score, "author": pd.get("author",""),
                        "sub": sub, "url": "https://reddit.com"+pd.get("permalink",""), "title": title
                    })
        except:
            pass
        print(f"  Reddit r/{sub} q={query}: {len(posts)} posts")
    except Exception as e:
        print(f"  Reddit err {sub}/{query}: {e}")
    finally:
        await page.close()
    return posts

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # Trustpilot context
        tp_ctx = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        await tp_ctx.add_cookies(TP_COOKIES)
        
        print("=== Trustpilot ===")
        for domain, name in PLATFORMS:
            revs = []
            for stars in ["5","1","2"]:
                r = await scrape_tp_page(tp_ctx, domain, stars)
                revs.extend(r)
                if len([x for x in revs if x["stars"]>=4]) >= 2 and len([x for x in revs if x["stars"]<=2]) >= 1:
                    break
            results[f"tp_{domain}"] = revs
            pos = [x for x in revs if x.get("stars",0) >= 4]
            neg = [x for x in revs if x.get("stars",0) <= 2]
            print(f"  {name}: {len(pos)} pos, {len(neg)} neg")
        
        await tp_ctx.close()
        
        # Reddit context
        rd_ctx = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        await rd_ctx.add_cookies(RD_COOKIES)
        
        print("\n=== Reddit ===")
        for query, sub in REDDIT_QUERIES:
            posts = await scrape_reddit_page(rd_ctx, query, sub)
            results[f"reddit_{query.replace(' ','_')}"] = posts
        
        await rd_ctx.close()
        await browser.close()
    
    with open("C:/Users/admin/Authority-Building/scraped_reviews.json","w",encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved to scraped_reviews.json")

asyncio.run(main())
