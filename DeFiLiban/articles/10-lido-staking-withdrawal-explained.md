---
title: "Lido Staking and Withdrawal Explained"
slug: "/protocols/staking/lido-staking-withdrawal-explained"
meta_title: "Lido Staking and Withdrawal Explained: Queue, stETH Peg, and Protocol Risk"
meta_description: "How Lido staking works, how stETH rebase accrual functions, what the Ethereum validator exit queue means for withdrawal timing, when stETH has depegged and why, and how Lido compares to Rocket Pool, Frax ETH, and Coinbase cbETH."
search_intent: "Informational"
primary_keyword: "lido staking withdrawal explained"
secondary_keywords:
  - "steth peg explained"
  - "lido withdrawal queue"
  - "steth vs reth"
  - "lido validator concentration risk"
  - "liquid staking token risk"
category: "protocols/staking"
last_reviewed: "2026-07-27"
schema:
  - "Article"
  - "FAQPage"
  - "BreadcrumbList"
internal_links:
  - "/infrastructure/layer2/eigenlayer-restaking-explained"
  - "/protocols/dex/pendle-finance-yield-tokenization"
  - "/risk/smart-contract/defi-yield-farming-risks-2026"
---

# Lido Staking and Withdrawal Explained: Queue, stETH Peg, and Protocol Risk

Lido is the largest liquid staking protocol on Ethereum. It accepts ETH, stakes it via a whitelisted set of professional node operators, and returns stETH -- a rebasing token that accrues Ethereum staking rewards continuously in the holder's wallet. As of Q2 2026, Lido holds approximately 9-10 million staked ETH, representing roughly 28-30% of all ETH staked on the Ethereum beacon chain (verify against Dune Analytics or the Lido dashboard at stake.lido.fi at publish time).

Three practical questions define Lido's value and risk for most users: how fast can you withdraw staked ETH, when does stETH depeg from ETH and why, and what protocol-level risks are specific to Lido as opposed to ETH staking in general. This article works through each.

## How Lido Staking Works: Validator Delegation and stETH Issuance

Depositing ETH into Lido:

1. The user deposits ETH into the Lido staking contract on Ethereum mainnet
2. Lido issues stETH 1:1 at deposit: 1 ETH deposited = 1 stETH issued
3. Lido batches deposited ETH into 32-ETH increments and assigns them to node operators
4. Node operators run Ethereum validator clients, stake the 32 ETH on the beacon chain, and earn consensus and execution layer rewards
5. Lido's oracle committee reads the accumulated rewards from the beacon chain and updates the stETH rebase

The node operator set is whitelisted and managed by Lido governance. Operators are professional staking companies -- P2P Validator, Chorus One, Blockdaemon, Kiln, and others -- rather than anonymous permissionless validators. The governance DAO approves and removes operators, sets fee splits, and manages protocol parameters.

Lido takes a 10% fee on staking rewards, split between node operators (5%) and the Lido DAO treasury (5%). The stETH holder receives the remaining 90% of staking yield via the rebase mechanism.

## Mechanism Table: Stake, stETH Rebase, Withdrawal Request, and Queue

| Action | Contract | Process | Time to complete | Risk at this step |
|---|---|---|---|---|
| Stake ETH | Lido staking contract (stETH) | ETH deposited; stETH minted 1:1; ETH queued for node operator assignment | Immediate (stETH minted in same tx) | Smart contract; oracle for stETH price in secondary markets |
| stETH rebase | stETH contract; Lido oracle | Oracle committee reads beacon chain state; rebase updates all stETH balances proportionally | Daily (oracle report every 24h) | Oracle committee consensus; beacon chain read delay |
| Request withdrawal | Lido withdrawal queue (withdrawalQueue) | User burns stETH; receives NFT representing their withdrawal request position in queue | Queue position determined at request time | Smart contract; queue wait time |
| Process withdrawal | Lido oracle + node operators | Lido requests validator exits from node operators; beacon chain validator exit queue processes them | Hours to weeks depending on exit queue depth | Ethereum exit queue depth; node operator responsiveness |
| Finalize withdrawal | withdrawalQueue contract | User claims ETH against finalized withdrawal NFT | After finalization (user must claim) | Claim function is permissionless; ETH sits safely in contract until claimed |

## How the Ethereum Validator Exit Queue Affects Lido Withdrawal Times

Since Ethereum's Shanghai/Capella upgrade in April 2023, staked ETH withdrawals have been enabled. The process involves the Ethereum validator exit queue, which limits how many validators can exit per epoch (every 6.4 minutes).

