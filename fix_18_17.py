import re

# Article 18: replace existing What users say block in Mechanism 3 section with real Nexo reviews
with open("DeFiLiban/swapzone-batch/articles/18-best-crypto-staking-platforms-2026.md", encoding="utf-8") as fh:
    c = fh.read()

# Fix encoding artifacts (latin1 misread as bytes)
c = c.replace("\u00c2\u00a0", " ").replace("\u00e2\u0080\u0094", "--").replace("\u00e2\u0098\u0085", "*")

# Find and replace the Mechanism 3 What users say block with real Nexo block
old_block_start = c.find("**What users say**", c.find("### Mechanism 3"))
if old_block_start >= 0:
    # Find end of block (next heading or blank-blank)
    old_block_end = c.find("\n\n\n", old_block_start+5)
    if old_block_end < 0:
        old_block_end = c.find("\n## ", old_block_start)
    
    nexo_block = """
**What users say**

**Positive**
> "I've been an active user and I never had any issue with NEXO. Customer Service is excellent, the app is well designed and my personal experience with NEXO is positive."
>
> -- customer, [Trustpilot](https://www.trustpilot.com/reviews/6a79ae436f54bddb7c38fc01)

**Critical**
> "Borrowing is available for Nevada so I signed up and got verified. But borrowing is NOT available to me specifically. Contacted support, escalated to agent, waited over an hour. This company is a joke."
>
> -- J., [Trustpilot](https://www.trustpilot.com/reviews/6a7f35f8d9178ca012a98b07)

> **DeFiLiban Editorial -- My take:** The anonymous reviewer's 'never had any issue' is a common Nexo baseline -- the platform is stable and well-designed for passive yield. J.'s borrowing restriction is legitimate and specific: Nexo restricts products by jurisdiction, and the verification flow doesn't surface this until you're already KYC'd. If you're staking (not borrowing), J.'s complaint is not relevant to you. The staking product is the more consistent half of Nexo.

"""
    c = c[:old_block_start] + nexo_block + c[old_block_end:]
    print("Replaced Nexo block in article 18")

with open("DeFiLiban/swapzone-batch/articles/18-best-crypto-staking-platforms-2026.md", "w", encoding="utf-8") as fh:
    fh.write(c)

# Fix encoding artifacts in article 17
with open("Kanalcoin/swapzone-batch/articles/17-dex-vs-cex-vs-aggregator-2026.md", encoding="utf-8") as fh:
    c17 = fh.read()

c17 = c17.replace("â€"", "--").replace("â€™", "'").replace("â€˜", "'").replace("â€œ", '"').replace("â€", '"')
c17 = c17.replace("â˜…", "*")

with open("Kanalcoin/swapzone-batch/articles/17-dex-vs-cex-vs-aggregator-2026.md", "w", encoding="utf-8") as fh:
    fh.write(c17)
print("Fixed encoding in article 17")

# Fix encoding artifacts in article 20
with open("Kanalcoin/swapzone-batch/articles/20-aud-to-btc-exchange-australia-2026.md", encoding="utf-8") as fh:
    c20 = fh.read()

c20 = c20.replace("â€"", "--").replace("â€™", "'").replace("â€˜", "'").replace("â€œ", '"').replace("â€", '"')
c20 = c20.replace("â˜…", "*")

with open("Kanalcoin/swapzone-batch/articles/20-aud-to-btc-exchange-australia-2026.md", "w", encoding="utf-8") as fh:
    fh.write(c20)
print("Fixed encoding in article 20")
