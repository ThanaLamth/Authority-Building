const { chromium } = require("playwright");
const path = require("path");
const delay = ms => new Promise(r => setTimeout(r, ms));

const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";

const PROXY = { server: "http://103.82.195.202:20250", username: "vq46", password: "vq46" };
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

// Sites that need longer JS challenge resolution
const SLOW = [
  ["https://rollbit.com",              C + "C-01-rollbit-withdrawal-test.png",          12000],
  ["https://rollbit.com/sports",       C + "C-05-rollbit-sportsbook-ui.png",            12000],
  ["https://stake.com/sports/football",C + "C-05-stake-sportsbook-odds-screen.png",     14000],
  ["https://stake.com/sports/esports", C + "C-06-stake-sportsbook-esports-markets.png", 14000],
  ["https://stake.com/sports",         K + "K-03-stake-sportsbook-sea-access.png",      12000],
  ["https://bets.io/promotions",       C + "C-07-betsio-welcome-bonus-terms.png",       12000],
  ["https://bets.io/promotions",       C + "C-08-betsio-200-percent-bonus-terms.png",   10000],
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
  // Mask webdriver property
  await page.addInitScript(() => {
    Object.defineProperty(navigator, "webdriver", { get: () => undefined });
  });
  try {
    // Use networkidle so JS challenges fully resolve
    await page.goto(url, { waitUntil: "networkidle", timeout: 50000 });
    await delay(wait);
    await page.screenshot({ path: file, fullPage: false });
    const kb = Math.round(require("fs").statSync(file).size / 1024);
    const status = kb > 50 ? "REAL" : "CF?";
    console.log(status + " " + kb + "KB  " + path.basename(file));
  } catch (e) {
    console.error("ERR " + path.basename(file) + " -- " + e.message.slice(0, 80));
  }
  await ctx.close();
}

(async () => {
  const browser = await chromium.launch({
    headless: true,
    proxy: PROXY,
    args: ["--no-sandbox","--disable-blink-features=AutomationControlled"]
  });
  // Sequential for CF bypass (parallel can trigger bot detection)
  for (const [url, file, wait] of SLOW) {
    await shot(browser, url, file, wait);
  }
  await browser.close();
})();
