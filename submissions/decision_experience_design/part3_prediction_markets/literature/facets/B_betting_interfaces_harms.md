# B. Gamified and betting-style interfaces and behavioral harms

Facet B of the Decision Experience Design (DXD) Part 3 literature review. Agent-drafted on 2026-10-03. The author has not reviewed it, and none of the text below is the author's.

What this facet covers. The interface features of online betting and trading apps (push notifications, confetti and badges, live odds, in-play and micro-event betting, one-tap trading, leaderboards, streaks) and what the literature says about their effect on risk-taking and overtrading. It also covers dark patterns and deceptive design in financial and gambling interfaces, and the evidence on whether users of these interfaces learn from feedback or overfit to noise. The synthesis answers three questions. B1: what the research shows about interface features and risk-taking or overtrading. B2: what the dark-pattern literature establishes and how far it reaches gambling and finance. B3: whether outcome feedback produces learning, calibration or noise-fitting.

Legend for read status. Every entry in this facet is abstract only: I read the database abstract returned by Consensus on 2026-10-03 and no full text. No entry is read in full or in part. Nothing here may be quoted beyond its abstract. Bearing on the Part 3 argument is marked supports, complicates or refutes. The argument being tested is that decision markets such as Polymarket and Kalshi are poor decision experience design.

Method note on peer review. Journal articles and refereed proceedings are marked as such. Working papers and SSRN postings are flagged. Six entries carry a working-paper or SSRN DOI because that is the DOI the database returned; their journal DOIs are on the verify list at the end.

---

## (a) Search log

All searches ran on 2026-10-03. Hits is the count the source reported.

| # | Source | Exact query or request | Hits | Notes |
|---|---|---|---|---|
| 1 | Scholar Gateway semanticSearch (topN 8) | Do gamification features in retail trading apps such as confetti, push notifications and leaderboards increase risk-taking and overtrading? | 0 | Failed: INVALID_QUERY, Could not resolve user identity from CONNECT. Not retried. Scholar Gateway was not usable this session. |
| 2 | Consensus | gamification retail trading app Robinhood risk-taking overtrading | 20 | Surfaced Chapkovski et al. 2024 and 2025, Hüller et al. 2023, Barber et al. 2022, Newall 2022, Chaudhry et al. 2021, Ridgeway et al. 2023 |
| 3 | Consensus | sports betting apps push notifications in-play betting microbetting harm | 20 | Surfaced Hing et al. 2022, 2023, 2025, Parke et al. 2019, Rockloff et al. 2026, Killick et al. 2018, Russell et al. 2018, Vieira et al. 2023, Farrell et al. 2026 |
| 4 | Consensus | dark patterns deceptive design e-commerce prevalence and effectiveness on consumers | 20 | Surfaced Mathur et al. 2019, Luguri and Strahilevitz 2019, Zac et al. 2025, Sin et al. 2022, OECD 2022, McGarrigle et al. 2026 |
| 5 | Consensus | Barber Odean trading is hazardous to your wealth; online investors overconfidence and overtrading | 20 | Surfaced Barber and Odean 2000, Barber and Odean 2002, Odean 2011 reprint, Mosenhauer et al. 2021, Bregu 2020 |
| 6 | Consensus | forecasting tournaments training probabilistic reasoning improves calibration; outcome feedback learning | 20 | Surfaced Mellers et al. 2014, Chang et al. 2016, Moore et al. 2016, Benson and Onkal 1992, Stone and Opel 2000, Hauenstein et al. 2024, Martin et al. 2024 |
| 7 | Consensus | Smart(phone) investing? within investor-time analysis of new technologies and trading behavior mobile app | 20 | Surfaced Kalda et al. 2021, Cen 2023, Liu et al. 2024. Most of the other hits were technology-adoption surveys and were not used. |
| 8 | Consensus | near-miss effect loss chasing gambling slot machines and online betting | 19 | Surfaced Clark et al. 2009, Barton et al. 2017, Pisklak et al. 2019, Palmer et al. 2024, Zhang et al. 2024 (two papers) |
| 9 | Consensus | prediction market traders learning from feedback, overfitting noise, trader experience and performance | 20 | Surfaced Seru et al. 2010, Barber 2019, Nicolosi et al. 2009, Cowgill and Zitzewitz 2014. Many hits were agent-based simulations and were not used. |
| 10 | Consensus (page_size 8) | Wisdom of the Robinhood crowd: herding, attention, and returns of Robinhood investors | 8 | Found Welch 2020 (NBER record). No Welch paper on gamification surfaced. |
| 11 | Consensus (page_size 8) | The dark (patterns) side of UX design taxonomy of manipulative interface strategies | 8 | Found Gray et al. 2018 |
| 12 | Consensus (page_size 10) | betting app features, gambling harm, loss chasing and responsible gambling tools effectiveness Gainsbury Newall | 10 | Found Harris et al. 2016, Edson et al. 2025 and 2026 (not used). No Gainsbury paper surfaced. |
| 13 | Crossref REST (curl through the configured proxy) | 9 query.bibliographic lookups (Welch; Gray; Luguri and Strahilevitz journal DOI; Odean 1999; Barber and Odean 2000; Gainsbury; Newall; Hing; Kalda) | 0 | Failed: curl exit 56, CONNECT tunnel failed, response 403. The status endpoint shows a policy denial. I did not try to get around it. |
| 14 | OpenAlex REST (curl through the configured proxy) | one request, /works?per-page=1 | 0 | Failed: CONNECT tunnel failed, response 403. Same policy denial. Not retried. |

