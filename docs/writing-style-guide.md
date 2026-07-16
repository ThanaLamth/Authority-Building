# Writing Style Guide — Authority Building Network
## 10 Sites, 10 Signatures
Last updated: 2026-07-16

Each site in this network covers a distinct slice of the crypto space and targets a different reader.
This guide defines the voice, sentence logic, structural patterns, and vocabulary that make each site
recognizable so no two articles across the network read the same way.

---

## How to use this guide

Before writing any article, read the site section below. Then:

1. Match the **sentence rhythm** described for that site.
2. Use only vocabulary from the **Use / Avoid** list for that site.
3. Apply the **structural pattern** -- some sites never use numbered lists; some always do.
4. Check the **reader test**: if your article would confuse that reader, rewrite until it would not.

---

# 1. Coinlineup
**Identity:** Beginner crypto explainer
**Pillar:** /guides/ -- crypto-basics, wallets, DeFi, security
**Reader:** Someone who searched "what is a stablecoin" or "best bitcoin wallet for beginners."
They know crypto exists. They do not know how it works yet.

## Voice
Plain, patient, never condescending. Think of a smart older sibling explaining something at dinner,
not a professor. Every concept gets one sentence of context before being used.
Never assume prior knowledge. Never reward prior knowledge either.

## Sentence rhythm
Short. Then medium. Then short again.
Each paragraph is one idea. Max 2-3 sentences before a line break.
If a sentence needs a comma, ask whether it should be two sentences instead.

## Structure
- Always open with the decision the reader is facing, not a definition
- Use numbered lists for steps, bullet lists for comparisons
- Include a plain-language summary box before the deep dive
- End each platform section with a one-sentence verdict: "Best for X, not great for Y"
- Add a FAQ section at the bottom -- beginners search in questions

## Vocabulary
Use: simple, safe, clear, easy to set up, works with, supports, free to use, no technical setup required,
beginner-friendly, trusted, widely available, worth knowing, step-by-step
Avoid: liquidity, execution, onchain, derivatives, institutional, market structure, composable,
trustless, sovereign, non-custodial (unless immediately explained in plain language)

## Signature moves
- Analogies before definitions: "Think of a stablecoin like a poker chip that always equals one dollar."
- Warn readers what NOT to do before telling them what to do
- Parenthetical plain-language glossary: "self-custody (keeping your own keys, not relying on an exchange)"
- Never use jargon two sentences in a row without a plain restatement

## Reader test
Would a person who has owned crypto for less than 6 months finish the article and know exactly what to do next?
If not, simplify.

---

# 2. Coinwy
**Identity:** Practical community hub -- tools, wallets, exchanges, strategies
**Pillar:** /how-to/, /tools/, /wallets/, /exchanges/, /strategies/
**Reader:** Active crypto user with 1-3 years of experience. Has a wallet, uses an exchange,
wants to level up their setup. They are not new. They are optimizing.

## Voice
Peer-to-peer, direct, slightly opinionated. Like a forum power user who tested every tool
and is sharing findings without a pitch deck. No fluff, no filler praise. Honest about trade-offs.

## Sentence rhythm
Mostly medium sentences. Short sentences for verdicts and warnings.
Lists are fine -- this reader scans. But every list needs a framing sentence before it.
Avoid paragraph walls. 3-4 sentences max, then break.

## Structure
- Open with the workflow gap: "Here is the problem most portfolio trackers create."
- Comparison tables early -- this reader wants to orient fast before reading depth
- Rate each tool by specific use case, not general stars
- "Our pick for X" callouts in bold at start of each section
- End with a setup recommendation, not just a ranking

## Vocabulary
Use: syncs with, supports, connects to, tracks, integrates, lets you, gives you,
works best when, worth the trade-off, clean interface, reliable, free tier, paid plan,
portfolio, DeFi position, multi-chain, hot wallet, cold wallet, staking, yield
Avoid: institutional, market structure, macro, narrative (as standalone concept),
trustless, sovereign without context

## Signature moves
- "The problem with most X tools is Y" as an opener
- Quick 3-line comparison snippet before the full breakdown
- Explicit "not recommended for" -- what the tool is bad at
- Friction scores: call out setup friction explicitly ("takes 20 minutes to connect your first wallet")

## Reader test
Would a crypto user who already has a portfolio setup find something useful here that they did not know before?
If not, go deeper.

---

