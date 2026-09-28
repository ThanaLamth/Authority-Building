import glob

files = {
    "08": "coinwy/swapzone-batch/articles/08-eth-to-btc-swap-best-rate.md",
    "09": "coinwy/swapzone-batch/articles/09-btc-to-trx-exchange-2026.md",
    "10": "coinwy/swapzone-batch/articles/10-best-ton-exchange-gram-2026.md",
}

for num, path in files.items():
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    # Find ### Swapzone section
    start = content.find("### Swapzone")
    end = content.find("###", start+5)
    section = content[start:end]
    print(f"=== {num} ### Swapzone section ===")
    print(section[-400:])
    print()