The exit churn limit scales with the total number of active validators:

| Active validators | Max validator exits per epoch | Max validator exits per day |
|---|---|---|
| 0 - 262,143 | 4 | 900 |
| 262,144 - 524,287 | 5 | 1,125 |
| 524,288 - 786,431 | 6 | 1,350 |
| >786,432 (current range as of mid-2026) | 8-10 | ~1,800-2,250 |

Each Lido validator holds 32 ETH. At 1,800 exits per day from a base of ~300,000 Lido validators, full queue clearance in a stressed scenario would take months. In practice, Lido does not request mass validator exits -- it only exits validators to fulfill withdrawal requests that cannot be covered by the protocol's buffer (ETH from new deposits not yet staked).

For normal withdrawal volume, Lido's withdrawal time ranges from hours (when the buffer has available ETH) to several days (when validator exits are needed and the Ethereum exit queue is moderately loaded). During a stress scenario where many Lido stakers request simultaneous withdrawals -- a mass exit event -- the exit queue would extend significantly. This is not a Lido-specific risk; it is an Ethereum protocol constraint that applies to all staking validators.

## What the stETH/ETH Peg Represents and When It Deviates

stETH is not strictly pegged to ETH. It is redeemable for ETH via Lido's withdrawal queue, but the redemption involves a queue wait of variable duration. stETH's market price on Curve's stETH/ETH pool reflects the premium or discount of immediate liquidity versus the queued redemption path.

When stETH trades at 1:1 with ETH, the market is pricing the queue wait and smart contract risk at zero incremental discount -- effectively valuing immediate liquidity parity with queued redemption. When stETH trades below 1 ETH, the discount represents either:
- A queue wait premium: the market requires compensation for waiting in the withdrawal queue
- A risk premium: elevated perceived risk of Lido smart contract failure or validator slashing
- A forced selling event: holders who need ETH immediately are willing to sell stETH below parity

**stETH/ETH peg history:**

| Date | stETH/ETH price | Cause |
|---|---|---|
| Pre-Shanghai (2021-early 2023) | 0.95-1.01 | No withdrawal functionality; discount reflected illiquidity |
| June 2022 | ~0.94 | Three Arrows Capital collapse; forced stETH selling; Celsius Network liquidity crisis |
| Post-Shanghai (April 2023+) | 0.9995-1.0005 | Withdrawals enabled; arbitrage mechanism closes depeg rapidly |
| 2024-2026 | 0.9990-1.0010 | Tight peg with occasional small deviations during market stress |

The post-Shanghai peg is significantly tighter because the withdrawal mechanism creates an arbitrage path: when stETH trades below 1 ETH, arbitrageurs buy stETH at discount and withdraw it for ETH, capturing the spread minus the queue wait cost. This arbitrage mechanism was unavailable before April 2023, which is why pre-Shanghai depeg events were severe and persistent.

## Risk Profile: Smart Contract, Validator Concentration, Oracle, and Governance

### Smart contract risk

Lido's core contracts have been audited by Sigma Prime, Oxorio, MixBytes, Certora (formal verification), and others across multiple versions. The stETH contract, the withdrawal queue, and the oracle module are among the most audited liquid staking contracts in DeFi. No exploit has occurred in Lido's core staking contracts.

The higher smart contract risk surface is in Lido's integrations: stETH is accepted as collateral in Aave v3, Compound v3, Maker, and other protocols. An exploit affecting these integrations can drain protocol pools with stETH collateral even without a Lido contract exploit. The July 2023 Curve reentrancy exploit exposed this dynamic: protocols using Curve's stETH pool price as an oracle input were affected by an oracle manipulation that originated in Curve, not Lido.

### Validator concentration risk

Lido's node operators are a whitelisted set. This is the most frequently cited structural criticism of Lido. As of mid-2026, Lido's top five operators held approximately 30-40% of Lido's total staked ETH between them (verify against Lido's operator statistics at stake.lido.fi at publish). If these operators colluded -- or if their infrastructure were compromised simultaneously -- they could threaten Ethereum network properties.

More broadly, Lido holding 28-30% of all staked ETH means that Lido's combined operator set is approaching the 33% threshold that would allow finality delay attacks (not theft, but disruption) if coordinated. Ethereum researchers including Danny Ryan have written extensively about this risk. Lido's counterargument is that the operators are not coordinated, are contractually bound, and would have their reputations and staked capital at risk in a coordination attack. The structural concern remains unresolved regardless of whether the attack is likely.

