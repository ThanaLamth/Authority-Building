import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tp_casino.json', encoding='utf-8') as f:
    tp = json.load(f)
with open('reddit_casino.json', encoding='utf-8') as f:
    reddit = json.load(f)

def pick_reviews(platform, n_pos=2, n_neg=2):
    reviews = tp.get(platform, [])
    pos = [r for r in reviews if r['rating']>=4 and len(r.get('text',''))>80][:n_pos]
    neg = [r for r in reviews if r['rating']<=2 and len(r.get('text',''))>60][:n_neg]
    return pos, neg

def pick_reddit(platform, n=2):
    items = reddit.get(platform, [])
    good = [i for i in items
            if i.get('author','') not in ['AutoModerator','[deleted]','']
            and len((i.get('text') or i.get('title','') or ''))>40
            and i.get('score',0)>=3]
    return sorted(good, key=lambda x: x.get('score',0), reverse=True)[:n]

def build_wus_block(platform, casino_name):
    pos, neg = pick_reviews(platform)
    reddits = pick_reddit(platform)
    reviews = tp.get(platform,[])
    total = len(reviews)
    avg = round(sum(r['rating'] for r in reviews)/total, 1) if total else 0

    lines = ['\n\n## What Users Say — ' + casino_name + '\n']
    lines.append('**Trustpilot:** ' + str(avg) + '/5 from sample of ' + str(total) + ' recent reviews (September 2026)\n')

    if pos:
        lines.append('\n**Positive:**\n')
        for r in pos:
            text = r['text'][:260].strip().replace('"',"'")
            date = r['date'][:10] if r.get('date') else ''
            lines.append('> "' + text + '"\n>\n> — ' + r['author'] + ', [' + str(r['rating']) + ' stars, Trustpilot](' + r['url'] + ') ' + date + '\n')

    if neg:
        lines.append('\n**Critical:**\n')
        for r in neg:
            text = r['text'][:260].strip().replace('"',"'")
            date = r['date'][:10] if r.get('date') else ''
            lines.append('> "' + text + '"\n>\n> — ' + r['author'] + ', [' + str(r['rating']) + ' star, Trustpilot](' + r['url'] + ') ' + date + '\n')

    if reddits:
        lines.append('\n**Reddit:**\n')
        for item in reddits:
            txt = (item.get('text') or item.get('title') or '').strip()[:220].replace('"',"'")
            score = item.get('score',0)
            author = item.get('author','')
            sub = item.get('subreddit','')
            url = item.get('url','')
            lines.append('> "' + txt + '"\n>\n> — u/' + author + ', [r/' + sub + '](' + url + ') (' + str(score) + ' points)\n')

    return '\n'.join(lines)

# Fix Rollblock article - remove wrongly added Winna WUS, add proper Rollblock WUS
rb_path = r'C:\Users\admin\Authority-Building\Coincu\articles\16-rollblock-review-2026.md'
with open(rb_path, encoding='utf-8') as f:
    content = f.read()

# Remove any existing WUS blocks from Winna
if '## What Users Say' in content:
    # Keep only up to first WUS block if it was the wrong one
    first_wus = content.index('## What Users Say')
    # Check if this is Winna or Rollblock
    snippet = content[first_wus:first_wus+50]
    if 'Winna' in snippet:
        content = content[:first_wus].rstrip()

# Add Rollblock WUS before FAQ
wus = build_wus_block('rollblock.io', 'Rollblock')
faq_idx = content.rfind('\n## FAQ')
if faq_idx > 0:
    content = content[:faq_idx] + '\n' + wus + '\n' + content[faq_idx:]
else:
    content = content + '\n' + wus

with open(rb_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed Rollblock article')

# Inject into CCpress roundup (Bai 1)
ccpress_path = r'C:\Users\admin\Authority-Building\CCpress\articles\24-best-crypto-casinos-october-2026.md'
with open(ccpress_path, encoding='utf-8') as f:
    content = f.read()

# Build combined WUS for top 3 casinos at CCpress
wus_stake = build_wus_block('stake.com', 'Stake.com')
wus_bc = build_wus_block('bc.game', 'BC.Game')
wus_1win = build_wus_block('1win.com', '1win')

# Inject after Stake section
for needle, wus in [('**Verdict:** The most defensible choice', wus_stake),
                    ('**Verdict:** Credible platform with real strengths', wus_bc),
                    ('**Verdict:** Strong choice for football', wus_1win)]:
    if needle in content:
        idx = content.index(needle) + len(needle)
        next_para = content.find('\n\n---', idx)
        if next_para == -1: next_para = content.find('\n---', idx)
        if next_para > 0:
            content = content[:next_para] + '\n' + wus + content[next_para:]

with open(ccpress_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Injected WUS into CCpress roundup')

# Inject into Kanalcoin Vietnam article (stake + bc.game data)
vn_path = r'C:\Users\admin\Authority-Building\Kanalcoin\articles\12-best-crypto-casinos-vietnam-2026.md'
with open(vn_path, encoding='utf-8') as f:
    content = f.read()

wus_stake_k = build_wus_block('stake.com', 'Stake.com')
wus_bc_k = build_wus_block('bc.game', 'BC.Game')

for needle, wus in [('**My take:** Stake is the strongest recommendation', wus_stake_k),
                    ('**My take:** BC.Game is the default recommendation', wus_bc_k)]:
    if needle in content:
        idx = content.index(needle) + len(needle)
        next_sec = content.find('\n---\n', idx)
        if next_sec > 0:
            content = content[:next_sec] + '\n' + wus + content[next_sec:]

with open(vn_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Injected WUS into Kanalcoin Vietnam article')

# Inject into Kanalcoin No-KYC article
nokyc_path = r'C:\Users\admin\Authority-Building\Kanalcoin\articles\11-best-no-kyc-crypto-casinos-2026.md'
with open(nokyc_path, encoding='utf-8') as f:
    content = f.read()

wus_roobet = build_wus_block('stake.com', 'Stake.com (no-KYC threshold)')

faq_idx = content.rfind('\n## FAQ')
if faq_idx > 0:
    content = content[:faq_idx] + '\n' + wus_roobet + '\n' + content[faq_idx:]

with open(nokyc_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Injected WUS into Kanalcoin No-KYC article')

print('All done.')
