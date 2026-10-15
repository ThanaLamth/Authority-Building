import os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
from cloakbrowser import launch

PROXY = "http://b06x:b06x@103.82.22.77:18504"
OUT   = r"C:\Users\admin\Authority-Building\images"

print("Launching CloakBrowser headed for Rollbit...")
browser = launch(
    proxy=PROXY,
    headless=False,
    humanize=True,
    geoip=True,
)
page = browser.new_page()
page.set_viewport_size({"width": 1280, "height": 900})
page.set_extra_http_headers({"Accept-Language": "en-US,en;q=0.9"})

print("  -> goto https://rollbit.com")
page.goto("https://rollbit.com", timeout=40000, wait_until="domcontentloaded")
print("  -> waiting 10s for Cloudflare challenge...")
page.wait_for_timeout(10000)

title = page.title()
url = page.url
print(f"  title: {title}")
print(f"  url:   {url}")

path = os.path.join(OUT, "rollbit-halloween-promo.png")
page.screenshot(path=path, full_page=False)
size = os.path.getsize(path)
print(f"  saved: {path} ({size//1024}KB)")

browser.close()
