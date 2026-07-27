---
title: "Uniswap v4 Hooks and Liquidity Pools Explained"
slug: "/protocols/dex/uniswap-v4-hooks-liquidity-pools"
meta_title: "Uniswap v4 Hooks and Liquidity Pools: Mechanism, Risk, and What Changes"
meta_description: "How Uniswap v4 hooks work, when they fire, what they can modify, and what the 2025 hook exploits confirm about the risk profile for LPs in the singleton architecture."
search_intent: "Informational"
primary_keyword: "uniswap v4 liquidity pools explained"
secondary_keywords:
  - "uniswap v4 hooks explained"
  - "uniswap v4 vs v3"
  - "uniswap v4 singleton architecture"
  - "uniswap v4 hook risk"
  - "concentrated liquidity v4"
category: "protocols/dex"
last_reviewed: "2026-07-27"
schema:
  - "Article"
  - "FAQPage"
  - "BreadcrumbList"
internal_links:
  - "/protocols/lending/aave-v3-borrowing-rates-explained"
  - "/yield/farming/impermanent-loss-explained"
  - "/risk/exploits/defi-bridge-risk-explained"
---

# Uniswap v4 Hooks and Liquidity Pools: Mechanism, Risk, and What Changes

Uniswap v4 launched on Ethereum mainnet on January 30, 2025, alongside nine other chains simultaneously, after nine independent audits, a $2.35 million security competition with 500+ researchers, and a $15.5 million bug bounty -- the largest in DeFi history at launch. The core architectural changes are two: a singleton PoolManager contract that replaces the per-pool factory model, and a hook framework that lets external contracts execute logic at ten defined points in the swap and liquidity lifecycle.

The PoolManager has operated without a critical exploit since launch. Hook contracts have not. Cork Protocol lost $11 million in May 2025 because a `beforeSwap` hook function was missing a single access control modifier. Bunni -- the largest LP optimization hook on v4 at the time -- lost $8.4 million in September 2025 through a rounding flaw in its liquidity distribution logic, despite audits from Trail of Bits and Cyfrin. That distinction between protocol risk and hook risk is now documented in real loss data, not theory.

For LPs, the mechanism understanding that matters most is this: which risks live in the PoolManager and which risks live in the hook contract, and how to tell which category a given pool falls into.

| Component | v3 | v4 | Change |
|---|---|---|---|
| Pool deployment | One contract per pool | Singleton PoolManager | Pool creation cost reduced by 99.99% |
| Hook framework | None | 10 callback points | Custom logic at swap and liquidity lifecycle |
| Accounting model | Per-swap settlement | Flash accounting (net settlement) | Reduces intermediate token transfers |
| Fee tiers | Fixed (0.01%, 0.05%, 0.3%, 1%) | Configurable per pool | More granularity, more liquidity fragmentation |
| Liquidity model | Concentrated, tick-based | Same as v3 | No change to LP position mechanics |
| Protocol fee governance | Factory-level | PoolManager + hook governance | Expanded; February 2026 DAO voted 10% fee on high-volume pools |

## What Uniswap v4 Changes Relative to v3

In v3, the factory pattern deployed a new contract for every (token0, token1, fee) combination. Pool creation cost meaningful gas, and all pool state lived in separate contracts. v4 replaces this with a single PoolManager contract holding all pool state. Pool creation becomes a state write rather than a deployment. Uniswap Labs reported 99.99% reduction in pool creation cost; Business Wire's launch announcement confirmed the same figure.

Flash accounting reduces per-swap gas further. The PoolManager tracks net token balances across an entire transaction and requires one settlement at the end, not one per swap leg. A three-hop trade settles as one net transfer per token, not three, which changes the cost model for arbitrage and multi-pool routing meaningfully.

By mid-2026, v4 had settled approximately $355 billion in cumulative volume -- roughly $190 billion on Ethereum mainnet and $70 billion on Unichain -- across 15+ networks including Base, Arbitrum, BNB Chain, and Polygon. Adoption was gradual: most liquidity stayed in v3 through early 2025, with v4 gaining share as routing integrations from 1inch, CoW Swap, Paraswap, and Matcha indexed hook-enabled pools through mid-2025.

## How Hooks Work: When They Fire and What They Can Modify

