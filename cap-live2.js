const { chromium } = require("playwright");
const path = require("path");
const delay = ms => new Promise(r => setTimeout(r, ms));

const PROXY = { server: "http://103.82.195.202:20250", username: "vq46", password: "vq46" };
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

const SW = "C:\\Users\\admin\\Authority-Building\\coinwy\\swapzone-batch\\media\\";
const SK = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\swapzone-batch\\media\\";
const SD = "C:\\Users\\admin\\Authority-Building\\DeFiLiban\\swapzone-batch\\media\\";
const RC = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const RK = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";
const RP = "C:\\Users\\admin\\Authority-Building\\CCpress\\research-batch\\media\\";

const TARGETS = [
  // Missing swapzone batch
  ["https://www.coinspot.com.au/", SK+"live-coinspot-homepage.png", 6000],
  ["https://youhodler.com/", SD+"live-youhodler-homepage.png", 6000],
  // Research batch - casino/betting
  ["https://bc.game/", RC+"live-bcgame-homepage.png", 7000],
  ["https://jackbit.com/", RC+"live-jackbit-homepage.png", 7000],
  ["https://wild.io/", RC+"live-wildio-homepage.png", 7000],
  ["https://bitcasino.io/", RC+"live-bitcasino-homepage.png", 7000],
  ["https://www.cryptogames.com/", RC+"live-cryptogames-homepage.png", 6000],
  ["https://sportsbet.io/", RC+"live-sportsbetio-homepage.png", 7000],
  // AI trading bots
  ["https://3commas.io/", RC+"live-3commas-homepage.png", 6000],
  ["https://www.pionex.com/", RC+"live-pionex-homepage.png", 6000],
  ["https://www.cryptohopper.com/", RC+"live-cryptohopper-homepage.png", 6000],
  ["https://bitsgap.com/", RC+"live-bitsgap-homepage.png", 6000],
  ["https://hummingbot.org/", RC+"live-hummingbot-homepage.png", 6000],
  // Prediction markets
  ["https://polymarket.com/", RP+"live-polymarket-homepage.png", 7000],
  ["https://kalshi.com/", RP+"live-kalshi-homepage.png", 7000],
  ["https://manifold.markets/", RP+"live-manifold-homepage.png", 6000],
  // DeFi/perps
  ["https://dydx.exchange/", RP+"live-dydx-homepage.png", 7000],
  ["https://synthetix.io/", RP+"live-synthetix-homepage.png", 6000],
  ["https://www.drift.trade/", RP+"live-drift-homepage.png", 7000],
  // AI agent crypto
  ["https://elizaos.ai/", RP+"live-elizaos-homepage.png", 6000],
  ["https://www.virtuals.io/", RP+"live-virtuals-homepage.png", 7000],
  ["https://olas.network/", RP+"live-olas-homepage.png", 6000],
  ["https://bittensor.com/", RP+"live-bittensor-homepage.png", 6000],
  // SEA platforms
  ["https://www.indodax.com/", RK+"live-indodax-homepage.png", 6000],
  ["https://www.bitkub.com/", RK+"live-bitkub-homepage.png", 6000],
  ["https://coins.ph/", RK+"live-coinsph-homepage.png", 6000],
  // Payment
  ["https://stripe.com/crypto", RC+"live-stripe-crypto-page.png", 6000],
  ["https://commerce.coinbase.com/", RC+"live-coinbase-commerce-homepage.png", 6000],
];

async function shot(browser, url, file, wait) {
  const ctx = await browser.newContext({ userAgent: UA, viewport: { width: 1440, height: 900 }, locale: "en-US", timezoneId: "America/New_York" });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 40000 });
    await delay(wait);
    await page.screenshot({ path: file, fullPage: false });
    const kb = require("fs").statSync(file).size / 1024;
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
