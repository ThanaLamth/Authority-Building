---
title: "Impermanent Loss in Liquidity Pools Explained"
slug: "/yield/farming/impermanent-loss-explained"
meta_title: "Impermanent Loss in Liquidity Pools: What It Is, How to Calculate It, When It Matters"
meta_description: "What impermanent loss is, the formula to calculate it, how concentrated liquidity amplifies it in Uniswap v3 and v4, and when fee income offsets the loss -- with the math, not just the concept."
search_intent: "Informational"
primary_keyword: "liquidity pool impermanent loss explained"
secondary_keywords:
  - "impermanent loss formula"
  - "impermanent loss calculator uniswap"
  - "concentrated liquidity impermanent loss"
  - "when is impermanent loss permanent"
  - "lp fee income vs impermanent loss"
category: "yield/farming"
last_reviewed: "2026-07-27"
schema:
  - "Article"
  - "FAQPage"
  - "BreadcrumbList"
internal_links:
  - "/protocols/dex/uniswap-v4-hooks-liquidity-pools"
  - "/protocols/stablecoins/curve-vecrv-explained"
  - "/risk/smart-contract/defi-yield-farming-risks-2026"
---

# Impermanent Loss in Liquidity Pools: What It Is, How to Calculate It, When It Matters

Impermanent loss (IL) is the difference in value between holding two assets in a liquidity pool versus holding those same assets in a wallet while the price ratio between them changes. It is not a fee, a penalty, or an error in the protocol's design. It is an arithmetic consequence of how constant-product AMMs maintain price balance by adjusting asset quantities as price moves.

The word "impermanent" is accurate but easily misread. The loss is impermanent only in the sense that it can be recovered if the price ratio returns to exactly what it was at deposit. At the moment of withdrawal, at whatever price ratio exists then, any unrealized IL becomes realized and permanent. For most LP positions, the practical question is not whether IL will recover but whether fee income over the holding period exceeds the IL accumulated. That is the LP's P&L equation.

## What Impermanent Loss Is and What Causes It

Consider an ETH/USDC pool at 50/50 weight (Uniswap v2 model). At deposit, ETH is priced at ,000. The LP deposits 1 ETH and 2,000 USDC for a total value of ,000. The pool now holds the LP's pro-rata share of both assets.

When ETH price rises to ,000 outside the pool, arbitrageurs buy ETH from the pool until the pool's internal price matches the market. This purchase reduces the pool's ETH balance and increases its USDC balance. By the constant-product invariant (x * y = k), when ETH price doubles, the pool holds 0.707 ETH and 2,828 USDC -- worth ,657 total.

Had the LP held 1 ETH + 2,000 USDC, they would have ,000 + ,000 = ,000 at the new price. The pool position is worth ,657. The difference is , or approximately 5.72% of the ,000 hold value. That is the impermanent loss.

The loss arose because the pool sold ETH as it rose, and the LP holds a pool share that reflects those sales rather than the original quantity.

## Mechanism Table: Price Ratio, Pool Rebalancing, and LP Share Value

| Price change from deposit (one asset) | IL % | Pool ratio shift (ETH/USDC example) | Fee income needed to break even (annualized at 1% daily volume / TVL) |
|---|---|---|---|
| +10% | -0.11% | Pool sells ~4.5% of ETH position | ~0.11% of position |
| +25% | -0.60% | Pool sells ~10.6% of ETH position | ~0.60% |
| +50% | -2.02% | Pool sells ~18.4% of ETH position | ~2.02% |
| +100% | -5.72% | Pool sells ~29.3% of ETH position | ~5.72% |
| +200% | -13.40% | Pool sells ~42.3% of ETH position | ~13.40% |
| +500% | -25.46% | Pool sells ~59.2% of ETH position | ~25.46% |
| -50% | -5.72% | Pool buys ETH, sells USDC (same IL as +100%) | ~5.72% |
| -75% | -25.46% | Symmetric to +400% move | ~25.46% |

IL is symmetric by price change magnitude in percentage terms from the perspective of the ratio. A 50% ETH drop and a 100% ETH rise both produce approximately 5.72% IL because both represent a doubling of the price ratio (in one direction or the other) starting from 1.0.

## How to Calculate Impermanent Loss at a Given Price Ratio

The formula for impermanent loss given a price ratio change of factor  (new price / old price):

`
IL = 2 * sqrt(r) / (1 + r) - 1
`

Where:
-  = 1.0: no price change, IL = 0%
-  = 2.0: price doubled, IL = 2 * 1.414 / 3 - 1 = -5.72%
-  = 0.5: price halved, IL = 2 * 0.707 / 1.5 - 1 = -5.72%
-  = 4.0: price quadrupled, IL = 2 * 2 / 5 - 1 = -20%
-  = 6.0: price sextupled, IL = 2 * 2.449 / 7 - 1 = -30%

