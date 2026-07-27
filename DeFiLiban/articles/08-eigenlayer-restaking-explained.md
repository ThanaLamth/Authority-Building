---
title: "EigenLayer Restaking Explained"
slug: "/infrastructure/layer2/eigenlayer-restaking-explained"
meta_title: "EigenLayer Restaking Explained: Mechanism, Slashing Risk, and AVS Security Model"
meta_description: "How EigenLayer restaking works, what AVSs are and what they pay for, how liquid restaking protocols layer on top, slashing conditions, and how EigenLayer compares to Symbiotic and Karak."
search_intent: "Informational"
primary_keyword: "eigenlayer restaking explained"
secondary_keywords:
  - "eigenlayer avs explained"
  - "eigenlayer slashing risk"
  - "liquid restaking protocol risk"
  - "eigenlayer vs symbiotic"
  - "restaked eth security model"
category: "infrastructure/layer2"
last_reviewed: "2026-07-27"
schema:
  - "Article"
  - "FAQPage"
  - "BreadcrumbList"
internal_links:
  - "/protocols/staking/lido-staking-withdrawal-explained"
  - "/risk/smart-contract/defi-yield-farming-risks-2026"
  - "/risk/exploits/defi-bridge-risk-explained"
---

# EigenLayer Restaking Explained: Mechanism, Slashing Risk, and AVS Security Model

Ethereum's security is the aggregate of staked ETH enforced by slashing: validators who behave dishonestly have a portion of their staked ETH destroyed. EigenLayer extends this mechanism. Restakers opt in to subject their staked ETH to additional slashing conditions beyond Ethereum's base consensus rules, in exchange for rewards from the protocols (called AVSs -- Actively Validated Services) that use that security.

The value proposition is economic: AVSs need security but cannot bootstrap a validator set from scratch. Restakers supply existing, already-staked ETH as security for AVSs, and receive AVS-specific rewards on top of base Ethereum staking yield. The risk is that restakers who behave incorrectly for an AVS can have their ETH slashed by that AVS's slashing conditions, independent of their Ethereum consensus behavior.

EigenLayer launched slashing on mainnet in Q1 2026, following a multi-year testnet period. As of Q2 2026, EigenLayer held approximately -15 billion in total restaked ETH value across native restakers and liquid restaking protocol deposits (verify against DefiLlama at publish time -- figures change daily).

## What EigenLayer Does: Restaking ETH Security to Multiple Networks

Ethereum requires validators to stake 32 ETH and behave correctly in consensus. Slashing -- the destruction of up to 100% of a validator's stake -- enforces this. The slashing is imposed by the Ethereum protocol itself when a validator double-signs or equivocates.

EigenLayer adds an opt-in layer. Validators (and holders of liquid staking tokens like stETH, rETH, or cbETH) can opt in to EigenLayer and select specific AVSs to secure. By opting in, they agree to additional slashing conditions defined by each AVS they join. If they violate an AVS's slashing condition, a portion of their restaked position -- which is the same ETH position securing Ethereum consensus -- is slashed.

The result: one pool of staked ETH secures multiple services simultaneously. The economic security provided to each AVS is not a separate pool of capital; it is the same ETH, subject to multiple independent slashing conditions. This is the core of EigenLayer's design and the core of its risk profile.

## Mechanism Table: Restaking, Operator, AVS, and Slashing

