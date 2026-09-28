for path in ["DeFiLiban/swapzone-batch/articles/18-best-crypto-staking-platforms-2026.md",
             "DeFiLiban/swapzone-batch/articles/19-best-crypto-loan-platforms-2026.md"]:
    with open(path, encoding="utf-8") as fh:
        c = fh.read()
    print(f"=== {path} ===")
    idx = c.find("### Nexo")
    if idx >= 0:
        print("Found ### Nexo at", idx)
        end = c.find("###", idx+5)
        section = c[idx:end if end>0 else idx+1000]
        print("Has What users say:", "**What users say**" in section)
        print(section[:200])
    # What about CeFi mechanism
    idx2 = c.find("CeFi staking")
    if idx2 >= 0:
        print("CeFi staking section:", c[idx2:idx2+100])
    print()
