# DeFiLiban -- First 10 Article Outlines

Site identity: DeFi protocol deep-dive specialist
Pillar: /protocols/, /yield/, /liquidity/, /risk/, /infrastructure/
Reader: DeFi practitioners -- yield farmers, protocol researchers, DAO contributors, on-chain analysts
Voice: Technical and precise. Mechanism first, judgment second. Clinical on risk.
Date: 2026-07-24

---

## Shared brief rules

- Open with the protocol's core mechanism -- what it optimizes and how
- Mechanism table required: input / output / constraint per core function
- Risk section covers all four: smart contract, liquidity, oracle, governance
- Cite protocol docs or on-chain data for every numerical claim
- Comparable protocols section: one sentence per comparable, difference only
- End with yield/risk trade-off summary, not a general conclusion
- Banned: easy to use, beginner-friendly, simple, just, game-changing, revolutionary

---

## Article list

| # | Primary keyword | H1 | Path |
|---|---|---|---|
| 1 | `uniswap v4 liquidity pools explained` | Uniswap v4 Hooks and Liquidity Pools: Mechanism, Risk, and What Changes | `/protocols/dex/uniswap-v4-hooks-liquidity-pools` |
| 2 | `aave v3 borrowing rates explained` | Aave v3 Interest Rate Model: How Borrowing Rates Are Set and What Moves Them | `/protocols/lending/aave-v3-borrowing-rates-explained` |
| 3 | `curve finance vecrv explained` | Curve Finance veCRV Explained: Governance Weight, Gauge Votes, and Bribe Markets | `/protocols/stablecoins/curve-vecrv-explained` |
| 4 | `liquidity pool impermanent loss explained` | Impermanent Loss in Liquidity Pools: What It Is, How to Calculate It, When It Matters | `/yield/farming/impermanent-loss-explained` |
| 5 | `defi yield farming risks 2026` | DeFi Yield Farming Risks in 2026: Smart Contract, Oracle, Liquidity, and Governance | `/risk/smart-contract/defi-yield-farming-risks-2026` |
| 6 | `maker dao dsr explained` | MakerDAO DSR Explained: How the Dai Savings Rate Works and What Sets It | `/protocols/stablecoins/makerdao-dsr-explained` |
| 7 | `pendle finance yield tokenization` | Pendle Finance Yield Tokenization: PT, YT, and the Mechanics Behind Fixed Yield on DeFi | `/protocols/dex/pendle-finance-yield-tokenization` |
| 8 | `eigenlayer restaking explained` | EigenLayer Restaking Explained: Mechanism, Slashing Risk, and AVS Security Model | `/infrastructure/layer2/eigenlayer-restaking-explained` |
| 9 | `defi bridge risk explained` | DeFi Bridge Risk: How Cross-Chain Bridges Fail and What the On-Chain Evidence Shows | `/risk/exploits/defi-bridge-risk-explained` |
| 10 | `lido staking withdrawal explained` | Lido Staking and Withdrawal Explained: Queue, stETH Peg, and Protocol Risk | `/protocols/staking/lido-staking-withdrawal-explained` |

---

## Article 1 -- Uniswap v4 Hooks and Liquidity Pools

**Primary keyword:** `uniswap v4 liquidity pools explained`
**H1:** Uniswap v4 Hooks and Liquidity Pools: Mechanism, Risk, and What Changes
**Path:** `/protocols/dex/uniswap-v4-hooks-liquidity-pools`
**Word count target:** 1,200-1,800

**H2 skeleton:**
1. What Uniswap v4 Changes Relative to v3
2. How Hooks Work: When They Fire and What They Can Modify
3. Mechanism Table: Pool Creation, Swap, Liquidity, and Hook Interaction
4. Concentrated Liquidity in v4: What Carries Over From v3
5. Risk Profile: Smart Contract, Hook Dependency, and Governance
6. Comparable Protocols: How v4 Differs From Curve v2, Balancer v3, and Ambient
7. Yield and Risk Trade-Off: What LPs Gain and What They Take On

**Mechanism table columns:** Function | Input | Output | Constraint | Hook point (before/after)

**Key data to include:**
- Gas savings from singleton architecture (v4 eliminates per-pool deployment)
- Hook categories: BeforeSwap, AfterSwap, BeforeAddLiquidity, AfterAddLiquidity, BeforeRemoveLiquidity, AfterRemoveLiquidity
- Tick spacing and fee tier changes in v4
- Singleton contract vs. factory pattern comparison

