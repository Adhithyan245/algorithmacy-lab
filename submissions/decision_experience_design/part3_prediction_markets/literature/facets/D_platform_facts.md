# D. Platform facts and primary sources

*Facet D of the Decision Experience Design (DXD) Part 3 literature review. Agent-drafted on 2026-10-03. The author has not reviewed it, and none of the text below is the author's.*

**What this facet covers.** How Polymarket and Kalshi present markets (D1), how contracts resolve and what documented disputes show (D2), and the regulatory and market-structure facts that shape the interface (D3). **Headline limitation: no primary source could be opened this session.** Every platform and regulator domain I tried (docs.polymarket.com, polymarket.com, kalshi.com, help.kalshi.com, docs.kalshi.com, cftc.gov, courtlistener.com, federalregister.gov, sec.gov, congress.gov, wikipedia, reuters, arxiv, ssrn, crossref, and the law-firm and news pages that WebSearch returned) was refused by the network egress proxy (HTTP 403 on CONNECT; WebFetch error EGRESS_BLOCKED). This is an organization policy block, not a bot wall, and I did not try to route around it. What I have is (i) WebSearch result summaries, which are secondary and unverified against the pages, and (ii) Consensus abstracts for academic papers. Under the brief's rule, nothing in section (b) is a verified platform fact. Section (c) lists every claim that needs a primary fetch before it enters the essay.

**Legend for read status.** *Search summary only* = the WebSearch tool returned a generated summary of results; I did not open the page. *Abstract only* = a Consensus record with abstract. *Not accessible* = the page was refused. Bearing on the essay's thesis (decision markets are poor decision experience design) is marked **supports**, **complicates** or **refutes**.

---

## (a) Search log

All requests ran on 2026-10-03.

| # | Source | Exact query / request | Result | Notes |
|---|---|---|---|---|
| 1 | WebFetch | docs.polymarket.com `/polymarket-learn/trading/fees` | EGRESS_BLOCKED | Not accessible |
| 2 | WebFetch | docs.polymarket.com `/polymarket-learn/markets/how-are-markets-resolved` | EGRESS_BLOCKED | Not accessible |
| 3 | WebFetch | help.kalshi.com (root) | EGRESS_BLOCKED | Not accessible |
| 4 | WebFetch | kalshi.com/regulatory/rulebook | EGRESS_BLOCKED | Not accessible |
| 5 | curl via proxy | HEAD on 14 hosts: docs.polymarket.com, polymarket.com, kalshi.com, help.kalshi.com, docs.kalshi.com, api.elections.kalshi.com, cftc.gov, courtlistener.com, wikipedia, api.crossref.org, reuters.com, arxiv.org, papers.ssrn.com, federalregister.gov | 14 of 14 returned CONNECT 403 | The proxy status endpoint showed no relay failures; per /root/.ccr/README.md, 403 is an egress policy denial and is to be reported, not retried. Reported here. |
| 6 | WebFetch | dlapiper.com 2026-09 tracker; congress.gov CRS LSB11441; theblock.co 2026-09-26; sec.gov Robinhood 10-Q | All EGRESS_BLOCKED | URLs taken from search 7 results. Not accessible |
| 7 | WebSearch | `Kalshi sports contracts share of volume 2026 CFTC state lawsuits` | 9 links, summary | Secondary. Used for D3. |
| 8 | WebSearch | `Polymarket UMA oracle dispute resolution controversy market ruling` | 9 links, summary | Secondary. Used for D2. |
| 9 | WebSearch | `Polymarket US relaunch CFTC approval QCEX app sports contracts fees` | 9 links, summary | Secondary. Used for D3 and D1 (fees). |
| 10 | WebSearch | `Kalshi fee schedule taker fee formula help center order types limit market cents` | 9 links, summary | Secondary (fee-calculator blogs, not Kalshi). Used for D1. |
| 11 | WebSearch | `Polymarket volume share sports versus politics 2026 monthly volume breakdown` | 10 links, summary | Secondary. Includes a Pew Research short read. Used for D3. |
| 12 | WebSearch | `Kalshi market resolution dispute rule clarification after trading began contract wording lawsuit settlement` | 9 links, summary | Secondary. Used for D2. |
| 13 | Consensus | `Polymarket Kalshi prediction market accuracy favorite-longshot bias` | 20 | Academic. Used in sections B4 and B5. |
| 14 | Consensus | `prediction markets sports contracts gambling Kalshi retail users behavior regulation` | 20 | Academic. Used in B4 to B6. |
| 15 | Scholar Gateway | `What do empirical studies of Polymarket and Kalshi trading data show about accuracy, favorite-longshot bias, wash trading, and the share of sports contracts?` | Error | `INVALID_QUERY: Could not resolve user identity from CONNECT`. Logged and skipped, as Facet A recorded on 2026-10-01. |

