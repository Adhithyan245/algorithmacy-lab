# A: Prediction-market theory and decision use

*Facet A of the Decision Experience Design (DXD) Part 3 literature base ("Decision markets as poor decision experience design"). Agent-drafted on 2026-10-03. The author has not reviewed it, and none of the text below is the author's.*

What this facet covers. The theory of what prediction markets are for (information aggregation and forecasting accuracy), the conditions under which a market price can be read as a probability (risk preferences, belief heterogeneity, favorite-longshot bias, fees, thin markets, manipulation), the evidence on how decision-makers use prices (corporate and policy use, futarchy and decision markets), and what a market asks a participant to do compared with what a decision-maker needs. The questions the synthesis answers are A1 to A3. A1: what does the literature claim prediction markets are for, and under what conditions does the price equal a probability? A2: is there evidence on how decision-makers actually use market prices as inputs to decisions? A3: what do the markets ask the participant to do (a trade, a position size, liquidity provision), versus what a decision-maker needs (a probability and a decision)?

Legend for read status. Every entry below was matched to a database record, in each case a Consensus record that carries the abstract, a DOI where one exists, and a stable Consensus URL. The Crossref and OpenAlex lookups the task specified were blocked by the session's egress policy (rows 14 to 16 of the search log), so no DOI was resolved against Crossref and no metadata was cross-checked against a second database. Read status is "abstract only" for every entry: I read the abstract text the Consensus record returned and nothing else. No full text was opened. Claims below are therefore limited to what an abstract says, and an abstract-only entry must not be quoted beyond its abstract. Bearing on the Part 3 argument is marked supports, complicates or refutes. Peer-review status: entries whose venue is arXiv or an SSRN or CESifo working-paper series are flagged as preprints or working papers in the entry.

Author lists. Consensus truncates author lists to a first author and "et al." In the bib file I write "and others" in those cases. Where the task brief supplies a second author (Zitzewitz) I say so in the entry's note.

Sources not in the bib. Items I know of but did not match to a database record this session are in section (d), the [verify] list. They are not cited in the entries or the synthesis.

---

## (a) Search log

All searches ran on 2026-10-03. Hits is the count the source reported.

| # | Source | Exact query / request | Hits | Notes |
|---|---|---|---|---|
| 1 | Consensus `search` | `prediction markets information aggregation forecasting accuracy` | 20 | Surfaced Wolfers and Zitzewitz 2004, Berg et al. 2008, Atanasov et al. 2017 and 2022, Snowberg et al. chapter, Hanson et al. 2006, Deck et al. 2012 |
| 2 | Consensus `search` | `favorite-longshot bias prediction market prices as probabilities risk neutrality` | 20 | Surfaced Page et al. 2013, Gandhi et al. 2014, Whelan 2023, Snowberg and Wolfers working paper, He et al. 2016, Newall et al. 2021 review |
| 3 | Consensus `search` | `corporate internal prediction markets Google Ford Hewlett-Packard use in decision making` | 19 | Surfaced Cowgill et al. 2009 and 2014, Montgomery et al. 2013, Malone 2004, O'Leary 2013/2014/2015, Dianat et al. 2020, Ottaviani et al. 2007 |
| 4 | Consensus `search` | `The promise of prediction markets Arrow Science 2008` | 20 | Surfaced Arrow et al. 2008 (one-sentence abstract), Servan-Schreiber et al. 2004, Dreber et al. 2015, Nechepurenko 2026 |
| 5 | Consensus `search` | `futarchy decision markets conditional prediction markets for policy decisions` | 20 | Surfaced Hanson 2013, Chen et al. 2011, Teschner et al. 2017, Abramowicz 2003 and 2008 (book), Siemroth 2019, Weidener et al. 2025 |
| 6 | Consensus `search` | `interpreting prices as probabilities Manski Wolfers Zitzewitz heterogeneous beliefs prediction market` | 20 | Surfaced Manski 2006, Gjerstad 2004, Ottaviani et al. 2009, Bottazzi et al. 2019, Mantovani et al. 2025. Wolfers and Zitzewitz 2006 "Interpreting prices as probabilities" did not appear. |
| 7 | Consensus `search` | `superforecasters geopolitical forecasting tournament Tetlock Mellers accuracy` | 20 | Surfaced Mellers et al. 2014 and 2015, Tetlock and Gardner 2016, Tetlock et al. 2014, Moore et al. 2016, Atanasov et al. 2020. Only Mellers 2015 and the book are entered; the rest are tournament papers outside the market question. |
| 8 | Consensus `search` | `Polymarket Kalshi traders profits retail participants prediction market accuracy calibration liquidity` | 20 | Surfaced Le 2026, Burgi et al. 2026, Dubach 2026, Dudley et al. 2026, Adegbenro 2026, Saguillo et al. 2025 (arbitrage). Almost all 2026 preprints. No study of retail user behavior or user decision use. |
| 9 | Consensus `search` | `Rhode Strumpf manipulating political stock markets; thin markets and manipulation of prediction market prices` | 20 | Surfaced Rhode et al. 2006, Hanson et al. 2006 and 2009, Rasooly et al. 2025, Choo et al. 2022, Johnson et al. 2025 |
| 10 | Consensus `search` | `Kelly criterion optimal bet size prediction market traders position sizing bankroll` | 20 | Surfaced Thorp 2008, MacLean et al. 2010 and 2011, Baker et al. 2013, Meister 2024, Vecer 2026. Mostly sports-betting and finance work. |
| 11 | Consensus `search` | `do decision makers use prediction market forecasts adoption organizations barriers managers trust` | 20 | Surfaced Choo et al. 2022, Seemann et al. 2012, Buckley 2009 and 2015, Goel et al. 2010, Green and Armstrong 2007 (Delphi vs markets), Velasco et al. 2012 |
| 12 | Consensus `search` | `Hanson logarithmic market scoring rule automated market maker liquidity thin markets combinatorial information market design` | 20 | Surfaced Hanson 2003 and 2012, Chen et al. 2007/2008, Slamka et al. 2013, Berg et al. 2012 |
| 13 | Scholar Gateway `semanticSearch` | `Under what conditions do prediction market prices equal probabilities, given risk aversion, thin markets, and manipulation?` (topN 8) | 0 | Failed: `INVALID_QUERY: Could not resolve user identity from CONNECT`. Not retried; the same error hit Facet A of Part 2 on 2026-10-01. Scholar Gateway was not reachable. |
| 14 | Crossref `/works/{doi}` via curl and Python through the configured proxy | 43 DOIs (a draft list of the candidate entries as drawn from Consensus), one request each | 0 | All 43 failed with `CONNECT tunnel failed, response 403`. The proxy status endpoint recorded `connect_rejected ... gateway answered 403 to CONNECT (policy denial or upstream failure)` for host `api.crossref.org:443`. Per /root/.ccr/README.md, a 403 is an egress-policy denial; I did not retry or route around it. |
| 15 | OpenAlex `/works/doi:{doi}` via curl | 1 test DOI (10.1126/science.1157679) | 0 | `CONNECT tunnel failed, response 403`. Treated as the same policy denial; I did not make further OpenAlex calls. |
| 16 | Crossref `query.bibliographic` and OpenAlex `search` title queries for sources without a DOI in Consensus (Manski journal DOI; Wolfers and Zitzewitz 2006; Cowgill and Zitzewitz 2015 journal version; Snowberg and Wolfers published version; Rhode and Strumpf 2004/2013; Malone HBR DOI) | Not run | 0 | Blocked by the same policy as rows 14 and 15, so I did not issue them. These sources are in the [verify] list. |

