import asyncio
from playwright.async_api import async_playwright
import os

BASE = r"C:\Users\admin\Authority-Building"

RETRY = [
    ("Kanalcoin/swapzone-batch/media/20-austrac-register.png",       "https://www.austrac.gov.au/business/register-and-re-register"),
    ("DeFiLiban/swapzone-batch/media/18-lido-dashboard.png",         "https://lido.fi/"),
    ("DeFiLiban/swapzone-batch/media/18-rocketpool-dashboard.png",   "https://rocketpool.net/"),
    ("DeFiLiban/swapzone-batch/media/18-nexo-earn.png",              "https://nexo.com/earn"),
    ("DeFiLiban/swapzone-batch/media/19-youhodler-homepage.png",     "https://www.youhodler.com/"),
    ("DeFiLiban/swapzone-batch/media/19-coinrabbit-loan.png",        "https://coinrabbit.io/"),
    ("DeFiLiban/swapzone-batch/media/19-nexo-loan.png",              "https://nexo.com/borrow"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for path, url in RETRY:
            dest = os.path.join(BASE, path)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            # fresh context per site
            ctx = await browser.new_context(
                viewport={"width": 1440, "height": 900},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )
            page = await ctx.new_page()
            try:
                await page.goto(url, timeout=30000, wait_until="domcontentloaded")
                await page.wait_for_timeout(3000)
                await page.screenshot(path=dest, full_page=True)
                print(f"OK   {path}")
            except Exception as e:
                print(f"FAIL {path} — {e}")
            finally:
                await ctx.close()
        await browser.close()

asyncio.run(main())
