const { chromium } = require("playwright");
const path = require("path");

const TARGETS = [
  { name: "gamdom-halloween",    url: "https://gamdom.com/promotions",                         file: "gamdom-halloween-promo.png",   wait: 5000 },
  { name: "rollbit-halloween",   url: "https://rollbit.com",                                   file: "rollbit-halloween-promo.png",  wait: 5000 },
  { name: "wildio-halloween",    url: "https://wild.io",                                       file: "wildio-halloween-promo.png",   wait: 5000 },
  { name: "bcgame-halloween",    url: "https://bc.game",                                       file: "bcgame-halloween-promo.png",   wait: 5000 },
  { name: "trustpilot-bcgame",   url: "https://www.trustpilot.com/review/bc.game",             file: "trustpilot-bcgame.png",        wait: 6000 },
  { name: "trustpilot-gamdom",   url: "https://www.trustpilot.com/review/gamdom.com",          file: "trustpilot-gamdom.png",        wait: 6000 },
];

const OUT_DIR = path.join(__dirname, "images");

(async () => {
  const browser = await chromium.launch({ headless: true, args: ["--no-sandbox","--disable-dev-shm-usage"] });
  for (const t of TARGETS) {
    const page = await browser.newPage();
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.setExtraHTTPHeaders({ "Accept-Language": "en-US,en;q=0.9" });
    try {
      console.log("Navigating:", t.url);
      await page.goto(t.url, { timeout: 30000, waitUntil: "domcontentloaded" });
      await page.waitForTimeout(t.wait);
      const outPath = path.join(OUT_DIR, t.file);
      await page.screenshot({ path: outPath, fullPage: false });
      const fs = require("fs");
      const size = fs.statSync(outPath).size;
      console.log("OK", t.name, outPath, size, "bytes");
    } catch (e) {
      console.error("FAIL", t.name, e.message.slice(0, 120));
    }
    await page.close();
  }
  await browser.close();
  console.log("All done.");
})();