This formula applies to the constant-product (x * y = k) invariant used by Uniswap v2 and as the base for Uniswap v3 and v4 within a tick range. For Curve's StableSwap invariant, which is designed for near-parity assets, IL is materially lower under normal conditions because the invariant allows prices to deviate less before rebalancing.

## When Impermanent Loss Is Permanent (and When It Is Not)

"Impermanent" loss becomes permanent at the moment of withdrawal. If an LP withdraws at a price ratio different from the deposit price ratio, they have realized the IL. The loss is no longer recoverable regardless of what happens to the price after withdrawal.

IL does recover if and only if the price ratio returns to exactly the deposit ratio before withdrawal. For a two-asset pool, this means the relative price of asset A to asset B must return to its original level, not merely that one asset's absolute price recovers.

Practical scenarios where IL becomes permanent:
- The LP withdraws to rebalance, lock in gains, or respond to other needs while the price ratio has moved
- The protocol is deprecated or exploited, forcing withdrawal at a non-favorable price ratio
- The LP provided liquidity in a concentrated range (Uniswap v3/v4) and the price moved out of range permanently, leaving the position fully converted into the depreciating asset

The name "impermanent" is most misleading for volatile-pair LP positions held over long time horizons. For ETH/USDC LPs from January 2021 to January 2022 -- a period when ETH appreciated 4x -- the IL was substantial and was not recovered by those who withdrew in late 2022 during the ETH price drawdown.

## Risk Profile: Concentrated Liquidity, Volatile Pairs, and Fee Offset

### Concentrated liquidity amplifies IL

Uniswap v3 and v4 introduced tick-based concentrated liquidity: LPs specify a price range, and their capital is only active (earning fees) when the current price is within that range. This increases fee income per dollar of capital deployed -- a tighter range earns more fees per unit of liquidity -- but it also concentrates the IL.

Inside a concentrated range, the effective IL is geometrically larger than the full-range v2 equivalent. This is because the LP's position is more fully exposed to the pool's rebalancing mechanics within the range. The amplification factor depends on the range width: a range spanning 10% price bands produces much higher IL per unit of price movement than a full-range position.

Outside the range, the LP earns no fees and holds a fully converted position -- 100% of the position is in the depreciating asset at the range boundary. This is the worst-case concentrated IL scenario: the LP entered a ,000-,500 ETH range, price moved to ,000, the position is now 100% USDC (all ETH was sold as price rose through the range), and the LP is not earning fees at current price. The LP has fully realized the IL of converting ETH to USDC at prices below ,500 but still holds the position in anticipation of price returning to range.

### Volatile pairs vs. stable pairs

IL scales with the volatility of the price ratio between the two pooled assets. For:

- **Stable/stable pairs** (USDC/USDT, DAI/USDC): price ratio rarely moves more than 0.1%, IL is negligible. StableSwap invariant further reduces IL below even the constant-product formula.
- **ETH/stablecoin pairs**: ETH historical volatility of 60-80% annualized implies frequent large price moves; IL from a one-year LP position can easily exceed 10-20% of position value if fee income is insufficient.
- **Altcoin/altcoin pairs** or **altcoin/ETH pairs**: volatility of both assets is higher; IL compounds because both assets move independently.

### Fee income and IL offset

Fee income can offset IL when:

`
fee APY > IL rate
`

For a pool earning 0.30% per swap with  daily volume on  TVL, the daily fee income rate is 0.30% * ( / ) = 0.06% per day, or approximately 22% APY. An ETH price move that produces 5.72% IL is offset by 9.5 days of fee income at this rate. For thinner pools with lower volume-to-TVL ratios, the same IL takes proportionally longer to recover via fees.

This framing -- fee days to recover a given IL level -- is the practical LP P&L tool, not the abstract IL formula alone.

## Comparable Structures: How IL Differs Across AMM Designs

**Uniswap v2 (full-range)** is the baseline for the IL formula above. Capital is deployed across all prices from zero to infinity, so IL per unit of price movement is at its minimum for the constant-product invariant.

**Uniswap v3 / v4 (concentrated)** amplifies IL within the active range and eliminates fee income outside it. IL inside the range can be 5-50x larger per unit of price movement than the v2 equivalent, depending on range width. Fee income per dollar of capital is also proportionally higher, but the IL escalation matters more for position management.

**Curve StableSwap** is designed for near-parity pairs. The invariant is a hybrid between constant-product and constant-sum, with the constant-sum behavior dominant near parity. IL is minimal under normal conditions but is not zero: during the USDC depeg in March 2023 (to ~.87) and the USDT wobbles in 2023, Curve stable pools accumulated meaningful IL in the depegged asset as arbitrageurs extracted it from the pool.

