import asyncio
from playwright.async_api import async_playwright
import os, time

BASE = r"C:\Users\admin\Authority-Building"

SHOTS = [
    # ── COINWY ──────────────────────────────────────────────────────────────
    # 01
    ("coinwy/swapzone-batch/media/01-swapzone-homepage.png",            "https://swapzone.io/",                                              "full"),
    ("coinwy/swapzone-batch/media/01-swapspace-homepage.png",           "https://swapspace.co/",                                             "full"),
    ("coinwy/swapzone-batch/media/01-simpleswap-homepage.png",          "https://simpleswap.io/",                                            "full"),
    ("coinwy/swapzone-batch/media/01-stealthex-homepage.png",           "https://stealthex.io/",                                             "full"),
    # 02
    ("coinwy/swapzone-batch/media/02-binance-direct-swap.png",          "https://www.binance.com/en/convert",                                "full"),
    # 03
    ("coinwy/swapzone-batch/media/03-simpleswap-flow.png",              "https://simpleswap.io/",                                            "full"),
    ("coinwy/swapzone-batch/media/03-stealthex-flow.png",               "https://stealthex.io/",                                             "full"),
    # 04
    ("coinwy/swapzone-batch/media/04-exolix-fixed-rate.png",            "https://exolix.com/",                                               "full"),
    # 05
    ("coinwy/swapzone-batch/media/05-stealthex-btc-xmr.png",           "https://stealthex.io/",                                             "full"),
    ("coinwy/swapzone-batch/media/05-godex-btc-xmr.png",               "https://godex.io/",                                                 "full"),
    # 06
    ("coinwy/swapzone-batch/media/06-changenow-usdt-btc.png",          "https://changenow.io/",                                             "full"),
    # 07
    ("coinwy/swapzone-batch/media/07-swapspace-btc-eth.png",           "https://swapspace.co/",                                             "full"),
    # 08
    ("coinwy/swapzone-batch/media/08-exolix-eth-btc.png",              "https://exolix.com/",                                               "full"),
    # 10
    ("coinwy/swapzone-batch/media/10-telegram-wallet-ton.png",         "https://telegram.org/blog/payments-2-0-and-co",                     "full"),
    # 11
    ("coinwy/swapzone-batch/media/11-changenow-homepage.png",          "https://changenow.io/",                                             "full"),
    ("coinwy/swapzone-batch/media/11-swapzone-partners.png",           "https://swapzone.io/partners",                                      "full"),
    # 12
    ("coinwy/swapzone-batch/media/12-swapspace-homepage.png",          "https://swapspace.co/",                                             "full"),
    # 13
    ("coinwy/swapzone-batch/media/13-exolix-homepage.png",             "https://exolix.com/",                                               "full"),
    ("coinwy/swapzone-batch/media/13-letsexchange-homepage.png",       "https://letsexchange.io/",                                          "full"),
    # ── KANALCOIN ───────────────────────────────────────────────────────────
    # 14
    ("Kanalcoin/swapzone-batch/media/14-kucoin-homepage.png",          "https://www.kucoin.com/",                                           "full"),
    # 15
    ("Kanalcoin/swapzone-batch/media/15-changenow-eur-btc.png",        "https://changenow.io/",                                             "full"),
    ("Kanalcoin/swapzone-batch/media/15-kraken-homepage.png",          "https://www.kraken.com/",                                           "full"),
    # 16
    ("Kanalcoin/swapzone-batch/media/16-stealthex-xmr.png",           "https://stealthex.io/",                                             "full"),
    ("Kanalcoin/swapzone-batch/media/16-exolix-xmr.png",              "https://exolix.com/",                                               "full"),
    # 17
    ("Kanalcoin/swapzone-batch/media/17-uniswap-dex.png",             "https://app.uniswap.org/",                                          "full"),
    ("Kanalcoin/swapzone-batch/media/17-binance-cex.png",             "https://www.binance.com/en",                                        "full"),
    # 20
    ("Kanalcoin/swapzone-batch/media/20-coinspot-homepage.png",        "https://www.coinspot.com.au/",                                      "full"),
    ("Kanalcoin/swapzone-batch/media/20-swyftx-homepage.png",         "https://swyftx.com/",                                               "full"),
    ("Kanalcoin/swapzone-batch/media/20-austrac-register.png",        "https://www.austrac.gov.au/business/register-and-re-register",      "full"),
    # ── DEFILIBAN ───────────────────────────────────────────────────────────
    # 18
    ("DeFiLiban/swapzone-batch/media/18-lido-dashboard.png",          "https://lido.fi/",                                                  "full"),
    ("DeFiLiban/swapzone-batch/media/18-rocketpool-dashboard.png",    "https://rocketpool.net/",                                           "full"),
    ("DeFiLiban/swapzone-batch/media/18-nexo-earn.png",               "https://nexo.com/earn",                                             "full"),
    # 19
    ("DeFiLiban/swapzone-batch/media/19-youhodler-homepage.png",      "https://www.youhodler.com/",                                        "full"),
    ("DeFiLiban/swapzone-batch/media/19-coinrabbit-loan.png",         "https://coinrabbit.io/",                                            "full"),
    ("DeFiLiban/swapzone-batch/media/19-nexo-loan.png",               "https://nexo.com/borrow",                                           "full"),
]

