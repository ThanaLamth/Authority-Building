import asyncio
import cloakbrowser

REDDIT_COOKIES = [
    {"name": "reddit_session", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpsVFdYNlFVUEloWktaRG1rR0pVd1gvdWNFK01BSjBYRE12RU1kNzVxTXQ4IiwidHlwIjoiSldUIn0.eyJzdWIiOiJ0Ml9pajJ2ZW1pYjAiLCJleHAiOjE4MDE0ODgyMDguODM4NTAxLCJpYXQiOjE3ODU4NDk4MDguODM4NTAxLCJqdGkiOiJBa2NNMUpEWldYMEtiUzl5UnZzcTh4T3FpemVad1EiLCJhdCI6MSwiY2lkIjoiY29va2llIiwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnlLamdVRUFBRF9fd0VWQUxrIiwiZmxvIjozLCJhbXIiOlsic3NvIl19.RUuKGpf1m2T68RE9HorT_x5TXd_GWm7sKmFmoFqqZbjvj75O_vlh3H1fyHloOuC6K2hLdj7xdPUUF5ySXikXe69tkexQ-Ldnxv2t3Df2oLJ3YkLGCed_Nk44fifN4hf77wM18tVfwDViN34gGYW5JEiuAaLXDoYHIFW_YkOpchjVDVlrkHB9cYnxjKbvk0t1zOUNpEPfgsHQ_JFonLN_kfEoEI7pEQuA5AmGuIUgpO8i-HxKzivgbNGHuYvCCp20kJ97DuUvJvF1eFZkgPB_ad-FlAzvMzkQZVAfx4bbAbZBfUfWdtNpAr_Wgz4CT1FCxnghoA30DA4TxdrvjrzXbw", "domain": ".reddit.com", "path": "/"},
    {"name": "token_v2", "value": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzg2NTIyODAzLjc5MTc1MSwiaWF0IjoxNzg2NDM2NDAzLjc5MTc1MSwianRpIjoiM0ZGcUhlMmpCTU0xcG5pa2RrVkRPb0V1UDNtSU9RIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhaWQiOiJ0Ml9pajJ2ZW1pYjAiLCJhdCI6MSwibGNhIjoxNjkzMjIxNjI0NjEzLCJzY3AiOiJlSnhra2RHT3REQUloZC1GYTVfZ2Y1VV9tMDF0Y1lhc0xRYW9rM243RFZvY2s3MDdjRDRwSFA5REtvcUZEQ1pYZ3FuQUJGZ1RyVERCUnVUOW5MbTNnMmlOZTh0WXNabkNCRm13RkRya21MR3NpUVFtZUpJYXl4c21vSUxOeUZ5dXRHTk5MVDBRSnFoY01yZUZIcGMyb2JrYmk1NmRHRlc1ckR5b3NWZmwwdGpHRkxZbnhqY2JxdzJwdUM2bk1rbkxRdmtzWHZUak45VzM5dm16X1NhMEo4T0txdW1CM2hsSkNHNHNmcGltM2Q5VGs1NnRDeGExOTNxUTJ1ZDYzSzU5MWl3ME83ZWY2X2xySXhtWFkyaC1KdnQzMXktaEE0ODhMelBxQUVhczRVY1pkbVFkX2xVSFVMbWdKR01KNHRNSTVNcmwyMzhKdG12VHY4YnRFejk4TS1LbU5feldETlJ6Q2VMUXBfSDFHd0FBX184UTFlVFIiLCJyY2lkIjoiOXlUdUVWc2lieDZ0LWJpbFZlQVNDUFNZQlJtTVZXUmVSR1JncldjdHQzcyIsImZsbyI6Mn0.L-islac7kDH7l6F2UKhnGBJujKecYwSFkFQygRwjXGyKESTqXmGfWB_MAS6v2kyspgZMC57GMSvBBYVpvKeyM1IRnLd1p5xrUtsl0hESZ7L2MCADkDU3CH3qTG43D6ToQmGMcu73TmEy_bz5OW2Z3r79pRCnGzkZUdyc9h8oeAGBM3A_1LToPm9sO17Rp7kbGmSNrUCw55iihQtMpTbcuVc-6tSMHDBx5fXOqD9iHtn4880EnRYZMcCiuOCwIXbVZ7SvzgNOktdDwQ1vqGK-aCHdOby-rZ4uOvZZY2Di281ZjG9oEHYTs1N2HpgNavMi8Y0zwTBFfz4wcKy1d844sw", "domain": ".reddit.com", "path": "/"},
    {"name": "csrf_token", "value": "d83ef64ac116fbccb3282f74243ab73d", "domain": ".reddit.com", "path": "/"},
    {"name": "loid", "value": "000000000ij2vemib0.2.1693221624613.Z0FBQUFBQnFjZWZSODFCNWhuZmRWY1plV3hhZ0Nzdm0xNHh3eEZ4QzZROXZ1eHdVXzFfYjRxdjMtZFBqM0QwMU1tWUxiWEhXTUF1R0dzdm1QMlpmVk5Tdy1UVjdEaVh5Vmw5ZlJsQXRJREYwRzFGZEp4WGVMbk95aDd1V0FSU05tTDNLb21aSXIyWDc", "domain": ".reddit.com", "path": "/"},
    {"name": "edgebucket", "value": "Mf4rxScXl9I4eGp6HH", "domain": ".reddit.com", "path": "/"},
]

async def main():
    ctx = await cloakbrowser.launch_context_async(headless=True, viewport={"width": 1440, "height": 900})
    await ctx.add_cookies(REDDIT_COOKIES)
    
    page = await ctx.new_page()
    url = "https://www.reddit.com/search/?q=Swapzone+review&type=comment&sort=top&t=all"
    await page.goto(url, timeout=30000)
    await asyncio.sleep(8)
    
    html = await page.content()
    # Save HTML for inspection
    with open(r"C:\Users\admin\Authority-Building\reddit_debug.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    # Also try JS extraction
    data = await page.evaluate("""
    () => {
        // Get all shreddit-comment elements
        const comments = Array.from(document.querySelectorAll('shreddit-comment'));
        const results = comments.slice(0, 5).map(c => {
            return {
                outerHTML: c.outerHTML.substring(0, 500),
                textContent: c.textContent.substring(0, 300),
                attrs: Array.from(c.attributes).map(a => a.name + '=' + a.value.substring(0, 100))
            };
        });
        
        // Also check for comment-body
        const bodies = Array.from(document.querySelectorAll('[slot="comment"],.Comment,.comment-body'));
        const bodyTexts = bodies.slice(0, 5).map(b => b.textContent.substring(0, 200));
        
        // What elements are on page
        const tags = new Set();
        document.querySelectorAll('*').forEach(el => {
            if (el.tagName.startsWith('SHREDDIT') || el.tagName.startsWith('REDDIT') || el.tagName.startsWith('FACEPLATE')) {
                tags.add(el.tagName);
            }
        });
        
        return {
            comments: results,
            bodies: bodyTexts,
            tags: Array.from(tags),
            url: window.location.href,
            title: document.title
        };
    }
    """)
    
    print("URL:", data.get("url"))
    print("Title:", data.get("title"))
    print("Shreddit tags:", data.get("tags"))
    print("Comment count:", len(data.get("comments", [])))
    if data.get("comments"):
        c = data["comments"][0]
        print("First comment attrs:", c.get("attrs"))
        print("First comment text:", c.get("textContent", "")[:200])
    print("Body texts:", data.get("bodies", [])[:2])
    
    # Check HTML size
    print(f"HTML size: {len(html)} chars")
    # Show snippet around 'body' keyword
    idx = html.lower().find('"body"')
    if idx >= 0:
        print("Found 'body' in JSON at:", html[idx:idx+200])
    else:
        idx2 = html.lower().find('swapzone')
        if idx2 >= 0:
            print("Found 'swapzone' at:", html[idx2:idx2+300])
    
    await ctx.close()

asyncio.run(main())
