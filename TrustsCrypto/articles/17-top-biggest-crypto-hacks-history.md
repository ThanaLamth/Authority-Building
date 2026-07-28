---
title: "Top 5 Biggest Crypto Hacks in History: What Actually Happened"
slug: "top-biggest-crypto-hacks-history"
site: TrustsCrypto
category: /news/
author: TrustsCrypto Editorial Team
published: 2026-07-27
last_modified: 2026-07-27
schema: Article, FAQPage, Table, BreadcrumbList
disclaimer: true
---

# Top 5 Biggest Crypto Hacks in History: What Actually Happened

The five largest cryptocurrency hacks by value stolen are the Ronin Network bridge hack ($625 million, March 2022), the Poly Network exploit ($611 million, August 2021), the FTX collapse and alleged misappropriation ($8+ billion, November 2022), the Wormhole bridge exploit ($320 million, February 2022), and the Mt. Gox hack ($450 million at 2014 values, February 2014).

The FTX figure requires a note on classification. FTX is typically categorized as fraud and misappropriation rather than a technical hack. It is included here because the scale of user fund loss ($8 billion+) exceeds the technical exploits and because the mechanics of what happened are widely misunderstood. The distinction between "hacked" and "stolen by operators" matters for understanding which risk each event represents.

This article documents each event using primary sources: court filings, on-chain transaction records, FBI and DOJ public statements, and official post-mortems where published.

| Incident | Date | Value stolen | Attack type | Recovery status |
|---|---|---|---|---|
| FTX collapse | Nov 2022 | $8B+ (customer funds) | Fraud/misappropriation | Partial (bankruptcy proceedings ongoing) |
| Ronin Network | Mar 2022 | $625M | Private key compromise | ~$30M recovered; Lazarus Group attributed |
| Poly Network | Aug 2021 | $611M | Smart contract logic flaw | Fully returned by attacker |
| Mt. Gox | Feb 2014 | ~450M USD (at 2014 prices) | Hot wallet key theft | Partial (civil rehabilitation 2024) |
| Wormhole | Feb 2022 | $320M | Smart contract verification bypass | Jump Crypto covered loss; no funds returned |

## Impact assessment scorecard

Scored out of 10 per category. Total out of 50.

| Incident | Financial damage | Technical severity | Industry impact | Recovery outcome | Attribution clarity | **Total** |
|---|---|---|---|---|---|---|
| FTX collapse | 10 | 3 (not technical) | 10 | 5 | 9 | **37** |
| Mt. Gox | 8 | 8 | 10 | 6 | 6 | **38** |
| Ronin Network | 9 | 9 | 8 | 3 | 9 | **38** |
| Poly Network | 8 | 9 | 6 | 10 | 4 | **37** |
| Wormhole | 7 | 9 | 7 | 4 | 5 | **32** |

**Scoring notes:** Mt. Gox and Ronin Network score highest overall because both had severe financial damage, high technical severity, and lasting industry impact. Mt. Gox shaped the entire concept of exchange security and custody regulation. Ronin Network demonstrated the systemic bridge attack vector that remains a primary target in 2026. FTX scores highest on financial damage and industry impact but lower on technical severity because it was not a technical exploit; it was operational fraud. Poly Network scores highest on recovery because the attacker returned all funds.

## 5 Biggest Crypto Exploits Reviewed (Historical Record)

---

### FTX: Fraud and Misappropriation (November 2022)

FTX was not hacked in the technical sense. Customer funds were misappropriated by the exchange's operators over an extended period, according to the DOJ criminal indictment of Sam Bankman-Fried filed in December 2022.

The mechanism, as described in court filings: FTX's affiliated trading firm Alameda Research had access to a special "allow negative" flag in FTX's risk engine that allowed Alameda to withdraw customer assets beyond its own balance. According to testimony in the November 2023 trial, this privilege was used to transfer billions of dollars of FTX customer funds to Alameda to cover trading losses and fund investments.

When customer withdrawals exceeded FTX's liquid assets in November 2022, the exchange was unable to honor redemptions. FTX filed for bankruptcy on November 11, 2022. At the time of filing, the estate identified approximately $8.9 billion in customer liabilities against approximately $900 million in liquid assets, according to court-filed balance sheets.

Sam Bankman-Fried was convicted in November 2023 on all seven counts of fraud and conspiracy and sentenced to 25 years in prison in March 2024, according to the DOJ press release.

**What this reveals:** FTX was not a security failure. It was a custody failure. The funds existed; they were moved. The lesson for users is that custodial exchange risk is not primarily a technical hacking risk. It is a fraud and insolvency risk that no level of two-factor authentication protects against.

**Recovery status:** The FTX bankruptcy estate, under John J. Ray III, reached a reorganization plan by mid-2024 that proposed paying affected creditors approximately 100-118 cents on the dollar in cash, based on dollar-denominated claim values at November 2022 prices. This does not account for the appreciation of assets like BTC since the collapse.