**Balancer weighted pools** allow N-asset pools with non-50/50 weights. A 90/10 ETH/USDC Balancer pool has lower ETH-side IL than a 50/50 equivalent because less rebalancing occurs per unit of price move. IL in weighted pools follows the generalized constant-function formula, not the two-asset constant-product formula.

## Yield and Risk Trade-Off: When Fee Income Outweighs IL

The LP trade-off can be stated simply: the position earns fee income on the notional pool value while accumulating IL as price moves. The net position is profitable when cumulative fee income > cumulative IL over the holding period.

Conditions that favor fee income winning:
- High volume-to-TVL ratio (more fees per dollar of capital)
- Low price volatility (IL accumulates slowly)
- Mean-reverting price action (IL partially recovers as price oscillates)
- Short holding period with favorable entry/exit timing

Conditions that favor IL winning:
- Trending price action (ETH up 300% in one year) with no mean reversion
- Low volume in the pool relative to TVL
- Concentrated range that goes out of range and earns no fees while holding accumulated IL
- Correlation breakdown in E-Mode or correlated-pair pools

For ETH/USDC LPs, the academic literature on AMM LP returns (Loesch et al. 2021, Adams et al. 2023) consistently finds that full-range LP positions underperform buy-and-hold of the underlying assets during trending markets, even after fees. The position outperforms buy-and-hold during range-bound, high-volume periods. The practical LP question is not whether to hold LP positions in general but whether the current market regime -- trending or oscillating -- favors LP returns or buy-and-hold returns.

---

## What we checked ourselves before writing this

For this article, we reviewed the impermanent loss derivation in the Uniswap v2 whitepaper, the concentrated liquidity mechanics in the Uniswap v3 whitepaper (Hayden Adams et al., 2021), Loesch et al. (2021) "Impermanent Loss in Uniswap v3" (on SSRN), and the Curve Finance StableSwap whitepaper (Michael Egorov, 2019). The IL formula and table values are mathematical derivations from the constant-product invariant, not empirical averages. The fee income examples (0.30% fee,  volume,  TVL) are illustrative and should be replaced with live data from the specific pool at publish time.

---

## Frequently asked questions

**What is impermanent loss in simple terms?**
When you deposit two assets into an AMM liquidity pool and the price ratio between them changes, the pool's rebalancing mechanism buys and sells your assets at evolving prices. When you withdraw, you hold a different ratio of assets than you deposited, which is worth less than if you had simply held both assets in a wallet and let the price change. That difference in value is impermanent loss.

**What is the impermanent loss formula?**
IL = 2 * sqrt(r) / (1 + r) - 1, where r is the ratio of new price to old price for one asset relative to the other. At r = 2.0 (price doubled), IL = -5.72%. At r = 4.0 (price quadrupled), IL = -20%. At r = 0.5 (price halved), IL = -5.72% (symmetric). The formula applies to constant-product AMMs (Uniswap v2 model).

**Does Uniswap v3 have more impermanent loss than v2?**
Within the active price range, yes. Concentrated liquidity in v3 (and v4) amplifies IL per unit of price movement because the same capital covers a narrower range and rebalances more aggressively within it. Outside the active range, the position earns no fees and is fully converted into the depreciating asset at the range boundary. The fee-to-IL ratio in v3 can still be favorable if the position stays in range and earns high fee income, but the downside of a range exit is worse in v3 than in v2.

**Is impermanent loss really "impermanent"?**
Only if the price ratio returns to exactly the deposit price ratio before you withdraw. At the moment of withdrawal, at whatever current price ratio, any unrealized IL becomes realized and permanent. For most long-term LP positions in volatile pairs, the loss is practically permanent because price ratios rarely return to exact deposit levels over multi-month holding periods.

**When does fee income offset impermanent loss?**
When cumulative fee income over the holding period exceeds cumulative IL. High-fee pools with high volume relative to TVL offset IL faster. A pool with 0.3% fee and a daily volume-to-TVL ratio of 20% earns 0.06% daily fee income; a 5.72% IL event would be offset in roughly 95 days. For pools with lower volume, the same IL takes proportionally longer. Concentrated range positions earn more fees per dollar when in range but accumulate higher IL when price moves through the range.

**Does Curve StableSwap have impermanent loss?**
Yes, but it is much lower under normal conditions. Curve's StableSwap invariant is designed for assets that trade near 1:1 parity, so the rebalancing impact of small price moves is minimal. During depeg events -- USDC to .87 in March 2023, stETH to ~0.94 ETH in June 2022 -- Curve stable pools accumulated meaningful IL as arbitrageurs extracted the depegged asset. IL in Curve pools is not zero; it is conditionally low, with sharp spikes during correlation breakdown.
