const { chromium } = require("playwright");
const fs = require("fs");
const delay = ms => new Promise(r => setTimeout(r, ms));
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";
const RK = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";

(async () => {
  const browser = await chromium.launch({ headless: false });
  const ctx = await browser.newContext({ userAgent: UA, viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  await page.goto("https://www.bitkub.com/", { waitUntil: "networkidle", timeout: 40000 });
  await delay(5000);
  await page.screenshot({ path: RK+"live-bitkub-homepage.png" });
  const kb = fs.statSync(RK+"live-bitkub-homepage.png").size / 1024;
  console.log(kb.toFixed(0)+"KB");
  await browser.close();
})();
