---
title: "Aave v3 Interest Rate Model Explained"
slug: "/protocols/lending/aave-v3-borrowing-rates-explained"
meta_title: "Aave v3 Interest Rate Model: How Borrowing Rates Are Set and What Moves Them"
meta_description: "How Aave v3 sets borrowing rates using the utilization ratio, what Slope 1 and Slope 2 mean, how E-Mode and Isolation Mode change risk parameters, and how Aave v3 compares to Compound v3 and Euler."
search_intent: "Informational"
primary_keyword: "aave v3 borrowing rates explained"
secondary_keywords:
  - "aave v3 interest rate model"
  - "aave v3 utilization ratio"
  - "aave v3 e-mode explained"
  - "aave v3 isolation mode"
  - "aave v3 vs compound v3"
category: "protocols/lending"
last_reviewed: "2026-07-27"
schema:
  - "Article"
  - "FAQPage"
  - "BreadcrumbList"
internal_links:
  - "/yield/farming/impermanent-loss-explained"
  - "/risk/smart-contract/defi-yield-farming-risks-2026"
  - "/protocols/stablecoins/makerdao-dsr-explained"
---

# Aave v3 Interest Rate Model: How Borrowing Rates Are Set and What Moves Them

Aave v3 does not use an order book or a fixed yield schedule. Every borrowing rate it quotes is a continuous function of one variable: what fraction of the supplied liquidity is currently borrowed. That variable is the utilization ratio, and every rate change in Aave v3 traces back to it.

The protocol launched on Polygon on March 16, 2022, and subsequently expanded to Ethereum mainnet, Arbitrum, Optimism, Avalanche, Base, BNB Chain, Scroll, and additional networks. As of Q2 2026, Aave v3 held approximately  billion in total value locked across all deployments, making it the largest decentralized lending protocol by TVL. The auditors who reviewed v3 before launch included Trail of Bits, ABDK, Sigma Prime, Peckshield, OpenZeppelin, and SigmaPrime. No critical exploit has occurred in Aave v3's core lending contracts as of July 2026.

The mechanism that matters to suppliers and borrowers is the interest rate model. Understanding it means understanding three things: the utilization ratio formula, the two-slope structure, and what E-Mode and Isolation Mode change about which rates apply to which assets.

## How Aave v3 Sets Interest Rates: The Utilization Ratio Model

The utilization ratio U is:

`
U = total borrows / total liquidity
`

where 	otal liquidity = total supplied + accrued interest - total borrows.

When U is low -- most liquidity is sitting idle -- borrowing rates are cheap. When U approaches 1.0 -- nearly all liquidity is borrowed and suppliers have little left to withdraw -- rates spike steeply. This spike is the protocol's tool for rebalancing: high rates deter new borrowing and attract new supply, which pulls U back down.

Each asset on Aave has its own interest rate strategy contract that encodes four parameters:

| Parameter | What it is | Who sets it |
|---|---|---|
| optimalUtilizationRate (U*) | The utilization threshold that separates the two rate slopes | Aave governance vote |
| aseVariableBorrowRate | The minimum borrow rate at U=0 | Aave governance vote |
| ariableRateSlope1 | Rate increase per unit of utilization below U* | Aave governance vote |
| ariableRateSlope2 | Rate increase per unit of utilization above U* | Aave governance vote |

For USDC on Ethereum as of June 2026, these were approximately: U* = 90%, base = 0%, Slope 1 = 6%, Slope 2 = 60%. At 90% utilization, the borrow APY approaches 6%. At 95% utilization, Slope 2 kicks in and the rate climbs rapidly toward the theoretical maximum. At 100% utilization, no liquidity can be withdrawn. The steep Slope 2 makes full utilization economically self-correcting before it becomes a liquidity crisis.

## Mechanism Table: Supply, Borrow, Liquidation, and Rate Adjustment

