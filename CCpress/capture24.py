import asyncio
from playwright.async_api import async_playwright
import os

OUT = r"C:\Users\admin\Authority-Building\CCpress\media\2026-07-24"
os.makedirs(OUT, exist_ok=True)

targets = [
    # Art 14 - Influencers
    ("vitalik-ethereum-foundation-2026-07-24.png", "https://ethereum.org/en/foundation/"),
    ("saylor-strategy-bitcoin-2026-07-24.png", "https://www.strategy.com/bitcoin"),
    ("coinbase-newsroom-2026-07-24.png", "https://www.coinbase.com/blog"),
    ("lummis-senate-2026-07-24.png", "https://www.lummis.senate.gov"),
    ("tether-transparency-2026-07-24.png", "https://tether.to/en/transparency/"),
    # Art 15 - VC Firms
    ("a16z-crypto-2026-07-24.png", "https://a16zcrypto.com"),
    ("paradigm-xyz-2026-07-24.png", "https://www.paradigm.xyz"),
    ("coinbase-ventures-2026-07-24.png", "https://www.coinbase.com/ventures"),
    ("electric-capital-devreport-2026-07-24.png", "https://www.developerreport.com"),
    ("haun-ventures-2026-07-24.png", "https://www.haun.co"),
    # Art 16 - Exchanges
    ("coinmarketcap-exchanges-2026-07-24.png", "https://coinmarketcap.com/rankings/exchanges/"),
    ("binance-compliance-2026-07-24.png", "https://www.binance.com/en/support/faq/binance-doj-settlement-detail"),
    ("coinbase-institutional-2026-07-24.png", "https://www.coinbase.com/institutional"),
    ("kraken-home-2026-07-24.png", "https://www.kraken.com"),
    ("okx-home-2026-07-24.png", "https://www.okx.com"),
]

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for fname, url in targets:
            try:
                page = await browser.new_page(viewport={"width": 1440, "height": 900})
                await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                await page.wait_for_timeout(3000)
                out_path = os.path.join(OUT, fname)
                await page.screenshot(path=out_path, full_page=False)
                print(f"OK: {fname}")
                await page.close()
            except Exception as e:
                print(f"FAIL: {fname} -- {str(e)[:80]}")
        await browser.close()

asyncio.run(capture())
