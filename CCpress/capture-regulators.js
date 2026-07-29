const { chromium } = require("playwright");

const captures = [
  { url: "https://www.cftc.gov/digitalassets/index.htm", file: "cftc-digital-assets-2026-07-21.png" },
  { url: "https://www.eba.europa.eu/regulation-and-policy/markets-in-crypto-assets-mica", file: "eba-mica-supervision-2026-07-21.png" },
  { url: "https://www.gov.uk/government/organisations/hm-treasury", file: "uk-treasury-financial-services-2026-07-21.png" },
  { url: "https://www.vara.ae/en/licensing/", file: "vara-licensing-portal-2026-07-21.png" },
  { url: "https://www.mas.gov.sg/regulation/digital-payment-token-services", file: "mas-dpt-register-2026-07-21.png" },
  { url: "https://www.sfc.hk/en/Regulatory-functions/Intermediaries/Virtual-assets", file: "hk-sfc-vasp-list-2026-07-21.png" },
  { url: "https://www.congress.gov/search?q=%7B%22congress%22%3A%22119%22%2C%22search%22%3A%22GENIUS+Act%22%7D", file: "congress-genius-act-2026-07-21.png" },
  { url: "https://www.federalreserve.gov/supervisionreg/topics/cryptocurrencies.htm", file: "occ-federal-reserve-crypto-2026-07-21.png" }
];

const OUT = "C:\\Users\\admin\\Authority-Building\\CCpress\\media\\2026-07-21\\";

(async () => {
  const browser = await chromium.launch({ headless: true });
  for (const { url, file } of captures) {
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
    try {
      await page.goto(url, { waitUntil: "domcontentloaded", timeout: 30000 });
      await page.waitForTimeout(3000);
      await page.screenshot({ path: OUT + file, fullPage: false });
      console.log("OK " + file);
    } catch (e) {
      console.log("FAIL " + file + " -- " + e.message.slice(0, 80));
    } finally {
      await page.close();
    }
  }
  await browser.close();
})();
