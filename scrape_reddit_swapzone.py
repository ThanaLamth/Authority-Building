import asyncio
import json
import re
import urllib.parse
import cloakbrowser

REDDIT_COOKIES = [
    {"name": "reddit_session", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpsVFdYNlFVUEloWktaRG1rR0pVd1gvdWNFK01BSjBYRE12RU1kNzVxTXQ4IiwidHlwIjoiSldUIn0.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDE0ODgyMDguODM4NTAxLCJpYXQiOjE3ODU4NDk4MDguODM4NTAxLCJqdGkiOiJBa2NNMUpEWldYMEtiUzl5UnZzcTh4T3FpemVad1EiLCJhdCI6MSwiY2lkIjoiY29va2llIiwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnlLamdVRUFBRF9fd0VWQUxrIiwiZmxvIjozLCJhbXIiOlsic3NvIl19.RUuKGpf1m2T68RE9HorT_x5TXd_GWm7sKmFmoFqqZbjvj75O_vlh3H1fyHloOuC6K2hLdj7xdPUUF5ySXikXe69tkexQ-Ldnxv2t3Df2oLJ3YkLGCed_Nk44fifN4hf77wM18tVfwDViN34gGYW5JEiuAaLXDoYHIFW_YkOpchjVDVlrkHB9cYnxjKbvk0t1zOUNpEPfgsHQ_JFonLN_kfEoEI7pEQuA5AmGuIUgpO8i-HxKzivgbNGHuYvCCp20kJ97DuUvJvF1eFZkgPB_ad-FlAzvMzkQZVAfx4bbAbZBfUfWdtNpAr_Wgz4CT1FCxnghoA30DA4TxdrvjrzXbw", "domain": ".reddit.com", "path": "/"},
    {"name": "token_v2", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzg2NTIyODAzLjc5MTc1MSwiaWF0IjoxNzg2NDM2NDAzLjc5MTc1MSwianRpIjoiM0ZGcUhlMmpCTU0xcG5pa2RrVkRPb0V1UDNtSU9RIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhdCI6MSwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5feldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJyY2lkIjoiOXlUdUVWc2lieDZ0LWJpbFZlQVNDUFNZQlJtTVZXUmVSR1JncldjdHQzcyIsImZsbyI6Mn0.L-islac7kDH7l6F2UKhnGBJujKecYwSFkFQygRwjXGyKESTqXmGfWB_MAS6v2kyspgZMC57GMSvBBYVpvKeyM1IRnLd1p5xrUtsl0hESZ7L2MCADkDU3CH3qTG43D6ToQmGMcu73TmEy_bz5OW2Z3r79pRCnGzkZUdyc9h8oeAGBM3A_1LToPm9sO17Rp7kbGmSNrUCw55iihQtMpTbcuVc-6tSMHDBx5fXOqD9iHtn4880EnRYZMcCiuOCwIXbVZ7SvzgNOktdDwQ1vqGK-aCHdOby-rZ4uOvZZY2Di281ZjG9oEHYTs1N2HpgNavMi8Y0zwTBFfz4wcKy1d844sw", "domain": ".reddit.com", "path": "/"},
    {"name": "csrf_token", "value": "d83ef64ac116fbccb3282f74243ab73d", "domain": ".reddit.com", "path": "/"},
    {"name": "loid", "value": "000000000ij2vemib0.2.1693221624613.Z0FBQUFBQnFjZWZSODFCNWhuZmRWY1plV3hhZ0Nzdm0xNHh3eEZ4QzZROXZ1eHdVXzFfYjRxdjMtZFBqM0QwMU1tWUxiWEhXTUF1R0dzdm1QMlpmVk5Tdy1UVjdEaVh5Vmw5ZlJsQXRJREYwRzFGZEp4WGVMbk95aDd1V0FSU05tTDNLb21aSXIyWDc", "domain": ".reddit.com", "path": "/"},
    {"name": "edgebucket", "value": "Mf4rxScXl9I4eGp6HH", "domain": ".reddit.com", "path": "/"},
]

QUERIES = [
    {"article": "01", "query": "Swapzone exchange aggregator review"},
    {"article": "01b", "query": "StealthEX swap review reddit"},
    {"article": "01c", "query": "SimpleSwap crypto exchange experience"},
    {"article": "02", "query": "crypto exchange aggregator compare rates"},
    {"article": "03", "query": "instant crypto swap no registration no KYC"},
    {"article": "04", "query": "fixed rate vs floating rate crypto swap"},
    {"article": "05", "query": "BTC to XMR swap exchange Monero no KYC"},
    {"article": "06", "query": "USDT to BTC exchange rate conversion"},
    {"article": "07", "query": "swap BTC ETH best rate exchange"},
    {"article": "08", "query": "ETH to BTC swap which exchange"},
    {"article": "09", "query": "BTC TRX exchange Tron USDT"},
    {"article": "10", "query": "TON Toncoin exchange purchase"},
    {"article": "11", "query": "ChangeNOW exchange experience review"},
    {"article": "12", "query": "SwapSpace exchange rate comparison"},
    {"article": "13", "query": "ChangeNOW alternatives best crypto swap"},
    {"article": "14", "query": "no KYC crypto exchange without verification"},
    {"article": "15", "query": "EUR to BTC exchange SEPA bank"},
    {"article": "16", "query": "buy Monero XMR with euros EUR"},
    {"article": "17", "query": "DEX vs CEX crypto trading pros cons"},
    {"article": "18", "query": "Lido staking ETH review Rocket Pool"},
    {"article": "19", "query": "crypto loan platform YouHodler Nexo review"},
    {"article": "20", "query": "CoinSpot AUD crypto exchange Australia review"},
]

def clean_text(t):
    t = t.strip()
    t = re.sub(r"\s+", " ", t)
    return t

def is_good_comment(text, author):
    if not text or not author:
        return False
    if author.lower() in ("automoderator", "[deleted]", "[removed]", "deleted"):
        return False
    text = clean_text(text)
    if len(text) < 60 or len(text) > 600:
        return False
    bad = ["referral", "ref link", "my ref", "sign up with my", "use my code", "http://bit.ly"]
    if any(b in text.lower() for b in bad):
        return False
    return True

async def scrape_query(ctx, query, article_id):
    page = await ctx.new_page()
    results = []
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://www.reddit.com/search/?q={encoded}&type=comment&sort=top&t=all"
        await page.goto(url, timeout=30000)
        await asyncio.sleep(7)
        
        html = await page.content()
        
        # Extract from JSON embedded in page
        found_texts = []
        found_authors = []
        found_permalinks = []
        
        # Look for t1_ comment objects in JSON
        body_matches = re.findall(r'"body"\s*:\s*"((?:[^"\\]|\\.){{60,500}})"', html)
        author_matches = re.findall(r'"author"\s*:\s*"([a-zA-Z0-9_\-]{{2,20}})"', html)
        link_matches = re.findall(r'"permalink"\s*:\s*"(/r/[^"]+/comments/[^"]+?)"', html)
        
        print(f"  [{article_id}] bodies={len(body_matches)} authors={len(author_matches)} links={len(link_matches)}")
        
        for i, body in enumerate(body_matches[:15]):
            text = body.replace("\\n", " ").replace('\\"', '"').replace("\\/", "/").replace("\\u0026", "&")
            text = clean_text(text)
            author = author_matches[i] if i < len(author_matches) else "unknown"
            permalink = "https://reddit.com" + link_matches[i].replace("\\/", "/") if i < len(link_matches) else ""
            if is_good_comment(text, author):
                results.append({
                    "text": text[:500],
                    "author": author,
                    "permalink": permalink,
                    "score": 0,
                    "query": query
                })
        
        print(f"  [{article_id}] good comments: {len(results)}")
        
    except Exception as e:
        print(f"  Error [{article_id}]: {e}")
    finally:
        await page.close()
    return results

async def main():
    print("Launching CloakBrowser...")
    ctx = await cloakbrowser.launch_context_async(
        headless=True,
        viewport={"width": 1440, "height": 900}
    )
    
    await ctx.add_cookies(REDDIT_COOKIES)
    
    # Check login
    page = await ctx.new_page()
    await page.goto("https://www.reddit.com/", timeout=30000)
    await asyncio.sleep(5)
    title = await page.title()
    print(f"Reddit title: {title}")
    await page.close()
    
    all_results = {}
    
    for q in QUERIES:
        article_raw = q["article"]
        article = article_raw.rstrip("bc")
        query = q["query"]
        print(f"\nArticle {article_raw}: {query}")
        results = await scrape_query(ctx, query, article_raw)
        if article not in all_results:
            all_results[article] = []
        all_results[article].extend(results)
        await asyncio.sleep(3)
    
    await ctx.close()
    
    out = r"C:\Users\admin\Authority-Building\swapzone_reddit_results.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"\nSaved: {out}")
    total = 0
    for k, v in all_results.items():
        n = len(v)
        total += n
        if n > 0:
            print(f"  Article {k}: {n} comments -- [{v[0]['text'][:80]}...]")
        else:
            print(f"  Article {k}: 0 comments")
    print(f"Total: {total} comments across {len(all_results)} articles")

asyncio.run(main())
