# Coinlive -- First 10 Article Outlines

Site identity: Real-time market pulse -- flash alert style
Pillar: /market-moves/, /price-action/, /exchange-flows/, /macro-events/
Reader: Active traders and on-chain analysts watching live market data. Multiple screens open.
Voice: Tight, data-first, calm and observational. No warm-up.
Date: 2026-07-24

---

## Shared brief rules

- Lead with the number: "Bitcoin dropped 4.2% in 40 minutes as..."
- Always include the timeframe: "over the past 4 hours," not "recently"
- One data point per sentence. Two related can share a sentence with a comma.
- No sentence above 25 words in market-moves or price-action pieces.
- Macro-events can run longer for context.
- Exchange-flows articles stay tightest.
- Banned: moon, dump, FOMO, FUD, diamond hands, historic (unless factually so), unprecedented (unless so)

---

## Article list

| # | Primary keyword | H1 | Pillar | Path |
|---|---|---|---|---|
| 1 | `bitcoin price action live` | Bitcoin Price Action: Current Level, Breakout Zones, and Exchange Flow Context | price-action | `/price-action/bitcoin/bitcoin-price-action-live` |
| 2 | `ethereum exchange outflows` | Ethereum Exchange Outflows: Net Flow Data, Wallet Destinations, and 30-Day Baseline | exchange-flows | `/exchange-flows/ethereum/ethereum-exchange-outflows` |
| 3 | `bitcoin liquidation data` | Bitcoin Liquidation Data: Long and Short Positions, Exchange Breakdown, and Trigger Levels | price-action | `/price-action/liquidations/bitcoin-liquidation-data` |
| 4 | `crypto market open interest` | Crypto Open Interest: Current Data Across BTC, ETH, and Altcoins | price-action | `/price-action/bitcoin/crypto-market-open-interest` |
| 5 | `bitcoin whale exchange inflows` | Bitcoin Whale Exchange Inflows: On-Chain Signal and Historical Pattern | exchange-flows | `/exchange-flows/whales/bitcoin-whale-exchange-inflows` |
| 6 | `fed rate decision crypto market` | Fed Rate Decision and Crypto Market: Immediate Price and Derivatives Response | macro-events | `/macro-events/regulation/fed-rate-decision-crypto-market` |
| 7 | `ethereum price breakout` | Ethereum Price Breakout: Setup, Trigger Level, and Volume Confirmation | price-action | `/price-action/breakouts/ethereum-price-breakout` |
| 8 | `crypto funding rate tracker` | Crypto Funding Rate Tracker: Which Assets Are Stretched Long or Short | price-action | `/price-action/volatility/crypto-funding-rate-tracker` |
| 9 | `usdt stablecoin inflows exchange` | USDT Exchange Inflows: Stablecoin Supply Data and What It Signals | exchange-flows | `/exchange-flows/inflows/usdt-stablecoin-inflows-exchange` |
| 10 | `bitcoin etf flow data today` | Bitcoin ETF Flow Data Today: Net Inflows, Outflows, and What the Derivatives Market Shows | macro-events | `/macro-events/etf/bitcoin-etf-flow-data-today` |

---

## Article 1 -- Bitcoin Price Action Live

**Primary keyword:** `bitcoin price action live`
**H1:** Bitcoin Price Action: Current Level, Breakout Zones, and Exchange Flow Context
**Pillar:** /price-action/
**Path:** `/price-action/bitcoin/bitcoin-price-action-live`
**Word count target:** 400-600 (price-action format -- dense, short sentences)

**Structure (price-action):** setup (level/zone) + trigger (event/threshold) + measured outcome (liquidations/flow)

**H2 skeleton:**
1. Current Price Level and Recent Range
2. Key Levels: Resistance and Support Zones With Volume Evidence
3. Liquidation Map: Which Levels Carry the Largest Liquidation Clusters
4. Exchange Flow Context: Net Inflows or Outflows Over the Past 24 Hours
5. What to Watch