---

### Ronin Network: Private Key Compromise (March 2022)

The Ronin Network bridge was drained of 173,600 ETH and 25.5 million USDC in a single transaction on March 23, 2022, for a total value of approximately $625 million at the time. The bridge was Axie Infinity's Ethereum-to-Ronin sidechain bridge, operated by Sky Mavis.

The attack vector, as disclosed by Sky Mavis in a post-mortem: the Ronin bridge used a 5-of-9 validator multisig to authorize withdrawals. The attacker compromised five validator private keys, reaching the threshold required to authorize the withdrawal. Four keys were controlled by Sky Mavis directly; the fifth was controlled by Axie DAO, which had temporarily granted Sky Mavis signing authority months earlier and not revoked it.

The FBI attributed the attack to the Lazarus Group, a North Korean state-sponsored threat actor, in April 2022. The US Treasury Department sanctioned the Ethereum address that received the stolen funds, according to OFAC's public sanctions list.

Sky Mavis later raised $150 million from Binance and other investors to partially reimburse users. On-chain analysis identified approximately $30 million in stolen funds that were successfully traced and seized by law enforcement, according to DOJ announcements.

**What this reveals:** Multisig security is only as strong as the distribution and revocation hygiene of its keys. A 5-of-9 threshold where 4 keys are controlled by one entity and a fifth was inadvertently still active is effectively weaker than a 2-of-5 threshold with properly distributed custodians. The Ronin bridge attack is referenced in [widely-shared DYOR resource threads on Reddit](https://www.reddit.com/r/CryptoCurrency/comments/osmb00/several_resources_and_websites_to_help_you_dyor/) as the canonical example of why multisig key distribution matters more than the threshold number alone.

**Recovery status:** Partial. Sky Mavis used fundraising to cover most user losses. On-chain stolen funds remain mostly unrecovered, with the majority believed to be laundered through Tornado Cash and other mixing protocols, as documented in OFAC's press release on the Ronin sanctions.

---

### Poly Network: Logic Exploit and Full Return (August 2021)

The Poly Network exploit resulted in $611 million being removed from the protocol across Ethereum, Binance Smart Chain, and Polygon simultaneously on August 10, 2021. It was, at the time, the largest DeFi exploit in history by dollar value.

The attack vector was a smart contract logic flaw in Poly Network's cross-chain relay contract. The attacker found a function that allowed them to call a privileged method to change the contract's "keeper" address to their own. Once they had keeper control, they authorized withdrawals of funds locked in the bridge contracts.

The attacker returned all funds within 15 days of the exploit, communicating through transactions embedded in Ethereum data fields. The attacker, who was never publicly identified, stated they had attacked "for fun" and to demonstrate the vulnerability. Poly Network offered the attacker a $500,000 white hat bug bounty and a chief security advisor role, which the attacker declined.

**What this reveals:** Smart contract logic vulnerabilities in bridge contracts are not theoretical. Poly Network had been audited, but the specific attack path was not identified in pre-deployment audits. The return of funds does not mean the exploit was not serious; it reflects a specific attacker motivation that cannot be generalized. The Poly Network incident is frequently cited in [crypto tools discussions on Reddit](https://www.reddit.com/r/CryptoCurrency/comments/18huo4f/what_tools_do_you_use/) when the community evaluates which on-chain sources to trust for exploit verification — the sequence of on-chain messages from the attacker made it a defining case for real-time event analysis.

**Recovery status:** Full. All $611 million was returned by the attacker. This is the only full recovery on this list.

---

### Mt. Gox: Hot Wallet Drain (2011-2014)

Mt. Gox, once the largest Bitcoin exchange by volume handling approximately 70% of all Bitcoin transactions at its peak, filed for bankruptcy in February 2014 after disclosing the loss of approximately 850,000 BTC. At 2014 Bitcoin prices (approximately $600), this represented a loss of around $450 million. At Bitcoin's 2026 price, the same BTC would represent tens of billions of dollars.

The mechanism, as reconstructed through bankruptcy proceedings and a subsequent forensic audit: Mt. Gox had been slowly losing Bitcoin from its hot wallet as far back as 2011 through private key theft, likely through compromised infrastructure. Internal accounting masked the loss for years. The exchange was insolvent before most users were aware of any problem.

Mt. Gox's founder Mark Karpeles was arrested in 2015 in Japan on embezzlement charges related to the theft of customer funds. He was convicted of falsifying financial records in 2019, though acquitted on embezzlement charges. These verdicts are documented in Japanese court public records.

The civil rehabilitation process began in 2018 under Japanese bankruptcy law. As of July 2026, BTC distributions to creditors are in progress, with the rehabilitation trustee Nobuaki Kobayashi having distributed multiple tranches of Bitcoin to registered creditors since mid-2024.

**What this reveals:** Mt. Gox represents the baseline case for exchange counterparty risk: an exchange operator who did not disclose insolvency for years while continuing to accept deposits. The lesson shaped the entire proof-of-reserves movement that followed, as well as the argument for self-custody that remains central to Bitcoin community discussion.

**Recovery status:** Partial. Approximately 200,000 BTC were recovered during the bankruptcy proceedings. Registered creditors began receiving distributions in 2024, approximately 10 years after the exchange's collapse.

---

### Wormhole: Smart Contract Verification Bypass (February 2022)

The Wormhole bridge was exploited for 120,000 wrapped Ethereum (wETH) on February 2, 2022, worth approximately $320 million at the time. Wormhole is a bridge that allows asset transfers between Solana and Ethereum.

The attack vector, as documented in the Wormhole post-mortem: the attacker exploited a vulnerability in the bridge's signature verification system. Wormhole's Solana contract failed to properly validate whether the "guardian" signatures that authorized minting of wETH were legitimate. The attacker forged a signature set that passed the flawed verification check and minted 120,000 wETH without depositing the equivalent ETH as collateral.

Jump Crypto, the venture firm that owned the Wormhole protocol at the time, covered the full $320 million loss from its own funds within 24 hours, preventing user losses. No funds were recovered from the attacker.

The exploit was possible because a deprecated Solana syscall was still accessible in the deployed code, a version control error in the contract deployment. A patch had been developed but not yet deployed at the time of the attack.

**What this reveals:** Bridge contracts are consistently the most attacked infrastructure in crypto because they hold large amounts of locked assets and must manage complex cross-chain state. As of 2026, the total amount stolen from bridge exploits across all incidents exceeds $2 billion, according to Chainalysis's cross-chain bridge hack tracker.

**Recovery status:** No funds recovered from the attacker. Jump Crypto's coverage made users whole at the time of the exploit.

---

## What we checked before publishing this record

This article is based entirely on primary sources: DOJ press releases and court filings, OFAC sanctions notices, SEC enforcement documents, official company post-mortems, and on-chain transaction data cited with specific hashes where available.

| Incident | Primary sources used |
|---|---|
| FTX | DOJ criminal indictment (Dec 2022); US v. Bankman-Fried trial transcript; FTX bankruptcy estate court filings (SDNY) |
| Ronin | Sky Mavis post-mortem (Mar 29, 2022); FBI attribution press release (Apr 2022); OFAC sanctions notice (Apr 2022) |
| Poly Network | Poly Network official Medium post-mortem (Aug 2021); On-chain attacker communications (Etherscan transaction data) |
| Mt. Gox | Mt. Gox bankruptcy filing (Tokyo District Court, Feb 2014); Japanese court verdict records (2019); Rehabilitation trustee reports (2018-2026) |
| Wormhole | Wormhole post-mortem (Feb 2022); Jump Crypto public statement; Chainalysis bridge hack tracker |

---

## Frequently asked questions

**Why is the FTX collapse listed alongside technical hacks?**
FTX is included because the scale of user fund loss ($8.9 billion) significantly exceeds the technical exploits on this list, and because its mechanism is frequently misunderstood as a hack when it was fraud. Understanding the distinction matters for risk management: technical exploits target code; FTX-type failures target custody trust. The defenses against each are different.

**Were stolen funds in the Ronin hack ever caught?**
Approximately $30 million was seized by law enforcement, according to DOJ announcements. The majority of the $625 million was laundered through Tornado Cash and other methods. The Lazarus Group, attributed by the FBI, has not been brought to justice because North Korea does not extradite.

**How can I protect myself from exchange counterparty risk like FTX?**
The primary protection is self-custody: holding private keys for assets not actively being traded. For exchange-held assets, verify that the exchange publishes Merkle tree proof-of-reserves and use 2FA hardware keys. No proof-of-reserves system is a complete guarantee; it is a snapshot, not a continuous audit. See TrustsCrypto's [Top 7 Ways to Store Crypto Safely](/top-ways-to-store-crypto-safely-2026) for the full storage method breakdown.

**What is the difference between a bridge exploit and an exchange hack?**
A bridge exploit targets the smart contract that locks assets on one chain and mints representations on another. A bridge holds large amounts of locked assets and requires complex cross-chain state management, creating multiple attack surfaces. An exchange hack typically targets an exchange's hot wallet private keys or internal systems. Both result in loss of user funds, but the attack vectors and defenses are different.

**Is Mt. Gox creditor distribution complete?**
As of July 2026, distribution is ongoing. The rehabilitation trustee Nobuaki Kobayashi has distributed multiple tranches of BTC and BCH to registered creditors through approved custody providers. Not all creditors have completed the registration and verification process required to receive funds. Current distribution status is updated by the rehabilitation trustee on the official Mt. Gox website.

---

*This article documents historical events using public sources. It is for informational purposes only. Source links to court filings and official press releases are cited inline. TrustsCrypto does not represent the completeness of any legal proceeding or bankruptcy distribution process referenced here.*