---

## (b) Entries

Entries follow the facet's questions: purposes and accuracy (A1), the conditions under which price is a probability (A1), decision use (A2), and what the market asks of the participant (A3). In every entry the record line gives the DOI as Consensus reported it and the Consensus URL. The DOIs were not resolved against Crossref.


### B1. What markets are for, and how well they forecast (RQ-A1)

`wolfers2004prediction` | Wolfers, J., & Zitzewitz, E. (2004). *Prediction Markets*. Journal of Economic Perspectives.
- *Record:* DOI: 10.1257/0895330041371321. Consensus: https://consensus.app/papers/details/81c556c00fee5b5dafe76399254cb419/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Simple markets can aggregate dispersed information into forecasts of uncertain events. Market forecasts are typically fairly accurate and beat most moderately sophisticated benchmarks. Carefully designed contracts reveal the market's expectation of probabilities, means and medians. The paper also names market design issues and the domains where markets are most likely to help.
- *Bearing:* supports the claim that the literature's stated purpose is forecasting by aggregation. The abstract speaks of what 'carefully designed contracts' can yield, which sets up the A3 contrast with the contracts a retail platform lists. *Note:* Venue inferred from my knowledge of the DOI, not from the record, which lists 'Unknown Journal'; unverified. Volume and pages not checked.

`arrow2008promise` | Arrow, K., and others (2008). *The Promise of Prediction Markets*. Science.
- *Record:* DOI: 10.1126/science.1157679. Consensus: https://consensus.app/papers/details/51485fb753d5508b9ac2c64677b4641f/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* The record's abstract says that the ability of groups to make predictions is a potent research tool that should be freed of unnecessary government restrictions.
- *Bearing:* supports the advocacy reading: the article argues for permission, not for decision-maker design. Nothing in the abstract addresses how a decision-maker should use a price. I cannot say more without the full text. *Note:* Consensus gives a one-sentence abstract and a truncated author list.

`berg2008accuracy` | Berg, J. E., and others (2008). *Prediction Market Accuracy in the Long Run*. International Journal of Forecasting.
- *Record:* DOI: 10.1016/j.ijforecast.2008.03.007. Consensus: https://consensus.app/papers/details/01dc38dfc88d5c439cfc3e18d6da0a8f/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Across five US presidential elections (1988 to 2004), the Iowa Electronic Markets vote-share price was closer to the outcome than 964 polls 74% of the time, and significantly better in every election at horizons beyond 100 days.
- *Bearing:* supports the accuracy claim in a long-running election setting, the Iowa Electronic Markets. This is the evidence base the platform era inherits; the abstract does not describe stakes or market size. *Note:* Record lists 'Joyce E. Berg et al.'; I did not confirm Rietz as co-author from the record.

`atanasov2017distilling` | Atanasov, P., and others (2017). *Distilling the Wisdom of Crowds: Prediction Markets vs. Prediction Polls*. Management Science.
- *Record:* DOI: 10.1287/mnsc.2015.2374. Consensus: https://consensus.app/papers/details/8586986bbee753508ac70bd80195dea8/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In a randomized, two-season geopolitical tournament (more than 2,400 forecasters, 261 events), last-day market prices beat the simple mean of poll forecasts. Team polls aggregated with temporal decay, performance weighting and recalibration beat the market, most at the start of long-duration questions.
- *Bearing:* complicates the 'markets are best' claim and bears directly on A3. The competing instrument asks forecasters for a probability judgment scored by Brier score, not for a trade.

`atanasov2022crowd` | Atanasov, P., and others (2022). *Crowd Prediction Systems: Markets, Polls, and Elite Forecasters*. Proceedings of the 23rd ACM Conference on Economics and Computation.
- *Record:* DOI: 10.1145/3490486.3538265. Consensus: https://consensus.app/papers/details/14fa70bd731d594281339f220156ce09/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In a randomized experiment (more than 1,300 forecasters, 147 questions), a logarithmic market scoring rule market had 14% lower Brier scores than a continuous double auction market, with the gap largest for questions that drew few traders. The authors also compare elite small crowds with larger sub-elite crowds.
- *Bearing:* complicates: a continuous double auction, the architecture of an order-book platform, underperformed in thin markets. This is the nearest experimental evidence on the microstructure that Polymarket and Kalshi use, though neither platform is named in the abstract.

`mellers2015identifying` | Mellers, B., and others (2015). *Identifying and Cultivating Superforecasters as a Method of Improving Probabilistic Predictions*. Perspectives on Psychological Science.
- *Record:* DOI: 10.1177/1745691615577794. Consensus: https://consensus.app/papers/details/67208e5ba77f52509e6fe498bf0cf54a/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In the US intelligence-community forecasting tournaments, the winning strategy culled top performers each year into elite teams. Superforecasters stayed accurate across hundreds of questions. The authors credit cognitive style, task skills, motivation and enriched environments.
- *Bearing:* supports a contrast the essay can use: the Tetlock-line instruments train, team and score a person who states a probability. A market asks for something else (A3).

`tetlock2016superforecasting` | Tetlock, P., & Gardner, D. (2016). *Superforecasting: The Art and Science of Prediction*. Crown.
- *Record:* DOI: 10.5860/choice.196400. Consensus: https://consensus.app/papers/details/1323e41870e5581f8f988a24c22e7690/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record); the DOI resolves to a Choice review record of the book, so I did not treat it as the book itself.
- *What it argues:* The record's blurb says Good Judgment Project volunteers beat other benchmarks, competitors and prediction markets, and beat intelligence analysts with classified access, and that good forecasting involves gathering evidence, thinking probabilistically, working in teams, keeping score and admitting error.
- *Bearing:* supports the contrast with markets, but on the blurb only. The tournament papers (Mellers et al., Atanasov et al.) carry the evidence; I would not cite the book for a specific number. *Note:* Consensus publication year 2016; the DOI is the Choice review record. Publisher not given in the record; I did not add it.

`goel2010prediction` | Goel, S., and others (2010). *Prediction without Markets*. ACM conference proceedings (venue not given in the record).
- *Record:* DOI: 10.1145/1807342.1807400. Consensus: https://consensus.app/papers/details/7d03891235b1591f9d39d7858eaa0622/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Across thousands of sporting and movie events, the advantage of prediction markets over polls and statistical models is surprisingly small on squared error, calibration and discrimination. Nearly all predictive power comes from two or three parameters, so costs should be weighed against modest benefits.
- *Bearing:* complicates the accuracy claim by size, not sign, and supports the point that a market's edge over a cheap baseline can be small.

