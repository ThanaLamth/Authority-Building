---
title: "ChangeNOW vs DeFi Swaps 2026: CeFi Aggregator vs DEX Protocols Compared"
slug: "/ai-agents/changenow-defi-swap-mcp-2026"
meta_title: "ChangeNOW vs DeFi Swaps 2026 | CeFi Aggregator vs DEX Protocols"
meta_description: "Analytical comparison of ChangeNOW's CeFi aggregator model against DEX protocols including Li.Fi, Rango, 1inch, and Uniswap. Mechanism differences, risk profiles, and use-case boundaries explained."
primary_keyword: "changenow defi alternative"
secondary_keywords:
  - "changenow vs uniswap"
  - "changenow vs 1inch"
  - "cefi vs defi swap"
  - "changenow defi comparison"
  - "dex aggregator vs changenow"
  - "changenow smart contracts"
schema: "Article + FAQPage"
category: "ai-agents"
last_reviewed: "2026-10-14"
author: "AiCrypto Editorial Team"
internal_links:
  - "/exchanges/aggregators/changenow-review-2026"
  - "/exchanges/aggregators/how-instant-crypto-swaps-work-2026"
---

# ChangeNOW vs DeFi Swaps 2026: CeFi Aggregator vs DEX Protocols Compared

*By AiCrypto Editorial Team, Reviewed October 2026*

> **Editorial methodology**, mechanism research, protocol documentation review, on-chain verification, risk taxonomy application across custody, liquidity, oracle, and regulatory dimensions.

ChangeNOW occupies a structurally distinct category from DeFi swap protocols: it is a CeFi aggregator that routes swaps off-chain through liquidity partnerships, whereas DEX aggregators like Li.Fi, Rango Exchange, and 1inch execute swaps on-chain through smart contracts with the user retaining custody throughout. The question of which model is appropriate for a given transaction is not answered by fees alone, it involves evaluating trust assumptions, asset coverage, gas dependencies, compliance exposure, and risk profiles that differ significantly between the two models.

---

## Architectural Divergence: Off-Chain Routing vs On-Chain Execution

The most consequential difference between ChangeNOW and DEX protocols is not visible in the user interface, it is the location where the swap actually executes.

**ChangeNOW's off-chain routing model** works as follows: the user sends funds to a ChangeNOW-controlled deposit address, ChangeNOW processes the swap through its liquidity partner network (centralized exchanges, OTC desks), and delivers the output asset to the user's destination address. The swap logic, rate negotiation, and fill execution are entirely off-chain. The only on-chain events are the inbound transfer to ChangeNOW's deposit address and the outbound transfer from ChangeNOW's delivery address. There are no smart contracts involved in the swap execution itself.

**DEX aggregator on-chain execution** works differently: the user connects a self-custody wallet, signs a transaction that invokes the aggregator's smart contracts, and those contracts route the swap through one or more on-chain liquidity pools (Uniswap V3, Curve, Balancer, etc.) atomically within a single transaction or a bridged multi-step flow. The user never relinquishes custody. The trade-off is that the user must hold the network's gas token, accept smart contract execution risk, and operate within the EVM ecosystem's constraints.

This architectural difference cascades into every dimension of the comparison that follows.

---

## Comparison Table: ChangeNOW vs DEX Aggregators

| Dimension | ChangeNOW | Li.Fi | Rango Exchange | 1inch | Uniswap |
|---|---|---|---|---|---|
| **Custody during swap** | Yes (CeFi routing) | No (smart contracts) | No (smart contracts) | No (smart contracts) | No (smart contracts) |
| **BTC as input/output** | Yes | No (wrapped only) | Limited | No | No |
| **Fiat on-ramp** | Yes (60+ currencies) | No | No | No | No |
| **Gas required by user** | No | Yes (destination chain) | Yes | Yes | Yes |
| **KYC requirement** | Threshold-triggered | None (wallet-only) | None (wallet-only) | None (wallet-only) | None (wallet-only) |
| **Smart contract risk** | None (off-chain) | Yes | Yes | Yes | Yes |
| **MEV exposure** | None (off-chain) | Yes | Yes | Yes | Yes |
| **Cross-chain bridge risk** | Minimal (internal routing) | Yes (bridge contracts) | Yes (bridge contracts) | Limited | No |
| **Coins supported** | 1000+ | EVM + select chains | Multi-chain broad | EVM-focused | EVM-focused |

