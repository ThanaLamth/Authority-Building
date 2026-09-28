import os, pathlib

BASE = r"C:\Users\admin\Authority-Building"

patches = {}

patches[r"coinwy\swapzone-batch\articles\01-best-crypto-exchange-aggregators-2026.md"] = [
    (
        "one query, rates from 10 to 20-plus providers, in real time.\n\nThe best crypto exchange aggregators",
        "one query, rates from 10 to 20-plus providers, in real time.\n\n**Live Screenshot — Swapzone Homepage (July 2026)**\nFile: `../media/live-swapzone-homepage.png`\nAlt text: `Swapzone crypto exchange aggregator homepage showing live query interface, July 2026`\nCaption: `Swapzone homepage reviewed in July 2026 — queries 18-plus partner exchanges in real time to surface the best rate across providers.`\n\n![Swapzone crypto exchange aggregator homepage showing live query interface, July 2026](../media/live-swapzone-homepage.png)\n\n*Swapzone homepage reviewed in July 2026.*\n\nThe best crypto exchange aggregators"
    ),
]
patches[r"coinwy\swapzone-batch\articles\02-crypto-exchange-aggregator-vs-regular-exchange.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone BTC to ETH Query vs Single Exchange (July 2026)**\nFile: `../media/live-swapzone-btc-eth-query.png`\nAlt text: `Swapzone BTC to ETH query showing multiple provider rates simultaneously, July 2026`\nCaption: `Swapzone BTC to ETH query reviewed in July 2026 — competing provider rates shown simultaneously, the core advantage over going direct to a single exchange.`\n\n![Swapzone BTC to ETH query showing multiple provider rates simultaneously, July 2026](../media/live-swapzone-btc-eth-query.png)\n\n*Swapzone BTC to ETH query, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\03-best-instant-crypto-swap-no-registration.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone No-Registration Flow (July 2026)**\nFile: `../media/live-swapzone-homepage.png`\nAlt text: `Swapzone no-account swap interface showing instant crypto swap without registration, July 2026`\nCaption: `Swapzone swap interface reviewed in July 2026 — no account, no email, no KYC required to initiate a swap at the aggregator level.`\n\n![Swapzone no-account swap interface showing instant crypto swap without registration, July 2026](../media/live-swapzone-homepage.png)\n\n*Swapzone no-registration swap flow, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\04-fixed-rate-vs-floating-rate-crypto-swap.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone Rate Type Toggle (July 2026)**\nFile: `../media/live-swapzone-btc-eth-query.png`\nAlt text: `Swapzone BTC to ETH query showing fixed and floating rate toggle options across providers, July 2026`\nCaption: `Swapzone rate type options reviewed in July 2026 — fixed and floating rate providers shown side by side for the same pair, enabling direct comparison.`\n\n![Swapzone BTC to ETH query showing fixed and floating rate toggle options across providers, July 2026](../media/live-swapzone-btc-eth-query.png)\n\n*Swapzone fixed vs floating rate toggle, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\05-btc-to-xmr-exchange-2026.md"] = [
    (
        "Note on speed: XMR requires",
        "**Live Screenshot — Swapzone BTC to XMR Live Query (July 2026)**\nFile: `../media/live-swapzone-btc-xmr-query.png`\nAlt text: `Swapzone BTC to XMR live query results showing provider rates and availability, July 2026`\nCaption: `Swapzone BTC to XMR live query captured July 2026 — provider availability and rates at time of capture. Run your own query to verify current conditions.`\n\n![Swapzone BTC to XMR live query results showing provider rates and availability, July 2026](../media/live-swapzone-btc-xmr-query.png)\n\n*Swapzone BTC to XMR live query, July 2026.*\n\nNote on speed: XMR requires"
    ),
    ("StealthEX: Our Pick for Large Amounts No KYC\n\nStealthEX offers", "StealthEX: Our Pick for Large Amounts No KYC\n\n[StealthEX](https://stealthex.io/) offers"),
    ("Exolix: Our Pick for Fixed Rate Guarantee\n\nExolix is", "Exolix: Our Pick for Fixed Rate Guarantee\n\n[Exolix](https://exolix.com/) is"),
    ("Godex: Our Pick for Floating Rate Without Account\n\nGodex operates", "Godex: Our Pick for Floating Rate Without Account\n\n[Godex](https://godex.io/) operates"),
    ("SideShift: Our Pick If You Only Have BTC and Need Basic XMR\n\nSideShift requires", "SideShift: Our Pick If You Only Have BTC and Need Basic XMR\n\n[SideShift](https://sideshift.ai/) requires"),
]
patches[r"coinwy\swapzone-batch\articles\06-usdt-to-btc-best-rate-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone USDT to BTC Query (July 2026)**\nFile: `../media/live-swapzone-usdt-btc-query.png`\nAlt text: `Swapzone USDT to BTC live query showing competing provider rates and spread, July 2026`\nCaption: `Swapzone USDT to BTC query reviewed in July 2026 — rates from multiple providers shown simultaneously for spread comparison.`\n\n![Swapzone USDT to BTC live query showing competing provider rates and spread, July 2026](../media/live-swapzone-usdt-btc-query.png)\n\n*Swapzone USDT to BTC query, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\07-btc-to-eth-exchange-rate-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone BTC to ETH Query (July 2026)**\nFile: `../media/live-swapzone-btc-eth-query.png`\nAlt text: `Swapzone BTC to ETH live query results showing provider rates, July 2026`\nCaption: `Swapzone BTC to ETH query reviewed in July 2026 — rates and provider availability shown at time of capture.`\n\n![Swapzone BTC to ETH live query results showing provider rates, July 2026](../media/live-swapzone-btc-eth-query.png)\n\n*Swapzone BTC to ETH query, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\08-eth-to-btc-swap-best-rate.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone ETH to BTC Query (July 2026)**\nFile: `../media/live-swapzone-eth-btc-query.png`\nAlt text: `Swapzone ETH to BTC live query comparing provider rates and rate type options, July 2026`\nCaption: `Swapzone ETH to BTC query reviewed in July 2026 — provider rates and fixed vs floating options captured at review time.`\n\n![Swapzone ETH to BTC live query comparing provider rates and rate type options, July 2026](../media/live-swapzone-eth-btc-query.png)\n\n*Swapzone ETH to BTC query, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\09-btc-to-trx-exchange-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone BTC to TRX Query (July 2026)**\nFile: `../media/live-swapzone-btc-trx-query.png`\nAlt text: `Swapzone BTC to TRX live query showing provider availability and rates, July 2026`\nCaption: `Swapzone BTC to TRX query reviewed in July 2026 — provider rates and availability at time of capture.`\n\n![Swapzone BTC to TRX live query showing provider availability and rates, July 2026](../media/live-swapzone-btc-trx-query.png)\n\n*Swapzone BTC to TRX query, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\10-best-ton-exchange-gram-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone BTC to TON Query (July 2026)**\nFile: `../media/live-swapzone-btc-ton-query.png`\nAlt text: `Swapzone BTC to TON live query results showing provider rates and TON pair availability, July 2026`\nCaption: `Swapzone BTC to TON query reviewed in July 2026 — rates and provider availability for the TON pair at time of capture.`\n\n![Swapzone BTC to TON live query results showing provider rates and TON pair availability, July 2026](../media/live-swapzone-btc-ton-query.png)\n\n*Swapzone BTC to TON query, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\11-swapzone-vs-changenow.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone Homepage (July 2026)**\nFile: `../media/live-swapzone-homepage.png`\nAlt text: `Swapzone homepage captured July 2026 for this Swapzone vs ChangeNOW comparison`\nCaption: `Swapzone homepage reviewed in July 2026 as part of our head-to-head comparison with ChangeNOW — aggregator model and partner network.`\n\n![Swapzone homepage captured July 2026 for this Swapzone vs ChangeNOW comparison](../media/live-swapzone-homepage.png)\n\n*Swapzone homepage, July 2026.*\n\n**Live Screenshot — ChangeNOW Homepage (July 2026)**\nFile: `../media/live-changenow-homepage.png`\nAlt text: `ChangeNOW instant crypto swap homepage captured July 2026 for head-to-head comparison with Swapzone`\nCaption: `ChangeNOW homepage reviewed in July 2026 as part of our Swapzone vs ChangeNOW comparison — instant swap interface and coin selection.`\n\n![ChangeNOW instant crypto swap homepage captured July 2026 for head-to-head comparison with Swapzone](../media/live-changenow-homepage.png)\n\n*ChangeNOW homepage, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\12-swapzone-vs-swapspace.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone Homepage (July 2026)**\nFile: `../media/live-swapzone-homepage.png`\nAlt text: `Swapzone homepage captured July 2026 for Swapzone vs SwapSpace comparison`\nCaption: `Swapzone homepage reviewed in July 2026 as part of our Swapzone vs SwapSpace comparison.`\n\n![Swapzone homepage captured July 2026 for Swapzone vs SwapSpace comparison](../media/live-swapzone-homepage.png)\n\n*Swapzone homepage, July 2026.*\n\n**Live Screenshot — SwapSpace Homepage (July 2026)**\nFile: `../media/live-swapspace-homepage.png`\nAlt text: `SwapSpace crypto exchange aggregator homepage captured July 2026 for comparison with Swapzone`\nCaption: `SwapSpace homepage reviewed in July 2026 as part of our Swapzone vs SwapSpace comparison — partner count and coin coverage.`\n\n![SwapSpace crypto exchange aggregator homepage captured July 2026 for comparison with Swapzone](../media/live-swapspace-homepage.png)\n\n*SwapSpace homepage, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\swapzone-batch\articles\13-best-changenow-alternatives-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone as Top ChangeNOW Alternative (July 2026)**\nFile: `../media/live-swapzone-homepage.png`\nAlt text: `Swapzone homepage reviewed July 2026 as the leading ChangeNOW alternative for crypto exchange aggregation`\nCaption: `Swapzone homepage reviewed in July 2026 — the leading ChangeNOW alternative, covering 18-plus partner exchanges for real-time rate comparison.`\n\n![Swapzone homepage reviewed July 2026 as the leading ChangeNOW alternative for crypto exchange aggregation](../media/live-swapzone-homepage.png)\n\n*Swapzone homepage, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"Kanalcoin\swapzone-batch\articles\14-no-kyc-crypto-exchanges-2026.md"] = [
    (
        "[Swapzone requires no account, no email, no KYC",
        "**Live Screenshot — Swapzone No-KYC Entry Flow (July 2026)**\nFile: `../media/live-swapzone-homepage.png`\nAlt text: `Swapzone homepage July 2026 showing no registration or KYC required to initiate a swap from Indonesia Thailand Philippines`\nCaption: `Swapzone homepage reviewed in July 2026 — no account, no email, no KYC required. Accessible without geo-restriction from Indonesia, Thailand, and the Philippines.`\n\n![Swapzone homepage July 2026 showing no registration or KYC required to initiate a swap from Indonesia Thailand Philippines](../media/live-swapzone-homepage.png)\n\n*Swapzone no-KYC entry flow, July 2026.*\n\n[Swapzone requires no account, no email, no KYC"
    ),
]
patches[r"Kanalcoin\swapzone-batch\articles\15-eur-to-btc-exchange-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone EUR to BTC Query (July 2026)**\nFile: `../media/live-swapzone-eur-btc-query.png`\nAlt text: `Swapzone EUR to BTC live query results showing SEPA-compatible provider rates July 2026`\nCaption: `Swapzone EUR to BTC query reviewed in July 2026 — provider rates for SEPA-compatible fiat-to-crypto routes at time of capture.`\n\n![Swapzone EUR to BTC live query results showing SEPA-compatible provider rates July 2026](../media/live-swapzone-eur-btc-query.png)\n\n*Swapzone EUR to BTC query, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"Kanalcoin\swapzone-batch\articles\16-eur-to-xmr-exchange-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone EUR to XMR Query (July 2026)**\nFile: `../media/live-swapzone-eur-xmr-query.png`\nAlt text: `Swapzone EUR to XMR live query showing provider availability for fiat-to-privacy-coin swap July 2026`\nCaption: `Swapzone EUR to XMR query reviewed in July 2026 — provider availability for this rare fiat-to-Monero route captured at review time.`\n\n![Swapzone EUR to XMR live query showing provider availability for fiat-to-privacy-coin swap July 2026](../media/live-swapzone-eur-xmr-query.png)\n\n*Swapzone EUR to XMR query, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"Kanalcoin\swapzone-batch\articles\17-dex-vs-cex-vs-aggregator-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone Aggregator Interface (July 2026)**\nFile: `../media/live-swapzone-btc-eth-query.png`\nAlt text: `Swapzone aggregator querying DEX and CEX provider rates simultaneously July 2026`\nCaption: `Swapzone aggregator query reviewed in July 2026 — the aggregator model sits between DEX and CEX, surfacing rates from both provider types in one interface.`\n\n![Swapzone aggregator querying DEX and CEX provider rates simultaneously July 2026](../media/live-swapzone-btc-eth-query.png)\n\n*Swapzone aggregator reviewed in July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"Kanalcoin\swapzone-batch\articles\20-aud-to-btc-exchange-australia-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Swapzone AUD to BTC Query (July 2026)**\nFile: `../media/live-swapzone-aud-btc-query.png`\nAlt text: `Swapzone AUD to BTC live query showing Australian fiat-to-crypto provider rates July 2026`\nCaption: `Swapzone AUD to BTC query reviewed in July 2026 — provider rates for Australian fiat deposits and AUSTRAC-registered exchange routes.`\n\n![Swapzone AUD to BTC live query showing Australian fiat-to-crypto provider rates July 2026](../media/live-swapzone-aud-btc-query.png)\n\n*Swapzone AUD to BTC query, July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"DeFiLiban\swapzone-batch\articles\18-best-crypto-staking-platforms-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Lido Finance Staking Dashboard (July 2026)**\nFile: `../media/live-lido-homepage.png`\nAlt text: `Lido Finance liquid staking homepage showing stETH APR and TVL, July 2026`\nCaption: `Lido Finance homepage reviewed in July 2026 — the largest liquid staking protocol by TVL, offering daily stETH yield accrual without lockup.`\n\n![Lido Finance liquid staking homepage showing stETH APR and TVL, July 2026](../media/live-lido-homepage.png)\n\n*Lido Finance homepage reviewed in July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"DeFiLiban\swapzone-batch\articles\19-best-crypto-loan-platforms-2026.md"] = [
    (
        "## Quick Comparison",
        "**Live Screenshot — Nexo Crypto Lending Platform (July 2026)**\nFile: `../media/live-nexo-homepage.png`\nAlt text: `Nexo crypto lending homepage showing LTV ratios and instant credit line terms, July 2026`\nCaption: `Nexo homepage reviewed in July 2026 — instant crypto-backed credit lines with disclosed LTV ratios and liquidation thresholds.`\n\n![Nexo crypto lending homepage showing LTV ratios and instant credit line terms, July 2026](../media/live-nexo-homepage.png)\n\n*Nexo homepage reviewed in July 2026.*\n\n## Quick Comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-01-best-crypto-casinos-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — BC.Game Crypto Casino (July 2026)**\nFile: `../media/live-bcgame-homepage.png`\nAlt text: `BC.Game crypto casino homepage showing game categories and crypto deposit options, July 2026`\nCaption: `BC.Game homepage reviewed in July 2026 — one of the highest-volume crypto casinos, with BTC, ETH, and SOL deposits supported natively.`\n\n![BC.Game crypto casino homepage showing game categories and crypto deposit options, July 2026](../media/live-bcgame-homepage.png)\n\n*BC.Game homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-02-best-bitcoin-casinos-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — Jackbit Bitcoin Casino (July 2026)**\nFile: `../media/live-jackbit-homepage.png`\nAlt text: `Jackbit Bitcoin casino homepage showing provably fair games and instant BTC withdrawal, July 2026`\nCaption: `Jackbit homepage reviewed in July 2026 — provably fair games, instant BTC withdrawals, no mandatory KYC for standard play.`\n\n![Jackbit Bitcoin casino homepage showing provably fair games and instant BTC withdrawal, July 2026](../media/live-jackbit-homepage.png)\n\n*Jackbit homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-03-best-no-kyc-crypto-casinos-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — BC.Game No-KYC Crypto Casino (July 2026)**\nFile: `../media/live-bcgame-homepage.png`\nAlt text: `BC.Game no-KYC crypto casino homepage reviewed July 2026`\nCaption: `BC.Game homepage reviewed in July 2026 — no mandatory KYC for crypto deposits and standard gameplay.`\n\n![BC.Game no-KYC crypto casino homepage reviewed July 2026](../media/live-bcgame-homepage.png)\n\n*BC.Game homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-04-best-telegram-casinos-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — BC.Game Telegram Casino Integration (July 2026)**\nFile: `../media/live-bcgame-homepage.png`\nAlt text: `BC.Game casino homepage with Telegram bot and TON wallet integration, July 2026`\nCaption: `BC.Game homepage reviewed in July 2026 — Telegram bot active, supporting TON wallet deposits alongside BTC and ETH.`\n\n![BC.Game casino homepage with Telegram bot and TON wallet integration, July 2026](../media/live-bcgame-homepage.png)\n\n*BC.Game homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-05-best-online-betting-platforms-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — Sportsbet.io Betting Platform (July 2026)**\nFile: `../media/live-sportsbetio-homepage.png`\nAlt text: `Sportsbet.io crypto sports betting homepage showing live markets and BTC deposit options, July 2026`\nCaption: `Sportsbet.io homepage reviewed in July 2026 — high-volume crypto sports betting with live markets and instant crypto withdrawals.`\n\n![Sportsbet.io crypto sports betting homepage showing live markets and BTC deposit options, July 2026](../media/live-sportsbetio-homepage.png)\n\n*Sportsbet.io homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-06-best-crypto-sports-betting-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — Sportsbet.io Live Betting Markets (July 2026)**\nFile: `../media/live-sportsbetio-homepage.png`\nAlt text: `Sportsbet.io live sports betting with in-play options and crypto withdrawals, July 2026`\nCaption: `Sportsbet.io homepage reviewed in July 2026 — live in-play betting markets across major sports leagues, BTC and USDT withdrawals.`\n\n![Sportsbet.io live sports betting with in-play options and crypto withdrawals, July 2026](../media/live-sportsbetio-homepage.png)\n\n*Sportsbet.io sports betting interface, July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-07-best-new-crypto-casinos-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — Wild.io New Crypto Casino (July 2026)**\nFile: `../media/live-wildio-homepage.png`\nAlt text: `Wild.io new crypto casino homepage showing welcome bonus and crypto payment options, July 2026`\nCaption: `Wild.io homepage reviewed in July 2026 — new-generation crypto casino with structured welcome bonus and no-KYC entry for standard deposits.`\n\n![Wild.io new crypto casino homepage showing welcome bonus and crypto payment options, July 2026](../media/live-wildio-homepage.png)\n\n*Wild.io homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-08-best-crypto-casino-bonuses-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — Jackbit Casino Bonus Structure (July 2026)**\nFile: `../media/live-jackbit-homepage.png`\nAlt text: `Jackbit crypto casino homepage showing welcome bonus terms and provably fair badge, July 2026`\nCaption: `Jackbit homepage reviewed in July 2026 — bonus terms and wagering requirements disclosed upfront, provably fair verification available for eligible games.`\n\n![Jackbit crypto casino homepage showing welcome bonus terms and provably fair badge, July 2026](../media/live-jackbit-homepage.png)\n\n*Jackbit homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-09-best-ai-trading-bots-2026.md"] = [
    (
        "## 5 best AI trading bots reviewed (2026 list)",
        "**Live Screenshot — 3Commas Trading Bot Platform (July 2026)**\nFile: `../media/live-3commas-homepage.png`\nAlt text: `3Commas AI trading bot platform showing DCA and grid bot options with exchange integrations, July 2026`\nCaption: `3Commas homepage reviewed in July 2026 — DCA bots, grid bots, and SmartTrade terminal across 23-plus exchange integrations.`\n\n![3Commas AI trading bot platform showing DCA and grid bot options with exchange integrations, July 2026](../media/live-3commas-homepage.png)\n\n*3Commas homepage reviewed in July 2026.*\n\n## 5 best AI trading bots reviewed (2026 list)"
    ),
    ("### 3Commas\n\n3Commas is", "### [3Commas](https://3commas.io/)\n\n3Commas is"),
    ("### Pionex\n\nPionex is", "### [Pionex](https://www.pionex.com/)\n\nPionex is"),
    ("### Cryptohopper\n\nCryptohopper", "### [Cryptohopper](https://www.cryptohopper.com/)\n\nCryptohopper"),
    ("### Bitsgap\n\nBitsgap", "### [Bitsgap](https://bitsgap.com/)\n\nBitsgap"),
    ("### Hummingbot\n\nHummingbot", "### [Hummingbot](https://hummingbot.org/)\n\nHummingbot"),
]
patches[r"coinwy\research-batch\articles\C-10-bitmex-bitmart-alternatives-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — 3Commas Platform (July 2026)**\nFile: `../media/live-3commas-homepage.png`\nAlt text: `3Commas trading platform reviewed July 2026 as recommended alternative for BitMEX and BitMart users`\nCaption: `3Commas homepage reviewed in July 2026 — recommended tool layer for users migrating from BitMEX or BitMart seeking DCA and grid bot strategies.`\n\n![3Commas trading platform reviewed July 2026 as recommended alternative for BitMEX and BitMart users](../media/live-3commas-homepage.png)\n\n*3Commas homepage, July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"coinwy\research-batch\articles\C-11-best-stablecoin-payment-platforms-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — Stripe Crypto Payment Integration (July 2026)**\nFile: `../media/live-stripe-crypto-page.png`\nAlt text: `Stripe crypto payment page showing USDC and Solana stablecoin payment rails for merchants, July 2026`\nCaption: `Stripe crypto payments page reviewed in July 2026 — USDC on Solana payment rails for merchants, part of our stablecoin payment platform comparison.`\n\n![Stripe crypto payment page showing USDC and Solana stablecoin payment rails for merchants, July 2026](../media/live-stripe-crypto-page.png)\n\n*Stripe crypto payments page reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"Kanalcoin\research-batch\articles\K-01-best-telegram-casinos-sea-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — BC.Game Telegram Casino for SEA (July 2026)**\nFile: `../media/live-bcgame-homepage.png`\nAlt text: `BC.Game casino with Telegram integration accessible from Indonesia Thailand Vietnam Philippines July 2026`\nCaption: `BC.Game homepage reviewed in July 2026 — Telegram bot active, TON wallet integration, accessible from SEA without geo-restriction.`\n\n![BC.Game casino with Telegram integration accessible from Indonesia Thailand Vietnam Philippines July 2026](../media/live-bcgame-homepage.png)\n\n*BC.Game homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"Kanalcoin\research-batch\articles\K-02-best-no-kyc-crypto-casinos-sea-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — BC.Game No-KYC Casino for SEA (July 2026)**\nFile: `../media/live-bcgame-homepage.png`\nAlt text: `BC.Game no-KYC crypto casino accessible from Indonesia Thailand Philippines July 2026`\nCaption: `BC.Game homepage reviewed in July 2026 — no mandatory KYC, accepts BTC, ETH, USDT with P2P options for IDR, THB, and PHP.`\n\n![BC.Game no-KYC crypto casino accessible from Indonesia Thailand Philippines July 2026](../media/live-bcgame-homepage.png)\n\n*BC.Game homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"Kanalcoin\research-batch\articles\K-03-best-crypto-sports-betting-sea-2026.md"] = [
    (
        "## Quick comparison",
        "**Live Screenshot — Sportsbet.io SEA Access (July 2026)**\nFile: `../media/live-sportsbetio-homepage.png`\nAlt text: `Sportsbet.io crypto sports betting accessible from Southeast Asia with live markets July 2026`\nCaption: `Sportsbet.io homepage reviewed in July 2026 — accessible from Indonesia, Thailand, Vietnam, Philippines without geo-block, crypto deposits and live markets.`\n\n![Sportsbet.io crypto sports betting accessible from Southeast Asia with live markets July 2026](../media/live-sportsbetio-homepage.png)\n\n*Sportsbet.io homepage reviewed in July 2026.*\n\n## Quick comparison"
    ),
]
patches[r"Kanalcoin\research-batch\articles\K-04-best-crypto-robinhood-sea-2026.md"] = [
    (
        "| Asset | Robinhood listed",
        "**Live Screenshot — Indodax Exchange for SEA Investors (July 2026)**\nFile: `../media/live-indodax-homepage.png`\nAlt text: `Indodax Indonesia crypto exchange homepage showing BTC ETH XRP trading pairs, July 2026`\nCaption: `Indodax homepage reviewed in July 2026 — Indonesia's largest regulated exchange, covering most Robinhood-listed assets for IDR-based investors.`\n\n![Indodax Indonesia crypto exchange homepage showing BTC ETH XRP trading pairs, July 2026](../media/live-indodax-homepage.png)\n\n*Indodax homepage reviewed in July 2026.*\n\n| Asset | Robinhood listed"
    ),
]
patches[r"CCpress\research-batch\articles\P-01-ai-agent-crypto-power-map-2026.md"] = [
    (
        "## Three types of AI agent crypto projects",
        "**Live Screenshot — ElizaOS AI Agent Framework (July 2026)**\nFile: `../media/live-elizaos-homepage.png`\nAlt text: `ElizaOS AI agent open-source framework homepage, reviewed July 2026`\nCaption: `ElizaOS homepage reviewed in July 2026 — the open-source AI agent framework at the center of the ai16z ecosystem, infrastructure layer not a speculative token.`\n\n![ElizaOS AI agent open-source framework homepage, reviewed July 2026](../media/live-elizaos-homepage.png)\n\n*ElizaOS homepage reviewed in July 2026.*\n\n## Three types of AI agent crypto projects"
    ),
]
patches[r"CCpress\research-batch\articles\P-02-polymarket-cftc-prediction-markets-2026.md"] = [
    (
        "## The liquidity reality",
        "**Live Screenshot — Polymarket Prediction Market (July 2026)**\nFile: `../media/live-polymarket-homepage.png`\nAlt text: `Polymarket decentralized prediction market homepage showing active event markets, July 2026`\nCaption: `Polymarket homepage reviewed in July 2026 — largest on-chain prediction market by liquidity, US users blocked since 2022 CFTC settlement.`\n\n![Polymarket decentralized prediction market homepage showing active event markets, July 2026](../media/live-polymarket-homepage.png)\n\n*Polymarket homepage reviewed in July 2026.*\n\n**Live Screenshot — Kalshi CFTC-Licensed Markets (July 2026)**\nFile: `../media/live-kalshi-homepage.png`\nAlt text: `Kalshi CFTC-licensed event contract market homepage showing regulated prediction markets for US users, July 2026`\nCaption: `Kalshi homepage reviewed in July 2026 — the only CFTC-designated contract market for event contracts as of July 2026, legally accessible to US persons.`\n\n![Kalshi CFTC-licensed event contract market homepage showing regulated prediction markets for US users, July 2026](../media/live-kalshi-homepage.png)\n\n*Kalshi homepage reviewed in July 2026.*\n\n## The liquidity reality"
    ),
]
patches[r"CCpress\research-batch\articles\P-03-tokenized-stock-perps-sec-scrutiny-2026.md"] = [
    (
        "## The oracle problem",
        "**Live Screenshot — dYdX Perpetuals Platform After Stock Delisting (July 2026)**\nFile: `../media/live-dydx-homepage.png`\nAlt text: `dYdX decentralized perpetuals platform after delisting synthetic equity products July 2026`\nCaption: `dYdX homepage reviewed in July 2026 — the platform delisted most synthetic equity products citing regulatory requirements, the clearest public acknowledgment of SEC risk in this category.`\n\n![dYdX decentralized perpetuals platform after delisting synthetic equity products July 2026](../media/live-dydx-homepage.png)\n\n*dYdX homepage reviewed in July 2026.*\n\n**Live Screenshot — Synthetix Protocol (July 2026)**\nFile: `../media/live-synthetix-homepage.png`\nAlt text: `Synthetix synthetic asset protocol homepage showing SNX governance structure, July 2026`\nCaption: `Synthetix homepage reviewed in July 2026 — the foundational synthetic asset protocol governed by SNX token holders, without SEC or CFTC registration.`\n\n![Synthetix synthetic asset protocol homepage showing SNX governance structure, July 2026](../media/live-synthetix-homepage.png)\n\n*Synthetix homepage reviewed in July 2026.*\n\n## The oracle problem"
    ),
]

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
            skipped_ops.append(old[:50])
    if content != original:
        pathlib.Path(full_path).write_text(content, encoding="utf-8")
        patched.append("PATCHED (" + str(applied) + "/" + str(len(ops)) + "): " + rel_path)
    else:
        patched.append("NO CHANGE: " + rel_path)
    for s in skipped_ops:
        errors.append("  SKIP in " + rel_path + ": '" + s + "'")

for p in patched:
    print(p)
print("---")
for e in errors:
    print(e)
print("Total: " + str(len(patches)))