---

## (b) Entries

Entries follow the research questions. Bib keys are in D_platform_facts.bib. Each web-summary entry carries the access date 2026-10-03.

### B1. How the platforms present markets (D1)

**No primary source was readable, so D1 has no verified fact about price display, order entry, default order types, mobile app, categories, notifications or share features.** The only D1 material is below.

**kalshi_fees_secondary** — Fee-calculator and explainer pages returned by WebSearch (marketmath.io, pm.wiki, polykal.net, others; none by Kalshi). Not opened.
- *Read status:* search summary only.
- *What it argues:* Kalshi's taker fee is stated as 0.07 x C x (1 minus C) per contract, rounded up to the cent, with C the contract price in dollars; the maximum falls at 50 cents (1.75 cents per contract). Maker fees are stated as 25 percent of the taker fee. Orders that take liquidity execute against the resting order book, which implies an order-book interface with limit orders.
- *Bearing:* **supports**, if confirmed. A fee that peaks at 50 cents and shrinks toward the extremes is an interface-relevant fact (cost depends on the price the user sees). Confirm against the Kalshi fee schedule PDF before use. [verify]

**polymarket_us_fees_secondary** — Search summary of crypto-news pages on the December 2025 US relaunch (bitcoinmagazine.com, cryptonews.com and others). Not opened.
- *Read status:* search summary only.
- *What it argues:* the summary says the platform charges no direct trading fees on the international site (gas and spreads only) and about 0.01 percent for US traders through QCEX. The two sources the summary draws on are not named, and the 0.01 percent figure conflicts with how I expect a sports-heavy US exchange to charge. [verify]
- *Bearing:* unknown. Do not cite.

**kalshi_chart_study** — Sah, S., et al. (2026). Prediction market visualizations, betting, and uncertainty: a study of Reddit posts and comments. arXiv 2608.16814.
- *Read status:* abstract only (Consensus).
- *What it argues:* prediction-market platforms present contracts through visualizations of probabilities, prices, trends, odds and payouts that "often appear precise" but do not show uncertainty directly. From about 12,000 posts and 96,000 comments in r/Kalshi, the authors thematically analyze 360 posts that contain visualizations. Users read uncertainty off market movement, struggle with probability information, question liquidity, critique the design and tie charts to betting decisions.
- *Bearing:* **supports** the essay's claim that the display, not the mechanism, is where the decision experience lives. It is a preprint. It is also the only item in this facet that studies how users read the interface.

### B2. Documented resolution disputes on Polymarket (D2)

