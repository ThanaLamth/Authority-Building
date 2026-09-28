import asyncio, json, re
from playwright.async_api import async_playwright

RD_COOKIES = [
    {"name":"reddit_session","value":"eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpsVFdYNlFVUEloWktaRG1rR0pVd1gvdWNFK01BSjBYRE12RU1kNzVxTXQ4IiwidHlwIjoiSldUIn0.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDI3MDMxNDAuMjkwODA4LCJpYXQiOjE3ODcwNjQ3NDAuMjkwODA4LCJqdGkiOiJiTjJxaEppeWRmamdCazl4ZWktcW1Fa21YYTBiVlEiLCJhdCI6MSwiY2lkIjoiY29va2llIiwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnlLamdVRUFBRF9fd0VWQUxrIiwiZmxvIjozLCJhbXIiOlsic3NvIl19.pGlpIlMl41p3KyZ6084QBkrMpX4RIOBq58ZyWtiVUT06buVRZ1NfYqSPHFanlU0sZ4QBAmzuFPaGzmuLw0JW2fgfD6Ut6yDph5drP9VccH5AAXvxNdvxb9K6t-4zSM9IdMLjVAjc7fO6uAQfqj5qU86nxgWxPm_aCkQxb-QQIFvv7Y4MwZFlhS_Oqfzz0hDUx106ECXIbD7dFgFPbRCjvqd3Rdu0P5_Osf1ci9wJNUdFYi1rgLcOWx0WyRxF-3D0dx_ItW4Ypycqg62XVdVbq5hjFyYqK6kd2wKcnne6PCmqU5bC6snO3YgN-kTG_8Uw8RKytcr-o9nQMOxQkbym6g","domain":".reddit.com","path":"/"},
    {"name":"token_v2","value":"eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzg3MTUxMTQwLjg4NTUwNCwiaWF0IjoxNzg3MDY0NzQwLjg4NTUwNCwianRpIjoiM2NLVDFUUzAwVENPUF95QlBtaHdwTFJuV2hvTHZRIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhdCI6MSwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5ieldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJyY2lkIjoiRjhjM0J0QURjLUVhVFZNWGdoSEFCOF9FQ1ZuUExyUnBqMVVhQUNFUW1CZyIsImZsbyI6Mn0.BXJg3W8D0Ulrqnq-T6tAvLZWjbzvNgMl9nkf86HASuR4zPqKNTn_vAkDwsY6x1HcU_OnfFgGuA7hLhqMAr12hk7GdlUOrIhPTYX4mk9hC2nqBUPy_SjtE6SlUtXzOqPrAqLwfP1_oQ30Jy_halMA7HtY7wH1irQ_8__d8RJYo9feXc9r9y0XQRMbmZT4nwr-VUdQQJaCfTRMonbM0m8KRGDZl-yD_GfF-nn5rrYs3jpIT7MR73U9Cp5lK51dNFfjRXHC3w5XDscJQVTJ-30Tilq24BS0tBzMzvGDjB846g_EPEsOjqCMP7NHRbWW2Hzo9d0VBBEBmfO5NDfv0feqyg","domain":".reddit.com","path":"/"},
    {"name":"loid","value":"000000000ij2vemib0.2.1693221624613.Z0FBQUFBQnFjZWZSODFCNWhuZmRWY1plV3hhZ0Nzdm0xNHh3eEZ4QzZROXZ1eHdVXzFfYjRxdjMtZFBqM0QwMU1tWUxiWEhXTUF1R0dzdm1QMlpmVk5Tdy1UVjdEaVh5Vmw5ZlJsQXRJREYwRzFGZEp4WGVMbk95aDd1V0FSU05tTDNLb21aSXIyWDc","domain":".reddit.com","path":"/"},
]

QUERIES = [
    ("swapzone", "CryptoCurrency"),
    ("stealthex", "CryptoCurrency"),
    ("changenow exchange", "CryptoCurrency"),
    ("simpleswap exchange", "CryptoCurrency"),
    ("exolix", "CryptoCurrency"),
    ("swapspace", "CryptoCurrency"),
    ("nexo crypto", "CryptoCurrency"),
    ("lido staking", "ethfinance"),
    ("swapzone", "Bitcoin"),
    ("changenow", "Bitcoin"),
]

