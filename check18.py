with open("DeFiLiban/swapzone-batch/articles/18-best-crypto-staking-platforms-2026.md", encoding="utf-8") as fh:
    c = fh.read()

# Find Mechanism 3
idx = c.find("### Mechanism 3")
end = c.find("###", idx+5)
section = c[idx:end]
print("MECHANISM 3 SECTION:")
print(section)
