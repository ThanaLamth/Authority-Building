# NFTEnex First-Hand Upgrade SOP

This SOP defines how the team should run real hands-on tests for the first four NFTEnex articles that benefit most from stronger E-E-A-T evidence.

## Scope

Upgrade these four articles first:

1. `nftenex/articles/01-best-nft-minting-tools-2026.md`
2. `nftenex/articles/04-best-nft-marketplaces-for-creator-royalties-2026.md`
3. `nftenex/articles/05-best-nft-storage-tools-2026.md`
4. `nftenex/articles/07-best-nft-apis-2026.md`

## Goal

Replace purely editorial comparison language with real first-hand evidence where possible:

- direct test workflow
- screenshots from the real process
- measured observations
- real friction points
- troubleshooting notes
- clearer "better for X, worse for Y" judgments

## Shared Test Standard

Use one controlled package across all four articles.

### Test collection

- Collection name: `NFTEnex Test Drop July 2026`
- Asset count: `5`
- Asset type: `PNG`
- Metadata files: `5 JSON files`

### Metadata fields

Each metadata file should include:

- `name`
- `description`
- `image`
- `attributes`

### Wallets

Prepare:

- `creator wallet`
- `buyer wallet`
- `observer wallet`

### Chains

- Preferred chain: `Base`
- Fallback chain: `Polygon`

If one platform cannot support the shared chain for the exact workflow being tested, document the fallback clearly.

### Tracking sheet columns

Use one shared sheet with these columns:

- article
- tool or platform
- date tested
- chain used
- test owner
- time to account ready
- time to first successful action
- total steps
- major friction point
- failed step
- screenshots captured
- final verdict

## Evidence Rules

Only claim what was actually tested.

### Safe language after a real test

- `In our test run...`
- `During setup...`
- `When we completed the workflow...`
- `The biggest delay came from...`
- `The easiest part of the process was...`

### Safe language if testing stayed partial

- `From the public product surface we reviewed...`
- `Based on the current live documentation...`
- `What we could verify directly was...`

Do not claim:

- long-term usage unless true
- perfect reliability unless proven
- broad performance claims from one narrow test

## Screenshot Standards

Capture original screenshots only.

Do not use:

- stock images
- promo images from the vendor
- screenshots from third-party blogs

### Required labeling format for article insertion

```md
**Featured Image**
File: `../media/example.png`
Alt text: `SEO-clean description of what the image shows`
Caption: `Editorial caption tied to the article topic.`
```

Follow-up blocks:

- `Screenshot 1`
- `Screenshot 2`
- `Screenshot 3` if needed

### Caption rules

Captions should be:

- editorial
- natural
- SEO-clean
- specific to the page topic

Do not mention:

- internal tools
- repos
- browser names
- capture process

## Quantitative Rules

Every upgraded article should add at least one measured observation per tested tool where practical.

Examples:

- time to account ready
- time to first successful mint
- time to first successful API response
- number of required setup steps
- number of manual interventions

If exact measurement is not available, do not invent it.

Use this kind of sentence instead:

`At this stage, we are comfortable describing the workflow difference qualitatively, but not assigning a hard time benchmark until the full live test is complete.`

## Test Workflow 1: Minting Tools

Target article:

- `nftenex/articles/01-best-nft-minting-tools-2026.md`

### Priority shortlist

- Thirdweb
- Crossmint
- Zora
- Manifold

### Goal

Prove:

- setup friction
- contract control
- checkout behavior
- time to first mint

### Exact workflow

1. Create account or sign in using a clean creator workflow.
2. Start one new collection using the shared 5-asset package.
3. Configure chain, contract type, metadata source, and mint settings.
4. Publish a low-cost live mint flow.
5. Mint one item from the buyer wallet.
6. Confirm the minted item appears in wallet or marketplace view.

### Record

- time from landing page to collection created
- time from collection created to first live mint
- number of mandatory decisions before publish
- whether card checkout exists
- whether mainstream onboarding feels realistic
- what broke or felt unclear

### Capture

- dashboard home
- collection setup screen
- contract or settings screen
- checkout or mint screen
- minted asset in wallet or marketplace
- any error or confusing step

### Upgrade requirements for the article

Add:

- one short methodology paragraph
- one measured comparison line per tool
- one real friction note per tool
- one `better for X, worse for Y` sentence per tool

## Test Workflow 2: Creator Royalties

Target article:

- `nftenex/articles/04-best-nft-marketplaces-for-creator-royalties-2026.md`

### Priority shortlist

- OpenSea
- Magic Eden
- Zora
- Manifold storefront flow

### Goal

Prove:

- how visible royalties are
- how configurable they are
- how easy they are to verify

### Exact workflow

1. Use the shared test collection.
2. Set one fixed royalty value, for example `5%`.
3. List one asset where the platform supports the flow.
4. Check where royalty settings are shown during setup.
5. Check where fee breakdown is shown during listing or checkout.
6. Execute one low-value secondary sale if practical.
7. Confirm whether creator earnings logic is visible after sale.

### Record

- steps required to find royalty settings
- whether royalty wording is clear or vague
- whether fee breakdown is visible before confirmation
- whether royalty appears enforced, surfaced, or mostly hidden
- whether the creator can verify outcome without reading docs

### Capture

- royalty setting screen
- fee or help page actually used during the test
- listing screen
- checkout fee breakdown
- post-sale history or earnings evidence
- any mismatch between docs and UX

### Upgrade requirements for the article

Add:

- one first-hand section on how hard royalties were to verify
- one screenshot-backed note on fee visibility
- one real downside for each platform
- one sentence on who should avoid each marketplace

## Test Workflow 3: Storage Tools

Target article:

- `nftenex/articles/05-best-nft-storage-tools-2026.md`

### Priority shortlist

- Pinata
- one Arweave-based flow
- Filebase
- Lighthouse

Optional:

- self-managed IPFS pinning

### Goal

Prove:

- upload clarity
- retrieval confidence
- operational burden

### Exact workflow

1. Upload the shared 5-asset and metadata package.
2. Generate the final asset URLs, content IDs, or transaction references.
3. Resolve each asset from at least three gateways or retrieval surfaces.
4. Link one metadata file to one live test NFT.
5. Recheck retrieval after 24 hours.
6. Note what the team would need to maintain long term.

### Record

- time to upload full package
- time to first successful retrieval
- number of manual steps
- whether proof output is obvious
- whether fallback retrieval is easy
- whether the workflow feels safe for non-technical operators

### Capture

- upload screen
- CID or transaction output
- metadata JSON rendered
- asset resolving from gateway
- linked asset shown in wallet or marketplace
- any failed or inconsistent retrieval

### Upgrade requirements for the article

Add:

- one measured sentence on upload or retrieval
- one practical note on maintenance burden
- one troubleshooting note if retrieval failed
- one clear recommendation by team type

## Test Workflow 4: NFT APIs

Target article:

- `nftenex/articles/07-best-nft-apis-2026.md`

### Priority shortlist

- Alchemy
- Reservoir
- SimpleHash
- QuickNode

Optional second pass:

- Moralis
- Zerion
- Blockdaemon

### Goal

Prove:

- docs clarity
- time to first useful response
- response usefulness

### Exact workflow

1. Create account and generate API key.
2. Run four calls against the same wallet or collection:
   - wallet NFT ownership
   - single token metadata
   - transfer history
   - collection-level lookup or market context
3. Validate response shape against the same expected fields.
4. Check how much normalization or cleanup is still needed.
5. Note any rate-limit, auth, or docs friction.

### Record

- time to first successful authenticated call
- number of steps before first useful response
- docs clarity
- metadata completeness
- ownership accuracy
- whether response is ready for product use or still messy

### Capture

- docs page
- API key or dashboard screen
- successful response in Postman or terminal
- one edge-case or error response
- side-by-side field comparison notes

### Upgrade requirements for the article

Add:

- one real `time to first useful response` note
- one docs-friction note
- one response-quality note
- one sentence on which product team should avoid each API

## Article Update Rules After Testing

For each upgraded article, replace vague language with:

- exact workflow used
- date tested
- chain used
- wallets used
- one measured number
- one real friction point
- one screenshot-backed observation
- one troubleshooting or limitation note

## Minimum Deliverables Per Upgraded Article

Each article should end the upgrade cycle with:

- updated trust block
- one first-hand methodology section
- at least two original screenshots from the real test
- at least one measured observation
- at least one explicit tradeoff grounded in the test
- one clearer final chooser section

## Publish Gate

Before the upgraded version goes live, confirm:

- screenshots are original and labeled correctly
- captions are SEO-clean
- no sentence overclaims test depth
- dates tested are included where needed
- any chain-specific caveat is disclosed
- article still reads like editorial analysis, not a product diary