| Action | Input | Output | Rate driver | Risk at this step |
|---|---|---|---|---|
| Supply | Asset deposited to pool | aToken issued 1:1 | U decreases, borrow rate falls | Smart contract; aToken de-pegging |
| Borrow | Collateral pledged, debt taken | Borrowed asset, variable debt token | U increases, borrow rate rises | Oracle feed for collateral pricing |
| Rate update | Block timestamp change | New borrow APY per asset | Continuous: new U at each block | None -- pure computation |
| Liquidation | Health factor < 1.0 | Collateral sold, debt repaid, bonus to liquidator | U may shift | Oracle failure can trigger false liquidation |
| Rate param change | AAVE governance vote | New U*, Slope 1, Slope 2 | Governance execution delay | Governance attack or parameter error |

aTokens are interest-bearing: 1 aUSDC holds slightly more than 1 USDC value at any time after deposit, accruing supply APY continuously. The borrow rate is always higher than the supply rate because utilization is never 100% and Aave captures the spread.

## What the Optimal Utilization Ratio Is and Why It Matters

U* is the inflection point of the rate curve. Below it, rate changes per unit of U are gradual. Above it, rate changes are severe. The design intent is that normal market activity keeps U below U*: borrowers take debt, repay it, and supply stays adequately liquid. U* is where the protocol communicates urgency.

Different asset classes have different U* values because their liquidity risk profiles differ:

- **USDC, USDT, DAI** (Ethereum mainnet, ~June 2026): U* = 90%. Stablecoins are borrowed heavily for leverage and yield strategies; the protocol tolerates high utilization before applying steep rates.
- **WBTC, WETH**: U* = 80-85%. Crypto collateral is more volatile; earlier rate pressure discourages utilization that could leave the pool illiquid during a market drawdown.
- **Long-tail assets**: U* = 45-65%. Higher rate pressure at lower utilization because thinner liquidity and faster price movements make full utilization dangerous.

When U consistently stays above U*, that is the on-chain signal that the pool needs either a parameter adjustment (lower U*, steeper Slope 1) or more supply capital. Aave governance votes have adjusted U* and slope parameters for USDC, DAI, and WBTC multiple times in 2024-2026 in response to market conditions, with proposals initiated through the Aave governance forum and executed via the Aave governance contracts with a minimum time delay.

## How Isolation Mode and E-Mode Change Risk Parameters

**E-Mode (Efficiency Mode)** groups correlated assets and allows tighter loan-to-value ratios between them. A borrower in the stablecoin E-Mode category can supply USDC and borrow USDT with an LTV of 97% rather than the default ~75% cross-asset LTV. This works because correlated assets -- stablecoins, liquid staking tokens versus ETH -- are unlikely to diverge sharply against each other in a short window. The trade-off: E-Mode positions concentrate correlated-asset liquidation risk. During stress events that break stable correlations (the USDC depeg during the Silicon Valley Bank collapse in March 2023, the stETH depeg in June 2022), E-Mode's tight LTV ratios produce cascading liquidations from positions that were technically efficient minutes before.

Each E-Mode category has its own LTV, liquidation threshold, and liquidation bonus:

| Category | LTV | Liquidation threshold | Liquidation bonus |
|---|---|---|---|
| Stablecoins | 97% | 97.5% | 0% |
| ETH-correlated (ETH/stETH/wstETH) | 93% | 95% | 1% |
| BTC-correlated | 90% | 93% | 2% |

**Isolation Mode** works in the opposite direction. When a new or higher-risk asset is listed on Aave, governance can place it in Isolation Mode, which means it can be used as collateral but only to borrow a specific subset of approved stablecoins, and only up to a debt ceiling. Isolation Mode prevents a new asset from contaminating the entire cross-asset collateral pool if its price oracle or liquidity profile proves unreliable. When Aave expanded to non-canonical assets in 2024-2025, Isolation Mode was the mechanism that allowed those listings without requiring the same audit bar as USDC or ETH.

## Risk Profile: Oracle, Liquidation, Governance, and Smart Contract

### Oracle risk

Aave v3 uses Chainlink price feeds as its primary oracle for collateral valuation. Health factor calculations run on these feeds: when a feed reports a price drop, health factors fall, and liquidations trigger. An oracle that reports a false price -- through a flash loan attack, data feed manipulation, or Chainlink node failure -- can trigger mass liquidations against healthy positions, or prevent correct liquidations against underwater ones.