Consequence. No DOI below was re-checked against Crossref or OpenAlex. Each DOI and each bibliographic detail comes from the Consensus record returned the same day. Where the record omitted volume, pages or co-authors, the bib file leaves them out. Sources I know of but could not match to a record are on the verify list and are not in the bib.

---

## (b) Entries

Entries follow the facet's questions. Each gives the citekey, the reference, the read status, what the source argues, and its bearing on Part 3.

### B1. Interface features, risk-taking and overtrading

barber2000hazardous. Barber, B. and Odean, T. (2000). Trading is hazardous to your wealth. SSRN DOI 10.2139/ssrn.219228 (record lists the Journal of Finance).
- Read status: abstract only.
- What it argues: among 66,465 households at a discount broker, 1991 to 1996, the heaviest traders earned 11.4 percent a year against 17.9 percent for the market, and overconfidence explains the high trading.
- Bearing: supports. It is the baseline for overtrading before apps. It does not test any interface feature.

barber2002online. Barber, B. and Odean, T. (2002). Online investors: do the slow die first? SSRN DOI 10.2139/ssrn.219242 (record lists the Review of Financial Studies).
- Read status: abstract only.
- What it argues: 1,607 investors who moved from phone to online trading traded more actively, more speculatively and less profitably afterwards. Lower costs and faster execution did not explain the change; overconfidence, self-attribution bias and illusions of knowledge and control did.
- Bearing: supports. It is the earliest within-investor evidence that a change of interface changes trading. It also separates friction from psychology, which matters for one-tap trading.

odean1999trade. Odean, T. Do investors trade too much? DOI 10.2307/j.ctvcm4j8j.28 (a book reprint; the record gives 2011).
- Read status: abstract only.
- What it argues: the securities that 10,000 discount-broker accounts bought underperformed those they sold, even net of liquidity and tax motives.
- Bearing: supports. Cite only after the AER article is matched (verify list).

barber2022attention. Barber, B. and others (2022). Attention-induced trading and returns: evidence from Robinhood users. Journal of Finance. DOI 10.1111/jofi.13183.
- Read status: abstract only.
- What it argues: Robinhood investors show more attention-induced trading than other retail investors, outages cut trading in high-attention stocks, and the pattern is partly driven by the app's own features. Heavy buying forecasts negative returns, with average 20-day abnormal returns of -4.7 percent for the top purchased stocks.
- Bearing: supports. It ties app design to herding with a measured cost, but it cannot say which feature does the work.

welch2020wisdom. Welch, I. (2020). The wisdom of the Robinhood crowd. NBER working paper, DOI 10.3386/w27866 (record lists the Journal of Finance).
- Read status: abstract only.
- What it argues: Robinhood investors collectively raised holdings in the March 2020 crash, did not panic, and their consensus portfolio did well from mid-2018 to mid-2020.
- Bearing: complicates. The abstract is about crowd performance, not gamification. The brief cites Welch 2022 on Robinhood-style gamification; I found no Welch abstract that makes that claim. Part 3 should cite Welch as a counterweight (retail crowds are not simply noise), not as a gamification source.

