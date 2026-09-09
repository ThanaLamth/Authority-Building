import asyncio
import cloakbrowser
import os

BASE = r"C:\Users\admin\Authority-Building"
CW  = os.path.join(BASE, "coinwy", "changenow-batch", "media")
KN  = os.path.join(BASE, "Kanalcoin", "changenow-batch", "media")
CP  = os.path.join(BASE, "CCpress", "changenow-batch", "media")
DL  = os.path.join(BASE, "DeFiLiban", "changenow-batch", "media")

# (url, filename, folder, wait_sec, description)
TARGETS = [
    # coinwy batch pair pages
    ("https://changenow.io/exchange?from=btc&to=xmr",        "live-changenow-btc-xmr.png",    CW,  10, "BTC to XMR swap"),
    ("https://changenow.io/exchange?from=usdttrc20&to=btc",  "live-changenow-usdt-btc.png",   CW,  10, "USDT to BTC swap"),
    ("https://simpleswap.io/",                                "live-simpleswap-homepage.png",  CW,   7, "SimpleSwap homepage"),
    ("https://changelly.com/",                                "live-changelly-homepage.png",   CW,   8, "Changelly homepage"),
    ("https://stealthex.io/",                                 "live-stealthex-homepage.png",   CW,   7, "StealthEX homepage (coinwy)"),
    # kanalcoin batch pair pages
    ("https://changenow.io/exchange?from=eur&to=btc",         "live-changenow-eur-btc.png",    KN,  10, "EUR to BTC"),
    ("https://changenow.io/buy-crypto",                        "live-changenow-fiat-buy.png",   KN,  10, "Fiat buy crypto page"),
    ("https://changenow.io/exchange?from=eth&to=btc",          "live-changenow-eth-btc.png",    KN,  10, "ETH to BTC"),
    ("https://changenow.io/exchange?from=btc&to=eth",          "live-changenow-btc-eth.png",    KN,  10, "BTC to ETH"),
    ("https://stealthex.io/",                                  "live-stealthex-homepage.png",   KN,   7, "StealthEX homepage (kanalcoin)"),
    # ccpress batch
    ("https://changenow.io/api",                               "live-changenow-api-page.png",   CP,   9, "ChangeNOW API page"),
    ("https://www.trustpilot.com/review/changenow.io",         "live-changenow-trustpilot.png", CP,  12, "ChangeNOW Trustpilot"),
    # defiliban batch
    ("https://changenow.io/exchange?from=btc&to=eth",          "live-changenow-swap-widget.png",DL,  10, "ChangeNOW swap widget (DeFiLiban)"),
    ("https://app.1inch.io/",                                  "live-1inch-dex.png",            DL,  12, "1inch DEX"),
]

async def capture(url, savepath, wait_sec, desc):
    ctx = await cloakbrowser.launch_context_async(
        headless=True,
        viewport={"width": 1440, "height": 900}
    )
    page = await ctx.new_page()
    try:
        print(f"  Capturing: {desc}")
        await page.goto(url, timeout=35000)
        await asyncio.sleep(wait_sec)
        # Dismiss cookie banners
        for sel in ['#onetrust-accept-btn-handler','[id*="cookie"] button',
                    '.cc-btn.cc-allow','button[id*="accept"]']:
            try:
                el = await page.query_selector(sel)
                if el:
                    await el.click()
                    await asyncio.sleep(0.8)
            except:
                pass
        await page.screenshot(path=savepath)
        size = os.path.getsize(savepath)
        print(f"  Saved ({size//1024}KB): {savepath}")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False
    finally:
        await ctx.close()

async def main():
    print("ChangeNOW batch screenshot capture")
    print(f"Total targets: {len(TARGETS)}\n")
    ok = 0
    for url, fname, folder, wait_sec, desc in TARGETS:
        savepath = os.path.join(folder, fname)
        # Skip if file already looks good (>50KB)
        if os.path.exists(savepath) and os.path.getsize(savepath) > 50000:
            print(f"  SKIP (exists): {fname}")
            ok += 1
            continue
        success = await capture(url, savepath, wait_sec, desc)
        if success:
            ok += 1
        await asyncio.sleep(2)
    print(f"\nDone: {ok}/{len(TARGETS)} captures successful.")

asyncio.run(main())
