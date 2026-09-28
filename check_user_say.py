import glob

for fname in ["11-swapzone-vs-changenow.md", "12-swapzone-vs-swapspace.md", "17-dex-vs-cex-vs-aggregator-2026.md", "20-aud-to-btc-exchange-australia-2026.md"]:
    paths = glob.glob(f"**/{fname}", recursive=True)
    if not paths: continue
    with open(paths[0], encoding="utf-8") as fh:
        content = fh.read()
    start = content.find("## What users actually say")
    if start < 0:
        start = content.find("## What users say")
    if start < 0:
        print(f"{fname}: no user say section")
        continue
    end = content.find("\n##", start + 5)
    section = content[start:end] if end > 0 else content[start:]
    print(f"=== {fname} 'What users say' ===")
    print(section[:800])
    print()