Aave mitigated this with price feed fallbacks and circuit breakers in v3: if Chainlink feeds go stale or deviate beyond a threshold, the protocol can pause. The Gauntlet and Chaos Labs risk teams, contracted by Aave DAO, monitor oracle deviation metrics and propose parameter adjustments when feed reliability degrades. No Aave v3 exploit has originated from a Chainlink oracle failure as of July 2026, but oracle risk remains the largest single non-code risk category for any lending protocol.

### Liquidation mechanics

Liquidation occurs when a borrower's health factor falls below 1.0:

`
Health Factor = (sum of collateral value * liquidation threshold) / total debt value
`

When HF < 1.0, any address can repay up to 50% of the borrower's debt and receive the equivalent collateral value plus a liquidation bonus. For USDC debt, the bonus on ETH collateral is 5%: for every  of debt repaid, the liquidator receives  in collateral. The bonus creates the economic incentive for liquidators to act immediately when HF dips below 1.0.

The risk to borrowers is that liquidation is not negotiated: it triggers automatically, executes in the same block, and the borrower loses collateral whether they were aware of the health factor drop or not. High-volatility assets and narrow LTV buffers shorten the time between a market move and a liquidation.

### Smart contract risk

Aave v3 has the deepest audit history of any lending protocol: six audit firms pre-launch, continuous formal verification work through Certora, and an ongoing bug bounty through Immunefi with a maximum payout of ,000. The core contracts -- Pool, LendingPool, AToken, VariableDebtToken -- have operated without exploit since March 2022. Third-party integrations and cross-chain deployments carry incremental risk that the core Ethereum contracts do not.

### Governance risk

The AAVE token governs parameter changes: U*, slopes, LTV ratios, asset listings, E-Mode categories, and fee settings. The governance process includes forum discussion, off-chain Snapshot vote, and on-chain vote with an execution timelock. Parameter errors have occurred: a September 2021 Compound governance error (not Aave, but structurally similar) caused  million in erroneous COMP distributions. Aave governance has not produced a comparable error in v3, but the delegation structure -- where large AAVE holders dominate votes -- means that governance risk is partially a question of whether large token holders act in protocol rather than self-interest.

## Comparable Protocols: Compound v3 and Euler

**Compound v3 (Comet)** uses a single-asset borrowing model: each Comet market has one base borrowable asset (USDC or ETH) and accepts multiple collateral types. Borrowers cannot borrow arbitrary assets cross-collateral; they borrow only the Comet's base asset. This simplifies the rate model and reduces composability risk, but it limits flexibility compared to Aave v3's open cross-asset model. Compound v3's utilization model is structurally similar to Aave v3's, but parameters are set per Comet rather than per asset within a shared pool.

