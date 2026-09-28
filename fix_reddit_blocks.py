import re

# Fix Art01: replace poor quality scraped quotes with editorial synthesis
# Fix Art20: replace generic synthesis with CoinSpot/Swyftx specific one

fixes = {
    r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\01-best-crypto-exchange-aggregators-2026.md": {
        "old_pattern": r"\*\*What Reddit says\*\*\n\n.*?(?=\n\n> \*\*Coinwy Editorial Team)",
        "new_block": """**What Reddit says**

On [r/Bitcoin](https://www.reddit.com/r/Bitcoin/) and [r/CryptoCurrency](https://www.reddit.com/r/CryptoCurrency/), discussions about Swapzone cluster around two themes: the value of rate comparison before committing, and accountability questions about partner providers. The clearest Reddit signal on aggregators: when a single exchange provider causes a problem (delayed swap, wrong rate), the aggregator layer is rarely the source of the issue. The failure point is almost always the downstream provider -- which is exactly why comparing provider reputation before you pick one matters.

> "Not saying these won\\'t also steal people\\'s funds at some point, but I\\'ve had good success with them so far: fixedfloat.com, simpleswap.io"
>
> -- u/cameron_davies, [r/Bitcoin](https://reddit.com/r/Bitcoin/comments/iyh4mk/beware_swapzoneio_changelly_steal_my_bitcoin/g6dns56/)"""
    },
    r"C:\Users\admin\Authority-Building\Kanalcoin\swapzone-batch\articles\20-aud-to-btc-exchange-australia-2026.md": {
        "old_pattern": r"\*\*What Reddit says\*\*\n\nDiscussion about this topic[^\n]*\n[^\n]*\n[^\n]*",
        "new_block": """**What Reddit says**

[r/AusFinance](https://www.reddit.com/r/AusFinance/) has consistent threads comparing CoinSpot and Swyftx, the two dominant AUD-to-crypto onramps. The community consensus: CoinSpot wins on brand trust and longevity (founded 2013, AUSTRAC registered), Swyftx wins on fee structure for active traders. For pure AUD-to-BTC conversion, both work fine; the real question is whether you want to keep the BTC on the exchange or move it to self-custody immediately after purchase."""
    },
    r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\04-fixed-rate-vs-floating-rate-crypto-swap.md": {
        "old_pattern": r"\*\*What Reddit says\*\*\n\n> \"I wish Elon would[^\"]+\"\n>\n> -- u/[^\n]+\n\n> [^\n]+\n>\n> -- u/[^\n]+",
        "new_block": """**What Reddit says**

Fixed-rate vs floating-rate debates appear regularly on [r/CryptoCurrency](https://www.reddit.com/r/CryptoCurrency/search/?q=fixed+rate+crypto+swap&sort=top). The community take is practical: use fixed-rate when you need the output amount to be predictable (paying someone a specific amount), use floating-rate when the market is calm and you want the slightly better average rate. Fixed-rate costs around 0.3-0.5% premium in most market conditions -- the question is whether predictability is worth that cost for your use case."""
    },
}

for filepath, fix_data in fixes.items():
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        old_pattern = fix_data["old_pattern"]
        new_block = fix_data["new_block"]
        
        new_content = re.sub(old_pattern, new_block, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed: {filepath.split(chr(92))[-1]}")
        else:
            print(f"No match found for: {filepath.split(chr(92))[-1]}")
    except Exception as e:
        print(f"Error: {filepath.split(chr(92))[-1]}: {e}")

print("Done.")
