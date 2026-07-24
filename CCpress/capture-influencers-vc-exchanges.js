const { chromium } = require("playwright");
const path = require("path");
const OUT = "C:\\Users\\admin\\Authority-Building\\CCpress\\media\\2026-07-24\\";

const targets = [
  // Art 14 - Influencers
  { file: "vitalik-ethereum-foundation-2026-07-24.png", url: "https://ethereum.org/en/foundation/" },
  { file: "saylor-strategy-bitcoin-2026-07-24.png", url: "https://www.strategy.com/bitcoin" },
  { file: "coinbase-armstrong-newsroom-2026-07-24.png", url: "https://www.coinbase.com/blog" },
  { file: "lummis-senate-bitcoin-caucus-2026-07-24.png", url: "https://www.lummis.senate.gov" },
  { file: "tether-ardoino-transparency-2026-07-24.png", url: "https://tether.to/en/transparency/" },

  // Art 15 - VC Firms
  { file: "a16z-crypto-portfolio-2026-07-24.png", url: "https://a16zcrypto.com" },
  { file: "paradigm-portfolio-2026-07-24.png", url: "https://www.paradigm.xyz" },
  { file: "coinbase-ventures-2026-07-24.png", url: "https://www.coinbase.com/ventures" },
  { file: "electric-capital-dev-report-2026-07-24.png", url: "https://www.developerreport.com" },
  { file: "haun-ventures-2026-07-24.png", url: "https://www.haun.co" },

  // Art 16 - Exchanges
  { file: "binance-compliance-2026-07-24.png", url: "https://www.binance.com/en/blog/compliance" },
  { file: "coinbase-institutional-2026-07-24.png", url: "https://www.coinbase.com/institutional" },
  { file: "coinmarketcap-exchanges-2026-07-24.png", url: "https://coinmarketcap.com/rankings/exchanges/" },
  { file: "kraken-europe-2026-07-24.png", url: "https://www.kraken.com/en-eu" },
  { file: "okx-derivatives-2026-07-24.png", url: "https://www.okx.com/markets/futures" },
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
