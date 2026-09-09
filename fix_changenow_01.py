import json, re, os

BASE = r"C:\Users\admin\Authority-Building"
tp_all = json.load(open(os.path.join(BASE, "tp_fresh.json"), encoding="utf-8"))
cn_tp = tp_all.get("changenow.io", [])
reddit_all = json.load(open(os.path.join(BASE, "reddit_fresh.json"), encoding="utf-8"))
cn_reddit = reddit_all.get("changenow swap", [])

def clean(text):
    if not text: return ""
    text = text.replace("\u2019", "'").replace("\u2014", "-").replace("\u2013", "-")
    text = re.sub(r"[^\x00-\x7F\u00C0-\u024F]", "", text)
    return re.sub(r"\s+", " ", text).strip()

def fmt_date(d):
    if not d: return ""
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", d)
    if m:
        months = ["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        return f"{months[int(m.group(2))]} {m.group(3)}, {m.group(1)}"
    return d

def shorten(t, n=350):
    t = t[:n]
    cut = max(t.rfind("."), t.rfind("!"), t.rfind("?"))
    return (t[:cut+1] if cut > n//2 else t.rstrip()+"...").strip()

pos = sorted([r for r in cn_tp if r.get("rating",0)>=4 and len(r.get("text",""))>80],
             key=lambda x: len(x.get("text","")), reverse=True)[:2]
neg = sorted([r for r in cn_tp if r.get("rating",0)<=2 and len(r.get("text",""))>80],
             key=lambda x: len(x.get("text","")), reverse=True)[:1]
reds = sorted([r for r in cn_reddit
               if r.get("body") and len(r.get("body",""))>60
               and "changenow" in r.get("body","").lower()
               and r.get("author","") not in ("[deleted]","AutoModerator")],
              key=lambda x: x.get("score",0), reverse=True)[:2]

lines = []
if pos:
    lines.append("**Trustpilot \u2014 positive**\n")
    for r in pos:
        txt = clean(shorten(r["text"]))
        name = clean(r.get("author","") or "Anonymous")
        date = fmt_date(r.get("date",""))
        url = r.get("url","https://www.trustpilot.com/review/changenow.io")
        ss = "\u2605"*int(r.get("rating",5)) + "\u2606"*(5-int(r.get("rating",5)))
        lines += [f'> "{txt}"', ">",
                  f"> \u2014 {name}, [{ss} Trustpilot]({url})" + (f", {date}" if date else ""), ""]
if neg:
    lines.append("**Trustpilot \u2014 critical**\n")
    for r in neg:
        txt = clean(shorten(r["text"]))
        name = clean(r.get("author","") or "Anonymous")
        date = fmt_date(r.get("date",""))
        url = r.get("url","https://www.trustpilot.com/review/changenow.io")
        ss = "\u2605"*int(r.get("rating",1)) + "\u2606"*(5-int(r.get("rating",1)))
        lines += [f'> "{txt}"', ">",
                  f"> \u2014 {name}, [{ss} Trustpilot]({url})" + (f", {date}" if date else ""), ""]
if reds:
    lines.append("**Reddit community**\n")
    for r in reds:
        body = clean(r["body"][:280])
        sub = r.get("subreddit","CryptoCurrency")
        user = r.get("author","?")
        sc = r.get("score",0)
        plink = r.get("permalink","")
        url = ("https://reddit.com"+plink) if plink else f"https://www.reddit.com/r/{sub}/"
        lines += [f'> "{body}"', ">",
                  f"> \u2014 u/{user}, [r/{sub}]({url}) ({sc} points)", ""]
lines.append("> **Coinwy Editorial \u2014 My take:** The Trustpilot corpus at 450,000+ reviews is the strongest credibility signal ChangeNOW has. Compliance holds appear in a minority of reviews and are resolved \u2014 the pattern matches AML process, not exit-scam behaviour.")

block = "\n".join(lines)

fp = os.path.join(BASE, "coinwy/changenow-batch/articles/01-changenow-vs-swapzone-2026.md")
content = open(fp, encoding="utf-8").read()
new_content = re.sub(
    r"(## What users actually say\n)(.*?)(?=\n## )",
    lambda m: m.group(1)+"\n"+block+"\n",
    content, flags=re.DOTALL|re.IGNORECASE
)
if new_content != content:
    open(fp, "w", encoding="utf-8").write(new_content)
    print("OK: 01-changenow-vs-swapzone-2026.md updated")
else:
    print("ERROR: no change")
