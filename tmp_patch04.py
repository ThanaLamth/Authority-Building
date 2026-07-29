import pathlib

p = pathlib.Path(r'C:\Users\admin\Authority-Building\coinwy\articles\04-best-cross-chain-bridges-2026.md')
text = p.read_text(encoding='utf-8')

anchor = '## The biggest bridge risks in 2026'
insert = '''## Pros and cons by bridge

| Bridge | Strengths | Risks |
|--------|-----------|-------|
| Across | Fastest EVM settlement (sub-60s on most routes); 0.05-0.1% LP fee is competitive; fee + time visible before wallet connect | EVM-only; no Solana, Sui, or Cosmos support |
| Stargate | Delivers native USDC/USDT on destination (not wrapped); deepest stablecoin liquidity for large transfers | LP fee scales with transfer size; not cheapest on small transfers |
| deBridge | EVM-to-Solana swap-and-bridge in one transaction; route details visible before confirm | More complexity than simple bridges; slippage on top of bridge fee |
| Wormhole | Deepest Solana and Sui ecosystem integration; \ exploit fully covered, no repeat incident since | Infrastructure layer; user experience depends on which frontend app is used |
| Squid | One-click cross-chain swap UX; handles EVM-to-Cosmos routes | Aggregation adds abstraction; gas estimate accuracy lags during congestion |

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
