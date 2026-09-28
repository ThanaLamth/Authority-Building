const { chromium } = require("playwright");
const path = require("path");
const delay = ms => new Promise(r => setTimeout(r, ms));
const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";
const P = "C:\\Users\\admin\\Authority-Building\\CCpress\\research-batch\\media\\";

async function shot(page, url, file, wait) {
  try {
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 25000 });
    await delay(wait || 4000);
    await page.screenshot({ path: file, fullPage: false });
    console.log("OK " + path.basename(file));
  } catch(e) { console.error("FAIL " + path.basename(file) + " " + e.message.slice(0,60)); }
}

(async () => {
  const browser = await chromium.launch({ headless: true, args: ["--no-sandbox","--disable-web-security","--lang=en-US"] });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });

  await shot(page, "https://rollbit.com", C+"C-01-rollbit-withdrawal-test.png", 5000);
  await shot(page, "https://mbitcasino.io", C+"C-02-mbit-lightning-network-deposit.png", 5000);
  await shot(page, "https://cloudbet.com", C+"C-02-cloudbet-btc-sportsbook-casino.png", 5000);
  await shot(page, "https://crypto.games", C+"C-03-cryptogames-no-kyc-provably-fair.png", 4000);
  await shot(page, "https://1xbit.com", C+"C-03-1xbit-level1-kyc-no-id.png", 5000);
  await shot(page, "https://jackbit.com", C+"C-07-jackbit-withdrawal-speed-provably-fair.png", 5000);
  await shot(page, "https://bets.io/promotions", C+"C-07-betsio-welcome-bonus-terms.png", 5000);
  await shot(page, "https://bets.io/promotions", C+"C-08-betsio-200-percent-bonus-terms.png", 4000);
  await shot(page, "https://wild.io/promotions", C+"C-08-wildio-no-deposit-free-spins.png", 5000);
  await shot(page, "https://3commas.io", C+"C-09-3commas-dca-bot-risk-settings.png", 5000);

  await page.close();
  await browser.close();
  console.log("Batch 1 done");
})();
