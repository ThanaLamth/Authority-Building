import asyncio
from playwright.async_api import async_playwright
import os

BASE = r"C:\Users\admin\Authority-Building"

SHOTS = [
    # 01
    ("coinwy/swapzone-batch/media/01-swapzone-homepage.png",           "https://swapzone.io/"),
    ("coinwy/swapzone-batch/media/01-swapspace-homepage.png",          "https://swapspace.co/"),
    ("coinwy/swapzone-batch/media/01-simpleswap-homepage.png",         "https://simpleswap.io/"),
    ("coinwy/swapzone-batch/media/01-stealthex-homepage.png",          "https://stealthex.io/"),
    # 02
    ("coinwy/swapzone-batch/media/02-binance-direct-swap.png",         "https://www.binance.com/en/convert"),
    # 03
    ("coinwy/swapzone-batch/media/03-simpleswap-flow.png",             "https://simpleswap.io/"),
    ("coinwy/swapzone-batch/media/03-stealthex-flow.png",              "https://stealthex.io/"),
    # 04
    ("coinwy/swapzone-batch/media/04-exolix-fixed-rate.png",           "https://exolix.com/"),
    # 05
    ("coinwy/swapzone-batch/media/05-stealthex-btc-xmr.png",          "https://stealthex.io/"),
    ("coinwy/swapzone-batch/media/05-godex-btc-xmr.png",              "https://godex.io/"),
    # 06
    ("coinwy/swapzone-batch/media/06-changenow-usdt-btc.png",         "https://changenow.io/"),
    # 07
    ("coinwy/swapzone-batch/media/07-swapspace-btc-eth.png",          "https://swapspace.co/"),
    # 08
    ("coinwy/swapzone-batch/media/08-exolix-eth-btc.png",             "https://exolix.com/"),
    # 11
    ("coinwy/swapzone-batch/media/11-changenow-homepage.png",         "https://changenow.io/"),
    ("coinwy/swapzone-batch/media/11-swapzone-partners.png",          "https://swapzone.io/partners"),
    # 12
    ("coinwy/swapzone-batch/media/12-swapspace-homepage.png",         "https://swapspace.co/"),
    # 13
    ("coinwy/swapzone-batch/media/13-exolix-homepage.png",            "https://exolix.com/"),
    ("coinwy/swapzone-batch/media/13-letsexchange-homepage.png",      "https://letsexchange.io/"),
    # 14
    ("Kanalcoin/swapzone-batch/media/14-kucoin-homepage.png",         "https://www.kucoin.com/"),
    # 15
    ("Kanalcoin/swapzone-batch/media/15-changenow-eur-btc.png",       "https://changenow.io/"),
    ("Kanalcoin/swapzone-batch/media/15-kraken-homepage.png",         "https://www.kraken.com/"),
    # 16
    ("Kanalcoin/swapzone-batch/media/16-stealthex-xmr.png",          "https://stealthex.io/"),
    ("Kanalcoin/swapzone-batch/media/16-exolix-xmr.png",             "https://exolix.com/"),
    # 17
    ("Kanalcoin/swapzone-batch/media/17-uniswap-dex.png",            "https://app.uniswap.org/"),
    ("Kanalcoin/swapzone-batch/media/17-binance-cex.png",            "https://www.binance.com/en"),
    # 20
    ("Kanalcoin/swapzone-batch/media/20-coinspot-homepage.png",       "https://www.coinspot.com.au/"),
    ("Kanalcoin/swapzone-batch/media/20-swyftx-homepage.png",        "https://swyftx.com/"),
    ("Kanalcoin/swapzone-batch/media/20-austrac-register.png",       "https://www.austrac.gov.au/business/register-and-re-register"),
    # 18
    ("DeFiLiban/swapzone-batch/media/18-lido-dashboard.png",         "https://lido.fi/"),
    ("DeFiLiban/swapzone-batch/media/18-rocketpool-dashboard.png",   "https://rocketpool.net/"),
    ("DeFiLiban/swapzone-batch/media/18-nexo-earn.png",              "https://nexo.com/earn"),
    # 19
    ("DeFiLiban/swapzone-batch/media/19-youhodler-homepage.png",     "https://www.youhodler.com/"),
    ("DeFiLiban/swapzone-batch/media/19-coinrabbit-loan.png",        "https://coinrabbit.io/"),
    ("DeFiLiban/swapzone-batch/media/19-nexo-loan.png",              "https://nexo.com/borrow"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        page = await ctx.new_page()
        for path, url in SHOTS:
            dest = os.path.join(BASE, path)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            try:
                await page.goto(url, timeout=25000, wait_until="domcontentloaded")
                await page.wait_for_timeout(2500)
                await page.screenshot(path=dest, full_page=True)
                print(f"OK   {path}")
            except Exception as e:
                print(f"FAIL {path} — {e}")
        await browser.close()

asyncio.run(main())
