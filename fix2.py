import sys
sys.stdout.reconfigure(encoding="utf-8")
with open("Kanalcoin/articles/14-best-crypto-casinos-halloween-2026.md", "r", encoding="utf-8") as f:
    content = f.read()

old_str = "If you specifically want to play the new Big Bass Halloween Splash 1000 slot within a competition, **Rollbit's $40,000 Pragmatic Play Hunt** qualifies exactly that. The multiplier-hunt format rewards a lucky big win rather than the biggest bankroll \u2014 a better format for most players."
new_str = "If you want the most variety in October competitions, **Rollbit's SLOTOBER + Target Hunters** is unmatched \u2014 10+ simultaneous promotions across different games, with outcome-based Target Hunter formats (hit a target win, earn a share) rather than wager races. Minimum bet on most events: $0.20\u20130.40."

if old_str in content:
    content = content.replace(old_str, new_str)
    print("My Take rollbit updated!")
else:
    print("Still not found. Trying with raw apostrophe...")
    idx = content.find("Rollbit's $40,000 Pragmatic Play Hunt")
    print("Rollbit Pragmatic Hunt at:", idx)

# Also update FAQ reference
old_faq = "**What is Big Bass Halloween Splash 1000 really a new game?**\nYes. Pragmatic Play released it on October 12, 2026 \u2014 confirmed by European Gaming's press release. It's the fourth Halloween entry in the Big Bass franchise, built on the Splash 1000 engine with Halloween theming, pumpkin modifiers, and medium volatility."
new_faq = "**Is Big Bass Halloween Splash 1000 really a new game?**\nYes. Pragmatic Play released it on October 12, 2026 \u2014 confirmed by European Gaming's press release. It's the fourth Halloween entry in the Big Bass franchise, built on the Splash 1000 engine with Halloween theming, pumpkin modifiers, and medium volatility. On Rollbit, you can target it via the SLOTOBER challenge list."

if old_faq in content:
    content = content.replace(old_faq, new_faq)
    print("FAQ updated")

with open("Kanalcoin/articles/14-best-crypto-casinos-halloween-2026.md", "w", encoding="utf-8") as f:
    f.write(content)
print("Saved. Length:", len(content))
