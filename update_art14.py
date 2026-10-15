import sys, re
sys.stdout.reconfigure(encoding="utf-8")

FILEPATH = "Kanalcoin/articles/14-best-crypto-casinos-halloween-2026.md"
with open(FILEPATH, "r", encoding="utf-8") as f:
    content = f.read()

changes = []

# 1. meta_description
old = "Best crypto casinos for Halloween 2026 \u2014 Gamdom $50K Spooky Hill, Rollbit $40K Pragmatic Hunt, Wild.io $5K + free spins. Live-verified events, beginner guide to RTP and bonuses."
new = "Best crypto casinos for Halloween 2026 \u2014 Gamdom $50K Spooky Hill + $35K High Roller Oct 31, Rollbit SLOTOBER $20K mystery bounties, Wild.io $5K + free spins. Live-verified Oct 15 2026."
if old in content:
    content = content.replace(old, new)
    changes.append("meta_description updated")

# 2. comparison table rollbit row
old2 = "| **Rollbit** | Pragmatic Play $40K Halloween | **$40,000** | Oct (current) | Slot multiplier hunters |"
new2 = "| **Rollbit** | SLOTOBER $20K + 10+ Target Hunters | **$20,000+** | All October | Slot hunters, multiplier fans |"
if old2 in content:
    content = content.replace(old2, new2)
    changes.append("table rollbit row updated")

# 3. Add Gamdom High Roller row
old3 = "| **Gamdom** | 30K Spooktacular Showdown | **$30,000** | October | Mixed: tournament + drops |"
new3 = "| **Gamdom** | 30K Spooktacular Showdown | **$30,000** | October | Mixed: tournament + drops |\n| **Gamdom** | $50K Exclusive High Roller | **$35,000** leaderboard | Oct 31\u2013Nov 4 | High rollers (elite) |"
if old3 in content:
    content = content.replace(old3, new3)
    changes.append("gamdom high roller row added")

# 4. Source verification line
old4 = "Rollbit $40K confirmed via [blog.rollbit.com](https://blog.rollbit.com/author/michael/)."
new4 = 'Rollbit SLOTOBER $20K confirmed via [blog.rollbit.com/tag/promotions](https://blog.rollbit.com/tag/promotions/) \u2014 "SLOTOBER HAS ARRIVED! With it comes $20,000 in mystery bounties spread across 31 challenges on 31 of our most popular games."'
if old4 in content:
    content = content.replace(old4, new4)
    changes.append("source verification updated")

print("Changes made:", changes)
print("Old content length:", len(content))

# 5. Replace Rollbit section body
ROLLBIT_OLD = """### 2. Rollbit \u2014 $40,000 Pragmatic Play Halloween Competition \u2b50 Best Multiplier Event

**What the event is:**
Rollbit is running an exclusive $40,000 Halloween competition in partnership with Pragmatic Play. This is not a standard wager race (whoever bets the most wins). It\u2019s a **Multiplier Hunt** \u2014 you earn points by hitting high win multipliers within eligible slots.

**How the point system works:**
- Hit a 20x win or more \u2192 10 points
- Hit a 50x win or more \u2192 50 points
- Hit a 100x win or more \u2192 100 points
- Hit a 250x win \u2192 200 points
- Hit a 500x win \u2192 400 points
- Hit a 1,000x win \u2192 600 points
- Hit a 2,000x win \u2192 1,000 points

**Why this format is more beginner-friendly than a wager race:**
In a pure wager race, the richest player wins by simply betting the most money. In a Multiplier Hunt, a player betting $0.40 per spin who hits a 500x win earns 400 points \u2014 competing directly with someone betting $100 who also hits 500x. The minimum qualifying bet is **$0.40** \u2014 genuinely accessible.

**How Rollbit\u2019s RLB token adds value:**
Rollbit has its own token (RLB). When you hold RLB, you earn passive income from the casino\u2019s house edge \u2014 distributed automatically to stakers. This means active players during the Halloween competition earn prize pool points *plus* passive RLB staking distributions simultaneously. It\u2019s like getting two return streams from one gaming session.

**What users say:**

> "Once the same Pragmatic Play title is available at several casinos, the casino around the game matters more than the game itself."
>
> \u2014 r/AR15QandA, [Big Bass Halloween Splash 1000 Released Today](https://www.reddit.com/r/AR15QandA/comments/1x3x3w2/big_bass_halloween_splash_1000_released_today/), October 12, 2026

| Detail | Value |
|---|---|
| Event | Pragmatic Play $40K Halloween Competition |
| Prize Pool | $40,000 |
| Format | Multiplier Hunt (points per win multiplier) |
| Min. Bet | $0.40 |
| RLB Staking | Yes (passive rakeback) |
| No-KYC | Yes |"""

