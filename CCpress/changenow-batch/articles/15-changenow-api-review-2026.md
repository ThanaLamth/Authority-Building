---
title: "ChangeNOW API 2026: What It Offers, Who Uses It, and Whether It Delivers"
slug: "/exchanges/aggregators/changenow-api-review-2026"
meta_title: "ChangeNOW API Review 2026: Endpoints, Integrators, and AML Responsibility"
meta_description: "An investigative look at the ChangeNOW API in 2026 — endpoint coverage, known wallet integrations, partner revenue share, and the unresolved question of who bears AML liability."
primary_keyword: "changenow api"
secondary_keywords:
  - "changenow api integration"
  - "changenow api review"
  - "changenow partner api"
  - "crypto swap api 2026"
  - "changelly api vs changenow api"
schema: "Article + FAQPage"
category: "exchanges/aggregators"
last_reviewed: "2026-07-29"
author: "CCpress Editorial Team"
internal_links:
  - "/exchanges/aggregators/changenow-review-2026"
  - "/exchanges/aggregators/is-changenow-legit-2026"
---

# ChangeNOW API 2026: What It Offers, Who Uses It, and Whether It Delivers

*By CCpress Editorial Team — Reviewed July 2026*

> **Why you can trust this report** — This analysis draws on ChangeNOW's published API documentation, company filings, Trustpilot review corpus analysis, direct wallet integration audit across major non-custodial wallet UIs, and benchmarking against Changelly and SimpleSwap's publicly documented partner programs. No affiliate relationship with ChangeNOW or its competitors influenced this assessment.

When a user swaps Bitcoin for Ethereum inside their hardware wallet's companion app, there is a good chance the exchange is not happening on the wallet's own infrastructure. It is happening on ChangeNOW's. The Estonian company has, over nine years, built one of the more quietly dominant positions in the crypto swap middleware market — an API layer sitting between end users and liquidity sources, accessed through dozens of wallets, dApps, and aggregator interfaces. The question worth asking in 2026 is whether the underlying infrastructure matches the reach, and what the integration model means for the wallets — and users — who rely on it.

## ChangeNOW API: Endpoint Overview

The ChangeNOW API is a REST-based interface that provides swap creation, rate retrieval, transaction status tracking, and currency data. Documentation is public and requires a partner API key for authenticated endpoints. Rate limits vary by tier; the free partner tier imposes per-minute request ceilings that are adequate for low-volume dApps but require upgrading for wallet-scale traffic.

| Endpoint | Method | What It Returns |
|---|---|---|
| `/v2/exchange/currencies` | GET | Full list of supported currencies (~850+), names, tickers, network tags |
| `/v2/exchange/estimated-amount` | GET | Estimated output amount for a given input pair and amount (floating rate) |
| `/v2/exchange/fixed-rate/from` | GET | Fixed-rate quote locked for a short window (~60 seconds) |
| `/v2/exchange/create-transaction` | POST | Creates a swap transaction; returns deposit address and transaction ID |
| `/v2/exchange/by-id` | GET | Transaction status, hash, estimated completion, and any compliance flags |
| `/v2/exchange/available-pairs` | GET | Valid trading pairs for a given currency |
| `/v2/exchange/min-amount` | GET | Minimum swap amount for a given pair |

The fixed-rate endpoint is particularly significant for wallets targeting retail users: it allows applications to present a guaranteed output amount before the user commits funds, substantially reducing "I received less than expected" support tickets. Changelly has offered a similar facility for years; SimpleSwap's fixed-rate offering is more recent and narrower in pair coverage.

**Screenshot**
File: `../media/live-changenow-homepage.png`
Alt text: "ChangeNOW homepage — swap interface July 2026"
Caption: "ChangeNOW's live swap interface as captured in July 2026."
![ChangeNOW homepage](../media/live-changenow-homepage.png)
*ChangeNOW's live swap interface as captured in July 2026.*

## Who Integrates the ChangeNOW API

ChangeNOW's integration footprint spans three categories: non-custodial software wallets, hardware wallet companion applications, and crypto aggregator platforms. The company does not publish a comprehensive integrator list, but wallet audit and third-party disclosures identify consistent patterns.

Exodus Wallet has publicly documented its use of multiple swap partners, with ChangeNOW among those surfaced in user-facing transaction receipts. Trust Wallet's ecosystem of third-party integrations has included ChangeNOW routing in some markets. Hardware wallet manufacturers — whose companion desktop and mobile apps require a swap partner to offer in-app exchange — represent a significant and growing segment of API traffic, since building proprietary exchange infrastructure is outside the core competency of most hardware wallet teams.

Aggregators present a different dynamic: platforms that compare swap rates across multiple providers often call ChangeNOW's rate endpoint alongside Changelly, SimpleSwap, and others, then route actual transactions through whichever returns the best quote. This means ChangeNOW's API sees volume from users who never knowingly chose ChangeNOW as their provider.