### Oracle risk

Lido uses an oracle committee of 9 addresses to report beacon chain state to the rebase contract. The oracle quorum requirement is 5-of-9. Oracle reports determine stETH rebase rates. A compromised oracle committee that underreports rewards would reduce stETH holder yield. An oracle report that overestimates could create accounting inconsistencies. Lido's oracle architecture includes sanity checks on reported values to limit the impact of individual erroneous reports.

stETH's use as collateral in Aave and other lending protocols creates oracle exposure in those protocols: if Chainlink's stETH price feed becomes stale or provides incorrect data, lending protocol liquidations could be incorrectly triggered. This is lending protocol oracle risk, not Lido smart contract risk, but it affects stETH holders who are also Aave depositors.

### Governance risk

Lido's governance token is LDO. LDO holders vote on operator additions/removals, fee changes, protocol upgrades, and treasury allocations. LDO holder concentration is moderate: as of mid-2026, the top 10 LDO holders controlled approximately 40-50% of the supply including the Lido DAO treasury and early investor allocations (verify against Etherscan token holder data at publish). The governance process includes a governance forum, Snapshot off-chain vote, and on-chain vote with an Aragon-based contract system.

The governance risk most specific to Lido is operator management: a governance vote that adds a compromised node operator or removes important safeguards from the operator set could affect staking security. The second governance risk is fee structure: a governance vote could reallocate the current 10% fee (5% operator / 5% DAO), potentially reducing node operator incentives for careful operation.

## Comparable Protocols: Rocket Pool, Frax ETH, and Coinbase cbETH

**Rocket Pool (rETH)** uses a permissionless node operator model. Anyone can run a Rocket Pool validator by depositing 8 ETH (down from 16 ETH after the Atlas upgrade in April 2023) and providing RPL token collateral as a security bond. rETH is a non-rebasing token: its value accrues against ETH over time rather than through balance increases. rETH/ETH exchange rate grows continuously as staking rewards accumulate. Permissionless validators mean more geographic and entity diversification than Lido's whitelisted set, at the cost of variable operator quality and lower capital efficiency (operators must provide their own bond capital). Rocket Pool's total staked ETH is approximately 3-4% of total ETH staking, versus Lido's ~28-30%.

**Frax ETH (frxETH / sfrxETH)** uses a dual-token model. frxETH is a 1:1 ETH peg token with no embedded yield. sfrxETH (staked frxETH) is the yield-bearing version: depositing frxETH into the sfrxETH vault earns all staking yield from the Frax validator set. Users who hold frxETH without staking it into sfrxETH receive no yield but enable higher yield for sfrxETH holders (their ETH is still staked, the yield simply concentrates in sfrxETH). The practical effect: sfrxETH APY is typically slightly higher than stETH APY because not all frxETH holders stake into sfrxETH.

**Coinbase cbETH** is centralized custodial liquid staking. Coinbase runs validators, issues cbETH as a receipt token, and manages withdrawals through Coinbase's own processes. cbETH is simpler from a user perspective: no node operator governance, no oracle committee, no DAO. The risks are simpler too: Coinbase counterparty risk and Coinbase operational continuity. cbETH is subject to Coinbase's terms of service and regulatory status, which is a different risk category than Lido's smart contract and governance risks.

## Yield and Risk Trade-Off: What stETH Holders Earn vs. What They Put at Risk

**stETH holders earn:**
- 90% of Ethereum staking yield (consensus rewards + execution layer tips + MEV), after Lido's 10% fee
- As of mid-2026, gross staking APY on Ethereum ranged from 3-4% annualized, varying with validator set growth and block activity; stETH APY approximately 2.7-3.6% (verify at stake.lido.fi at publish)
- DeFi composability: stETH is accepted as collateral in Aave, Compound, and Maker; can earn additional yield through restaking via EigenLayer

**What stETH holders put at risk:**
- Smart contract risk: Lido staking contracts (low risk given audit depth and track record) and integration protocol risk (Aave, Curve, etc.)
- stETH secondary market depeg: most pronounced during market stress before withdrawal arbitrage resolves the depeg; post-Shanghai depeg events have been short and small
- Withdrawal queue duration risk: during mass exit scenarios, withdrawal queue wait could extend to weeks or months
- Validator slashing: Lido validator slashing is rare, insurance fund exists, but slashing events do reduce stETH supply and reduce the ETH redeemed per stETH below 1:1
- Network concentration risk: Lido's market share creates a structural risk to Ethereum; regulatory or governance pressure on Lido as a protocol is a systemic risk without a direct comparable in permissionless alternatives