kalda2021smartphone. Kalda, A. and others (2021). Smart(phone) investing? NBER working paper, DOI 10.3386/w28363.
- Read status: abstract only.
- What it argues: comparing the same investor in the same month across platforms at two German banks, smartphone trades are riskier, more lottery-type and more return-chasing. Digital nudges and screen size do not mechanically drive the result, and the effects persist.
- Bearing: complicates. It shows a device effect on risk-taking within investor, but it rules out nudges as the mechanism. Part 3 must not credit confetti or notifications for this result.

cen2023smartphone. Cen, X. (2023). Smartphone trading technology, investor behavior, and mutual fund performance. Management Science. DOI 10.1287/mnsc.2021.02099.
- Read status: abstract only.
- What it argues: a natural experiment around an adviser's app release. Adopters pay more attention, trade more and chase short-term fund returns, and fund returns fall.
- Bearing: supports, with an externality: the harm reaches non-adopters.

liu2024mobile. Liu, C. and others (2024). Mobile apps, trading behaviors, and portfolio performance. Information Systems Research. DOI 10.1287/isre.2020.0616.
- Read status: abstract only.
- What it argues: in China, app adoption leaves portfolio performance unchanged on average. Lower time constraints help, a modest rise in trend chasing hurts, and heavy use has an inverted U relation to performance.
- Bearing: complicates. The app effect is mixed, not uniformly harmful.

chapkovski2024gamification. Chapkovski, P., Khapko, M. and Zoican, M. (2024). Trading gamification and investor behavior. Management Science. DOI 10.1287/mnsc.2022.02650.
- Read status: abstract only.
- What it argues: in a randomized online experiment, hedonic gamification (confetti, badges) raises trading volume by 5.17 percent on average, but 70 percent of the platform difference is self-selection and 30 percent is gamification. Gamification-preferring participants trade more noisily. Price-trend notifications help investors with accurate beliefs and reinforce the mistakes of those with wrong beliefs.
- Bearing: complicates and supports. The causal effect is real but small, and self-selection matters. The notification result is directly relevant to B3.

chapkovski2025gamified. Chapkovski, P. and others (2025). Gamified risk-taking. Journal of Behavioral and Experimental Finance. DOI 10.1016/j.jbef.2025.101049.
- Read status: abstract only.
- What it argues: with 605 participants in four countries, nudges toward holding volatile assets amplify risk-taking, most for inexperienced traders with low financial literacy.
- Bearing: supports.

huller2023gamified. Hüller, C. and others (2023). When financial platforms become gamified, consumers' risk preferences change. Journal of the Association for Consumer Research. DOI 10.1086/726431.
- Read status: abstract only.
- What it argues: six experiments (N = 3,766) show that game elements such as leaderboards make investment choices riskier, because they add a goal of winning. Once the goal is reached, the extra risk-taking stops.
- Bearing: supports, and names a mechanism (goal pursuit) that a leaderboard on a decision market would trigger.

chaudhry2021design. Chaudhry, S. and others (2021). Design patterns of investing apps and their effects on investing behaviors. ACM DIS. DOI 10.1145/3461778.3462008.
- Read status: abstract only.
- What it argues: it derives design guidelines from finance, dual-process theory and uncertain-reward interfaces, then finds that popular trading apps generally do not follow them.
- Bearing: supports, as an audit rather than a causal test.

ridgeway2023predatory. Ridgeway, A. and others (2023). Predatory inclusion and the Robinhood app. Technical Communication. DOI 10.55177/tc191789.
- Read status: abstract only.
- What it argues: a critical interface analysis of deposit, browse and trade microinteractions finds a manufactured sense of urgency that encourages overtrading.
- Bearing: supports as interpretive evidence only. No behavior was measured.

newall2022gamblification. Newall, P. and others (2022). The gamblification of investing. International Journal of Environmental Research and Public Health. DOI 10.3390/ijerph19095391.
- Read status: abstract only.
- What it argues: a gamblified product leads most users to lose, attracts people at risk of gambling harm, and uses gambling design principles (high frequency, lottery-like wins). High-frequency trading and high-risk derivatives qualify.
- Bearing: supports. It supplies a three-part test that Part 3 can apply to event contracts.

