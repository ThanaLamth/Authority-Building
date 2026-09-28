import os, pathlib

BASE = r"C:\Users\admin\Authority-Building"

def ins(anchor, img, alt, cap):
    block = "**Live Screenshot (July 2026)**\nFile: `../media/{img}`\nAlt text: `{alt}`\nCaption: `{cap}`\n\n![{alt}](../media/{img})\n\n*{cap}*\n\n{anchor}".format(img=img, alt=alt, cap=cap, anchor=anchor)
    return (anchor, block)

patches = {
"coinwy\\swapzone-batch\\articles\\01-best-crypto-exchange-aggregators-2026.md": [
    ins("## Ranking scorecard","live-swapzone-homepage.png","Swapzone crypto exchange aggregator homepage July 2026","Swapzone homepage reviewed July 2026 -- queries 18-plus exchanges in real time to surface the best rate."),
],
"coinwy\\swapzone-batch\\articles\\06-usdt-to-btc-best-rate-2026.md": [
    ins("## Comparison Table: 5 USDT to BTC Services","live-swapzone-usdt-btc-query.png","Swapzone USDT to BTC live query July 2026","Swapzone USDT to BTC query reviewed July 2026 -- multiple provider rates shown simultaneously for spread comparison."),
],
"coinwy\\swapzone-batch\\articles\\07-btc-to-eth-exchange-rate-2026.md": [
    ins("## Comparison","live-swapzone-btc-eth-query.png","Swapzone BTC to ETH live query July 2026","Swapzone BTC to ETH query reviewed July 2026 -- provider rates captured at review time."),
],
"coinwy\\swapzone-batch\\articles\\08-eth-to-btc-swap-best-rate.md": [
    ins("## Comparison","live-swapzone-eth-btc-query.png","Swapzone ETH to BTC live query July 2026","Swapzone ETH to BTC query reviewed July 2026 -- provider rates and rate type options at review time."),
],
"coinwy\\swapzone-batch\\articles\\09-btc-to-trx-exchange-2026.md": [
    ins("## Comparison","live-swapzone-btc-trx-query.png","Swapzone BTC to TRX live query July 2026","Swapzone BTC to TRX query reviewed July 2026 -- provider rates and availability at capture time."),
],
"coinwy\\swapzone-batch\\articles\\10-best-ton-exchange-gram-2026.md": [
    ins("## Comparison","live-swapzone-btc-ton-query.png","Swapzone BTC to TON live query July 2026","Swapzone BTC to TON query reviewed July 2026 -- provider rates and availability for the TON pair."),
],
"coinwy\\swapzone-batch\\articles\\11-swapzone-vs-changenow.md": [
    ins("## When Swapzone surfaces a better rate than ChangeNOW","live-swapzone-homepage.png","Swapzone homepage July 2026 for Swapzone vs ChangeNOW comparison","Swapzone homepage reviewed July 2026 -- aggregator vs direct swap comparison."),
    ins("## When ChangeNOW is the right direct choice","live-changenow-homepage.png","ChangeNOW instant swap homepage July 2026","ChangeNOW homepage reviewed July 2026 as part of our Swapzone vs ChangeNOW comparison."),
],
"coinwy\\swapzone-batch\\articles\\12-swapzone-vs-swapspace.md": [
    ins("## Does partner count actually matter?","live-swapzone-homepage.png","Swapzone homepage July 2026 for Swapzone vs SwapSpace comparison","Swapzone homepage reviewed July 2026 as part of our Swapzone vs SwapSpace head-to-head."),
],
"coinwy\\swapzone-batch\\articles\\13-best-changenow-alternatives-2026.md": [
    ins("## Ranking scorecard","live-swapzone-homepage.png","Swapzone top ChangeNOW alternative homepage July 2026","Swapzone homepage reviewed July 2026 -- leading ChangeNOW alternative covering 18-plus exchange partners."),
],
"Kanalcoin\\swapzone-batch\\articles\\15-eur-to-btc-exchange-2026.md": [
    ins("## Ranking scorecard","live-swapzone-eur-btc-query.png","Swapzone EUR to BTC live query July 2026","Swapzone EUR to BTC query reviewed July 2026 -- provider rates for SEPA fiat-to-crypto routes at capture time."),
],
"Kanalcoin\\swapzone-batch\\articles\\16-eur-to-xmr-exchange-2026.md": [
    ins("## Ranking scorecard","live-swapzone-eur-xmr-query.png","Swapzone EUR to XMR live query July 2026","Swapzone EUR to XMR query reviewed July 2026 -- provider availability for fiat-to-Monero route at capture time."),
],
"Kanalcoin\\swapzone-batch\\articles\\17-dex-vs-cex-vs-aggregator-2026.md": [
    ins("## DEX in Southeast Asia: where it works and where it does not","live-swapzone-btc-eth-query.png","Swapzone aggregator querying DEX and CEX providers July 2026","Swapzone aggregator reviewed July 2026 -- bridges DEX and CEX provider rates in a single query interface."),
],
"Kanalcoin\\swapzone-batch\\articles\\20-aud-to-btc-exchange-australia-2026.md": [
    ins("## Ranking scorecard","live-swapzone-aud-btc-query.png","Swapzone AUD to BTC live query July 2026","Swapzone AUD to BTC query reviewed July 2026 -- provider rates for Australian fiat-to-crypto routes."),
],
"DeFiLiban\\swapzone-batch\\articles\\18-best-crypto-staking-platforms-2026.md": [
    ins("## The four staking mechanisms","live-lido-homepage.png","Lido Finance liquid staking homepage July 2026","Lido Finance homepage reviewed July 2026 -- largest liquid staking protocol by TVL, daily stETH yield without lockup."),
],
"DeFiLiban\\swapzone-batch\\articles\\19-best-crypto-loan-platforms-2026.md": [
    ins("## The LTV ratio: the most critical number","live-nexo-homepage.png","Nexo crypto lending platform homepage July 2026","Nexo homepage reviewed July 2026 -- instant crypto-backed credit lines with disclosed LTV ratios and liquidation thresholds."),
],
"coinwy\\research-batch\\articles\\C-01-best-crypto-casinos-2026.md": [
    ins("## Quick Comparison Table","live-bcgame-homepage.png","BC.Game crypto casino homepage July 2026","BC.Game homepage reviewed July 2026 -- one of the highest-volume crypto casinos with BTC, ETH, SOL deposits."),
],
"coinwy\\research-batch\\articles\\C-02-best-bitcoin-casinos-2026.md": [
    ins("## The Bitcoin hold model: why it matters","live-jackbit-homepage.png","Jackbit Bitcoin casino homepage July 2026","Jackbit homepage reviewed July 2026 -- provably fair games, instant BTC withdrawals, no mandatory KYC for standard play."),
],
"coinwy\\research-batch\\articles\\C-03-best-no-kyc-crypto-casinos-2026.md": [
    ins('## What "no-KYC" actually means at a crypto casino',"live-bcgame-homepage.png","BC.Game no-KYC crypto casino homepage July 2026","BC.Game homepage reviewed July 2026 -- no mandatory KYC for crypto deposits and standard gameplay."),
],
"coinwy\\research-batch\\articles\\C-04-best-telegram-casinos-2026.md": [
    ins("## 3 types of Telegram casinos (read this before you pick)","live-bcgame-homepage.png","BC.Game Telegram casino integration July 2026","BC.Game homepage reviewed July 2026 -- Telegram bot active, TON wallet deposits supported."),
],
"coinwy\\research-batch\\articles\\C-05-best-online-betting-platforms-2026.md": [
    ins("## Quick Comparison Table","live-sportsbetio-homepage.png","Sportsbet.io crypto sports betting homepage July 2026","Sportsbet.io homepage reviewed July 2026 -- high-volume crypto sports betting with live markets and instant crypto withdrawals."),
],
"coinwy\\research-batch\\articles\\C-06-best-crypto-sports-betting-2026.md": [
    ins("## Why crypto sportsbooks settle faster","live-sportsbetio-homepage.png","Sportsbet.io live betting markets July 2026","Sportsbet.io homepage reviewed July 2026 -- live in-play betting across major sports, BTC and USDT withdrawals."),
],
"coinwy\\research-batch\\articles\\C-07-best-new-crypto-casinos-2026.md": [
    ins("## The problem with most new casino lists","live-wildio-homepage.png","Wild.io new crypto casino homepage July 2026","Wild.io homepage reviewed July 2026 -- new-generation crypto casino with structured welcome bonus and no-KYC entry."),
],
"coinwy\\research-batch\\articles\\C-08-best-crypto-casino-bonuses-2026.md": [
    ins("## The EV formula every bonus hunter should know","live-jackbit-homepage.png","Jackbit casino bonus structure July 2026","Jackbit homepage reviewed July 2026 -- bonus terms and wagering requirements disclosed upfront, provably fair verification available."),
],
"coinwy\\research-batch\\articles\\C-10-bitmex-bitmart-alternatives-2026.md": [
    ins("## Why users are leaving BitMEX and BitMart","live-3commas-homepage.png","3Commas trading platform July 2026 as BitMEX alternative","3Commas homepage reviewed July 2026 -- recommended tool layer for users migrating from BitMEX or BitMart."),
],
"coinwy\\research-batch\\articles\\C-11-best-stablecoin-payment-platforms-2026.md": [
    ins("## The two things that actually matter","live-stripe-crypto-page.png","Stripe crypto payment page July 2026","Stripe crypto payments page reviewed July 2026 -- USDC on Solana payment rails for merchants."),
],
"Kanalcoin\\research-batch\\articles\\K-01-best-telegram-casinos-sea-2026.md": [
    ins("## Why Telegram casinos work differently for SEA users","live-bcgame-homepage.png","BC.Game Telegram casino for SEA July 2026","BC.Game homepage reviewed July 2026 -- Telegram bot active, accessible from Indonesia Thailand Vietnam Philippines."),
],
"Kanalcoin\\research-batch\\articles\\K-02-best-no-kyc-crypto-casinos-sea-2026.md": [
    ins("## Why KYC matters differently in SEA","live-bcgame-homepage.png","BC.Game no-KYC casino SEA July 2026","BC.Game homepage reviewed July 2026 -- no mandatory KYC, P2P options for IDR, THB, PHP."),
],
"Kanalcoin\\research-batch\\articles\\K-03-best-crypto-sports-betting-sea-2026.md": [
    ins("## What makes crypto sportsbooks better for SEA users","live-sportsbetio-homepage.png","Sportsbet.io sports betting accessible from SEA July 2026","Sportsbet.io homepage reviewed July 2026 -- accessible from Indonesia Thailand Vietnam Philippines, live markets."),
],
"CCpress\\research-batch\\articles\\P-02-polymarket-cftc-prediction-markets-2026.md": [
    ins("## The Polymarket CFTC story","live-polymarket-homepage.png","Polymarket prediction market homepage July 2026","Polymarket homepage reviewed July 2026 -- largest on-chain prediction market by liquidity, US users blocked since 2022 CFTC settlement."),
    ins("## Who filled the gap","live-kalshi-homepage.png","Kalshi CFTC-licensed prediction market July 2026","Kalshi homepage reviewed July 2026 -- only CFTC-designated contract market for event contracts as of July 2026."),
],
"CCpress\\research-batch\\articles\\P-03-tokenized-stock-perps-sec-scrutiny-2026.md": [
    ins("## How tokenized stock perpetuals work","live-dydx-homepage.png","dYdX perpetuals platform after synthetic equity delisting July 2026","dYdX homepage reviewed July 2026 -- delisted most synthetic equity products citing regulatory requirements."),
    ins("## The SEC question","live-synthetix-homepage.png","Synthetix synthetic asset protocol July 2026","Synthetix homepage reviewed July 2026 -- synthetic asset protocol governed by SNX holders without SEC or CFTC registration."),
],
}

errors = []
patched = []
for rel_path, ops in patches.items():
    full_path = os.path.join(BASE, rel_path)
    if not os.path.exists(full_path):
        errors.append("NOT FOUND: " + rel_path)
        continue
    content = pathlib.Path(full_path).read_text(encoding="utf-8")
    original = content
    applied = 0
    skipped_ops = []
    for (old, new) in ops:
        if old in content:
            content = content.replace(old, new, 1)
            applied += 1
        else:
            skipped_ops.append(old[:60])
    if content != original:
        pathlib.Path(full_path).write_text(content, encoding="utf-8")
        patched.append("PATCHED (" + str(applied) + "/" + str(len(ops)) + "): " + rel_path)
    else:
        patched.append("NO CHANGE: " + rel_path)
    for s in skipped_ops:
        errors.append("  SKIP: " + repr(s))
for p in patched:
    print(p)
print("---")
for e in errors:
    print(e)
