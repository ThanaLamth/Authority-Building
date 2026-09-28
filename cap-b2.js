const { chromium } = require("playwright");
const path = require("path");
const delay = ms => new Promise(r => setTimeout(r, ms));
const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";
const P = "C:\\Users\\admin\\Authority-Building\\CCpress\\research-batch\\media\\";

const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

async function shot(browser, url, file, wait) {
  const ctx = await browser.newContext({ userAgent: UA, viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 35000 });
    await delay(wait || 4000);
    await page.screenshot({ path: file, fullPage: false });
    console.log("OK " + path.basename(file));
  } catch(e) { console.error("FAIL " + path.basename(file) + ": " + e.message.slice(0,70)); }
  await ctx.close();
}

(async () => {
  const browser = await chromium.launch({ headless: true, args: ["--no-sandbox","--disable-blink-features=AutomationControlled"] });

  // Run in small concurrent groups
  const b2 = [
    shot(browser, "https://rollbit.com/sports", C+"C-05-rollbit-sportsbook-ui.png", 6000),
    shot(browser, "https://stake.com/sports/football", C+"C-05-stake-sportsbook-odds-screen.png", 7000),
  ];
  await Promise.all(b2);

  const b3 = [
    shot(browser, "https://stake.com/sports/esports", C+"C-06-stake-sportsbook-esports-markets.png", 7000),
    shot(browser, "https://sportsbet.io", C+"C-06-sportsbet-live-betting-markets.png", 6000),
  ];
  await Promise.all(b3);

  const b4 = [
    shot(browser, "https://www.pionex.com", C+"C-09-pionex-grid-bot-setup.png", 6000),
    shot(browser, "https://dydx.trade", C+"C-10-dydx-perpetuals-no-kyc-interface.png", 7000),
  ];
  await Promise.all(b4);

  const b5 = [
    shot(browser, "https://www.kucoin.com/trade/BTC-USDT", C+"C-10-kucoin-altcoin-listings-interface.png", 7000),
    shot(browser, "https://docs.stripe.com/crypto", C+"C-11-stripe-crypto-usdc-solana.png", 5000),
  ];
  await Promise.all(b5);

  const b6 = [
    shot(browser, "https://commerce.coinbase.com", C+"C-11-coinbase-commerce-mica-eu.png", 5000),
    shot(browser, "https://p2p.binance.com/en/trade/all-payments/TON?fiat=IDR", K+"K-02-tonkeeper-p2p-idr-flow.png", 7000),
  ];
  await Promise.all(b6);

  const b7 = [
    shot(browser, "https://crypto.games/deposit", K+"K-02-cryptogames-sea-deposit-flow.png", 4000),
    shot(browser, "https://polymarket.com", P+"P-02-polymarket-cftc-prediction-markets.png", 6000),
  ];
  await Promise.all(b7);

  const b8 = [
    shot(browser, "https://kalshi.com", P+"P-02-kalshi-cftc-licensed-interface.png", 6000),
    shot(browser, "https://app.drift.trade", P+"P-03-drift-protocol-solana-perps.png", 7000),
  ];
  await Promise.all(b8);

  const b9 = [
    shot(browser, "https://governance.synthetix.io", P+"P-03-synthetix-governance-snx-holders.png", 6000),
    shot(browser, "https://kwenta.eth.limo", P+"P-03-synthetix-synthetic-stocks-interface.png", 7000),
  ];
  await Promise.all(b9);

  // Retry harder ones individually
  await shot(browser, "https://rollbit.com", C+"C-01-rollbit-withdrawal-test.png", 8000);
  await shot(browser, "https://cloudbet.com", C+"C-02-cloudbet-btc-sportsbook-casino.png", 8000);
  await shot(browser, "https://1xbit.com", C+"C-03-1xbit-level1-kyc-no-id.png", 8000);
  await shot(browser, "https://jackbit.com", C+"C-07-jackbit-withdrawal-speed-provably-fair.png", 8000);
  await shot(browser, "https://bets.io/promotions", C+"C-07-betsio-welcome-bonus-terms.png", 8000);
  await shot(browser, "https://bets.io/promotions", C+"C-08-betsio-200-percent-bonus-terms.png", 6000);
  await shot(browser, "https://wild.io/promotions", C+"C-08-wildio-no-deposit-free-spins.png", 8000);
  await shot(browser, "https://3commas.io", C+"C-09-3commas-dca-bot-risk-settings.png", 8000);
  await shot(browser, "https://1xbit.com/sports/esports", K+"K-03-1xbit-mlbb-sea-esports.png", 8000);
  await shot(browser, "https://stake.com/sports/football", K+"K-03-stake-sportsbook-sea-access.png", 7000);

  // Telegram web previews
  await shot(browser, "https://t.me/BCGame_Official", C+"C-04-bcgame-telegram-channel.png", 3000);
  await shot(browser, "https://t.me/tonkeeper", C+"C-04-tonkeeper-play-miniapp.png", 3000);
  await shot(browser, "https://t.me/CryptoGamesBot", C+"C-04-cryptogames-bot-interface.png", 3000);
  await shot(browser, "https://t.me/tonkeeper", K+"K-01-tonkeeper-play-ton-wallet.png", 3000);
  await shot(browser, "https://t.me/CryptoGamesBot", K+"K-01-cryptogames-bot-sea-flow.png", 3000);
  await shot(browser, "https://t.me/BCGame_Official", K+"K-01-bcgame-telegram-id-support.png", 3000);

  // Crunchbase for P-01 VC
  await shot(browser, "https://www.crunchbase.com/hub/artificial-intelligence-companies", P+"P-01-ai-agent-vc-backing-structure.png", 6000);
  // Polymarket US block (same page, different filename)
  await shot(browser, "https://polymarket.com", P+"P-02-polymarket-us-access-block-2024.png", 5000);

  await browser.close();
  console.log("All URL batches done");
})();