`stastny2018comparative` | Stastny, B. J., and others (2018). *Comparative Evaluation of the Forecast Accuracy of Analysis Reports and a Prediction Market*. Judgment and Decision Making.
- *Record:* DOI: 10.1017/s1930297500007105. Consensus: https://consensus.app/papers/details/a3577d5b6e5d5483bb7dd6b168624b26/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In an intelligence-community market, 99 event forecasts were closer to ground truth than probabilities imputed from 41 analysis reports, by 0.114 on average.
- *Bearing:* supports an organizational use case: a market beating written analysis. It is also an A2 data point, since analysts read reports and market prices side by side.


### B2. When a price is a probability: conditions, biases and manipulation (RQ-A1)

`manski2006interpreting` | Manski, C. F. (2006). *Interpreting the Predictions of Prediction Markets*. Economics Letters.
- *Record:* DOI: 10.3386/w10359. Consensus: https://consensus.app/papers/details/542774a10088575691d1a362b43450d6/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* If traders are risk-neutral price takers with heterogeneous beliefs, the price of an all-or-nothing contract reveals nothing about the dispersion of beliefs and only partly identifies their central tendency. Most traders believe more than the price when the price is above 0.5, and less when it is below. The mean belief lies in an interval whose midpoint is the equilibrium price.
- *Bearing:* supports the answer to A1. Even in the textbook case, price is not the probability in the strict sense: it is a point in an interval around the mean belief. The 'price equals probability' reading needs extra assumptions. *Note:* The DOI printed in the Consensus record (10.3386/w10359) is an NBER working-paper identifier, not the journal DOI. Not resolved against Crossref (blocked). Journal DOI is in the [verify] list.

`gjerstad2004risk` | Gjerstad, S. D. (2004). *Risk Aversion, Beliefs, and Prediction Market Equilibrium*. Working paper (series listed as 'Public Economics' in the record).
- *Record:* DOI: none in the record. Consensus: https://consensus.app/papers/details/e809a17dd35959e49fc5d5066d01f6e5/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Replying to Manski, the paper shows that both risk aversion and the distribution of beliefs shape the equilibrium price. For relative risk aversion near empirical estimates and plausible belief distributions, the price is very near the traders' mean belief.
- *Bearing:* complicates Manski: the gap between price and mean belief is small under plausible parameters. Together the two papers say the condition is parametric, not guaranteed. *Note:* No DOI in the record. Series name taken from the record; unverified.

`ottaviani2009aggregation` | Ottaviani, M., and others (2009). *Aggregation of Information and Beliefs: Asset Pricing Lessons from Prediction Markets*. SSRN working paper.
- *Record:* DOI: 10.2139/ssrn.1447369. Consensus: https://consensus.app/papers/details/508ba02cc4a55358adab05addaa26931/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In a binary market where risk-neutral traders have heterogeneous priors and limited budgets, the rational-expectations price underreacts to information. The effect matches a favorite-longshot bias and grows with belief heterogeneity.
- *Bearing:* supports: a favorite-longshot pattern can arise with risk-neutral traders, so price compression toward 50% need not signal irrationality, and it still breaks 'price equals probability'. *Note:* Preprint. The record gives 'M. Ottaviani et al.'.

`page2013prediction` | Page, L., and others (2013). *Do Prediction Markets Produce Well-Calibrated Probability Forecasts?*. not given in the record.
- *Record:* DOI: 10.1111/j.1468-0297.2012.02561.x. Consensus: https://consensus.app/papers/details/717a56cf07795fb69a9bee74865e18bd/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Time to expiration should push prices toward a favorite-longshot bias, and a large transaction dataset confirms it. Markets are reasonably well calibrated near expiry and significantly biased for events further out. The miscalibration is exploitable only by traders with a low discount rate.
- *Bearing:* supports a condition that bears on platform contracts: long-dated contracts tie up capital, so price carries a time-value wedge. *Note:* Consensus lists 'Unknown Journal'.

`gandhi2014belief` | Gandhi, A. J., and others (2014). *Does Belief Heterogeneity Explain Asset Prices: The Case of the Longshot Bias*. The Review of Economic Studies.
- *Record:* DOI: 10.1093/restud/rdu017. Consensus: https://consensus.app/papers/details/af458fe0e60f5b84b7aabdf980eb62cc/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Belief differences alone produce a longshot bias in a market for Arrow-Debreu securities. Estimation on betting data finds a two-type population: mostly traders with nearly correct beliefs (70%) and noise traders with dispersed beliefs. The belief model beats risk-love and prospect-theory explanations.
- *Bearing:* supports: the bias is a property of who trades, which is a participant-mix condition, not a constant of the instrument.

`snowberg2007explaining` | Snowberg, E., & Wolfers, J. (2007). *Explaining the Favorite-Longshot Bias: Is It Risk-Love or Misperceptions?*. Working paper (NBER series per Consensus).
- *Record:* DOI: none in the record. Consensus: https://consensus.app/papers/details/3586805a3c575c0baa383d5b2fa03de6/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Tests on compound bets in horse-race pools favor probability misperception (a prospect-theory pattern) over risk-love as the source of the favorite-longshot bias. The paper also finds the bias too small to yield profit opportunities.
- *Bearing:* supports: the bias is a robust, small distortion in betting markets, and one explanation is how participants perceive small probabilities. *Note:* Working-paper version only. The record's author string reads 'Erik C. Snowberg et al.'; Wolfers is named as an author because the record's acknowledgment text says 'Wolfers gratefully acknowledges' support; the author field itself reads 'Erik C. Snowberg et al.'. A published version exists per my recollection; see [verify].

`whelan2023prices` | Whelan, K. (2023). *On Prices and Returns in Commercial Prediction Markets*. Quantitative Finance.
- *Record:* DOI: 10.1080/14697688.2023.2257756. Consensus: https://consensus.app/papers/details/cf9a58a3402057d8a44ddb2dcadc11e3/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Starting from a model where price equals the true probability without fees, adding the fees that commercial markets charge puts low-probability contract prices below the true probability and produces a favorite-longshot pattern in post-fee loss rates. The result holds even if the operator makes the fee schedule more generous to low-probability contracts.
- *Bearing:* supports a platform-specific condition for A1: on a fee-charging commercial market, the quoted price is not the probability even in the model's benign case.

`bottazzi2019far` | Bottazzi, G., and others (2019). *Far from the Madding Crowd: Collective Wisdom in Prediction Markets*. Quantitative Finance.
- *Record:* DOI: 10.1080/14697688.2019.1622285. Consensus: https://consensus.app/papers/details/2ba448474319569a88039b7ff9f7138c/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In a repeated market with fractional-Kelly traders holding heterogeneous beliefs, prices generally do not converge to the true probabilities and are not maximum likelihood estimators of them. When more than one trader survives, the average price still approximates the true probability with less information loss than any individual belief.
- *Bearing:* complicates: price is a good summary under survival conditions and not a point estimate. It also connects position sizing (A3) to what the price means (A1).

