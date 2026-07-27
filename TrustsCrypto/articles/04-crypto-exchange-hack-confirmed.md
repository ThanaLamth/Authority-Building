---
title: "What Bybit Confirmed About the February 2025 Hack: Disclosed Amount, Affected Users, and Response"
slug: "/news/crypto-exchange-hack-confirmed"
meta_title: "Bybit Hack February 2025: What Was Confirmed, What Remains Unverified"
meta_description: "What Bybit confirmed about the February 2025 security incident: the disclosed amount, attack vector, affected accounts, and what remained unverified at time of writing."
schema: "NewsArticle"
primary_keyword: "crypto exchange hack confirmed"
last_reviewed: "2026-07-27"
---

# What Bybit Confirmed About the February 2025 Hack: Disclosed Amount, Affected Users, and Response

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "What Bybit Confirmed About the February 2025 Hack: Disclosed Amount, Affected Users, and Response",
  "description": "What Bybit confirmed about the February 2025 security incident: the disclosed amount, attack vector, affected accounts, and what remained unverified at time of writing.",
  "datePublished": "2026-07-27",
  "dateModified": "2026-07-27",
  "publisher": {
    "@type": "Organization",
    "name": "TrustsCrypto"
  }
}
```

Bybit confirmed a security incident on February 21, 2025, via a statement from CEO Ben Zhou posted on X (formerly Twitter) and subsequently on the exchange's official blog. The exchange disclosed that approximately 401,347 ETH, valued at roughly USD 1.46 billion at the time of the incident, was transferred without authorization from a cold wallet.

## What Bybit Disclosed About the Incident

Bybit's initial disclosure stated that the affected wallet was an Ethereum multisignature cold wallet managed through the Safe{Wallet} interface. The attacker manipulated the signing interface so that what appeared to Bybit's signers as a routine transaction was in fact a transaction that transferred control of the wallet to an attacker-controlled address.

The technique is described in the security research community as a "blind signing" attack: the signers approved a transaction without being able to verify its actual on-chain content because the Safe{Wallet} UI they were viewing had been compromised. The on-chain transaction the signers approved changed the smart contract logic of the multisig to transfer ownership, after which the attacker drained the wallet.

Bybit disclosed the following assets were taken:

- 401,347 ETH
- 90,376 stETH (Lido staked ETH)
- 15,000 cmETH
- 8,000 mETH

At the time of the incident, the combined value was estimated at approximately USD 1.46 to 1.5 billion, making it the largest confirmed crypto theft by disclosed dollar value at that point in time.

Blockchain analytics firms Chainalysis and TRM Labs attributed the attack to the Lazarus Group, a threat actor associated with the Democratic People's Republic of Korea (DPRK) that has been responsible for multiple prior crypto thefts, per their published analyses dated February 22, 2025.

## Why the Disclosure Timeline and Scope Matter for Affected Users

Bybit's CEO disclosed the incident publicly within hours of detection. The exchange did not pause withdrawals. Ben Zhou stated in a public post that Bybit's assets were fully backed and that client funds were not at risk because Bybit had sufficient reserves to cover the loss independently.

Safe{Wallet} (formerly Gnosis Safe) published a post-incident analysis confirming that its smart contract infrastructure had not been compromised. The attack targeted the Safe front-end interface used by Bybit's signing team, not the Safe smart contract itself.

That distinction carries operational weight for other institutional users of multisig infrastructure: the risk in this case was not a smart contract vulnerability but a compromise of the web-based signing interface. Users relying on hardware-enforced transaction display rather than a browser-based interface face a different risk profile.

## Which User Accounts and Funds Are Confirmed Affected

Bybit confirmed that only the specific cold wallet that held the Ethereum assets listed above was affected. No other wallets, no user hot wallets, and no other chains were named in the disclosure as affected.

Bybit stated that all user accounts remained fully accessible and that client withdrawal requests processed normally throughout the incident. The exchange confirmed it covered the loss from its own balance sheet and from emergency liquidity provided by other market participants including Binance and Bitget, which lent funds to cover the short-term liquidity requirement.

The specific number of users directly affected by the wallet loss was not disclosed. Because Bybit covered the loss before any user fund shortage occurred, the direct user impact was limited to the temporary uncertainty during the hours between disclosure and the first confirmation that client funds were covered.

## What Remains Unconfirmed or Under Investigation

The exact identity of the individual or individuals who compromised the Safe{Wallet} front-end has not been confirmed in a public criminal indictment or law enforcement statement at time of writing. The attribution to Lazarus Group is based on blockchain analytics methodology -- wallet clustering, transaction patterns, and mixer usage -- which is investigative evidence, not a judicial finding.

Whether any portion of the stolen funds is recoverable remained unclear at time of writing. Lazarus Group-linked funds from prior incidents, including the 2022 Ronin bridge attack, have remained largely unrecovered despite blockchain tracing. Pending confirmation: no recovery agreement or fund return had been disclosed at time of writing.

The Safe{Wallet} front-end compromise vector had not been fully documented in a public post-mortem at the time of this review. Safe published an initial analysis but had not released a full technical disclosure of how the attacker gained access to the signing interface.

## What Affected Users Should Do Now and What to Watch

Users with open positions or funds on Bybit at the time of the incident should confirm their account balance matches expected holdings. Bybit published a proof-of-reserves report following the incident to document solvency. Independent verification of that report against on-chain data is the most reliable check.

Institutional users of multisig wallets that use browser-based signing interfaces should evaluate whether their signing workflow provides transaction-level verification independent of the browser display. Hardware wallet integration with on-device transaction display is one available mitigation.

The Lazarus Group's known patterns include laundering through multiple chains and mixers in the weeks following a theft. On-chain monitoring firms continue to publish wallet cluster updates. Any official law enforcement action, asset freeze, or exchange-level blacklisting of the identified wallets would be a material update to this incident's status.

---

**Sources reviewed for this article**

- Bybit CEO Ben Zhou statement on X, February 21, 2025
- Safe{Wallet} incident analysis, February 22, 2025: https://safe.global/blog/
- Chainalysis attribution report, February 22, 2025: https://www.chainalysis.com/blog/
- TRM Labs attribution analysis: https://www.trmlabs.com/post/
- Bybit proof-of-reserves following the incident: https://www.bybit.com/