import asyncio, nodriver as uc, sys

CU = r"C:\Users\admin\Authority-Building\Coincu\media\casino-oct26"
KN = r"C:\Users\admin\Authority-Building\Kanalcoin\media\casino-oct26"
CP = r"C:\Users\admin\Authority-Building\CCpress\media\casino-oct26"
TT = r"C:\Users\admin\Authority-Building\topkentopnews\media\casino-oct26"

TARGETS = [
    ("https://stake.com/",           CU+r"\live-stake-homepage.png",     14, "Stake homepage"),
    ("https://stake.com/sports",     CU+r"\live-stake-sports.png",       12, "Stake sports"),
    ("https://jack.com/",            CU+r"\live-jack-homepage.png",      12, "Jack.com"),
    ("https://1win.com/",            CU+r"\live-1win-homepage.png",      12, "1win homepage"),
    ("https://rollblock.io/",        TT+r"\live-rollblock-homepage.png", 14, "Rollblock"),
    ("https://rollbit.com/",         TT+r"\live-rollbit-homepage.png",   14, "Rollbit"),
    ("https://stake.com/",           CP+r"\live-stake-homepage.png",     14, "Stake CCpress"),
]

async def main():
    browser = await uc.start(headless=True)
    for url, savepath, wait_s, desc in TARGETS:
        try:
            print(f"Capturing: {desc}")
            tab = await browser.get(url)
            await asyncio.sleep(wait_s)
            await tab.save_screenshot(savepath)
            print(f"  OK: {savepath}")
        except Exception as e:
            print(f"  ERROR: {str(e)[:80]}")
        await asyncio.sleep(3)
    await browser.stop()

asyncio.run(main())
