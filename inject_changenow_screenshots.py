import re, os

BASE = r"C:\Users\admin\Authority-Building"
CW = os.path.join(BASE, "coinwy", "changenow-batch")

# (filepath, image, alt, caption)
INJECT = [
    (os.path.join(CW, "articles/03-changenow-review-2026.md"),
     "live-changenow-homepage.png",
     "ChangeNOW homepage — swap interface July 2026",
     "ChangeNOW's swap interface showing BTC-to-ETH rate, captured July 2026."),
    (os.path.join(CW, "articles/04-changenow-vs-simpleswap-2026.md"),
     "live-simpleswap-homepage.png",
     "SimpleSwap homepage — interface comparison July 2026",
     "SimpleSwap's interface captured in July 2026 for direct comparison with ChangeNOW."),
    (os.path.join(CW, "articles/05-changenow-vs-changelly-2026.md"),
     "live-changelly-homepage.png",
     "Changelly homepage — interface comparison July 2026",
     "Changelly's homepage as captured in July 2026."),
    (os.path.join(CW, "articles/06-changenow-vs-stealthex-2026.md"),
     "live-stealthex-homepage.png",
     "StealthEX homepage — interface comparison July 2026",
     "StealthEX's homepage as captured in July 2026."),
    (os.path.join(CW, "articles/07-btc-to-xmr-changenow-2026.md"),
     "live-changenow-btc-xmr.png",
     "ChangeNOW BTC to XMR swap — live rate and XMR recipient field, July 2026",
     "ChangeNOW's BTC-to-XMR swap form showing 157 XMR rate with recipient address field, captured July 2026."),
    (os.path.join(CW, "articles/08-usdt-to-btc-changenow-2026.md"),
     "live-changenow-usdt-btc.png",
     "ChangeNOW USDT to BTC swap — live estimated rate July 2026",
     "ChangeNOW's USDT-to-BTC swap form with live rate, captured July 2026."),
]

# Screenshot block template
def make_block(img, alt, cap):
    return f"""**Screenshot**
File: `../media/{img}`
Alt text: "{alt}"
Caption: "{cap}"
![{alt}](../media/{img})
*{cap}*"""

# Insert after the first markdown table (after first | ... | line block)
TABLE_END = re.compile(r'(\|[^\n]+\|\n)+', re.MULTILINE)

def inject_screenshot(fp, img, alt, cap):
    if not os.path.exists(fp):
        print(f"  MISSING: {fp}")
        return False
    content = open(fp, encoding="utf-8").read()

    # Already has image
    if "![" in content:
        print(f"  SKIP (has img): {os.path.basename(fp)}")
        return False

    block = "\n" + make_block(img, alt, cap) + "\n"

    # Find end of first table and insert after it
    m = TABLE_END.search(content)
    if m:
        insert_pos = m.end()
        new_content = content[:insert_pos] + block + content[insert_pos:]
        open(fp, "w", encoding="utf-8").write(new_content)
        print(f"  OK (after table): {os.path.basename(fp)} -> {img}")
        return True
    else:
        # fallback: insert after first --- separator
        sep = content.find("\n---\n", content.find("---\n") + 4)
        if sep >= 0:
            insert_pos = sep + 5
            new_content = content[:insert_pos] + block + content[insert_pos:]
            open(fp, "w", encoding="utf-8").write(new_content)
            print(f"  OK (after separator): {os.path.basename(fp)} -> {img}")
            return True
        print(f"  ERROR: no insertion point for {os.path.basename(fp)}")
        return False

print("Injecting screenshot blocks into articles 03-08...")
changed = 0
for fp, img, alt, cap in INJECT:
    changed += inject_screenshot(fp, img, alt, cap)
print(f"\nDone: {changed}/{len(INJECT)} articles updated.")
