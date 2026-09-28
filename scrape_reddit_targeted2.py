import asyncio
import json
import urllib.parse
import cloakbrowser

REDDIT_COOKIES = [
    {"name": "reddit_session", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpsVFdYNlFVUEloWktaRG1rR0pVd1gvdWNFK01BSjBYRE12RU1kNzVxTXQ4IiwidHlwIjoiSldUIn0.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDE0ODgyMDguODM4NTAxLCJpYXQiOjE3ODU4NDk4MDguODM4NTAxLCJqdGkiOiJBa2NNMUpEWldYMEtiUzl5UnZzcTh4T3FpemVad1EiLCJhdCI6MSwiY2lkIjoiY29va2llIiwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnlLamdVRUFBRF9fd0VWQUxrIiwiZmxvIjozLCJhbXIiOlsic3NvIl19.RUuKGpf1m2T68RE9HorT_x5TXd_GWm7sKmFmoFqqZbjvj75O_vlh3H1fyHloOuC6K2hLdj7xdPUUF5ySXikXe69tkexQ-Ldnxv2t3Df2oLJ3YkLGCed_Nk44fifN4hf77wM18tVfwDViN34gGYW5JEiuAaLXDoYHIFW_YkOpchjVDVlrkHB9cYnxjKbvk0t1zOUNpEPfgsHQ_JFonLN_kfEoEI7pEQuA5AmGuIUgpO8i-HxKzivgbNGHuYvCCp20kJ97DuUvJvF1eFZkgPB_ad-FlAzvMzkQZVAfx4bbAbZBfUfWdtNpAr_Wgz4CT1FCxnghoA30DA4TxdrvjrzXbw", "domain": ".reddit.com", "path": "/"},
    {"name": "token_v2", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzg2NTIyODAzLjc5MTc1MSwiaWF0IjoxNzg2NDM2NDAzLjc5MTc1MSwianRpIjoiM0ZGcUhlMmpCTU0xcG5pa2RrVkRPb0V1UDNtSU9RIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhdCI6MSwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5feldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJyY2lkIjoiOXlUdUVWc2lieDZ0LWJpbFZlQVNDUFNZQlJtTVZXUmVSR1JncldjdHQzcyIsImZsbyI6Mn0.L-islac7kDH7l6F2UKhnGBJujKecYwSFkFQygRwjXGyKESTqXmGfWB_MAS6v2kyspgZMC57GMSvBBYVpvKeyM1IRnLd1p5xrUtsl0hESZ7L2MCADkDU3CH3qTG43D6ToQmGMcu73TmEy_bz5OW2Z3r79pRCnGzkZUdyc9h8oeAGBM3A_1LToPm9sO17Rp7kbGmSNrUCw55iihQtMpTbcuVc-6tSMHDBx5fXOqD9iHtn4880EnRYZMcCiuOCwIXbVZ7SvzgNOktdDwQ1vqGK-aCHdOby-rZ4uOvZZY2Di281ZjG9oEHYTs1N2HpgNavMi8Y0zwTBFfz4wcKy1d844sw", "domain": ".reddit.com", "path": "/"},
    {"name": "csrf_token", "value": "d83ef64ac116fbccb3282f74243ab73d", "domain": ".reddit.com", "path": "/"},
]

# Search WITHIN subreddit for posts with platform name in title, then take top comments
# Filter: post must be about the platform (title check), comment 60-500 chars, not deleted
SEARCHES = [
    ("01", "Swapzone", ["CryptoCurrency", "CryptoMarkets", "Bitcoin"], None),
    ("01", "StealthEX", ["CryptoCurrency", "Bitcoin"], None),
    ("01", "SimpleSwap", ["CryptoCurrency", "Bitcoin"], None),
    ("02", "aggregator exchange crypto", ["CryptoCurrency"], None),
    ("03", "no-KYC swap crypto", ["CryptoCurrency", "privacy"], None),
    ("04", "fixed rate swap", ["CryptoCurrency", "Bitcoin"], None),
    ("05", "Monero exchange", ["Monero", "CryptoCurrency"], "XMR"),
    ("05", "XMR no KYC exchange", ["Monero"], None),
    ("06", "USDT BTC swap", ["CryptoCurrency"], None),
    ("07", "BTC ETH exchange swap", ["CryptoCurrency"], None),
    ("08", "ETH BTC swap", ["CryptoCurrency"], None),
    ("09", "TRX Tron exchange", ["Tronix", "CryptoCurrency"], None),
    ("10", "Toncoin exchange", ["Toncoin", "CryptoCurrency"], None),
    ("11", "ChangeNOW", ["CryptoCurrency", "Bitcoin"], None),
    ("12", "SwapSpace exchange", ["CryptoCurrency"], None),
    ("13", "ChangeNOW alternative", ["CryptoCurrency"], None),
    ("14", "no KYC exchange", ["CryptoCurrency", "privacy"], None),
    ("15", "EUR bitcoin SEPA", ["CryptoCurrency", "eupersonalfinance"], None),
    ("16", "Monero euro buy", ["Monero"], None),
    ("17", "DEX versus CEX", ["CryptoCurrency", "defi"], None),
    ("18", "Lido staking", ["ethfinance", "CryptoCurrency"], None),
    ("18", "Rocket Pool", ["CryptoCurrency", "ethfinance"], None),
    ("19", "YouHodler", ["CryptoCurrency"], None),
    ("19", "Nexo loan", ["CryptoCurrency"], None),
    ("20", "CoinSpot", ["AusFinance", "CryptoCurrency"], None),
    ("20", "Swyftx", ["AusFinance", "CryptoCurrency"], None),
]

def is_good(body, author):
    if not body or not author:
        return False
    if author.lower() in ('[deleted]', '[removed]', 'automoderator', 'deleted', 'bot'):
        return False
    body = body.strip()
    if len(body) < 60 or len(body) > 700:
        return False
    if any(b in body.lower() for b in ['referral', 'ref link', 'use my code', 'promo code']):
        return False
    # Not just low-quality noise
    noise = ['!', 'lol', 'wow', 'nice', 'great', 'amazing', 'thanks']
    if all(n in body.lower() for n in ['lol']) and len(body) < 100:
        return False
    return True

async def fetch_api(page, url):
    result = await page.evaluate(f"""
    async () => {{
        try {{
            const r = await fetch({json.dumps(url)}, {{
                credentials: 'include',
                headers: {{'Accept': 'application/json'}}
            }});
            if (!r.ok) return {{error: r.status}};
            return await r.json();
        }} catch(e) {{ return {{error: e.toString()}}; }}
    }}
    """)
    return result

async def main():
    ctx = await cloakbrowser.launch_context_async(headless=True, viewport={"width": 1440, "height": 900})
    await ctx.add_cookies(REDDIT_COOKIES)
    
    page = await ctx.new_page()
    await page.goto("https://www.reddit.com/", timeout=15000)
    await asyncio.sleep(2)
    
    all_results = {}
    
    for art_id, query, subreddits, must_contain in SEARCHES:
        key = art_id.zfill(2)
        
        for sub in subreddits:
            enc = urllib.parse.quote(query)
            url = f"https://www.reddit.com/r/{sub}/search.json?q={enc}&restrict_sr=1&sort=top&t=all&limit=10"
            data = await fetch_api(page, url)
            
            if 'error' in data or 'data' not in data:
                continue
            
            posts = data['data'].get('children', [])
            
            for post in posts[:5]:
                pd = post.get('data', {})
                post_id = pd.get('id')
                num_c = pd.get('num_comments', 0)
                title = pd.get('title', '')
                
                if not post_id or num_c < 2:
                    continue
                
                # Post title must reference query term (loose check)
                q_words = [w.lower() for w in query.split() if len(w) > 3]
                if not any(qw in title.lower() for qw in q_words):
                    continue
                
                # Fetch top-level comments
                comments_url = f"https://www.reddit.com/r/{sub}/comments/{post_id}.json?limit=20&sort=top&depth=1"
                cr = await fetch_api(page, comments_url)
                
                if not isinstance(cr, list) or len(cr) < 2:
                    continue
                
                comments = cr[1].get('data', {}).get('children', [])
                for c in comments:
                    if c.get('kind') != 't1':
                        continue
                    cd = c.get('data', {})
                    author = cd.get('author', '')
                    body = cd.get('body', '')
                    score = cd.get('score', 0)
                    permalink = 'https://reddit.com' + cd.get('permalink', '')
                    
                    if not is_good(body, author):
                        continue
                    if must_contain and must_contain.lower() not in body.lower():
                        continue
                    
                    comment_data = {
                        'text': body[:500].strip(),
                        'author': author,
                        'permalink': permalink,
                        'score': score,
                        'subreddit': sub,
                        'post_title': title[:80],
                    }
                    
                    if key not in all_results:
                        all_results[key] = []
                    
                    # Avoid duplicates
                    if not any(c2['author'] == author for c2 in all_results[key]):
                        all_results[key].append(comment_data)
                        print(f"  Art{key}+{sub}: u/{author} (score={score}): {body[:80]}...")
                    
                    if len(all_results.get(key, [])) >= 6:
                        break
                
                if len(all_results.get(key, [])) >= 6:
                    break
                await asyncio.sleep(0.3)
            
            if len(all_results.get(key, [])) >= 6:
                break
        
        await asyncio.sleep(0.8)
    
    await page.close()
    await ctx.close()
    
    out = r"C:\Users\admin\Authority-Building\swapzone_reddit_targeted.json"
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"\nResults summary:")
    for k in sorted(all_results.keys()):
        v = all_results[k]
        print(f"  Art {k}: {len(v)} comments")

asyncio.run(main())