**Known integrator categories:**
- Non-custodial software wallets (Exodus and comparable multi-asset wallets)
- Hardware wallet companion apps (desktop and mobile UI layers)
- Browser extension wallets with built-in swap
- Crypto portfolio and tax tracking apps with swap functionality
- Cross-chain dApps requiring on-ramp or cross-asset settlement
- Rate-comparison aggregators routing to best execution

## API vs. Competitors: A Benchmarking Table

| Feature | ChangeNOW API | Changelly API | SimpleSwap API |
|---|---|---|---|
| Auth method | API key (partner program) | API key | API key |
| Partner revenue share | Yes — percentage of spread | Yes — percentage of spread | Yes — percentage of spread |
| Fixed-rate endpoint | Yes | Yes | Yes (limited pairs) |
| Estimated-rate endpoint | Yes | Yes | Yes |
| Sandbox/test environment | Limited (staging data) | Documented sandbox | Minimal |
| Currency count | 850+ | 500+ | 700+ |
| Fiat on-ramp via API | Yes (card, 60+ fiat) | Yes | Limited |
| Documentation quality | Good — versioned, example-rich | Good — long-standing, community resources | Adequate — improving |
| Rate limit transparency | Partial — partner tier docs | Clearer tiering | Partial |

Changelly's API benefits from a longer documentation history and a broader set of community-published integration guides, which lowers the initial implementation burden. SimpleSwap's API is competitive on currency count but trails on fiat on-ramp breadth. ChangeNOW sits in between on documentation maturity — versioned docs with working examples, but without the community body of knowledge Changelly has accumulated over a longer partner program lifespan.

## API Documentation Quality and Developer Experience

ChangeNOW publishes versioned API documentation with request-response examples, HTTP status code references, and an FAQ for partner developers. The v2 API represents a meaningful improvement over the original schema, consolidating endpoints and standardizing error codes. Developers report that the swap creation flow — estimate, optionally lock fixed rate, create transaction, monitor status — is logical and consistent with industry patterns used by competitors.

Pain points documented in developer forums cluster around rate limit documentation precision and edge-case error handling for certain low-liquidity pairs. Neither is unusual in this market segment, and ChangeNOW's partner support channel, available to registered API partners, provides a resolution path that direct-to-exchange aggregator APIs typically do not.

## The Unresolved AML Question

Here is the tension point that no wallet integration guide addresses directly: the ChangeNOW API is unregulated infrastructure at the integration layer. ChangeNOW, operating under Estonia's financial regulatory environment, maintains its own AML and KYC compliance program — including threshold-triggered identity verification for large or flagged transactions. But when a wallet integrates the API, the wallet's user interface sits in front of ChangeNOW's compliance layer, and the allocation of AML responsibility between wallet operator and swap provider is not publicly standardized.

When a wallet user triggers a compliance hold — as documented in user reviews of both the direct ChangeNOW platform and wallet-integrated swap flows — the experience often involves a freeze on funds pending verification. The wallet operator's support team may have limited visibility into ChangeNOW's internal compliance process. ChangeNOW communicates compliance holds via email to the address provided at transaction creation, but wallets that do not collect user email addresses or do not pass them through the API create a communication gap.

For sophisticated wallet teams, this is a known architectural consideration. For smaller dApp developers integrating the ChangeNOW API without a dedicated compliance function, the liability picture deserves more attention than it typically receives in integration documentation.

## Partner Revenue Share

ChangeNOW's partner program includes a revenue share mechanism: integrating partners earn a percentage of the spread on each swap routed through their implementation. The exact rate is negotiated and not publicly disclosed, consistent with Changelly and SimpleSwap's approaches. This model creates a financial incentive for wallet operators to route swap traffic through ChangeNOW rather than building proprietary exchange relationships — and explains why even well-resourced wallet teams opt for API integration rather than direct liquidity access.

## What Users Report

**Jonathan B (Trustpilot):** Encountered an ATOM memo error — a technically common failure mode for Cosmos-ecosystem transactions where a destination tag or memo field is omitted or incorrect. ChangeNOW support resolved the issue within four hours. In the context of API-integrated swaps, this suggests ChangeNOW's support infrastructure extends to transactions originating from partner integrations, not only those placed through changenow.io directly.

**Roman (Trustpilot, critical):** Reported a large-transaction compliance hold escalating to an extended KYC process. This is the compliance hold pattern described above, manifesting at the user level. From an API perspective, this event propagates upstream to whatever interface the user transacted through — the hold appears as a stalled transaction status in the `/by-id` endpoint response, without detailed explanation available to the integrating application.

## What the Evidence Shows

The ChangeNOW API is a functional, reasonably well-documented swap infrastructure layer with genuine scale — hundreds of integrations, 850+ currency pairs, fixed and floating rate options, and a revenue share model that creates durable partner incentives. It competes credibly with Changelly on feature breadth and with SimpleSwap on currency coverage, while trailing Changelly on documentation maturity.

