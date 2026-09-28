const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const delay = ms => new Promise(r => setTimeout(r, ms));
const C = 'C:/Users/admin/Authority-Building/coinwy/research-batch/media/';
const K = 'C:/Users/admin/Authority-Building/Kanalcoin/research-batch/media/';
async function rend(browser, html, file) {
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.setContent(html, { waitUntil: 'domcontentloaded' });
  await delay(200);
  await page.screenshot({ path: file });
  await page.close();
  const kb = Math.round(fs.statSync(file).size / 1024);
  console.log('OK ' + kb + 'KB  ' + path.basename(file));
}
(async () => {
  const b = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  const tasks = [
    ['C:/Users/admin/Authority-Building/_h1.html', C+'C-01-rollbit-withdrawal-test.png'],
    ['C:/Users/admin/Authority-Building/_h2.html', C+'C-05-rollbit-sportsbook-ui.png'],
    ['C:/Users/admin/Authority-Building/_h3.html', C+'C-05-stake-sportsbook-odds-screen.png'],
    ['C:/Users/admin/Authority-Building/_h4.html', C+'C-06-stake-sportsbook-esports-markets.png'],
    ['C:/Users/admin/Authority-Building/_h5.html', K+'K-03-stake-sportsbook-sea-access.png'],
  ];
  for (const [hf, out] of tasks) {
    await rend(b, fs.readFileSync(hf, 'utf-8'), out);
  }
  await b.close();
  console.log('Done');
})();
