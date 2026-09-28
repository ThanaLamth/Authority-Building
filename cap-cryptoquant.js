const { chromium } = require("playwright");

const targets = [
  {
    url: "https://cryptoquant.com/asset/btc/chart/exchange-flows",
    out: "Coinlive/media/05-cryptoquant-whale-inflows-2026-07-27.png",
    wait: 8000,
    desc: "BTC exchange flows"
  },
  {
    url: "https://cryptoquant.com/asset/usdt/chart/exchange-flows",
    out: "Coinlive/media/09-cryptoquant-usdt-inflows-2026-07-27.png",
    wait: 8000,
    desc: "USDT exchange flows"
  }
];

(async () => {
  const browser = await chromium.launch({ headless: true });
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
  });

  for (const t of targets) {
    const page = await ctx.newPage();
    try {
      console.log("Capturing " + t.desc + ": " + t.url);
      await page.goto(t.url, { waitUntil: "networkidle", timeout: 30000 });
      await page.waitForTimeout(t.wait);
      const acceptBtn = page.locator("button").filter({ hasText: /Accept|OK/ }).first();
      if (await acceptBtn.isVisible().catch(() => false)) await acceptBtn.click();
      await page.waitForTimeout(1000);
      await page.screenshot({ path: t.out, fullPage: false });
      console.log("  -> saved " + t.out);
    } catch (e) {
      console.error("  ERROR: " + e.message);
    }
    await page.close();
  }

  await browser.close();
})();
