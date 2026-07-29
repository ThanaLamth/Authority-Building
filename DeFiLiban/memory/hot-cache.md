# DeFiLiban Research Hot-Cache
Date: 2026-07-27
Scope: Articles 1, 2, 3 -- top/list series
Pipeline: serp-analysis -> competitor-analysis -> content-gap-analysis

---

## Article 1 -- DeFi Lending Protocols

### TVL (DeFiLlama, May 24, 2026 via eco.com)
- Aave V3: $14.6B
- Morpho Blue: $11.8B
- Sky Lending: $5.6B
- Spark: $3.5B
- Fluid: ~$1B (Ethereum + Arb + Base + Polygon)
- Compound V3: ~$2.7B (NOT in final top-5 -- replaced by Fluid)

### Protocol parameters
- Aave USDC: LTV 77%, liquidation threshold 80%, liquidation bonus 5%
- Morpho LLTV: 86% stable collateral, 77% ETH (immutable per market post-deployment)
- Aave oracle: Chainlink + custom AaveOracle wrapper with fallback path
- Aave audits: OpenZeppelin, Trail of Bits, SigmaPrime, Certora, ABDK -- 10+ reviews since V3 2022

### Key differentiators (zero competitor coverage)
- Oracle blast radius: Aave monolithic (one failure = all pools) vs Morpho per-market (one failure = one market)
- Morpho LLTV immutability: cannot be changed post-deployment -- hardest security guarantee in the category
- Fluid hybrid risk: lending+DEX creates correlated risk surfaces not present in pure lending protocols
- Sky SSR: set 4.5-6% by governance vote, not market demand -- political rate risk

### Outline changes required
- Replace Compound v3 with Fluid as #3 protocol (TVL: ~$1B, Instadapp-built, lending+DEX hybrid)
- H1 update: "Aave, Morpho, Fluid, Euler, and Spark Ranked"
- Add oracle blast radius as H2 or comparison table column
- Add Morpho immutability as explicit bullet in Morpho section

---

## Article 2 -- Liquid Staking ETH

### TVL and market data
- Lido TVL: $20.71B (DeFiLlama, April 2026)
- Total liquid staking TVL: $42.09B
- Lido market share: ~33% of all staked ETH
- Lido fee: 10% (5% DAO + 5% node operators)
- Rocket Pool TVL: ~$898.8M (July 2026)
- Rocket Pool node operators: ~2,000 independent
- stETH/ETH Curve pool: $500M+ routinely

### CRITICAL CORRECTION
- Rocket Pool Saturn 1 upgrade: bond = 4 ETH, RPL NOW OPTIONAL (was 8 ETH + RPL)
- Outline weakness bullet ("8 ETH + RPL price volatility") is OUTDATED and must be corrected

### Slashing record (on-chain, rated.network)
- Lido CSM slash: March 13, 2026 -- 6 validators, <0.047 ETH total penalties
- Prior Lido slash: October 2023 -- 20 validators, ~20 ETH total

### Key differentiators (zero competitor coverage)
- Saturn 1 architecture change and minipool economics implications
- Slashing event data with on-chain epoch evidence
- frxETH vs sfrxETH dual-token yield routing mechanics
- StakeWise v3 vault-level isolation model
- Secondary market depth numbers

---

## Article 3 -- Perpetual DEX

### Market share data (April-July 2026)
- Hyperliquid: 70%+ perp DEX volume, $180B+ 30-day, $7.3B OI -- CLEAR #1
- dYdX: $300-500M daily volume, ~$327M TVL -- #2
- GMX v2: ~$152M TVL -- #3 (fallen significantly from 2024)
- Vertex: smaller, niche -- #4
- Gains Network: synthetic coverage, gDAI vault -- #5

### CRITICAL REORDER (current outline is wrong)
- Current: GMX #1, Hyperliquid #3
- Correct: Hyperliquid #1, dYdX #2, GMX #3, Vertex #4, Gains Network #5
- H1 must reflect new order

### HyperBFT (no editorial competitor covers this)
- HotStuff-inspired BFT consensus
- 3f+1 validator requirement, 2/3 honest majority
- HyperCore (native perp L1) vs HyperEVM (EVM sidechain)
- Hyperps: oracle-independent, EMA-based mark price (not Chainlink/Pyth)
- Audit firms: QuillAudits, Zealynx

### Volume quality red flags
- Aster: 70% to 15% market share when incentive program ended
- Lighter: $232B pre-launch month, collapsed post-TGE
- dYdX: 73% market share 2023 -> single digits 2026

### Key differentiators
- HyperBFT security model (highest-priority unique angle)
- Volume quality analysis with Aster/Lighter case studies
- dYdX collapse narrative with market share data
- HyperCore vs HyperEVM settlement finality
- Gains gDAI vault capacity vs max OI mathematical relationship
