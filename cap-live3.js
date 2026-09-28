const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const delay = ms => new Promise(r => setTimeout(r, ms));

const PROXY = { server: "http://103.82.195.202:20250", username: "vq46", password: "vq46" };
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

const SK = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\swapzone-batch\\media\\";
const RC = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const RP = "C:\\Users\\admin\\Authority-Building\\CCpress\\research-batch\\media\\";
const RK = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";

// Re-capture SMALL files with fallbacks + missing ones
const TARGETS = [
  // coinspot failed - try .au directly
  ["https://coinspot.com.au/", SK+"live-coinspot-homepage.png", 8000],
  // coinbase-commerce timed out
  ["https://commerce.coinbase.com/", RC+"live-coinbase-commerce-homepage.png", 8000],
  // cryptogames was SMALL (27KB) - try different page
  ["https://www.cryptogames.com/games", RC+"live-cryptogames-homepage.png", 7000],
  // kalshi was SMALL (12KB) - try with longer wait
  ["https://kalshi.com/markets", RP+"live-kalshi-homepage.png", 9000],
  // bitkub was SMALL (25KB) - try longer wait
  ["https://www.bitkub.com/exchange/THB-BTC", RK+"live-bitkub-homepage.png", 9000],
];

async function shot(browser, url, file, wait) {
  const ctx = await browser.newContext({ userAgent: UA, viewport: { width: 1440, height: 900 }, locale: "en-US", timezoneId: "America/New_York" });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 40000 });
    await delay(wait);
    await page.screenshot({ path: file, fullPage: false });
    const kb = fs.statSync(file).size / 1024;
    console.log((kb < 30 ? "SMALL " : "OK    ") + kb.toFixed(0) + "KB  " + path.basename(file));
  } catch (e) {
    console.error("ERR   " + path.basename(file) + " -- " + e.message.slice(0, 80));
  }
  await ctx.close();
}

(async () => {
  const browser = await chromium.launch({ headless: true, proxy: PROXY });
  for (const [url, file, wait] of TARGETS) {
    await shot(browser, url, file, wait);
  }
  await browser.close();
  console.log("DONE");
})();
