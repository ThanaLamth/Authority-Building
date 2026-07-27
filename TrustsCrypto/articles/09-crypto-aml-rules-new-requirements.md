---
title: "What the New AML Rules Require From Crypto Firms: Scope, Deadline, and Penalties"
slug: "/news/crypto-aml-rules-new-requirements"
meta_title: "Crypto AML Rules 2024: FinCEN Requirements for VASPs Explained"
meta_description: "What FinCEN's 2024 AML rules require from crypto firms: which entities are in scope, what KYC and transaction monitoring obligations apply, the Travel Rule threshold, and penalties for non-compliance."
schema: "NewsArticle"
primary_keyword: "crypto aml rules new requirements"
last_reviewed: "2026-07-27"
---

# What the New AML Rules Require From Crypto Firms: Scope, Deadline, and Penalties

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "What the New AML Rules Require From Crypto Firms: Scope, Deadline, and Penalties",
  "description": "What FinCEN's 2024 AML rules require from crypto firms: which entities are in scope, what KYC and transaction monitoring obligations apply, the Travel Rule threshold, and penalties for non-compliance.",
  "datePublished": "2026-07-27",
  "dateModified": "2026-07-27",
  "publisher": {
    "@type": "Organization",
    "name": "TrustsCrypto"
  }
}
```

The Financial Crimes Enforcement Network (FinCEN) published a Notice of Proposed Rulemaking in the Federal Register on May 14, 2024, proposing to designate "international convertible virtual currency mixing" as a primary money laundering concern under Section 311 of the USA PATRIOT Act. The proposed rule requires covered financial institutions, including crypto exchanges and money services businesses that are already Bank Secrecy Act (BSA)-regulated, to implement enhanced due diligence requirements for transactions involving mixing services. This article covers both that May 2024 proposed rule and the existing BSA obligations that apply to virtual asset service providers (VASPs) under current FinCEN regulations.

## What the New AML Rules Actually Require From Crypto Firms

Crypto firms that are money services businesses (MSBs) under 31 C.F.R. § 1010.100(ff) are already subject to existing BSA requirements. Those existing requirements are: registration with FinCEN as a money services business; implementation of an anti-money laundering program with written policies, internal controls, and independent testing; appointment of a designated compliance officer; and ongoing training.

The existing Travel Rule obligation for MSBs, codified at 31 C.F.R. § 1010.410, requires MSBs to transmit certain information to the next financial institution in any funds transfer of USD 3,000 or more. FinCEN has stated that this rule applies to convertible virtual currency transfers above that threshold. The Travel Rule refers specifically to FATF Recommendation 16 in the international framework; the U.S. threshold is USD 3,000, which differs from FATF's recommended threshold of USD 1,000 applied by many non-U.S. jurisdictions.

Under the May 2024 proposed Section 311 rule, covered institutions would be required to prohibit or apply enhanced due diligence to transactions from or to mixers, including: maintaining records of mixer-related transactions, filing Suspicious Activity Reports (SARs) for transactions with mixer indicators, and implementing technical controls to identify transactions involving known mixer addresses.

A proposed rule is not a final rule. The comment period for the May 2024 NPRM closed in August 2024. A final rule had not been published in the Federal Register at the time of this article's last review. Pending confirmation: the status of the Section 311 mixer rule as final or proposed should be verified at FinCEN.gov before making compliance decisions.

## Why These Requirements Change Compliance Obligations for VASPs

The distinction between a proposed rule and a final rule carries legal weight for compliance planning. Proposed rules set out an agency's intended requirements and invite public comment; they do not impose binding legal obligations on their own. Once a final rule is published in the Federal Register with an effective date, obligations become enforceable.

For the existing BSA obligations already in effect, the consequences of non-compliance are not theoretical. FinCEN has levied civil monetary penalties against crypto firms including BitMEX (USD 100 million in a 2021 consent order with DOJ and CFTC alongside FinCEN's civil component), Bittrex (USD 29 million in 2023), and Coinbase's predecessor entity for BSA violations (as part of a broader settlement). These penalties are disclosed on FinCEN's enforcement actions page.

The Section 311 designation, if finalized, would be significant because it would require covered institutions to take affirmative steps to screen for and report mixer-involved transactions rather than simply filing SARs when they identify suspicious activity. That moves the obligation from reactive to proactive.

## Which Firms, Products, and Jurisdictions Are In Scope

The existing BSA obligations apply to crypto exchanges, peer-to-peer exchangers, and administrators of convertible virtual currency that are doing business "wholly or in substantial part" in the United States. Firms incorporated offshore but accepting U.S. customers are not automatically exempt.

The Section 311 proposed rule applies to "covered financial institutions," a defined term in the PATRIOT Act that includes banks and MSBs. It does not directly apply to decentralized protocols or non-custodial wallet software, because those are not financial institutions under the statutory definition.

Hardware wallet manufacturers, open-source protocol developers, and node operators are not covered financial institutions under the existing statutory framework. FinCEN's 2019 guidance clarified that non-custodial actors -- those who do not control customer funds -- are generally not money services businesses. That guidance remains in effect.

The European Union's Anti-Money Laundering Regulation (AMLA), which established a new pan-EU supervisory authority for AML compliance in the financial sector including crypto asset service providers, operates under a separate legal framework from U.S. FinCEN requirements. CASPs registered under MiCA are subject to the AMLR's requirements, which are distinct from the U.S. BSA framework.

## What Remains Unclear About Implementation or Enforcement Priority

FinCEN has not published a comprehensive enforcement priority list for 2024 or 2025 that ranks which VASP types it will examine first under the BSA framework. Prior enforcement actions suggest the agency has focused on firms with large U.S. customer bases and evidence of systematic compliance failures rather than small operators.

How FinCEN's Section 311 designation for mixers would interact with privacy-preserving protocols that are designed for legitimate uses -- including Tornado Cash, which a U.S. federal appeals court ruled in November 2024 that FinCEN's Office of Foreign Assets Control (OFAC) had overstepped by sanctioning its immutable smart contracts -- is an unresolved question. The OFAC sanctioning of Tornado Cash and the Section 311 designation are separate but related regulatory actions that had not been fully coordinated at time of writing.

No-action periods for firms that self-identify as non-compliant with mixer-related requirements have not been announced.

## What Compliance Teams and Affected Firms Should Watch

FinCEN.gov publishes final rules in the Federal Register section of its website. Compliance teams should monitor that page for the final Section 311 mixer rule publication, which will include an effective date and any compliance phase-in periods.

BSA examination guidance from FinCEN and the Federal functional regulators (OCC, FDIC, Federal Reserve for bank-affiliated entities) is published through the FFIEC BSA/AML Examination Manual. The 2024 edition includes updated sections on virtual currency.

Any subsequent OFAC action naming specific mixer addresses or protocols should be treated as a sanctions compliance matter, separate from the BSA obligations, because the legal authority and enforcement mechanism are different. OFAC maintains the SDN list and publishes updates at treasury.gov.

---

**Sources reviewed for this article**

- FinCEN Notice of Proposed Rulemaking, Section 311 mixer designation, May 14, 2024: https://www.federalregister.gov/documents/2024/05/14/2024-10474
- FinCEN, Bank Secrecy Act regulations: https://www.fincen.gov/resources/statutes-and-regulations
- FinCEN guidance on convertible virtual currency, 2019: https://www.fincen.gov/sites/default/files/2019-05/FinCEN%20Guidance%20CVC%20FINAL%20508.pdf
- FFIEC BSA/AML Examination Manual: https://bsaaml.ffiec.gov/manual
- U.S. Court of Appeals, Fifth Circuit, Tornado Cash OFAC ruling, November 2024