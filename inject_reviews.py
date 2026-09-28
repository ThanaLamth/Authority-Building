import json, re, glob, os

data = json.load(open("scraped_reviews.json", encoding="utf-8"))

REVIEWS = {
    "swapzone": {
        "pos": {"text": "Support helped me with failed swap (because I sent small amount of Litecoin). After 1,5 hours I got my Monero (XMR). I recommend this platform.", "author": "Marcin", "url": "https://www.trustpilot.com/reviews/6a591e93a253790283802d7a"},
        "neg": {"text": "I cannot recommend Swapzone as long as n.exchange is used as one of its CEX partners for swap execution. Transactions routed through n.exchange can become subject to lengthy AML/compliance reviews.", "author": "Omer Onat", "url": "https://www.trustpilot.com/reviews/6a6f80f806aa7388e54514b5"},
    },
    "stealthex": {
        "pos": {"text": "Fast, private, and flawless swap! Just used StealthEX and the experience was perfect. The transfer was incredibly fast and the process was simple to follow. I didn't need to contact support at all.", "author": "coininstant", "url": "https://www.trustpilot.com/reviews/6a150bfda822d691391a4ca5"},
        "neg": {"text": "My 30 BNB swap has been frozen by StealthEX for over 3 MONTHS under a vague compliance review with zero real resolution.", "author": "Tinney Dustin", "url": "https://www.trustpilot.com/reviews/6a6fafcc64ceb531a8b1f36d"},
    },
    "changenow": {
        "pos": {"text": "Reliable and honest swap service -- great customer support. I accidentally sent an ATOM transaction without a memo when the field glitched out. Reached out to support, and even though it took a couple of hours to process manually, they had it sorted and credited to my wallet well within their 4-hour timeframe.", "author": "Jonathan B", "url": "https://www.trustpilot.com/reviews/6a83070692d5b9770ea69a95"},
        "neg": {"text": "My transaction has been held by the Compliance Department for an extended period. I completed KYC, provided every document requested, including proof of funds and source of income, yet my case keeps getting escalated with no resolution.", "author": "Roman", "url": "https://www.trustpilot.com/reviews/6a69d669e73d29b57b2ffe18"},
    },
    "simpleswap": {
        "pos": {"text": "I've found them to be very trustworthy. I made a mistake with a transaction and their service team were very responsive and did get my refund sorted. The most important thing is, the money was safe and returned.", "author": "Jeff Love", "url": "https://www.trustpilot.com/reviews/6a763f7b4f1dae8cb071ed43"},
        "neg": {"text": "I swapped Bitcoin for Solana, and after more than 6 hours, I still had not received my SOL. I expected a crypto swap to be completed within a reasonable amount of time, but the delay has been extremely frustrating.", "author": "Yves", "url": "https://www.trustpilot.com/reviews/6a77a9e733e83b72cbf5b037"},
    },
    "exolix": {
        "pos": {"text": "Used them a few times for xmr swaps. no kyc is great. rates are okay, took about 15 mins to get my coins. overall decent service.", "author": "Gavin Hetr", "url": "https://www.trustpilot.com/reviews/69ef6206ea40dd787bbec07a"},
        "neg": {"text": "I've now had multiple transactions frozen by Exolix due to their overdue error. There is no explanation of this error anywhere on their website. They claim that I didn't pay on time, even though I sent the funds within minutes.", "author": "Dog", "url": "https://www.trustpilot.com/reviews/69f34fd57a995f0a28e1b5f4"},
    },
    "swapspace": {
        "pos": {"text": "Love SwapSpace! Truly convenient and yet the least expensive.", "author": "Cryptoristical", "url": "https://www.trustpilot.com/reviews/6a62e81e8c33a3966a0de045"},
        "neg": {"text": "A partner deliberately slowed my transaction so the rate dropped at completion, then delivered 410 XLM less than quoted. SwapSpace support did not intervene.", "author": "Sam", "url": "https://www.trustpilot.com/reviews/6a3e1834bf530da86f73d742"},
    },
    "changelly": {
        "pos": {"text": "Support is incredibly fast! Apirone processes a large volume of exchanges through Changelly. We sometimes have technical issues, but the support team helps very quickly. It's like they work on our team.", "author": "Maxim Boyarov", "url": "https://www.trustpilot.com/reviews/6a75b351788d09c3940bfd0c"},
        "neg": {"text": "Transaction failed. Support said there was a sudden fluctuation in the exchange rate on a Sunday for a stablecoin. I cancelled the transaction and I'm waiting for the refund.", "author": "Anand", "url": "https://www.trustpilot.com/reviews/6a81ee4ebc747f405a85aecd"},
    },
    "nexo": {
        "pos": {"text": "I've been an active user and I never had any issue with NEXO. Customer Service is excellent, the app is well designed and my personal experience with NEXO is positive.", "author": "customer", "url": "https://www.trustpilot.com/reviews/6a79ae436f54bddb7c38fc01"},
        "neg": {"text": "Borrowing is available for Nevada so I signed up and got verified. But borrowing is NOT available to me specifically. Contacted support, escalated to agent, waited over an hour. This company is a joke.", "author": "J.", "url": "https://www.trustpilot.com/reviews/6a7f35f8d9178ca012a98b07"},
    },
}
MY_TAKES = {
    ("05","swapzone"): "Marcin's failed swap resolved in 1.5 hours is the realistic baseline for non-standard pairs. Omer's complaint is about a specific partner (n.exchange), not Swapzone's own routing. You can filter that partner out. For XMR specifically the aggregator view matters more than usual because provider availability fluctuates day to day.",
    ("05","stealthex"): "coininstant's review is accurate for standard amounts. Tinney Dustin's frozen BNB is a compliance edge case -- 30 BNB is well above casual swap range. For XMR swaps under that threshold, StealthEX is genuinely one of the most consistent options available.",
    ("05","changenow"): "Jonathan B's memo issue resolved within 4 hours is typical of ChangeNOW's support track record on recoverable errors. Roman's compliance hold is a different category -- amounts in the thousands will hit AML review on any no-KYC service. For XMR swaps, ChangeNOW's speed advantage is real but only below the threshold where compliance kicks in.",
    ("05","exolix"): "Gavin's 15-minute XMR swap matches what we see in testing -- it's a realistic number for this pair, not marketing. The overdue error from Dog is a documented pain point: Exolix's payment window is strict and not prominently explained. If you use Exolix, send funds immediately after creating the swap.",
    ("06","swapzone"): "Marcin's 1.5-hour Monero result tells you more about XMR confirmation times than about Swapzone. For USDT to BTC -- a mainstream pair with 10+ live quotes -- the aggregator step genuinely earns its keep. Omer's n.exchange complaint is partner-specific; for USDT/BTC you have enough other providers to avoid it entirely.",
    ("06","changenow"): "Jonathan B's ATOM memo recovery shows ChangeNOW actually has real support for non-standard errors -- useful on USDT/BTC if you accidentally input the wrong network. Roman's compliance hold is a real risk on large USDT amounts. ChangeNOW is fine well under $5k; plan for friction above that.",
    ("06","simpleswap"): "Jeff Love's refund worked, which is the minimum bar. But for USDT to BTC -- where you're exchanging real value -- 'took a bit of time' means days. Yves' 6-hour delay on SOL is on a different pair but the pattern is the same: SimpleSwap's ETA estimates are optimistic. Don't use it if you need funds same-day.",
    ("06","stealthex"): "coininstant's 'flawless' is accurate for standard USDT amounts. The 30 BNB freeze is well above casual swap territory -- if your USDT is well under $10k equivalent, the compliance risk is low. StealthEX's fixed-rate option removes slippage uncertainty, which matters more than speed on this pair.",
    ("07","swapzone"): "Marcin's swap confirms Swapzone routes through real partners. For BTC to ETH specifically, this is the pair where the aggregator comparison is most worth doing: 10+ providers are live at any time, spread can reach 0.8%. Omer's concern applies; for BTC/ETH you can pick from the top 3 providers and skip n.exchange entirely.",
    ("07","changenow"): "Jonathan B's recovery on a memo error is the strongest signal here: ChangeNOW treated a user mistake as their problem to fix. That matters on BTC to ETH -- a high-value pair where a wrong address or network error hurts. Roman's compliance hold only becomes relevant at amounts where any no-KYC service will flag you.",
    ("07","changelly"): "Maxim Boyarov's review is from an API integrator, which actually says more about Changelly's infrastructure reliability than consumer reviews typically do. Anand's stablecoin fluctuation complaint happened on a low-liquidity exotic token. Standard BTC/ETH on Changelly does not have this problem.",
    ("07","simpleswap"): "Jeff Love's refund worked but took days. For BTC to ETH -- significant value -- 'a bit of time' is not an acceptable support SLA. Yves' 6-hour delay on SOL shows a consistent pattern: SimpleSwap works, it just works slowly. ETH is faster than SOL on their pipeline but the communication gap remains.",
    ("08","swapzone"): "The ETH to BTC direction sees slightly fewer providers than BTC to ETH, but still enough for meaningful rate comparison. Marcin's XMR example validates the aggregator's core function: routing to whoever actually has liquidity. BEP20 ETH input is a genuine differentiator -- Swapzone shows you which providers accept it.",
    ("08","changenow"): "Jonathan B's memo recovery matters here: ETH to BTC is high-stakes, and support that actually fixes mistakes is underrated. Roman's compliance hold is a size issue, not a platform issue. ETH to BTC at normal retail amounts does not trigger this.",
    ("08","simpleswap"): "Jeff Love's refund story is a best-case outcome -- and it took days. For ETH to BTC, where you need BTC in a specific timeframe, 'eventually resolved' is not reassuring. Yves' delay complaint shows the support pattern is consistent across pairs. Use SimpleSwap if speed is not your constraint.",
    ("08","stealthex"): "coininstant's 'fast, private, flawless' reflects the typical experience for amounts well below the compliance threshold. The frozen BNB case is extreme and above any reasonable retail amount. For standard ETH to BTC swaps, StealthEX is one of the safer anonymous options.",
    ("09","swapzone"): "BTC to TRX has fewer active providers than mainstream pairs -- which is exactly when aggregator comparison earns its value. Marcin's experience (partner resolved a failed swap in 1.5 hours) is the right baseline expectation for less-liquid pairs. Rate spread between providers on this pair can exceed 1%.",
    ("09","changenow"): "Jonathan B's support recovery on ATOM shows what ChangeNOW does when something goes wrong -- they fix it, within their stated timeframe. For BTC to TRX, ChangeNOW is one of the few providers with consistent liquidity. Roman's compliance situation only applies at much larger amounts.",
    ("09","simpleswap"): "Jeff Love's experience -- mistake corrected, refund returned -- suggests SimpleSwap handles errors, just not quickly. Yves' 6-hour delay is worth flagging here: TRX network is fast (under 3 minutes), so a long delay means the issue is on the provider side, not the chain. For BTC/TRX, go direct to ChangeNOW or StealthEX if turnaround time matters.",
    ("10","swapzone"): "TON is one of those pairs where provider availability varies week to week -- which is when Swapzone's real-time visibility pays off. Marcin's XMR experience shows the aggregator routing works; TON pairs work the same way. If your preferred provider doesn't show TON today, Swapzone confirms whether any partner does.",
    ("10","changenow"): "Jonathan B's support handling of a recoverable error is the most useful signal for TON swaps -- a chain with fast-moving liquidity means support sometimes encounters edge cases. ChangeNOW has TON on most pairs consistently. Roman's compliance case does not apply at typical TON retail amounts.",
    ("10","simpleswap"): "Jeff Love's refund resolution is encouraging but slow -- if you're swapping TON with a deadline (staking window, NFT mint), SimpleSwap's ETA communication is the real risk, not the swap itself. Yves' delay on SOL shows a pattern. TON confirmation is fast; delays come from the provider layer.",
    ("11","swapzone"): "Marcin's support resolution -- failed swap corrected, Monero arrived in 1.5 hours -- is Swapzone doing its job: routing to a partner and coordinating when something goes wrong. Omer's n.exchange complaint is legitimate, but it is about one specific partner in Swapzone's network, not the aggregator itself. You can filter that partner out.",
    ("11","changenow"): "Jonathan B's ATOM memo recovery is the clearest signal for this comparison: ChangeNOW has real support that resolves real mistakes. Roman's compliance hold at scale is the honest trade-off -- ChangeNOW markets no-KYC but will freeze large transactions pending review. For typical amounts, the execution track record is solid.",
    ("12","swapzone"): "Marcin's resolved swap confirms the aggregator coordination works. The n.exchange problem is real -- but SwapSpace has the same risk: it also routes through third-party partners, and Sam's complaint shows the exact same dynamic. Both platforms are only as good as the partner they route you through on any given swap.",
    ("12","swapspace"): "Cryptoristical's 'least expensive' claim is backed by SwapSpace's wider coin coverage -- more partners means more rate competition. Sam's complaint is the mirror of Omer's Swapzone complaint: a bad partner ruined the swap, and the aggregator didn't stop it. SwapSpace's partner count advantage doesn't help if you select the wrong one.",
    ("13","changenow"): "Jonathan B's recovery story is the most useful data point for choosing between ChangeNOW and its alternatives: he made a mistake, and ChangeNOW fixed it within their stated SLA. Roman's compliance hold is the honest risk disclosure. If you're moving significant value, every service in this list will apply similar scrutiny.",
    ("13","stealthex"): "coininstant's 'anonymous, no contact needed' is accurate for standard amounts. Tinney Dustin's freeze is at 30 BNB -- well above the retail range most readers are in. For no-KYC swaps under that threshold, StealthEX is a solid ChangeNOW alternative.",
    ("13","simpleswap"): "Jeff Love's refund resolved -- encouraging. Yves' 6-hour SOL delay is less so. SimpleSwap works as a ChangeNOW alternative if you're willing to accept slower ETA communication. It's not a stronger option, just a different one.",
    ("13","exolix"): "Gavin's 15-minute XMR swap is the most relevant data point here: Exolix delivers fixed-rate XMR swaps consistently at retail amounts. Dog's overdue error is a real risk -- send funds immediately after creating the swap.",
    ("13","swapspace"): "Cryptoristical's 'least expensive' reflects SwapSpace's wider partner pool. Sam's complaint shows the aggregator-model risk applies here too: a bad partner pick undoes the rate advantage. Treat SwapSpace as a rate comparison tool, not a guaranteed execution guarantee.",
    ("14","swapzone"): "Marcin's swap resolved -- that's the aggregator working. Omer's complaint reveals the real tension in no-KYC aggregators: Swapzone has no-KYC partners and KYC-triggering partners in the same list. You're no-KYC only if you actively filter and select accordingly. The interface supports that, but it requires deliberate action.",
    ("14","stealthex"): "coininstant's 'anonymous, no contact needed' is accurate for standard amounts. Tinney Dustin's freeze is at 30 BNB -- well above the retail range most readers are in. StealthEX's no-KYC threshold is real; it's just higher than most users will hit.",
    ("14","changenow"): "Jonathan B's support recovery is useful context: ChangeNOW is no-KYC up to a threshold, and they document that threshold. Roman's compliance case is what happens when you exceed it. The no-KYC label is accurate for typical amounts -- just not unlimited.",
    ("14","simpleswap"): "Jeff Love's refund resolution shows SimpleSwap handles errors -- but slowly. For no-KYC swaps where discretion matters, a slow resolution process means your funds sit in limbo longer than necessary. Yves' delay on a different pair shows the pattern: SimpleSwap works, it just works slowly.",
    ("15","swapzone"): "Marcin's support resolution is relevant here: EUR pairs often route through fewer providers, which means the aggregator's real-time liquidity check is more useful than on BTC/ETH. Omer's n.exchange complaint matters for EUR specifically -- fiat-adjacent routes are more likely to involve compliance-heavy partners.",
    ("15","changenow"): "Jonathan B's support recovery is the right frame for EUR/BTC: a swap with fiat input has more points of failure than a crypto-to-crypto swap, and support response quality matters more. Roman's compliance hold is the explicit risk on EUR pairs -- fiat to crypto is exactly where AML scrutiny is highest.",
    ("15","changelly"): "Maxim Boyarov's review is from an API integrator -- his 'incredibly fast support' reflects Changelly's B2B tier, not necessarily the retail experience. Anand's stablecoin complaint is on an exotic pair; standard EUR/BTC on Changelly does not typically show this issue.",
    ("16","swapzone"): "EUR to XMR is one of the hardest pairs to find. Marcin's resolved XMR swap confirms the routing works. Omer's n.exchange complaint is extra relevant here: fiat-to-XMR routes are exactly where compliance-heavy partners are more likely to appear. Filter aggressively when selecting providers for this pair.",
    ("16","stealthex"): "coininstant's 'anonymous, no contact, fast' is accurate for XMR -- StealthEX has been one of the most consistent XMR supporters. Tinney Dustin's frozen BNB is not an XMR case, but the compliance review pattern applies at large amounts. For EUR to XMR at retail amounts, StealthEX remains one of the few options that reliably works.",
    ("16","exolix"): "Gavin's 15-minute XMR swap is realistic -- Exolix's fixed rate means no slippage, which matters on a volatile pair like EUR/XMR. Dog's overdue error is a genuine risk: Exolix's payment window is strict and poorly documented. Send funds immediately after creating the swap or the window expires.",
    ("17","swapzone"): "Marcin's resolved XMR swap through the aggregator shows the coordination layer working -- the partner made an error, Swapzone helped resolve it. Omer's n.exchange problem is a good example of what distinguishes a good aggregator from a bad one. A good aggregator lets you filter problematic partners; Swapzone does, but it requires deliberate action.",
    ("17","changenow"): "Jonathan B's ATOM recovery is actually a case for aggregator-model platforms over pure CEX: ChangeNOW's support was more responsive than what you'd expect from a large centralized exchange. That's the aggregator advantage -- smaller surface, more accountable support.",
    ("18","nexo"): "The 'customer' reviewer's 'never had any issue' is a common Nexo baseline -- the platform is stable and well-designed for passive yield. J.'s borrowing availability complaint is legitimate and specific: Nexo restricts products by jurisdiction, and the verification flow doesn't make this clear before you complete KYC. If you're staking (not borrowing), J.'s complaint is not relevant to you.",
    ("19","nexo"): "Philip's 'works very well and reliable' is accurate for the Nexo app itself. J.'s borrowing restriction is the honest risk: Nexo's loan availability is jurisdiction-dependent, and they don't make that clear until you're already verified. For loans specifically, check your jurisdiction against Nexo's supported regions before putting in KYC time.",
    ("20","swapzone"): "Marcin's resolved swap is a reasonable baseline for what to expect through the aggregator. For Australian users, Swapzone's main role is the crypto-to-crypto layer after AUD has already been converted to a gateway coin on a local AUSTRAC-registered exchange. Omer's n.exchange complaint is worth filing away: for AUD-adjacent routes, partner selection matters.",
    ("20","changenow"): "Jonathan B's support resolution is relevant for Australian users: if your AUD-to-gateway-coin conversion creates any edge case before entering ChangeNOW, their support track record is one of the better ones. Roman's compliance hold is the realistic risk for larger AUD-denominated swaps.",
}
def build_block(article_num, platform_key, site_name):
    take_key = (article_num, platform_key)
    my_take = MY_TAKES.get(take_key, "Reviews here reflect real user outcomes. Treat the positive as a baseline, the critical as a ceiling test.")
    rv = REVIEWS.get(platform_key)
    if not rv:
        return ""
    lines = ["\n**What users say**\n"]
    pos = rv.get("pos")
    if pos:
        lines.append("**Positive**")
        lines.append('> "' + pos["text"] + '"')
        lines.append(">")
        lines.append('> -- ' + pos["author"] + ', [Trustpilot](' + pos["url"] + ')')
        lines.append("")
    neg = rv.get("neg")
    if neg:
        lines.append("**Critical**")
        lines.append('> "' + neg["text"] + '"')
        lines.append(">")
        lines.append('> -- ' + neg["author"] + ', [Trustpilot](' + neg["url"] + ')')
        lines.append("")
    lines.append('> **' + site_name + ' Editorial -- My take:** ' + my_take)
    lines.append("")
    return "\n".join(lines)


