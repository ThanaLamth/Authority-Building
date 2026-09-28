import asyncio
import cloakbrowser
import pathlib

async def main():
    async with cloakbrowser.AsyncCloakBrowser(headless=True) as browser:
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        print("Loading BTC page first to warm up session...")
        await page.goto("https://cryptoquant.com/asset/btc/chart/exchange-flows")
        await asyncio.sleep(8)
        print("Title:", await page.title())
        print("Clicking USDT tab...")
        try:
            await page.click("text=USDT(ETH)", timeout=5000)
            await asyncio.sleep(8)
        except Exception as e:
            print("Click failed:", e)
            # try direct nav
            await page.goto("https://cryptoquant.com/asset/usdt/chart/exchange-flows")
            await asyncio.sleep(10)
        title = await page.title()
        print("Final title:", title)
        path = pathlib.Path("Coinlive/media/09-cryptoquant-usdt-inflows-2026-07-27.png")
        await page.screenshot(path=str(path))
        print("Saved to", path)

asyncio.run(main())