mosenhauer2021casino. Mosenhauer, M. and others (2021). The stock market as a casino. Journal of Behavioral Addictions. DOI 10.1556/2006.2021.00058.
- Read status: abstract only.
- What it argues: among 795 US gambler-investors, self-reported portfolio turnover rises with problem gambling scores, after controls for literacy and overconfidence.
- Bearing: supports, but it is a retrospective cross-section.

oksanen2022gambling. Oksanen, A. and others (2022). Gambling and online trading. Public Health. DOI 10.1016/j.puhe.2022.01.027.
- Read status: abstract only.
- What it argues: in a Finnish survey (N = 1,530), real-time stock-trading platform use and crypto trading are associated with more excessive behavior and distress, while regular investing is not.
- Bearing: supports as association only.

parke2019continuous. Parke, A. and others (2019). Transformation of sports betting into a rapid and continuous gambling activity. International Journal of Mental Health and Addiction. DOI 10.1007/s11469-018-0049-8.
- Read status: abstract only.
- What it argues: interviews with 19 problem sports bettors yield an online sports betting loop sustained by live betting, cash-out, micro-event betting and instant depositing.
- Bearing: supports. It is the closest description of a loop that continuous event contracts could reproduce.

hing2022smartphone. Hing, N. and others (2022). Immediate access ... everywhere you go. International Journal of Mental Health and Addiction. DOI 10.1007/s11469-022-00933-8.
- Read status: abstract only.
- What it argues: interviews with 33 young Australian bettors link smartphone betting to more frequent, impulsive, longer-odds betting and loss chasing.
- Bearing: supports (qualitative).

hing2023situational. Hing, N. and others (2023). Situational features of smartphone betting. Journal of Behavioral Addictions. DOI 10.1556/2006.2023.00065.
- Read status: abstract only.
- What it argues: an ecological momentary assessment of 1,378 sessions finds that anywhere-anytime betting, privacy and more promotions are associated with more short-term harm.
- Bearing: supports.

hing2025direct and rockloff2026direct. Hing, N. and others (2025), DOI 10.1556/2006.2025.00067; Rockloff, M. and others (2026), Addiction, DOI 10.1111/add.70369.
- Read status: abstract only (both).
- What they argue: Hing et al. find in 4,020 observations that each extra operator message raises bets, spending and harm, with email, text and app notifications all associated with more spending. Rockloff et al. randomized 227 bettors to opt out of direct marketing and found 23 percent fewer bets, 39 percent less spending and 67 percent fewer short-term harms.
- Bearing: supports, and Rockloff is the strongest causal evidence on notifications in this facet. The sample is gamblers on Australian operators, not prediction-market users.

hing2019wagering. Hing, N. and others (2019). Wagering advertisements and inducements. Journal of Gambling Studies. DOI 10.1007/s10899-018-09823-y.
- Read status: abstract only.
- What it argues: regular bettors report near-daily exposure to ads and inducements, and substantial minorities report larger or more frequent bets on exposure days. Direct messages and in-app ads were the most influential.
- Bearing: supports, but the influence is self-reported.

killick2018inplay, russell2018microbets, vieira2023inplay, farrell2026live. In-play and micro-event betting (DOIs 10.1007/s11469-018-9896-6, 10.1007/s10899-018-9810-y, 10.1556/2006.2023.00030, 10.1556/2006.2025.00491).
- Read status: abstract only (all four).
- What they argue: Killick et al. scoped 16 papers and 338 sites and judge in-play betting potentially more harmful because of its structure. Russell et al. surveyed 1,813 Australian bettors: 78 percent of micro-event bettors met problem-gambling criteria, and the authors suggest a ban would be targeted. Vieira et al. find in-play bettors in Ontario report higher severity and harm than single-event and traditional bettors. Farrell et al. (85 cases, 84 controls, exploratory) find more in-play betting, cash-out and in-app streaming among higher-risk bettors.
- Bearing: supports, with one caution. All four are cross-sectional or exploratory, so they cannot separate feature effects from who chooses the feature.

torrance2023structural and quintero2023microbetting. Scoping reviews (DOIs 10.1080/16066359.2023.2241350, 10.1007/s10899-023-10239-6).
- Read status: abstract only.
- What they argue: Torrance et al. (26 records, 8 patents) describe instant access, rapid continuous betting, cash-out and instant deposit as the structural features of online sports betting. Quintero Garzola et al. (22 references) link microbetting to severe problem gambling and impulsivity.
- Bearing: supports as maps of the field. Both inherit the weak causal designs of what they review.

