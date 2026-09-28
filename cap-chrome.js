const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const delay = ms => new Promise(r => setTimeout(r, ms));

const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";

const PROXY = { server: "http://103.82.195.202:20250", username: "vq46", password: "vq46" };
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.72 Safari/537.36";

const TARGETS = [
  ["https://rollbit.com",               C + "C-01-rollbit-withdrawal-test.png",          14000],
  ["https://rollbit.com/sports",        C + "C-05-rollbit-sportsbook-ui.png",            14000],
  ["https://stake.com/sports/football", C + "C-05-stake-sportsbook-odds-screen.png",     16000],
  ["https://stake.com/sports/esports",  C + "C-06-stake-sportsbook-esports-markets.png", 16000],
  ["https://stake.com/sports",          K + "K-03-stake-sportsbook-sea-access.png",      14000],
];

async function shot(browser, url, file, wait) {
  const ctx = await browser.newContext({
    userAgent: UA,
    viewport: { width: 1440, height: 900 },
    locale: "en-US",
    timezoneId: "America/New_York",
    extraHTTPHeaders: { "Accept-Language": "en-US,en;q=0.9" }
  });
  const page = await ctx.newPage();
  await page.addInitScript(() => {
    Object.defineProperty(navigator, "webdriver", { get: () => undefined });
    window.chrome = { runtime: {} };
  });
  try {
    await page.goto(url, { waitUntil: "networkidle", timeout: 55000 });
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
  // Use system Chrome to bypass Playwright detection
  const browser = await chromium.launch({
    channel: "chrome",
    headless: true,
    proxy: PROXY,
    args: ["--no-sandbox","--disable-blink-features=AutomationControlled","--disable-dev-shm-usage"]
  });
  for (const [url, file, wait] of TARGETS) {
    await shot(browser, url, file, wait);
  }
  await browser.close();
})();