**Lead template:** "Bitcoin is trading at $[X] as of [time UTC], [Y]% [above/below] the [timeframe] [high/low]. The [level] zone has [held/broken] [number] times in the past [timeframe]."

**Key data points per section:**
- Current price + 24h change % + 7d change %
- Nearest resistance: $[X] (volume node or prior swing high)
- Nearest support: $[X] (volume node or prior swing low)
- Liquidation cluster above: $[X] (cite Coinglass liquidation heatmap)
- Liquidation cluster below: $[X]
- Net exchange flow: [direction] over past 24h vs. 30-day baseline (cite CryptoQuant or Glassnode)

**Format rules:**
- No sentence exceeds 25 words
- Every level must have a source (CoinGecko, Glassnode, Coinglass, TradingView)
- "What to watch" closes with a specific threshold, not a general observation

---

## Article 2 -- Ethereum Exchange Outflows

**Primary keyword:** `ethereum exchange outflows`
**H1:** Ethereum Exchange Outflows: Net Flow Data, Wallet Destinations, and 30-Day Baseline
**Pillar:** /exchange-flows/
**Path:** `/exchange-flows/ethereum/ethereum-exchange-outflows`
**Word count target:** 350-500 (exchange-flows format -- tightest)

**Structure (exchange-flows):** net flow direction + asset + exchange + comparison to 30-day baseline

**H2 skeleton:**
1. Net Ethereum Exchange Flow: Current Reading vs. 30-Day Baseline
2. Which Exchanges Showed the Largest Outflows
3. Where the Outflows Are Going: Wallet Type Breakdown
4. What to Watch

**Lead template:** "Ethereum net outflows from exchanges reached [X ETH] in the [24h/7d] period ending [date], the [highest/lowest] reading in [timeframe], per [CryptoQuant/Glassnode]."

**Key data points per section:**
- Net flow (ETH amount + USD equivalent at time of reporting)
- Top 3 exchanges by outflow volume with individual amounts
- Destination wallet types: self-custody cold wallets, OTC desk addresses, staking contracts, unknown
- 30-day baseline comparison: current reading vs. 30-day average
- 7-day trend: sustained outflow pattern or reversal?

**Format rules:**
- Exchange-flows pieces carry the tightest sentence discipline
- Never write "ETH leaving exchanges suggests buying" -- report the flow, not the inferred intent
- If destination wallets are unknown or unlabeled, say so
- Baseline comparison is required in every exchange-flows article

---

## Article 3 -- Bitcoin Liquidation Data

**Primary keyword:** `bitcoin liquidation data`
**H1:** Bitcoin Liquidation Data: Long and Short Positions, Exchange Breakdown, and Trigger Levels
**Pillar:** /price-action/
**Path:** `/price-action/liquidations/bitcoin-liquidation-data`
**Word count target:** 400-600

**Structure (price-action):** setup + trigger threshold + measured outcome

**H2 skeleton:**
1. Total Bitcoin Liquidations in the Last 24 Hours
2. Long vs. Short Breakdown: Which Side Took the Larger Hit
3. Exchange Breakdown: Where Liquidations Were Concentrated
4. Liquidation Cluster Map: Key Levels That Remain Loaded
5. What to Watch

**Lead template:** "$[X] in Bitcoin long positions were liquidated in the [Y]-hour period ending [time UTC] on [date], per Coinglass. Short liquidations totaled $[Z] in the same period."

**Key data points per section:**
- Total liquidations (24h) in USD
- Long/short split by percentage
- Top 3 exchanges by liquidation volume with individual totals
- Largest single liquidation order (if Coinglass data shows it)
- Remaining liquidation clusters by price level (from heatmap)

**Format rules:**
- "Liquidated" = forced position closure by exchange -- not voluntary selling
- Always attribute to Coinglass or equivalent primary source
- Liquidation clusters are future risk levels -- present them as data, not predictions
- The "what to watch" section must name specific price thresholds