clark2009nearmiss, barton2017ldw, pisklak2019nearmiss, palmer2024nearmiss. Near-miss (DOIs 10.1016/j.neuron.2008.12.031, 10.1007/s10899-017-9688-0, 10.1007/s10899-019-09891-8, 10.1037/adb0000999).
- Read status: abstract only (all four).
- What they argue: Clark et al. find near-misses are less pleasant but raise the desire to play, only when the player has personal control. Barton et al. review 51 studies: near-misses motivate continued play but their effects on emotion and betting vary. Palmer et al. replicate in an online slot simulator: faster spins and bigger bets after near-misses. Pisklak et al. report failures to support the effect in pigeons and humans.
- Bearing: complicates. The near-miss effect is real in some paradigms and absent in others. Part 3 should cite it only for products with a skill or control framing, and then only as a hypothesis for event contracts. No study here involves a market interface.

zhang2024within and zhang2024between. Chasing in an online eCasino (DOIs 10.1038/s41598-024-70738-3, 10.1556/2006.2024.00022).
- Read status: abstract only.
- What they argue: within sessions, gamblers bet more and play longer after immediate losses, but less after cumulative losses. Between sessions the evidence for loss chasing is limited and the evidence for win chasing is clear.
- Bearing: complicates. Loss chasing is not the uniform behavior the lay account assumes.

harris2016harmmin. Harris, A. and others (2016). A critical review of the harm-minimisation tools available for electronic gambling. Journal of Gambling Studies. DOI 10.1007/s10899-016-9624-8.
- Read status: abstract only.
- What it argues: it reviews breaks in play, pop-up messages, limit setting and behavioral tracking, and the empirical evidence on whether they change cognition and behavior.
- Bearing: complicates. A design remedy exists in the literature, but the abstract does not give effect sizes.

### B2. Dark patterns and deceptive design

gray2018dark. Gray, C. M. and others (2018). The dark (patterns) side of UX design. ACM CHI. DOI 10.1145/3173574.3174108.
- Read status: abstract only.
- What it argues: a content analysis of practitioner-identified dark patterns finds a wide range of ethical concerns conflated under one term, and a shared worry that designers become complicit in manipulation.
- Bearing: supports. It is the design-ethics anchor for Part 3, and it concerns practice, not user outcomes.

mathur2019scale. Mathur, A. and others (2019). Dark patterns at scale. Proc. ACM HCI. DOI 10.1145/3359183.
- Read status: abstract only.
- What it argues: from about 53K product pages on about 11K shopping sites, the authors found 1,818 dark-pattern instances in 15 types and 7 categories, 183 sites with deceptive practices, and 22 third-party providers selling dark patterns as a service.
- Bearing: supports as prevalence evidence. The sample is shopping sites, not financial or betting interfaces.

luguri2019shining. Luguri, J. B. and others (2019). Shining a light on dark patterns. SSRN DOI 10.2139/ssrn.3431205 (record lists the Journal of Legal Analysis).
- Read status: abstract only.
- What it argues: in two experiments with representative US samples, mild dark patterns more than doubled sign-up for a dubious service and aggressive ones nearly quadrupled it. Aggressive patterns caused backlash and mild ones did not. Less educated subjects were more susceptible.
- Bearing: supports as effect-size evidence that design, not price, drives choice. The task was a data-protection subscription, not a trade.

zac2025vulnerability, sin2022darkpatterns, oecd2022dark. Susceptibility and policy (DOIs 10.1017/bpp.2024.49, 10.1017/bpp.2022.11, 10.1787/44f5e846-en).
- Read status: abstract only.
- What they argue: Zac et al. find susceptibility across all groups and only weak support for income, education or age as vulnerability proxies; added friction after a dark pattern reduces its effect, so one-click payment is where it works best. Sin et al. find dark patterns raise purchase impulsivity and that any intervention beats none. The OECD report gives a working definition and reviews prevalence, effectiveness and harm.
- Bearing: supports. The one-click result bears directly on one-tap trading, though the experiments are shopping tasks.

