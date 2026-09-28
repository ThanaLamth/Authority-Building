const { chromium } = require("playwright");
const delay = ms => new Promise(r => setTimeout(r, ms));

const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";

const CU = "C:\\Users\\admin\\Authority-Building\\Coincu\\media\\casino-oct26\\";
const KN = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\media\\casino-oct26\\";
const CP = "C:\\Users\\admin\\Authority-Building\\CCpress\\media\\casino-oct26\\";
const TT = "C:\\Users\\admin\\Authority-Building\\topkentopnews\\media\\casino-oct26\\";

const TARGETS = [
  ["https://stake.com/",              CU+"live-stake-homepage.png",     9000,  "Stake.com homepage"],
  ["https://bc.game/",                CU+"live-bcgame-homepage.png",    10000, "BC.Game homepage"],
  ["https://1win.com/",               CU+"live-1win-homepage.png",      8000,  "1win homepage"],
  ["https://jack.com/",               CU+"live-jack-homepage.png",      8000,  "Jack.com homepage"],
  ["https://winna.com/",              CU+"live-winna-homepage.png",     8000,  "Winna homepage"],
  ["https://rollblock.io/",           CU+"live-rollblock-homepage.png", 9000,  "Rollblock homepage"],
  ["https://roobet.com/",             KN+"live-roobet-homepage.png",    8000,  "Roobet homepage"],
  ["https://cloudbet.com/",           KN+"live-cloudbet-homepage.png",  9000,  "Cloudbet homepage"],
  ["https://bitstarz.com/",           KN+"live-bitstarz-homepage.png",  8000,  "BitStarz homepage"],
  ["https://rollbit.com/",            TT+"live-rollbit-homepage.png",   9000,  "Rollbit homepage"],
  ["https://stake.com/",              CP+"live-stake-homepage.png",     9000,  "Stake.com CCpress"],
  ["https://bc.game/",                KN+"live-bcgame-homepage.png",    10000, "BC.Game Kanalcoin"],
  ["https://1win.com/sports/",        CU+"live-1win-sports.png",        9000,  "1win sportsbook"],
  ["https://stake.com/sports",        CU+"live-stake-sports.png",       9000,  "Stake sportsbook"],
];

(async () => {
  const browser = await chromium.launch({
    headless: true,
    args: ["--no-sandbox","--disable-setuid-sandbox","--disable-blink-features=AutomationControlled","--disable-web-security"]
  });

  for (const [url, savepath, wait, desc] of TARGETS) {
    const ctx = await browser.newContext({
      userAgent: UA,
      viewport: { width: 1440, height: 900 },
      locale: "en-US",
      ignoreHTTPSErrors: true,
    });
    const page = await ctx.newPage();
    try {
      console.log(`Capturing: ${desc}`);
      await page.goto(url, { timeout: 35000, waitUntil: "domcontentloaded" });
      await delay(wait);
      for (const sel of [
        'button[id*="accept"]','#onetrust-accept-btn-handler',
        '.cc-btn.cc-allow','button:has-text("Accept all")',
        'button:has-text("I agree")','button:has-text("Accept cookies")'
      ]) {
        try { const el = await page.$(sel); if (el) { await el.click(); await delay(500); } } catch(_){}
      }
      await page.screenshot({ path: savepath, fullPage: false });
      console.log(`  OK: ${savepath}`);
    } catch(e) {
      console.log(`  ERROR: ${e.message.split("\n")[0]}`);
    }
    await ctx.close();
    await delay(2000);
  }

  await browser.close();
  console.log("\nDone.");
})();
