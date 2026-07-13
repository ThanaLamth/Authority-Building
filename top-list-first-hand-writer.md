# Top/List First-Hand Writer

This is the working formula for writing top/list, comparison, and roundup articles so they read like direct editorial work instead of generic SEO copy.

It is designed for articles that use some real first-hand review, but do not overclaim full product testing where that did not happen.

## Core principle

Do not pretend you tested more than you actually tested.

If you only reviewed public product surfaces, say that clearly.

If you completed a real workflow, say what you did, what happened, and what still needs deeper verification.

The writing should feel:

- direct
- observed
- balanced
- specific
- editorial

## Intro formula

Write the intro in two short paragraphs.

Paragraph 1:

- name the real user problem
- explain the decision the reader is trying to make

Paragraph 2:

- explain how the article evaluates the options
- show judgment, not just coverage

Example pattern:

`The real problem is not X. The real problem is Y.`

`That is why this article does not rank these options by feature count alone. It looks at them through the lens of friction, fit, tradeoffs, and long-term usefulness.`

## Trust block formula

Place a short trust block near the top of the article.

It should say:

- what was reviewed
- when it was reviewed
- what was checked directly
- what still needs deeper verification

Example pattern:

> Why you can trust this guide
>
> This guide is based on live public product surfaces and official references reviewed in July 2026. We directly checked the public positioning, visible workflow framing, and documentation shown below. Anything that depends on a logged-in workflow, live pricing, or a full end-to-end test still needs final verification before publication.

## First-hand section formula

Use a real section in the body, not an editor note.

Good H2 patterns:

- `What we checked ourselves before ranking these tools`
- `What we checked ourselves before comparing these platforms`
- `What changed once we looked at the actual public flow`

That section should do four things:

1. say what was directly reviewed
2. state the limit of that review
3. show visual evidence
4. explain what stood out

Example pattern:

`For this article, we reviewed the live public product surfaces of the shortlisted options so the comparison would not depend only on feature summaries and recycled roundups.`

`That direct review does not replace a full logged-in or end-to-end workflow test. But it does show something important very quickly: where each product puts friction, who it is built for, and what kind of user it expects.`

## First-person formula

Use first person only when it reflects a real action.

Safe phrases:

- `we reviewed`
- `we checked`
- `we noticed`
- `what stood out immediately was`
- `from the public surface we reviewed`
- `based on what we could verify directly`

If you only reviewed public surfaces, say that clearly.

Do not use:

- `we tested everything`
- `we used this for months`
- `we found this perfect`

unless that is literally true and defensible.

## What stood out formula

This is the sentence pattern that makes the article feel observed.

Examples:

- `What stood out immediately was not the feature count. It was the posture of the product.`
- `The clearest difference was not capability. It was where each platform puts friction in the workflow.`
- `Even before a logged-in test, the interface already signals who the product is really built for.`

This section should end with judgment.

Example:

`That makes this stronger for teams that need flexibility, but weaker for teams that only want the shortest path to launch.`

## Balanced evaluation formula

Every strong section needs both upside and downside.

Pattern:

1. state the strength
2. explain why it matters
3. state the weakness
4. explain who should avoid it

Example:

`X is strong because it reduces the gap between a fast launch and a more expandable stack later. But that same flexibility creates more decisions early in the process, which can feel like overhead if your only goal is a lightweight launch.`

## Tool review formula

Use the same structure for every item in the list.

```md
### Tool Name

X is a strong choice for [use case]. From the public flow we reviewed, it immediately felt more like [type of product] than [other type]. That is a strength if you need [benefit], but it becomes a weakness if your priority is [other need].

Best for:
- ...
- ...

Tradeoffs:
- ...
- ...
- ...
```

## Visual evidence formula

Screenshots should not sit silently in the article.

The prose should refer to what the visuals reveal.

Examples:

- `The screenshots above show why this matters.`
- `That visual difference is not cosmetic. It signals which kind of user the product expects.`
- `Even before a logged-in test, the interface already tells you whether the product is optimized for control, speed, or broader accessibility.`

## Publishing image workflow

Every image block should be labeled explicitly for the CMS workflow.

Use this format:

```md
**Featured Image**
File: `../media/example-image.png`
Alt text: `Clear SEO description of what the image shows`
Caption: `Editorial, SEO-clean caption tied to the article topic.`

![Clear SEO description of what the image shows](../media/example-image.png)

*Editorial, SEO-clean caption tied to the article topic.*
```

Follow-up image blocks:

```md
**Screenshot 1**
File: `../media/example-image-2.png`
Alt text: `Clear SEO description of what the image shows`
Caption: `Editorial, SEO-clean caption tied to the article topic.`
```

```md
**Screenshot 2**
File: `../media/example-image-3.png`
Alt text: `Clear SEO description of what the image shows`
Caption: `Editorial, SEO-clean caption tied to the article topic.`
```

## Caption formula

Captions should sound editorial and SEO-clean.

Examples:

- `Thirdweb homepage captured during our July 2026 review of NFT minting platforms.`
- `Magic Eden fee documentation captured during our July 2026 review of creator-royalty marketplaces.`
- `Parallel homepage captured during our July 2026 review of NFT games.`

Avoid:

- internal tool references
- repo references
- browser or capture-process references
- technical notes that do not help the reader

## Quantitative writing formula

If you have real data, use it.

Examples:

- setup time
- time to first successful action
- number of steps before checkout
- retrieval success
- onboarding friction

If you do not have hard data yet, do not fake precision.

Use this pattern:

`At this stage, we are comfortable describing the workflow difference qualitatively, but not yet assigning a hard performance number until the live test is complete.`

## Anti-PR rule

Every compliment should have a counterweight.

Examples:

- `This is powerful, but...`
- `This is cleaner, but...`
- `This feels easier, but...`
- `This is the better option for X, not for everyone.`

If a section only praises, it will read like sponsored copy.

## Closing formula

The ending should help the reader choose.

Pattern:

- choose A if...
- choose B if...
- choose C if...

Example:

`Choose Thirdweb if you need the best overall balance between control and long-term flexibility. Choose Crossmint if mainstream onboarding is the hardest problem in your launch. Choose Zora if the release is really a creator-publishing play rather than a generic sales workflow.`

## Fast checklist

- Did we say what we directly checked?
- Did we avoid overstating the depth of testing?
- Did we use first person only where true?
- Did we include at least one observed judgment?
- Did we show both strength and weakness?
- Did we label each image block for publishing?
- Did we keep captions editorial and SEO-clean?
- Did we avoid hype?
- Did the ending help the reader choose?