---

## Article 4 -- Crypto Market Open Interest

**Primary keyword:** `crypto market open interest`
**H1:** Crypto Market Open Interest: Current Data Across BTC, ETH, and Altcoins
**Pillar:** /price-action/
**Path:** `/price-action/bitcoin/crypto-market-open-interest`
**Word count target:** 450-650

**Structure:** observation (OI level) + mechanism (what high/low OI means for position risk) + implication (what changes this)

**H2 skeleton:**
1. Total Crypto Open Interest: Current Reading and Recent Trend
2. Bitcoin Open Interest: Level, Change, and Funding Rate Context
3. Ethereum Open Interest: Level and Comparison to BTC Dominance in OI
4. Altcoin OI: Which Markets Are Most Stretched
5. What to Watch

**Lead template:** "Total crypto derivatives open interest reached $[X] on [date], [direction] from $[Y] one week earlier, per Coinglass. Bitcoin accounted for $[Z] of the total."

**Key data points per section:**
- Total OI by market (BTC, ETH, top altcoins)
- OI change % over 7 days and 30 days
- Funding rates for each major market (positive = long-skewed, negative = short-skewed)
- Historical context: current OI vs. prior cycle peak OI (cite Coinglass historical data)
- Exchange breakdown: which exchanges carry the most OI (Binance, OKX, Bybit, CME)

**Format rules:**
- OI alone is not directional -- funding rate is required as the second data point
- CME OI is important to report separately: it represents institutional positioning
- "OI is high" without a funding rate comparison is incomplete -- always pair both

---

## Article 5 -- Bitcoin Whale Exchange Inflows

**Primary keyword:** `bitcoin whale exchange inflows`
**H1:** Bitcoin Whale Exchange Inflows: On-Chain Signal and Historical Pattern
**Pillar:** /exchange-flows/
**Path:** `/exchange-flows/whales/bitcoin-whale-exchange-inflows`
**Word count target:** 350-500

**Structure (exchange-flows):** net flow direction + asset + exchange + comparison to 30-day baseline

**H2 skeleton:**
1. Current Whale Inflow Reading and Timeframe
2. Which Exchanges Are Receiving the Largest Whale Transfers
3. How This Compares to the 30-Day Baseline and Prior Episodes
4. What to Watch

**Lead template:** "[X] BTC in whale-sized transactions (defined as transactions above [threshold]) moved to exchanges in the [24h/7d] window ending [date], per [CryptoQuant/Glassnode]. This is [Y]% [above/below] the 30-day average."

**Key data points per section:**
- Whale threshold definition used (must be stated -- commonly >$1M or >100 BTC)
- Top 3 exchange destinations with individual BTC amounts
- 30-day baseline comparison
- Historical precedent: did similar whale inflow levels precede specific market outcomes? (report as data, not prediction)

**Format rules:**
- Define "whale" -- do not use the term without specifying the threshold
- "Whale inflows to exchanges" is observable; "whales are selling" is an inference -- never collapse them
- Historical comparison is context, not prediction -- frame it as such
- Source must be named for every flow figure

---

## Article 6 -- Fed Rate Decision and Crypto Market

**Primary keyword:** `fed rate decision crypto market`
**H1:** Fed Rate Decision and Crypto Market: Immediate Price and Derivatives Response
**Pillar:** /macro-events/
**Path:** `/macro-events/regulation/fed-rate-decision-crypto-market`
**Word count target:** 600-900 (macro-events can run longer for context)

**Structure (macro-events):** event + primary market reaction + on-chain or derivatives confirmation

**H2 skeleton:**
1. What the Fed Announced and What the Market Expected
2. Bitcoin and Ethereum Immediate Price Response: First 60 Minutes
3. Derivatives Response: Funding Rate and OI Change Post-Announcement
4. Exchange Flow Response: Any Notable Inflows or Outflows in the Hour After
5. What the Next Fed Meeting Implies for Market Positioning