**Euler v2** uses a modular vault design where each vault is an isolated market with its own risk parameters. Rather than isolating assets at the protocol level (like Aave's Isolation Mode), Euler v2 isolates at the vault level: each vault creator sets LTV, oracle, and interest rate strategy independently. The flexibility is greater than Aave, but so is the burden on vault operators to set parameters correctly. Euler v1 lost  million in March 2023 to a reentrancy exploit; Euler v2 was redesigned with formal verification and launched in 2024.

## Yield and Risk Trade-Off: What Suppliers and Borrowers Each Take On

**Suppliers** earn the spread between what borrowers pay (borrow APY) and what the protocol keeps (reserve factor, typically 10-20% per asset). Supply APY = borrow APY * U * (1 - reserve factor). At U = 90% and a borrow APY of 6%, a supplier earns roughly 4.9% on stablecoins. The risk is smart contract, oracle, and governance -- not market price risk on the supplied asset if it is a stablecoin. The residual risk is that a mass liquidation event or oracle failure cascades through the pool faster than the liquidation mechanism can resolve positions.

**Borrowers** take on the rate risk of a variable model: borrowing APY can spike from 6% to 60%+ if utilization hits the Slope 2 range. Borrowers using collateral assets also carry the collateral liquidation risk: a 5% drop in ETH price when using ETH as collateral at a 75% LTV does not trigger liquidation, but a 20% drop often does. The tension that matters for borrowers: E-Mode offers capital efficiency that can cut the required collateral buffer by 15-20% compared to default mode, but it does so by assuming correlated assets will not diverge -- an assumption that has broken during every major crypto market stress event in 2022 and 2023.

The Aave v3 interest rate model is among the most battle-tested designs in DeFi. Its risk record holds up precisely because the interest rate mechanism does what it is designed to do: apply rate pressure before utilization becomes a crisis. What it cannot do is protect against oracle failure, governance missteps, or collateral-asset price cascades. Those risks are structurally outside the rate model, and no interest rate design resolves them.

---

## What we checked ourselves before writing this

For this article, we reviewed the Aave v3 technical documentation at docs.aave.com, the Aave v3 whitepaper (January 2022), the Aave governance forum (governance.aave.com) for parameter update history, the Certora formal verification reports for Aave v3 core contracts, and the Gauntlet risk parameter recommendations published through 2024-2026. We referenced the Aave v3 interest rate strategy contracts on Etherscan for USDC and WETH parameter values (verified June 2026). All utilization ratio examples are illustrative of the mechanism and should be verified against live Aave analytics (app.aave.com or DefiLlama lending data) at publish time.

---

## Frequently asked questions

**How does Aave v3 calculate the borrowing rate?**
Aave v3 uses a two-slope linear model. Below the optimal utilization ratio (U*), the borrow rate increases gradually with utilization via Slope 1. Above U*, the rate increases steeply via Slope 2. The formula is: if U <= U*, borrow rate = base rate + (U / U*) * Slope 1; if U > U*, borrow rate = base rate + Slope 1 + ((U - U*) / (1 - U*)) * Slope 2. Each asset has its own rate strategy contract with separately configured parameters.

**What is E-Mode in Aave v3?**
E-Mode (Efficiency Mode) allows borrowers to use assets from a correlated category -- stablecoins, ETH-correlated, BTC-correlated -- with tighter loan-to-value ratios than the cross-asset default. The stablecoin E-Mode allows LTVs up to 97%, compared to a typical 75-80% for cross-asset borrowing. E-Mode increases capital efficiency but concentrates liquidation risk because correlated assets that define the category tend to depeg simultaneously during market stress.

**What is Isolation Mode in Aave v3?**
Isolation Mode restricts a listed collateral asset to borrowing only specific stablecoins, up to a governance-set debt ceiling. It is used for new or higher-risk assets that governance wants to list without exposing the full cross-asset collateral pool to the asset's oracle or liquidity risk. Isolated assets cannot be used as cross-collateral with non-isolated assets in the same borrowing position.

**What triggers a liquidation in Aave v3?**
Liquidation triggers when a borrower's health factor falls below 1.0. Health factor equals the sum of (collateral value * liquidation threshold) divided by total debt value. Any address can then repay up to 50% of the debt and receive the collateral equivalent plus the liquidation bonus for that asset. Liquidations are permissionless, immediate, and execute in the same block as the trigger.

**How has Aave v3 changed governance of rate parameters?**
Aave governance (AIP process) sets all core risk parameters: U*, Slope 1, Slope 2, LTV, liquidation threshold, reserve factor, and E-Mode category membership. The Gauntlet and Chaos Labs risk teams submit parameter recommendations on a regular basis based on on-chain utilization and volatility data. Proposals go through a forum discussion period, an off-chain Snapshot vote, an on-chain governance vote, and a timelock before execution.

**What is the difference between variable and stable borrow rates in Aave v3?**
Aave v3 deprecated the stable borrow rate feature during the v3.1 upgrade in April 2024, following a vulnerability disclosure in v2's stable rate implementation and sustained low demand for stable rates across v3 markets. As of April 2024, all new borrowing positions in v3 use variable rates. Existing stable rate positions were migrated through the protocol's debt swap mechanism.