# Swapzone query shots need special handling (select pair then screenshot)
SWAPZONE_QUERIES = [
    # (filename, from_coin, to_coin, amount_label)
    ("coinwy/swapzone-batch/media/01-swapzone-query-btc-eth.png",      "BTC", "ETH"),
    ("coinwy/swapzone-batch/media/02-swapzone-query-results.png",      "BTC", "ETH"),
    ("coinwy/swapzone-batch/media/03-swapzone-no-registration-flow.png","BTC", "ETH"),
    ("coinwy/swapzone-batch/media/04-swapzone-rate-toggle.png",        "BTC", "ETH"),
    ("coinwy/swapzone-batch/media/05-swapzone-btc-xmr-results.png",    "BTC", "XMR"),
    ("coinwy/swapzone-batch/media/06-swapzone-usdt-btc-results.png",   "USDT","BTC"),
    ("coinwy/swapzone-batch/media/07-swapzone-btc-eth-results.png",    "BTC", "ETH"),
    ("coinwy/swapzone-batch/media/08-swapzone-eth-btc-results.png",    "ETH", "BTC"),
    ("coinwy/swapzone-batch/media/09-swapzone-btc-trx-results.png",    "BTC", "TRX"),
    ("coinwy/swapzone-batch/media/10-swapzone-btc-ton-results.png",    "BTC", "TON"),
    ("coinwy/swapzone-batch/media/11-swapzone-query-with-changenow.png","BTC","ETH"),
    ("coinwy/swapzone-batch/media/12-swapzone-btc-eth-results.png",    "BTC", "ETH"),
    ("coinwy/swapzone-batch/media/12-swapzone-homepage.png",           None,  None),
    ("coinwy/swapzone-batch/media/13-swapzone-homepage.png",           None,  None),
    ("coinwy/swapzone-batch/media/14-swapzone-no-kyc-flow.png",        "BTC", "ETH"),
    ("coinwy/swapzone-batch/media/15-swapzone-eur-btc-results.png",    "EUR", "BTC"),
    ("coinwy/swapzone-batch/media/16-swapzone-eur-xmr-results.png",    "BTC", "XMR"),
    ("coinwy/swapzone-batch/media/17-swapzone-aggregator-results.png", "BTC", "ETH"),
    ("coinwy/swapzone-batch/media/20-swapzone-aud-btc-results.png",    "AUD", "BTC"),
    ("DeFiLiban/swapzone-batch/media/18-swapzone-staking-page.png",   None,  None),
    ("DeFiLiban/swapzone-batch/media/19-swapzone-loans-page.png",     None,  None),
]

async def capture(page, path, url, full=True):
    dest = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        await page.goto(url, timeout=20000, wait_until="domcontentloaded")
        await page.wait_for_timeout(2500)
        await page.screenshot(path=dest, full_page=full)
        print(f"OK   {path}")
    except Exception as e:
        print(f"FAIL {path} — {e}")

async def capture_swapzone(page, path, from_c, to_c):
    dest = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        if from_c is None:
            # homepage or special page
            if "staking" in path:
                url = "https://swapzone.io/staking"
            elif "loan" in path:
                url = "https://swapzone.io/loans"
            else:
                url = "https://swapzone.io/"
            await page.goto(url, timeout=20000, wait_until="domcontentloaded")
            await page.wait_for_timeout(2500)
        else:
            url = f"https://swapzone.io/exchange?from={from_c}&to={to_c}"
            await page.goto(url, timeout=20000, wait_until="domcontentloaded")
            await page.wait_for_timeout(4000)
        await page.screenshot(path=dest, full_page=True)
        print(f"OK   {path}")
    except Exception as e:
        print(f"FAIL {path} — {e}")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1440, "height": 900},
                                        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
        page = await ctx.new_page()

        print(f"\n=== Swapzone queries ({len(SWAPZONE_QUERIES)}) ===")
        for row in SWAPZONE_QUERIES:
            await capture_swapzone(page, row[0], row[1], row[2])

        print(f"\n=== Other sites ({len(SHOTS)}) ===")
        for row in SHOTS:
            await capture(page, row[0], row[1])

        await browser.close()
        print("\nAll done.")

asyncio.run(main())