**Lead template:** "The Federal Reserve [held/raised/cut] its benchmark rate to [X]% on [date], [in line with / contrary to] market expectations of [X]%, per [FOMC statement / Fed press release]."

**Key data points per section:**
- Decision date, rate level, and expected level (from CME FedWatch at time of announcement)
- BTC price 1 hour before vs. 1 hour after announcement (with exact prices and timestamps)
- ETH same comparison
- Funding rate change (positive/negative shift, by how many basis points)
- OI change in first hour after announcement
- Any notable exchange flow signal in the hour after

**Format rules:**
- Macro-events articles close with one on-chain or derivatives data point as confirmation
- Use CME FedWatch probabilities as "market expectation" -- not analyst opinion
- Immediate reaction (first 60 minutes) is more reliable than 24h move because noise increases over time
- Do not attribute a price move solely to the Fed decision -- state the correlation, not the causation

---

## Article 7 -- Ethereum Price Breakout

**Primary keyword:** `ethereum price breakout`
**H1:** Ethereum Price Breakout: Setup, Trigger Level, and Volume Confirmation
**Pillar:** /price-action/
**Path:** `/price-action/breakouts/ethereum-price-breakout`
**Word count target:** 400-600

**Structure (price-action):** setup (level/zone) + trigger (event/threshold) + measured outcome

**H2 skeleton:**
1. Current Ethereum Price and the Range It Is Breaking From
2. What Defines the Breakout Level: Volume Node, Prior Resistance, or Liquidation Cluster
3. Volume and OI Confirmation: Is the Move Validated?
4. What a Failed Breakout Would Look Like
5. What to Watch

**Lead template:** "Ethereum broke above $[X] on [date] at [time UTC], clearing resistance that had held since [date]. Volume in the first [Y] minutes of the move reached [Z], per [CoinGecko/TradingView]."

**Key data points per section:**
- Breakout level in USD (precise)
- Volume in the breakout candle vs. prior 5-day average volume
- OI change at time of breakout
- Funding rate at breakout: is longs paying shorts, or the reverse?
- Failed breakout definition: close below $[X] would negate the move
- Next key level above: $[Y] (volume node or prior swing high)

**Format rules:**
- A breakout is defined by a close above the level, not a wick through it
- Volume confirmation is required -- a move on low volume is noted as unconfirmed
- "Breakout" without OI and funding context is incomplete for derivatives traders
- The "failed breakout" scenario must be stated with a specific price level

---

## Article 8 -- Crypto Funding Rate Tracker

**Primary keyword:** `crypto funding rate tracker`
**H1:** Crypto Funding Rate Tracker: Which Assets Are Stretched Long or Short
**Pillar:** /price-action/
**Path:** `/price-action/volatility/crypto-funding-rate-tracker`
**Word count target:** 400-600

**Structure:** observation + mechanism + implication

**H2 skeleton:**
1. Current Funding Rate Snapshot Across Major Assets
2. Most Stretched Long Positions: Assets With Highest Positive Funding
3. Most Stretched Short Positions: Assets With Highest Negative Funding
4. Bitcoin and Ethereum Funding Rate Trend: 7-Day Pattern
5. What to Watch

**Lead template:** "Bitcoin perpetual funding rate sits at [+/-X]% per 8 hours as of [date], [above/below] the neutral level, per Coinglass. [Asset] carries the highest positive funding rate at [Y]%, suggesting long-side concentration."

**Key data points per section:**
- Funding rate table: top 10 assets by absolute funding rate value
- Positive funding rate list: who is paying longs (short squeeze potential if rate extreme)
- Negative funding rate list: who is paying shorts (long squeeze potential if rate extreme)
- BTC and ETH 7-day funding rate trend (chart context in text form: "rate has been positive for 5 of 7 days")
- Historical comparison: current BTC funding rate vs. peak readings in prior 90 days

