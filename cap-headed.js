const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const delay = ms => new Promise(r => setTimeout(r, ms));

const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";

const PROXY = { server: "http://103.82.195.202:20250", username: "vq46", password: "vq46" };
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.72 Safari/537.36";

const TARGETS = [
  ["https://rollbit.com",               C + "C-01-rollbit-withdrawal-test.png",          16000],
  ["https://rollbit.com/sports",        C + "C-05-rollbit-sportsbook-ui.png",            16000],
  ["https://stake.com/sports/football", C + "C-05-stake-sportsbook-odds-screen.png",     18000],
  ["https://stake.com/sports/esports",  C + "C-06-stake-sportsbook-esports-markets.png", 18000],
  ["https://stake.com/sports",          K + "K-03-stake-sportsbook-sea-access.png",      16000],
];

async function shot(browser, url, file, wait) {
  const ctx = await browser.newContext({
    userAgent: UA,
    viewport: { width: 1440, height: 900 },
    locale: "en-US",
    timezoneId: "America/New_York",
  });
  const page = await ctx.newPage();
  await page.addInitScript(() => {
    Object.defineProperty(navigator, "webdriver", { get: () => undefined });
    window.chrome = { runtime: {}, loadTimes: function(){}, csi: function(){}, app: {} };
    Object.defineProperty(navigator, "plugins", { get: () => [1,2,3,4,5] });
    Object.defineProperty(navigator, "languages", { get: () => ["en-US","en"] });
  });
  try {
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
    // Extra long wait for Turnstile to complete
    await delay(wait);
    await page.screenshot({ path: file });
    const kb = Math.round(fs.statSync(file).size / 1024);
    console.log((kb > 50 ? "REAL" : "CF? ") + " " + kb + "KB  " + path.basename(file));
  } catch (e) {
    console.error("ERR  " + path.basename(file) + " -- " + e.message.slice(0,80));
  }
  await ctx.close();
}

(async () => {
  // headed=false but with all stealth patches
  const browser = await chromium.launch({
    channel: "chrome",
    headless: false,   // HEADED -- defeats most Turnstile/CF bot checks
    proxy: PROXY,
    args: [
      "--no-sandbox",
      "--start-maximized",
      "--disable-infobars",
      "--disable-blink-features=AutomationControlled",
    ]
  });
  for (const [url, file, wait] of TARGETS) {
    await shot(browser, url, file, wait);
  }
  await browser.close();
  console.log("Done");
})();