if ROLLBIT_OLD in content:
    ROLLBIT_NEW = """### 2. Rollbit \u2014 SLOTOBER $20K + October Target Hunters \u2b50 Most Active Promotions

**What SLOTOBER is:**
Rollbit has branded all of October 2026 as "SLOTOBER" \u2014 a month-long campaign running **$20,000 in mystery bounties** across 31 challenges on 31 popular games. Each challenge is tied to a specific slot or game. Complete the challenge (hit a required multiplier, reach a win target) and you claim that game\u2019s hidden prize. Three challenges pay **$2,000 each** and six challenges pay **$1,000 each**.

**Beginner explanation \u2014 what a Target Hunter promotion is:**
Rollbit also runs multiple concurrent "Target Hunter" events. A Target Hunter tells you: "hit a 250x win on [specific game] and earn a share of the prize pool." Unlike leaderboards where only the top 10 finish, Target Hunters reward *any* player who hits the target during the event window. Think of it like a stamp card: complete the goal, get the reward. Volume doesn\u2019t determine winners \u2014 specific outcomes do.

> **Source:** Rollbit official blog, [blog.rollbit.com/tag/promotions](https://blog.rollbit.com/tag/promotions/), October 2026 \u2014 *"SLOTOBER HAS ARRIVED! With it comes $20,000 in mystery bounties spread across 31 challenges on 31 of our most popular games. Complete a challenge to claim that game\u2019s hidden bounty. The prize is a mystery."*

**Active October Target Hunters and Blitzes (verified Oct 2026):**
| Game | Prize Pool | Format |
|---|---|---|
| Le Vampire (Hacksaw Gaming) | **$8,000** | Target Hunter |
| Cub Cabana (Kitsune Studios, early access) | **$20,000** | Blitz: every 200x+ win |
| Animo City Roulette | **$8,000** | Single-number 30x+ win |
| VS Slots (Johnny vs Chicken + others) | **$8,000** | Target Hunter |
| Fury of Anubis + Ra vs Osiris (Pragmatic) | **$15,000** | Highest Combined Multiplier |
| Moon Rush (Pragmatic Play) | **$8,000** | Target Hunter |
| Barbarossa Dragon Empire (boosted RTP) | **$20,000** | Blitz |
| Legacy of Dead (Play\u2019N Go) | **$10,000** | Target Hunter (up to 5 shares) |
| Epic Ze Zeus (Hacksaw Gaming) | **$5,000 + $250** | Target Hunter + highest bet bonus |
| BGaming Blitz (eligible BGaming slots) | **$20,000** | Every 150x win earns a share |

**What users say:**

> "Once the same Pragmatic Play title is available at several casinos, the casino around the game matters more than the game itself."
>
> \u2014 r/AR15QandA, [Big Bass Halloween Splash 1000 Released Today](https://www.reddit.com/r/AR15QandA/comments/1x3x3w2/big_bass_halloween_splash_1000_released_today/), October 12, 2026

| Detail | Value |
|---|---|
| Main October Event | SLOTOBER ($20,000 mystery bounties, 31 challenges) |
| Concurrent Target Hunters | 10+ active simultaneously |
| Format | Target Hunter + Blitz (outcome-based, not wager-based) |
| Min. Bet | $0.20\u2013$0.40 per spin |
| RLB Staking | Yes (passive rakeback on all bets) |
| No-KYC | Yes |"""
    content = content.replace(ROLLBIT_OLD, ROLLBIT_NEW)
    changes.append("rollbit section replaced")
    print("Rollbit section replaced!")
else:
    print("ERROR: Rollbit old section not found exactly")
    # Debug: find partial match
    idx = content.find("### 2. Rollbit")
    if idx > 0:
        print("Found heading at", idx)
        snippet = content[idx:idx+200]
        print(repr(snippet))

print("All changes:", changes)
with open(FILEPATH, "w", encoding="utf-8") as f:
    f.write(content)
print("File saved successfully. Length:", len(content))
