import glob, os

for fname in ["08-eth-to-btc-swap-best-rate.md", "09-btc-to-trx-exchange-2026.md", "10-best-ton-exchange-gram-2026.md"]:
    paths = glob.glob(f"**/{fname}", recursive=True)
    if not paths:
        print(f"{fname}: not found")
        continue
    with open(paths[0], encoding="utf-8") as fh:
        content = fh.read()
    start = content.find("### Swapzone")
    if start < 0:
        print(f"{fname}: No Swapzone section")
        continue
    after = content.find("###", start + 5)
    section = content[start:after] if after > 0 else content[start:start+1000]
    print(f"=== {fname} Swapzone section (last 400 chars) ===")
    print(section[-400:])
    print()
