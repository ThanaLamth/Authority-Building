import asyncio
import json
import re
import cloakbrowser

PLATFORMS = {
    "changenow": "https://www.trustpilot.com/review/changenow.io",
    "stealthex": "https://www.trustpilot.com/review/stealthex.io",
    "simpleswap": "https://www.trustpilot.com/review/simpleswap.io",
    "swapspace": "https://www.trustpilot.com/review/swapspace.co",
    "exolix": "https://www.trustpilot.com/review/exolix.com",
    "fixedfloat": "https://www.trustpilot.com/review/fixedfloat.com",
    "godex": "https://www.trustpilot.com/review/godex.io",
    "letsexchange": "https://www.trustpilot.com/review/letsexchange.io",
    "coinspot": "https://www.trustpilot.com/review/coinspot.com.au",
    "swyftx": "https://www.trustpilot.com/review/swyftx.com",
    "nexo": "https://www.trustpilot.com/review/nexo.io",
    "youhodler": "https://www.trustpilot.com/review/youhodler.com",
    "rocketpool": "https://www.trustpilot.com/review/rocketpool.net",
    "kraken": "https://www.trustpilot.com/review/kraken.com",
}

def clean(t):
    t = t.strip()
    return re.sub(r'\s+', ' ', t)

def is_good(text, reviewer):
    if not text or not reviewer:
        return False
    t = clean(text)
    if len(t) < 80 or len(t) > 600:
        return False
    bad = ['referral', 'promo', 'use my code', 'ref link']
    return not any(b in t.lower() for b in bad)

async def scrape_tp(page, name, url):
    reviews = []
    try:
        await page.goto(url, timeout=30000)
        await asyncio.sleep(7)
        
        data = await page.evaluate("""
        () => {
            const results = [];
            
            // Method 1: __NEXT_DATA__
            const nextData = document.querySelector('#__NEXT_DATA__');
            if (nextData) {
                try {
                    const d = JSON.parse(nextData.textContent);
                    const reviews = d?.props?.pageProps?.reviews || [];
                    for (const r of reviews) {
                        const text = r?.text || r?.title || '';
                        const reviewer = r?.consumer?.displayName || '';
                        const rating = r?.rating || 0;
                        const date = r?.dates?.publishedDate || r?.createdAt || '';
                        const id = r?.id || '';
                        results.push({
                            text, reviewer, rating, date: date.substring(0, 7),
                            permalink: id ? 'https://www.trustpilot.com/reviews/' + id : ''
                        });
                    }
                } catch(e) {}
            }
            
            if (results.length > 0) return {source: 'next_data', results};
            
            // Method 2: DOM with actual classes
            const cards = document.querySelectorAll('article[class*="paper"]');
            for (const card of cards) {
                const textEl = card.querySelector('p[class*="reviewText"], p[class*="reviewContent"], [class*="reviewBody"]');
                const authorEl = card.querySelector('span[class*="consumerName"], [class*="displayName"]');
                const ratingEl = card.querySelector('[class*="starRating"] img');
                const dateEl = card.querySelector('time');
                const linkEl = card.querySelector('a[href*="/reviews/"]');
                
                if (textEl) {
                    results.push({
                        text: textEl.textContent.trim(),
                        reviewer: authorEl ? authorEl.textContent.trim() : 'Anonymous',
                        rating: ratingEl ? parseInt(ratingEl.alt || '0') : 0,
                        date: dateEl ? (dateEl.getAttribute('datetime') || '').substring(0, 7) : '',
                        permalink: linkEl ? linkEl.href : ''
                    });
                }
            }
            return {source: 'dom', results};
        }
        """)
        
        raw = data.get('results', [])
        print(f"  {name}: source={data.get('source')}, raw={len(raw)}")
        
        for r in raw:
            text = clean(r.get('text', ''))
            reviewer = r.get('reviewer', '').strip()
            rating = r.get('rating', 0)
            if is_good(text, reviewer):
                reviews.append({
                    'text': text[:400],
                    'reviewer': reviewer,
                    'rating': int(rating) if rating else 0,
                    'date': r.get('date', ''),
                    'permalink': r.get('permalink', ''),
                    'platform': name,
                })
        
        print(f"  {name}: good reviews = {len(reviews)}")
        for rv in reviews[:2]:
            print(f"    [{rv['rating']}*] {rv['reviewer']}: {rv['text'][:80]}...")
        
    except Exception as e:
        print(f"  Error {name}: {e}")
    
    return reviews

async def main():
    ctx = await cloakbrowser.launch_context_async(headless=True, viewport={"width": 1440, "height": 900})
    page = await ctx.new_page()
    
    all_reviews = {}
    
    for name, url in PLATFORMS.items():
        print(f"\n{name}:")
        reviews = await scrape_tp(page, name, url)
        all_reviews[name] = reviews
        await asyncio.sleep(4)
    
    await page.close()
    await ctx.close()
    
    out = r"C:\Users\admin\Authority-Building\trustpilot_platform_reviews.json"
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(all_reviews, f, ensure_ascii=False, indent=2)
    
    print(f"\nSaved: {out}")
    total = sum(len(v) for v in all_reviews.values())
    print(f"Total good reviews: {total}")

asyncio.run(main())
