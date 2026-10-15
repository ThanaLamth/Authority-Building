import os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
from cloakbrowser import launch

PROXY = "http://b06x:b06x@103.82.22.77:18504"
OUT   = r"C:\Users\admin\Authority-Building\images"

print("Launching CloakBrowser headed + humanize for Rollbit...")
browser = launch(proxy=PROXY, headless=False, humanize=True, geoip=True)
page = browser.new_page()
page.set_viewport_size({"width": 1280, "height": 900})
page.set_extra_http_headers({"Accept-Language": "en-US,en;q=0.9"})
print("  -> goto https://rollbit.com")
page.goto("https://rollbit.com", timeout=45000, wait_until="domcontentloaded")
for i in range(15):
    time.sleep(2)
    title = page.title()
    print(f"  [{i*2}s] title={title!r}")
    if "just a moment" not in title.lower() and "performing" not in title.lower():
        print("  Cloudflare cleared!")
        break
time.sleep(3)
path = os.path.join(OUT, "rollbit-halloween-promo.png")
page.screenshot(path=path, full_page=False)
print(f"  saved {os.path.getsize(path)//1024}KB")
browser.close()
