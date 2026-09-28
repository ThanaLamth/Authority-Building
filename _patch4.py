import os, pathlib

BASE = r"C:\Users\admin\Authority-Building"

def ins(anchor, img, alt, cap):
    block = "**Live Screenshot (July 2026)**\nFile: `../media/{img}`\nAlt text: `{alt}`\nCaption: `{cap}`\n\n![{alt}](../media/{img})\n\n*{cap}*\n\n{anchor}".format(img=img, alt=alt, cap=cap, anchor=anchor)
    return (anchor, block)

patches = {
"coinwy\\swapzone-batch\\articles\\08-eth-to-btc-swap-best-rate.md": [
    ins("## 6 ETH to BTC Services Reviewed (2026 List)","live-swapzone-eth-btc-query.png","Swapzone ETH to BTC live query July 2026","Swapzone ETH to BTC query reviewed July 2026 -- provider rates and rate type options at review time."),
],
"coinwy\\swapzone-batch\\articles\\09-btc-to-trx-exchange-2026.md": [
    ins("## 5 BTC to TRX Services Reviewed (2026 List)","live-swapzone-btc-trx-query.png","Swapzone BTC to TRX live query July 2026","Swapzone BTC to TRX query reviewed July 2026 -- provider rates and availability at capture time."),
],
"coinwy\\swapzone-batch\\articles\\10-best-ton-exchange-gram-2026.md": [
    ins("## Ranking scorecard","live-swapzone-btc-ton-query.png","Swapzone BTC to TON live query July 2026","Swapzone BTC to TON query reviewed July 2026 -- provider rates and availability for the TON pair."),
],
}

for rel_path, ops in patches.items():
    full_path = os.path.join(BASE, rel_path)
    content = pathlib.Path(full_path).read_text(encoding="utf-8")
    original = content
    for (old, new) in ops:
        if old in content:
            content = content.replace(old, new, 1)
            print("PATCHED: " + rel_path)
        else:
            print("SKIP: " + repr(old[:60]) + " in " + rel_path)
    if content != original:
        pathlib.Path(full_path).write_text(content, encoding="utf-8")