Hooks are external contracts assigned to a pool at initialization. The assignment is permanent: hooks cannot be changed after a pool is created. The PoolManager calls hook callbacks at ten defined points by reading permission bits encoded in the hook contract address -- a design that makes which callbacks are active visible on-chain without reading the hook's logic.

| Callback | Fires | What it can modify |
|---|---|---|
| BeforeInitialize | Before pool creation | Can revert to block pool creation |
| AfterInitialize | After pool creation | Read-only by convention |
| BeforeAddLiquidity | Before LP deposits liquidity | Can modify amounts or revert |
| AfterAddLiquidity | After LP deposits | Can modify delta returned to LP |
| BeforeRemoveLiquidity | Before LP withdraws | Can modify amounts or revert |
| AfterRemoveLiquidity | After LP withdraws | Can modify delta returned to LP |
| BeforeSwap | Before swap execution | Can modify swap params or override fee |
| AfterSwap | After swap execution | Can modify swap delta |
| BeforeDonate | Before donate call | Can revert or redirect |
| AfterDonate | After donate call | Read access to final state |

`BeforeSwap` and the two liquidity callbacks carry the highest LP exposure. A hook with `BeforeSwap` access can override the pool fee, reject swaps, or redirect fee flow within the same transaction. A hook with `BeforeAddLiquidity` or `AfterAddLiquidity` access can modify or redirect funds during LP deposit. The Bunni exploit exploited custom accounting in the liquidity callbacks, not the swap path -- a rounding flaw in how liquidity distribution across ticks was calculated that allowed free swaps: zero input tokens in, non-zero output tokens out.

## Concentrated Liquidity in v4: What Carries Over From v3

The tick-based concentrated liquidity model from v3 is unchanged. LPs select a price range by setting lower and upper tick boundaries; liquidity is active only when the current price is inside that range; out-of-range positions earn no fees.

v4 removes the fixed fee tier restriction. v3 allowed only 0.01%, 0.05%, 0.30%, and 1.00%. v4 allows any fee value at pool initialization, and hooks can dynamically adjust fees via `BeforeSwap`. The practical consequence is liquidity fragmentation: the same token pair can now exist across many fee tier and hook combinations, splitting depth across configurations rather than concentrating it in four standard tiers.

For LP position mechanics, v4 does not fix the impermanent loss problem from v3. Concentrated liquidity amplifies IL relative to full-range positions; the tighter the range, the more IL is realized when price moves out of range. Some hook contracts implement auto-rebalancing to reduce range-exit frequency, but auto-rebalancing hooks must execute trades, which exposes LPs to slippage and adds hook dependency risk to the IL mitigation benefit. See the [impermanent loss explainer](/yield/farming/impermanent-loss-explained) for the IL calculation framework.

## Risk Profile: Smart Contract, Hook Dependency, Liquidity, and Governance

### Smart contract risk

The PoolManager is the singleton that holds all pool accounting. A critical vulnerability in it would expose all pools simultaneously -- a higher blast radius than v3's per-pool design. The mitigation is a more concentrated, and thus more thoroughly audited, codebase: nine independent audit firms, a $2.35M security competition, and a $15.5M bug bounty pre-launch. As of July 2026, the PoolManager has not been exploited.

### Hook dependency risk

This is the risk category that 2025 confirmed with real loss data.

**Cork Protocol, May 2025, $11 million.** Cork used a Uniswap v4 hook to build stablecoin depeg hedging markets. The `beforeSwap` function in their hook lacked an access control modifier, which allowed an attacker to call it directly, bypassing the intended sequencing. A single missing modifier in a hook function -- not a flaw in the PoolManager -- was the entire exploit path. Auditors had reviewed the code, but the specific access pattern was not caught before the exploit.

**Bunni, September 2, 2025, $8.4 million.** Bunni was the largest LP optimization hook on v4 at the time of the exploit. The flaw was a rounding error in its liquidity distribution accounting logic -- Trail of Bits identified related dust accumulation issues in their audit (TOB-BUNNI-15 through 18), but the exploitable rounding path in the production version led to free swaps. The Bunni team shut the protocol down in October 2025 and open-sourced the contracts. The key post-mortem sentence from datawallet.com's post-exploit analysis applies: "the v4 core has operated without incident since launch, and the exploit touched Bunni's own contracts rather than the PoolManager."

