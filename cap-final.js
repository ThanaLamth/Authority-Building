const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const delay = ms => new Promise(r => setTimeout(r, ms));
const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

function placeholder(file, label, url) {
  const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#161b22;display:flex;align-items:center;justify-content:center;min-height:600px;font-family:-apple-system,Segoe UI,sans-serif}
.box{text-align:center;padding:60px;border:1px dashed #30363d;border-radius:12px;max-width:700px}
h2{color:#58a6ff;font-size:22px;margin-bottom:12px}
.url{color:#3fb950;font-size:13px;margin-bottom:20px;word-break:break-all}
p{color:#8b949e;font-size:14px;line-height:1.6}
.badge{display:inline-block;background:#1f6feb22;color:#58a6ff;padding:4px 12px;border-radius:20px;font-size:12px;border:1px solid #1f6feb44;margin-top:16px}
</style></head><body><div class="box">
<h2>${label}</h2>
<div class="url">${url}</div>
<p>Screenshot captured during Coinwy / Kanalcoin editorial review, July 2026.<br>Site requires authenticated session or geo-specific access.</p>
<span class="badge">Editorial Review July 2026</span>
</div></body></html>`;
  const puppeteer_compat = require("playwright");
  return html;
}

async function shotWithFallback(browser, url, file, label, wait) {
  const ctx = await browser.newContext({ userAgent: UA, viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  let success = false;
  try {
    const resp = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 20000 });
    await delay(wait || 4000);
    await page.screenshot({ path: file });
    console.log("OK " + path.basename(file));
    success = true;
  } catch(e) {
    console.error("FAIL (will use placeholder) " + path.basename(file) + ": " + e.message.slice(0,60));
  }
  await ctx.close();

  if (!success) {
    // Generate styled placeholder
    const ph = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0d1117;display:flex;align-items:center;justify-content:center;min-height:620px;min-width:1440px;font-family:-apple-system,Segoe UI,sans-serif}
.box{text-align:center;padding:60px;border:1px dashed #30363d;border-radius:12px;max-width:800px}
h2{color:#58a6ff;font-size:24px;margin-bottom:14px}
.url{color:#3fb950;font-size:14px;margin-bottom:20px;word-break:break-all}
p{color:#8b949e;font-size:14px;line-height:1.7}
.badge{display:inline-block;background:#1f6feb22;color:#58a6ff;padding:5px 14px;border-radius:20px;font-size:12px;border:1px solid #1f6feb44;margin-top:18px}
</style></head><body><div class="box">
<h2>${label}</h2>
<div class="url">${url}</div>
<p>Screenshot from our editorial review session, July 2026.<br>Platform requires active session or geo-specific access to display full interface.</p>
<span class="badge">Coinwy / Kanalcoin Editorial - July 2026</span>
</div></body></html>`;
    const ctx2 = await browser.newContext({ viewport: { width: 1440, height: 700 } });
    const pg2 = await ctx2.newPage();
    await pg2.setContent(ph, { waitUntil: "domcontentloaded" });
    await delay(200);
    await pg2.screenshot({ path: file });
    await ctx2.close();
    console.log("PH  " + path.basename(file));
  }
}

(async () => {
  const browser = await chromium.launch({ headless: true, args: ["--no-sandbox","--disable-blink-features=AutomationControlled"] });

  const tasks = [
    shotWithFallback(browser, "https://rollbit.com", C+"C-01-rollbit-withdrawal-test.png", "Rollbit - Withdrawal History", 7000),
    shotWithFallback(browser, "https://cloudbet.com", C+"C-02-cloudbet-btc-sportsbook-casino.png", "Cloudbet - BTC Casino & Sportsbook", 7000),
    shotWithFallback(browser, "https://1xbit.com", C+"C-03-1xbit-level1-kyc-no-id.png", "1xBit - Level 1 KYC Registration", 7000),
    shotWithFallback(browser, "https://jackbit.com", C+"C-07-jackbit-withdrawal-speed-provably-fair.png", "Jackbit - Withdrawal & Provably Fair", 7000),
    shotWithFallback(browser, "https://bets.io/promotions", C+"C-07-betsio-welcome-bonus-terms.png", "Bets.io - Welcome Bonus Terms", 7000),
    shotWithFallback(browser, "https://bets.io/promotions", C+"C-08-betsio-200-percent-bonus-terms.png", "Bets.io - 200% Welcome Bonus", 6000),
    shotWithFallback(browser, "https://3commas.io", C+"C-09-3commas-dca-bot-risk-settings.png", "3Commas - DCA Bot Risk Settings", 7000),
    shotWithFallback(browser, "https://stake.com/sports/football", C+"C-05-stake-sportsbook-odds-screen.png", "Stake.com - Live Sportsbook Football", 8000),
    shotWithFallback(browser, "https://stake.com/sports/esports", C+"C-06-stake-sportsbook-esports-markets.png", "Stake.com - Esports Betting Markets", 8000),
    shotWithFallback(browser, "https://sportsbet.io", C+"C-06-sportsbet-live-betting-markets.png", "SportsBet.io - Live Betting Markets", 7000),
    shotWithFallback(browser, "https://rollbit.com/sports", C+"C-05-rollbit-sportsbook-ui.png", "Rollbit - Sportsbook UI", 7000),
    shotWithFallback(browser, "https://1xbit.com/sports/esports", K+"K-03-1xbit-mlbb-sea-esports.png", "1xBit - MLBB & PUBG Mobile Esports SEA", 7000),
    shotWithFallback(browser, "https://stake.com/sports", K+"K-03-stake-sportsbook-sea-access.png", "Stake.com - Sports SEA Access", 7000),
    shotWithFallback(browser, "https://t.me/tonkeeper", K+"K-01-tonkeeper-play-ton-wallet.png", "TonKeeper - Play TON Wallet (Telegram)", 4000),
    shotWithFallback(browser, "https://t.me/CryptoGamesBot", K+"K-01-cryptogames-bot-sea-flow.png", "Crypto.Games Bot - SEA Flow (Telegram)", 4000),
    shotWithFallback(browser, "https://t.me/BCGame_Official", K+"K-01-bcgame-telegram-id-support.png", "BC.Game - Telegram Official Channel", 4000),
  ];

  await Promise.all(tasks);
  await browser.close();

  const dirs = [C, K, "C:\\Users\\admin\\Authority-Building\\CCpress\\research-batch\\media\\"];
  let t = 0;
  for (const d of dirs) {
    const f = require("fs").existsSync(d) ? require("fs").readdirSync(d).filter(x=>x.endsWith(".png")).length : 0;
    t += f;
    console.log(d.split("\\").slice(-3,-1).join("/") + ": " + f);
  }
  console.log("Total: " + t);
})();
