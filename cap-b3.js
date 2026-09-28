const { chromium } = require("playwright");
const path = require("path");
const delay = ms => new Promise(r => setTimeout(r, ms));
const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

async function shot(browser, url, file, wait) {
  const ctx = await browser.newContext({ userAgent: UA, viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 40000 });
    await delay(wait || 6000);
    await page.screenshot({ path: file });
    console.log("OK " + path.basename(file));
  } catch(e) { console.error("FAIL " + path.basename(file) + ": " + e.message.slice(0,80)); }
  await ctx.close();
}

(async () => {
  const browser = await chromium.launch({ headless: true, args: ["--no-sandbox","--disable-blink-features=AutomationControlled"] });
  await shot(browser, "https://rollbit.com", C+"C-01-rollbit-withdrawal-test.png", 8000);
  await shot(browser, "https://cloudbet.com", C+"C-02-cloudbet-btc-sportsbook-casino.png", 8000);
  await shot(browser, "https://1xbit.com", C+"C-03-1xbit-level1-kyc-no-id.png", 8000);
  await shot(browser, "https://jackbit.com", C+"C-07-jackbit-withdrawal-speed-provably-fair.png", 8000);
  await shot(browser, "https://bets.io/promotions", C+"C-07-betsio-welcome-bonus-terms.png", 8000);
  await shot(browser, "https://bets.io/promotions", C+"C-08-betsio-200-percent-bonus-terms.png", 6000);
  await shot(browser, "https://3commas.io", C+"C-09-3commas-dca-bot-risk-settings.png", 8000);
  await shot(browser, "https://stake.com/sports/football", C+"C-05-stake-sportsbook-odds-screen.png", 8000);
  await shot(browser, "https://stake.com/sports/esports", C+"C-06-stake-sportsbook-esports-markets.png", 8000);
  await shot(browser, "https://sportsbet.io", C+"C-06-sportsbet-live-betting-markets.png", 7000);
  await shot(browser, "https://rollbit.com/sports", C+"C-05-rollbit-sportsbook-ui.png", 7000);
  await shot(browser, "https://1xbit.com/sports/esports", K+"K-03-1xbit-mlbb-sea-esports.png", 8000);
  await shot(browser, "https://stake.com/sports", K+"K-03-stake-sportsbook-sea-access.png", 7000);
  await shot(browser, "https://t.me/tonkeeper", K+"K-01-tonkeeper-play-ton-wallet.png", 4000);
  await shot(browser, "https://t.me/CryptoGamesBot", K+"K-01-cryptogames-bot-sea-flow.png", 4000);
  await shot(browser, "https://t.me/BCGame_Official", K+"K-01-bcgame-telegram-id-support.png", 4000);
  await browser.close();
  console.log("Done");
})();
