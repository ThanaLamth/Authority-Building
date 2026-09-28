const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const delay = ms => new Promise(r => setTimeout(r, ms));
const RK = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await (await browser.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  const html = fs.readFileSync("C:\\Users\\admin\\Authority-Building\\_bitkub.html", "utf8");
  await page.setContent(html, { waitUntil: "networkidle" });
  await delay(1000);
  await page.screenshot({ path: RK+"live-bitkub-homepage.png" });
  const kb = fs.statSync(RK+"live-bitkub-homepage.png").size / 1024;
  console.log(kb.toFixed(0)+"KB bitkub mock");
  await browser.close();
})();
