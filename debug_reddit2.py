import asyncio
import json
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
    
    # Try JSON API
    url = "https://www.reddit.com/search.json?q=Swapzone+review&type=comment&sort=top&t=all&limit=10"
    await page.goto(url, timeout=30000)
    await asyncio.sleep(3)
    
    content = await page.content()
    print("JSON API response length:", len(content))
    print("First 1000 chars:", content[:1000])
    
    # Try to get JSON via fetch
    result = await page.evaluate("""
    async () => {
        try {
            const r = await fetch('https://www.reddit.com/search.json?q=Swapzone+review&type=comment&sort=top&t=all&limit=5', {
                credentials: 'include',
                headers: {'Accept': 'application/json'}
            });
            const text = await r.text();
            return {status: r.status, text: text.substring(0, 2000)};
        } catch(e) {
            return {error: e.toString()};
        }
    }
    """)
    print("Fetch result:", result)
    
    await ctx.close()

asyncio.run(main())
