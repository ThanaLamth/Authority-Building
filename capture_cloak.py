import os, time, sys
sys.stdout.reconfigure(encoding="utf-8")
from cloakbrowser import launch

PROXY = "http://b06x:b06x@103.82.22.77:18504"
OUT   = r"C:\Users\admin\Authority-Building\images"

def capture(url, outfile, use_proxy=True, wait=7):
    proxy = PROXY if use_proxy else None
    browser = launch(
        proxy=proxy,
        headless=True,
        humanize=True,
    )
    try:
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 900})
        page.set_extra_http_headers({"Accept-Language": "en-US,en;q=0.9"})
        print(f"  -> goto {url}")
        page.goto(url, timeout=40000, wait_until="domcontentloaded")
        page.wait_for_timeout(wait * 1000)
        path = os.path.join(OUT, outfile)
        page.screenshot(path=path, full_page=False)
        size = os.path.getsize(path)
        print(f"  OK {outfile}  {size//1024}KB")
        return size
    except Exception as e:
        print(f"  FAIL {outfile}: {str(e)[:120]}")
        return 0
    finally:
        browser.close()

# Rollbit — Cloudflare, must use proxy
print("=== Rollbit ===")
capture("https://rollbit.com", "rollbit-halloween-promo.png", use_proxy=True, wait=8)

# Gamdom promotions — maintenance or geo, try proxy
print("=== Gamdom promotions ===")
capture("https://gamdom.com/promotions", "gamdom-halloween-promo.png", use_proxy=True, wait=8)