---

**Screenshot**
File: `../media/live-1inch-dex.png.png`
Alt text: "1inch DEX aggregator interface, on-chain swap comparison, July 2026"
Caption: "1inch DEX aggregator interface for comparison with ChangeNOW's CeFi model, captured July 2026."
![ChangeNOW swap interface](../media/live-1inch-dex.png)
*1inch DEX aggregator interface for comparison with ChangeNOW's CeFi model, captured July 2026.*

---

## We Tested It (October 2026)

ChangeNOW's homepage now advertises MCP client integration: "Let your AI agent swap crypto — works with any MCP client." This blurs the CeFi/DeFi boundary somewhat — ChangeNOW is positioning itself as infrastructure for autonomous agent-driven swaps, not just a manual swap UI.

---

## When CeFi Routing (ChangeNOW) Is the Appropriate Model

**Cross-chain swaps involving Bitcoin as input or output** represent the clearest use case for CeFi aggregators. Bitcoin is a UTXO chain with no EVM compatibility; it cannot be natively swapped through smart contract protocols without first wrapping it (WBTC, cbBTC, etc.), which introduces bridge and custody risk of its own. ChangeNOW handles BTC directly through its liquidity partner network, no wrapping required, no bridge contract to trust. For a user who needs to move native BTC to ETH or a stablecoin, ChangeNOW's routing architecture is architecturally more direct than any DEX path.

**Fiat on-ramp requirements** are another strong differentiator. ChangeNOW supports 60+ fiat currencies with card and bank transfer options. DEX aggregators are crypto-native; they have no fiat entry mechanism. A user converting EUR to USDC for the first time cannot accomplish that through 1inch or Uniswap without first acquiring crypto through a separate fiat gateway.

**Users without gas tokens** face a practical barrier when attempting to use DEX aggregators. Initiating a swap on Li.Fi or 1inch requires ETH (or the native token of whichever chain is involved) in the connected wallet. Users who hold only the asset they want to swap, and not the gas currency, cannot execute. ChangeNOW has no gas requirement on the user's side; the gas cost is embedded in the spread.

**Compliance-neutral transaction contexts** with moderate swap sizes benefit from ChangeNOW's established settlement infrastructure and Trustpilot-verified reliability (4.6/5 across 450,000+ reviews as of mid-2026), where the custody window is brief and refund mechanisms are well-documented.

---

## When DEX Aggregators Are the Appropriate Model

**Non-custodial execution requirements** make DEX aggregators the only viable option. If a user's operational mandate, risk tolerance, or institutional framework requires that funds never leave self-custody during a swap, smart contract-based execution is the necessary architecture. ChangeNOW's model involves a custody transfer by design.

**EVM-native swaps with gas available** are more cost-efficient and verifiable on-chain through DEX routes. For a swap between two ERC-20 tokens on Ethereum or an EVM-compatible L2, Li.Fi or 1inch can route the swap through the deepest on-chain liquidity with full transaction transparency, every step is verifiable on the block explorer without trusting a third party's status tracker.

**DeFi composability** is unavailable through ChangeNOW. Users who need a swap as part of a broader DeFi workflow, depositing output assets directly into a yield protocol, using a swap as a step in an automated strategy, or integrating with a DeFi front-end, must use smart contract execution. ChangeNOW delivers funds to a destination address; it cannot chain into a contract call.

**MEV sensitivity** cuts both ways. ChangeNOW's off-chain routing removes MEV exposure entirely, there is no mempool for searchers to front-run. DEX aggregators like 1inch have MEV protection features (Fusion mode, private mempools), but on-chain execution remains inherently more exposed. For large EVM swaps, the trade-off between DEX transparency and ChangeNOW's MEV-neutral routing deserves explicit evaluation.

---

## Risk Taxonomy: CeFi vs DeFi Risk Profiles

**1. Custody risk**, This is where the two models diverge most sharply. ChangeNOW users transfer custody of funds for the duration of the swap, typically 5?20 minutes for common pairs. DEX users retain custody throughout, with smart contracts acting as execution agents rather than custodians. However, smart contracts are custodians of a different kind during atomic execution: funds are locked in contract state until the transaction finalizes. The risk character differs: CeFi custody risk is counterparty and operational; DeFi custody risk is code-based and irreversible on execution failure.

