const { chromium } = require("playwright");
const path = require("path");
const delay = ms => new Promise(r => setTimeout(r, ms));

const PROXY = { server: "http://103.82.195.202:20250", username: "vq46", password: "vq46" };
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

const CU  = "C:\\Users\\admin\\Authority-Building\\Coincu\\media\\casino-oct26\\";
const KN  = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\media\\casino-oct26\\";
const CP  = "C:\\Users\\admin\\Authority-Building\\CCpress\\media\\casino-oct26\\";
const CL  = "C:\\Users\\admin\\Authority-Building\\Coinlive\\media\\casino-oct26\\";
const TT  = "C:\\Users\\admin\\Authority-Building\\topkentopnews\\media\\casino-oct26\\";

// [url, savepath, wait_ms, description]
const TARGETS = [
  // === STAKE.COM ===
  ["https://stake.com/", CU+"live-stake-homepage.png", 8000, "Stake.com homepage"],
  ["https://stake.com/sports", CU+"live-stake-sports.png", 8000, "Stake.com sportsbook"],
  ["https://stake.com/casino/games/originals", CU+"live-stake-originals.png", 7000, "Stake Originals games"],

  // === BC.GAME ===
  ["https://bc.game/", KN+"live-bcgame-homepage.png", 9000, "BC.Game homepage"],
  ["https://bc.game/", CU+"live-bcgame-homepage.png", 9000, "BC.Game homepage (Coincu)"],

  // === 1WIN ===
  ["https://1win.com/", CU+"live-1win-homepage.png", 8000, "1win homepage"],
  ["https://1win.com/sports/", CU+"live-1win-sports.png", 8000, "1win sportsbook"],

  // === JACK.COM ===
  ["https://jack.com/", CU+"live-jack-homepage.png", 7000, "Jack.com homepage"],

  // === WINNA ===
  ["https://winna.com/", CU+"live-winna-homepage.png", 7000, "Winna homepage"],

  // === ROLLBLOCK ===
  ["https://rollblock.io/", CU+"live-rollblock-homepage.png", 8000, "Rollblock homepage"],
  ["https://rollblock.io/staking", CU+"live-rollblock-staking.png", 8000, "Rollblock RBLK staking"],

  // === ROOBET ===
  ["https://roobet.com/", KN+"live-roobet-homepage.png", 7000, "Roobet homepage"],

  // === CLOUDBET ===
  ["https://cloudbet.com/", KN+"live-cloudbet-homepage.png", 8000, "Cloudbet homepage"],

  // === BITSTARZ ===
  ["https://bitstarz.com/", KN+"live-bitstarz-homepage.png", 7000, "BitStarz homepage"],

  // For CCpress roundup
  ["https://stake.com/", CP+"live-stake-homepage.png", 8000, "Stake.com for CCpress"],
  ["https://bc.game/", CP+"live-bcgame-homepage.png", 9000, "BC.Game for CCpress"],

  // For Coinlive
  ["https://stake.com/sports", CL+"live-stake-sports.png", 8000, "Stake sportsbook Coinlive"],
  ["https://1win.com/sports/", CL+"live-1win-sports.png", 8000, "1win sportsbook Coinlive"],

  // For tokentopnews (GambleFi tokens)
  ["https://rollblock.io/", TT+"live-rollblock-homepage.png", 8000, "Rollblock for tokentopnews"],
  ["https://rollbit.com/", TT+"live-rollbit-homepage.png", 8000, "Rollbit for tokentopnews"],
  ["https://t.me/tgcasino_bot", TT+"live-tgcasino.png", 7000, "TG.Casino Telegram"],
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
      await page.goto(url, { timeout: 30000, waitUntil: "domcontentloaded" });
      await delay(wait);
      for (const sel of [
        '[id*="cookie"] button','[class*="cookie"] button',
        'button[id*="accept"]','#onetrust-accept-btn-handler',
        '.cc-btn.cc-allow','button:has-text("Accept")',
        'button:has-text("I agree")','button:has-text("Got it")'
      ]) {
        try { const el = await page.$(sel); if (el) { await el.click(); await delay(600); } } catch(_){}
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