The central tension: Lido's scale is both its main feature and its main risk. The same liquidity depth and DeFi composability that makes stETH the de facto liquid staking standard is a consequence of Lido holding 28-30% of staked ETH -- a concentration that creates risks for Ethereum's network health that smaller liquid staking alternatives do not create individually. Whether Lido's market share will decline through natural competitive pressure (Rocket Pool, Frax ETH, institutional alternatives) or requires active intervention by the Ethereum community is an open governance question with no resolution as of mid-2026.

---

## What we checked ourselves before writing this

For this article, we reviewed the Lido Finance documentation at docs.lido.fi, the stETH technical specification, the Lido withdrawal queue documentation, Ethereum's validator exit churn limit specification from the official consensus spec (github.com/ethereum/consensus-specs), Danny Ryan's blog posts on Ethereum staking centralization risks, the Curve stETH/ETH pool historical peg data (Dune Analytics), and the Lido oracle committee documentation. stETH market share (~28-30% of staked ETH), validator exit queue depth calculations, and node operator concentration statistics are approximate as of Q2 2026 and should be verified against Dune Analytics lido.lido.fi dashboard and Etherscan at publish time.

---

## Frequently asked questions

**How does Lido staking work?**
Users deposit ETH into Lido's staking contract and receive stETH 1:1. Lido batches the ETH into 32-ETH increments and assigns them to whitelisted professional node operators who run Ethereum validators. Staking rewards accumulate on the beacon chain; Lido's oracle committee reads those rewards daily and updates stETH balances proportionally (the rebase). stETH holders receive 90% of the staking yield; Lido takes 10% split between operators and the DAO treasury.

**How does Lido withdrawal work?**
Users request a withdrawal by burning stETH through Lido's withdrawal queue contract. They receive an NFT representing their queue position. Lido fulfills requests using the ETH buffer (newly deposited ETH not yet staked) first. When the buffer is insufficient, Lido requests validator exits from node operators. Exiting validators go through the Ethereum beacon chain exit queue. Once the ETH is processed, the NFT can be claimed for ETH. Normal withdrawal times range from hours to several days; during high-demand periods, the Ethereum exit queue can extend this to weeks.

**Has stETH ever depegged from ETH?**
Yes. The most significant depeg was in June 2022 when stETH fell to approximately 0.94 ETH during the Three Arrows Capital collapse and Celsius Network crisis, which triggered forced stETH selling. Before Ethereum's Shanghai upgrade (April 2023), there was no withdrawal mechanism, so stETH depeg could not be closed by arbitrage. Post-Shanghai, stETH has maintained a tight peg of 0.9990-1.0010 ETH because arbitrageurs buy stETH at discount and redeem it for ETH through the withdrawal queue, closing any depeg rapidly.

**What is the Lido withdrawal queue wait time?**
Under normal conditions: hours to a few days, depending on whether Lido's ETH buffer can cover the withdrawal without validator exits. Under stress conditions (mass withdrawal requests), the Ethereum beacon chain exit queue limits how many validators can exit per day; with a large validator set, full exit queue processing under stress could take weeks. This is an Ethereum protocol constraint, not specific to Lido.

**How does stETH compare to rETH?**
stETH (Lido) is a rebasing token: its quantity in your wallet grows daily as rewards accrue. It is issued by a protocol using a whitelisted operator set. rETH (Rocket Pool) is a non-rebasing token: its value versus ETH grows over time, but the quantity stays constant. It is issued by a protocol using permissionless node operators who must provide collateral bonds. rETH holders have greater operator decentralization; stETH holders have greater DeFi composability and liquidity depth. Lido is approximately 8-10x larger than Rocket Pool by staked ETH.

**What are the main risks of holding stETH?**
The main risks are: (1) Lido smart contract risk -- extensive audits and long track record, but no contract is exploit-proof; (2) stETH secondary market depeg -- typically small and short-lived post-Shanghai, but can be severe in acute market stress; (3) validator slashing -- node operators who are slashed reduce the ETH backing per stETH; Lido has a slashing insurance fund but it does not cover catastrophic events; (4) withdrawal queue duration during stress scenarios; and (5) Lido's Ethereum network centralization risk -- Lido's ~28-30% of staked ETH approaches thresholds that could affect Ethereum network properties if the operator set were coordinated adversarially.
