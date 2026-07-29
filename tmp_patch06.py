import pathlib

p = pathlib.Path(r'C:\Users\admin\Authority-Building\coinwy\articles\06-best-defi-yield-farming-platforms-2026.md')
text = p.read_text(encoding='utf-8')

anchor = '## The real risks behind DeFi yield in 2026'
insert = '''## Pros and cons by platform

| Platform | Strengths | Risks |
|----------|-----------|-------|
| Aave | Transparent yield source; clean exit any time (when utilization <100%); 4-6% USDC supply rate on v3; lowest friction (3/10) | Cascade liquidations can temporarily block withdrawal during market stress; rates variable |
| Pendle | Fixed yield via PT (4-6% annualized on stETH/USDC); active yield positioning via YT; captures yield curve trading | Requires understanding PT/YT mechanics before using; not passive; maturity exit needs a buyer |
| Morpho | Better lending efficiency than basic Aave via peer-to-peer matching and isolated markets | Isolated markets mean concentrated exposure per pool; not beginner-friendly |
| Curve | Minimal impermanent loss on stable pairs; fee income from high-volume pools (1-4% annualized on 3pool) | Advantage disappears outside pegged-asset pairs; veTokenomics complexity |
| Lido | 3-4% ETH staking yield; stETH composable on Aave, Curve, Pendle simultaneously | Three risk layers: Lido smart-contract risk, stETH peg risk (de-pegged to 0.93 ETH in June 2022), validator slashing risk |

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
