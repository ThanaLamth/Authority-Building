const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const delay = ms => new Promise(r => setTimeout(r, ms));

const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

const SK = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\swapzone-batch\\media\\";
const RC = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const RP = "C:\\Users\\admin\\Authority-Building\\CCpress\\research-batch\\media\\";
const RK = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";

// No proxy for AU-geo blocked sites, coinbase alternative
const TARGETS = [
  ["https://www.coinbase.com/commerce", RC+"live-coinbase-commerce-homepage.png", 8000, null],
  ["https://coinspot.com.au/", SK+"live-coinspot-homepage.png", 8000, null],
  ["https://kalshi.com/", RP+"live-kalshi-homepage.png", 9000, null],
  ["https://www.bitkub.com/", RK+"live-bitkub-homepage.png", 9000, null],
];

async function shot(browser, url, file, wait) {
  const ctx = await browser.newContext({ userAgent: UA, viewport: { width: 1440, height: 900 }, locale: "en-US" });
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
  const browser = await chromium.launch({ headless: true });
  for (const [url, file, wait] of TARGETS) {
    await shot(browser, url, file, wait);
  }
  await browser.close();
  console.log("DONE");
})();
