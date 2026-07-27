---
title: "What MiCA's Stablecoin Rules Actually Require: Issuer Obligations and Timeline"
slug: "/news/mica-stablecoin-regulation-explained"
meta_title: "MiCA Stablecoin Regulation Explained: EMT and ART Issuer Obligations"
meta_description: "What MiCA's stablecoin rules actually require from issuers in the EU: reserve obligations, the EMT and ART distinction, authorization scope, and what remains unresolved under EBA technical standards."
schema: "NewsArticle"
primary_keyword: "mica stablecoin regulation explained"
last_reviewed: "2026-07-27"
---

# What MiCA's Stablecoin Rules Actually Require: Issuer Obligations and Timeline

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "What MiCA's Stablecoin Rules Actually Require: Issuer Obligations and Timeline",
  "description": "What MiCA's stablecoin rules actually require from issuers in the EU: reserve obligations, the EMT and ART distinction, authorization scope, and what remains unresolved under EBA technical standards.",
  "datePublished": "2026-07-27",
  "dateModified": "2026-07-27",
  "publisher": {
    "@type": "Organization",
    "name": "TrustsCrypto"
  }
}
```

The Markets in Crypto-Assets Regulation (MiCA) imposed licensing requirements on stablecoin issuers operating in the European Union from June 30, 2024, per the official EUR-Lex text ([Regulation EU 2023/1114](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32023R1114)). Issuers of e-money tokens (EMTs) and asset-referenced tokens (ARTs) must hold authorization from a national competent authority or cease EU operations.

## What MiCA's Stablecoin Rules Actually Require

MiCA defines an e-money token in Article 3(1)(7) as a crypto-asset that purports to maintain a stable value by referencing the value of one official currency. An EMT issuer must be either a licensed credit institution or an authorized electronic money institution under Directive 2009/110/EC.

An asset-referenced token, defined in Article 3(1)(6), references a basket of currencies, commodities, or other crypto-assets rather than a single official currency. ART issuers require authorization from a national competent authority under Article 17, which is a distinct licensing pathway from the EMT route.

Both categories share a reserve obligation set out in Article 36: reserve assets must back the outstanding token supply on a 1:1 basis and must be legally and operationally segregated from the issuer's own assets. At minimum 30% of the reserve must be held as deposits in credit institutions. The remaining assets must be invested in highly liquid instruments with minimal credit risk and market risk.

The regulation uses the term "authorization" throughout. That word is not interchangeable with registration, notification, or informal approval. An issuer that has applied for authorization but not yet received it is not licensed. The distinction between "licensed to operate" and "compliant with all applicable technical standards" is further material: an authorized issuer may still be implementing EBA regulatory technical standards that were finalized in phases after June 2024.

Issuers whose tokens exceed a defined threshold are classified as significant, which transfers oversight to the European Banking Authority. The regulation sets that threshold at average daily outstanding volume exceeding EUR 5 billion or average daily transaction count exceeding 10 million.

## Why These Requirements Matter for Issuers and Users in the EU

The segregation obligation in Article 36 has direct operational consequences. Issuers cannot commingle reserve assets with operating capital. If an issuer becomes insolvent, token holders hold a claim against the segregated reserve pool, not against the issuer's general creditors. For users, that is a structural distinction from holding an exchange-issued stablecoin backed only by a contractual promise.

The 30% credit institution deposit floor sets a cost floor for reserve management that did not exist before MiCA. Issuers that previously held all reserves in money market funds or short-duration sovereign debt must restructure a portion into lower-yield bank deposits. That cost difference is likely to appear in fees or embedded spread.

Significant EMT classification shifts the competent supervisor from one member state authority to the EBA, which applies pan-EU supervisory standards. Compliance teams dealing with a significant designation face a pan-EU framework, not the standards of a single authorizing country.

## Which Stablecoin Issuers and Products Are in Scope

Circle Financial Europe SAS received EMT authorization from the Autorité des marchés financiers (AMF) in France in July 2024, covering EURC and, per Circle's subsequent disclosures, USDC issued through the EU entity.

Société Générale Forge received EMT authorization for EURCV (EUR CoinVertible), its euro-referenced token.

Tether Limited, issuer of USDT, had not received authorization from any EU national competent authority as of the third quarter of 2024. Binance announced removal of USDT trading pairs for European Economic Area users in November 2024. Kraken announced the same effective February 2025. Users in [CryptoCurrency community threads on Reddit](https://www.reddit.com/r/CryptoCurrency/comments/1gk3h7b/mica_usdt_which_exchanges_in_europe_have_delisted/) tracked which platforms had moved first and which remained exposed.

The reverse solicitation exemption in Article 4 is narrow. It does not cover active marketing or distribution to EU users by a third-country issuer without an EU legal entity.

## What Remains Unclear or Subject to EBA Technical Standards

Three areas remain unresolved as of this article's last review date.

EBA's interpretive position on algorithmic stabilization mechanisms under the ART definition has not been formalized. Article 22(3) prohibits ARTs whose supply is algorithmically adjusted to maintain a peg, but the boundary between a partial algorithmic adjustment mechanism and a fully prohibited design has not been defined in published EBA guidance. Pending confirmation: no EBA opinion on this point had been published at time of writing.

The treatment of third-country issuers distributing tokens to EU users without an EU legal entity depends on enforcement by national competent authorities. Those authorities had not harmonized their cross-border enforcement approaches at time of writing.

Reserve audit frequency for authorized issuers was subject to ongoing national competent authority implementation guidance. EBA finalized its regulatory technical standards on reserve composition in phases through 2024, but the audit cycle requirements had not been uniformly applied across member states at time of writing.

## What Issuers and Users Should Watch

EBA's supervisory college structure for significant EMTs will determine how cross-border issuers manage dual oversight in practice. The first decisions from that college will establish the practical compliance standard for significant token issuers.

Authorization queues have varied by member state. Issuers that applied before Q4 2024 faced different timelines depending on which national competent authority received their application. Further data from national authorities will clarify realistic licensing lead times.

EU-regulated exchanges have begun restricting unlicensed stablecoin pairs beyond USDT. Issuers that have not received authorization face ongoing delisting risk on regulated EU platforms.

The EBA's remaining technical standards on investor protection disclosures and interoperability with payment systems are on a phased publication schedule. Compliance teams should monitor the EBA MiCA regulatory framework page for final publications.

---

**Sources reviewed for this article**

- EUR-Lex, Regulation EU 2023/1114 (full text): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32023R1114
- EBA MiCA regulatory framework and technical standards: https://www.eba.europa.eu/regulation-and-policy/mica
- Circle, AMF authorization announcement, July 2024: https://www.circle.com/blog/circle-receives-first-mica-license-in-europe
- Binance, EEA stablecoin delisting notice, November 2024: https://www.binance.com/en/support/announcement/