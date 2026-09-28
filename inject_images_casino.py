import os, sys
sys.stdout.reconfigure(encoding='utf-8')

# Map: (file, search_text_to_insert_after, image_md)
INJECTIONS = [
    # BC.Game review (Coincu)
    (
        r"C:\Users\admin\Authority-Building\Coincu\articles\14-bc-game-review-2026.md",
        "## Game library: 9,000+ titles across 100+ providers",
        "\n![BC.Game homepage showing casino, sports, and BC Originals sections](../media/casino-oct26/live-bcgame-homepage.png)\n*BC.Game homepage — casino lobby, sports betting, and BC Originals, September 2026.*\n"
    ),
    # Winna review (Coincu) - already has media in article from previous batch, skip - add to rollblock article
    (
        r"C:\Users\admin\Authority-Building\Coincu\articles\14-bc-game-review-2026.md",
        "## Bonuses and promotions",
        "\n![BC.Game game lobby showing category filters, provider list, and active promotions](../media/casino-oct26/live-bcgame-homepage.png)\n*BC.Game lobby: casino, sports, BC Originals, live casino, and crypto futures in one interface.*\n"
    ),
    # Kanalcoin No-KYC article
    (
        r"C:\Users\admin\Authority-Building\Kanalcoin\articles\11-best-no-kyc-crypto-casinos-2026.md",
        "### 3. BC.Game — No KYC with 150+ Cryptos",
        "\n![BC.Game homepage showing 150+ crypto support and sign-in options](../media/casino-oct26/live-bcgame-homepage.png)\n*BC.Game — 150+ cryptocurrencies accepted, no KYC required below threshold.*\n"
    ),
    (
        r"C:\Users\admin\Authority-Building\Kanalcoin\articles\11-best-no-kyc-crypto-casinos-2026.md",
        "### 5. Metaspins — Full Anonymity, BTC-Focused",
        "\n![Roobet homepage showing anonymous casino registration with no email or ID required](../media/casino-oct26/live-roobet-homepage.png)\n*Roobet — no email, no KYC, no ID at any withdrawal level.*\n"
    ),
    # Kanalcoin Vietnam article
    (
        r"C:\Users\admin\Authority-Building\Kanalcoin\articles\12-best-crypto-casinos-vietnam-2026.md",
        "### 1. BC.Game — Best for Vietnamese Players",
        "\n![BC.Game homepage with VND currency display and Vietnamese market support](../media/casino-oct26/live-bcgame-homepage.png)\n*BC.Game homepage — showing VND currency option, casino and sports navigation, September 2026.*\n"
    ),
    # Kanalcoin Stake Alternatives
    (
        r"C:\Users\admin\Authority-Building\Kanalcoin\articles\13-stake-alternatives-2026.md",
        "### 1. BC.Game — Best Alternative for New Players",
        "\n![BC.Game homepage demonstrating wider crypto support and sign-up options vs Stake.com](../media/casino-oct26/live-bcgame-homepage.png)\n*BC.Game — 150+ crypto deposits and 220% welcome bonus, two key advantages over Stake.com.*\n"
    ),
    (
        r"C:\Users\admin\Authority-Building\Kanalcoin\articles\13-stake-alternatives-2026.md",
        "### 6. Cloudbet — Best for High-Stakes and Longevity",
        "\n![Cloudbet homepage showing 50+ cryptocurrency support and high-roller sportsbook](../media/casino-oct26/live-cloudbet-homepage.png)\n*Cloudbet — operating since 2013, 50+ cryptocurrencies, dedicated high-roller service.*\n"
    ),
]

for fpath, needle, img_md in INJECTIONS:
    if not os.path.exists(fpath):
        print(f"MISSING: {fpath}")
        continue
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    if needle not in content:
        print(f"NEEDLE NOT FOUND in {os.path.basename(fpath)}: {needle[:40]}")
        continue
    # Only inject if image not already there
    img_filename = img_md.split('(')[1].split(')')[0].split('/')[-1]
    section_idx = content.index(needle)
    # Check if image already in next 300 chars
    if img_filename in content[section_idx:section_idx+400]:
        print(f"Already has image: {os.path.basename(fpath)}")
        continue
    # Insert after the heading line
    line_end = content.index('\n', section_idx) + 1
    new_content = content[:line_end] + img_md + content[line_end:]
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Injected into {os.path.basename(fpath)}: {img_filename}")

print("Image injection done.")
