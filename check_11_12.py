import glob

for fname in ["11-swapzone-vs-changenow.md", "12-swapzone-vs-swapspace.md", "17-dex-vs-cex-vs-aggregator-2026.md", "20-aud-to-btc-exchange-australia-2026.md"]:
    paths = glob.glob(f"**/{fname}", recursive=True)
    if not paths: continue
    with open(paths[0], encoding="utf-8") as fh:
        content = fh.read()
    print(f"=== {fname} ===")
    # Show all headings
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("#"):
            print(f"  L{i}: {line}")
    print(f"  Length: {len(content)} chars")
    print()
