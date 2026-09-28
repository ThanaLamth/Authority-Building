import asyncio
import json
import urllib.parse
import cloakbrowser

REDDIT_COOKIES = [
    {"name": "reddit_session", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpsVFdYNlFVUEloWktaRG1rR0pVd1gvdWNFK01BSjBYRE12RU1kNzVxTXQ4IiwidHlwIjoiSldUIn0.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDE0ODgyMDguODM4NTAxLCJpYXQiOjE3ODU4NDk4MDguODM4NTAxLCJqdGkiOiJBa2NNMUpEWldYMEtiUzl5UnZzcTh4T3FpemVad1EiLCJhdCI6MSwiY2lkIjoiY29va2llIiwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnlLamdVRUFBRF9fd0VWQUxrIiwiZmxvIjozLCJhbXIiOlsic3NvIl19.RUuKGpf1m2T68RE9HorT_x5TXd_GWm7sKmFmoFqqZbjvj75O_vlh3H1fyHloOuC6K2hLdj7xdPUUF5ySXikXe69tkexQ-Ldnxv2t3Df2oLJ3YkLGCed_Nk44fifN4hf77wM18tVfwDViN34gGYW5JEiuAaLXDoYHIFW_YkOpchjVDVlrkHB9cYnxjKbvk0t1zOUNpEPfgsHQ_JFonLN_kfEoEI7pEQuA5AmGuIUgpO8i-HxKzivgbNGHuYvCCp20kJ97DuUvJvF1eFZkgPB_ad-FlAzvMzkQZVAfx4bbAbZBfUfWdtNpAr_Wgz4CT1FCxnghoA30DA4TxdrvjrzXbw", "domain": ".reddit.com", "path": "/"},
    {"name": "token_v2", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzg2NTIyODAzLjc5MTc1MSwiaWF0IjoxNzg2NDM2NDAzLjc5MTc1MSwianRpIjoiM0ZGcUhlMmpCTU0xcG5pa2RrVkRPb0V1UDNtSU9RIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhdCI6MSwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5feldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJyY2lkIjoiOXlUdUVWc2lieDZ0LWJpbFZlQVNDUFNZQlJtTVZXUmVSR1JncldjdHQzcyIsImZsbyI6Mn0.L-islac7kDH7l6F2UKhnGBJujKecYwSFkFQygRwjXGyKESTqXmGfWB_MAS6v2kyspgZMC57GMSvBBYVpvKeyM1IRnLd1p5xrUtsl0hESZ7L2MCADkDU3CH3qTG43D6ToQmGMcu73TmEy_bz5OW2Z3r79pRCnGzkZUdyc9h8oeAGBM3A_1LToPm9sO17Rp7kbGmSNrUCw55iihQtMpTbcuVc-6tSMHDBx5fXOqD9iHtn4880EnRYZMcCiuOCwIXbVZ7SvzgNOktdDwQ1vqGK-aCHdOby-rZ4uOvZZY2Di281ZjG9oEHYTs1N2HpgNavMi8Y0zwTBFfz4wcKy1d844sw", "domain": ".reddit.com", "path": "/"},
    {"name": "csrf_token", "value": "d83ef64ac116fbccb3282f74243ab73d", "domain": ".reddit.com", "path": "/"},
]

# Platform -> targeted subreddit queries (use exact platform name + restrict_sr=1 for subreddit)
PLATFORM_SEARCHES = [
    # (article_ids, query, subreddits)
    (["01"], "Swapzone", ["CryptoCurrency", "CryptoMarkets"]),
    (["01"], "StealthEX exchange", ["CryptoCurrency"]),
    (["01", "03", "13"], "SimpleSwap exchange", ["CryptoCurrency", "Bitcoin"]),
    (["01", "13"], "SwapSpace exchange", ["CryptoCurrency"]),
    (["02"], "crypto exchange aggregator compare rates", ["CryptoCurrency"]),
    (["03"], "no KYC swap exchange anonymous", ["CryptoCurrency", "privacy"]),
    (["04"], "fixed rate crypto swap fees", ["CryptoCurrency"]),
    (["05"], "Monero XMR exchange no KYC", ["Monero", "CryptoCurrency"]),
    (["06"], "USDT to BTC exchange best rate", ["CryptoCurrency"]),
    (["07", "08"], "BTC ETH swap exchange rate", ["CryptoCurrency", "Bitcoin"]),
    (["09"], "Tron TRX exchange crypto", ["Tronix", "CryptoCurrency"]),
    (["10"], "Toncoin TON exchange buy", ["Toncoin", "CryptoCurrency"]),
    (["11"], "ChangeNOW exchange review", ["CryptoCurrency"]),
    (["12"], "SwapSpace exchange review", ["CryptoCurrency"]),
    (["13"], "ChangeNOW alternatives exchange", ["CryptoCurrency"]),
    (["14"], "anonymous crypto swap no verification", ["CryptoCurrency", "privacy"]),
    (["15"], "EUR BTC exchange SEPA bank transfer", ["CryptoCurrency", "eupersonalfinance"]),
    (["16"], "buy Monero euro EUR XMR", ["Monero"]),
    (["17"], "DEX decentralized exchange vs CEX", ["CryptoCurrency", "defi"]),
    (["18"], "Lido staking ETH liquid staking", ["ethfinance", "CryptoCurrency"]),
    (["19"], "YouHodler Nexo crypto loan borrow", ["CryptoCurrency"]),
    (["20"], "CoinSpot Swyftx Australia crypto AUD", ["AusFinance", "CryptoCurrency"]),
]

def is_good_comment(body, author, subreddit, query_keywords):
    if not body or not author:
        return False
    if author.lower() in ('[deleted]', '[removed]', 'automoderator', 'deleted'):
        return False
    body = body.strip()
    if len(body) < 60 or len(body) > 700:
        return False
    bad = ['referral', 'ref link', 'use my code', 'http://bit.ly', 'promo code']
    if any(b in body.lower() for b in bad):
        return False
    # Check if comment mentions at least one keyword
    kws = [k.lower() for k in query_keywords]
    body_lower = body.lower()
    has_kw = any(kw in body_lower for kw in kws)
    return has_kw

async def fetch_api(page, url):
    result = await page.evaluate(f"""
    async () => {{
        try {{
            const r = await fetch({json.dumps(url)}, {{
                credentials: 'include',
                headers: {{'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}}
            }});
            if (!r.ok) return {{error: r.status}};
            return await r.json();
        }} catch(e) {{
            return {{error: e.toString()}};
        }}
    }}
    """)
    return result

async def main():
    ctx = await cloakbrowser.launch_context_async(headless=True, viewport={"width": 1440, "height": 900})
    await ctx.add_cookies(REDDIT_COOKIES)
    
    page = await ctx.new_page()
    await page.goto("https://www.reddit.com/", timeout=15000)
    await asyncio.sleep(3)
    
    # Initialize results per article
    all_results = {str(i).zfill(2): [] for i in range(1, 21)}
    # Fix key format
    all_results = {f"{i:02d}" if i < 10 else str(i): [] for i in range(1, 21)}
    
    for article_ids, query, subreddits in PLATFORM_SEARCHES:
        # Extract keywords from query
        keywords = [w for w in query.split() if len(w) > 3]
        
        for sub in subreddits:
            enc_q = urllib.parse.quote(query)
            search_url = f"https://www.reddit.com/r/{sub}/search.json?q={enc_q}&restrict_sr=1&sort=top&t=all&limit=8"
            data = await fetch_api(page, search_url)
            
            if 'error' in data:
                continue
            
            posts = data.get('data', {}).get('children', [])
            print(f"  Query='{query[:35]}' r/{sub}: {len(posts)} posts")
            
            found_comments = 0
            for post in posts[:4]:
                if found_comments >= 4:
                    break
                pd = post.get('data', {})
                post_id = pd.get('id')
                if not post_id or pd.get('num_comments', 0) < 1:
                    continue
                
                # Check post title has keyword relevance
                title = pd.get('title', '').lower()
                if not any(kw.lower() in title for kw in keywords):
                    continue
                
                comments_url = f"https://www.reddit.com/r/{sub}/comments/{post_id}.json?limit=20&sort=top"
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
                    
                    if is_good_comment(body, author, sub, keywords):
                        comment_data = {
                            'text': body[:500].strip(),
                            'author': author,
                            'permalink': permalink,
                            'score': score,
                            'subreddit': sub,
                            'post_title': pd.get('title', '')[:80],
                        }
                        for art_id in article_ids:
                            normalized = art_id.zfill(2)
                            # Only add if not too many already
                            if len(all_results.get(normalized, [])) < 8:
                                all_results.setdefault(normalized, []).append(comment_data)
                                found_comments += 1
                                print(f"    +comment for {normalized}: u/{author} (score={score}): {body[:80]}...")
                        if found_comments >= 4:
                            break
                
                await asyncio.sleep(0.4)
        await asyncio.sleep(1)
    
    await page.close()
    await ctx.close()
    
    out = r"C:\Users\admin\Authority-Building\swapzone_reddit_targeted.json"
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"\nSaved: {out}")
    for k, v in sorted(all_results.items()):
        if v:
            print(f"  Article {k}: {len(v)} comments -- {v[0]['text'][:80]}...")
        else:
            print(f"  Article {k}: 0 comments")

asyncio.run(main())
