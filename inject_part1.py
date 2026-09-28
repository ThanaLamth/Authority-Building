import json, re, glob, os

data = json.load(open("scraped_reviews.json", encoding="utf-8"))

REVIEWS = {
    "swapzone": {
        "pos": {"text": "Support helped me with failed swap (because I sent small amount of Litecoin). After 1,5 hours I got my Monero (XMR). I recommend this platform.", "author": "Marcin", "url": "https://www.trustpilot.com/reviews/6a591e93a253790283802d7a"},
        "neg": {"text": "I cannot recommend Swapzone as long as n.exchange is used as one of its CEX partners for swap execution. Transactions routed through n.exchange can become subject to lengthy AML/compliance reviews.", "author": "Omer Onat", "url": "https://www.trustpilot.com/reviews/6a6f80f806aa7388e54514b5"},
    },
    "stealthex": {
        "pos": {"text": "Fast, private, and flawless swap! Just used StealthEX and the experience was perfect. The transfer was incredibly fast and the process was simple to follow. I didn't need to contact support at all.", "author": "coininstant", "url": "https://www.trustpilot.com/reviews/6a150bfda822d691391a4ca5"},
        "neg": {"text": "My 30 BNB swap has been frozen by StealthEX for over 3 MONTHS under a vague compliance review with zero real resolution.", "author": "Tinney Dustin", "url": "https://www.trustpilot.com/reviews/6a6fafcc64ceb531a8b1f36d"},
    },
    "changenow": {
        "pos": {"text": "Reliable and honest swap service -- great customer support. I accidentally sent an ATOM transaction without a memo when the field glitched out. Reached out to support, and even though it took a couple of hours to process manually, they had it sorted and credited to my wallet well within their 4-hour timeframe.", "author": "Jonathan B", "url": "https://www.trustpilot.com/reviews/6a83070692d5b9770ea69a95"},
        "neg": {"text": "My transaction has been held by the Compliance Department for an extended period. I completed KYC, provided every document requested, including proof of funds and source of income, yet my case keeps getting escalated with no resolution.", "author": "Roman", "url": "https://www.trustpilot.com/reviews/6a69d669e73d29b57b2ffe18"},
    },
    "simpleswap": {
        "pos": {"text": "I've found them to be very trustworthy. I made a mistake with a transaction and their service team were very responsive and did get my refund sorted. The most important thing is, the money was safe and returned.", "author": "Jeff Love", "url": "https://www.trustpilot.com/reviews/6a763f7b4f1dae8cb071ed43"},
        "neg": {"text": "I swapped Bitcoin for Solana, and after more than 6 hours, I still had not received my SOL. I expected a crypto swap to be completed within a reasonable amount of time, but the delay has been extremely frustrating.", "author": "Yves", "url": "https://www.trustpilot.com/reviews/6a77a9e733e83b72cbf5b037"},
    },
    "exolix": {
        "pos": {"text": "Used them a few times for xmr swaps. no kyc is great. rates are okay, took about 15 mins to get my coins. overall decent service.", "author": "Gavin Hetr", "url": "https://www.trustpilot.com/reviews/69ef6206ea40dd787bbec07a"},
        "neg": {"text": "I've now had multiple transactions frozen by Exolix due to their overdue error. There is no explanation of this error anywhere on their website. They claim that I didn't pay on time, even though I sent the funds within minutes.", "author": "Dog", "url": "https://www.trustpilot.com/reviews/69f34fd57a995f0a28e1b5f4"},
    },
    "swapspace": {
        "pos": {"text": "Love SwapSpace! Truly convenient and yet the least expensive.", "author": "Cryptoristical", "url": "https://www.trustpilot.com/reviews/6a62e81e8c33a3966a0de045"},
        "neg": {"text": "A partner deliberately slowed my transaction so the rate dropped at completion, then delivered 410 XLM less than quoted. SwapSpace support did not intervene.", "author": "Sam", "url": "https://www.trustpilot.com/reviews/6a3e1834bf530da86f73d742"},
    },
    "changelly": {
        "pos": {"text": "Support is incredibly fast! Apirone processes a large volume of exchanges through Changelly. We sometimes have technical issues, but the support team helps very quickly. It's like they work on our team.", "author": "Maxim Boyarov", "url": "https://www.trustpilot.com/reviews/6a75b351788d09c3940bfd0c"},
        "neg": {"text": "Transaction failed. Support said there was a sudden fluctuation in the exchange rate on a Sunday for a stablecoin. I cancelled the transaction and I'm waiting for the refund.", "author": "Anand", "url": "https://www.trustpilot.com/reviews/6a81ee4ebc747f405a85aecd"},
    },
    "nexo": {
        "pos": {"text": "I've been an active user and I never had any issue with NEXO. Customer Service is excellent, the app is well designed and my personal experience with NEXO is positive.", "author": "customer", "url": "https://www.trustpilot.com/reviews/6a79ae436f54bddb7c38fc01"},
        "neg": {"text": "Borrowing is available for Nevada so I signed up and got verified. But borrowing is NOT available to me specifically. Contacted support, escalated to agent, waited over an hour. This company is a joke.", "author": "J.", "url": "https://www.trustpilot.com/reviews/6a7f35f8d9178ca012a98b07"},
    },
}