mcgarrigle2026gambling. McGarrigle, J. and others (2026). Dark patterns in online gambling. Journal of Behavioral Addictions. DOI 10.1556/2006.2025.00096.
- Read status: abstract only.
- What it argues: a preregistered scoping review (n = 16) lists hidden management tools, complex inducements, withdrawal minimums, account-closing friction, high default stakes and urgency prompts. Evidence on behavioral impact is limited because operator data are closed.
- Bearing: supports and sets the gap: gambling dark patterns are catalogued, not measured.

### B3. Feedback, learning and noise

seru2010learning. Seru, A. and others (2010). Learning by trading. SSRN DOI 10.2139/ssrn.891694 (record lists the Review of Financial Studies).
- Read status: abstract only.
- What it argues: some investors improve with experience, but much of the apparent learning is attrition of those who learn they are bad. Ignoring attrition overstates learning speed.
- Bearing: complicates in a useful way. Aggregate improvement on a market can reflect who leaves.

barber2019learning. Barber, B. M. and others (2019). Learning, fast or slow. Review of Asset Pricing Studies. DOI 10.1093/rapstu/raz006.
- Read status: abstract only.
- What it argues: among Taiwanese day traders, losers quit more often, yet aggregate performance is negative, 74 percent of volume comes from traders with a history of losses, and 97 percent are likely to lose in future. This fits overconfidence and biased learning, not rational trading to learn.
- Bearing: supports. It is the strongest abstract here for the claim that repeated feedback does not cure speculation.

nicolosi2009learn. Nicolosi, G. and others (2009). Do individual investors learn from their trading experience? Journal of Financial Markets. DOI 10.1016/j.finmar.2008.07.001.
- Read status: abstract only.
- What it argues: investors trade more when their history suggests stock-selection ability, and experience improves performance, with heterogeneity across investors.
- Bearing: complicates. Some learning does occur.

bregu2020feedback. Bregu, K. (2020). Overconfidence and (over)trading: the effect of feedback on trading behavior. Journal of Socio-Economics. DOI 10.1016/j.socec.2020.101598.
- Read status: abstract only.
- What it argues: in a laboratory design where overconfidence in information accuracy creates a reason to overtrade, feedback on accuracy changes how much overconfidence drives trading. Overconfidence raises volume and weakly cuts profit.
- Bearing: supports a conditional claim: feedback on the right quantity can limit overtrading.

benson1992feedback and stone2000training. Feedback type (DOIs 10.1016/0169-2070(92)90066-i, 10.1006/obhd.2000.2910).
- Read status: abstract only.
- What they argue: Benson and Onkal found simple outcome feedback had very little effect on probability forecasters, while calibration feedback improved calibration, in one step. Stone and Opel found performance feedback reduced overconfidence, environmental feedback improved discrimination, and neither improved the other; environmental feedback raised overconfidence.
- Bearing: supports. Plain win-or-lose outcome feedback, which is what a market position gives, is the weak kind. Calibration feedback needs a scoring rule and a record of many forecasts.

mellers2014psych, tetlock2014tournaments, chang2016champs, moore2016calibration. Tetlock-style training (DOIs 10.1177/0956797614524255, 10.1177/0963721414534257, 10.1017/s1930297500004599, 10.1287/mnsc.2016.2525).
- Read status: abstract only (all four).
- What they argue: in the geopolitical tournaments, probability training, teaming and tracking improved calibration and resolution. A training module of under an hour raised Brier accuracy by 6 to 11 percent. Forecasters' confidence roughly matched accuracy over three years, with about 3 percent overconfidence, and training reduced it. Tetlock et al. describe the tournament as a level-playing-field comparison that beat the crowd average.
- Bearing: supports a design claim. Learning from forecasts is possible when questions resolve against probabilities, scores are returned and training is given. A trading interface offers prices and profit, not Brier scores.

hauenstein2024rethinking and martin2024practical. Limits on the training result (DOIs 10.1177/09567976241266481, 10.1002/ffo2.199).
- Read status: abstract only.
- What they argue: Hauenstein et al. reanalyse the Mellers data with an item response model and find that controlling extraneous variables substantially reduces, eliminates or sometimes reverses the teaming and training effects. Martin et al. (N1 = 610, N2 = 871) found no calibration gain from either outcome feedback or Practical-score feedback.
- Bearing: complicates. The training literature is contested, and Part 3 should state it that way.

