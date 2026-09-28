import asyncio
from playwright.async_api import async_playwright
import json, sys, time

TRUSTPILOT_COOKIES = [
    {"name": "jwt", "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcklkIjoiNmE2YjE3OGQ3YjA1MDIwN2ZhYmZhOWE5IiwiaGFzQWNjZXB0ZWRUZXJtcyI6dHJ1ZSwiaXNCbG9ja2VkRm9yUmVwb3J0aW5nIjpmYWxzZSwiYWNjZXNzVG9rZW4iOiJtbXEzUGR6aDZNRTU1WnhQRUJyWGx6VmptS3VEIiwiYXV0aGVudGljYXRpb25Tb3VyY2UiOiJnb29nbGUiLCJpYXQiOjE3ODU0MDMyODIsImV4cCI6MTc5MzE3OTI4Mn0.ehJWip9l1xFTsiGX9_MnjXQEJYyuCGl7VpAaI29m7bc", "domain": ".trustpilot.com", "path": "/"},
    {"name": "tp-consumer-id", "value": "6a6b178d7b050207fabfa9a9", "domain": ".trustpilot.com", "path": "/"},
    {"name": "TP.uuid", "value": "bb1e72da-d08e-4a3f-a643-1e0bdf641f5d", "domain": ".trustpilot.com", "path": "/"},
]

PLATFORMS = ["swapzone.io","stealthex.io","changenow.io","simpleswap.io","exolix.com","swapspace.co","letsexchange.io","sideshift.ai"]

async def scrape_platform(page, domain, max_pages=2):
    reviews = []
    for pg in range(1, max_pages+1):
        url = "https://www.trustpilot.com/review/" + domain + "?page=" + str(pg)
        try:
            await page.goto(url, timeout=20000, wait_until="domcontentloaded")
            await page.wait_for_timeout(3000)
            nd = await page.evaluate("() => { const el = document.getElementById('__NEXT_DATA__'); return el ? el.textContent : null; }")
            if not nd:
                break
            data = json.loads(nd)
            page_reviews = data.get("props", {}).get("pageProps", {}).get("reviews", [])
            if not page_reviews:
                break
            for r in page_reviews:
                rid = r.get("id","")
                reviews.append({
                    "id": rid,
                    "rating": r.get("rating", 0),
                    "text": r.get("text",""),
                    "title": r.get("title",""),
                    "author": r.get("consumer", {}).get("displayName",""),
                    "date": r.get("dates", {}).get("publishedDate",""),
                    "url": "https://www.trustpilot.com/reviews/" + rid,
                })
        except Exception as e:
            sys.stdout.buffer.write(("Error " + domain + " p" + str(pg) + ": " + str(e) + "\n").encode("utf-8"))
            break
    return reviews

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context()
        await ctx.add_cookies(TRUSTPILOT_COOKIES)
        page = await ctx.new_page()
        await page.goto("https://www.trustpilot.com/", timeout=20000, wait_until="domcontentloaded")
        await page.wait_for_timeout(4000)
        
        all_results = {}
        for domain in PLATFORMS:
            sys.stdout.buffer.write(("Scraping " + domain + "...\n").encode("utf-8"))
            reviews = await scrape_platform(page, domain)
            all_results[domain] = reviews
            sys.stdout.buffer.write(("  " + str(len(reviews)) + " reviews\n").encode("utf-8"))
            await page.wait_for_timeout(2000)
        
        with open(r"C:\Users\admin\Authority-Building\tp_fresh.json", "w", encoding="utf-8") as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
        sys.stdout.buffer.write(b"Saved tp_fresh.json\n")
        await browser.close()

asyncio.run(main())
