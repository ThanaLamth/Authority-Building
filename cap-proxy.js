const { chromium } = require("playwright");
const path = require("path");
const delay = ms => new Promise(r => setTimeout(r, ms));

const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";

const PROXY = {
  server: "http://103.82.195.202:20250",
  username: "vq46",
  password: "vq46"
};

const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

const TARGETS = [
  ["https://rollbit.com",                      C + "C-01-rollbit-withdrawal-test.png",          7000],
  ["https://rollbit.com/sports",               C + "C-05-rollbit-sportsbook-ui.png",            7000],
  ["https://cloudbet.com",                     C + "C-02-cloudbet-btc-sportsbook-casino.png",   8000],
  ["https://1xbit.com",                        C + "C-03-1xbit-level1-kyc-no-id.png",           7000],
  ["https://1xbit.com/sports/esports",         K + "K-03-1xbit-mlbb-sea-esports.png",           8000],
  ["https://stake.com/sports/football",        C + "C-05-stake-sportsbook-odds-screen.png",     8000],
  ["https://stake.com/sports/esports",         C + "C-06-stake-sportsbook-esports-markets.png", 8000],
  ["https://stake.com/sports",                 K + "K-03-stake-sportsbook-sea-access.png",      7000],
  ["https://sportsbet.io/sports/football",     C + "C-06-sportsbet-live-betting-markets.png",   8000],
  ["https://jackbit.com",                      C + "C-07-jackbit-withdrawal-speed-provably-fair.png", 7000],
  ["https://bets.io/promotions",               C + "C-07-betsio-welcome-bonus-terms.png",       8000],
  ["https://bets.io/promotions",               C + "C-08-betsio-200-percent-bonus-terms.png",   6000],
];

async function shot(browser, url, file, wait) {
  const ctx = await browser.newContext({
    userAgent: UA,
    viewport: { width: 1440, height: 900 },
    locale: "en-US",
    timezoneId: "America/New_York",
  });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 40000 });
    await delay(wait);
    await page.screenshot({ path: file, fullPage: false });
    console.log("OK  " + path.basename(file));
  } catch (e) {
    console.error("ERR " + path.basename(file) + " -- " + e.message.slice(0, 80));
  }
  await ctx.close();
}

(async () => {
  console.log("Launching with US ISP proxy 103.82.195.202:20250...");
  const browser = await chromium.launch({
    headless: true,
    proxy: PROXY,
    args: [
      "--no-sandbox",
      "--disable-blink-features=AutomationControlled",
      "--disable-web-security",
    ]
  });

  // Fire all in parallel -- proxy handles geo, sites should load
  await Promise.all(TARGETS.map(([url, file, wait]) => shot(browser, url, file, wait)));

  await browser.close();

  // Report
  const fs = require("fs");
  const dirs = [C, K];
  let total = 0;
  for (const d of dirs) {
    const files = fs.existsSync(d) ? fs.readdirSync(d).filter(f => f.endsWith(".png")) : [];
    total += files.length;
  }
  console.log("\nDone. Total PNGs: " + total);
})();
