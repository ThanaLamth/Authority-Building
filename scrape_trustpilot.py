import asyncio
import json
import re
import cloakbrowser

PLATFORMS = {
    "swapzone": "https://www.trustpilot.com/review/swapzone.io",
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
    "lido": "https://www.trustpilot.com/review/lido.fi",
    "kraken": "https://www.trustpilot.com/review/kraken.com",
}

def clean_text(t):
    t = t.strip()
    t = re.sub(r'\s+', ' ', t)
    return t

def is_good_review(text, reviewer):
    if not text or not reviewer:
        return False
    text = clean_text(text)
    if len(text) < 80 or len(text) > 600:
        return False
    bad = ['referral', 'promo code', 'ref link', 'use my code']
    return not any(b in text.lower() for b in bad)

async def scrape_platform(page, name, url):
    reviews = []
    try:
        await page.goto(url, timeout=30000)
        await asyncio.sleep(6)
        
        # Extract reviews via JS
        data = await page.evaluate("""
        () => {
            const reviews = [];
            
            // Try structured data
            const scripts = document.querySelectorAll('script[type="application/ld+json"]');
            for (const s of scripts) {
                try {
                    const d = JSON.parse(s.textContent);
                    if (d['@type'] === 'LocalBusiness' && d.review) {
                        for (const r of d.review) {
                            const body = r.reviewBody || r.description || '';
                            const author = r.author && r.author.name ? r.author.name : '';
                            const rating = r.reviewRating && r.reviewRating.ratingValue ? r.reviewRating.ratingValue : 0;
                            const date = r.datePublished || '';
                            if (body && author) {
                                reviews.push({text: body, reviewer: author, rating: rating, date: date, permalink: ''});
                            }
                        }
                    } else if (Array.isArray(d)) {
                        for (const item of d) {
                            if (item['@type'] === 'Review') {
                                const body = item.reviewBody || '';
                                const author = item.author && item.author.name ? item.author.name : '';
                                const rating = item.reviewRating && item.reviewRating.ratingValue ? item.reviewRating.ratingValue : 0;
                                const date = item.datePublished || '';
                                if (body) reviews.push({text: body, reviewer: author, rating: rating, date: date, permalink: ''});
                            }
                        }
                    }
                } catch(e) {}
            }
            
            if (reviews.length > 0) return {source: 'ld+json', reviews};
            
            // Try DOM elements
            const cards = document.querySelectorAll('[data-service-review-card-paper], .styles_reviewCardInner__EwDq2, article[class*="paper_paper"]');
            for (const card of cards) {
                const bodyEl = card.querySelector('p[data-service-review-text-typography-wrapper], .styles_reviewContent__0Q2Tg p, [class*="reviewBody"]');
                const authorEl = card.querySelector('[class*="consumerName"], [class*="authorName"], span[class*="typography"]');
                const ratingEl = card.querySelector('[class*="star-rating_starRating"] img, [class*="starRating"] img');
                const dateEl = card.querySelector('time');
                
                if (bodyEl) {
                    const text = bodyEl.textContent.trim();
                    const reviewer = authorEl ? authorEl.textContent.trim() : 'Anonymous';
                    const rating = ratingEl ? parseInt(ratingEl.alt || '0') : 0;
                    const date = dateEl ? dateEl.getAttribute('datetime') || '' : '';
                    reviews.push({text, reviewer, rating, date, permalink: ''});
                }
            }
            
            return {source: 'dom', reviews: reviews.slice(0, 20)};
        }
        """)
        
        raw = data.get('reviews', [])
        print(f"  {name}: source={data.get('source')}, raw={len(raw)}")
        
        for r in raw:
            text = clean_text(r.get('text', ''))
            reviewer = r.get('reviewer', '').strip()
            rating = r.get('rating', 0)
            date = r.get('date', '')[:7]  # YYYY-MM
            
            if is_good_review(text, reviewer):
                reviews.append({
                    'text': text[:400],
                    'reviewer': reviewer,
                    'rating': int(rating) if rating else 0,
                    'date': date,
                    'permalink': '',
                    'platform': name,
                })
        
        # Also try to get specific review permalinks
        if reviews:
            links = await page.evaluate("""
            () => {
                const links = [];
                document.querySelectorAll('a[href*="/reviews/"]').forEach(a => {
                    if (a.href && a.href.includes('/reviews/') && !a.href.includes('/review/')) {
                        links.push(a.href);
                    }
                });
                return links.slice(0, 20);
            }
            """)
            # Match links to reviews by position
            for i, link in enumerate(links[:len(reviews)]):
                if i < len(reviews):
                    reviews[i]['permalink'] = link
        
    except Exception as e:
        print(f"  Error {name}: {e}")
    
    return reviews

async def main():
    ctx = await cloakbrowser.launch_context_async(headless=True, viewport={"width": 1440, "height": 900})
    
    all_reviews = {}
    page = await ctx.new_page()
    
    for name, url in PLATFORMS.items():
        print(f"\nScraping {name}: {url}")
        reviews = await scrape_platform(page, name, url)
        all_reviews[name] = reviews
        print(f"  Good reviews: {len(reviews)}")
        for r in reviews[:2]:
            print(f"    [{r['rating']}*] {r['reviewer']}: {r['text'][:80]}...")
        await asyncio.sleep(3)
    
    await page.close()
    await ctx.close()
    
    out = r"C:\Users\admin\Authority-Building\trustpilot_platform_reviews.json"
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(all_reviews, f, ensure_ascii=False, indent=2)
    
    print(f"\nSaved: {out}")
    total = sum(len(v) for v in all_reviews.values())
    print(f"Total reviews: {total}")

asyncio.run(main())
