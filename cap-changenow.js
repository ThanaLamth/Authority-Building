const { chromium } = require("playwright");
const path = require("path");
const delay = ms => new Promise(r => setTimeout(r, ms));

const PROXY = { server: "http://103.82.195.202:20250", username: "vq46", password: "vq46" };
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

const CW  = "C:\\Users\\admin\\Authority-Building\\coinwy\\changenow-batch\\media\\";
const KN  = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\changenow-batch\\media\\";
const CP  = "C:\\Users\\admin\\Authority-Building\\CCpress\\changenow-batch\\media\\";
const DL  = "C:\\Users\\admin\\Authority-Building\\DeFiLiban\\changenow-batch\\media\\";

// [url, savepath, wait_ms, description]
const TARGETS = [
  // === COINWY batch ===
  // Art 01: changenow-vs-swapzone
  ["https://changenow.io/", CW+"live-changenow-homepage.png", 7000, "ChangeNOW homepage"],
  ["https://swapzone.io/", CW+"live-swapzone-homepage.png", 8000, "Swapzone homepage"],
  // Art 04: vs simpleswap
  ["https://simpleswap.io/", CW+"live-simpleswap-homepage.png", 6000, "SimpleSwap homepage"],
  // Art 05: vs changelly
  ["https://changelly.com/", CW+"live-changelly-homepage.png", 7000, "Changelly homepage"],
  // Art 06: vs stealthex
  ["https://stealthex.io/", CW+"live-stealthex-homepage.png", 6000, "StealthEX homepage"],
  // Art 07: BTC to XMR
  ["https://changenow.io/exchange?from=btc&to=xmr", CW+"live-changenow-btc-xmr.png", 9000, "ChangeNOW BTC to XMR"],
  // Art 08: USDT to BTC
  ["https://changenow.io/exchange?from=usdttrc20&to=btc", CW+"live-changenow-usdt-btc.png", 9000, "ChangeNOW USDT to BTC"],

  // === KANALCOIN batch ===
  // Art 09: no-kyc guide — ChangeNOW privacy/no-kyc page
  ["https://changenow.io/", KN+"live-changenow-nokyc.png", 7000, "ChangeNOW homepage (no-KYC article)"],
  // Art 10: EUR to BTC
  ["https://changenow.io/exchange?from=eur&to=btc", KN+"live-changenow-eur-btc.png", 9000, "ChangeNOW EUR to BTC"],
  // Art 11: fiat buy crypto — Buy/Sell tab
  ["https://changenow.io/buy-crypto", KN+"live-changenow-fiat-buy.png", 9000, "ChangeNOW fiat buy crypto"],
  // Art 12: best no-kyc exchange roundup (show ChangeNOW + StealthEX side by side not possible, use ChangeNOW)
  ["https://stealthex.io/", KN+"live-stealthex-homepage.png", 6000, "StealthEX homepage"],
  // Art 13: ETH to BTC
  ["https://changenow.io/exchange?from=eth&to=btc", KN+"live-changenow-eth-btc.png", 9000, "ChangeNOW ETH to BTC"],
  // Art 14: BTC to ETH
  ["https://changenow.io/exchange?from=btc&to=eth", KN+"live-changenow-btc-eth.png", 9000, "ChangeNOW BTC to ETH"],

  // === CCPRESS batch ===
  // Art 15: API review — ChangeNOW API docs page
  ["https://changenow.io/api", CP+"live-changenow-api-page.png", 8000, "ChangeNOW API page"],
  // Art 16: is changenow legit — Trustpilot page
  ["https://www.trustpilot.com/review/changenow.io", CP+"live-changenow-trustpilot.png", 10000, "ChangeNOW Trustpilot page"],

  // === DEFILIBAN batch ===
  // Art 17: how instant swaps work — ChangeNOW swap widget
  ["https://changenow.io/exchange?from=btc&to=eth", DL+"live-changenow-swap-widget.png", 9000, "ChangeNOW swap widget"],
  // Art 18: changenow vs defi — 1inch for comparison
  ["https://app.1inch.io/", DL+"live-1inch-dex.png", 10000, "1inch DEX aggregator"],
];

(async () => {
  const browser = await chromium.launch({
    proxy: PROXY,
    headless: true,
    args: ["--no-sandbox","--disable-setuid-sandbox","--disable-blink-features=AutomationControlled"]
  });

  for (const [url, savepath, wait, desc] of TARGETS) {
    const ctx = await browser.newContext({
      userAgent: UA,
      viewport: { width: 1440, height: 900 },
      locale: "en-US",
    });
    const page = await ctx.newPage();
    try {
      console.log(`Capturing: ${desc}`);
      console.log(`  URL: ${url}`);
      await page.goto(url, { timeout: 30000, waitUntil: "domcontentloaded" });
      await delay(wait);
      // Dismiss cookie banners
      for (const sel of ['[id*="cookie"] button','[class*="cookie"] button','button[id*="accept"]','#onetrust-accept-btn-handler','.cc-btn.cc-allow']) {
        try { const el = await page.$(sel); if (el) { await el.click(); await delay(500); } } catch(_){}
      }
      await page.screenshot({ path: savepath, fullPage: false });
      console.log(`  Saved: ${savepath}`);
    } catch(e) {
      console.log(`  ERROR: ${e.message}`);
    }
    await ctx.close();
    await delay(1500);
  }

  await browser.close();
  console.log("\nAll captures done.");
})();
