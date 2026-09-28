import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tp_casino.json', encoding='utf-8') as f:
    tp = json.load(f)
with open('reddit_casino.json', encoding='utf-8') as f:
    reddit = json.load(f)

for platform in tp:
    reviews = tp[platform]
    total = len(reviews)
    avg = sum(r['rating'] for r in reviews)/total if total else 0
    pos = [r for r in reviews if r['rating']>=4 and len(r.get('text',''))>60]
    neg = [r for r in reviews if r['rating']<=2 and len(r.get('text',''))>60]
    print('=== ' + platform + ' (' + str(total) + ' reviews, avg ' + str(round(avg,1)) + ') pos=' + str(len(pos)) + ' neg=' + str(len(neg)))
    if pos:
        r=pos[0]
        print('  POS ' + str(r['rating']) + 'star ' + r['author'] + ': ' + r['text'][:100])
        print('  URL: ' + r['url'] + '  date: ' + r['date'][:10])
    if neg:
        r=neg[0]
        print('  NEG ' + str(r['rating']) + 'star ' + r['author'] + ': ' + r['text'][:100])
        print('  URL: ' + r['url'] + '  date: ' + r['date'][:10])
    print()

for platform in reddit:
    items = reddit[platform]
    print('--- ' + platform + ' (' + str(len(items)) + ' items) ---')
    for item in sorted(items, key=lambda x: x.get('score',0), reverse=True)[:3]:
        txt = (item.get('text') or item.get('title',''))[:120]
        print('  [' + str(item.get('score',0)) + '] u/' + item.get('author','') + ' r/' + item.get('subreddit','') + ': ' + txt)
    print()
