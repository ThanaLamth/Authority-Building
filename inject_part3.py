def build_block(article_num, platform_key, site_name):
    take_key = (article_num, platform_key)
    my_take = MY_TAKES.get(take_key, "Reviews here reflect real user outcomes. Treat the positive as a baseline, the critical as a ceiling test.")
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
    sep_idx = section.rfind("\n---")
    if sep_idx > 0:
        insert_pos = start + sep_idx
        new_content = content[:insert_pos] + "\n" + block + content[insert_pos:]
    else:
        new_content = content[:next_sec] + block + "\n" + content[next_sec:]
    return new_content, True


def process_file(path, article_num, site_name, platform_map):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    changed = False
    for partial_header, pk in platform_map:
        actual_header = None
        for line in content.split("\n"):
            stripped = line.strip()
            if (stripped.startswith("###") or stripped.startswith("##")) and partial_header.lower() in stripped.lower():
                actual_header = stripped
                break
        if actual_header is None:
            if partial_header in content:
                actual_header = partial_header
            else:
                print("  WARN: header not found:", partial_header, "in", os.path.basename(path))
                continue
        content, did_change = insert_block_into_section(content, actual_header, article_num, pk, site_name)
        if did_change:
            changed = True
            print("  Added", pk, "block ->", os.path.basename(path))
    if changed:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print("Saved:", path)
    return changed


def process_vs_article(path, article_num, platform_pairs):
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
    for label, pk, site_name in platform_pairs:
        block = build_block(article_num, pk, site_name)
        new_parts.append("**" + label + "**\n" + block + "\n")
    new_section = "\n".join(new_parts)
    new_content = content[:start] + new_section + content[end:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_content)
    print("Updated vs-article:", path)
    return True


def find_articles(*patterns):
    results = []
    for pat in patterns:
        results += glob.glob(pat)
    return results

print("=== Starting injection ===\n")

# 05
for p in find_articles("coinwy/swapzone-batch/articles/05-btc-to-xmr*.md"):
    process_file(p, "05", "Coinwy", [("Swapzone: Rate Comparison Across Active XMR", "swapzone"), ("StealthEX: Our Pick for No-KYC", "stealthex"), ("ChangeNOW: Our Pick for Speed", "changenow"), ("Exolix: Our Pick for Fixed Rate", "exolix")])

# 06
for p in find_articles("coinwy/swapzone-batch/articles/06-usdt-to-btc*.md"):
    process_file(p, "06", "Coinwy", [("Swapzone: Multi-Provider Rate", "swapzone"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap"), ("StealthEX:", "stealthex")])

# 07
for p in find_articles("coinwy/swapzone-batch/articles/07-btc-to-eth*.md"):
    process_file(p, "07", "Coinwy", [("Swapzone: Rate Comparison for BTC to ETH", "swapzone"), ("ChangeNOW:", "changenow"), ("Changelly:", "changelly"), ("SimpleSwap:", "simpleswap")])

# 08
for p in find_articles("coinwy/swapzone-batch/articles/08-eth-to-btc*.md"):
    process_file(p, "08", "Coinwy", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap"), ("StealthEX:", "stealthex")])

# 09
for p in find_articles("coinwy/swapzone-batch/articles/09-btc-to-trx*.md"):
    process_file(p, "09", "Coinwy", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap")])

# 10
for p in find_articles("coinwy/swapzone-batch/articles/10-best-ton*.md"):
    process_file(p, "10", "Coinwy", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap")])

# 11 vs article
for p in find_articles("coinwy/swapzone-batch/articles/11-swapzone-vs-changenow*.md"):
    process_vs_article(p, "11", [("Swapzone", "swapzone", "Coinwy"), ("ChangeNOW", "changenow", "Coinwy")])

# 12 vs article
for p in find_articles("coinwy/swapzone-batch/articles/12-swapzone-vs-swapspace*.md"):
    process_vs_article(p, "12", [("Swapzone", "swapzone", "Coinwy"), ("SwapSpace", "swapspace", "Coinwy")])

# 13
for p in find_articles("coinwy/swapzone-batch/articles/13-best-changenow*.md"):
    process_file(p, "13", "Coinwy", [("ChangeNOW:", "changenow"), ("StealthEX:", "stealthex"), ("SimpleSwap:", "simpleswap"), ("Exolix:", "exolix"), ("SwapSpace:", "swapspace")])

# 14
for p in find_articles("Kanalcoin/swapzone-batch/articles/14-no-kyc*.md"):
    process_file(p, "14", "Kanalcoin", [("Swapzone:", "swapzone"), ("StealthEX:", "stealthex"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap")])

# 15
for p in find_articles("Kanalcoin/swapzone-batch/articles/15-eur-to-btc*.md"):
    process_file(p, "15", "Kanalcoin", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow"), ("Changelly:", "changelly")])

# 16
for p in find_articles("Kanalcoin/swapzone-batch/articles/16-eur-to-xmr*.md"):
    process_file(p, "16", "Kanalcoin", [("Swapzone:", "swapzone"), ("StealthEX:", "stealthex"), ("Exolix:", "exolix")])

# 17
for p in find_articles("Kanalcoin/swapzone-batch/articles/17-dex-vs-cex*.md"):
    process_file(p, "17", "Kanalcoin", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow")])

# 18
for p in find_articles("DeFiLiban/swapzone-batch/articles/18-best-crypto-staking*.md"):
    process_file(p, "18", "DeFiLiban", [("Nexo:", "nexo")])

# 19
for p in find_articles("DeFiLiban/swapzone-batch/articles/19-best-crypto-loan*.md"):
    process_file(p, "19", "DeFiLiban", [("Nexo:", "nexo")])

# 20
for p in find_articles("Kanalcoin/swapzone-batch/articles/20-aud-to-btc*.md"):
    process_file(p, "20", "Kanalcoin", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow")])

print("\n=== Done ===")
