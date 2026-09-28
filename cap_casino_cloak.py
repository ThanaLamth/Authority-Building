import asyncio, cloakbrowser, pathlib, sys

CU = r"C:\Users\admin\Authority-Building\Coincu\media\casino-oct26"
KN = r"C:\Users\admin\Authority-Building\Kanalcoin\media\casino-oct26"
CP = r"C:\Users\admin\Authority-Building\CCpress\media\casino-oct26"
TT = r"C:\Users\admin\Authority-Building\topkentopnews\media\casino-oct26"

TARGETS = [
    ("https://stake.com/",           CU+r"\live-stake-homepage.png",     12000, "Stake homepage"),
    ("https://stake.com/sports",     CU+r"\live-stake-sports.png",       12000, "Stake sports"),
    ("https://jack.com/",            CU+r"\live-jack-homepage.png",      10000, "Jack.com"),
    ("https://1win.com/",            CU+r"\live-1win-homepage.png",      10000, "1win homepage"),
    ("https://rollblock.io/",        CU+r"\live-rollblock-homepage.png", 12000, "Rollblock"),
    ("https://rollblock.io/staking", TT+r"\live-rollblock-staking.png",  12000, "Rollblock staking"),
    ("https://rollbit.com/",         TT+r"\live-rollbit-homepage.png",   12000, "Rollbit"),
    ("https://stake.com/",           CP+r"\live-stake-homepage.png",     12000, "Stake CCpress"),
]

async def main():
    async with cloakbrowser.AsyncCloakBrowser(headless=True) as browser:
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        for url, savepath, wait_ms, desc in TARGETS:
            try:
                print(f"Capturing: {desc}")
                await page.goto(url, timeout=40000)
                await asyncio.sleep(wait_ms / 1000)
                # dismiss cookie banners
                for sel in ['button:has-text("Accept")', 'button:has-text("I agree")', '#onetrust-accept-btn-handler', 'button:has-text("Got it")']:
                    try:
                        el = await page.query_selector(sel)
                        if el:
                            await el.click()
                            await asyncio.sleep(0.6)
                    except:
                        pass
                await page.screenshot(path=savepath)
                print(f"  OK: {savepath}")
            except Exception as e:
                print(f"  ERROR: {str(e)[:80]}")
            await asyncio.sleep(3)

asyncio.run(main())
