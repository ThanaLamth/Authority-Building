const { chromium } = require("playwright");
const delay = ms => new Promise(r => setTimeout(r, ms));
const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";
const CU = "C:\\Users\\admin\\Authority-Building\\Coincu\\media\\casino-oct26\\";
const KN = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\media\\casino-oct26\\";
const TT = "C:\\Users\\admin\\Authority-Building\\topkentopnews\\media\\casino-oct26\\";

const TARGETS = [
  ["https://stake.com/",      CU+"live-stake-homepage.png",     10000, "Stake.com Coincu"],
  ["https://bc.game/",        CU+"live-bcgame-homepage.png",    11000, "BC.Game Coincu"],
  ["https://1win.app/",       CU+"live-1win-homepage.png",       9000, "1win homepage (.app)"],
  ["https://rollblock.io/",   TT+"live-rollblock-homepage.png", 10000, "Rollblock"],
  ["https://rollbit.com/",    TT+"live-rollbit-homepage.png",   10000, "Rollbit"],
  ["https://stake.com/sports",CU+"live-stake-sports.png",       10000, "Stake sportsbook retry"],
];

(async () => {
  const browser = await chromium.launch({ headless:true, args:["--no-sandbox","--disable-blink-features=AutomationControlled"] });
  for (const [url, savepath, wait, desc] of TARGETS) {
    const ctx = await browser.newContext({ userAgent:UA, viewport:{width:1440,height:900}, locale:"en-US" });
    const page = await ctx.newPage();
    try {
      console.log("Capturing: " + desc);
      await page.goto(url, { timeout:40000, waitUntil:"domcontentloaded" });
      await delay(wait);
      for (const sel of ['button:has-text("Accept")','button:has-text("I agree")','#onetrust-accept-btn-handler']) {
        try { const el = await page.$(sel); if (el) { await el.click(); await delay(500); } } catch(_){}
      }
      await page.screenshot({ path:savepath, fullPage:false });
      console.log("  OK: " + savepath);
    } catch(e) { console.log("  ERROR: " + e.message.split("\n")[0]); }
    await ctx.close();
    await delay(3000);
  }
  await browser.close();
  console.log("Done.");
})();