# 3. Kanalcoin
**Identity:** Southeast Asian / ASEAN perspective on global crypto
**Pillar:** /asia/ (Vietnam, Indonesia, Thailand, South Korea, Japan), /europe/, /americas/
**Reader:** Retail crypto user in SEA. Cares about local fiat access, remittance use cases,
local regulation, and regional adoption. Mobile-first. Price-sensitive.

## Voice
Grounded, regionally aware, respectful of local market nuance. Never default to Western crypto assumptions.
Name local rails, local brands, local regulators alongside global players.
A product that works in the US but not with IDR bank transfers is not good for this reader.

## Sentence rhythm
Medium sentences, accessible vocabulary. Write as if the article will be lightly machine-translated
and must still be clear. Avoid idioms, complex passive constructions, and US/EU cultural references.

## Structure
- Open with the local decision context: "For users in Vietnam / Indonesia / SEA..."
- Country-specific sections or callouts within sections
- Always include: fiat access, local payment rails, language support, regulation status
- Comparison table with country coverage as a column
- End with a country-by-country quick pick

## Vocabulary
Use: local fiat, bank transfer, P2P, IDR, THB, VND, regulated in, licensed by, mobile app,
easy deposit, low minimum, available in [country], regional exchange, remittance, local support
Avoid: institutional-grade, Bloomberg Terminal style, macro hedge, derivatives as primary concept,
trustless without local-language analogy

## Signature moves
- Flag when a platform is geo-restricted in a specific SEA country
- Note app store availability (iOS + Android) -- critical in mobile-first markets
- Reference local regulation explicitly: OJK (Indonesia), SEC Thailand, SSC Vietnam, FSC Korea
- Include "remittance use case" check for stablecoin articles

## Reader test
Would a retail user in Jakarta or Hanoi find this more useful than a generic global crypto article?
If not, add more local detail.

---

# 4. BitcoinMaximalist (BitcoinInfoNews)
**Identity:** Bitcoin-maximalist with deep network fundamentals focus
**Pillar:** /bitcoin-news, /bitcoin-guides, /bitcoin-markets, /bitcoin-mining, /bitcoin-ecosystem
**Reader:** Bitcoin-only holder. Cares about self-custody, signing models, network security,
Lightning, Ordinals, Layer 2. Technically literate. Skeptical of anything that dilutes Bitcoin's properties.
Altcoins are out of scope by default.

## Voice
Precise, technically grounded, philosophically consistent. Not evangelical -- assumed.
Bitcoin is the reference frame, not a thing being compared to other things.
Cite network fundamentals (hashrate, difficulty, UTXO set, block subsidy) as naturally
as other sites cite price.

## Sentence rhythm
Longer and more structured than other sites. This reader tolerates complexity if it is precise.
Use subordinate clauses and qualifications where they are technically necessary.
Lists for comparisons and spec tables. Prose for reasoning and tradeoff explanation.

## Structure
- Open with the custody or security question the reader is actually facing
- Verified table early: what was tested vs not tested
- Per-product sections with: signing model, backup logic, multisig support, software compatibility
- Bitcoin-specific tradeoffs only -- no generic "great for DeFi" language
- End with a self-custody setup recommendation and a security note

## Vocabulary
Use: self-custody, sovereign, airgap, PSBT, multisig, seed phrase, backup, signing model,
open-source, Bitcoin-only, hashrate, difficulty, block subsidy, Lightning, UTXO,
Taproot, Ordinals, Schnorr, descriptor wallet, watch-only
Avoid: altcoin praise, DeFi yield, portfolio tracker framing, "invest in" language,
"best for beginners" without a sovereignty-first framing

## Signature moves
- Technical spec tables: airgap | open-source firmware | passphrase support | multisig compatibility
- "This is a Bitcoin-only recommendation" as explicit framing when relevant
- Signing model explained before product verdict -- never skip it
- Security warnings about specific failure modes: SIM swap, supply chain, cloud backup risk

## Reader test
Would a Bitcoiner who reads technical self-custody research find this technically credible?
If not, go deeper on the fundamentals.

---

# 5. CCpress (Theccpress)
**Identity:** Crypto narrative journalism -- investigative, conflict-driven, power-focused
**Pillar:** /stories/, /conflicts/, /people/, /power/, /investigations/
**Reader:** Crypto-aware reader who wants the story behind the story.
Follows industry drama, knows the players, wants accountability and context -- not just price.
Expects citations, named sources, and editorial judgment.

## Voice
Investigative, editorial, morally clear without moralizing. Write like a beat reporter
who has covered the industry for three cycles. Name the actors. State the stakes.
Do not hedge facts into meaninglessness. If a company failed, say it failed.
If a regulator acted late, say it acted late.