**Risk section must cover:**
- Smart contract: singleton = one exploit surface covers all pools
- Hook risk: malicious or buggy hooks can drain LP funds
- Governance: hook deployment is permissionless -- no audit requirement enforced at protocol level
- Liquidity: same concentrated liquidity range risk as v3 -- out-of-range positions earn no fees

**Comparable protocols (one sentence each):**
- Curve v2: internal AMM with dynamic pegging, no hooks, tighter for stable-volatile pairs
- Balancer v3: vault-based, hooks exist but pool logic is more constrained
- Ambient (formerly CrocSwap): unified liquidity design, no hook framework

**Tension carry:** The hook framework is the most significant architectural change in Uniswap v4 -- and also the most significant new attack surface. Whether that trade-off resolves in favor of LPs depends on whether the hook audit ecosystem matures before a major hook exploit occurs.

---

## Article 2 -- Aave v3 Interest Rate Model

**Primary keyword:** `aave v3 borrowing rates explained`
**H1:** Aave v3 Interest Rate Model: How Borrowing Rates Are Set and What Moves Them
**Path:** `/protocols/lending/aave-v3-borrowing-rates-explained`
**Word count target:** 1,000-1,500

**H2 skeleton:**
1. How Aave v3 Sets Interest Rates: The Utilization Ratio Model
2. Mechanism Table: Supply, Borrow, Liquidation, and Rate Adjustment
3. What the Optimal Utilization Ratio Is and Why It Matters
4. How Isolation Mode and E-Mode Change Risk Parameters
5. Risk Profile: Oracle, Liquidation, and Governance
6. Comparable Protocols: How Aave v3 Differs From Compound v3 and Euler
7. Yield and Risk Trade-Off: What Suppliers and Borrowers Each Take On

**Mechanism table columns:** Parameter | Current value (at publish) | What sets it | Effect on rate

**Key data to include:**
- Utilization ratio formula: total borrows / total liquidity
- Slope 1 (below optimal utilization) and Slope 2 (above optimal utilization) mechanics
- Optimal utilization thresholds by asset (ETH, USDC, BTC)
- E-Mode: correlated asset category with tighter LTV ratios
- Isolation Mode: new assets isolated from cross-collateralization

**Risk section must cover:**
- Oracle risk: Chainlink price feed failures affecting liquidation triggers
- Liquidation risk: health factor below 1.0 triggers liquidation; bonus structure incentivizes liquidators
- Smart contract: v3 has been audited by multiple firms -- cite them
- Governance: rate parameters changed by AAVE governance; list major parameter votes from 2025-2026

**Comparable protocols (one sentence each):**
- Compound v3 (Comet): single-asset borrowing model, simpler but less flexible
- Euler v2: modular vault design, risk isolation at the vault level rather than the protocol level

**Tension carry:** Aave v3's E-Mode allows tighter capital efficiency but concentrates correlated-asset liquidation risk in the same market stress scenario where those correlations break down most severely.

---

## Article 3 -- Curve Finance veCRV

**Primary keyword:** `curve finance vecrv explained`
**H1:** Curve Finance veCRV Explained: Governance Weight, Gauge Votes, and Bribe Markets
**Path:** `/protocols/stablecoins/curve-vecrv-explained`
**Word count target:** 1,200-1,600

**H2 skeleton:**
1. What veCRV Is and How It Is Created
2. Mechanism Table: CRV Lock, veCRV Decay, Gauge Weight, and Boost
3. How Gauge Votes Determine CRV Emissions Per Pool
4. What the Bribe Market Is and How It Works (Votium, Paladin, Hidden Hand)
5. Risk Profile: Governance Concentration, Smart Contract, and Liquidity
6. Comparable Protocols: veTokenomics in Balancer (veBAL) and Frax (veFXS)
7. Yield and Risk Trade-Off for CRV Lockers vs. Liquidity Providers

**Mechanism table columns:** Action | Input | Output | Time constraint | Decay behavior

**Key data to include:**
- veCRV = CRV locked * (lock duration / 4 years), decaying linearly to 0
- Maximum lock: 4 years for 1 CRV = 1 veCRV
- Gauge weight: determines % of CRV emissions allocated to a pool per epoch
- Boost: up to 2.5x on LP rewards for veCRV holders providing liquidity
- Bribe market: protocols pay veCRV holders to vote for their pool's gauge

