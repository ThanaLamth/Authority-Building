import json
import re
import os

with open(r"C:\Users\admin\Authority-Building\trustpilot_platform_reviews.json", "r", encoding="utf-8") as f:
    tp_data = json.load(f)

PLATFORM_MAP = {
    "swapzone": "swapzone", "swapspace": "swapspace", "simpleswap": "simpleswap",
    "changenow": "changenow", "stealthex": "stealthex", "exolix": "exolix",
    "fixedfloat": "fixedfloat", "fixed float": "fixedfloat", "godex": "godex",
    "letsexchange": "letsexchange", "lets exchange": "letsexchange",
    "coinspot": "coinspot", "swyftx": "swyftx", "nexo": "nexo",
    "youhodler": "youhodler", "you hodler": "youhodler",
    "rocketpool": "rocketpool", "rocket pool": "rocketpool",
    "kraken": "kraken",
}

ARTICLES = {
    "11": r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\11-swapzone-vs-changenow.md",
    "12": r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\12-swapzone-vs-swapspace.md",
    "13": r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\13-best-changenow-alternatives-2026.md",
    "14": r"C:\Users\admin\Authority-Building\Kanalcoin\swapzone-batch\articles\14-no-kyc-crypto-exchanges-2026.md",
    "15": r"C:\Users\admin\Authority-Building\Kanalcoin\swapzone-batch\articles\15-eur-to-btc-exchange-2026.md",
    "16": r"C:\Users\admin\Authority-Building\Kanalcoin\swapzone-batch\articles\16-eur-to-xmr-exchange-2026.md",
    "17": r"C:\Users\admin\Authority-Building\Kanalcoin\swapzone-batch\articles\17-dex-vs-cex-vs-aggregator-2026.md",
    "18": r"C:\Users\admin\Authority-Building\DeFiLiban\swapzone-batch\articles\18-best-crypto-staking-platforms-2026.md",
    "19": r"C:\Users\admin\Authority-Building\DeFiLiban\swapzone-batch\articles\19-best-crypto-loan-platforms-2026.md",
    "20": r"C:\Users\admin\Authority-Building\Kanalcoin\swapzone-batch\articles\20-aud-to-btc-exchange-australia-2026.md",
}

def build_wus_block(platform_key):
    reviews = tp_data.get(platform_key, [])
    if not reviews:
        return None
    
    positives = sorted(
        [r for r in reviews if r.get('rating', 0) >= 4 and len(r.get('text', '')) > 100],
        key=lambda x: len(x.get('text', '')), reverse=True
    )
    criticals = sorted(
        [r for r in reviews if r.get('rating', 0) <= 2 and len(r.get('text', '')) > 100],
        key=lambda x: len(x.get('text', '')), reverse=True
    )
    
    pos = positives[0] if positives else None
    neg = criticals[0] if criticals else None
    
    if not pos and not neg:
        return None
    
    lines = ["\n**What users say**\n"]
    
    if pos:
        text = pos['text'][:350]
        if len(pos['text']) > 350:
            last_s = max(text.rfind('.'), text.rfind('!'), text.rfind('?'))
            if last_s > 200:
                text = text[:last_s+1]
        reviewer = pos['reviewer']
        date = pos.get('date', '')
        permalink = pos.get('permalink', '')
        star = chr(9733) * int(pos.get('rating', 5))
        lines.append("**Positive**")
        lines.append(f'> "{text}"')
        lines.append('>')
        if permalink:
            lines.append(f'> -- {reviewer}, [Trustpilot]({permalink}) ({star}, {date})')
        else:
            lines.append(f'> -- {reviewer}, Trustpilot ({star}, {date})')
        lines.append("")
    
    if neg:
        text = neg['text'][:350]
        if len(neg['text']) > 350:
            last_s = max(text.rfind('.'), text.rfind('!'), text.rfind('?'))
            if last_s > 200:
                text = text[:last_s+1]
        reviewer = neg['reviewer']
        date = neg.get('date', '')
        permalink = neg.get('permalink', '')
        star = chr(9733) * int(neg.get('rating', 1))
        lines.append("**Critical**")
        lines.append(f'> "{text}"')
        lines.append('>')
        if permalink:
            lines.append(f'> -- {reviewer}, [Trustpilot]({permalink}) ({star}, {date})')
        else:
            lines.append(f'> -- {reviewer}, Trustpilot ({star}, {date})')
        lines.append("")
    
    return "\n".join(lines)

def inject_tp_into_sections(filepath, article_id):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    section_pattern = re.compile(r'(### ([^\n]+))(.*?)(?=\n### |\Z)', re.DOTALL)
    
    modified = False
    result = content
    offset = 0
    
    for m in section_pattern.finditer(content):
        section_header = m.group(2).strip()
        section_text = m.group(3)
        
        if "**What users say**" in section_text:
            continue
        
        platform_key = None
        header_lower = section_header.lower()
        for name, key in PLATFORM_MAP.items():
            if name.lower() in header_lower or header_lower.startswith(name.lower()):
                platform_key = key
                break
        
        if not platform_key:
            continue
        
        wus = build_wus_block(platform_key)
        if not wus:
            continue
        
        section_end = m.end(3)
        actual_end = section_end + offset
        sec_start_in_result = m.start(3) + offset
        sec_text_in_result = result[sec_start_in_result:actual_end]
        
        stripped = sec_text_in_result.rstrip()
        insert_at = sec_start_in_result + len(stripped)
        
        result = result[:insert_at] + "\n" + wus + result[insert_at:]
        offset += len("\n" + wus)
        modified = True
        print(f"  Art {article_id} | ### {section_header}: injected {platform_key}")
    
    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(f"  Art {article_id}: no new sections to inject")
    
    return modified

for art_id, filepath in ARTICLES.items():
    if not os.path.exists(filepath):
        print(f"Art {art_id}: not found")
        continue
    print(f"\nArt {art_id}:")
    inject_tp_into_sections(filepath, art_id)

print("\nDone.")
