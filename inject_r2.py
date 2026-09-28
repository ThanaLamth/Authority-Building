# Part 3 corrected: use exact header names
import json, re, glob, os

exec(open("inject_part1.py", encoding="utf-8").read())
exec(open("inject_part2.py", encoding="utf-8").read())

def build_block(article_num, platform_key, site_name):
    take_key = (article_num, platform_key)
    my_take = MY_TAKES.get(take_key, "Reviews here reflect real user outcomes.")
    rv = REVIEWS.get(platform_key)
    if not rv:
        return ""
    lines = ["\n**What users say**\n"]
    pos = rv.get("pos")
    if pos:
        lines.append("**Positive**")
        lines.append('> "' + pos["text"] + '"')
        lines.append(">")
        lines.append('> -- ' + pos["author"] + ', [Trustpilot](' + pos["url"] + ')')
        lines.append("")
    neg = rv.get("neg")
    if neg:
        lines.append("**Critical**")
        lines.append('> "' + neg["text"] + '"')
        lines.append(">")
        lines.append('> -- ' + neg["author"] + ', [Trustpilot](' + neg["url"] + ')')
        lines.append("")
    lines.append('> **' + site_name + ' Editorial -- My take:** ' + my_take)
    lines.append("")
    return "\n".join(lines)


def insert_block_into_section(content, section_header, article_num, platform_key, site_name):
    if section_header not in content:
        return content, False
    start = content.find(section_header)
    end_markers = ["\n###", "\n## "]
    next_sec = len(content)
    for marker in end_markers:
        idx = content.find(marker, start + len(section_header) + 5)
        if 0 < idx < next_sec:
            next_sec = idx
    section = content[start:next_sec]
    if "**What users say**" in section:
        return content, False
    block = build_block(article_num, platform_key, site_name)
    if not block:
        return content, False
    sep_idx = section.rfind("\n\n\n")
    if sep_idx > 0:
        insert_pos = start + sep_idx
    else:
        insert_pos = next_sec
    new_content = content[:insert_pos] + "\n" + block + content[insert_pos:]
    return new_content, True


def process_file(path, article_num, site_name, platform_map):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    changed = False
    for exact_header, pk in platform_map:
        if exact_header not in content:
            print("  WARN not found:", repr(exact_header), "in", os.path.basename(path))
            continue
        content, did_change = insert_block_into_section(content, exact_header, article_num, pk, site_name)
        if did_change:
            changed = True
            print("  Added", pk, "->", os.path.basename(path))
    if changed:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print("Saved:", os.path.basename(path))
    return changed


def process_vs_or_bottom(path, article_num, platform_pairs, site_name):
    """For vs-articles and articles without per-provider sections, replace the 'What users actually say' section."""
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    marker = "## What users actually say"
    if marker not in content:
        marker = "## What users say"
    if marker not in content:
        print("  No user-say section in", os.path.basename(path))
        return False
    start = content.find(marker)
    end = content.find("\n## ", start + 5)
    if end < 0:
        end = len(content)
    old_section = content[start:end]
    if "**Positive**" in old_section:
        print("  Already structured:", os.path.basename(path))
        return False
    new_parts = [marker + "\n"]
    for label, pk in platform_pairs:
        block = build_block(article_num, pk, site_name)
        new_parts.append("**" + label + "**\n" + block + "\n")
    new_section = "\n".join(new_parts)
    new_content = content[:start] + new_section + content[end:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_content)
    print("Updated:", os.path.basename(path))
    return True


print("=== Starting injection round 2 ===\n")

# 08: ETH to BTC -- bare ### headers
path08 = "coinwy/swapzone-batch/articles/08-eth-to-btc-swap-best-rate.md"
process_file(path08, "08", "Coinwy", [
    ("### Swapzone", "swapzone"), ("### ChangeNOW", "changenow"),
    ("### SimpleSwap", "simpleswap"), ("### StealthEX", "stealthex"),
])

# 09: BTC to TRX
path09 = "coinwy/swapzone-batch/articles/09-btc-to-trx-exchange-2026.md"
process_file(path09, "09", "Coinwy", [
    ("### Swapzone", "swapzone"), ("### ChangeNOW", "changenow"),
    ("### SimpleSwap", "simpleswap"),
])

# 10: TON
path10 = "coinwy/swapzone-batch/articles/10-best-ton-exchange-gram-2026.md"
process_file(path10, "10", "Coinwy", [
    ("### Swapzone", "swapzone"), ("### ChangeNOW", "changenow"),
    ("### SimpleSwap", "simpleswap"),
])

# 13: ChangeNOW alternatives
path13 = "coinwy/swapzone-batch/articles/13-best-changenow-alternatives-2026.md"
process_file(path13, "13", "Coinwy", [
    ("### Swapzone", "swapzone"), ("### SwapSpace", "swapspace"),
    ("### StealthEX", "stealthex"), ("### SimpleSwap", "simpleswap"),
    ("### Exolix", "exolix"), ("### Changelly", "changelly"),
])

# 14: No-KYC
path14 = "Kanalcoin/swapzone-batch/articles/14-no-kyc-crypto-exchanges-2026.md"
process_file(path14, "14", "Kanalcoin", [
    ("### Swapzone", "swapzone"), ("### StealthEX", "stealthex"),
    ("### ChangeNOW", "changenow"), ("### SimpleSwap", "simpleswap"),
])

# 15: EUR to BTC
path15 = "Kanalcoin/swapzone-batch/articles/15-eur-to-btc-exchange-2026.md"
process_file(path15, "15", "Kanalcoin", [
    ("### Swapzone", "swapzone"), ("### ChangeNOW", "changenow"),
    ("### Changelly", "changelly"),
])

# 16: EUR to XMR
path16 = "Kanalcoin/swapzone-batch/articles/16-eur-to-xmr-exchange-2026.md"
process_file(path16, "16", "Kanalcoin", [
    ("### Swapzone", "swapzone"), ("### StealthEX", "stealthex"),
    ("### Exolix", "exolix"),
])

# 17: DEX vs CEX -- Swapzone appears in "Aggregator" section, add to bottom
path17 = "Kanalcoin/swapzone-batch/articles/17-dex-vs-cex-vs-aggregator-2026.md"
process_vs_or_bottom(path17, "17", [
    ("Swapzone (aggregator)", "swapzone"),
    ("ChangeNOW (direct)", "changenow"),
], "Kanalcoin")

# 18: Staking -- Nexo is under "CeFi staking" H3
path18 = "DeFiLiban/swapzone-batch/articles/18-best-crypto-staking-platforms-2026.md"
process_file(path18, "18", "DeFiLiban", [
    ("### Mechanism 3: CeFi staking and yield (Nexo, CoinRabbit)", "nexo"),
])

# 19: Loans -- Nexo is a ### section
path19 = "DeFiLiban/swapzone-batch/articles/19-best-crypto-loan-platforms-2026.md"
process_file(path19, "19", "DeFiLiban", [
    ("### Nexo", "nexo"),
])

# 20: AUD to BTC -- Swapzone has its own ## section, ChangeNOW doesn't have a standalone section
path20 = "Kanalcoin/swapzone-batch/articles/20-aud-to-btc-exchange-australia-2026.md"
process_file(path20, "20", "Kanalcoin", [
    ("## Where Swapzone fits for Australian users", "swapzone"),
])
# ChangeNOW not in standalone section - add to bottom
process_vs_or_bottom(path20, "20", [
    ("Swapzone", "swapzone"), ("ChangeNOW", "changenow"),
], "Kanalcoin")

print("\n=== Done ===")