cowgill2014corporate. Cowgill, B. and others (2014). Corporate prediction markets. ACM EC. DOI 10.1145/2600057.2602901.
- Read status: abstract only.
- What it argues: markets at Google, Ford and Firm X beat expert forecasts by up to 25 percent in mean squared error, with an optimism bias. Efficiency improves as experienced and higher-scoring traders trade against the bias and less skilled traders exit.
- Bearing: complicates. It shows learning by selection in low-stakes corporate markets, which differ from open retail markets.

---

## (c) Synthesis

B1: what the interface literature shows. Three lines of evidence converge on a modest, real, contested effect. The classic overtrading results (Barber and Odean 2000, 2002) show that more active trading costs retail investors and that moving online made trading more speculative. The app-era studies show that smartphone trading raises risk-taking and return chasing (Kalda et al. 2021; Cen 2023), though Liu et al. (2024) find no net performance change. The experiments on gamification find that confetti, badges and leaderboards raise volume and risk-taking (Chapkovski et al. 2024, 2025; Hüller et al. 2023), but Chapkovski et al. attribute 70 percent of the volume gap to self-selection, and Kalda et al. rule out nudges as the driver of the smartphone effect. The sports-betting literature supplies the most direct evidence on notifications: Rockloff et al. (2026) randomly cut direct marketing and found fewer bets, less spending and fewer harms. Live, in-play and micro-event features are associated with higher problem-gambling severity, but every study of them is cross-sectional or exploratory. The near-miss literature is split and was built on slot machines. For Part 3 this means one can say that gamified and continuous betting interfaces plausibly raise risk-taking, and that notifications have causal support. One cannot yet say which feature does the work in a prediction-market app.

B2: dark patterns. The general literature establishes prevalence (Mathur et al. 2019), large effects on choice (Luguri and Strahilevitz 2019), broad susceptibility and a role for one-click completion (Zac et al. 2025). Gray et al. (2018) supply the design-ethics frame. For gambling, McGarrigle et al. (2026) catalogue the patterns and report that behavioral evidence is thin. I found no study of dark patterns in a prediction-market or event-contract interface.

B3: learning versus noise. The evidence points both ways. Experience improves some investors (Nicolosi et al. 2009), but a large share of apparent learning is attrition (Seru et al. 2010), and day traders keep losing despite many rounds of feedback (Barber 2019). Simple outcome feedback does little for probability judgment (Benson and Onkal 1992); calibration feedback and structured training do better (Stone and Opel 2000; Mellers et al. 2014; Chang et al. 2016), though the training effect is contested (Hauenstein et al. 2024; Martin et al. 2024). Price-trend notifications can reinforce mistakes in people with wrong beliefs (Chapkovski et al. 2024). The design implication for Part 3 is that a market interface returns outcome feedback, which is the weak kind, and not the calibration feedback that the forecasting literature uses.

---

## (d) Gaps

- No peer-reviewed study in this facet examines Polymarket, Kalshi or any event-contract interface. I ran no query aimed at them in this facet.
- Causal evidence on confetti, streaks and one-tap trading specifically is missing. Streaks were not matched to any record.
- Everything rests on abstracts. Effect sizes and designs have not been read in full.
- Crossref and OpenAlex were blocked, so DOIs and metadata are unchecked against a second source.
- Scholar Gateway failed, so there is no semantic-search pass.

## (e) Verify list

These items are not in the bib. Each came to mind from background knowledge or from the brief and was not matched to a database record this session.

- Luguri and Strahilevitz, Journal of Legal Analysis 2021: journal DOI and volume. The bib has only the SSRN DOI.
- Welch, Journal of Finance 2022: DOI and volume. The bib has only the NBER DOI.
- Barber and Odean, Journal of Finance 2000 and Review of Financial Studies 2002: journal DOIs. The bib has SSRN DOIs.
- Odean, American Economic Review 1999: the original article, as against the 2011 reprint DOI in the bib.
- Kalda et al. published version, if any, and full author list.
- Full author lists for every entry with "and others" in the bib.
- Gainsbury and Newall works on betting apps beyond the 2022 gamblification paper: not retrieved.
- Any Welch paper on Robinhood gamification: none found; the brief's citation may refer to a different paper.
- Streak mechanics in trading or betting apps: no study identified.
- Tetlock and Gardner, Superforecasting (book): not searched; not in the bib.
