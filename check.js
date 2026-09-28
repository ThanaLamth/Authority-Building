const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const delay = ms => new Promise(r => setTimeout(r, ms));

const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";

// No proxy for content check -- just see what the CF page says
(async () => {
  const browser = await chromium.launch({ headless: true, args: ["--no-sandbox"] });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("https://rollbit.com", { waitUntil: "domcontentloaded", timeout: 30000 });
  await delay(3000);
  const title = await page.title();
  const body = await page.evaluate(() => document.body.innerText.slice(0, 300));
  console.log("Title:", title);
  console.log("Body:", body);
  await browser.close();
})();
