---
title: "What the Ethereum Dencun Upgrade Actually Changed: EIP Summary, Validator Impact, and What Is Still Pending"
slug: "/blockchain/ethereum-upgrade-what-changed"
meta_title: "Ethereum Dencun Upgrade Explained: EIPs, Validator Impact, and What Changed"
meta_description: "What the Ethereum Dencun upgrade activated on March 13, 2024: the included EIPs, the impact on validators and Layer 2 fees, and what was not included or remains pending."
schema: "NewsArticle"
primary_keyword: "ethereum upgrade what changed"
last_reviewed: "2026-07-27"
---

# What the Ethereum Dencun Upgrade Actually Changed: EIP Summary, Validator Impact, and What Is Still Pending

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "What the Ethereum Dencun Upgrade Actually Changed: EIP Summary, Validator Impact, and What Is Still Pending",
  "description": "What the Ethereum Dencun upgrade activated on March 13, 2024: the included EIPs, the impact on validators and Layer 2 fees, and what was not included or remains pending.",
  "datePublished": "2026-07-27",
  "dateModified": "2026-07-27",
  "publisher": {
    "@type": "Organization",
    "name": "TrustsCrypto"
  }
}
```

The Ethereum Dencun upgrade activated at epoch 269568, block 19426587, on March 13, 2024, per the Ethereum Foundation's announcement at blog.ethereum.org. Dencun combined execution layer changes (Cancun) with consensus layer changes (Deneb) and included nine Ethereum Improvement Proposals.

## What the Upgrade Activated and When

The nine EIPs activated in Dencun are:

- EIP-4844 (proto-danksharding): introduced blob-carrying transactions, a new transaction type that carries temporary binary data attached to Ethereum blocks. Blob data is held by consensus layer clients for approximately 18 days, not permanently, reducing long-term storage requirements. This is the primary EIP in Dencun.
- EIP-1153 (transient storage opcodes): added TSTORE and TLOAD opcodes, which create storage that persists only within a single transaction. Reduces gas cost for temporary storage patterns used in re-entrancy locks and flash loans.
- EIP-4788 (beacon block root in EVM): exposes the hash of the previous beacon chain block header in the EVM execution environment. Used by staking protocols and restaking infrastructure.
- EIP-5656 (MCOPY): introduced a new memory copying opcode that reduces gas cost for operations that copy data within EVM memory.
- EIP-6780 (SELFDESTRUCT): restricted the SELFDESTRUCT opcode. After Dencun, SELFDESTRUCT still transfers ETH balance but no longer deletes contract storage unless the call is in the same transaction that created the contract. Affects contracts that relied on SELFDESTRUCT for storage clearing.
- EIP-7044 (perpetually valid signed voluntary exits): changed the validity of signed voluntary exits so they remain valid across future forks. Reduces operational risk for staking pools that pre-sign exit messages.
- EIP-7045 (increase max attestation inclusion slot): extended the window within which validators can include attestations from one epoch to two epochs.
- EIP-7514 (add max epoch churn limit): capped the maximum number of validators that can join the active set per epoch at 8, to slow potential validator set growth.
- EIP-7516 (BLOBBASEFEE opcode): added an opcode allowing smart contracts to query the current blob base fee, enabling contracts to respond dynamically to blob congestion.

## Why the Included EIPs Matter for Validators, Developers, and Users

EIP-4844 is the mechanism that directly reduced Layer 2 transaction fees. Before Dencun, Layer 2 networks posted their transaction data to Ethereum as calldata, which is stored permanently and was priced accordingly. After Dencun, Layer 2 networks could post the same data as blobs, which are priced separately from calldata and expire after approximately 18 days.

The practical effect was a reduction in Layer 2 data posting costs of approximately 80-90% in the weeks following activation, per on-chain fee data from networks including Arbitrum, Optimism, and Base. That reduction translated into lower transaction fees for end users on those networks.

EIP-7514's churn limit matters for validator queue context. The Ethereum validator set had grown substantially in 2023 and early 2024. Uncapped growth at the prior rate would have lengthened activation queues to months, increased consensus overhead, and raised questions about network efficiency at very large validator counts. The cap is adjustable through governance but was set at 8 per epoch at activation.

## Which Users, Validators, and Applications Are Directly Affected

Layer 2 users are the most directly affected by the fee reduction from EIP-4844. On-chain data from Arbitrum and Optimism showed average transaction fees falling from approximately USD 0.50-2.00 per transaction to under USD 0.05 in the weeks following Dencun, based on data aggregated by L2Beat and Dune Analytics dashboards.

Staking pool operators using pre-signed voluntary exits benefit from EIP-7044. Before this change, signed exit messages could become invalid across hard forks, requiring pools to manage re-signing logistics at each upgrade. After Dencun, those messages remain valid indefinitely.

Smart contracts that relied on SELFDESTRUCT for storage clearing need review. The restricted behavior introduced by EIP-6780 changes the gas cost and functional outcome of that opcode in contracts deployed before Dencun that called SELFDESTRUCT outside of the contract creation transaction.

## What Was Not Included or Remains Under Development for Future Forks

Dencun did not include full danksharding, which would expand blob capacity significantly beyond the initial limit of three blobs per block target (six maximum) introduced in EIP-4844. Full danksharding remains under research as a multi-year roadmap item.

Ethereum Improvement Proposals related to verkle trees, which would change Ethereum's state storage structure to reduce the data needed for stateless clients, were not included in Dencun. Verkle tree migration was under active development and targeted for a subsequent upgrade.

EIP-3074 (AUTH and AUTHCALL opcodes), which was under discussion for Dencun but was ultimately excluded, was later included in the Pectra upgrade rather than Dencun. Its absence from Dencun was noted in Ethereum developer community discussions as a deliberate scope decision.

## What the Ethereum Community Should Watch in the 30 Days After Activation

Client team release notes and hotfix activity in the 30 days after March 13 are the first signal of any unforeseen issues. All major client teams -- Geth, Nethermind, Besu, Erigon, and their consensus layer counterparts -- released Dencun-compatible versions before activation. No hotfix releases were issued by major client teams in the 30 days after activation as of this review.

Blob base fee data on beaconcha.in and mempool.space provides the earliest signal of whether blob space is congested. If blob demand grows faster than the current capacity, base fees for blobs will rise and reduce the fee advantage for Layer 2 networks. That signal would indicate whether EIP-4844's parameters need adjustment in a subsequent upgrade.

Client diversity at activation per clientdiversity.org data showed Geth as the majority execution client by a margin that remained above the 33% single-client risk threshold for the consensus layer. That concentration has been a persistent area of concern in Ethereum developer community discussions predating Dencun.

---

**Sources reviewed for this article**

- Ethereum Foundation blog, Dencun upgrade announcement: https://blog.ethereum.org/2024/02/27/dencun-mainnet-announcement
- EIPs referenced: https://eips.ethereum.org (EIP-4844, EIP-1153, EIP-4788, EIP-5656, EIP-6780, EIP-7044, EIP-7045, EIP-7514, EIP-7516)
- L2Beat blob fee tracking: https://l2beat.com
- beaconcha.in epoch and client diversity data: https://beaconcha.in
- clientdiversity.org at activation: https://clientdiversity.org