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

// [url, savepath, wait_ms]
const TARGETS = [
  // === SWAPZONE BATCH LIVE CAPTURES ===
  // Swapzone itself
  ["https://swapzone.io/", SW+"live-swapzone-homepage.png", 7000],
  ["https://swapzone.io/?from=BTC&to=XMR", SW+"live-swapzone-btc-xmr-query.png", 9000],
  ["https://swapzone.io/?from=BTC&to=ETH", SW+"live-swapzone-btc-eth-query.png", 9000],
  ["https://swapzone.io/?from=USDT&to=BTC", SW+"live-swapzone-usdt-btc-query.png", 9000],
  ["https://swapzone.io/?from=ETH&to=BTC", SW+"live-swapzone-eth-btc-query.png", 9000],
  ["https://swapzone.io/?from=BTC&to=TON", SW+"live-swapzone-btc-ton-query.png", 9000],
  ["https://swapzone.io/?from=BTC&to=TRX", SW+"live-swapzone-btc-trx-query.png", 9000],
  ["https://swapzone.io/?from=EUR&to=BTC", SK+"live-swapzone-eur-btc-query.png", 9000],
  ["https://swapzone.io/?from=EUR&to=XMR", SK+"live-swapzone-eur-xmr-query.png", 9000],
  ["https://swapzone.io/?from=AUD&to=BTC", SK+"live-swapzone-aud-btc-query.png", 9000],
  // Partner sites - swapzone batch
  ["https://stealthex.io/", SW+"live-stealthex-homepage.png", 6000],
  ["https://changenow.io/", SW+"live-changenow-homepage.png", 6000],
  ["https://exolix.com/", SW+"live-exolix-homepage.png", 6000],
  ["https://godex.io/", SW+"live-godex-homepage.png", 6000],
  ["https://swapspace.co/", SW+"live-swapspace-homepage.png", 6000],
  ["https://simpleswap.io/", SW+"live-simpleswap-homepage.png", 6000],
  ["https://letsexchange.io/", SW+"live-letsexchange-homepage.png", 6000],
  // AUD/Australia
  ["https://www.coinspot.com.au/", SK+"live-coinspot-homepage.png", 6000],
  ["https://swyftx.com/", SK+"live-swyftx-homepage.png", 6000],
  // DeFiLiban - staking/loan
  ["https://lido.fi/", SD+"live-lido-homepage.png", 7000],
  ["https://rocketpool.net/", SD+"live-rocketpool-homepage.png", 6000],
  ["https://nexo.com/", SD+"live-nexo-homepage.png", 6000],
  ["https://coinrabbit.io/", SD+"live-coinrabbit-homepage.png", 6000],
  ["https://youhodler.com/", SD+"live-youhodler-homepage.png", 6000],
  // === RESEARCH BATCH LIVE CAPTURES ===
  // Crypto casinos / betting
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
  // DeFi / perps / tokenized stocks
  ["https://dydx.exchange/", RP+"live-dydx-homepage.png", 7000],
  ["https://synthetix.io/", RP+"live-synthetix-homepage.png", 6000],
  ["https://www.drift.trade/", RP+"live-drift-homepage.png", 7000],
  // AI agent crypto
  ["https://elizaos.ai/", RP+"live-elizaos-homepage.png", 6000],
  ["https://www.virtuals.io/", RP+"live-virtuals-homepage.png", 7000],
  ["https://olas.network/", RP+"live-olas-homepage.png", 6000],
  ["https://bittensor.com/", RP+"live-bittensor-homepage.png", 6000],
  // SEA platforms (Kanalcoin research)
  ["https://www.indodax.com/", RK+"live-indodax-homepage.png", 6000],
  ["https://www.bitkub.com/", RK+"live-bitkub-homepage.png", 6000],
  ["https://coins.ph/", RK+"live-coinsph-homepage.png", 6000],
  // Payment platforms
  ["https://commerce.coinbase.com/", RC+"live-coinbase-commerce-homepage.png", 6000],
  ["https://stripe.com/crypto", RC+"live-stripe-crypto-page.png", 6000],
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
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
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
