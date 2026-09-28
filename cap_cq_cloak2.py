import asyncio
import cloakbrowser
import pathlib

async def main():
    ctx = await cloakbrowser.launch_context_async(
        headless=True,
        viewport={"width": 1440, "height": 900}
    )
    page = await ctx.new_page()
    print("Loading BTC exchange flows to warm session...")
    await page.goto("https://cryptoquant.com/asset/btc/chart/exchange-flows")
    await asyncio.sleep(8)
    print("Title:", await page.title())

    # Click USDT(ETH) tab
    try:
        await page.click("text=USDT(ETH)", timeout=5000)
        await asyncio.sleep(8)
    except Exception as e:
        print("Tab click failed:", e)

    title = await page.title()
    print("Final title:", title)
    out = "Coinlive/media/09-cryptoquant-usdt-inflows-2026-07-27.png"
    await page.screenshot(path=out)
    print("Saved:", out)
    await ctx.close()

asyncio.run(main())