**2. Liquidity risk**, ChangeNOW's floating-rate mode exposes users to slippage when liquidity partner order books are thin; fixed-rate mode transfers that risk to ChangeNOW but carries a wider spread. DEX aggregators route through on-chain pools, where slippage is a function of pool depth and trade size, visible and calculable before execution via slippage tolerance settings. Neither model eliminates liquidity risk; both make it visible in different ways.

**3. Oracle/rate risk**, ChangeNOW's rate infrastructure aggregates feeds from liquidity partners; feed failures or significant price dislocations during routing can cause rate discrepancies on fixed-rate orders, potentially triggering rate renegotiation or refund. DEX aggregators use on-chain price discovery, Uniswap's TWAP feeds, Chainlink integrations, which are subject to oracle manipulation on low-liquidity pools and sandwich attack exposure on large orders. Oracle risk exists in both models but operates through different mechanisms.

**4. Regulatory/compliance risk**, ChangeNOW applies threshold-triggered KYC and AML screening. Transactions flagged by automated compliance systems can be held pending identity verification, with funds remaining in ChangeNOW's custody during that window. DEX aggregators have no KYC layer; compliance responsibility lies with the user's jurisdiction. On-chain transparency means DEX transactions are fully auditable by blockchain analytics tools. Regulatory risk for DEX users is indirect (analytical traceability) rather than direct (operational hold by provider).

---

## When to Use vs When to Avoid

**ChangeNOW is appropriate when:**
- Native BTC, BCH, LTC, or other non-EVM assets are involved as input or output
- A fiat entry or exit is part of the transaction
- The user lacks gas tokens for on-chain execution
- A brief custody window is acceptable in exchange for routing simplicity
- Transaction size is below the likely compliance threshold

**DEX aggregators are appropriate when:**
- Full non-custodial execution is a hard requirement
- The swap involves EVM-compatible assets with available gas
- DeFi composability or programmatic integration is required
- On-chain transaction verifiability is operationally important
- Large EVM trades benefit from MEV protection mechanisms offered by protocol-native features

**Neither model is universally superior.** The appropriate choice is determined by the asset types involved, the user's custody requirements, gas availability, transaction size, and compliance context, not by a blanket preference for CeFi or DeFi.

---

## What Users Say

**Trustpilot, positive**

