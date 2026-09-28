const { chromium } = require("playwright");
const fs = require("fs");
const delay = ms => new Promise(r => setTimeout(r, ms));

const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

const CL  = "C:\\Users\\admin\\Authority-Building\\Coinlive\\media\\";
const CLP = "C:\\Users\\admin\\Authority-Building\\Coinlineup\\media\\";
const BM  = "C:\\Users\\admin\\Authority-Building\\BitcoinMaximalist\\media\\2026-07-29\\";
const KSW = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\swapzone-batch\\media\\";

[CL, CLP, BM, KSW].forEach(d => fs.mkdirSync(d, { recursive: true }));

const TARGETS = [
  // COINLIVE
  ["https://www.coinglass.com/pro/futures/LiquidationHeatMap", CL+"01-coinglass-btc-heatmap-2026-07-27.png", 10000],
  ["https://studio.glassnode.com/metrics?a=ETH&m=distribution.BalanceExchanges", CL+"02-glassnode-eth-outflows-2026-07-27.png", 10000],
  ["https://www.coinglass.com/LiquidationData", CL+"03-coinglass-btc-liquidations-2026-07-27.png", 9000],
  ["https://www.coinglass.com/OpenInterest", CL+"04-coinglass-oi-dashboard-2026-07-27.png", 9000],
  ["https://cryptoquant.com/asset/btc/chart/exchange-flows/inflow-mean-ma7", CL+"05-cryptoquant-whale-inflows-2026-07-27.png", 10000],
  ["https://www.coinglass.com/", CL+"06-btc-fomc-response-july-2026.png", 9000],
  ["https://www.tradingview.com/chart/?symbol=BINANCE%3AETHUSDT", CL+"07-eth-range-breakout-setup-2026-07-27.png", 12000],
  ["https://www.coinglass.com/FundingRate", CL+"08-coinglass-funding-rates-2026-07-27.png", 9000],
  ["https://cryptoquant.com/asset/usdt/chart/exchange-flows", CL+"09-cryptoquant-usdt-inflows-2026-07-27.png", 10000],
  ["https://farside.co.uk/bitcoin-etf-flow-all-data/", CL+"10-bitcoin-etf-flows-july-2026.png", 9000],
  // COINLINEUP
  ["https://bittensor.com/", CLP+"07-bittensor-home-2026-07-27.png", 8000],
  ["https://dogecoin.com/", CLP+"08-dogecoin-home-2026-07-27.png", 8000],
  ["https://www.coinbase.com/wallet", CLP+"09-coinbase-wallet-2026-07-27.png", 9000],
  ["https://www.coinbase.com/", CLP+"10-coinbase-home-2026-07-27.png", 9000],
  // BITCOINMAXIMALIST
  ["https://app.1inch.io/", BM+"1inch-app-2026-07-29.png", 10000],
  ["https://cow.fi/", BM+"cowprotocol-home-2026-07-29.png", 8000],
  ["https://app.odos.xyz/", BM+"odos-app-2026-07-29.png", 10000],
  // KANALCOIN SWAPZONE-BATCH
  ["https://swapzone.io/", KSW+"live-swapzone-homepage.png", 9000],
  ["https://swapzone.io/?from=BTC&to=XMR", KSW+"14-swapzone-no-kyc-flow.png", 11000],
  ["https://swapzone.io/?from=EUR&to=BTC", KSW+"15-swapzone-eur-btc-results.png", 11000],
  ["https://swapzone.io/?from=EUR&to=XMR", KSW+"16-swapzone-eur-xmr-results.png", 11000],
  ["https://swapzone.io/?from=BTC&to=ETH", KSW+"17-swapzone-aggregator-results.png", 11000],
  ["https://swapzone.io/?from=BTC&to=ETH", KSW+"live-swapzone-btc-eth-query.png", 11000],
  ["https://swapzone.io/?from=AUD&to=BTC", KSW+"20-swapzone-aud-btc-results.png", 11000],
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
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 35000 });
    await delay(wait);
    await page.screenshot({ path: file, fullPage: false });
    const size = fs.statSync(file).size;
    console.log(`OK  ${size.toString().padStart(8)}b  ${require("path").basename(file)}`);
  } catch (e) {
    console.log(`ERR ${require("path").basename(file)}: ${e.message.slice(0,90)}`);
  } finally {
    await ctx.close();
  }
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  for (const [url, file, wait] of TARGETS) {
    process.stdout.write(`> ${require("path").basename(file).padEnd(50)}`);
    await shot(browser, url, file, wait);
  }
  await browser.close();
  console.log("\nAll done.");
})();