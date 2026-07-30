import re, os

BASE = r"C:\Users\admin\Authority-Building"

def img(rel_path, alt, caption):
    return f'\n![{alt}](../media/{rel_path})\n*{caption}*\n'

# Each entry: (article_path, insert_after_pattern, image_block)
# insert_after_pattern = regex that matches the LAST line of the table block to insert after
PATCHES = [

  # ── COINWY ──────────────────────────────────────────────────────────────

  ("coinwy/swapzone-batch/articles/01-best-crypto-exchange-aggregators-2026.md",
   r"\| SideShift \|",
   img("01-swapzone-query-btc-eth.png",
       "Swapzone BTC to ETH query results showing 8 providers with rates, speed, and fixed/float toggle — July 2026",
       "Swapzone query: BTC→ETH, results ranked by rate across 8+ providers. Partner list and rates change — verify at swapzone.io before any swap.")),

  ("coinwy/swapzone-batch/articles/02-crypto-exchange-aggregator-vs-regular-exchange.md",
   r"\|.*aggregator.*\||\|.*exchange.*\||\|.*CEX.*\||\|.*DEX.*\|",
   img("02-swapzone-query-results.png",
       "Swapzone multi-provider query results showing rate comparison across providers in a single interface — July 2026",
       "One Swapzone query surfaces rates from multiple providers simultaneously. A direct exchange shows only its own rate.")),

  ("coinwy/swapzone-batch/articles/03-best-instant-crypto-swap-no-registration.md",
   r"\|.*registration.*\||\|.*KYC.*\||\|.*account.*\|",
   img("03-swapzone-no-registration-flow.png",
       "Swapzone swap entry flow showing no login or account creation required — July 2026",
       "Swapzone swap start: no account, no login prompt. Destination wallet address is the only required input.")),

  ("coinwy/swapzone-batch/articles/04-fixed-rate-vs-floating-rate-crypto-swap.md",
   r"\|.*fixed.*\||\|.*float.*\||\|.*rate type.*\|",
   img("04-swapzone-rate-toggle.png",
       "Swapzone results page showing fixed and floating rate toggle for provider selection — July 2026",
       "Swapzone rate toggle: filter results by fixed or floating rate before selecting a provider.")),

  ("coinwy/swapzone-batch/articles/05-btc-to-xmr-exchange-2026.md",
   r"\| SideShift \|",
   img("05-swapzone-btc-xmr-results.png",
       "Swapzone BTC to XMR query results showing StealthEX, Exolix, and other providers with rates — July 2026",
       "Swapzone BTC→XMR query, July 2026. StealthEX appeared in top position across multiple queries. Provider availability and rates change — verify directly.")),

  ("coinwy/swapzone-batch/articles/06-usdt-to-btc-best-rate-2026.md",
   r"\|.*USDT.*\||\|.*tether.*\||\|.*rate.*swap.*\||\| ChangeNOW \||\| Exolix \|",
   img("06-swapzone-usdt-btc-results.png",
       "Swapzone USDT to BTC query showing provider list with rates and estimated completion time — July 2026",
       "Swapzone USDT→BTC results, July 2026. Top provider and rate vary by time and amount — check live before swapping.")),

  ("coinwy/swapzone-batch/articles/07-btc-to-eth-exchange-rate-2026.md",
   r"\|.*BTC.*ETH.*\||\|.*rate.*\|.*speed.*\||\| StealthEX \||\| Exolix \||\| ChangeNOW \|",
   img("07-swapzone-btc-eth-results.png",
       "Swapzone BTC to ETH query results with provider rate comparison — July 2026",
       "Swapzone BTC→ETH results, July 2026. Rate spread between providers typically 0.3–0.8% on this pair.")),

  ("coinwy/swapzone-batch/articles/08-eth-to-btc-swap-best-rate.md",
   r"\|.*ETH.*BTC.*\||\|.*rate.*\|.*speed.*\||\| StealthEX \||\| Exolix \||\| ChangeNOW \|",
   img("08-swapzone-eth-btc-results.png",
       "Swapzone ETH to BTC query results showing provider comparison — July 2026",
       "Swapzone ETH→BTC results, July 2026. Rates change with ETH/BTC market movement — verify before executing.")),

  ("coinwy/swapzone-batch/articles/09-btc-to-trx-exchange-2026.md",
   r"\|.*TRX.*\||\|.*tron.*\||\| StealthEX \||\| Exolix \||\| ChangeNOW \|",
   img("09-swapzone-btc-trx-results.png",
       "Swapzone BTC to TRX query results — July 2026",
       "Swapzone BTC→TRX, July 2026. TRX pairs have fewer active providers than BTC/ETH — check availability directly.")),

  ("coinwy/swapzone-batch/articles/10-best-ton-exchange-gram-2026.md",
   r"\|.*TON.*\||\|.*gram.*\||\| StealthEX \||\| Exolix \||\| ChangeNOW \|",
   img("10-swapzone-btc-ton-results.png",
       "Swapzone BTC to TON query showing providers offering TON swaps — July 2026",
       "Swapzone BTC→TON results, July 2026. TON liquidity varies — Swapzone aggregates available providers in one query.")),

  ("coinwy/swapzone-batch/articles/11-swapzone-vs-changenow.md",
   r"\| Coins \|",
   img("11-swapzone-query-with-changenow.png",
       "Swapzone BTC to ETH results with ChangeNOW appearing as one of the listed providers — July 2026",
       "ChangeNOW appears in Swapzone query results alongside other providers. Running Swapzone first checks ChangeNOW's rate automatically.")),

  ("coinwy/swapzone-batch/articles/12-swapzone-vs-swapspace.md",
   r"\|.*partner.*\||\|.*coin.*count.*\||\|.*coverage.*\||\| Fiat support \||\| Registration \|",
   img("12-swapzone-btc-eth-results.png",
       "Swapzone BTC to ETH results for rate comparison — July 2026",
       "Swapzone BTC→ETH results, July 2026. Compare against SwapSpace for the same pair to check rate spread.")),

  ("coinwy/swapzone-batch/articles/13-best-changenow-alternatives-2026.md",
   r"\|.*alternative.*\||\|.*ChangeNOW.*\||\|.*KYC.*\|.*fixed.*\||\| Exolix \||\| LetsExchange \|",
   img("13-swapzone-homepage.png",
       "Swapzone homepage showing partner logos and exchange aggregator interface — July 2026",
       "Swapzone as a ChangeNOW alternative: aggregates ChangeNOW alongside 17+ other providers in one rate query.")),

  # ── KANALCOIN ──────────────────────────────────────────────────────────

  ("Kanalcoin/swapzone-batch/articles/14-no-kyc-crypto-exchanges-2026.md",
   r"\|.*KYC.*\||\|.*registration.*\||\| ChangeNOW \||\| StealthEX \||\| Exolix \|",
   img("14-swapzone-no-kyc-flow.png",
       "Swapzone swap interface requiring no account or KYC at the aggregator level — July 2026",
       "Swapzone entry flow: no login, no identity check at aggregator level. Individual providers may trigger KYC at high amounts.")),

  ("Kanalcoin/swapzone-batch/articles/15-eur-to-btc-exchange-2026.md",
   r"\|.*EUR.*\||\|.*SEPA.*\||\|.*fiat.*\||\| ChangeNOW \||\| Kraken \|",
   img("15-swapzone-eur-btc-results.png",
       "Swapzone EUR to BTC query results showing fiat pair availability and provider rates — July 2026",
       "Swapzone EUR→BTC results, July 2026. Fiat pair availability depends on active partners — verify before initiating.")),

  ("Kanalcoin/swapzone-batch/articles/16-eur-to-xmr-exchange-2026.md",
   r"\|.*XMR.*\||\|.*monero.*\||\|.*EUR.*XMR.*\||\| StealthEX \||\| Exolix \|",
   img("16-swapzone-eur-xmr-results.png",
       "Swapzone BTC to XMR query results — July 2026",
       "EUR→XMR typically routes via BTC or ETH intermediate on most aggregators. Swapzone shows available paths in one query.")),

  ("Kanalcoin/swapzone-batch/articles/17-dex-vs-cex-vs-aggregator-2026.md",
   r"\|.*DEX.*\||\|.*CEX.*\||\|.*aggregator.*\||\|.*Uniswap.*\||\|.*Binance.*\|",
   img("17-swapzone-aggregator-results.png",
       "Swapzone aggregator interface showing multi-provider rate results in a single query — July 2026",
       "Swapzone aggregator: one query, rates from 18+ providers. Contrast with CEX (single platform rate) and DEX (on-chain liquidity pool).")),

  ("Kanalcoin/swapzone-batch/articles/20-aud-to-btc-exchange-australia-2026.md",
   r"\|.*AUD.*\||\|.*Australia.*\||\|.*AUSTRAC.*\||\| CoinSpot \||\| Swyftx \|",
   img("20-swapzone-aud-btc-results.png",
       "Swapzone AUD to BTC query showing fiat pair results — July 2026",
       "Swapzone AUD→BTC, July 2026. AUD fiat support routed through select partners — verify availability at swapzone.io before initiating.")),

  # ── DEFILIBAN ──────────────────────────────────────────────────────────

  ("DeFiLiban/swapzone-batch/articles/18-best-crypto-staking-platforms-2026.md",
   r"\| ANKR \(direct\) \|",
   img("18-swapzone-staking-page.png",
       "Swapzone staking page showing P2P, Nexo, CoinRabbit, and ANKR APR rates — July 2026",
       "Swapzone staking aggregator, July 2026: P2P 34.8% APR, Nexo 18.9% APR, CoinRabbit 5% APR, ANKR 0.92% APR. Rates change with market conditions — verify at swapzone.io/staking.")),

  ("DeFiLiban/swapzone-batch/articles/19-best-crypto-loan-platforms-2026.md",
   r"\|.*LTV.*\||\|.*APR.*\|.*loan.*\||\| CoinRabbit \||\| Nexo \||\| YouHodler \|",
   img("19-swapzone-loans-page.png",
       "Swapzone loans page showing YouHodler, CoinRabbit, and Nexo APR and LTV rates — July 2026",
       "Swapzone loan aggregator, July 2026. APR and LTV figures change — verify current rates at swapzone.io/loans before committing.")),
]

def patch_article(rel_path, pattern, image_block):
    path = os.path.join(BASE, rel_path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Already patched?
    fname = image_block.split("../media/")[1].split('"')[0] if "../media/" in image_block else ""
    if fname and fname in content:
        print(f"SKIP (already patched): {rel_path}")
        return

    lines = content.split("\n")
    insert_at = None

    # Find last line matching pattern
    for i, line in enumerate(lines):
        if re.search(pattern, line, re.IGNORECASE):
            insert_at = i

    if insert_at is None:
        # Fallback: find last table row (line starting with |) in first 80 lines
        for i, line in enumerate(lines[:80]):
            if line.startswith("|") and not line.startswith("| ---") and not line.startswith("|---"):
                insert_at = i
        print(f"WARN fallback insert at L{insert_at+1}: {rel_path}")
    else:
        print(f"OK   insert after L{insert_at+1}: {rel_path}")

    if insert_at is not None:
        lines.insert(insert_at + 1, image_block)
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

for rel_path, pattern, image_block in PATCHES:
    patch_article(rel_path, pattern, image_block)

print("\nAll patches applied.")
