# Competitor Analysis -- best defi lending protocols 2026
Date: 2026-07-27
Primary competitors: eco.com, koinly.io, dextools.io

## eco.com
- Holds 3 SERP positions for this keyword cluster
- Uses DeFiLlama TVL data (as of May 24, 2026)
- TVL figures cited: Aave V3 $14.6B, Morpho Blue $11.8B, Sky Lending $5.6B, Spark $3.5B, Compound V3 ~$2.7B
- Structure: ranked list with brief protocol descriptions
- Weaknesses: no oracle blast radius analysis; no Morpho immutability discussion; no comparison of liquidation engine mechanics; no Fluid mention

## koinly.io
- Informational tone, broad audience targeting
- Missing: curator model risk explanation for Morpho; no E-Mode concentration risk analysis
- No audit count comparison
- Missing: Sky Savings Rate governance risk (4.5-6% set by vote, not market)
- Missing: Fluid entirely

## dextools.io
- Multiple articles, thin on mechanism depth
- No per-market isolation comparison (Aave monolithic oracle vs Morpho per-market)
- No formal verification or audit trail by firm
- Missing: Fluid, post-exploit audit provenance for Euler v2

## Content gap summary (lending)
| Gap | Competitor coverage | Priority |
|-----|---------------------|----------|
| Liquidation engine mechanics comparison | None | High |
| Oracle blast radius: monolithic vs isolated | None | High |
| Morpho LLTV immutability post-deployment | None | High |
| Fluid lending+DEX hybrid risk surfaces | None | High |
| Sky SSR governance vs. market-driven rate | None | Medium |
| Euler v2 audit provenance post-exploit | None | Medium |
| Aave audit trail by firm (10+ audits) | Partial (eco.com names firms) | Low |

## Key differentiator to build
DeFiLiban should own the oracle blast radius and liquidation engine comparison angle. Morpho LLTV immutability is the single most important security differentiation and zero competitors explain it.
