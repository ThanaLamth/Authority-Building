import glob

files = {
    "08": "coinwy/swapzone-batch/articles/08-eth-to-btc-swap-best-rate.md",
    "09": "coinwy/swapzone-batch/articles/09-btc-to-trx-exchange-2026.md",
    "10": "coinwy/swapzone-batch/articles/10-best-ton-exchange-gram-2026.md",
    "13": "coinwy/swapzone-batch/articles/13-best-changenow-alternatives-2026.md",
    "14": "Kanalcoin/swapzone-batch/articles/14-no-kyc-crypto-exchanges-2026.md",
    "15": "Kanalcoin/swapzone-batch/articles/15-eur-to-btc-exchange-2026.md",
    "16": "Kanalcoin/swapzone-batch/articles/16-eur-to-xmr-exchange-2026.md",
    "17": "Kanalcoin/swapzone-batch/articles/17-dex-vs-cex-vs-aggregator-2026.md",
    "18": "DeFiLiban/swapzone-batch/articles/18-best-crypto-staking-platforms-2026.md",
    "19": "DeFiLiban/swapzone-batch/articles/19-best-crypto-loan-platforms-2026.md",
    "20": "Kanalcoin/swapzone-batch/articles/20-aud-to-btc-exchange-australia-2026.md",
}

for num, path in files.items():
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    print(f"=== {num} headers ===")
    for line in content.split("\n"):
        if line.startswith("#"):
            print(f"  {repr(line[:80])}")
    print()
