import re

REPLACEMENTS = {
    r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\02-crypto-exchange-aggregator-vs-regular-exchange.md": """**What Reddit says**

On [r/CryptoCurrency](https://www.reddit.com/r/CryptoCurrency/search/?q=crypto+exchange+aggregator&sort=top), discussions about aggregators vs direct exchanges typically arise from users who got burned by a bad rate on a single service. The consistent pattern: once someone discovers they can compare rates before committing, they do not go back. The secondary discussion is about how non-custodial aggregators sidestep the KYC exposure of going through a CEX for the same pair.""",

    r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\03-best-instant-crypto-swap-no-registration.md": """**What Reddit says**

[r/CryptoCurrency](https://www.reddit.com/r/CryptoCurrency/search/?q=instant+crypto+swap+no+KYC&sort=top) threads on no-registration swaps have one recurring piece of advice: non-custodial swap services are only as trustworthy as the provider, not the aggregator layer. Users who have had problems almost always trace the issue to a specific provider within a network, not the aggregator routing. The advice from experienced community members is to check provider reputation before selecting, and to use fixed-rate mode for amounts above $500.""",

    r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\09-btc-to-trx-exchange-2026.md": """**What Reddit says**

TRX exchange discussion on [r/Tronix](https://www.reddit.com/r/Tronix/) and [r/CryptoCurrency](https://www.reddit.com/r/CryptoCurrency/) focuses on TRX's primary use case: funding USDT-TRC20 gas fees. Most people buying TRX are not speculating on Tron itself -- they are getting a small TRX position to enable fee-free USDT transfers on the Tron network. The community advice for this use case is to use a no-KYC swap service for small TRX amounts rather than a CEX that requires identity verification for what is functionally a gas purchase.""",

    r"C:\Users\admin\Authority-Building\Kanalcoin\swapzone-batch\articles\14-no-kyc-crypto-exchanges-2026.md": """**What Reddit says**

No-KYC exchange discussions on [r/CryptoCurrency](https://www.reddit.com/r/CryptoCurrency/search/?q=no+KYC+crypto+exchange&sort=top) and [r/privacy](https://www.reddit.com/r/privacy/) are nuanced. The community distinguishes between platforms that are structurally non-custodial (and therefore have no KYC to enforce) vs platforms that are custodial but choose not to implement KYC below certain thresholds. The former category is more reliable for long-term no-KYC access -- regulatory pressure can force the latter to add KYC retroactively. The consensus recommendation for no-KYC swaps is non-custodial, wallet-to-wallet services.""",

    r"C:\Users\admin\Authority-Building\Kanalcoin\swapzone-batch\articles\16-eur-to-xmr-exchange-2026.md": """**What Reddit says**

Buying Monero with euros is a recurring question on [r/Monero](https://www.reddit.com/r/Monero/) and it has become harder over time. The community notes that major European CEXes have systematically delisted XMR (Kraken EU, Bittrex, Binance). The practical advice from the Monero subreddit in 2024-2026: use a regulated fiat-to-BTC onramp (Kraken, Bitstamp) for the EUR leg, then swap BTC to XMR via a non-custodial service like Trocador, BasicSwap, or an aggregator that includes XMR pairs. Direct EUR-to-XMR without touching a CEX is possible but requires peer-to-peer markets like LocalMonero.""",

    r"C:\Users\admin\Authority-Building\coinwy\swapzone-batch\articles\10-best-ton-exchange-gram-2026.md": """**What Reddit says**

TON exchange discussions on [r/Toncoin](https://www.reddit.com/r/Toncoin/) reflect the network's growth into a top-10 asset: the primary question is no longer whether exchanges carry TON, but which ones offer the best non-custodial access. Telegram Wallet is the most cited option for self-custody within the Telegram ecosystem, while for external swaps, community members point toward aggregators that include TON pairs rather than single-provider exchanges.""",
}

for filepath, new_block in REPLACEMENTS.items():
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Find and replace the What Reddit says block (up to the next > **Author My take)
        pattern = r'\*\*What Reddit says\*\*\r?\n.*?(?=\r?\n\r?\n> \*\*[A-Za-z])'
        new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed: {filepath.split(chr(92))[-1]}")
        else:
            print(f"No change: {filepath.split(chr(92))[-1]}")
    except Exception as e:
        print(f"Error {filepath.split(chr(92))[-1]}: {e}")

print("Done.")
