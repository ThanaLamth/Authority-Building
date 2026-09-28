import asyncio
import cloakbrowser
import pathlib

async def main():
    ctx = await cloakbrowser.launch_context_async(
        headless=True,
        viewport={"width": 1440, "height": 900}
    )
    page = await ctx.new_page()
    print("Loading changenow.io...")
    await page.goto("https://changenow.io/exchange?from=eur&to=btc")
    await asyncio.sleep(8)
    title = await page.title()
    print("Title:", title)
    out = "Kanalcoin/swapzone-batch/media/15-changenow-eur-btc.png"
    await page.screenshot(path=out)
    print("Saved:", out)
    await ctx.close()

asyncio.run(main())
