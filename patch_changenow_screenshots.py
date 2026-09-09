import re, os

BASE = r"C:\Users\admin\Authority-Building"

# (filepath, new_image_filename, new_alt_text, new_caption)
PATCHES = [
    # coinwy - comparison articles - show competitor homepage
    (os.path.join(BASE, "coinwy/changenow-batch/articles/04-changenow-vs-simpleswap-2026.md"),
     "live-simpleswap-homepage.png",
     "SimpleSwap homepage — interface comparison July 2026",
     "SimpleSwap's interface as captured in July 2026 for comparison with ChangeNOW."),
    (os.path.join(BASE, "coinwy/changenow-batch/articles/05-changenow-vs-changelly-2026.md"),
     "live-changelly-homepage.png",
     "Changelly homepage — interface comparison July 2026",
     "Changelly's homepage as captured in July 2026."),
    (os.path.join(BASE, "coinwy/changenow-batch/articles/06-changenow-vs-stealthex-2026.md"),
     "live-stealthex-homepage.png",
     "StealthEX homepage — interface comparison July 2026",
     "StealthEX's homepage as captured in July 2026."),
    # coinwy - pair-specific
    (os.path.join(BASE, "coinwy/changenow-batch/articles/07-btc-to-xmr-changenow-2026.md"),
     "live-changenow-btc-xmr.png",
     "ChangeNOW BTC to XMR swap widget — live rate July 2026",
     "ChangeNOW's BTC-to-XMR swap form showing live rate and recipient address field, captured July 2026."),
    (os.path.join(BASE, "coinwy/changenow-batch/articles/08-usdt-to-btc-changenow-2026.md"),
     "live-changenow-usdt-btc.png",
     "ChangeNOW USDT to BTC swap — live rate July 2026",
     "ChangeNOW's USDT-to-BTC form with live estimated rate, captured July 2026."),
    # kanalcoin - pair-specific
    (os.path.join(BASE, "Kanalcoin/changenow-batch/articles/10-eur-to-btc-changenow-2026.md"),
     "live-changenow-eur-btc.png",
     "ChangeNOW EUR to BTC buy form — Banxa and Guardarian providers shown, July 2026",
     "ChangeNOW's EUR-to-BTC buy form showing Banxa and Guardarian as fiat providers, captured July 2026."),
    (os.path.join(BASE, "Kanalcoin/changenow-batch/articles/11-changenow-fiat-buy-crypto-2026.md"),
     "live-changenow-fiat-buy.png",
     "ChangeNOW fiat buy crypto page — Buy/Sell tab July 2026",
     "ChangeNOW's Buy/Sell Crypto tab showing fiat on-ramp flow, captured July 2026."),
    (os.path.join(BASE, "Kanalcoin/changenow-batch/articles/13-eth-to-btc-changenow-2026.md"),
     "live-changenow-eth-btc.png",
     "ChangeNOW ETH to BTC swap — live estimated rate July 2026",
     "ChangeNOW's ETH-to-BTC swap form with live estimated rate, captured July 2026."),
    (os.path.join(BASE, "Kanalcoin/changenow-batch/articles/14-btc-to-eth-changenow-2026.md"),
     "live-changenow-btc-eth.png",
     "ChangeNOW BTC to ETH swap — live estimated rate July 2026",
     "ChangeNOW's BTC-to-ETH swap form with live estimated rate, captured July 2026."),
    # ccpress
    (os.path.join(BASE, "CCpress/changenow-batch/articles/15-changenow-api-review-2026.md"),
     "live-changenow-api-page.png",
     "ChangeNOW API documentation page — July 2026",
     "ChangeNOW's public API documentation page as captured in July 2026."),
    (os.path.join(BASE, "CCpress/changenow-batch/articles/16-is-changenow-legit-2026.md"),
     "live-changenow-trustpilot.png",
     "ChangeNOW Trustpilot page — 4.6 stars, 14K reviews, July 2026",
     "ChangeNOW's Trustpilot profile showing 4.6/5 rating and 14K+ reviews, captured July 2026."),
    # defiliban
    (os.path.join(BASE, "DeFiLiban/changenow-batch/articles/17-how-instant-crypto-swaps-work-2026.md"),
     "live-changenow-swap-widget.png",
     "ChangeNOW swap widget showing BTC-to-ETH custodial routing flow — July 2026",
     "ChangeNOW's swap execution interface demonstrating custodial routing mechanics, captured July 2026."),
    (os.path.join(BASE, "DeFiLiban/changenow-batch/articles/18-changenow-defi-alternative-2026.md"),
     "live-1inch-dex.png",
     "1inch DEX aggregator interface — on-chain swap comparison, July 2026",
     "1inch DEX aggregator interface for comparison with ChangeNOW's CeFi model, captured July 2026."),
]

# Regex to find and replace screenshot block (File/Alt/Caption line + markdown image)
IMG_BLOCK = re.compile(
    r'(File:\s*`\.\./media/)[^\n`]+(\.png`)\n'
    r'(Alt text:\s*")[^"]+(")\n'
    r'(Caption:\s*")[^"]+(")\n'
    r'(!\[[^\]]*\]\(\.\./media/)[^\)]+(\))\n'
    r'(\*[^\n]+\*)',
    re.MULTILINE
)

def patch_file(fp, new_img, new_alt, new_cap):
    if not os.path.exists(fp):
        print(f"  MISSING: {fp}")
        return False
    content = open(fp, encoding="utf-8").read()

    def replacer(m):
        img_stem = new_img.replace(".png", "")
        return (
            m.group(1) + new_img + m.group(2) + "\n" +
            m.group(3) + new_alt + m.group(4) + "\n" +
            m.group(5) + new_cap + m.group(6) + "\n" +
            m.group(7) + new_img + m.group(8) + "\n" +
            f"*{new_cap}*"
        )

    new_content, n = IMG_BLOCK.subn(replacer, content)
    if n > 0 and new_content != content:
        open(fp, "w", encoding="utf-8").write(new_content)
        print(f"  OK: {os.path.basename(fp)} -> {new_img}")
        return True
    else:
        # fallback: just replace the image filename in the markdown img tag
        new_content2 = re.sub(
            r'(\.\./media/)live-changenow-homepage\.png',
            r"\g<1>" + new_img,
            content
        )
        if new_content2 != content:
            open(fp, "w", encoding="utf-8").write(new_content2)
            print(f"  OK (fallback): {os.path.basename(fp)} -> {new_img}")
            return True
        print(f"  SKIPPED (no change): {os.path.basename(fp)}")
        return False

print("Patching article screenshot references...")
changed = 0
for fp, img, alt, cap in PATCHES:
    changed += patch_file(fp, img, alt, cap)
print(f"\nDone: {changed}/{len(PATCHES)} files patched.")