**z0r0z V4 Router, March 2026, $42,000.** Smaller but mechanically different: inline assembly in the router trusted a fixed calldata offset rather than validating it, which an attacker exploited. A router, not a hook, but the same principle: code outside the audited PoolManager core is the risk surface.

The pattern across all three: the PoolManager is safe; the surrounding ecosystem is not. Each hook is an independent trust domain, and the security of a pool is bounded by its least-audited attached contract. As Cyfrin put it in their v4 hooks security deep dive: "The complexity of hook security audits is no longer about reviewing a single codebase, but about auditing a complete sub-protocol."

### Liquidity risk

Out-of-range positions earn no fees, identical to v3. Fee tier fragmentation can thin depth in any single pool configuration. Auto-rebalancing hooks can reduce out-of-range time but add hook dependency. Hooks with custom accounting -- the type Bunni used -- override the concentrated liquidity model itself, which increases arithmetic bug surface significantly.

### Governance risk

The PoolManager governance is UNI token-based, with the standard Uniswap multi-stage process: temperature check on forum, Snapshot off-chain vote, on-chain vote with a two-day timelock. In February 2026, the DAO voted to enable a 10% protocol fee on a subset of high-volume v4 pools, with proceeds flowing to UNI stakers through a new staking module. The timelock is the main governance protection against execution attacks.

Hook contracts have their own governance -- or none. A hook can be ownerless and immutable, or it can have an upgradeable proxy with a multisig owner that one team controls. There is no registry of hook governance models. LPs in hook-enabled pools must inspect the hook contract's ownership and upgrade architecture individually.

## Comparable Protocols: How v4 Differs From Curve v2, Balancer v3, and Ambient

**Curve v2** uses an internal AMM with a price oracle embedded in the invariant itself. It targets volatile token pairs with a different mathematical model than Uniswap's constant-product base. Curve has no external hook framework. This makes it simpler to audit and carries no hook dependency risk, but it also lacks the programmability v4 offers. Curve's concentrated liquidity equivalent is harder to reason about because the dynamic pegging adjusts the effective price range automatically.

**Balancer v3** is vault-based -- all token balances live in one Vault contract, architecturally similar to v4's singleton design. Balancer v3 has a hook concept but constrains what hooks can do: pools must implement defined interfaces rather than open callbacks, and they must be registered with the vault before use. The Balancer approach reduces hook exploitability at the cost of flexibility. A Balancer hook cannot freely modify the delta returned to an LP in the way a Uniswap v4 hook can.

**Ambient (formerly CrocSwap)** uses a unified liquidity design -- one contract, multiple pool types (concentrated, full-range, knockout), no external hook framework. Ambient eliminates hook dependency risk entirely at the cost of programmability. It is the cleanest gas-optimized deployment for teams that do not need custom logic.

The differentiation as of mid-2026: v4 is the most extensible and carries the most hook-specific risk. Curve v2 is appropriate for volatile-pair liquidity without external callback dependency. Ambient is the cleanest for deployments that need gas efficiency without custom logic. Balancer v3 is the middle ground -- more extensible than Curve, more constrained than Uniswap v4.

## Yield and Risk Trade-Off: What LPs Gain and What They Take On

The risk-adjusted LP case in v4 differs by pool type, not by the protocol as a whole.

**No-hook pools (zero hook address):** LP risk is limited to PoolManager smart contract risk and the standard concentrated liquidity dynamics -- impermanent loss, out-of-range fee cutoff, fee tier fragmentation. No hook dependency risk. The PoolManager's security record since January 2025 supports this risk profile being lower than v3's per-pool attack surface.

**Hook-enabled pools with audited hooks:** The additional risk is the hook contract itself. An audit is a necessary condition but not a sufficient one -- Cork and Bunni were both audited, and both were exploited. The relevant question is whether the hook has been running on mainnet long enough to have survived a range of economic conditions, whether its code has been reviewed by multiple independent teams, and whether the team behind it has a public track record and can act on emergency bugs.

**Hook-enabled pools with unaudited hooks:** The risk profile is unbounded. A hook with `BeforeAddLiquidity`, `AfterAddLiquidity`, or `BeforeSwap` access and no audit is an open LP exposure. The 2,500+ hook-enabled pools created by mid-2025 included many experimental deployments. Not all were audited.