**Risk section must cover:**
- Governance concentration: Convex Finance controls majority of veCRV; single-entity risk
- Smart contract: veCRV lock contract is one of the most audited in DeFi -- but age adds technical debt
- Liquidity: CRV is illiquid when locked; early exit requires selling cvxCRV at a discount
- Oracle: Curve pools are used as price oracles by other protocols -- manipulation risk

**Comparable protocols (one sentence each):**
- Balancer veBAL: same ve-model applied to BAL, with similar gauge voting but smaller bribe market
- Frax veFXS: ve-model for FXS with direct protocol revenue distribution rather than emissions boost

**Tension carry:** The bribe market created around veCRV means that Curve's gauge system is now primarily a capital allocation mechanism for other protocols, not a system designed to optimize Curve's own liquidity. Whether that misalignment is structurally stable is the open question.

---

## Article 4 -- Impermanent Loss Explained

**Primary keyword:** `liquidity pool impermanent loss explained`
**H1:** Impermanent Loss in Liquidity Pools: What It Is, How to Calculate It, When It Matters
**Path:** `/yield/farming/impermanent-loss-explained`
**Word count target:** 1,000-1,400

**H2 skeleton:**
1. What Impermanent Loss Is and What Causes It
2. Mechanism Table: Price Ratio, Pool Rebalancing, and LP Share Value
3. How to Calculate Impermanent Loss at a Given Price Ratio
4. When Impermanent Loss Is Permanent (and When It Is Not)
5. Risk Profile: Concentrated Liquidity, Volatile Pairs, and Fee Offset
6. Comparable Structures: How IL Differs Across AMM Designs (Uniswap v2 vs. v3, Curve, Balancer)
7. Yield and Risk Trade-Off: When Fee Income Outweighs IL

**Mechanism table columns:** Price change from deposit | IL % | Pool ratio shift | Fee income needed to break even

**Key data to include:**
- IL formula: IL = 2 * sqrt(price_ratio) / (1 + price_ratio) - 1
- Table: 10% price change = ~0.1% IL; 50% = ~2.0% IL; 100% = ~5.7% IL; 200% = ~13.4% IL; 500% = ~25.5% IL
- Concentrated liquidity (Uniswap v3): IL is amplified within the range, zero outside it
- Fee income and IL offset: a pool earning 1% daily fee volume can offset substantial IL

**Risk section must cover:**
- Concentrated ranges: IL is geometrically larger in a narrow range -- show the math
- Volatile pairs: ETH/PEPE has different IL profile than ETH/USDC -- specify
- Rebalancing cost: each price move rebalances the pool, which has a gas cost in active management
- Time horizon: "impermanent" loss becomes permanent at the moment of withdrawal

**Comparable structures (one sentence each):**
- Curve StableSwap: designed for near-peg assets, IL is minimal in normal conditions
- Balancer weighted pools: multiple assets, IL distributes across all pool weights
- Uniswap v3 concentrated: IL within the range is larger than v2, but fee income per dollar is also larger

**Tension carry:** Concentrated liquidity positions earn more fees per dollar of capital but require active management to stay in range -- and the capital lost to IL while out of range does not earn fees to offset it.

---

## Article 5 -- DeFi Yield Farming Risks 2026

**Primary keyword:** `defi yield farming risks 2026`
**H1:** DeFi Yield Farming Risks in 2026: Smart Contract, Oracle, Liquidity, and Governance
**Path:** `/risk/smart-contract/defi-yield-farming-risks-2026`
**Word count target:** 1,400-1,800

**H2 skeleton:**
1. What Has Changed in the DeFi Risk Landscape Since 2023
2. Smart Contract Risk: What Audits Catch and What They Miss
3. Oracle Risk: How Price Feed Manipulation Triggers Protocol Failure
4. Liquidity Risk: What Happens When Exit Demand Exceeds Pool Depth
5. Governance Risk: How Token Voting Concentrates Protocol Control
6. Mechanism Table: Risk Type, Trigger Condition, Historical Example, Mitigation
7. Yield and Risk Trade-Off: What APY Levels Justify Each Risk Category

**Mechanism table columns:** Risk type | Trigger | Historical exploit (with date and amount) | Protocol-level mitigation | Residual risk