results = {}

async def scrape_comments(ctx, query, sub):
    page = await ctx.new_page()
    posts = []
    try:
        # Use Reddit search with old-reddit style for better data
        url = f"https://www.reddit.com/r/{sub}/search/?q={query}&sort=top&t=year&type=comment"
        await page.goto(url, wait_until="domcontentloaded", timeout=25000)
        await page.wait_for_timeout(4000)
        
        # Try to get structured data
        content = await page.content()
        
        # Look for shreddit-comment or post-body elements
        comments_el = await page.query_selector_all("shreddit-comment")
        if comments_el:
            for el in comments_el[:10]:
                try:
                    text_el = await el.query_selector("p, [slot='text-body']")
                    text = await text_el.inner_text() if text_el else ""
                    score_attr = await el.get_attribute("score") or "0"
                    author_attr = await el.get_attribute("author") or ""
                    permalink_attr = await el.get_attribute("permalink") or ""
                    q_word = query.split()[0].lower()
                    if text and len(text) > 60 and q_word in text.lower() and int(score_attr or 0) >= 2:
                        posts.append({
                            "text": text[:380], "score": int(score_attr or 0),
                            "author": author_attr, "sub": sub,
                            "url": f"https://reddit.com{permalink_attr}" if permalink_attr else f"https://reddit.com/r/{sub}/search/?q={query}"
                        })
                except: pass
        
        # Fallback: search posts
        if not posts:
            url2 = f"https://www.reddit.com/r/{sub}/search/?q={query}&sort=top&t=year"
            await page.goto(url2, wait_until="domcontentloaded", timeout=25000)
            await page.wait_for_timeout(3000)
            post_els = await page.query_selector_all("article, [data-testid='post-container'], shreddit-post")
            for el in post_els[:8]:
                try:
                    title_el = await el.query_selector("h1,h2,h3,[slot='title']")
                    title = await title_el.inner_text() if title_el else ""
                    body_el = await el.query_selector("[data-click-id='body'] p, [slot='text-body'] p")
                    body = await body_el.inner_text() if body_el else ""
                    score_el = await el.query_selector("[data-score], [aria-label*='point']")
                    score_text = await score_el.inner_text() if score_el else "0"
                    score = int(re.sub(r"[^\d]","",score_text) or 0)
                    link_el = await el.query_selector("a[href*='/comments/']")
                    href = await link_el.get_attribute("href") if link_el else ""
                    q_word = query.split()[0].lower()
                    text_combined = (title + " " + body)
                    if q_word in text_combined.lower() and score >= 2:
                        posts.append({
                            "text": (body or title)[:380], "score": score,
                            "author": "", "sub": sub,
                            "url": f"https://reddit.com{href}" if href.startswith("/") else href,
                            "title": title
                        })
                except: pass
        
        print(f"  r/{sub} q={query}: {len(posts)} items")
    except Exception as e:
        print(f"  Reddit err {sub}/{query}: {e}")
    finally:
        await page.close()
    return posts

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
        await ctx.add_cookies(RD_COOKIES)
        
        # Test login
        page = await ctx.new_page()
        await page.goto("https://www.reddit.com", wait_until="domcontentloaded", timeout=20000)
        await page.wait_for_timeout(2000)
        title = await page.title()
        print(f"Reddit page title: {title}")
        await page.close()
        
        all_reddit = {}
        for query, sub in QUERIES:
            posts = await scrape_comments(ctx, query, sub)
            key = f"reddit_{query.replace(' ','_')}_{sub}"
            all_reddit[key] = posts
        
        await ctx.close()
        await browser.close()
        
        with open("C:/Users/admin/Authority-Building/reddit_reviews.json","w",encoding="utf-8") as f:
            json.dump(all_reddit, f, ensure_ascii=False, indent=2)
        print("Saved reddit_reviews.json")

asyncio.run(main())
