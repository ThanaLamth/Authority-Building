const { chromium } = require("playwright");
const delay = ms => new Promise(r => setTimeout(r, ms));
const C = "C:\\Users\\admin\\Authority-Building\\coinwy\\research-batch\\media\\";
const K = "C:\\Users\\admin\\Authority-Building\\Kanalcoin\\research-batch\\media\\";
const P = "C:\\Users\\admin\\Authority-Building\\CCpress\\research-batch\\media\\";

function diag(title, site, css, body) {
  return `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#0d1117;font-family:-apple-system,Segoe UI,sans-serif;padding:40px;min-width:1280px;color:#e6edf3}
h2{font-size:18px;font-weight:600;margin-bottom:6px}.sub{color:#8b949e;font-size:12px;margin-bottom:28px}${css}
</style></head><body><h2>${title}</h2><div class="sub">${site} - Editorial - July 2026</div>${body}</body></html>`;
}

async function shot(browser, html, file) {
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1400, height: 900 });
  await page.setContent(html, { waitUntil: "domcontentloaded" });
  await delay(200);
  await page.screenshot({ path: file, fullPage: true });
  await page.close();
  console.log("OK " + file.split("\\").pop());
}

(async () => {
  const browser = await chromium.launch({ headless: true, args: ["--no-sandbox"] });

  // C-03 KYC tier diagram
  await shot(browser, diag("Crypto Casino KYC Level Framework","Coinwy",
    `.tier{display:grid;grid-template-columns:120px 1fr 1fr;gap:1px;background:#30363d;border:1px solid #30363d;border-radius:8px;overflow:hidden;margin-bottom:10px;font-size:13px}
.tier>div{padding:14px 16px;background:#161b22}.tier .label{background:#21262d;font-weight:700;font-size:14px;display:flex;align-items:center;gap:8px}
.l0{color:#3fb950}.l1{color:#d29922}.l2{color:#f0883e}.l3{color:#f85149}
.head{color:#8b949e;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.5px}.plat{color:#79c0ff;font-size:12px;margin-top:6px}`,
    `<div class="tier"><div class="label l0">Level 0</div><div><div class="head">What it means</div>Wallet address only - no email, no name, no ID at any point</div><div><div class="head">Platforms (July 2026)</div><div class="plat">Rollbit - Metaspins - Betplay.io - Duelbits - BC.Game (below $10k threshold)</div></div></div>
<div class="tier"><div class="label l1">Level 1</div><div><div class="head">What it means</div>Email required at registration; photo ID triggered at withdrawal threshold ($3k-$10k)</div><div><div class="head">Platforms</div><div class="plat">Stake.com - FortuneJack - Mystake - mBit Casino - 7Bit Casino - 1xBit</div></div></div>
<div class="tier"><div class="label l2">Level 2</div><div><div class="head">What it means</div>Photo ID + proof of address required before first withdrawal (regardless of amount)</div><div><div class="head">Platforms</div><div class="plat">Cloudbet - BitStarz - Punt Casino</div></div></div>
<div class="tier"><div class="label l3">Level 3</div><div><div class="head">What it means</div>Full KYC from first deposit - rare in crypto casinos, common in fiat-primary operators</div><div><div class="head">Platforms</div><div class="plat">Not recommended - none in our July 2026 review list</div></div></div>`
  ), C + "C-03-kyc-tier-comparison-crypto-casinos.png");

  // C-04 Telegram types diagram
  await shot(browser, diag("Three Types of Telegram Casinos","Coinwy",
    `.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.card{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:20px}
.card h3{color:#58a6ff;font-size:14px;margin-bottom:10px;font-weight:600}
.type{font-size:11px;color:#8b949e;text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px;border-bottom:1px solid #21262d;padding-bottom:8px}
.row{display:flex;justify-content:space-between;margin-bottom:7px;font-size:12.5px}
.lbl{color:#8b949e;min-width:100px}.val{color:#e6edf3;text-align:right;max-width:160px}
.green{color:#3fb950}.yellow{color:#d29922}`,
    `<div class="grid">
<div class="card"><div class="type">Type A</div><h3>Bot Casino</h3>
<div class="row"><span class="lbl">How it works</span><span class="val">Chat commands in Telegram DM</span></div>
<div class="row"><span class="lbl">Games</span><span class="val">Dice, crash, coin flip</span></div>
<div class="row"><span class="lbl">KYC</span><span class="val green">None</span></div>
<div class="row"><span class="lbl">Settlement</span><span class="val">BTC/ETH/SOL on-chain</span></div>
<div class="row"><span class="lbl">Examples</span><span class="val">Crypto.Games Bot, Satoshi Dice</span></div>
<div class="row"><span class="lbl">Provably fair</span><span class="val green">Yes - hash-verified</span></div></div>
<div class="card"><div class="type">Type B</div><h3>TON Mini-App</h3>
<div class="row"><span class="lbl">How it works</span><span class="val">Opens in Telegram browser layer</span></div>
<div class="row"><span class="lbl">Games</span><span class="val">Slots, crash, roulette</span></div>
<div class="row"><span class="lbl">KYC</span><span class="val green">None - wallet-only</span></div>
<div class="row"><span class="lbl">Settlement</span><span class="val">TON token, fast on-chain</span></div>
<div class="row"><span class="lbl">Examples</span><span class="val">TonKeeper Play, TON Games</span></div>
<div class="row"><span class="lbl">Provably fair</span><span class="val yellow">Partial</span></div></div>
<div class="card"><div class="type">Type C</div><h3>External Integration</h3>
<div class="row"><span class="lbl">How it works</span><span class="val">Telegram channel links to external site</span></div>
<div class="row"><span class="lbl">Games</span><span class="val">Full casino library</span></div>
<div class="row"><span class="lbl">KYC</span><span class="val yellow">Level 0-1</span></div>
<div class="row"><span class="lbl">Settlement</span><span class="val">Multi-chain BTC/ETH/TON</span></div>
<div class="row"><span class="lbl">Examples</span><span class="val">BC.Game, Rollbit, Stake</span></div>
<div class="row"><span class="lbl">Provably fair</span><span class="val green">Yes - on external site</span></div></div></div>`
  ), C + "C-04-telegram-casino-types-comparison.png");

  // P-01 AI power map
  await shot(browser, diag("AI Agent Crypto - Power Map 2026","CCpress",
    `.layer{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:20px;margin-bottom:14px}
.layer-hdr{display:flex;align-items:center;gap:10px;margin-bottom:14px}.layer-hdr h3{font-size:14px;font-weight:600}
.dot{width:10px;height:10px;border-radius:50%}.infra{background:#1f6feb}.token{background:#d29922}.proto{background:#3fb950}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.cell{background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:12px}
.cell .name{color:#79c0ff;font-weight:600;font-size:12.5px;margin-bottom:6px}
.cell .detail{color:#8b949e;font-size:11.5px;line-height:1.5}
.cell .control{margin-top:8px;font-size:11px;color:#d29922;border-top:1px solid #21262d;padding-top:6px}`,
    `<div class="layer"><div class="layer-hdr"><div class="dot infra"></div><h3>Layer 1 - Infrastructure (Cloud + Compute)</h3></div>
<div class="cols"><div class="cell"><div class="name">AWS/GCP/Azure</div><div class="detail">Runs inference workloads for Fetch.ai, Autonolas, ElizaOS agents</div><div class="control">Control: Traditional tech giants</div></div>
<div class="cell"><div class="name">Akash Network</div><div class="detail">Decentralized GPU marketplace for AI agent inference</div><div class="control">Control: AKT token holders via governance</div></div>
<div class="cell"><div class="name">Render Network</div><div class="detail">GPU rendering + AI workloads, Solana-based</div><div class="control">Control: RNDR token holders</div></div></div></div>
<div class="layer"><div class="layer-hdr"><div class="dot token"></div><h3>Layer 2 - Token + Treasury</h3></div>
<div class="cols"><div class="cell"><div class="name">Fetch.ai (FET to ASI)</div><div class="detail">Merged into ASI Alliance. VC: Outlier Ventures, Binance Labs. Token: ASI</div><div class="control">Control: ASI Alliance multisig + VC allocation locks</div></div>
<div class="cell"><div class="name">Autonolas (OLAS)</div><div class="detail">On-chain agent coordination protocol. VC: Coinfund, Fabric</div><div class="control">Control: OLAS governance + core team multisig</div></div>
<div class="cell"><div class="name">ElizaOS / ai16z</div><div class="detail">Open-source agent framework, ai16z DAO treasury</div><div class="control">Control: ai16z DAO - concentrated holder risk</div></div></div></div>
<div class="layer"><div class="layer-hdr"><div class="dot proto"></div><h3>Layer 3 - Autonomous Protocol (On-chain Actions)</h3></div>
<div class="cols"><div class="cell"><div class="name">Agent wallets</div><div class="detail">AI agents hold and transact crypto autonomously - admin key disclosure critical</div><div class="control">Control: Smart contract owner / upgradeability</div></div>
<div class="cell"><div class="name">Cross-chain bridges</div><div class="detail">Agents bridge assets via Wormhole, LayerZero - adds bridge risk layer</div><div class="control">Control: Bridge multisig operators</div></div>
<div class="cell"><div class="name">Governance votes</div><div class="detail">Some agents vote in DAOs autonomously - raises Sybil and collusion questions</div><div class="control">Control: Token holder quorum - varies by protocol</div></div></div></div>`
  ), P + "P-01-ai-agent-crypto-power-map.png");

  await browser.close();
  console.log("Diagram renders done");
})();
