import asyncio
from playwright.async_api import async_playwright
import os

BASE = r"C:\Users\admin\Authority-Building"

SWAPZONE_QUERIES = [
    ("coinwy/swapzone-batch/media/01-swapzone-query-btc-eth.png",       "BTC",  "ETH"),
    ("coinwy/swapzone-batch/media/02-swapzone-query-results.png",       "BTC",  "ETH"),
    ("coinwy/swapzone-batch/media/03-swapzone-no-registration-flow.png","BTC",  "ETH"),
    ("coinwy/swapzone-batch/media/04-swapzone-rate-toggle.png",         "BTC",  "ETH"),
    ("coinwy/swapzone-batch/media/05-swapzone-btc-xmr-results.png",     "BTC",  "XMR"),
    ("coinwy/swapzone-batch/media/06-swapzone-usdt-btc-results.png",    "USDT", "BTC"),
    ("coinwy/swapzone-batch/media/07-swapzone-btc-eth-results.png",     "BTC",  "ETH"),
    ("coinwy/swapzone-batch/media/08-swapzone-eth-btc-results.png",     "ETH",  "BTC"),
    ("coinwy/swapzone-batch/media/09-swapzone-btc-trx-results.png",     "BTC",  "TRX"),
    ("coinwy/swapzone-batch/media/10-swapzone-btc-ton-results.png",     "BTC",  "TON"),
    ("coinwy/swapzone-batch/media/11-swapzone-query-with-changenow.png","BTC",  "ETH"),
    ("coinwy/swapzone-batch/media/12-swapzone-btc-eth-results.png",     "BTC",  "ETH"),
    ("coinwy/swapzone-batch/media/12-swapzone-homepage.png",            None,   None),
    ("coinwy/swapzone-batch/media/13-swapzone-homepage.png",            None,   None),
    ("coinwy/swapzone-batch/media/14-swapzone-no-kyc-flow.png",         "BTC",  "ETH"),
    ("coinwy/swapzone-batch/media/15-swapzone-eur-btc-results.png",     "EUR",  "BTC"),
    ("coinwy/swapzone-batch/media/16-swapzone-eur-xmr-results.png",     "BTC",  "XMR"),
    ("coinwy/swapzone-batch/media/17-swapzone-aggregator-results.png",  "BTC",  "ETH"),
    ("coinwy/swapzone-batch/media/20-swapzone-aud-btc-results.png",     "AUD",  "BTC"),
    ("DeFiLiban/swapzone-batch/media/18-swapzone-staking-page.png",     None,   "staking"),
    ("DeFiLiban/swapzone-batch/media/19-swapzone-loans-page.png",       None,   "loans"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        page = await ctx.new_page()

        for path, from_c, to_c in SWAPZONE_QUERIES:
            dest = os.path.join(BASE, path)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            try:
                if from_c is None:
                    url = f"https://swapzone.io/{to_c}" if to_c else "https://swapzone.io/"
                else:
                    url = f"https://swapzone.io/exchange?from={from_c}&to={to_c}"
                await page.goto(url, timeout=25000, wait_until="domcontentloaded")
                await page.wait_for_timeout(3500)
                await page.screenshot(path=dest, full_page=True)
                print(f"OK   {path}")
            except Exception as e:
                print(f"FAIL {path} — {e}")

        await browser.close()

asyncio.run(main())