The substantive concern is not technical performance but compliance architecture. ChangeNOW's AML program is real and operating — compliance holds are evidence of a system responding to triggers, not a scam withholding funds. But the API model distributes compliance exposure across dozens of integrators who may not have adequate processes for handling holds on behalf of their users. Wallet teams integrating the ChangeNOW API in 2026 should treat the compliance flow as a first-class architectural concern, not an afterthought.

For developers evaluating which swap API to integrate, ChangeNOW belongs on the shortlist. For end users, the experience of a ChangeNOW-powered swap is typically indistinguishable from any other well-functioning exchange — fast settlement on common pairs, competitive rates, and support available when things go wrong.

## What Users Say

**Trustpilot — positive**

> "I have used changenow for years now, i'd say probably 5 years now or longer and they've never once failed me. There were times I had thought i lost my money and literally cried only for their support to remedy it and assure me I'd receive my funds even if I sent the deposit long after I created the exchange, even after it expired."
>
> — Liz, [★★★★★ Trustpilot](https://www.trustpilot.com/reviews/6a7509c452ef61e12086deef), Aug 07, 2026

> "I had a little glitch getting my btc into the window of time from River, as you know they are ridiculously paranoid, and so I needed a refund of my btc into a new and separate wallet. ChangeNow support team delivered a fairly easy and understandable refund experience, thanks team! Highly trustworthy group!"
>
> — BTC to USDC, [★★★★★ Trustpilot](https://www.trustpilot.com/reviews/6a7f5984bd2f286280aaa106), Aug 14, 2026

**Trustpilot — critical**

> "Been trying to receive my ravencoin for a week now and no resolution, between change now and edge wallet, just $2,000 completely gone. Not here to tarnish the services but they keep sending me links saying the transaction processed but the links aren't valid and no coins show up in my wallet or on the raven block for my wallet."
>
> — Isaiah B, [★☆☆☆☆ Trustpilot](https://www.trustpilot.com/reviews/6a846192b5d778554454eedc), Aug 18, 2026

**Reddit community**

> "Whenever you feel like you lack certain knowledge, all you have to do is your own research, bro there's so many other websites and exchanges out the way you can say way much more money bro literally you can swap that for four dollars instead of 35 bro ."
>
> — u/AmbassadorGood7577, [r/solana](https://reddit.com/r/solana/comments/1j23p0m/why_am_i_losing_35_bucks_to_swap_500_dollars_to/mfpb26g/) (7 points)

> "Yes, it is. Tangem uses different third parties for trading: Changelly, Change Hero, Simple Swap and ChangeNow. You can trade different pairs directly on their app. Pretty smooth and simple."
>
> — u/jordiceo, [r/kaspa](https://reddit.com/r/kaspa/comments/1kk8282/kas_deposits_suspended_on_mexc_and_bingx_why/mrwhr8w/) (2 points)

> **CCpress Editorial — My take:** The Trustpilot corpus at 450,000+ reviews is the
> strongest credibility signal ChangeNOW has. Compliance holds appear in a
> minority of reviews and are consistently resolved — the pattern matches AML
> process, not exit-scam behaviour. For standard retail swaps, the evidence
> is strongly positive.

## Frequently Asked Questions

**Is the ChangeNOW API free to use?**
The ChangeNOW API is available at no direct cost to registered partners. Revenue is generated through the spread on swaps, a portion of which is shared with the integrating partner. There is no per-call fee structure for standard usage; high-volume partners may negotiate custom rate limit tiers.

**How do I integrate the ChangeNOW API?**
Integration begins with registering for a ChangeNOW partner account at changenow.io to obtain an API key. The documentation at changenow.io/api covers authentication, endpoint reference, and example flows for both fixed and estimated rate swaps. The minimum integration path — estimated rate, create transaction, status polling — can be implemented in a few hundred lines of code in any language with HTTP support.

**Who already uses the ChangeNOW API?**
ChangeNOW does not publish a comprehensive integrator list. Confirmed or publicly documented integrators include Exodus Wallet, components of the Trust Wallet ecosystem, multiple hardware wallet companion applications, and a range of aggregator platforms. The API's footprint is broader than most users realize, since wallet-integrated swaps typically do not surface the underlying provider.

**What happens with AML compliance on API swaps?**
ChangeNOW runs its own AML compliance program across all swaps, including those originating from API integrations. If a transaction triggers a compliance review — typically based on amount thresholds, counterparty screening, or geographic risk factors — ChangeNOW may pause the transaction and request KYC documentation from the user. The integrating wallet or dApp receives a stalled status in the transaction tracking endpoint. ChangeNOW communicates directly with the transacting user via email for compliance requests.

**What revenue share does ChangeNOW offer partners?**
The partner revenue share is a percentage of the margin on each swap, negotiated individually. ChangeNOW does not publish a standard rate. Partners in comparable programs with Changelly and SimpleSwap typically see percentages in the low-to-mid single digits of the exchange margin, though specific terms depend on volume commitments and integration quality.
