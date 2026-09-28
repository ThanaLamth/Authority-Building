import re

files = [
    "Kanalcoin/swapzone-batch/articles/16-eur-to-xmr-exchange-2026.md",
    "Kanalcoin/swapzone-batch/articles/14-no-kyc-crypto-exchanges-2026.md",
    "Kanalcoin/swapzone-batch/articles/20-aud-to-btc-exchange-australia-2026.md",
    "DeFiLiban/swapzone-batch/articles/18-best-crypto-staking-platforms-2026.md",
    "DeFiLiban/swapzone-batch/articles/19-best-crypto-loan-platforms-2026.md",
    "coinwy/swapzone-batch/articles/13-best-changenow-alternatives-2026.md",
    "coinwy/swapzone-batch/articles/07-btc-to-eth-exchange-rate-2026.md",
]

for fname in files:
    with open(fname, encoding="utf-8") as fh:
        c = fh.read()
    name = fname.split("/")[-1]
    blocks = c.count("**What users say**")
    bad_chars = sum(1 for ch in c if ord(ch) > 0x00FF and ord(ch) < 0x0400)
    print(f"{name}: {blocks} blocks")
    for m in re.finditer(r"### (.+)", c):
        header = m.group(1)
        section_start = m.start()
        section_end = c.find("\n###", section_start+5)
        if section_end < 0:
            section_end = c.find("\n## ", section_start+5)
        section = c[section_start:section_end if section_end > 0 else section_start+2000]
        has_wus = "**What users say**" in section
        if has_wus:
            print(f"  OK: {header[:50]}")
    print()