## Sentence rhythm
Varied -- declarative short sentences for impact, medium for context, longer for analysis.
Never passive voice to protect a named party: "FTX collapsed" not "FTX was found to have issues."
Paragraphs are 2-4 sentences. Lead with the news, not the background.

## Structure
- Open with the central conflict or event, not general context
- Name the key actor in the first sentence
- Timeline blocks for complex sagas: date -- event -- consequence
- "Key players" or "Stakes" sidebar box
- Link between articles in the series to show the power map
- End with the unresolved question -- not a tidy summary

## Vocabulary
Use: collapse, enforcement, regulator, ruling, settlement, lawsuit, precedent, accountability,
allegations, fraud, misuse of funds, failed, violated, under investigation, market impact,
power structure, VC-backed, executives, creditors
Avoid: "space," "ecosystem" (too soft), "interesting narrative," "crypto community" as a vague mass,
passive constructions that obscure who did what, speculative price language

## Signature moves
- Open with a person or event, not a category definition
- Quote from public filings, official statements, or regulatory documents -- always cite
- "What this means for X" paragraph near the end: traders, creditors, regulators, builders
- Every article points forward or backward in the power map through internal links

## Reader test
Would an editor at a crypto news outlet accept this without cringing at the sourcing?
If not, add citations and sharpen the named-actor framing.

---

# 6. Coincu
**Identity:** Authoritative editorial with institutional and macro analysis
**Pillar:** /analysis/ (on-chain, derivatives, ETF, liquidity, institutional), /markets/, /research/
**Reader:** Professional or semi-professional crypto participant -- fund analyst, institutional allocator,
researcher, sophisticated trader. Expects depth, structure, citations, and a clear analytical framework.

## Voice
Authoritative, precise, structurally rigorous. Not academic -- but close.
Every claim is qualified with its basis. Every ranking has explicit criteria.
Never vague: not "institutional demand is growing" but
"institutional inflows into ETH-based products rose 40% QoQ through Q1 2026 [source]."

## Sentence rhythm
Longer, denser paragraphs than most sites. This reader does not need hand-holding.
But every paragraph has one clear job. Use headers to signal argument structure.

## Structure
- Open with the analytical problem, not the consumer question
- Criteria table or filter list before rankings: "We ranked by X, Y, Z because..."
- Per-entry sections with: structure, access model, risk, market role
- Data citations inline -- not footnotes, not vague "according to reports"
- End with a market-structure implication, not a buying recommendation

## Vocabulary
Use: institutional, structured product, access model, liquidity, on-chain distribution,
market structure, composable, capital flows, risk-adjusted, redemption mechanics,
regulatory framework, issuer structure, collateralization, settlement, RWA, tokenized
Avoid: "best for beginners," analogies before definitions, FAQ sections, "worth knowing,"
casual framing, price speculation without structural basis

## Signature moves
- Comparison table with structural columns: issuer | access | chain | redemption | risk
- Explicit analytical framework before the list: "This comparison prioritizes X over Y because..."
- "What this changes" section: market-structure implication of each product or event
- Cite primary sources: SEC filings, fund documentation, protocol governance posts

## Reader test
Would a crypto fund analyst use this as a first-pass research reference?
If not, add more structure and fewer adjectives.

---

# 7. MarketBit
**Identity:** Quantitative market analyst -- Bloomberg Terminal style
**Pillar:** /on-chain/, /derivatives/, /etf-flows/, /liquidity/, /market-structure/
**Reader:** Active trader, quant, or market-structure researcher.
Reads on-chain data, watches ETF flow dashboards, tracks funding rates and OI.
Comes to MarketBit for structured market interpretation, not news or product reviews.

## Voice
Data-first, terse, analytical without narrative padding.
State the metric. State what it means. State the implication for market structure.
No adjectives that do not carry data: not "significant buying pressure" but
"net inflows of  over 3 days [source]."
No consumer advice. No motivational framing.

## Sentence rhythm
Short declarative sentences. Dense information per sentence.
Lists for data breakdowns. Tables for metric comparisons.
Headers signal the data layer, not a question being answered.
Fewer transitions -- this reader connects the dots themselves.

## Structure
- Open with the market event or data observation, no preamble
- State the metric and timeframe before interpreting it
- Structure per section: observation -- mechanism -- market implication
- Include a "What to watch" section with specific signals or thresholds
- No product rankings -- only market analysis and structural explanation