**polymarket_uma_secondary** — WebSearch summary over polymarketguide.gitbook.io, crypto.news, gate.com, laikalabs.ai, webopedia.com, oddsshopper.com and a Substack. Not opened.
- *Read status:* search summary only.
- *What it argues:* a proposer posts an outcome with a bond; an unchallenged proposal becomes final; a dispute escalates to a vote of UMA token holders, which is final and on-chain. The summary reports more than 1,150 disputed Polymarket markets in the first five months of 2026, above the 2025 full-year total. It describes a Ukraine minerals market in which one holder cast about five million tokens across three accounts (about 25 percent of that round's vote) and traders on the losing side lost roughly 7 million dollars, and a market on whether Strategy would sell Bitcoin by 31 May 2026 that resolved No although a 1 June filing showed a sale of 32 BTC inside the window.
- *Bearing:* **supports**, if confirmed: the resolution rule lives outside the trading screen. Every figure here is a generated summary of crypto-news sources of unknown quality. [verify] Use only after reading the Polymarket market rules pages, the UMA documentation and at least one news report that cites a primary record (UMA voting portal or on-chain transaction).

### B3. Documented resolution disputes on Kalshi (D2)

**kalshi_disputes_secondary** — WebSearch summary over gamingamerica.com, coindesk.com, mdf-law.com, oddsshopper.com, defirate.com and a CFTC-hosted PDF titled "WIP Copy of Kalshi Klear Rulebook v1.2" (cftc.gov, May 2025). None opened.
- *Read status:* search summary only.
- *What it argues:* the summary reports a February 2026 market on whether Ali Khamenei would step down as Iran's Supreme Leader, with roughly 54 million dollars in volume before his reported death on 28 February; Kalshi invoked a death provision that settles at the last traded price before the death. It then reports that Kalshi notified the CFTC of a codified death-settlement rule (which can roll back to the price before rumors circulated) and began refunding trading fees on disputed settlements, after complaints, class actions and Congressional attention. The summary does not give dates for the codification or the refund policy.
- *Bearing:* **supports** the essay's argument about contract wording and mid-life rule change, if confirmed. The sequence (market trades, dispute occurs, rule is written afterward) is exactly the mid-market clarification the brief asked about, and it is the single most useful D2 lead. [verify] against the Kalshi rulebook, the CFTC self-certification filing and a news report that quotes the contract terms.

### B4. Regulatory and litigation facts (D3)

**state_litigation_secondary** — WebSearch summary over dlapiper.com (September 2026 tracker), theblock.co (26 September 2026), coindesk.com (28 August 2026), law360 and hklaw.com. Not opened.
- *Read status:* search summary only.
- *What it argues:* the Third Circuit held for Kalshi on preemption; the Ninth Circuit ruled 3-0 against Kalshi on 28 August 2026 (KalshiEX, LLC v. Assad); a Sixth Circuit panel on 25 September 2026 (a Friday, per the summary; the Block article is dated 26 September) held that Kalshi's sports contracts fall under state gambling oversight in Ohio and Tennessee, widening a circuit split. States named as plaintiffs or enforcers include Washington, Massachusetts, Michigan, Nevada, Connecticut, and Arizona (criminal charges); Kalshi has sued Nevada, New Jersey, Maryland, Ohio, New York and Utah.
- *Bearing:* **complicates.** The essay's design critique does not depend on the outcome of the preemption fight, but the essay should not describe Kalshi as plainly lawful or plainly unlawful. [verify] each ruling against the opinion (court website or CourtListener) and give docket numbers.

**cftc_designation_secondary** — Same search set plus CRS LSB11441 (title only: "CFTC Issues Proposed Rule Regarding Prediction Markets"), regulatoryoversight.com (December 2025), and Packin et al. (below).
- *Read status:* search summary only; the CRS page was refused.
- *What it argues:* Polymarket acquired QCEX (reported price 112 million dollars, July 2025), obtained an Amended Order of Designation from the CFTC in November 2025 (the Dhenabayu abstract dates it 25 November 2025), and launched a US app on 3 December 2025, first under the sports category in the App Store. A CFTC proposed rule on prediction markets exists (CRS title only; date and content not seen). I have no fetched source for Kalshi's own designation date; the Bürgi et al. abstract says Kalshi "has operated as the only federally licensed prediction market in the United States" since 2021, and the Dhenabayu abstract treats Kalshi as regulated "since 2020". The two academic sources disagree on the year. [verify]
- *Bearing:* **complicates.** The platforms are now exchanges under federal supervision, so the essay can treat their interface choices as choices of a regulated venue, not as grey-market design.

**packin2026inside** — Packin, N. G., et al. (2026). Inside the odds. SSRN 6913339 (doi:10.2139/ssrn.6913339).
- *Read status:* abstract only (Consensus). Working paper.
- *What it argues:* state courts have "increasingly treated" these markets as unlicensed sports wagering; the CFTC announced in February 2026 that it would defend federally regulated platforms against state enforcement; platforms act as de facto regulators of insider trading through private rulebooks (a January 2026 Polymarket trade before the detention of Nicolas Maduro is the triggering episode). In June 2026 Kalshi announced employment verification for traders in high-risk markets and a six-factor risk score for each proposed market. An LLM analysis of comments on the CFTC's 2024 proposed rule finds that neither regulators nor commenters engaged with insider-trading risk. The authors conclude that disclosure-centered approaches that assume informed, self-policing participation are undermined.
- *Bearing:* **supports.** The last point bears directly on the essay: the legal frame assumes participants can read and police the market.

**packin2026science** — Packin, N. G., et al. (2026). Prediction markets as a public health threat. *Science*. doi:10.1126/science.aee3932.
- *Read status:* abstract only (one line: "Scientific framing, gambling-like design, and regulatory gaps create risks of a new behavioral addiction and democratic manipulation.").
- *Bearing:* **supports** the gambling-design framing; peer-reviewed venue, but I saw one sentence. Do not quote beyond it.

**johnson2025addiction** — Johnson, B., et al. (2025). Prediction markets: an emerging form of gambling? *Addiction*. doi:10.1111/add.70272.
- *Read status:* abstract only (a short letter, text visible in Consensus).
- *What it argues:* prediction markets resemble gambling in function; because they sit under the CFTC and are regulated as investments, state harm-minimization measures (self-exclusion registers, advertising limits, in-product safer-gambling tools) generally do not apply. The letter names 24/7 mobile access, push notifications, easy deposits and short event cycles that permit loss chasing as risk factors.
- *Bearing:* **supports.** This is the closest peer-reviewed text to a design critique, and it lists interface features (notifications, mobile, deposits) as hazards. It is an argument, not a measurement.

### B5. Volume mix and price quality (D3)

**volume_mix_secondary** — WebSearch summary over pewresearch.org (23 September 2026, "Prediction markets' trading volume doubled between May and July, largely driven by sports"), trmlabs.com, defirate.com, statista.com and others. None opened.
- *Read status:* search summary only.
- *What it argues:* Sports contracts have made up about 80 percent of Kalshi volume since July 2024. Combined platform volume rose from about 26 billion dollars in May 2026 to about 53 billion in July; in June and July sports trading topped 58 billion on Kalshi and neared 22 billion on Polymarket (the World Cup period). For Polymarket, 2 September to 1 October 2026: sports 1.9 billion (40.6 percent), politics 263 million (5.7 percent). Sports is described as the largest Polymarket category at 39 to 40 percent overall. Kalshi volume for August 2026 is given as 38.67 billion dollars.
- *Bearing:* **supports** the essay if the "80 percent" and the Pew figures hold: the products people use most are sports contracts, not decision markets about elections or policy. The Pew item is the best candidate for a citable secondary source; fetch it. [verify] Note that the summary's own numbers do not reconcile (the June and July sports figures sum to about 80 billion, above the combined 47.7 plus 53 billion total only if volume is counted differently across sources), so the unit (notional versus dollars traded, one or both platforms) must be checked.

**cardozo2026flb** — Cardozo, M., et al. (2026). The favorite-longshot bias in prediction markets: evidence from Polymarket. arXiv 2609.12878.
- *Read status:* abstract only. Preprint.
- *What it argues:* using 588 million trades by 2.48 million accounts, purchases below 10 cents lose 19.3 cents per dollar and purchases at or above 90 cents earn 0.83 cents; the result changes sign with how contracts are grouped (longshots lose 6.3 cents per dollar when each contract is weighted equally, gain 4.1 cents when grouped by parent event); the two-sided pattern is robust in Crypto and Politics but "surprisingly absent in Sports".
- *Bearing:* **complicates.** Sports, the largest category, does not show the favorite-longshot pattern in this sample, so the essay should not use that bias as a general claim about prices on these platforms.

**burgi2026makers** — Bürgi, C., et al. (2026). Makers and takers: the economics of the Kalshi prediction market. CESifo Working Paper. doi:10.65864/s9kc4p0b7t.
- *Read status:* abstract only. Working paper.
- *What it argues:* on over 300,000 Kalshi contracts, prices are informative and improve toward close, but low-price contracts win far less often than break-even and high-price contracts earn small positive returns; makers (posting offers) are relatively well informed and takers accept their offers.
- *Bearing:* **supports** and **complicates.** Prices are informative, which cuts against any claim that the numbers are noise, but who gets the edge depends on order type, an interface decision.

**le2026decomposing** — Le, N. (2026). Decomposing crowd wisdom: domain-specific calibration dynamics in prediction markets. arXiv 2602.19520.
- *Read status:* abstract only. Preprint.
- *What it argues:* on 353 million trades across 429,000 binary contracts on Kalshi and Polymarket, calibration varies by domain, time to resolution and trade size; political markets show persistent underconfidence (prices compress toward 50 percent), replicated on Polymarket. "A price's meaning depends on what, when and how much is traded."
- *Bearing:* **supports** the point that a displayed price (cents or percent) is not a plain probability, though the paper's own bootstrap suggests about half the raw slope variation is estimation noise.

**moshrefi2026parlays** — Moshrefi, N. (2026). Prices, probabilities, and parlays: systematic bias in sports prediction markets. *2026 IEEE CIFEr*. doi:10.1109/cifer67845.2026.11692409.
- *Read status:* abstract only. Refereed conference paper.
- *What it argues:* on 23 million Kalshi moneyline trades, calibration holds mid-life but departs near expiry (a step-like curve in the final ten minutes), and cross-game parlays are overpriced relative to the product of leg prices, with overpricing growing in leg count.
- *Bearing:* **supports.** Combos and last-minute trading are product features, and the paper finds a markup there. This is the strongest hint of a design-level cost in sports contracts.

**dubach2026anatomy** — Dubach, P. D. (2026). The anatomy of a decentralized prediction market: microstructure evidence from the Polymarket order book. arXiv 2604.24366.
- *Read status:* abstract only. Preprint.
- *What it argues:* a 52-day archive of the order-book feed shows a median self-counterparty wash share of 1 percent with a 22 percent upper tail, a longshot spread premium, and that trade direction inferred from the public feed matches on-chain truth in only about 59 percent of buckets.
- *Bearing:* **complicates.** Wash trading is present but small at the median; the essay should not lean on a wash-trading claim for Polymarket. The 59 percent finding is a warning against any claim built on feed-inferred direction.

**whelan2023prices** — Whelan, K. (2023). On prices and returns in commercial prediction markets. *Quantitative Finance*. doi:10.1080/14697688.2023.2257756.
- *Read status:* abstract only. Peer reviewed.
- *What it argues:* with fees in the model, post-fee loss rates depend negatively on the probability of the event backed, a favorite-longshot pattern created by the fee itself, even if the fee schedule is generous to low-probability contracts.
- *Bearing:* **supports** the fee-as-design point; pairs with the Kalshi fee formula above.

**dhenabayu2026benford** — Dhenabayu, R. (2026). Does CFTC regulation reduce prediction market anomalies? A Benford's law and DiD analysis. *Jurnal Media Computer Science*. doi:10.37676/jmcs.v5i3.11900.
- *Read status:* abstract only. Low-prominence journal.
- *What it argues:* no significant effect of the 25 November 2025 CFTC amended order on Polymarket volume anomalies (beta 0.0038, p 0.073), with Kalshi as control. Used here only for the date and as a null result; treat the method with caution.

**baker2026retail** — Baker, S. R., et al. (2026). Retail betting markets. *Annual Review of Financial Economics*. doi:10.3386/w35520.
- *Read status:* abstract only.
- *What it argues:* it reviews convergence of sports betting, prediction markets and retail options, with attention to market design, behavioral drivers and regulatory arbitrage.
- *Bearing:* **supports** the framing of these products as a family of retail betting designs; check the full text for platform-specific design claims.

**Unused hits.** Page (2013) on calibration, Ottaviani and Sorensen on favorite-longshot explanations, and the other FLB theory papers from Consensus are background to Facet C or E (price interpretation) and are not repeated here. Diercks et al. (2026) on Kalshi macro markets is a counterweight (Kalshi forecasts as a useful benchmark for macro expectations) and is abstract-only; I list it in the .bib for the essay's fair-hearing paragraph.

---

## (c) Synthesis and verification list

**D1. Presentation.** Nothing here is verified. The three leads are the Kalshi fee formula (secondary), the Polymarket fee claim (secondary and doubtful), and one preprint on how users read Kalshi charts. The brief's checklist items (price as cents or percent, order book versus simple buy and sell, default order type, mobile app, categories, notifications, share and leaderboard features) all remain open. The academic abstracts imply cents-denominated prices ("purchases below 10 cents") and an order-book microstructure on both platforms, but that is an inference from the papers' vocabulary.

**D2. Resolution.** The picture from secondary sources is that resolution on Polymarket runs through a token-holder vote after a bond-backed proposal, and on Kalshi through the rulebook, with the rule sometimes written or sharpened after a controversial settlement. Both are consistent with the essay's thesis that the contract terms, not the screen, decide the user's outcome. Only the Khamenei and Strategy cases are concrete enough to use, and both need primary support.

**D3. Structure.** The sources agree that the US legal status is contested (circuit split), that sports dominate volume, and that Polymarket re-entered the US through a CFTC-registered acquisition in late 2025. They disagree or are silent on Kalshi's designation date.

**Surprises that bear on the thesis.**
1. If the Cardozo result holds, sports contracts, the largest segment, show no favorite-longshot bias on Polymarket. The essay should not claim systematic mispricing across categories.
2. The "decision market" frame is weakened by volume mix: the sources suggest most volume is sports, so the essay's target may be better named as sports-style event betting presented as a forecasting instrument.
3. Wash trading looks small at the median (1 percent), so skip that argument.

**[verify] list (do not state as fact until fetched).**
- Kalshi: price display (cents versus percent), order types and defaults, fee schedule document and effective dates, mobile app features, notification settings, share and leaderboard features, categories list.
- Polymarket: price display, order types, fee policy for the international site and for Polymarket US, notifications, share and leaderboard features, categories, UMA bond size and dispute timeline from the platform's own docs.
- Kalshi rulebook: death-settlement rule text and date, source-agency language, amendment history; the CFTC self-certification filings.
- Polymarket disputes: Ukraine minerals market and Strategy Bitcoin market details, the 1,150 disputed-market count, and the whale vote figures.
- Courts: Third Circuit, Ninth Circuit (KalshiEX v. Assad, 28 August 2026) and Sixth Circuit (late September 2026) opinions with docket numbers; list of state actions.
- CFTC: Kalshi designation date; November 2025 amended order for Polymarket (QCEX); the proposed rule on prediction markets (CRS LSB11441: date and content); the February 2026 CFTC statement that it would defend platforms.
- Volume: the Pew Research piece (23 September 2026), the 80 percent sports share for Kalshi, the Polymarket category split, the monthly volumes, and the unit used.
- Robinhood's 10-Q (June 2026) for any prediction-market disclosure.
- Scholar Gateway: not reachable; rerun when identity resolution works.
- The Consensus DOIs for arXiv items use an unfamiliar pattern (10.48550/arxiv.NNNN.NNNNN); confirm the arXiv IDs resolve before citing.

**Unblocking.** One fix covers most of the list: allow the egress proxy to reach docs.polymarket.com, polymarket.com, kalshi.com, help.kalshi.com, docs.kalshi.com, cftc.gov, courtlistener.com, pewresearch.org and sec.gov, then rerun this facet. See the environment network documentation page for how an owner changes the allowed hosts.