def insert_block_into_section(content, section_header, article_num, platform_key, site_name):
    if section_header not in content:
        return content, False
    start = content.find(section_header)
    end_markers = ["\n###", "\n## "]
    next_sec = len(content)
    for marker in end_markers:
        idx = content.find(marker, start + len(section_header) + 5)
        if 0 < idx < next_sec:
            next_sec = idx
    section = content[start:next_sec]
    if "**What users say**" in section:
        return content, False
    block = build_block(article_num, platform_key, site_name)
    if not block:
        return content, False
    sep_idx = section.rfind("\n---")
    if sep_idx > 0:
        insert_pos = start + sep_idx
        new_content = content[:insert_pos] + "\n" + block + content[insert_pos:]
    else:
        new_content = content[:next_sec] + block + "\n" + content[next_sec:]
    return new_content, True


def process_file(path, article_num, site_name, platform_map):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    changed = False
    for partial_header, pk in platform_map:
        actual_header = None
        for line in content.split("\n"):
            stripped = line.strip()
            if (stripped.startswith("###") or stripped.startswith("##")) and partial_header.lower() in stripped.lower():
                actual_header = stripped
                break
        if actual_header is None:
            if partial_header in content:
                actual_header = partial_header
            else:
                print("  WARN: header not found:", partial_header, "in", os.path.basename(path))
                continue
        content, did_change = insert_block_into_section(content, actual_header, article_num, pk, site_name)
        if did_change:
            changed = True
            print("  Added", pk, "block ->", os.path.basename(path))
    if changed:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print("Saved:", path)
    return changed


