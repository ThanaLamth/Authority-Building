const { chromium } = require('playwright-core');

const CCOUT = 'C:\\\\Users\\\\admin\\\\Authority-Building\\\\CCpress\\\\media\\\\2026-07-29\\\\';
const BMOUT = 'C:\\\\Users\\\\admin\\\\Authority-Building\\\\BitcoinMaximalist\\\\media\\\\2026-07-29\\\\';

const captures = [
  { url: 'https://app.1inch.io', file: CCOUT + '1inch-app-2026-07-29.png' },
  { url: 'https://cow.fi', file: CCOUT + 'cowprotocol-home-2026-07-29.png' },
  { url: 'https://paraswap.io', file: CCOUT + 'paraswap-home-2026-07-29.png' },
  { url: 'https://app.odos.xyz', file: CCOUT + 'odos-app-2026-07-29.png' },
  { url: 'https://app.uniswap.org', file: CCOUT + 'uniswap-x-2026-07-29.png' },
  { url: 'https://jup.ag', file: CCOUT + 'jupiter-app-2026-07-29.png' },
  { url: 'https://li.fi', file: CCOUT + 'lifi-home-2026-07-29.png' },
  { url: 'https://simpleswap.io', file: CCOUT + 'simpleswap-home-2026-07-29.png' },
  { url: 'https://changenow.io', file: CCOUT + 'changenow-home-2026-07-29.png' },
  { url: 'https://stealthex.io', file: CCOUT + 'stealthex-home-2026-07-29.png' },
  { url: 'https://www.coinbase.com', file: CCOUT + 'coinbase-home-2026-07-29.png' },
  { url: 'https://advanced.coinbase.com', file: CCOUT + 'coinbase-advanced-trade-2026-07-29.png' },
  { url: 'https://www.kraken.com', file: CCOUT + 'kraken-home-2026-07-29.png' },
  { url: 'https://exchange.gemini.com', file: CCOUT + 'gemini-activetrader-2026-07-29.png' },
  { url: 'https://www.bitstamp.net', file: CCOUT + 'bitstamp-home-2026-07-29.png' },
  { url: 'https://crypto.com', file: CCOUT + 'cryptocom-home-2026-07-29.png' },
  { url: 'https://www.binance.com/en/fee/schedule', file: CCOUT + 'binance-fee-schedule-2026-07-29.png' },
  { url: 'https://robosats.com', file: BMOUT + 'robosats-home-2026-07-29.png' },
  { url: 'https://bisq.network', file: BMOUT + 'bisq-home-2026-07-29.png' },
  { url: 'https://hodlhodl.com', file: BMOUT + 'hodlhodl-home-2026-07-29.png' },
  { url: 'https://sideshift.ai', file: BMOUT + 'sideshift-home-2026-07-29.png' },
  { url: 'https://docs.1inch.io', file: BMOUT + '1inch-docs-2026-07-29.png' },
  { url: 'https://docs.cow.fi', file: BMOUT + 'cowprotocol-docs-2026-07-29.png' },
  { url: 'https://developers.paraswap.network', file: BMOUT + 'paraswap-docs-2026-07-29.png' },
  { url: 'https://docs.odos.xyz', file: BMOUT + 'odos-docs-2026-07-29.png' },
  { url: 'https://wbtc.network', file: BMOUT + 'wbtc-network-2026-07-29.png' },
];

(async () => {
  const browser = await chromium.launch({ executablePath: 'C:/Users/admin/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe', headless: true });
  for (const { url, file } of captures) {
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
      await page.waitForTimeout(3000);
      await page.screenshot({ path: file, fullPage: false });
      console.log('OK ' + file.split('\\\\').pop());
    } catch (e) {
      console.log('FAIL ' + file.split('\\\\').pop() + ' -- ' + e.message.slice(0, 80));
    } finally {
      await page.close();
    }
  }
  await browser.close();
})();
