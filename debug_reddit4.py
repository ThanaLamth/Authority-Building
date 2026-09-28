import asyncio
import json
import cloakbrowser

REDDIT_COOKIES = [
    {"name": "reddit_session", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpsVFdYNlFVUEloWktaRG1rR0pVd1gvdWNFK01BSjBYRE12RU1kNzVxTXQ4IiwidHlwIjoiSldUIn0.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDE0ODgyMDguODM4NTAxLCJpYXQiOjE3ODU4NDk4MDguODM4NTAxLCJqdGkiOiJBa2NNMUpEWldYMEtiUzl5UnZzcTh4T3FpemVad1EiLCJhdCI6MSwiY2lkIjoiY29va2llIiwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnlLamdVRUFBRF9fd0VWQUxrIiwiZmxvIjozLCJhbXIiOlsic3NvIl19.RUuKGpf1m2T68RE9HorT_x5TXd_GWm7sKmFmoFqqZbjvj75O_vlh3H1fyHloOuC6K2hLdj7xdPUUF5ySXikXe69tkexQ-Ldnxv2t3Df2oLJ3YkLGCed_Nk44fifN4hf77wM18tVfwDViN34gGYW5JEiuAaLXDoYHIFW_YkOpchjVDVlrkHB9cYnxjKbvk0t1zOUNpEPfgsHQ_JFonLN_kfEoEI7pEQuA5AmGuIUgpO8i-HxKzivgbNGHuYvCCp20kJ97DuUvJvF1eFZkgPB_ad-FlAzvMzkQZVAfx4bbAbZBfUfWdtNpAr_Wgz4CT1FCxnghoA30DA4TxdrvjrzXbw", "domain": ".reddit.com", "path": "/"},
    {"name": "token_v2", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzg2NTIyODAzLjc5MTc1MSwiaWF0IjoxNzg2NDM2NDAzLjc5MTc1MSwianRpIjoiM0ZGcUhlMmpCTU0xcG5pa2RrVkRPb0V1UDNtSU9RIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhdCI6MSwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5feldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJyY2lkIjoiOXlUdUVWc2lieDZ0LWJpbFZlQVNDUFNZQlJtTVZXUmVSR1JncldjdHQzcyIsImZsbyI6Mn0.L-islac7kDH7l6F2UKhnGBJujKecYwSFkFQygRwjXGyKESTqXmGfWB_MAS6v2kyspgZMC57GMSvBBYVpvKeyM1IRnLd1p5xrUtsl0hESZ7L2MCADkDU3CH3qTG43D6ToQmGMcu73TmEy_bz5OW2Z3r79pRCnGzkZUdyc9h8oeAGBM3A_1LToPm9sO17Rp7kbGmSNrUCw55iihQtMpTbcuVc-6tSMHDBx5fXOqD9iHtn4880EnRYZMcCiuOCwIXbVZ7SvzgNOktdDwQ1vqGK-aCHdOby-rZ4uOvZZY2Di281ZjG9oEHYTs1N2HpgNavMi8Y0zwTBFfz4wcKy1d844sw", "domain": ".reddit.com", "path": "/"},
    {"name": "csrf_token", "value": "d83ef64ac116fbccb3282f74243ab73d", "domain": ".reddit.com", "path": "/"},
]

async def main():
    ctx = await cloakbrowser.launch_context_async(headless=True, viewport={"width": 1440, "height": 900})
    await ctx.add_cookies(REDDIT_COOKIES)
    
    page = await ctx.new_page()
    await page.goto("https://www.reddit.com/", timeout=15000)
    await asyncio.sleep(2)
    
    # Strategy: search for posts, get top post, fetch its comments
    # 1. Search posts about Swapzone
    search_url = "https://www.reddit.com/search.json?q=Swapzone+exchange&sort=top&t=all&limit=5"
    result = await page.evaluate(f"""
    async () => {{
        const r = await fetch('{search_url}', {{credentials: 'include', headers: {{'Accept': 'application/json'}}}});
        return await r.json();
    }}
    """)
    
    posts = result.get('data', {}).get('children', [])
    print(f"Found {len(posts)} posts")
    
    for post in posts[:3]:
        d = post['data']
        print(f"Post: r/{d.get('subreddit')} | {d.get('title','')[:60]} | score={d.get('score')} | comments={d.get('num_comments')}")
        post_id = d.get('id')
        subreddit = d.get('subreddit')
        if post_id and d.get('num_comments', 0) > 0:
            comments_url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}.json?limit=10&sort=top"
            cr = await page.evaluate(f"""
            async () => {{
                const r = await fetch('{comments_url}', {{credentials: 'include', headers: {{'Accept': 'application/json'}}}});
                return await r.json();
            }}
            """)
            if isinstance(cr, list) and len(cr) > 1:
                comments = cr[1].get('data', {}).get('children', [])
                print(f"  Got {len(comments)} top comments")
                for c in comments[:3]:
                    if c.get('kind') == 't1':
                        cd = c['data']
                        author = cd.get('author', '')
                        body = cd.get('body', '')
                        score = cd.get('score', 0)
                        permalink = "https://reddit.com" + cd.get('permalink', '')
                        if len(body) > 60 and author not in ('[deleted]', 'AutoModerator'):
                            print(f"  Comment by u/{author} (score={score}): {body[:200]}")
                            print(f"  Link: {permalink}")
    
    await page.close()
    await ctx.close()

asyncio.run(main())
