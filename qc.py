import sys, re
sys.stdout.reconfigure(encoding="utf-8")
with open("Kanalcoin/articles/14-best-crypto-casinos-halloween-2026.md", "r", encoding="utf-8") as f:
    content = f.read()

words = len(re.findall(r"\b\w+\b", content))
print("Word count:", words)
print()

checks = [
    ("SLOTOBER", "Rollbit SLOTOBER"),
    ("Persik333", "Reddit Gamdom confiscation"),
    ("AdTop8820", "Reddit Gamdom Keno"),
    ("High Roller", "Gamdom High Roller"),
    ("Target Hunter", "Target Hunter explained"),
    ("wildio-halloween-promo.png", "Wild.io screenshot"),
    ("bcgame-halloween-promo.png", "BC.Game screenshot"),
    ("trustpilot-bcgame.png", "Trustpilot BC.Game"),
    ("trustpilot-gamdom.png", "Trustpilot Gamdom"),
    ("beginner", "Beginner content"),
    ("FAQ", "FAQ section"),
    ("My Take", "Editorial section"),
    ("Oct 31", "Halloween date specific"),
    ("0.20", "Min bet mentioned"),
]
for needle, label in checks:
    found = needle in content
    status = "OK" if found else "MISSING"
    print(status, "-", label)
