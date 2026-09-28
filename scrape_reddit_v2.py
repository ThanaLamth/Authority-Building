import asyncio
import json
import urllib.parse
import cloakbrowser

REDDIT_COOKIES = [
    {"name": "reddit_session", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDE0ODgyMDguODM4NTAxLCJpYXQiOjE3ODU4NDk4MDguODM4NTAxfQ.eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpsVFdYNlFVUEloWktaRG1rR0pVd1gvdWNFK01BSjBYRE12RU1kNzVxTXQ4IiwidHlwIjoiSldUIn0.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDE0ODgyMDguODM4NTAxLCJpYXQiOjE3ODU4NDk4MDguODM4NTAxLCJqdGkiOiJBa2NNMUpEWldYMEtiUzl5UnZzcTh4T3FpemVad1EiLCJhdCI6MSwiY2lkIjoiY29va2llIiwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnlLamdVRUFBRF9fd0VWQUxrIiwiZmxvIjozLCJhbXIiOlsic3NvIl19.RUuKGpf1m2T68RE9HorT_x5TXd_GWm7sKmFmoFqqZbjvj75O_vlh3H1fyHloOuC6K2hLdj7xdPUUF5ySXikXe69tkexQ-Ldnxv2t3Df2oLJ3YkLGCed_Nk44fifN4hf77wM18tVfwDViN34gGYW5JEiuAaLXDoYHIFW_YkOpchjVDVlrkHB9cYnxjKbvk0t1zOUNpEPfgsHQ_JFonLN_kfEoEI7pEQuA5AmGuIUgpO8i-HxKzivgbNGHuYvCCp20kJ97DuUvJvF1eFZkgPB_ad-FlAzvMzkQZVAfx4bbAbZBfUfWdtNpAr_Wgz4CT1FCxnghoA30DA4TxdrvjrzXbw", "domain": ".reddit.com", "path": "/"},
    {"name": "token_v2", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzg2NTIyODAzLjc5MTc1MSwiaWF0IjoxNzg2NDM2NDAzLjc5MTc1MSwianRpIjoiM0ZGcUhlMmpCTU0xcG5pa2RrVkRPb0V1UDNtSU9RIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhdCI6MSwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5feldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJyY2lkIjoiOXlUdUVWc2lieDZ0LWJpbFZlQVNDUFNZQlJtTVZXUmVSR1JncldjdHQzcyIsImZsbyI6Mn0.L-islac7kDH7l6F2UKhnGBJujKecYwSFkFQygRwjXGyKESTqXmGfWB_MAS6v2kyspgZMC57GMSvBBYVpvKeyM1IRnLd1p5xrUtsl0hESZ7L2MCADkDU3CH3qTG43D6ToQmGMcu73TmEy_bz5OW2Z3r79pRCnGzkZUdyc9h8oeAGBM3A_1LToPm9sO17Rp7kbGmSNrUCw55iihQtMpTbcuVc-6tSMHDBx5fXOqD9iHtn4880EnRYZMcCiuOCwIXbVZ7SvzgNOktdDwQ1vqGK-aCHdOby-rZ4uOvZZY2Di281ZjG9oEHYTs1N2HpgNavMi8Y0zwTBFfz4wcKy1d844sw", "domain": ".reddit.com", "path": "/"},
    {"name": "csrf_token", "value": "d83ef64ac116fbccb3282f74243ab73d", "domain": ".reddit.com", "path": "/"},
]

# Article -> search queries (post titles containing these terms)
ARTICLE_QUERIES = {
    "01": ["Swapzone review", "StealthEX review", "SimpleSwap review", "SwapSpace exchange"],
    "02": ["crypto exchange aggregator", "crypto swap aggregator compare"],
    "03": ["instant crypto swap no KYC", "StealthEX no registration", "SimpleSwap no KYC"],
    "04": ["fixed rate crypto swap", "floating rate crypto swap"],
    "05": ["BTC XMR exchange Monero", "Monero no KYC exchange", "Godex XMR"],
    "06": ["USDT BTC exchange rate", "USDT to Bitcoin swap"],
    "07": ["BTC ETH swap best rate", "swap Bitcoin Ethereum"],
    "08": ["ETH BTC exchange", "swap Ethereum Bitcoin"],
    "09": ["BTC TRX exchange Tron", "Tron crypto swap"],
    "10": ["TON exchange Toncoin", "buy Toncoin exchange"],
    "11": ["ChangeNOW review", "ChangeNOW exchange experience"],
    "12": ["SwapSpace review", "SwapSpace exchange rate"],
    "13": ["ChangeNOW alternatives", "best no KYC swap exchange"],
    "14": ["no KYC exchange anonymous", "crypto swap no verification"],
    "15": ["EUR BTC exchange SEPA", "buy bitcoin europe bank"],
    "16": ["buy Monero XMR euro", "EUR XMR exchange"],
    "17": ["DEX vs CEX comparison", "decentralized vs centralized exchange"],
    "18": ["Lido staking ETH review", "Rocket Pool staking", "liquid staking"],
    "19": ["YouHodler review", "Nexo crypto loan", "crypto loan platform"],
    "20": ["CoinSpot review AUD", "Swyftx AUD exchange", "Australia crypto exchange"],
}

def is_good_comment(body, author, score=0):
    if not body or not author:
        return False
    if author.lower() in ('[deleted]', '[removed]', 'automoderator', 'deleted'):
        return False
    body = body.strip()
    if len(body) < 60 or len(body) > 600:
        return False
    bad = ['referral', 'ref link', 'my ref', 'use my code', 'http://bit.ly', 'promo code']
    return not any(b in body.lower() for b in bad)

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

async def get_comments_for_article(page, article_id, queries):
    all_comments = []
    seen_authors = set()
    
    for query in queries:
        if len(all_comments) >= 6:
            break
        
        # Search for posts
        encoded = urllib.parse.quote(query)
        search_url = f"https://www.reddit.com/search.json?q={encoded}&sort=top&t=all&limit=5"
        data = await fetch_api(page, search_url)
        
        if 'error' in data:
            print(f"  [{article_id}] search error: {data['error']}")
            continue
        
        posts = data.get('data', {}).get('children', [])
        print(f"  [{article_id}] query='{query[:40]}' posts={len(posts)}")
        
        for post in posts[:4]:
            if len(all_comments) >= 6:
                break
            
            pd = post.get('data', {})
            post_id = pd.get('id')
            subreddit = pd.get('subreddit', '')
            num_comments = pd.get('num_comments', 0)
            
            if not post_id or num_comments < 2:
                continue
            
            # Fetch comments for this post
            comments_url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}.json?limit=15&sort=top"
            cr = await fetch_api(page, comments_url)
            
            if isinstance(cr, list) and len(cr) > 1:
                comments = cr[1].get('data', {}).get('children', [])
                for c in comments:
                    if c.get('kind') != 't1':
                        continue
                    cd = c.get('data', {})
                    author = cd.get('author', '')
                    body = cd.get('body', '')
                    score = cd.get('score', 0)
                    permalink = 'https://reddit.com' + cd.get('permalink', '')
                    
                    if author in seen_authors:
                        continue
                    if is_good_comment(body, author, score):
                        seen_authors.add(author)
                        all_comments.append({
                            'text': body[:500].strip(),
                            'author': author,
                            'permalink': permalink,
                            'score': score,
                            'subreddit': subreddit,
                            'post_title': pd.get('title', '')[:80],
                            'query': query
                        })
                        if len(all_comments) >= 6:
                            break
            
            await asyncio.sleep(0.5)
    
    return all_comments

async def main():
    print("Launching CloakBrowser...")
    ctx = await cloakbrowser.launch_context_async(headless=True, viewport={"width": 1440, "height": 900})
    await ctx.add_cookies(REDDIT_COOKIES)
    
    page = await ctx.new_page()
    # Warm up session on reddit.com
    await page.goto("https://www.reddit.com/", timeout=15000)
    await asyncio.sleep(3)
    
    all_results = {}
    
    for article_id, queries in ARTICLE_QUERIES.items():
        print(f"\nArticle {article_id}:")
        comments = await get_comments_for_article(page, article_id, queries)
        all_results[article_id] = comments
        print(f"  Total good comments: {len(comments)}")
        for c in comments[:2]:
            print(f"    u/{c['author']} (score={c['score']}): {c['text'][:100]}...")
        await asyncio.sleep(1)
    
    await page.close()
    await ctx.close()
    
    out = r"C:\Users\admin\Authority-Building\swapzone_reddit_results.json"
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"\nSaved to {out}")
    total = sum(len(v) for v in all_results.values())
    print(f"Total comments: {total}")
    for k, v in all_results.items():
        print(f"  Article {k}: {len(v)} comments")

asyncio.run(main())