| Actor | Action | Economic stake | Slashing condition | Yield source |
|---|---|---|---|---|
| Restaker (native) | Restakes 32+ ETH directly into EigenLayer via validator withdrawal credentials | Full staked ETH | AVS-defined slashing condition + Ethereum consensus slashing | Ethereum staking APY + AVS rewards |
| Restaker (LST) | Deposits stETH/rETH/cbETH into EigenLayer smart contracts | LST value (which represents underlying ETH) | AVS-defined slashing on deposited LST | LST yield + AVS rewards (no Ethereum base staking APY directly) |
| Operator | Runs AVS software on behalf of delegated restakers | Restakers' ETH they manage | AVS slashing applies to operator's managed stake | Portion of AVS rewards + operator fee |
| AVS | Defines slashing conditions, pays operator rewards | None (the restaker's ETH is the security) | Sets own slashing conditions via EigenLayer's slasher contract | Pays rewards to restakers/operators from own protocol revenue or token |
| EigenLayer protocol | Enforces slashing conditions; manages operator/restaker delegation | None -- infrastructure only | N/A | Protocol fee (not yet enabled as of mid-2026) |

## How AVSs Use Restaked Security: What They Pay For and What They Risk

AVS categories as of mid-2026 include:
- **Data availability layers** (EigenDA, the first EigenLayer AVS): off-chain data storage attested by operators; restakers secure attestation honesty
- **Oracle networks**: operators attest to off-chain data; slashing if they provide incorrect data
- **Bridges and cross-chain messaging**: operators attest to event finality on other chains; slashing if they falsely attest
- **Rollup sequencers**: operators run rollup sequencing with slashable commitment to ordering rules

What an AVS pays for: economic security. An AVS with  billion in restaked ETH behind it can claim that attacking the AVS requires buying and risking  billion in ETH -- the same cost as attacking a significant portion of Ethereum's validator set. For protocols that need security guarantees (data availability, oracle networks, bridges) but do not have their own validator sets, this is the value of EigenLayer.

What the AVS risks: if its slashing conditions are poorly designed, they could be triggered by honest operator behavior (false slashing), destroying restaker capital and collapsing trust in the AVS. Poorly designed slashing conditions are an existential threat to AVS adoption.

## What Slashing Conditions Look Like for Restakers

Slashing in EigenLayer V2 (the architecture live as of Q1 2026) uses a "Unique Stake" model:

- Restakers allocate portions of their stake to specific operators and AVSs
- Slashing conditions are defined per AVS by their slashing contract
- When a slashing condition is met, the slashing contract can slash only the portion of stake allocated to that AVS -- not the restaker's full position

This is a significant design improvement over the V1 architecture, which had more open-ended slashing exposure. The Unique Stake model bounds AVS-specific slashing: an AVS can slash at most the allocated stake, not the restaker's entire position. Restakers can limit their AVS exposure by limiting the allocation percentage to any single AVS.

**Examples of slashing conditions by AVS type:**
- EigenDA operator slashing: if an operator attests to data availability for a batch and then goes offline before the data is accessible, or provides false availability proofs
- Oracle network slashing: if an operator attests to a price that deviates by more than X% from consensus
- Bridge slashing: if an operator attests to a transaction as finalized on chain A that was not finalized

None of these slashing conditions had triggered a major slashing event as of mid-2026, as EigenLayer's mainnet slashing was newly live and AVSs were in early operational stages.

## How Liquid Restaking Protocols Layer On Top

Liquid restaking protocols (LRTs) accept stETH, ETH, or other LSTs, deposit them into EigenLayer on behalf of users, select AVS exposures, and return a liquid receipt token:

- **Ether.fi**: the largest LRT by TVL; eETH and weETH; users deposit ETH, ether.fi restakes via EigenLayer and selects AVS allocations; weETH is used as collateral in Aave, Pendle, and other protocols
- **Renzo**: ezETH; deposits into EigenLayer and allocates to selected AVSs; April 2024 depegging event when ezETH/ETH trading price fell ~5% below NAV due to liquidity thin spot
- **Kelp DAO**: rsETH; similar LRT structure

The ezETH depeg in April 2024 is the most instructive LRT risk event to date. Renzo announced plans to exclude ezETH from an upcoming EIGEN airdrop, creating sell pressure on ezETH. Thin secondary market liquidity amplified this into a ~5% temporary depeg. The underlying restaked ETH was not slashed or lost -- the depeg was a secondary market liquidity event, not a slashing event or protocol exploit. But it demonstrates that LRT tokens, like stETH in June 2022, can depeg from their ETH value in secondary markets even when the underlying is intact.

LRT risks stacked on EigenLayer risks:
- Smart contract risk in the LRT protocol (separate from EigenLayer)
- AVS selection risk: LRT operators choose which AVSs to allocate to; restakers cannot always see or change this
- Secondary market liquidity risk: LRT tokens can depeg from NAV
- Yield compounding: LRTs may reinvest rewards in ways that create additional protocol dependencies

## Risk Profile: Smart Contract, Slashing Cascade, Governance, and Operator Concentration

### Smart contract risk

EigenLayer's core contracts are among the more recent high-value contracts in DeFi. The protocol went through several audits including Sigma Prime and Code4rena competitive audits before mainnet. However, EigenLayer's contract complexity is substantial: the delegation architecture, slashing contracts, AVS registration, and restaking mechanics involve multiple interacting contract systems with a shorter collective mainnet track record than Lido or Aave. Each new AVS integration adds smart contract risk specific to that AVS's slashing and reward contracts.

### Slashing cascade risk

The "restaking contagion" scenario: one operator manages restake across multiple AVSs. If that operator gets slashed by one AVS due to a genuine behavior violation, the same ETH position is reduced. If the same operator then fails to meet another AVS's requirements because their stake is now below threshold, a second slashing event triggers. Multiple AVS failures by the same operator, or by many operators simultaneously in a correlated failure (e.g., all running the same buggy AVS software), could produce concurrent slashing across the system.

EigenLayer's Unique Stake model was designed to limit cascade risk: the stake allocated to each AVS is capped, so slashing from one AVS cannot exceed the allocation to that AVS. This limits but does not eliminate cascade risk. A 10% allocation to a badly-designed AVS still represents a 10% potential loss of the restaked position. Across multiple AVSs with multiple bad designs, losses stack.

### Governance risk

EigenLayer is governed by the Eigen Foundation and the EIGEN token. As of mid-2026, on-chain governance was still in development phases; core protocol parameters were controlled by the EigenLayer team with multi-sig governance. The degree of decentralization in slashing parameter changes and AVS whitelist additions is lower than mature protocols like Aave or Compound. This is an expected early-stage governance condition, not a unique flaw -- but it means the risk of a governance mistake or team-level decision with unilateral impact is higher than in more mature on-chain governance systems.

### Operator concentration

As of mid-2026, a small number of operators (P2P Validator, Figment, Chorus One, and others) managed the majority of delegated restake on EigenLayer. Operator concentration means that one operator's failure, compromise, or slashing event affects a disproportionately large portion of restaked ETH. EigenLayer's interface allows restakers to see operator statistics including delegated TVL, AVS participation, and historical performance, which supports informed operator selection.

## Comparable Infrastructure: Symbiotic and Karak

**Symbiotic** is an alternative restaking protocol that accepts broader collateral types -- not only ETH and LSTs, but ERC-20 tokens more generally. Symbiotic's design allows any token with sufficient economic weight to serve as security for AVS-equivalents. This enables a more diverse restaking ecosystem but also means the collateral quality underpinning security is more variable than EigenLayer's ETH-denominated model.

**Karak** is a restaking protocol with a different AVS incentive and slashing model, initially focused on EVM chains with a more permissioned AVS onboarding process. As of mid-2026, Karak's TVL and AVS count were substantially smaller than EigenLayer's.

Both alternatives represent the same architectural bet as EigenLayer -- that staked assets can serve double duty as economic security for multiple services -- with different collateral policies and governance structures.

## Yield and Risk Trade-Off: What Restakers Earn and What They Put at Risk

**What restakers earn:**
- Base Ethereum staking yield (if natively restaking) or LST yield (if depositing LSTs)
- AVS rewards from each selected AVS: paid in EIGEN, the AVS's own token, or ETH; typically range from 0.5-3% additional APY per AVS as of mid-2026 (verify at publish)
- LRT protocols typically aggregate this into a single quoted APY

**What restakers put at risk:**
- Their staked ETH, subject to slashing by each AVS they are allocated to
- Secondary market value of LRT tokens (subject to depeg)
- Smart contract risk of EigenLayer + the LRT protocol + each AVS's slashing contract
- Governance risk of both EigenLayer protocol and individual AVS governance

The central tension: restaking allows the same ETH to earn yield from multiple sources simultaneously, which increases the apparent yield-to-capital ratio. It does so by adding slashing surfaces that did not exist before restaking. Each AVS allocation is an additional slashing condition applied to the same ETH. Whether the total AVS reward income justifies the total slashing risk exposure depends on the quality of each AVS's slashing contract design and operating conditions -- which, for most restakers, is not independently verifiable. The restaker's practical choice is between delegating to an operator with a public track record and limiting AVS exposure through allocation caps, or using an LRT that makes that selection on their behalf at the cost of opacity about the selection criteria.

---

## What we checked ourselves before writing this

For this article, we reviewed the EigenLayer whitepaper (Sreeram Kannan et al., 2023), EigenLayer's mainnet documentation at docs.eigenlayer.xyz, the EigenLayer V2 slashing architecture specification, ether.fi documentation at ether.fi/docs, the Renzo ezETH depeg event coverage from CoinDesk and Blockworks (April 2024), and DefiLlama LRT TVL data. EigenLayer TVL figures (-15B) are approximate and should be verified against DefiLlama at publish time. Operator concentration statistics should be verified against the EigenLayer app's operator dashboard at publish time.

---

## Frequently asked questions

**What is EigenLayer?**
EigenLayer is an Ethereum protocol that allows staked ETH to be "restaked" -- used as economic security for additional protocols (called Actively Validated Services, or AVSs) beyond Ethereum consensus itself. Restakers opt in to additional slashing conditions from AVSs and receive AVS-specific rewards in return for extending their staked ETH's security guarantees to those services.

**What is an AVS in EigenLayer?**
An AVS (Actively Validated Service) is a protocol that uses EigenLayer to bootstrap economic security. AVSs define their own slashing conditions and pay rewards to operators and restakers who secure them. Examples include EigenDA (a data availability layer), oracle networks, bridge attestation networks, and rollup sequencers.

**What is slashing in EigenLayer?**
Slashing is the destruction of a portion of a restaker's staked ETH when a slashing condition is violated. EigenLayer's Unique Stake model (V2, live Q1 2026) allows AVSs to slash only the specific allocation of stake directed to them, not the restaker's full position. An operator running an AVS incorrectly -- providing false attestations, going offline during required availability windows, or violating the AVS's specific behavioral rules -- can trigger slashing of the portion allocated to that AVS.

**What is liquid restaking and how does it work?**
Liquid restaking protocols (like ether.fi, Renzo, and Kelp) accept ETH or LSTs, deposit them into EigenLayer, select AVS allocations on behalf of users, and return a liquid receipt token (eETH, ezETH, rsETH). These tokens can be used in DeFi while the underlying ETH earns restaking yield. The risk is that the LRT operator's AVS selection and operational quality directly affects restaker exposure -- and LRT tokens can depeg from NAV in secondary markets even when the underlying position is intact.

**Can restaking cause cascading slashing?**
In theory, yes. If an operator manages restake across multiple AVSs and gets slashed by one AVS, their available stake for other AVSs decreases. If other AVSs have minimum stake thresholds, the operator's remaining stake may fall below them, triggering additional consequences. EigenLayer's Unique Stake model caps each AVS's slashing exposure to its specific allocation, limiting cascade severity, but does not eliminate it. No major cascade event had occurred as of mid-2026.

**How does EigenLayer compare to Symbiotic?**
EigenLayer focuses on ETH and liquid staking tokens as collateral. Symbiotic accepts broader ERC-20 collateral types, allowing a wider range of assets to serve as security for AVS-equivalent services. EigenLayer has substantially higher TVL and more AVS deployments as of mid-2026. Symbiotic's broader collateral policy introduces more variable collateral quality than EigenLayer's ETH-denominated model.