The updated tension carry from 2026: the question is no longer whether a hook exploit will happen -- it has happened three times in the first 18 months after launch. The question is whether the LP premium from hook-enabled strategies justifies the additional trust assumptions, given that even audited hooks have been exploited. The PoolManager itself represents what a well-audited singleton design looks like. Hook contracts represent the long tail of DeFi risk that has always characterized the permissionless space, now attached to Uniswap's liquidity base.

---

## What we checked ourselves before writing this

For this article, we reviewed the [Uniswap v4 core whitepaper](https://github.com/Uniswap/v4-core/blob/main/docs/whitepaper-v4.pdf), the official Uniswap v4 hook documentation at docs.uniswap.org, Uniswap Labs' launch announcement via Business Wire (January 29, 2025), the Cyfrin v4 hooks security deep dive (November 2025), the datawallet.com post-launch analysis covering the Bunni exploit (June 2026), and the KuCoin security review of hook attack vectors (June 2026) covering the Cork Protocol post-mortem.

We did not run LP positions on v4 pools or execute real transactions against hook contracts. All exploit figures ($11M Cork, $8.4M Bunni, $42K z0r0z) are sourced from post-mortems and security research published after the events. Cumulative volume data ($355B as of June 2026) is sourced from the datawallet.com analysis citing DefiLlama. These figures should be verified against live DefiLlama data at publish time, as they change continuously.

---

## Frequently asked questions

**What is the main difference between Uniswap v3 and v4?**
Uniswap v4 replaces the per-pool factory architecture with a singleton PoolManager contract and adds a hook framework with ten lifecycle callbacks for external contracts. v3 deployed one contract per pool. v4 holds all pool state in one contract, uses flash accounting for net settlement, allows configurable fee tiers, and supports hook logic at defined points in each swap, liquidity deposit, and withdrawal.

**Has Uniswap v4 been exploited?**
The PoolManager has not been exploited. Hook contracts built on top of v4 have been exploited three times in the first 18 months: Cork Protocol lost $11 million in May 2025 (missing access control modifier), Bunni lost $8.4 million in September 2025 (rounding flaw in liquidity accounting), and the z0r0z V4 Router lost $42,000 in March 2026 (calldata validation error). The distinction between PoolManager risk and hook risk is the core LP security question in v4.

**Can a Uniswap v4 hook steal LP funds?**
Yes, structurally. A hook with `BeforeAddLiquidity`, `AfterAddLiquidity`, or liquidity accounting access can modify or redirect LP fund flows. Bunni's exploit demonstrated this path: a rounding flaw in custom liquidity accounting allowed zero-input swaps that drained LP value. The protocol does not enforce audit requirements on hooks. LPs in hook-enabled pools must evaluate the hook contract, its audit history, and its governance independently.

**Does Uniswap v4 change how impermanent loss works?**
No. v4 uses the same tick-based concentrated liquidity model as v3. Out-of-range positions earn no fees. Impermanent loss dynamics are identical for equivalent position configurations. Some hook contracts implement auto-rebalancing, which can reduce out-of-range frequency but adds hook dependency risk and introduces slippage costs during rebalancing.

**What is flash accounting in Uniswap v4?**
Flash accounting means the PoolManager tracks net token balances across all operations in a single transaction and requires net settlement once at the end. In v3, each swap triggered individual token transfers. In v4, a series of swaps across multiple pools settles as one net transfer per token, which reduces ERC-20 transfer calls and the associated gas. A transaction is only valid if the PoolManager owes nothing and is owed nothing at the end.

**Which Uniswap v4 pools are the safest for LPs?**
Pools with a zero hook address carry no hook dependency risk. LP exposure is limited to PoolManager smart contract risk and concentrated liquidity dynamics. These pools benefit from v4's gas efficiency and configurable fees without requiring evaluation of any external hook contract. Among hook-enabled pools, the safest are those with audited hooks from identifiable teams, long mainnet track records, and simple hook logic -- the more callbacks a hook uses and the more external contracts it calls, the larger its attack surface.

**What changed in Uniswap v4 governance in 2026?**
In February 2026, the Uniswap DAO voted to enable a 10% protocol fee on a subset of high-volume v4 pools, with proceeds flowing to UNI stakers through a new staking module. The vote converted UNI from a pure governance token into a yield-bearing asset. The two-day timelock on governance execution remains in place as a defense against governance attacks. Hook contracts may have their own governance structures, which are separate from and independent of Uniswap's on-chain governance.