> "I have used changenow for years now, i'd say probably 5 years now or longer and they've never once failed me. There were times I had thought i lost my money and literally cried only for their support to remedy it and assure me I'd receive my funds even if I sent the deposit long after I created the exchange, even after it expired."
>
>, Liz, [????? Trustpilot](https://www.trustpilot.com/reviews/6a7509c452ef61e12086deef), Aug 07, 2026

> "I had a little glitch getting my btc into the window of time from River, as you know they are ridiculously paranoid, and so I needed a refund of my btc into a new and separate wallet. ChangeNow support team delivered a fairly easy and understandable refund experience, thanks team! Highly trustworthy group!"
>
>, BTC to USDC, [????? Trustpilot](https://www.trustpilot.com/reviews/6a7f5984bd2f286280aaa106), Aug 14, 2026

> "Fast, Secure, Fair rates. Has One of the best Live support I've seen in the crypto space"
>
> — Ahmad imanpour, [★★★★★ Trustpilot](https://www.trustpilot.com/review/changenow.io), Oct 13, 2026

> "I accidentally sent USDT instead of USDD on the TRON network and was worried that my funds might be lost. The exchange was completed successfully, and the support agent, Emil, quickly checked the transaction, confirmed its status, and provided the outgoing XMR transaction hash. The funds arrived safely. Clear, professional, and reassuring support—thank you!"
>
> — Yuan, [★★★★★ Trustpilot](https://www.trustpilot.com/review/changenow.io), Oct 12, 2026

**Trustpilot, critical**

> "Been trying to receive my ravencoin for a week now and no resolution, between change now and edge wallet, just $2,000 completely gone. Not here to tarnish the services but they keep sending me links saying the transaction processed but the links aren't valid and no coins show up in my wallet or on the raven block for my wallet."
>
>, Isaiah B, [????? Trustpilot](https://www.trustpilot.com/reviews/6a846192b5d778554454eedc), Aug 18, 2026

**Reddit community**

> "I simply wanted to exchange 2600 USDC for Monero, but my account was frozen. I fully cooperated with the verification process, providing KYC and proof of funds. However, this wasn't enough. The problem remains unresolved."
>
> — u/Ok-Pea-6054, [r/AskMonero](https://www.reddit.com/r/AskMonero/comments/1uatyov/changenow_holding_xmr_dont_make_this_mistake/)

> **AiCrypto Editorial — My take:** Ahmad's "one of the best live support" claim is credible — Yuan's error recovery story is exactly the kind of thing that makes CeFi operationally superior to DEX for error handling. But Ok-Pea-6054's case shows the other side: that human oversight also means human-imposed freezes with no automated path to resolution.


---

## ChangeNOW and AI Agents: MCP Client Support in 2026

ChangeNOW launched Model Context Protocol (MCP) client integration in 2026, advertised directly on its homepage as: "Let your AI agent swap crypto -- works with any MCP client." This positions ChangeNOW as infrastructure for autonomous agent-driven crypto swaps, a materially different capability from its retail swap UI.

For AI agents, ChangeNOW's architecture offers significant practical advantages over DEX protocols:

**No gas wallet management.** Executing a swap on Uniswap or 1inch requires the agent to hold and manage the destination chain's native gas token (ETH, MATIC, SOL, or equivalent), monitor gas prices, estimate gas limits, and sign transactions. This requires key management infrastructure, on-chain state monitoring, and error handling for transaction reverts. For an agent that simply needs to convert 500 USDT to BTC, this overhead is disproportionate to the task.

**Simple REST API.** ChangeNOW reduces a swap to a small number of HTTP calls: request a rate, create a swap order, receive a deposit address, poll for status. No blockchain interaction is required on the agent's side beyond delivering the deposit (which can itself be delegated to a custody or wallet service). The agent does not need to understand EVM ABI encoding, gas estimation, or transaction signing.

**Native cross-chain support.** An AI agent using DEX aggregators for a BTC-to-ETH conversion must navigate wrapping protocols, bridge contracts, and multi-step execution flows, each introducing failure modes requiring agent-side error handling. ChangeNOW handles the cross-chain routing internally; the agent provides a deposit address and a destination address.

**Audit trail.** For enterprise AI agents operating under compliance frameworks, ChangeNOW's swap records (swap IDs, timestamps, on-chain transaction hashes for both sides) provide a more structured audit trail than pseudonymous DEX interactions. Each swap creates a traceable record.

The practical limitation for AI agents: ChangeNOW's custodial model and compliance-triggered hold risk apply equally to agent-initiated swaps. For agents executing high volumes or large individual amounts, compliance trigger thresholds become a meaningful operational consideration. Agents should be designed to handle hold notifications and support interactions.

---

## Fee Model: Total Cost at Current ETH Gas Prices

ETH at $2,513 and gas at approximately 15 gwei (Ethereum mainnet, October 2026 baseline). For a $500 swap:

| Protocol | Protocol fee | User gas cost | Total effective cost | Gas token required |
|----------|-------------|---------------|---------------------|-------------------|
| ChangeNOW | ~0.5% ($2.50) | None (embedded) | ~$2.50 | No |
| 1inch (Fusion mode) | 0.3-1% ($1.50-5.00) | $3-15 ETH | ~$4.50-20 | Yes (ETH) |
| Uniswap V3 (0.3% pool) | 0.3% ($1.50) | $5-20 ETH | ~$6.50-21.50 | Yes (ETH) |
| Li.Fi cross-chain | 0.1-0.3% + bridge fee ($1-2) | $10-50 multi-chain | ~$15-55 | Yes (multiple) |

The table reveals a counter-intuitive result: for users who do not hold ETH, ChangeNOW's spread-based fee is often lower total cost than DEX alternatives. A user holding TRC20 USDT who wants to swap to BTC cannot use Uniswap at all (BTC is not EVM-native), and cannot use 1inch without first acquiring ETH for gas. ChangeNOW accepts TRC20 USDT directly with no ETH requirement.

For users who already hold ETH and are executing EVM-only swaps on L2 networks (Arbitrum, Optimism), gas costs drop to $0.10-2.00. At those gas levels, 1inch's Fusion mode can reduce total cost below ChangeNOW's spread for EVM-native pairs. The ChangeNOW cost advantage narrows but the operational simplicity advantage (no gas wallet, no contract signing) remains.

For BTC-involved swaps on any path, ChangeNOW is consistently lower total cost than any DEX route because DEX paths require wrapping BTC first (adding bridge fees and smart contract trust assumptions). No DEX supports native BTC as an input or output.

---

## Error Recovery: The CeFi Operational Advantage

One of ChangeNOW's most documented practical advantages over DEX protocols is the presence of a human support layer capable of intervening in failed or misrouted transactions.

**Wrong-network deposit recovery.** Trustpilot user Yuan (October 2026) documented accidentally sending USDT instead of USDD on the Tron network, with the exchange completing successfully after support agent Emil verified the transaction and provided the outgoing transaction hash. This type of recovery is possible because ChangeNOW's routing is off-chain: a support agent can identify that an unexpected asset arrived at a deposit address and, if the asset is supported on the platform, process the swap rather than leaving the funds permanently stranded.

ChangeNOW's documented policy covers wrong-network deposits for assets they support. If a user sends ERC20 USDT to a TRC20 deposit address and ERC20 USDT is a supported asset, ChangeNOW can recognize the deposit and process the swap at their discretion. This is not guaranteed, and response time varies, but the path to recovery exists. No DEX offers an equivalent path.

**DEX execution: irreversible by design.** On Uniswap, 1inch, or any DEX protocol, a transaction that executes on-chain is final. If a user approves a swap to the wrong address, interacts with the wrong contract, or loses funds to a contract exploit, there is no support team, no refund mechanism, and no recovery path. Smart contract execution is deterministic and immutable. This is the fundamental trade-off of non-custodial execution: you control the keys, but you also own every error.

This asymmetry makes ChangeNOW meaningfully advantageous for users with a history of wallet errors, high-value one-time transactions where confirmation of correct execution matters, or enterprise workflows where error recovery has operational value. The trade-off is explicit: ChangeNOW's error recovery capability exists because they maintain custody and control during routing. Non-custodial execution and human-recoverable errors are mutually exclusive.

---

## Cross-Chain UX: ChangeNOW vs Bridge Protocols

Cross-chain swaps represent the most practically useful swap category: moving value between different blockchain ecosystems without routing through a centralized exchange.

**ChangeNOW: single-step model.** A BTC to ETH swap on ChangeNOW is one step from the user's perspective. Send BTC to the deposit address, receive ETH at the destination address. ChangeNOW handles cross-chain routing internally through its liquidity partner network. No bridge contract interaction, no wrapped asset intermediate, no multi-step confirmation flow. Settlement is 5-15 minutes, driven primarily by Bitcoin's 10-minute block time.

**Li.Fi and Rango: multi-step bridge flows.** DEX aggregators that support cross-chain routing do so through bridge protocols (Stargate, Across, Hop, Circle CCTP, among others). A BTC to ETH swap via Li.Fi involves: wrapping BTC to WBTC via a custodial bridge, bridging WBTC to Ethereum through a bridge contract, then swapping WBTC to ETH via Uniswap or Curve. Each step involves a separate smart contract interaction, a separate confirmation window, and a separate failure mode. The bridge step alone requires 10-30 minutes for cross-chain finality, and bridge smart contract risk is not theoretical: bridge exploits have produced the largest losses in DeFi history.

**Failure risk comparison.** ChangeNOW's single-step model has one potential failure point: the provider's routing. Li.Fi's multi-step model has multiple independent failure points: the wrapping contract, the bridge contract, the DEX execution, and gas estimation on each chain involved. Each failure mode in the DEX path is independently irreversible once the step has executed on-chain.

**Cost comparison.** ChangeNOW's approximately 0.5% spread on BTC to ETH competes against Li.Fi's aggregate costs: bridge fee (0.05-0.2%), DEX pool fee (0.05-0.3%), and gas on multiple chains ($10-50 on mainnet). For mainnet cross-chain swaps involving BTC, ChangeNOW is consistently lower total cost for users without existing ETH. For L2-to-L2 EVM swaps (Arbitrum to Optimism, for example), Li.Fi's aggregated routing on low-gas chains can be cheaper and equally fast. Each model has its cost-effective zone.

---
## Frequently Asked Questions

**Is ChangeNOW a DeFi platform?**
No. ChangeNOW is a CeFi aggregator. It routes swaps through off-chain liquidity partnerships, centralized exchanges and OTC desks, rather than through smart contracts or on-chain liquidity pools. Funds pass through ChangeNOW's custody during the routing process. It does not use or interact with decentralized protocols such as Uniswap, Curve, or Aave in its execution flow.

**Can I use ChangeNOW without a crypto wallet?**
ChangeNOW does not require a connected wallet in the same sense that DEX aggregators do. Users provide a destination address, which can be any valid address on the output chain, including an exchange deposit address, and send funds to ChangeNOW's deposit address. No wallet software needs to connect to ChangeNOW's interface directly. For fiat-to-crypto flows, only a destination crypto address is required.

**Which typically has lower fees, ChangeNOW or Uniswap?**
The comparison depends on network conditions and asset pair. ChangeNOW embeds its fee in the exchange spread, with no separate gas cost to the user. Uniswap charges a pool fee (0.05%?1% depending on pool tier) plus Ethereum gas, which can range from negligible on L2s to significant during mainnet congestion. For BTC-involved swaps, ChangeNOW is frequently more cost-effective than any DEX path because DEX paths require wrapping BTC first, adding bridge fees and smart contract risk. For EVM stablecoin swaps on L2 networks, Uniswap or 1inch can be cheaper. Neither model is categorically lower cost.

**Does ChangeNOW use smart contracts?**
ChangeNOW's core swap execution does not rely on smart contracts. The swap is processed off-chain through ChangeNOW's liquidity network. On-chain activity consists of standard value-transfer transactions to and from addresses, not contract invocations. ChangeNOW does offer an API for third-party integrations, and some integrating platforms may wrap ChangeNOW's API calls within their own smart contract workflows, but that is architecture added by the integrator, not by ChangeNOW's core protocol.



**Is ChangeNOW a DeFi platform or a CeFi platform?**
ChangeNOW is a CeFi (centralized finance) platform. It routes swaps off-chain through its liquidity partner network, which includes centralized exchanges and OTC desks. Funds pass through ChangeNOW's custody during the swap. ChangeNOW does not interact with decentralized protocols like Uniswap, Curve, or Aave in its core execution flow, and swap execution does not involve smart contracts.

**Can AI agents use ChangeNOW to execute crypto swaps automatically?**
Yes. ChangeNOW launched MCP client support in 2026, allowing AI agents to initiate and monitor swaps through a standard API without managing gas wallets or signing blockchain transactions. The agent provides a deposit amount, input asset, output asset, and destination address; ChangeNOW handles all routing. This makes ChangeNOW significantly simpler to integrate for AI agents than DEX protocols, which require key management, gas token holdings, ABI encoding, and on-chain transaction monitoring.

**ChangeNOW vs 1inch: which is the better choice?**
The better choice depends on the assets and context. ChangeNOW is more appropriate for: BTC or other non-EVM assets as input or output, users without ETH for gas, cross-chain swaps originating from non-EVM chains, situations where error recovery matters, and AI agent integrations. 1inch is more appropriate for: EVM-native swaps where the user already holds ETH, L2 swaps with low gas costs, and non-custodial execution requirements. On Ethereum mainnet at current gas prices, ChangeNOW's total cost is often lower for users who do not hold ETH gas, because 1inch requires ETH that ChangeNOW does not.

**Is CeFi or DeFi safer for crypto swaps?**
Neither is universally safer. CeFi (ChangeNOW model) carries counterparty risk during the custody window, compliance hold risk on certain asset routes, and operational dependency on the provider. DeFi carries smart contract code risk, bridge hack risk, MEV exposure in public mempools, and full irreversibility on execution errors. CeFi provides human recovery paths for user errors; DeFi does not. For standard retail swaps at moderate amounts on established pairs, CeFi's documented error recovery and operational reliability have been practical advantages. For users requiring non-custodial guarantees or DeFi-native composability, DEX protocols are the necessary architecture.

**Does ChangeNOW use smart contracts to execute swaps?**
No. ChangeNOW's core swap execution is off-chain and does not involve smart contracts. The on-chain footprint consists of standard asset transfer transactions to and from ChangeNOW's addresses. Users interacting with ChangeNOW's interface do not sign smart contract transactions or interact with protocol contracts. Third-party developers who integrate ChangeNOW's API into their own smart contract systems may add a contract layer on top of the API calls, but that is external architecture added by the integrator, not part of ChangeNOW's own execution model.
