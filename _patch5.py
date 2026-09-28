import pathlib
BASE = r"C:\Users\admin\Authority-Building"

def ins(anchor, img, alt, cap):
    block = "**Live Screenshot (July 2026)**\nFile: `../media/{img}`\nAlt text: `{alt}`\nCaption: `{cap}`\n\n![{alt}](../media/{img})\n\n*{cap}*\n\n{anchor}".format(img=img, alt=alt, cap=cap, anchor=anchor)
    return (anchor, block)

fixes = [
    ("coinwy\\swapzone-batch\\articles\\03-best-instant-crypto-swap-no-registration.md",
     ins("## Comparison Table: 6 No-Registration Swap Services","live-swapzone-homepage.png","Swapzone no-account instant swap interface July 2026","Swapzone homepage reviewed July 2026 -- no account, no email, no KYC required at the aggregator level."))
]

for rel, (old, new) in fixes:
    fp = pathlib.Path(BASE) / rel
    c = fp.read_text(encoding="utf-8")
    if old in c:
        fp.write_text(c.replace(old, new, 1), encoding="utf-8")
        print("PATCHED: " + rel)
    else:
        print("SKIP: " + rel)