**Format rules:**
- Funding rate is an 8-hour payment between longs and shorts -- explain the direction clearly
- Positive funding = longs pay shorts = market is long-skewed
- Negative funding = shorts pay longs = market is short-skewed
- Extreme funding rates (above 0.1% per 8h or below -0.1%) are historically mean-reverting -- note the data, not the prediction

---

## Article 9 -- USDT Stablecoin Inflows Exchange

**Primary keyword:** `usdt stablecoin inflows exchange`
**H1:** USDT Exchange Inflows: Stablecoin Supply Data and What It Signals
**Pillar:** /exchange-flows/
**Path:** `/exchange-flows/inflows/usdt-stablecoin-inflows-exchange`
**Word count target:** 350-500

**Structure (exchange-flows):** net flow direction + asset + exchange + comparison to 30-day baseline

**H2 skeleton:**
1. Current USDT Exchange Inflow Reading
2. Which Exchanges Are Receiving the Largest USDT Inflows
3. Total USDT Supply Context: Mint and Burn Activity
4. What to Watch

**Lead template:** "[X] USDT moved to exchanges in the [24h/7d] period ending [date], per [CryptoQuant/Glassnode]. This is [Y]% [above/below] the 30-day average of [Z] USDT per day."

**Key data points per section:**
- USDT net exchange inflow in USD and token amount
- Top 3 exchanges by USDT inflow (Binance, OKX, Bybit typically dominate)
- 30-day baseline comparison
- USDT total supply: recent mint activity (cite Tether treasury wallet on-chain)
- USDT stablecoin supply ratio (SSR): ratio of Bitcoin market cap to stablecoin supply (cite Glassnode)

**Format rules:**
- USDT inflows to exchanges is observable; "buying pressure incoming" is an inference -- never collapse them
- Stablecoin inflows and price correlation have a documented but lagged relationship -- present the data, not the prediction
- Tether mint events are on-chain verifiable -- cite the treasury address or Whale Alert
- SSR is a useful secondary metric but requires defining it when first used

---

## Article 10 -- Bitcoin ETF Flow Data Today

**Primary keyword:** `bitcoin etf flow data today`
**H1:** Bitcoin ETF Flow Data Today: Net Inflows, Outflows, and What the Derivatives Market Shows
**Pillar:** /macro-events/
**Path:** `/macro-events/etf/bitcoin-etf-flow-data-today`
**Word count target:** 600-800

**Structure (macro-events):** event + primary market reaction + on-chain or derivatives confirmation

**H2 skeleton:**
1. Today's ETF Flow Data: Net Inflows or Outflows by Fund
2. Which Funds Are Leading Inflows and Which Are Seeing Redemptions
3. Cumulative Flow Trend: Week-Over-Week and Month-Over-Month Context
4. Derivatives Market Response: Spot vs. Futures Premium After Flow Data
5. What to Watch

**Lead template:** "US spot Bitcoin ETFs reported a combined [net inflow/outflow] of $[X] on [date], per [BitMEX Research / Bloomberg ETF tracker / official fund data]. [Fund] led with $[Y] in net [inflows/outflows]."

**Key data points per section:**
- Flow table: fund name | issuer | net flow (day) | cumulative AUM | data source
- Top 3 funds by net inflow and top fund by net outflow (if applicable)
- Week-over-week total flow comparison
- Month-to-date cumulative total
- Spot vs. futures premium: CME basis at time of flow data release (Contango or Backwardation?)
- Funding rate on perpetual markets: responding to ETF demand signal or decoupled?

**Format rules:**
- Macro-events articles close with one derivatives data point as confirmation
- ETF flows are reported on a one-day lag -- state the data lag explicitly
- Spot premium over futures (backwardation) is a different signal than the reverse -- define it
- Do not attribute price moves solely to ETF flows; they are one input among several
