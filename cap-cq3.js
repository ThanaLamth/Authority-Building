const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch({ headless: true });
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
  });
  const page = await ctx.newPage();
  try {
    // Start at BTC (bypasses Cloudflare), then switch to USDT tab
    console.log("Loading BTC exchange flows first...");
    await page.goto("https://cryptoquant.com/asset/btc/chart/exchange-flows", {
      waitUntil: "networkidle", timeout: 30000
    });
    await page.waitForTimeout(5000);

    // Accept cookies
    const btn = page.locator("button").filter({ hasText: /Accept|OK/ }).first();
    if (await btn.isVisible().catch(() => false)) { await btn.click(); await page.waitForTimeout(500); }

    // Click USDT(ETH) tab
    console.log("Clicking USDT tab...");
    await page.click("text=USDT(ETH)");
    await page.waitForTimeout(6000);
    await page.screenshot({ path: "Coinlive/media/09-cryptoquant-usdt-inflows-2026-07-27.png" });
    console.log("Saved USDT");
  } catch(e) {
    console.error("ERROR: " + e.message);
  }
  await browser.close();
})();
