import asyncio
import cloakbrowser

async def main():
    ctx = await cloakbrowser.launch_context_async(headless=True, viewport={"width": 1440, "height": 900})
    page = await ctx.new_page()
    
    await page.goto("https://www.trustpilot.com/review/changenow.io", timeout=30000)
    await asyncio.sleep(8)
    
    # Save HTML
    html = await page.content()
    with open(r"C:\Users\admin\Authority-Building\tp_debug.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    # Check what elements exist
    data = await page.evaluate("""
    () => {
        const result = {};
        
        // Check LD+JSON scripts
        const scripts = Array.from(document.querySelectorAll('script[type="application/ld+json"]'));
        result.ld_json_count = scripts.length;
        result.ld_json_types = scripts.map(s => {
            try { return JSON.parse(s.textContent)['@type'] || 'unknown'; } catch(e) { return 'parse_error'; }
        });
        
        // Check for review-related elements
        const reviewEls = document.querySelectorAll('[data-service-review-card-paper]');
        result.review_cards = reviewEls.length;
        
        const articles = document.querySelectorAll('article');
        result.articles = articles.length;
        
        // Check all classes containing 'review'
        const allEls = Array.from(document.querySelectorAll('*'));
        const reviewClasses = new Set();
        allEls.forEach(el => {
            if (el.className && typeof el.className === 'string') {
                el.className.split(' ').forEach(c => {
                    if (c.toLowerCase().includes('review')) reviewClasses.add(c);
                });
            }
        });
        result.review_classes = Array.from(reviewClasses).slice(0, 20);
        
        // Check page title
        result.title = document.title;
        result.url = window.location.href;
        
        // Check for next-data script
        const nextData = document.querySelector('#__NEXT_DATA__');
        if (nextData) {
            try {
                const d = JSON.parse(nextData.textContent);
                result.has_next_data = true;
                const str = JSON.stringify(d);
                result.next_data_sample = str.substring(0, 1000);
            } catch(e) { result.has_next_data = false; }
        } else {
            result.has_next_data = false;
        }
        
        return result;
    }
    """)
    
    print(f"Title: {data.get('title')}")
    print(f"URL: {data.get('url')}")
    print(f"LD+JSON count: {data.get('ld_json_count')}")
    print(f"LD+JSON types: {data.get('ld_json_types')}")
    print(f"Review cards: {data.get('review_cards')}")
    print(f"Articles: {data.get('articles')}")
    print(f"Has __NEXT_DATA__: {data.get('has_next_data')}")
    if data.get('review_classes'):
        print(f"Review classes: {data.get('review_classes')[:10]}")
    if data.get('next_data_sample'):
        print(f"NEXT_DATA sample: {data.get('next_data_sample')[:500]}")
    print(f"HTML size: {len(html)}")
    
    await ctx.close()

asyncio.run(main())