## Vocabulary
Use: open interest, funding rate, net inflows, outflows, liquidations, long/short ratio,
basis, perpetual, implied volatility, MVRV, SOPR, NVT, exchange reserves, whale accumulation,
support/resistance, market structure, capital flows, stablecoin supply, ETF flows
Avoid: "best for beginners," product reviews, "I think," narrative labels without data,
"the community believes," buying recommendations, consumer feature comparisons

## Signature moves
- Lead with the data point: "BTC funding rate turned negative on July 14 for the first time since March."
- Mechanism paragraph: explain WHY a metric moved, not just that it moved
- Threshold callouts: "Watch the X level -- a break below triggers Y dynamic"
- Cross-metric validation: one metric alone is never enough; always pair with a second

## Reader test
Would a trader who stares at Glassnode and Coinglass all day find a new angle here?
If not, go deeper into the data.

---

# 8. Tokentopnews (topkentopnews)
**Identity:** Narrative + macro intelligence for active market participants
**Pillar:** /insights/, /trends/, /narratives/, /macro/, /weekly-recap/
**Reader:** Active crypto participant who wants to understand the meta-game -- which narrative is dominant,
why institutional capital is moving, what the next rotation looks like.
Not a beginner. Not a pure quant. An engaged crypto investor who also reads macro.

## Voice
Narrative-driven, intellectually confident, forward-looking without being reckless.
Connect market events to larger cycles and structural forces.
Write like a market strategist giving a Monday morning briefing:
grounded in recent data, contextualizing it against the bigger picture.

## Sentence rhythm
Medium-to-long sentences for narrative flow. Short sentences to land key points.
Paragraphs 3-4 sentences -- enough to build an argument before moving on.
Headers frame the argument, not just the topic:
"Why the AI narrative is holding while DeFi stalls" not "AI vs DeFi."

## Structure
- Open with the narrative tension: what is the market debating this cycle?
- Establish the framework: what filter is being used to evaluate narratives or signals?
- Per-narrative sections: why it matters now | who is positioned | what breaks the thesis
- Connect narratives to each other -- this reader wants the map, not isolated data points
- End with a forward-looking setup: what to watch in the next 4-8 weeks

## Vocabulary
Use: narrative, cycle, rotation, positioning, institutional flows, macro backdrop,
altcoin season, dominance, liquidity conditions, risk-on, risk-off, sentiment,
on-chain signal, watchlist, catalyst, breakout setup, regime
Avoid: "best for beginners," product how-to, pure feature comparisons,
over-specifying price targets, claiming certainty about future price direction

## Signature moves
- "Narrative score" or "conviction level" per theme without false precision
- Connecting paragraph: how this narrative links to the macro or Bitcoin cycle context
- Watchlist section: 3-5 names per narrative with one-sentence rationale each
- "What breaks the thesis" as a required section per narrative -- intellectual honesty built in

## Reader test
Would a mid-level crypto fund analyst or an engaged retail investor who reads macro find this
more useful than a standard "top coins" list? If not, add more framework and fewer tickers.

---

# 9. AiCryptoCore (aicrypto)
**Identity:** AI x Crypto intersection analyst
**Pillar:** /ai-agents/, /ai-infrastructure/, /ai-trading/, /ai-data/, /ai-ecosystem/
**Reader:** Developer, researcher, or sophisticated investor tracking the AI-on-chain space.
Understands what an LLM is. Understands what a smart contract is.
Wants to know: what is actually built, what is the token doing in the network, what is hype.

## Voice
Technical but not academic. Stack-aware, skeptical of pure narrative plays,
genuinely excited by real infrastructure work. Write like a developer who also reads venture memos.
Demand evidence of product before crediting narrative.
"This is real infrastructure. This is not." -- that contrast is the signature.

## Sentence rhythm
Medium sentences for explanation, short for verdict and skepticism.
Avoid adjective inflation: not "powerful AI system" but "inference-at-cost model with verifiable outputs."

## Structure
- Open with the stack question: where does this project sit in the AI-crypto architecture?
- Use-case clarity before token analysis -- token value follows product value
- Per-project: stack position | token role | usage evidence | risk profile
- "Real vs narrative" callout per section
- End with a builder or investor decision framework, not a buying recommendation

## Vocabulary
Use: compute, inference, model weights, decentralized compute, GPU marketplace,
subnet, validator, on-chain agent, training data, oracle, indexing, DeFi agent,
verifiable compute, open-source model, token utility, agent economy
Avoid: "AI-powered" without specifying what the AI does, "revolutionary," vague agent claims
without showing what the agent actually does, pure market-cap framing

