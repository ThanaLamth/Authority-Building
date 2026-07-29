const { chromium } = require("playwright");
const path = require("path");
const OUT = "C:\\Users\\admin\\Authority-Building\\CCpress\\media\\2026-07-22\\";

const targets = [
  { file: "ftx-recovery-trust-2026-07-22.png",       url: "https://restructuring.ra.kroll.com/FTX/" },
  { file: "celsius-kroll-creditor-2026-07-22.png",   url: "https://restructuring.ra.kroll.com/Celsius/" },
  { file: "sec-unicoin-charges-2026-07-22.png",      url: "https://www.sec.gov/litigation/litreleases/2025/lr26314" },
  { file: "doj-binance-settlement-2026-07-22.png",   url: "https://www.justice.gov/opa/pr/binance-and-ceo-changpeng-zhao-plead-guilty-federal-charges" },
  { file: "sec-terraform-distribution-2026-07-22.png", url: "https://www.sec.gov/enforcement-litigation/distributions-harmed-investors/sec-v-terraform-labs-pte-ltd-do-hyeong-kwon-no-23-cv-1346-jsr-sdny" },
  { file: "sec-pgi-global-2026-07-22.png",           url: "https://www.sec.gov/newsroom/press-releases/2025/2025-69" },
];

(async () => {
  const browser = await chromium.launch({ headless: true });
  for (const t of targets) {
    try {
      const page = await browser.newPage();
      await page.setViewportSize({ width: 1440, height: 900 });
      await page.goto(t.url, { waitUntil: "domcontentloaded", timeout: 30000 });
      await page.waitForTimeout(3000);
      await page.screenshot({ path: path.join(OUT, t.file), fullPage: false });
      console.log("OK: " + t.file);
      await page.close();
    } catch (e) {
      console.log("FAIL: " + t.file + " -- " + e.message.slice(0, 80));
    }
  }
  await browser.close();
})();