**Key data to include:**
- Smart contract: Euler Finance exploit (March 2023, $197M), Ronin Bridge (March 2022, $625M)
- Oracle: Mango Markets oracle manipulation (October 2022, $116M)
- Liquidity: Iron Finance bank run (June 2021), Terra/UST spiral (May 2022)
- Governance: Tornado Cash governance attack (May 2023), Compound governance parameter error (September 2021)
- Total DeFi exploit losses 2022-2024 by category (cite Rekt.news or Chainalysis)

**Risk section (this article IS the risk section -- structured accordingly):**
- For each risk type: mechanism of failure, trigger conditions, on-chain observable signals before failure
- Do not use "could be exploited" -- name what the actual mechanism is

**Comparable protocols (one sentence each) -- most resilient vs. highest historical incidents:**
- Aave v3: one of the most audited lending protocols; no major exploit to date (as of publish)
- Curve: oracle manipulation via read-only reentrancy was the live attack vector in July 2023 ($70M)
- Yearn: multiple strategy exploits in 2021-2022 due to composability with exploited base protocols

**Tension carry:** The DeFi risk landscape in 2026 has shifted from simple rug pulls toward complex composability exploits -- where the vulnerability is not in one protocol's code but in the interaction between two correctly-written contracts that produce an unexpected state.

---

## Article 6 -- MakerDAO DSR Explained

**Primary keyword:** `maker dao dsr explained`
**H1:** MakerDAO DSR Explained: How the Dai Savings Rate Works and What Sets It
**Path:** `/protocols/stablecoins/makerdao-dsr-explained`
**Word count target:** 900-1,200

**H2 skeleton:**
1. What the DSR Is and How Dai Earns It
2. Mechanism Table: DSR Pot Contract, Savings, and Governance Control
3. How the DSR Rate Is Set: Governance Votes and the Stability Fee Relationship
4. What Sky (MakerDAO Rebrand) Changes About the DSR in 2025-2026
5. Risk Profile: Smart Contract, Peg Stability, and Governance
6. Comparable Structures: DSR vs. Aave sDAI vs. Compound USDC Yield
7. Yield and Risk Trade-Off: What DSR Depositors Hold vs. What They Give Up

**Mechanism table columns:** Action | Contract | Input | Output | Governance control point

**Key data to include:**
- DSR Pot contract address on Ethereum (cite Etherscan)
- DSR rate history 2023-2026: 1% -> 5% -> 8% -> current (verify at publish)
- DSR vs. base stability fee: DSR is funded by vault stability fees
- Sky rebranding: MakerDAO -> Sky, DAI -> USDS -- how DSR translates to the new token
- sDAI (ERC-4626 wrapper): accumulates DSR yield in a transferable token

**Risk section must cover:**
- Smart contract: Pot contract is one of MakerDAO's oldest deployed contracts; upgrade path is complex
- Peg stability: if vault collateral falls and stability fees cannot fund DSR, the rate must be cut
- Governance: DSR rate is set by MKR/SKY governance; rate changes are subject to governance vote delay
- Counterparty: DSR is backed by vault stability fees from RWA collateral as of 2025 -- RWA counterparty risk applies

**Comparable structures (one sentence each):**
- Aave sDAI: Aave accepts sDAI as collateral, extending DSR yield into borrowing power
- Compound cUSDC: Compound's lending rate for USDC is market-driven, not governance-set
- USDY (Ondo): tokenized treasury yield with different redemption and counterparty structure

**Tension carry:** MakerDAO's DSR is the most battle-tested savings mechanism in DeFi -- but its yield is now substantially backed by real-world assets, meaning the counterparty risk profile is closer to a money market fund than a pure on-chain protocol.

---

## Article 7 -- Pendle Finance Yield Tokenization

**Primary keyword:** `pendle finance yield tokenization`
**H1:** Pendle Finance Yield Tokenization: PT, YT, and the Mechanics Behind Fixed Yield on DeFi
**Path:** `/protocols/dex/pendle-finance-yield-tokenization`
**Word count target:** 1,200-1,600

**H2 skeleton:**
1. What Pendle Does: Splitting Yield From Principal
2. Mechanism Table: SY, PT, and YT Creation, Pricing, and Expiry
3. How PT Gives Fixed Yield and What the Discount Represents
4. How YT Gives Leveraged Yield Exposure and What the Risk Is
5. How the Pendle AMM Prices PT and YT
6. Risk Profile: Smart Contract, Liquidity, Oracle, and Maturity Risk
7. Comparable Protocols: Pendle vs. Element Finance, Sense Protocol
8. Yield and Risk Trade-Off: Fixed vs. Variable Yield Positions in Pendle

