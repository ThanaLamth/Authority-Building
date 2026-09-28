const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch({ headless: true });
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
  });
  const page = await ctx.newPage();
  try {
    console.log("Capturing USDT exchange flows...");
    await page.goto("https://cryptoquant.com/asset/usdt/chart/exchange-flows", {
      waitUntil: "domcontentloaded",
      timeout: 30000
    });
    await page.waitForTimeout(10000);
    const btn = page.locator("button").filter({ hasText: /Accept|OK/ }).first();
    if (await btn.isVisible().catch(() => false)) await btn.click();
    await page.waitForTimeout(1000);
    await page.screenshot({ path: "Coinlive/media/09-cryptoquant-usdt-inflows-2026-07-27.png" });
    console.log("Saved");
  } catch(e) {
    console.error("ERROR: " + e.message);
  }
  await browser.close();
})();