`mantovani2025when` | Mantovani, M., and others (2025). *When Do Prediction Markets Return Average Beliefs? Experimental Evidence*. Games and Economic Behavior.
- *Record:* DOI: 10.1016/j.geb.2025.12.004. Consensus: https://consensus.app/papers/details/1e238e7f232759ec974c9f7bb2341200/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Prices equal the average belief only under restrictive assumptions about risk preferences and the information equilibrium. In a lab, risk preferences did not significantly affect prices, and double-auction prices sat closer to average beliefs than call-auction prices. Traders updated toward observed prices, not toward the true state.
- *Bearing:* supports the condition list and adds a reflexive element: participants who read the price move toward it, which matters for any decision-maker who also reads it.

`le2026decomposing` | Le, N. (2026). *Decomposing Crowd Wisdom: Domain-Specific Calibration Dynamics in Prediction Markets*. arXiv preprint.
- *Record:* DOI: 10.48550/arxiv.2602.19520. Consensus: https://consensus.app/papers/details/6a5ca47afd1e5541ad1635ee142e0041/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Using 353 million trades across 429,000 binary contracts on Kalshi and Polymarket, the paper finds that calibration varies by domain, time to resolution and trade size. The most robust pattern is persistent underconfidence in political markets, where prices compress toward 50%. The author concludes that a price's meaning depends on what, when and how much is traded.
- *Bearing:* supports the central A1 answer for the two platforms the essay targets: the price-to-probability map is conditional and varies by contract type. The strongest platform-specific evidence found, but a preprint. *Note:* Preprint, not peer reviewed.

`burgi2026makers` | Bürgi, C., and others (2026). *Makers and Takers: The Economics of the Kalshi Prediction Market*. CESifo Working Papers.
- *Record:* DOI: 10.65864/s9kc4p0b7t. Consensus: https://consensus.app/papers/details/473d4da9dd305c7ea2b8959f52fb5ff7/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* On more than 300,000 Kalshi contracts, prices are informative and improve toward close, but show a clear favorite-longshot bias: low-price contracts win too rarely to break even, and high-price contracts win more often and earn small positive returns. A maker-taker framework fits the quote-driven microstructure.
- *Bearing:* supports: on Kalshi the price is informative, but a longshot contract is systematically overpriced for the participant who takes it. *Note:* Working paper. The DOI prefix (10.65864) is unfamiliar to me; I could not resolve it against Crossref (blocked), so it is recorded as the Consensus record states it and listed under [verify].

`dubach2026anatomy` | Dubach, P. D. (2026). *The Anatomy of a Decentralized Prediction Market: Microstructure Evidence from the Polymarket Order Book*. arXiv preprint.
- *Record:* DOI: 10.48550/arxiv.2604.24366. Consensus: https://consensus.app/papers/details/56d5e9eee36056d58b99fe88b2dc26e7/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* A tick-level archive of Polymarket's order book (600 markets, 52 days) yields eight stylized facts, including a longshot spread premium, a depth profile closer to uniform than top-of-book, and a self-counterparty wash share with a 1% median and a 22% upper tail. Trade direction inferred from the public feed matches on-chain truth in only about 59% of buckets.
- *Bearing:* supports A3: it documents what the participant actually faces (spread, depth, wash trades). It is also a caution that even researchers misread trade direction from the public feed. *Note:* Preprint, not peer reviewed.

`dudley2026infectious` | Dudley, C., and others (2026). *Prediction Markets Underperform Simple Baselines for Infectious Disease Forecasting*. arXiv preprint.
- *Record:* DOI: 10.48550/arxiv.2605.11220. Consensus: https://consensus.app/papers/details/f68d7e6397855efa9c04d544e1b145be/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Polymarket forecasts for US influenza hospitalizations and measles cases fail to beat standard benchmarks. The FluSight ensemble dominates, the best combination puts zero weight on the markets, and the authors name probability mass on impossible outcomes and low volume as sources of inefficiency.
- *Bearing:* complicates the accuracy claim for a decision-relevant public-health domain on a named platform; scope is limited to two settings. *Note:* Preprint, not peer reviewed.

