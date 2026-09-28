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

def pick_reddit(platform, n=3):
    items = reddit.get(platform, [])
    # Filter out spam/deleted
    good = [i for i in items
            if i.get('author','') not in ['AutoModerator','[deleted]','']
            and len((i.get('text') or i.get('title','')or''))>40
            and i.get('score',0)>=3]
    return sorted(good, key=lambda x: x.get('score',0), reverse=True)[:n]

def build_wus_block(platform, casino_name):
    pos, neg = pick_reviews(platform)
    reddits = pick_reddit(platform)

    lines = ['\n---\n', '## What Users Say\n']

    # Trustpilot score
    reviews = tp.get(platform,[])
    total = len(reviews)
    avg = round(sum(r['rating'] for r in reviews)/total, 1) if total else 0
    lines.append(f'**Trustpilot:** {avg}/5 from {total}+ reviews (sample, September 2026)\n')

    if pos:
        lines.append('\n**Positive reviews:**\n')
        for r in pos:
            text = r['text'][:280].strip()
            date = r['date'][:10] if r.get('date') else ''
            lines.append(f'> "{text}"\n>\n> — {r["author"]}, [{r["rating"]} stars, Trustpilot]({r["url"]}) {date}\n')

    if neg:
        lines.append('\n**Critical reviews:**\n')
        for r in neg:
            text = r['text'][:280].strip()
            date = r['date'][:10] if r.get('date') else ''
            lines.append(f'> "{text}"\n>\n> — {r["author"]}, [{r["rating"]} star, Trustpilot]({r["url"]}) {date}\n')

    if reddits:
        lines.append('\n**Reddit community signals:**\n')
        for item in reddits:
            txt = (item.get('text') or item.get('title') or '').strip()[:260]
            score = item.get('score',0)
            author = item.get('author','')
            sub = item.get('subreddit','')
            url = item.get('url','')
            lines.append(f'> "{txt}"\n>\n> — u/{author}, [r/{sub}]({url}) ({score} points)\n')

    return '\n'.join(lines)

# --- Platform map: (tp_key, casino_name, article_path, inject_after_pattern) ---
INJECT_MAP = [
    {
        'tp_key': 'stake.com',
        'name': 'Stake.com',
        'file': r'C:\Users\admin\Authority-Building\Coincu\articles\12-best-crypto-casinos-october-2026.md',
        'after': '**My take:** Stake.com is the benchmark.',
    },
    {
        'tp_key': 'bc.game',
        'name': 'BC.Game',
        'file': r'C:\Users\admin\Authority-Building\Coincu\articles\14-bc-game-review-2026.md',
        'after': '## Community reputation signals',
    },
    {
        'tp_key': '1win.com',
        'name': '1win',
        'file': r'C:\Users\admin\Authority-Building\Coincu\articles\15-1win-review-2026.md',
        'after': '## Community reputation signals',
    },
    {
        'tp_key': 'jack.com',
        'name': 'Jack.com',
        'file': r'C:\Users\admin\Authority-Building\Coincu\articles\13-jack-casino-review-2026.md',
        'after': '## Community reputation signals',
    },
    {
        'tp_key': 'winna.com',
        'name': 'Winna',
        'file': r'C:\Users\admin\Authority-Building\Coincu\articles\16-rollblock-review-2026.md',
        'after': None,  # append at end
    },
    {
        'tp_key': 'rollblock.io',
        'name': 'Rollblock',
        'file': r'C:\Users\admin\Authority-Building\Coincu\articles\16-rollblock-review-2026.md',
        'after': '## Community reputation and trust signals',
    },
]

for cfg in INJECT_MAP:
    fpath = cfg['file']
    if not os.path.exists(fpath):
        print(f'MISSING: {fpath}')
        continue

    with open(fpath, encoding='utf-8') as f:
        content = f.read()

    wus = build_wus_block(cfg['tp_key'], cfg['name'])

    after = cfg.get('after')
    if after and after in content:
        # Insert WUS block right after the matched line's paragraph
        idx = content.index(after) + len(after)
        # Find end of that paragraph (next blank line after the match)
        next_nl = content.find('\n\n', idx)
        if next_nl == -1:
            next_nl = len(content)
        new_content = content[:next_nl] + '\n' + wus + content[next_nl:]
    else:
        # Append before last FAQ section or at end
        faq_idx = content.rfind('\n## FAQ')
        if faq_idx > 0:
            new_content = content[:faq_idx] + '\n' + wus + '\n' + content[faq_idx:]
        else:
            new_content = content + '\n' + wus

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Injected WUS into {os.path.basename(fpath)} ({cfg["name"]})')

print('Done.')