## Signature moves
- Stack diagram in text: "Layer 0 (compute) -- Layer 1 (model) -- Layer 2 (agent application)"
- "What the token actually does" as a required section per project
- "Not yet proven" label for claims only in documentation, not live product
- Skepticism paragraph near the end: what would have to be true for this to fail?

## Reader test
Would a developer building an AI agent find the technical layer credible?
Would a quant investor find the token-utility section honest?
If either answer is no, revise.

---

# 10. NFTEnex (nftenex)
**Identity:** NFT and digital ownership specialist -- culture, markets, infrastructure
**Pillar:** /nft-ecosystem/, /nft-markets/, /nft-culture/, /gaming-nft/, /creator-economy/, /nft-infrastructure/
**Reader:** NFT creator, collector, developer, or infrastructure researcher.
Not a crypto-first reader -- an NFT-first reader. Cares about contract standards, minting tools,
creator royalties, marketplace liquidity, on-chain storage, community culture.

## Voice
First-person, evidence-based, opinionated from direct experience.
The NFTEnex voice is built on hands-on reviews: "we loaded the product, we navigated the dashboard,
here is what we found." Not speculation. Not aggregation. Direct experience, clearly bounded.
Where something was not directly tested, that limit is stated explicitly.

## Sentence rhythm
Max 45 words per prose paragraph -- enforced.
Experience paragraphs are sensory and direct: what did it feel like to land on this surface?
Captions are structured: [Platform] [surface type] [keyword], [Month YYYY] -- [extractable fact]. [Judgment.]

## Structure
- Factual intro paragraph: what the product is, year, chains, audience, pricing -- no opinions
- Reviewer verdict paragraph: where opinion and judgment live -- immediately after factual intro
- Experience paragraph before every screenshot: first-person, max 45 words, sensory-led
- SEO+AIO caption below every screenshot
- Community signal after Pros/Cons where a qualifying Reddit thread exists
- Verified table: what we checked vs what we did not

## Vocabulary
Use: minting, smart contract, royalties, creator, collector, on-chain, metadata, IPFS, Arweave,
pinning, wallet modal, authenticated dashboard, launch, floor price, ERC-721, ERC-1155,
marketplace, listing, ERC-2981, storage, verified, hands-on
Avoid: headless, programmatic, automation (as process descriptor), automated, leveraging, utilize,
seamlessly, cutting-edge, streamline, robust, delve into, it is worth noting, in conclusion

## Signature moves
- Two-paragraph platform opener: factual intro first, then verdict -- never merged
- Experience para before image: "Landing on Thirdweb's dashboard felt like..."
- Community signal: **Community signal:** [descriptive anchor](URL). [One sentence implication.]
- Star rating table with Unicode star characters -- never text-only labels
- Internal cross-links to related series articles: storage, metadata, royalties, marketplaces

## Reader test
Would an NFT developer evaluating minting tools find the review credible?
Would a creator choosing a marketplace trust the royalty analysis?
If not, add more direct evidence.

---

# Cross-site rules (apply to all 10 sites)

## Banned words (entire network)
headless, programmatic, automation (as process descriptor), automated review,
leveraging, utilize, seamlessly, cutting-edge, streamline, robust, delve into,
it is worth noting that, it is worth knowing that, in conclusion, in summary,
comprehensive (as empty praise), revolutionary, powerful (without specifics)

## Paragraph length
All sites: max 45 words per prose paragraph.
Exceptions: blockquotes, captions, tables, lists, headings.

## Internal link rule
- Max 3 cross-series internal links per article
- Only link when the mention is substantive -- not a passing keyword mention
- Use descriptive anchor text -- never "click here" or "this article"
- Never link intro paragraphs

## Community signal rule (NFTEnex + applies to any site doing hands-on reviews)
- Only add if: platform-specific thread, real user opinion, relevant subreddit, within 2 years
- Missing signal is better than a weak signal -- leave blank if no qualifying thread exists
- Format: **Community signal:** [anchor text](URL). [One implication sentence.]

## Screenshot / caption rule
- Alt text = literal image description (what is IN the image)
- Caption = SEO+AIO formula: [Platform] [surface] [keyword], [Month YYYY] -- [fact]. [Judgment.]
- Never duplicate alt text in caption
- Experience paragraph (first-person, max 45w) required above every screenshot in NFTEnex;
  strongly preferred for all other sites

## Word filter (run before every commit)
Scan article files for the banned word list above.
Fix all hits. Confirm 0 matches before pushing.