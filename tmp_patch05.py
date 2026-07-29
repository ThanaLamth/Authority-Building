import pathlib

p = pathlib.Path(r'C:\Users\admin\Authority-Building\coinwy\articles\05-best-decentralized-exchanges-2026.md')
text = p.read_text(encoding='utf-8')

anchor = '## DEX risks: slippage, MEV, and smart-contract exposure'
insert = '''## Pros and cons by DEX

| DEX | Strengths | Risks |
|-----|-----------|-------|
| Uniswap | Reference EVM venue; deepest liquidity on Ethereum L2s; fee tiers from 0.01% for stablecoins; transparent route before confirmation | EVM-only; aggregators sometimes find better routes on less common pairs |
| Jupiter | Best Solana routing (0.2-0.5% better execution than direct venue on split-liquidity pairs); integrates limit orders and DCA | Solana-only; not relevant for EVM users |
| PancakeSwap | Most accessible multi-chain retail experience; BNB Chain gas under \.10; integrated portfolio and earn | Slightly higher fees (0.17-0.25%) than Uniswap stablecoin tiers; not best execution on Ethereum mainnet |
| Hyperliquid | Decentralized perps at 0.02% maker / 0.05% taker; CEX-competitive latency (200-400ms); no custody risk | Derivatives venue only; not a spot swap tool |
| Curve | Lowest slippage on stable pairs (\,000-2,000 saved vs standard AMM on \ stablecoin trade); LP fees without impermanent loss risk | Niche use case; complex gauge/veTokenomics for advanced LP participation |

'''

if anchor not in text:
    print('ANCHOR NOT FOUND')
elif insert.strip() in text:
    print('ALREADY INSERTED')
else:
    new_text = text.replace(anchor, insert + anchor)
    new_text = new_text.replace('last_reviewed: "2026-07-22"', 'last_reviewed: "2026-07-24"', 1)
    p.write_text(new_text, encoding='utf-8')
    print('done')