**Mechanism table columns:** Token | What it represents | How it is created | At maturity | Market price driver

**Key data to include:**
- SY (Standardized Yield): wrapped yield-bearing token (e.g., wstETH, stUSDT, sDAI)
- PT (Principal Token): redeemable for 1 unit of SY at maturity; trades at a discount = fixed yield
- YT (Yield Token): entitlement to all yield from SY until maturity; trades at a premium to future yield expectations
- PT pricing: (1 / (1 + implied yield)) for the remaining period
- YT risks: if underlying yield drops, YT loses value; if yield rises, YT gains

**Risk section must cover:**
- Smart contract: Pendle V2 audited by multiple firms -- cite them
- Maturity risk: PT and YT expire worthless if not redeemed properly; UI risk for non-technical users
- Liquidity: PT/YT markets are thinner than underlying asset markets; slippage matters
- Oracle: underlying yield rate feeds impact YT pricing -- oracle manipulation risk from base protocol

**Comparable protocols (one sentence each):**
- Element Finance: similar PT/YT split model; ceased operations in 2023 -- cite what changed
- Sense Protocol: fixed-rate DeFi on Ethereum; smaller TVL and lower liquidity than Pendle

**Tension carry:** YT is one of the most misunderstood instruments in DeFi -- it provides leveraged yield exposure with no principal protection, which means a drop in the underlying yield rate can reduce YT value to near zero even when the base asset is untouched.

---

## Article 8 -- EigenLayer Restaking Explained

**Primary keyword:** `eigenlayer restaking explained`
**H1:** EigenLayer Restaking Explained: Mechanism, Slashing Risk, and AVS Security Model
**Path:** `/infrastructure/layer2/eigenlayer-restaking-explained`
**Word count target:** 1,400-1,800

**H2 skeleton:**
1. What EigenLayer Does: Restaking ETH Security to Multiple Networks
2. Mechanism Table: Restaking, Operator, AVS, and Slashing
3. How AVSs Use Restaked Security: What They Pay For and What They Risk
4. What Slashing Conditions Look Like for Restakers
5. How Liquid Restaking Protocols (Ether.fi, Renzo, Kelp) Layer On Top
6. Risk Profile: Smart Contract, Slashing Cascade, Governance, and Operator Concentration
7. Comparable Infrastructure: EigenLayer vs. Symbiotic vs. Karak
8. Yield and Risk Trade-Off: What Restakers Earn and What They Put at Risk

**Mechanism table columns:** Actor | Action | Economic stake | Slashing condition | Yield source

**Key data to include:**
- Restaked ETH total (cite EigenLayer dashboard or DefiLlama)
- AVS count and categories: oracle networks, data availability layers, bridges, sequencers
- Operator structure: validators opt into serving AVSs; earn AVS-specific rewards
- Slashing: double-signing or misbehavior for an AVS can slash restaked ETH
- Liquid restaking: ether.fi's eETH, Renzo's ezETH, Kelp's rsETH -- yield compounds but adds contract risk

**Risk section must cover:**
- Smart contract: EigenLayer core contracts are new -- audit history is shorter than Lido or Aave
- Slashing cascade: one operator's AVS misbehavior could slash ETH for all restakers through that operator
- Governance: EigenLayer governance controls slashing parameters and AVS inclusion
- Operator concentration: top 10 operators hold majority of delegated restake -- named concentration risk

**Comparable infrastructure (one sentence each):**
- Symbiotic: alternative restaking protocol with broader collateral types (not ETH-only)
- Karak: restaking with a different AVS incentive and slashing model

**Tension carry:** EigenLayer introduces a new type of DeFi risk: correlated slashing events where a systemic AVS failure could trigger simultaneous slashing across multiple operators and protocols -- the "restaking contagion" scenario that no historical DeFi stress test has yet encountered.

---

## Article 9 -- DeFi Bridge Risk Explained

**Primary keyword:** `defi bridge risk explained`
**H1:** DeFi Bridge Risk: How Cross-Chain Bridges Fail and What the On-Chain Evidence Shows
**Path:** `/risk/exploits/defi-bridge-risk-explained`
**Word count target:** 1,200-1,600