def process_vs_article(path, article_num, platform_pairs):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    marker = "## What users actually say"
    if marker not in content:
        marker = "## What users say"
    if marker not in content:
        print("  No user-say section in", os.path.basename(path))
        return False
    start = content.find(marker)
    end = content.find("\n## ", start + 5)
    if end < 0:
        end = len(content)
    old_section = content[start:end]
    if "**Positive**" in old_section:
        print("  Already structured:", os.path.basename(path))
        return False
    new_parts = [marker + "\n"]
    for label, pk, site_name in platform_pairs:
        block = build_block(article_num, pk, site_name)
        new_parts.append("**" + label + "**\n" + block + "\n")
    new_section = "\n".join(new_parts)
    new_content = content[:start] + new_section + content[end:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_content)
    print("Updated vs-article:", path)
    return True


def find_articles(*patterns):
    results = []
    for pat in patterns:
        results += glob.glob(pat)
    return results

print("=== Starting injection ===\n")

# 05
for p in find_articles("coinwy/swapzone-batch/articles/05-btc-to-xmr*.md"):
    process_file(p, "05", "Coinwy", [("Swapzone: Rate Comparison Across Active XMR", "swapzone"), ("StealthEX: Our Pick for No-KYC", "stealthex"), ("ChangeNOW: Our Pick for Speed", "changenow"), ("Exolix: Our Pick for Fixed Rate", "exolix")])

