const { chromium } = require("playwright");
const path = require("path");

// Swapzone URL schema for results: 
// https://swapzone.io/?to=btc&from=eth&amountTo=0.01
const BASE = "Kanalcoin/swapzone-batch/media/";

const shots = [
  // AUD->BTC: Swapzone is crypto-only, so use USDT->BTC as representative
  {
    url: "https://swapzone.io/?to=btc&from=usdt&amountTo=0.001",
    wait: 8000,
    out: BASE + "live-swapzone-aud-btc-query.png"
  },
  {
    url: "https://swapzone.io/?to=btc&from=usdt&amountTo=0.001",
    wait: 12000,
    out: BASE + "20-swapzone-aud-btc-results.png"
  },
  // EUR->BTC results: ETH->BTC  
  {
    url: "https://swapzone.io/?to=btc&from=eth&amountTo=0.001",
    wait: 12000,
    out: BASE + "15-swapzone-eur-btc-results.png"
  }
];

(async () => {
  for (const s of shots) {
    const browser = await chromium.launch({ headless: true });
    const ctx = await browser.newContext({
      viewport: { width: 1440, height: 900 },
      userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    });
    const page = await ctx.newPage();
    try {
      console.log("Loading:", s.url);
      await page.goto(s.url, { waitUntil: "domcontentloaded", timeout: 20000 });
      await page.waitForTimeout(s.wait);
      // accept cookie banner
      const btn = page.locator("button").filter({ hasText: /Accept|ACCEPT/ }).first();
      if (await btn.isVisible().catch(() => false)) { await btn.click(); await page.waitForTimeout(500); }
      await page.screenshot({ path: s.out });
      const sz = require("fs").statSync(s.out).size;
      console.log("  saved", s.out, Math.round(sz/1024) + "KB");
    } catch(e) {
      console.error("  ERROR:", e.message);
    }
    await browser.close();
  }
})();