`rhode2006manipulating` | Rhode, P., and others (2006). *Manipulating Political Stock Markets: A Field Experiment and a Century of Observational Data*. Natural Field Experiments (record's venue).
- *Record:* DOI: none in the record. Consensus: https://consensus.app/papers/details/bd93e2a1830256a288883830b182b9e2/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Across Wall Street markets (1880 to 1944), the Iowa Electronic Markets and TradeSports, speculative attacks initially moved prices but the changes were quickly undone. The authors find little evidence of systematic manipulation beyond short periods.
- *Bearing:* supports the benign side of the manipulation condition, in large and mid-sized markets. *Note:* No DOI in the record. The record gives 'P. Rhode et al.'; The record's author field is truncated.

`hanson2006information` | Hanson, R. D., and others (2006). *Information Aggregation and Manipulation in an Experimental Market*. Journal of Economic Behavior and Organization.
- *Record:* DOI: 10.1016/j.jebo.2004.09.011. Consensus: https://consensus.app/papers/details/16cf2bb57d1d5ce988d4a6776b4e137a/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In an experimental market, manipulators could not distort price accuracy, because subjects without a manipulation incentive offset the bias by shifting the threshold at which they accept trades.
- *Bearing:* supports the benign view in a lab.

`deck2012affecting` | Deck, C. A., and others (2012). *Affecting Policy by Manipulating Prediction Markets: Experimental Evidence*. Journal of Economic Behavior and Organization.
- *Record:* DOI: 10.1016/j.jebo.2012.10.017. Consensus: https://consensus.app/papers/details/e864ebf6269c5093914c1c47e985cc0f/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In the lab, single-minded, well-funded manipulators can destroy a market's ability to aggregate informative prices and mislead forecasters who rely on them, although bids and asks stay informative.
- *Bearing:* complicates the benign view when the price is used to steer a decision, which is the A2 setting.

`rasooly2025manipulable` | Rasooly, I., and others (2025). *How Manipulable Are Prediction Markets?*. working paper.
- *Record:* DOI: none in the record. Consensus: https://consensus.app/papers/details/aa7b6ce59cbb578ca350c41c7e265783/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* A field experiment that randomly shocked prices in 817 markets found that the effects of the trades remained visible 60 days later, though they faded. Markets with more traders, higher volume and an external probability source were harder to manipulate.
- *Bearing:* complicates: this is the most direct field evidence found on manipulability, and it points the opposite way from the older field results. It names thin markets as the weak case. *Note:* No DOI or venue in the record. Treat as a preprint.


### B3. How decision-makers use prices (RQ-A2)

`cowgill2014corporate` | Cowgill, B., & Zitzewitz, E. (2014). *Corporate Prediction Markets: Evidence from Google, Ford, and Firm X*. Proceedings of the Fifteenth ACM Conference on Economics and Computation.
- *Record:* DOI: 10.1145/2600057.2602901. Consensus: https://consensus.app/papers/details/e301c33e1daa515793c3f8324d1c3b1b/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* The abstract states that businesses and policymakers have been slow to adopt prediction markets in decision making. In data from Google, Ford and a private materials firm, the markets were relatively efficient despite thinness and weak incentives, and cut mean squared error by as much as 25% against experts. The notable inefficiency was optimism bias, which shrank as experienced traders learned and weaker ones left.
- *Bearing:* supports A2 in two directions. Accuracy is good in internal markets, and the abstract itself records that adoption lagged. It does not report what managers did with the prices. *Note:* The record lists 'Bo Cowgill et al.'; Zitzewitz is added from the task brief. The journal version (Review of Economic Studies) was not found; see [verify].

`cowgill2009using` | Cowgill, B., and others (2009). *Using Prediction Markets to Track Information Flows: Evidence from Google*. book chapter (Springer; chapter DOI as in record).
- *Record:* DOI: 10.1007/978-3-642-03821-1_2. Consensus: https://consensus.app/papers/details/262ebc1fd8f7595ca2501982db85c275/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Google ran the largest corporate prediction-market experiment the authors knew of from 2005. Participants were not typical of the workforce, and participation and success skewed toward engineers and quantitative staff.
- *Bearing:* complicates: the 'crowd' in a corporate market is a self-selected, technical subgroup, so the price is that subgroup's belief.

`montgomery2013experience` | Montgomery, T. A., and others (2013). *Experience from Hosting a Corporate Prediction Market: Benefits beyond the Forecasts*. Proceedings of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.
- *Record:* DOI: 10.1145/2487575.2488212. Consensus: https://consensus.app/papers/details/96f5e16c10e65168aa4b8151a3f4827c/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Ford ran one of the largest corporate markets known, asking about vehicle features, sales volumes, take rates and pricing. The authors report strong and weak correlations between predictions and outcomes, and describe side benefits: comments, price changes over time, ability to overcome bureaucratic limits, and filling gaps in corporate knowledge.
- *Bearing:* supports A2 with an insider account. The benefits listed are largely about information flow, not about a decision rule tied to the price.

`malone2004bringing` | Malone, T. (2004). *Bringing the Market Inside*. Harvard Business Review.
- *Record:* DOI: none in the record. Consensus: https://consensus.app/papers/details/a974d33c0a31537eb69ae1dbe9d9c9d7/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* The abstract says Hewlett-Packard tried a system where employees traded predictions about printer sales and that the markets predicted actual sales much more accurately than official HP forecasts. It also describes BP's internal emissions-permit trading.
- *Bearing:* supports the HP case as reported in a secondary source. I did not locate the primary HP study (see [verify]). *Note:* The DOI in the Consensus record (10.4135/9781452229805.n74) is a SAGE book-chapter DOI and does not match an HBR article, so I left the doi field empty. Record gives initial only.

`ottaviani2007outcome` | Ottaviani, M., and others (2007). *Outcome Manipulation in Corporate Prediction Markets*. Journal of the European Economic Association.
- *Record:* DOI: 10.1162/jeea.2007.5.2-3.554. Consensus: https://consensus.app/papers/details/1be7113a259b5b399450f3fc98474c6b/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* The paper gives a framework for markets in corporate decision making and characterizes the equilibrium amount of outcome manipulation and its effect on prices.
- *Bearing:* complicates: when the price drives a decision, those who can change the outcome are a new manipulation channel.

`choo2022manipulation` | Choo, L., and others (2022). *Manipulation and (Mis)trust in Prediction Markets*. Management Science.
- *Record:* DOI: 10.1287/mnsc.2021.4213. Consensus: https://consensus.app/papers/details/e469008d310e536ebe344ed83e2598e0/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In an experiment on managers' willingness to base decisions on market information, managers under-used the information in prices when manipulators were present, and mere suspicion of manipulation eroded trust and led to worse policies even without manipulation.
- *Bearing:* supports A2 directly: this is the clearest experimental evidence found on how decision-makers use a price, and it shows trust, not accuracy, governing use.

`dianat2020improving` | Dianat, A., and others (2020). *Improving Decisions with Market Information: An Experiment on Corporate Prediction Markets*. Experimental Economics.
- *Record:* DOI: 10.1007/s10683-020-09654-y. Consensus: https://consensus.app/papers/details/3b67996c41865dcd8c7c701262b0c78b/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In a lab setting where a manager takes a state-dependent decision using what workers reveal by trading, the theoretically superior market design did worse for manager decisions without top-down advice to participants. With advice, manager decisions improved and both designs performed alike.
- *Bearing:* supports A2 and A3: whether a price helps a decision depends on how participants are told to use the market, and a market's theoretical merits did not carry into decisions. *Note:* A correction notice exists (10.1007/s10683-021-09711-0) per Consensus; I did not read it.

`siemroth2019when` | Siemroth, C. (2019). *When Can Decision Makers Learn from Financial Market Prices?*. Journal of Money, Credit and Banking (per record).
- *Record:* DOI: 10.2139/ssrn.2980611. Consensus: https://consensus.app/papers/details/7dc0a007ea335ff5a7faf4bd8b239e4d/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* When policy affects asset values, traders may withhold information, and full revelation can be impossible because pricing becomes a self-defeating prophecy. The paper gives a necessary and sufficient condition for revealing equilibria and says some corporate markets are ill-designed and punish traders for revealing information.
- *Bearing:* complicates A2 in theory: using a price to decide changes what the price says. Relevant to any decision-maker who acts on a market that bets on the action. *Note:* The DOI is the SSRN working-paper identifier; the journal attribution is the record's.

`hanson2013vote` | Hanson, R. D. (2013). *Shall We Vote on Values, But Bet on Beliefs?*. Journal of Political Philosophy.
- *Record:* DOI: 10.1111/jopp.12008. Consensus: https://consensus.app/papers/details/6b73f08852f750618b703f9c6ff2cd20/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Futarchy: elected representatives define a measure of national welfare, and speculators say which policies will raise it. The paper works through thirty design issues and gives a specific proposal.
- *Bearing:* supports the claim that the strongest decision-use proposal is a design, not an observed practice. It assigns the trader the job of predicting the welfare measure conditional on policy.

`predmarketsdss2003` | (author field blank in the record) (2003). *Prediction Markets as Decision Support Systems*. Information Systems Frontiers 5(1), 79 to 93.
- *Record:* DOI: none in the record. Consensus: https://consensus.app/papers/details/96fa24354c9b53c596e8eb1b170ea4bb/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Using Iowa Electronic Markets conditional contracts from 1996, the paper shows how conditional markets (vote share given a nominee) could support decisions: Republicans could have inferred that Dole was a weak candidate.
- *Bearing:* supports A2 as an illustration of the decision-support idea, not as evidence of use. *Note:* The Consensus record has no author or DOI; the title field carries the journal citation. Attribution is withheld until checked (see [verify]).

`abramowicz2003information` | Abramowicz, M. (2003). *Information Markets, Administrative Decisionmaking, and Predictive Cost-Benefit Analysis*. University of Chicago Law Review.
- *Record:* DOI: 10.2139/ssrn.430640. Consensus: https://consensus.app/papers/details/d1f392e0cd785b04841dff9c46f046d2/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Written after the cancelled DARPA FutureMAP project, the article assesses whether information markets could help administrative agencies and concludes they could discipline agency predictions if hurdles such as manipulation are overcome. It proposes a predictive cost-benefit analysis in which a market predicts the result of a later retrospective analysis.
- *Bearing:* supports A2 with the main policy-use case on record: the one federal experiment named, FutureMAP, ended in a controversy that led to its cancellation (per the record), which is evidence about acceptance. *Note:* DOI is the SSRN identifier.

`chen2011decision` | Chen, Y.-L., and others (2011). *Decision Markets with Good Incentives*. book chapter (Springer; as in record).
- *Record:* DOI: 10.1007/978-3-642-25510-6_7. Consensus: https://consensus.app/papers/details/852d795058e75ad1ad3061a7bf553467/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Only the chosen action's prediction can be scored, so experts may be tempted to mislead a decision-maker. The authors construct incentive-compatible decision markets that require the decision-maker to risk taking every available action.
- *Bearing:* complicates A3: for a decision market to elicit honest probabilities, the decision-maker must give up deterministic choice.

`teschner2017manipulation` | Teschner, F., and others (2017). *Manipulation in Conditional Decision Markets*. Group Decision and Negotiation.
- *Record:* DOI: 10.1007/s10726-017-9531-0. Consensus: https://consensus.app/papers/details/9bd99f1ad973532ea97da1bd9274b602/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Because markets on non-executed decisions are void, manipulation is costless ex post. In online experiments, manipulation occurred only when a trader was alone, had enough power to move prices, and the decision tracked prices closely. A second trader eliminated it.
- *Bearing:* complicates the manipulation worry: it is conditional on market thinness and decision determinism, which a decision-maker could design around. *Note:* Consensus returns this record twice with identical content.

`buckley2015harnessing` | Buckley, P. (2015). *Harnessing the Wisdom of Crowds: Decision Spaces for Prediction Markets*. Business Horizons.
- *Record:* DOI: 10.1016/j.bushor.2015.09.003. Consensus: https://consensus.app/papers/details/add97cf562ed5602873ac868e913984f/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Prediction markets suit some decisions and contexts and not others. The article offers a framework for deciding where an organization should deploy them.
- *Bearing:* supports: the organizational literature itself says use is conditional on the decision type. *Note:* Record lists 'P. Buckley'.

`seemann2012influences` | Seemann, T., and others (2012). *Influences on the Trust in Prediction Markets*. The Journal of Prediction Markets.
- *Record:* DOI: 10.5750/jpm.v3i2.459. Consensus: https://consensus.app/papers/details/78bf3258c5125e82b995b1c065951cbb/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Many organizations remain reluctant to use prediction markets, and trust in results is a key obstacle. In surveys from six experimental markets, participants who were highly engaged and found trading exciting and entertaining trusted the results more.
- *Bearing:* complicates: trust in a market price tracks enjoyment of trading, a trader's attitude rather than a decision-maker's evidence.

`oleary2015user` | O'Leary, D. E. (2015). *User Participation in a Corporate Prediction Market*. Decision Support Systems.
- *Record:* DOI: 10.1016/j.dss.2015.07.004. Consensus: https://consensus.app/papers/details/1988720f191c5ea08e79b1c02cfa8a3d/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Analysis of unique traders by date in an internal market finds that traders appear to trade on specific information, a day-of-week effect, and participation falling over time.
- *Bearing:* complicates A2: participation decays, which erodes the information a decision-maker would use.

`velasco2012increasing` | Velasco, M., and others (2012). *Increasing Actionability of In-House Corporate Prediction Markets*. Proceedings of the ITI 2012 34th International Conference on Information Technology Interfaces.
- *Record:* DOI: 10.2498/iti.2012.0389. Consensus: https://consensus.app/papers/details/4296498b47a45715979d2da7bf291c5b/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Most in-house market research concerns accuracy. The paper instead addresses actionability, meaning usefulness in the company's decision process, and identifies two improvement factors: finer-grained questions and signals of informational need.
- *Bearing:* supports the gap claim: the authors say the field has studied accuracy more than use.

`weidener2025futarchy` | Weidener, L., and others (2025). *Futarchy in Decentralized Science: Empirical and Simulation Evidence for Outcome-Based Conditional Markets in DeSci DAOs*. Frontiers in Blockchain.
- *Record:* DOI: 10.3389/fbloc.2025.1650188. Consensus: https://consensus.app/papers/details/5a6caaffedc3594cb8c54ae27f42b01d/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* The study examines governance data from 13 decentralized science DAOs and simulates VitaDAO proposals. Under deterministic modeling, historical decisions fully aligned with futarchy-preferred outcomes, which the authors read as latent compatibility.
- *Bearing:* complicates: the evidence for futarchy-style use is a retrospective simulation, not an observed binding market.

`nechepurenko2026price` | Nechepurenko, M. (2026). *Price as Focal Point: Prediction Markets, Conditional Reflexivity, and the Politics of Common Knowledge*. arXiv preprint.
- *Record:* DOI: 10.48550/arxiv.2604.24147. Consensus: https://consensus.app/papers/details/50ec6cebb69f5b10b365d16fb781c1f0/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Under specifiable conditions, public market probabilities act as coordination devices that organize voters, donors, journalists and institutions. Using 2024 US election transaction data, the paper finds that social force depends on persistence, breadth of trader types and cross-platform consensus, and that the most visible market produced the least accurate forecasts.
- *Bearing:* supports the essay's concern: a price acts on decisions, and its authority can decouple from its accuracy. A single preprint, so I would not lean on the last claim. *Note:* Preprint, not peer reviewed.


### B4. What the market asks the participant to do (RQ-A3)

`hanson2003combinatorial` | Hanson, R. D. (2003). *Combinatorial Information Market Design*. Information Systems Frontiers.
- *Record:* DOI: 10.1023/a:1022058209073. Consensus: https://consensus.app/papers/details/68c7e4f81557581683742ff0978f9c2e/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Standard information markets suffer from thin-market and irrational-participation problems. Scoring rules avoid them but pool opinions poorly in thick markets, and market scoring rules become automated market makers when markets are thick and simple scoring rules when thin.
- *Bearing:* supports A3: the designer's own answer to thin markets is a market maker that is always willing to trade, which is a liquidity provision a participant never sees.

`hanson2012logarithmic` | Hanson, R. D. (2012). *Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation*. The Journal of Prediction Markets.
- *Record:* DOI: 10.5750/jpm.v1i1.417. Consensus: https://consensus.app/papers/details/f7cf96356b045602bcb2dc319c7f8ad5/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Scoring rules elicit good probability estimates from individuals and betting markets elicit good consensus estimates from groups. Market scoring rules combine the two, with groups costing no more than individuals.
- *Bearing:* supports A3: the instrument's founding idea fuses an individual's probability report with a group's consensus, and trade is the elicitation device.

`thorp2008kelly` | Thorp, E. (2008). *The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market*. Handbook chapter (Elsevier; as in record).
- *Record:* DOI: 10.1016/b978-044453248-0.50015-0. Consensus: https://consensus.app/papers/details/d79f224a141d5682947ca4b690c6d228/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* A gambler's central problem is finding positive-expectation bets, and the second is how much to bet. The chapter presents the Kelly criterion, which maximizes expected log wealth, for blackjack, sports betting and securities.
- *Bearing:* supports A3: sizing is a separate skill from forecasting, and a platform user must perform it. *Note:* Record lists 'E. Thorp'. Title in record is 'in Blackjack Sports Betting' without a comma; I added the comma.

`maclean2010long` | MacLean, L., and others (2010). *Long-Term Capital Growth: The Good and Bad Properties of the Kelly and Fractional Kelly Capital Growth Criteria*. Quantitative Finance.
- *Record:* DOI: 10.1080/14697688.2010.506108. Consensus: https://consensus.app/papers/details/e7d4306ef77b5ecfb7e2f36d18504752/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Kelly wagers maximize long-run growth but can be very large and risky short-term, and bettors can lose most of their wealth in bad scenarios, so care with fractional Kelly is crucial.
- *Bearing:* supports A3: even the optimal sizing rule exposes a participant to large drawdowns.

`baker2013optimal` | Baker, R., and others (2013). *Optimal Betting under Parameter Uncertainty: Improving the Kelly Criterion*. Decision Analysis.
- *Record:* DOI: 10.1287/deca.2013.0271. Consensus: https://consensus.app/papers/details/817b1a3f60e25197895cb70a34c9fd2c/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Kelly sizing ignores uncertainty in the win probability. Bets should be shrunk when the probability is estimated, and shrunken Kelly improved out-of-sample performance in simulation and tennis data.
- *Bearing:* supports A3: the sizing rule needs a probability the participant does not have with certainty, the same quantity a decision-maker wants from the market.

`meister2024kelly` | Meister, B. (2024). *Application of the Kelly Criterion to Prediction Markets*. arXiv preprint.
- *Record:* DOI: 10.48550/arxiv.2412.14144. Consensus: https://consensus.app/papers/details/fbb19af0c4e653908c55c291bc68e7bb/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* Mean beliefs generally differ from prices, so log-utility traders adjust risk and return relative to price. The paper shows with KL divergence how misjudging a bias and miscalculating the investment fraction affect portfolio growth.
- *Bearing:* supports A3: the participant's profit depends on belief minus price and on sizing, not on the price alone. *Note:* Preprint, not peer reviewed.

`johnson2025prediction` | Johnson, B., and others (2025). *Prediction Markets: An Emerging Form of Gambling?*. Addiction.
- *Record:* DOI: 10.1111/add.70272. Consensus: https://consensus.app/papers/details/47b7498b65a357939362e66d98e052f9/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* The authors say US prediction markets are overseen by the CFTC and often regulated as investments, so state harm-minimization measures generally do not apply, although the products resemble gambling. They point to short event cycles, repeated re-entry, loss chasing, 24/7 mobile access, push notifications and easy deposits.
- *Bearing:* supports A3 and Part 3's thesis: the participant's task, as the authors describe it, is repeated staking, with design features that encourage re-entry. This is a letter, not an empirical study. *Note:* Short letter; the record carries a long excerpt.

`adegbenro2026what` | Adegbenro, A. (2026). *What Prediction Markets Can See: Market Formation, Settlement Legibility, and the Geography of Tradable Uncertainty in Africa and Latin America*. arXiv preprint.
- *Record:* DOI: 10.48550/arxiv.2606.17503. Consensus: https://consensus.app/papers/details/2206a7b77d2a5495b4d8184931c78716/?utm_source=claude_desktop
- *Read status:* abstract only (Consensus record).
- *What it argues:* In 6,047 Polymarket and Kalshi contracts on Africa and Latin America, which uncertainties get listed depends on how legible they are to settle. Sports and elections sit near the top and conflict at the bottom, and the author concludes that inventories measure what platforms can settle as much as what traders believe.
- *Bearing:* supports A3: the question a decision-maker has may not be a question the market lists. A single preprint on two regions. *Note:* Preprint, not peer reviewed.


---

## (c) Synthesis

### A1. What markets are for, and when the price is a probability

The literature's stated purpose is forecasting by information aggregation. Wolfers and Zitzewitz (2004) state it for the field, Berg et al. (2008) give the strongest field result (the Iowa market was closer to the outcome than 964 polls 74% of the time), and Arrow et al. (2008) argue that the tool deserves fewer legal restrictions. The accuracy claim is conditional in the evidence itself. Atanasov et al. (2017) found that last-day market prices beat the simple mean of poll forecasts but lost to team polls aggregated with weighting and recalibration. Goel et al. (2010) found the edge over polls and statistical models surprisingly small. Atanasov et al. (2022) found a continuous double auction, the architecture of an order-book platform, underperformed a market-maker design in thin markets. Dudley et al. (2026, a preprint) found Polymarket forecasts for influenza and measles failed to beat standard benchmarks.

The conditions under which the price equals a probability are narrower than the field's shorthand suggests. Manski (2006) shows that with risk-neutral price takers and heterogeneous beliefs, the price is the midpoint of an interval for the mean belief and says nothing about dispersion. Gjerstad (2004) answers that, with plausible risk aversion, the price is very near the mean belief. Ottaviani et al. (2009) show that limited budgets alone produce underreaction to information and a favorite-longshot pattern, and Gandhi et al. (2014) trace the pattern to the mix of well-informed and noise traders. Page et al. (2013) add a time-to-expiry bias, Whelan (2023) shows that the fees of a commercial market push low-probability contract prices off the true probability, and Bottazzi et al. (2019) show that with Kelly-type traders the price does not converge to the true probability even though it can beat every individual belief. Mantovani et al. (2025) find in a lab that traders update toward the price, not the true state.

For the two platforms in question, the closest evidence is recent and mostly unrefereed. Le (2026) finds persistent underconfidence in political markets on Kalshi and Polymarket, with prices compressed toward 50%, and concludes that a price's meaning depends on what, when and how much is traded. Burgi et al. (2026) find a clear favorite-longshot bias on Kalshi. Dubach (2026) documents a longshot spread premium and a wash-trade share with a 22% upper tail on Polymarket. All three are working papers or preprints.

Manipulation evidence splits by setting. Rhode et al. (2006) and Hanson et al. (2006) find that price distortions are short-lived, while Deck et al. (2012) and Rasooly et al. (2025) find that well-funded or randomly placed trades distort prices, and Rasooly et al. find effects visible 60 days later, smaller in markets with more traders and volume. The settings the first group studied are large or mid-sized; the weak case in the second group is thin markets. A2 turns on this point, because a decision-maker who acts on a price gives someone a reason to move it.

Answer to A1. The literature says markets exist to aggregate dispersed information into forecasts. The price equals the probability under named conditions: risk-neutral or log-utility traders, homogeneous or well-mixed beliefs, no fees, enough depth to resist manipulation, and a short horizon. None of these is guaranteed on a commercial platform, and the platform-specific evidence found shows deviations that depend on contract type and horizon.

### A2. How decision-makers use prices

The evidence is thin, and almost none of it is about use. Cowgill and Zitzewitz's Google, Ford and Firm X study shows accurate internal markets (up to a 25% mean squared error reduction against experts) and, in its own abstract, that businesses and policymakers have been slow to adopt markets. Montgomery et al. (2013) describe the Ford market from the inside and list benefits that concern information flow, such as comments and bypassing bureaucratic limits, more than a decision rule. Cowgill et al. (2009) show that Google's participants were a self-selected, technical subgroup. O'Leary (2015) shows participation decaying over time. Velasco et al. (2012) say directly that research has concentrated on accuracy and that actionability is the open question.

The experimental evidence on use points toward trust, not accuracy, as the controlling variable. Choo et al. (2022) find that managers under-use price information when manipulators are present, and that suspicion alone leads to worse policy. Dianat et al. (2020) find that the theoretically superior market design did worse for manager decisions without top-down advice to participants. Seemann et al. (2012) find that trust in results rose with participants' enjoyment of trading. Siemroth (2019) shows in theory that when a decision changes asset values, full revelation can fail because pricing becomes a self-defeating prophecy.

The policy and governance proposals are designs, not observed practice. Hanson (2013) gives the futarchy design, Abramowicz (2003) the predictive cost-benefit design (and records the DARPA FutureMAP project, which was cancelled after controversy), Chen et al. (2011) show that honest elicitation in a decision market requires the decision-maker to risk taking every action, and Teschner et al. (2017) show that manipulation in conditional markets depends on thinness and on how tightly the decision tracks the price. The one live-governance check found is a retrospective simulation on DeSci DAO proposals (Weidener et al. 2025).

Answer to A2. There is evidence that corporate markets forecast well and some experimental evidence on how managers respond to them. I found no field study that traces a price to a decision and its consequence, and no study of how users of public platforms (as against employees of a firm) use a Polymarket or Kalshi price as a decision input. The Part 3 essay can say that the literature is silent on that use; it should not say that the use is harmful on this facet's evidence.

### A3. What the market asks of the participant, and what a decision-maker needs

The instrument the literature praises is specified as a forecasting device, and the designer's intent is probability reporting by an individual fused with group consensus (Hanson 2012; Hanson 2003 on market makers for thin markets). A participant on a commercial platform is asked for something else. The abstracts describe a participant who takes a position at a quoted price (Burgi et al. 2026, on makers and takers), faces a spread and depth profile (Dubach 2026), pays fees that alter the return profile (Whelan 2023), and sizes the position. The sizing literature says this is a separate skill with its own failure modes: the Kelly criterion requires an estimate of the probability (Baker et al. 2013 on shrinking when it is uncertain), delivers large drawdown risk (MacLean et al. 2010), and depends on the gap between belief and price (Meister 2024). A decision-maker's question is different: what is the probability, and what should I do? The tournament instruments answer the first half directly by asking forecasters for a probability and scoring it (Mellers et al. 2015; Atanasov et al. 2017), and Chen et al. (2011) show the second half requires the decision-maker's own commitments.

Two further mismatches appear. First, the question a decision-maker has may not be a listed contract: Adegbenro (2026) finds that listing follows settlement legibility, so inventories reflect what platforms can settle. Second, the price acts back on the decision-maker's world: Nechepurenko (2026, a preprint) argues public probabilities can serve as coordination devices whose authority decouples from accuracy, and Johnson et al. (2025, a letter) describe features such as short event cycles, 24/7 access and push notifications that encourage re-entry.

Answer to A3. The market asks the participant to trade at a price, manage a position and absorb fees and spreads. The decision-maker needs a calibrated probability and a rule for acting on it. The literature supports describing this as a mismatch of task, but the abstracts support it only indirectly, since no entry compares a user's market-based decision with an alternative instrument for the same user. This is an inference from several abstracts, and the essay should present it that way.

### Gaps

1. No study found of how retail users of Polymarket or Kalshi use prices to decide anything. Every platform paper is about prices, volume or microstructure.
2. No field study found that links a corporate or policy price to a decision and its outcome. The use evidence is lab experiments, case descriptions and proposals.
3. The platform-specific calibration and microstructure evidence (Le; Burgi; Dubach; Dudley; Adegbenro; Nechepurenko) is preprints and working papers.
4. Full texts were not read for any entry; Arrow et al. (2008) has only a one-sentence abstract in the record.
5. Crossref and OpenAlex were blocked, so no DOI and no metadata was cross-checked, and the Scholar Gateway search failed.

---

## (d) [verify] list

Not matched to a database record this session. None of these appears in the bib or in the entries.

- Wolfers and Zitzewitz (2006), "Interpreting prices as probabilities" (NBER working paper). Did not surface in the Consensus search; needed for A1.
- Cowgill and Zitzewitz journal version of the Google, Ford and Firm X study (Review of Economic Studies). Only the conference-proceedings record was found.
- Tetlock (2005), Expert Political Judgment. Cited by the Superforecasting record's blurb; not matched.
- Rhode and Strumpf, Journal of Economic Perspectives (2004) and later article on historical betting markets, and any manipulation article they published. Only the book-chapter record was found.
- The published version of Snowberg and Wolfers, "Explaining the favorite-longshot bias" (journal version and DOI).
- The journal DOI for Manski (2006), Economics Letters. The record's DOI is an NBER identifier.
- The Harvard Business Review DOI or stable URL for Malone (2004), and the primary HP study (Chen and Plott) behind the HP printer-sales claim. I know of the HP experiment only through the Malone abstract.
- The author and DOI for the Information Systems Frontiers 5(1) paper "Prediction Markets as Decision Support Systems". The record has neither.
- The CESifo DOI prefix 10.65864 for Burgi et al. (2026). It is recorded as Consensus gives it and is unresolved.
- The Berg and Rietz co-authorship of the Iowa Electronic Markets papers. The record names only "Joyce E. Berg et al."
- Platform documentation for Kalshi and Polymarket (contract terms, fee schedules, order-book mechanics) and any user-demographic data. Not retrieved; needed to ground A3 in how the platforms present the task.
- The published version, if any, of the arXiv and SSRN preprints entered here.
- Kelly (1956), the original criterion paper. The sizing entries cite later work only.