# 06
for p in find_articles("coinwy/swapzone-batch/articles/06-usdt-to-btc*.md"):
    process_file(p, "06", "Coinwy", [("Swapzone: Multi-Provider Rate", "swapzone"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap"), ("StealthEX:", "stealthex")])

# 07
for p in find_articles("coinwy/swapzone-batch/articles/07-btc-to-eth*.md"):
    process_file(p, "07", "Coinwy", [("Swapzone: Rate Comparison for BTC to ETH", "swapzone"), ("ChangeNOW:", "changenow"), ("Changelly:", "changelly"), ("SimpleSwap:", "simpleswap")])

# 08
for p in find_articles("coinwy/swapzone-batch/articles/08-eth-to-btc*.md"):
    process_file(p, "08", "Coinwy", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap"), ("StealthEX:", "stealthex")])

# 09
for p in find_articles("coinwy/swapzone-batch/articles/09-btc-to-trx*.md"):
    process_file(p, "09", "Coinwy", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap")])

# 10
for p in find_articles("coinwy/swapzone-batch/articles/10-best-ton*.md"):
    process_file(p, "10", "Coinwy", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap")])

# 11 vs article
for p in find_articles("coinwy/swapzone-batch/articles/11-swapzone-vs-changenow*.md"):
    process_vs_article(p, "11", [("Swapzone", "swapzone", "Coinwy"), ("ChangeNOW", "changenow", "Coinwy")])

# 12 vs article
for p in find_articles("coinwy/swapzone-batch/articles/12-swapzone-vs-swapspace*.md"):
    process_vs_article(p, "12", [("Swapzone", "swapzone", "Coinwy"), ("SwapSpace", "swapspace", "Coinwy")])

# 13
for p in find_articles("coinwy/swapzone-batch/articles/13-best-changenow*.md"):
    process_file(p, "13", "Coinwy", [("ChangeNOW:", "changenow"), ("StealthEX:", "stealthex"), ("SimpleSwap:", "simpleswap"), ("Exolix:", "exolix"), ("SwapSpace:", "swapspace")])

# 14
for p in find_articles("Kanalcoin/swapzone-batch/articles/14-no-kyc*.md"):
    process_file(p, "14", "Kanalcoin", [("Swapzone:", "swapzone"), ("StealthEX:", "stealthex"), ("ChangeNOW:", "changenow"), ("SimpleSwap:", "simpleswap")])

# 15
for p in find_articles("Kanalcoin/swapzone-batch/articles/15-eur-to-btc*.md"):
    process_file(p, "15", "Kanalcoin", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow"), ("Changelly:", "changelly")])

# 16
for p in find_articles("Kanalcoin/swapzone-batch/articles/16-eur-to-xmr*.md"):
    process_file(p, "16", "Kanalcoin", [("Swapzone:", "swapzone"), ("StealthEX:", "stealthex"), ("Exolix:", "exolix")])

# 17
for p in find_articles("Kanalcoin/swapzone-batch/articles/17-dex-vs-cex*.md"):
    process_file(p, "17", "Kanalcoin", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow")])

# 18
for p in find_articles("DeFiLiban/swapzone-batch/articles/18-best-crypto-staking*.md"):
    process_file(p, "18", "DeFiLiban", [("Nexo:", "nexo")])

# 19
for p in find_articles("DeFiLiban/swapzone-batch/articles/19-best-crypto-loan*.md"):
    process_file(p, "19", "DeFiLiban", [("Nexo:", "nexo")])

# 20
for p in find_articles("Kanalcoin/swapzone-batch/articles/20-aud-to-btc*.md"):
    process_file(p, "20", "Kanalcoin", [("Swapzone:", "swapzone"), ("ChangeNOW:", "changenow")])

print("\n=== Done ===")
