import sys
sys.stdout.reconfigure(encoding="utf-8")
with open("Kanalcoin/articles/14-best-crypto-casinos-halloween-2026.md", "r", encoding="utf-8") as f:
    content = f.read()

old_rollbit_mytake = "If you specifically want to play the new Big Bass Halloween Splash 1000 slot within a competition, **Rollbit\u2019s $40,000 Pragmatic Play Hunt** qualifies exactly that. The multiplier-hunt format rewards a lucky big win rather than the biggest bankroll \u2014 a better format for most players."
new_rollbit_mytake = "If you want the most variety in October competitions, **Rollbit\u2019s SLOTOBER + Target Hunters** is unmatched \u2014 10+ simultaneous promotions across different games, with outcome-based Target Hunter formats (hit a target win, earn a share) rather than wager races. Minimum bet on most events is $0.20\u20130.40."

if old_rollbit_mytake in content:
    content = content.replace(old_rollbit_mytake, new_rollbit_mytake)
    print("My Take rollbit updated!")
else:
    # Try raw find
    idx = content.find("Big Bass Halloween Splash 1000 slot")
    print("Not found. Big Bass at:", idx)
    if idx > 0:
        segment = content[idx-300:idx+400]
        print(repr(segment))

with open("Kanalcoin/articles/14-best-crypto-casinos-halloween-2026.md", "w", encoding="utf-8") as f:
    f.write(content)
print("Saved. Length:", len(content))