**H2 skeleton:**
1. What DeFi Bridges Do and Why They Are Structurally Risky
2. Mechanism Table: Lock-Mint, Burn-Mint, and Liquidity Network Bridge Models
3. The Three Categories of Bridge Exploit: Validator, Smart Contract, and Economic
4. Historical Exploit Data: Largest Bridge Hacks 2021-2026 With Root Cause
5. Risk Profile: Custodial Trust, Smart Contract Complexity, and Multi-Chain Surface
6. Comparable Bridges: Risk Profile Comparison Across Wormhole, LayerZero, Stargate, Across
7. Yield and Risk Trade-Off: When Bridge Liquidity Provision Is Worth the Risk

**Mechanism table columns:** Bridge type | How assets move | Custody model | Exploit surface | Historical example

**Key data to include:**
- Ronin Bridge: $625M (March 2022) -- validator key compromise
- Wormhole: $320M (February 2022) -- smart contract signature verification bypass
- Nomad: $190M (August 2022) -- initialization exploit, copy-paste attack
- Harmony Horizon: $100M (June 2022) -- validator key compromise
- Total bridge exploit losses 2021-2024 (cite Rekt.news or Chainalysis)

**Risk section must cover:**
- Validator risk: multisig bridges require majority of keys -- how many signers, how are keys held?
- Smart contract: bridges have one of the highest exploit rates per protocol in DeFi
- Economic: liquidity network bridges can fail when one chain's liquidity is drained
- Multi-chain surface: a bug on any connected chain can propagate to all connected chains

**Comparable bridges (one sentence each):**
- Across Protocol: intent-based architecture eliminates lock-mint model; different risk surface
- Stargate (LayerZero): unified liquidity pool model; economic risk concentrates in pool
- Wormhole: guardian validator set; past $320M exploit was patched but trust model unchanged

**Tension carry:** The safest bridge is one that handles the fewest assets and uses the most conservative trust model -- but the market consistently rewards higher-liquidity bridges that take on more trust assumptions to provide better UX. That tension has not resolved in favor of safety.

---

## Article 10 -- Lido Staking and Withdrawal Explained

**Primary keyword:** `lido staking withdrawal explained`
**H1:** Lido Staking and Withdrawal Explained: Queue, stETH Peg, and Protocol Risk
**Path:** `/protocols/staking/lido-staking-withdrawal-explained`
**Word count target:** 1,000-1,400

**H2 skeleton:**
1. How Lido Staking Works: Validator Delegation and stETH Issuance
2. Mechanism Table: Stake, stETH Rebase, Withdrawal Request, and Queue
3. How the Ethereum Validator Exit Queue Affects Lido Withdrawal Times
4. What the stETH/ETH Peg Represents and When It Deviates
5. Risk Profile: Smart Contract, Validator Concentration, Oracle, and Governance
6. Comparable Protocols: Lido vs. Rocket Pool vs. Frax ETH vs. Coinbase cbETH
7. Yield and Risk Trade-Off: What stETH Holders Earn vs. What They Put at Risk

**Mechanism table columns:** Action | Contract | Process | Time to complete | Risk at this step

**Key data to include:**
- Lido market share: ~28-30% of all staked ETH (verify at publish via Dune or Lido dashboard)
- stETH rebase: daily accrual of staking rewards via token balance increase
- Withdrawal: request queued on Ethereum beacon chain; Lido processes batch withdrawals
- stETH peg history: June 2022 depeg to ~0.94 ETH during Three Arrows Capital collapse
- Validator set: Lido uses whitelisted node operators -- not permissionless

**Risk section must cover:**
- Smart contract: Lido contracts are among the most audited in DeFi -- cite audit firms
- Validator concentration: Lido's share of ETH staking raises concerns about Ethereum network centralization
- Oracle: stETH price feeds are used by Aave, Compound, and others as collateral -- oracle manipulation risk
- Governance: LDO governance controls node operator whitelist and fee parameters

**Comparable protocols (one sentence each):**
- Rocket Pool: permissionless node operators, 8 or 16 ETH minimum, rETH accrues rather than rebases
- Frax ETH (frxETH): dual-token model; frxETH pegs to ETH, sfrxETH accumulates yield
- Coinbase cbETH: custodial liquid staking; simpler but requires trusting Coinbase

**Tension carry:** Lido's dominant market share creates a structural risk to Ethereum itself: a validator cartel controlling over 33% of staked ETH could theoretically delay or censor finality. That Lido has not exercised this power does not resolve the structural concern about whether it should hold it.
