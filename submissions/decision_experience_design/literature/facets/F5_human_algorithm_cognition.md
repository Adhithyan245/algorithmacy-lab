# F5 — The cognitive science of deciding with and through algorithms

Facet F5 of the Decision Experience Design (DXD) literature review. Built 2026-09-30 in worktree `wt-dxd`.
This file supplies the right-hand side of the analogy. It holds the empirical findings a DXD professional would need, as a UX designer needs the research on reading, cognitive load and perception.

**Counts.** 37 entries. 17 reuse an existing verified card and 20 rest on a database record I retrieved this session. By read status: 17 **read in full**, 1 **partial**, 19 **abstract only**. Entries built from a card inherit that card's read depth, and I say so where it applies.

The entry count exceeds the 15–25 target. The brief named about 25 sources, and searching and snowballing added ten more: entries 14–17, 21, 22 and 32–35. Most of the ten bear on *keeping track* or are counterevidence on transparency, two areas the named list left thin.

---

## (a) Search log

All searches ran on 2026-09-30. Crossref's `total-results` counts every relevance-ranked match, so its large totals mean nothing; I read only the top three records per query.

| # | Source | Exact query / call | Results | Used for |
|---|---|---|---|---|
| 1 | Repo grep (worktree) | `grep -ril '<k>' submissions/*/literature submissions/*/library org_frontier/research/*/literature` for k in: parasuraman, lee.*see, dzindolet, dietvorst, logg, burton, mahmud, bansal, bucinca, bu.inca, vaccaro, lai2023, kulesza, eslami, devito, bucher, cotter, risko, critical thinking, amershi, shneiderman | 0–8 files per key (amershi 0; shneiderman 1, unrelated; burton, mahmud, kulesza, risko: citations only, no card) | 17 reused cards |
| 2 | Repo grep | dell.acqua\|jagged; bastani; glickman; poursabzi; backward compat; kosmyna; gerlich; steyvers; schemmer | dellacqua2026 card found; the others had no card | Entry 34 |
| 3 | Crossref `query.bibliographic` | "Burton Stein Jensen 2020 A systematic review of algorithm aversion in augmented decision making" | 1,428,073 (top hit exact) | 10.1002/bdm.2155 |
| 4 | Crossref | "Mahmud What influences algorithmic decision-making? A systematic literature review on algorithm aversion 2022" | 2,136,032 (top hit exact) | 10.1016/j.techfore.2021.121390 |
| 5 | Crossref | "Vaccaro Almaatouq Malone When combinations of humans and AI are useful: A systematic review and meta-analysis" | 1,138,092 (hit 2 exact; hit 1 PsyArXiv preprint) | 10.1038/s41562-024-02024-1 |
| 6 | Crossref | "Bansal Beyond accuracy: the role of mental models in human-AI team performance HCOMP 2019" | 802,652 (top hit exact) | 10.1609/hcomp.v7i1.5285 |
| 7 | Crossref | "Kulesza Tell me more? The effects of mental model soundness on personalizing an intelligent agent" | 200,891 (top hit exact) | 10.1145/2207676.2207678 |
| 8 | Crossref | "Kulesza Too much, too little, or just right? Ways explanations impact end users' mental models" | 130,102 (top hit exact) | 10.1109/vlhcc.2013.6645235 |
| 9 | Crossref | "DeVito Gergle Birnholtz Algorithms ruin everything RIPTwitter folk theories" | 605,614 (hits 1–2 = DeVito 2017, 2018) | 10.1145/3025453.3025659 |
| 10 | Crossref | "DeVito How people form folk theories of social media feeds and what it means for how we study self-presentation" | 259,617 (top hit exact) | 10.1145/3173574.3173694 |
| 11 | Crossref | "Risko Gilbert Cognitive offloading Trends in Cognitive Sciences 2016" | 10,910,618 (top hit exact) | 10.1016/j.tics.2016.07.002 |
| 12 | Crossref | "Lee The impact of generative AI on critical thinking: self-reported reductions in cognitive effort and confidence effects knowledge workers" | 30,913 (top hit exact) | 10.1145/3706598.3713778 |
| 13 | Crossref | "Amershi Guidelines for human-AI interaction CHI 2019" | 11,540,482 (top hit exact) | 10.1145/3290605.3300233 |
| 14 | Crossref | "Shneiderman Human-centered artificial intelligence: reliable, safe and trustworthy" | 4,731,560 (top hit exact) | 10.1080/10447318.2020.1741118 |
| 15 | OpenAlex `/works/doi:` | the 12 DOIs from rows 3–14 (abstract_inverted_index, open_access, locations) | 12/12 resolved; 11 with abstracts (Risko none) | OA status, abstracts |
| 16 | pdftotext on OA PDFs | nature.com (Vaccaro), ojs.aaai.org (Bansal 2019 HCOMP) | 2 full texts | Entries 12, 29 |
| 17 | curl OA PDFs | dl.acm.org (Lee 2025; DeVito 2017), sciencedirect pdfft (Mahmud) | all three returned an HTML challenge page, not the PDF | — |
| 18 | Consensus `search` | "AI model updates break user mental models backward compatibility human-AI team" | 20 | Bansal 2019 AAAI updates; Mohanty 2025; Bauer 2023; Zhang 2020 lead; Steyvers 2023 lead |
| 19 | Consensus `search` | "generative AI reliance overreliance critical thinking cognitive offloading users" | 20 | Lee 2025 confirmed; Gerlich 2025 lead |
| 20 | Scholar Gateway `semanticSearch` | "Do explanations of AI recommendations improve appropriate reliance in human-AI decision making, or do they increase overreliance?" | **failed**: `INVALID_QUERY: Could not resolve user identity from CONNECT`; not retried | — |
| 21 | Crossref | "Bansal Nushi Kamar Weld Lasecki Horvitz Updates in human-AI teams: understanding and addressing the performance/compatibility tradeoff" | 2,877 (top hit exact) | 10.1609/aaai.v33i01.33012429 |
| 22 | Crossref | "Poursabzi-Sangdeh Manipulating and measuring model interpretability CHI 2021" | 11,667,905 (top hit exact) | 10.1145/3411764.3445315 |
| 23 | Crossref | "Jussupow Benbasat Heinzl Why are we averse towards algorithms? A comprehensive literature review on algorithm aversion" | 892,906 (top hit = their 2024 MISQ paper, not the 2020 ECIS review) | lead only |
| 24 | Crossref | "Dell'Acqua Navigating the jagged technological frontier field experimental evidence knowledge worker productivity quality" | 171,068 (hit 2 = Org Sci 2026) | matches card |
| 25 | Crossref | "Glickman Sharot How human-AI feedback loops alter human perceptual, emotional and social judgements" | 3,208,699 (hit 2 exact) | 10.1038/s41562-024-02077-2 |
| 26 | Crossref | "Bastani Generative AI without guardrails can harm learning" | 4,562,673 (hit 2 exact; hit 1 = correction) | 10.1073/pnas.2422633122 |
| 27 | arXiv API | first attempt over http with raw quotes | HTTP 400 on all six queries; retried over https | — |
| 28 | arXiv API | `ti:"Manipulating and Measuring Model Interpretability"` | 1 | 1802.07810v5 |
| 29 | arXiv API | `ti:"What Lies Beneath" AND au:Mohanty` | 1 | 2311.10652v6 |
| 30 | arXiv API | `au:Bastani AND ti:"harm learning"` | 0 | — |
| 31 | arXiv API | `ti:"Updates in Human-AI Teams"` | 0 (AAAI OJS copy used instead) | — |
| 32 | arXiv API | `ti:"Your Brain on ChatGPT"` | 2 (preprint + a comment) | lead only |
| 33 | arXiv API | `ti:"Human-Centered Artificial Intelligence" AND au:Shneiderman` | 1 | 2002.04087v2 |
| 34 | OpenAlex `/works/doi:` locations | 9 DOIs (AAAI updates, Bastani, Bauer, Mohanty, Poursabzi, Mahmud, Amershi, Kulesza 2013, Risko) | 9 resolved | OA copies found for AAAI, Bauer (Mannheim), Mohanty, Poursabzi, Bastani (PMC) |
| 35 | curl / pdftotext | AAAI OJS (Bansal updates), arXiv (Poursabzi, Mohanty, Shneiderman), Microsoft Research author copies (Lee 2025, Amershi 2019) | 6 full texts | Entries 21, 23, 26, 30–32 |
| 36 | curl | Mannheim MADOC (Bauer), city.ac.uk (Kulesza 2013), UCL Discovery (Risko), Glasgow eprints (Kulesza 2013), PMC (Bastani) | all failed (HTML or no PDF link) | abstract-only fallbacks |
| 37 | WebFetch | dl.acm.org/doi/fulltext/10.1145/3706598.3713778; pnas.org/doi/10.1073/pnas.2422633122 | 403 on both | — |
| 38 | PubMed efetch | PMID 40560616 (Bastani); PMID 27542527 (Risko & Gilbert) | 2 abstracts | Entries 17, 16 |
| 39 | Semantic Scholar graph API | DOI:10.1145/3706598.3713778; DOI:10.1016/j.tics.2016.07.002 | 2 records (Risko abstract elided by publisher) | OA status |
| 40 | Unpaywall | 10.1109/vlhcc.2013.6645235; 10.1145/3025453.3025659; 10.1002/bdm.2155 | 0; 1 (ACM gateway, blocked); 0 | — |
| 41 | OpenAlex `filter=cites:W4403839497` (Vaccaro 2024), sorted by citations | top 12 of **512** | Fernandes 2026 found; Dell'Acqua 2026 confirmed |
| 42 | OpenAlex `filter=cites:W2984353433` (Bansal 2019 HCOMP) | top 12 of **463** | Bucinca, Bansal 2021, Vasconcelos confirmed; Zhang 2020 found |
| 43 | OpenAlex `filter=cites:W2905034244` (Bansal 2019 AAAI updates) | top 10 of **287** | Zhang 2020; Fügener 2021 lead |
| 44 | OpenAlex `/works/doi:` | 10.1016/j.chb.2025.108779; 10.1145/3351095.3372852; 10.25300/misq/2021/16553; 10.1145/2858036.2858494; 10.1038/s41562-024-02077-2 | 5 abstracts | Entries 33, 22, 19, 35 |
| 45 | OpenAlex `filter=title_and_abstract.search:algorithmic literacy decision making experiment` sorted by citations | 69 | none added (top hits off-facet) |
| 46 | Crossref `/works/{doi}` | Bauer 2023, Zhang 2020, Fernandes, Glickman, Mohanty, Poursabzi | 6 records | volume/issue/pages |

Semantic Scholar keyword search was not used. The two S2 DOI lookups succeeded without rate-limiting.

---

## (b) Entries

Entries are grouped by the brief's clusters. Each entry's **Role** line uses the brief's labels.

### Trust and reliance on automation

**1. parasuraman1997humans**
Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors, 39*(2), 230–253. https://doi.org/10.1518/001872097778543886
*Verification:* card `submissions/algorithmacy_design_ethics/literature/library/parasuramanriley1997.md` (verbatim abstract via Consensus/S2). *Read status:* **abstract only**. The card adds secondary detail from Lee & See 2004 and Parasuraman et al. 2000, both read in full.
Parasuraman and Riley define four relations to automation. *Misuse* is "over reliance on automation, which can result in failures of monitoring or decision biases." *Disuse* is "the neglect or underutilization of automation," commonly caused by false alarms. *Abuse* is automation imposed by designers and managers "without due regard for the consequences for human performance" (abstract). The abstract names "the saliency of automation state indicators" as a factor in monitoring.
*Role in the DXD argument:* UX-cognitive-foundation / precursor. This is the human-factors vocabulary DXD inherits. "Abuse" already puts the design decision, not the operator, at the origin of misuse.

**2. lee2004trust**
Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392
*Verification:* card `submissions/algorithmacy_design_ethics/literature/library/leesee2004.md`. *Read status:* **read in full** (card built from the author-hosted PDF).
Lee and See define trust as "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" (p. 51). Appropriate trust has three parts: *calibration*, the correspondence between trust and capability (p. 55, Fig. 2), plus *resolution* and *specificity*, which includes *temporal* specificity, trust that tracks capability from moment to moment (pp. 55–56). Trust rests on three bases: performance, process and purpose (p. 59). A trust–reliance model fitted to pasteurization-plant data accounts for 60–86% of the variance in reliance (p. 70). Studies put the reliability below which trust collapses variously at 90%, 70% and 60% (p. 72). The first design rule reads "Design for appropriate trust, not greater trust" (p. 74).
*Role in the DXD argument:* UX-cognitive-foundation. Calibration is the target construct for all three algorithmacy operations, and temporal specificity is keeping-track under another name. Every term in the model is indexed to the trustor's own goals (card).

**3. parasuraman2010complacency**
Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055
*Verification:* card `.../algorithmacy_design_ethics/literature/library/parasuramanmanzey2010.md`. *Read status:* **read in full** (card built from the TU Berlin deposit).
Parasuraman and Manzey argue that complacency and automation bias are "different manifestations of overlapping automation-induced phenomena, with attention playing a central role" (p. 381). In the complacency paradigm, operators detected 82% of failures under variable-reliability automation but 33% under constant reliability (p. 384). Sixty minutes of practice did not remove the effect (p. 387). The review reports Mosier et al.'s (1998) pilots at 55% omission and 100% commission errors, with 67% recalling cues that were not there (pp. 392–393). "The presence of a second crewmember did not affect the strength of automation bias" (p. 397).
*Role in the DXD argument:* algorithmacy-cognitive-issue (keeping track). A reliable intermediary degrades the monitoring that keeping track requires, and constant reliability does the most damage.

**4. dzindolet2003role**
Dzindolet, M. T., Peterson, S. A., Pomranky, R. A., Pierce, L. G., & Beck, H. P. (2003). The role of trust in automation reliance. *International Journal of Human-Computer Studies, 58*(6), 697–718. https://doi.org/10.1016/S1071-5819(03)00038-7
*Verification:* card `.../algorithmacy_design_ethics/literature/library/dzindolet2003.md` (Consensus abstract; S2-verified). *Read status:* **abstract only**.
In three experiments, participants detected camouflaged soldiers with an automated aid. "After observing the automated aid make errors, participants distrusted even reliable aids, unless an explanation was provided regarding why the aid might err. Knowing why the aid might err increased trust in the decision aid and increased automation reliance, even when the trust was unwarranted" (abstract).
*Role in the DXD argument:* counterevidence to the literacy remedy (interpreting). An explanation acted on trust and reliance, not on appropriateness. This is the earliest version of the result that Bansal et al. (2021) reproduce with modern XAI.

### Algorithm aversion and appreciation

**5. dietvorst2015algorithm**
Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. *Journal of Experimental Psychology: General, 144*(1), 114–126. https://doi.org/10.1037/xge0000033
*Verification:* card `.../algorithmacy_design_ethics/literature/library/dietvorst2015.md`. *Read status:* **read in full** (online-first copy; page cites follow that copy's pagination).
Dietvorst and colleagues ran five incentivized studies (N = 361, 206, 410, 1,036, 354). The model beat the humans every time: r = .53 vs .16 on the MBA task and .92 vs .69 on the airline task (Table 3). Participants who had seen the model perform still chose it less often. The effect held among the 83% (610 of 741) who had watched the model beat the human. "People are more likely to abandon an algorithm than a human judge for making the same mistake" (p. 11).
*Role in the DXD argument:* algorithmacy-cognitive-issue (interpreting). People read an intermediary's errors asymmetrically, so seeing its output does not calibrate them.

**6. dietvorst2018overcoming**
Dietvorst, B. J., Simmons, J. P., & Massey, C. (2018). Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them. *Management Science, 64*(3), 1155–1170. https://doi.org/10.1287/mnsc.2016.2643
*Verification:* card `.../algorithmacy_design_ethics/literature/library/dietvorst2018.md`. A second card sits at `org_frontier/research/cognition/literature/cards/dietvorst2018overcoming.md`. *Read status:* **read in full**.
In Study 1 (N = 288), participants chose the model 32% of the time when the choice was all-or-nothing. The figure rose to 73% when they could change 10 of 20 forecasts and 76% when they could adjust every forecast by up to 10 percentiles. In Study 2 (N = 816), 47% chose the model when they could not modify it, against 71%, 71% and 68% when they could adjust by 10, 5 or 2 percentiles. The authors conclude that "willingness to use the model was not detectably altered by imposing an 80% reduction" in the adjustment allowed (p. 1161).
*Role in the DXD argument:* algorithmacy-cognitive-issue (specifying intent). What moves people is a felt channel for intent, not how large the channel is. That is a design variable DXD owns and literacy does not.

**7. logg2019algorithm**
Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes, 151*, 90–103. https://doi.org/10.1016/j.obhdp.2018.12.005
*Verification:* card `.../algorithmacy_design_ethics/literature/library/logg2019.md`. *Read status:* **read in full**.
Logg, Minson and Moore held the advice constant and varied only its label. Before any feedback, lay participants gave more weight to advice labelled algorithmic: weight on advice (WOA) .45 vs .30 (Exp 1A, d = .42), .37 vs .21 (1B) and .38 vs .26 (1C). JDM researchers predicted the opposite. National-security professionals discounted all advice and were less accurate (Exp 4). Appreciation survived a black box with no process description. The authors propose a "theory of machine," the lay beliefs about how algorithmic and human judgment differ (card).
*Role in the DXD argument:* competing-construct / algorithmacy-cognitive-issue (interpreting). The "theory of machine" is a lay model of the intermediary that exists before any use, which is the thing interpreting works on.

**8. burton2020systematic**
Burton, J. W., Stein, M.-K., & Jensen, T. B. (2020). A systematic review of algorithm aversion in augmented decision making. *Journal of Behavioral Decision Making, 33*(2), 220–239. https://doi.org/10.1002/bdm.2155
*Verification:* Crossref record (row 3) + OpenAlex abstract (row 15). *Read status:* **abstract only** (paywalled; no OA copy found).
Burton, Stein and Jensen review "61 peer-reviewed articles between 1950 and 2018" and sort the proposed causes and remedies of aversion into five themes: "expectations and expertise, decision autonomy, incentivization, cognitive compatibility, and divergent rationalities" (abstract). They conclude that resolving aversion "requires an updated research program with an emphasis on theory integration."
*Role in the DXD argument:* UX-cognitive-foundation (field map). "Cognitive compatibility" and "decision autonomy" are the themes that map onto interpreting and specifying intent.

**9. mahmud2022influences**
Mahmud, H., Islam, A. K. M. N., Ahmed, S. I., & Smolander, K. (2022). What influences algorithmic decision-making? A systematic literature review on algorithm aversion. *Technological Forecasting and Social Change, 175*, Article 121390. https://doi.org/10.1016/j.techfore.2021.121390
*Verification:* Crossref (row 4; full given names "A.K.M. Najmul" Islam, "Syed Ishtiaque" Ahmed) + OpenAlex abstract (row 15). *Read status:* **abstract only**. The article is OA, but the PDF endpoint returned a bot-challenge page.
Mahmud and colleagues review "80 empirical studies" from seven databases plus snowballing. They sort the factors behind aversion into four themes: "algorithm, individual, task, and high-level." "Algorithm and individual factors have been investigated extensively," but "very little attention has been given to exploring the task and high-level factors" (abstract).
*Role in the DXD argument:* UX-cognitive-foundation (field map) and a gap: the task and high-level (organizational, cultural) factors are exactly where coordination through an intermediary lives.

### Explanations, overreliance and human–AI decision performance

**10. bansal2021whole**
Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M. T., & Weld, D. S. (2021). Does the whole exceed its parts? The effect of AI explanations on complementary team performance. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (16 pp.). ACM. https://doi.org/10.1145/3411764.3445717
*Verification:* card `.../algorithmacy_design_ethics/literature/library/bansal2021.md` (arXiv v3 camera-ready). The card leaves the ACM article number unverified, so it is omitted. *Read status:* **read in full**.
Bansal and colleagues set AI accuracy near human accuracy and ran 1,626 crowdworkers. Every team beat both the human and the AI alone (beer reviews: 0.89 vs 0.84 and 0.82). No explanation condition beat simply showing the AI's confidence (beer z = −1.18, p = .24; book z = 1.23, p = .22; LSAT z = 0.427, p = .64). "Explanations increased the chance that humans will accept the AI's recommendation, regardless of its correctness" (card).
*Role in the DXD argument:* counterevidence to the literacy remedy (interpreting). An explanation raises acceptance, not discrimination between right and wrong advice.

**11. bucinca2021trust**
Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287
*Verification:* card `submissions/algorithmacy_scaffolding/literature/library/bucinca2021.md`. *Read status:* **read in full** (arXiv v1).
Buçinca, Malaya and Gajos tested three cognitive forcing functions (on demand, update, wait) against simple explainable-AI baselines, with N = 199 and a 75%-accurate simulated AI. On instances where the AI was wrong, the forcing functions beat the simple-XAI conditions: overall correct 0.09 vs 0.03 (d = .37), and overreliance on the detection sub-task fell to 0.48 from 0.64. Participants rated the designs that helped most as more complex and less preferred. The benefit went mainly to participants high in Need for Cognition.
*Role in the DXD argument:* algorithmacy-cognitive-issue (interpreting) and a design lever. Friction works where explanation does not, but people dislike the friction and its benefit is unequal. The preference–performance trade-off is a core DXD problem that UX's satisfaction metrics would get wrong.

**12. vaccaro2024combinations**
Vaccaro, M., Almaatouq, A., & Malone, T. W. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour, 8*(12), 2293–2303. https://doi.org/10.1038/s41562-024-02024-1
*Verification:* Crossref (row 5) + OpenAlex (row 15) + publisher OA PDF. *Read status:* **read in full** (main text; supplement not read).
Vaccaro, Almaatouq and Malone pooled a preregistered meta-analysis of 106 experiments reporting 370 effect sizes, from studies published between 1 January 2020 and 30 June 2023; 74 papers met inclusion (p. 2294). The results:
- **Synergy:** human–AI combinations did worse than the best of human or AI alone, "g = −0.23; t92 = −2.89; two-tailed P = 0.005; 95% CI, −0.39 to −0.07" (p. 2295).
- **Augmentation:** the combinations beat humans alone, g = 0.64 (95% CI 0.53 to 0.74) (p. 2295).
- **By task:** decision tasks lost, g = −0.27 (95% CI −0.44 to −0.10), while creation tasks gained, g = 0.19 (95% CI −0.09 to 0.48; P = 0.180, n = 34), and the difference between the two was significant (p. 2295).
- **By relative skill:** when the human alone beat the AI alone, the combination showed synergy, g = 0.46 (95% CI 0.28 to 0.66). When the AI alone was better, the combination lost, g = −0.54 (95% CI −0.71 to −0.37) (p. 2295).
- **Heterogeneity:** I² = 97.7% for synergy and 93.8% for augmentation.
- **Explanation and confidence displays:** "neither of these factors significantly affected the performance of human–AI systems" (p. 2294). The authors suggest researchers "may wish to de-emphasize this line of inquiry" (p. 2297).
- **Who decides:** in more than 95% of the systems, the human made the final decision (p. 2297).
- **Delegation:** only 3 experiments predetermined a division of subtasks, g = 0.22 (95% CI −0.42 to 0.87, n.s.) (p. 2297).
*Role in the DXD argument:* algorithmacy-cognitive-issue (interpreting), and the strongest single piece of counter-literacy evidence. Across 370 effect sizes, the explanation and confidence displays made no measurable difference to team performance; task structure and the human–AI skill ratio did.

**13. lai2023science**
Lai, V., Chen, C., Smith-Renner, A., Liao, Q. V., & Tan, C. (2023). Towards a science of human-AI decision making: An overview of design space in empirical human-subject studies. In *Proceedings of the 2023 ACM Conference on Fairness, Accountability, and Transparency (FAccT '23)*. ACM.
*Verification:* card `.../algorithmacy_design_ethics/literature/library/lai2023.md` (arXiv 2112.11471v1). The card could not verify the FAccT DOI, and I did not verify it either (**unverified**). *Read status:* **partial** (arXiv v1: §§1–3 and 5–6 read in full; §4 skimmed).
Lai and colleagues coded over 80 in-scope studies from CHI, CSCW, FAccT, IUI and ACL-family venues (2018–2021) on three axes: decision task, AI assistance elements and evaluation metrics. They found home-grown, unvalidated scales, and they found that studies routinely read reliance as trust although "many other factors besides trust can influence reliance, such as required efforts, perceived risk, self-confidence, and time constraints" (§5). The field, they write, should consider "what matters for different stakeholders instead of just the decision-makers" (§6).
*Role in the DXD argument:* UX-cognitive-foundation (field map) and a gap statement. The field studies one decider on the near side of the AI, and its own survey names the party on the far side as missing.

**14. vasconcelos2023explanations**
Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023). Explanations can reduce overreliance on AI systems during decision-making. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW1), Article 129. https://doi.org/10.1145/3579605
*Verification:* card `.../algorithmacy_design_ethics/literature/library/vasconcelos2023.md`. *Read status:* **read in full** (arXiv v2 with version-of-record pagination).
Vasconcelos and colleagues frame overreliance as a cost–benefit choice and tested it in five preregistered studies with maze tasks. In Study 1 (N = 340), explanations left overreliance unchanged on easy and medium mazes and cut it on hard ones. In Study 2, written explanations, which cost more to check, did not reduce overreliance where visual highlights did. "Overreliance is not an inevitability of cognition but a strategic decision where people are responsive to the costs and benefits" (129:3).
*Role in the DXD argument:* counterevidence (partial) that sharpens the thesis. Explanations do help, but only when checking the explanation costs less than doing the task. That is an interaction-cost claim, the kind UX makes about reading effort, not a comprehension claim.

**15. zhang2020effect**
Zhang, Y., Liao, Q. V., & Bellamy, R. K. E. (2020). Effect of confidence and explanation on accuracy and trust calibration in AI-assisted decision making. In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency* (pp. 295–305). ACM. https://doi.org/10.1145/3351095.3372852
*Verification:* Crossref (row 46) + OpenAlex abstract (row 44), found by snowballing (row 43). *Read status:* **abstract only** (the arXiv 2001.02114 copy was not read).
In two experiments where human and AI performed comparably alone, "confidence score can help calibrate people's trust in an AI model, but trust calibration alone is not sufficient to improve AI-assisted decision making, which may also depend on whether the human can bring in enough unique knowledge to complement the AI's errors." The authors "highlight the problems in using local explanation" (abstract).
*Role in the DXD argument:* counterevidence (partial). A case-level confidence display does calibrate trust, which is one point for transparency, but calibrated trust did not become better decisions.

**16. poursabzi2021manipulating**
Poursabzi-Sangdeh, F., Goldstein, D. G., Hofman, J. M., Wortman Vaughan, J., & Wallach, H. (2021). Manipulating and measuring model interpretability. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–52). ACM. https://doi.org/10.1145/3411764.3445315
*Verification:* Crossref (rows 22, 46) + arXiv 1802.07810v5 (row 28). *Read status:* **read in full** (arXiv v5, which carries the CHI '21 reference block; page cites are arXiv pagination).
In preregistered experiments (N = 3,800) on apartment-price prediction, participants who saw a clear model with few features "could better simulate the model's predictions. However, we did not find that participants more closely followed its predictions" (abstract). Participants shown a clear model were "less able to detect and correct for the model's sizable mistakes, seemingly due to information overload" (abstract; Exp. 1 result, arXiv p. 23). The effect did not replicate in one later experiment. It reappeared in a further experiment's arm that carried no "outlier focus" message.
*Role in the DXD argument:* counterevidence to the literacy remedy (interpreting), with the replication caveat. Making the model legible made it simulable, not correctable. Transparency here worked like extra text on a page, a cognitive-load cost that UX research would recognise.

**17. bauer2023explained**
Bauer, K., von Zahn, M., & Hinz, O. (2023). Expl(AI)ned: The impact of explainable artificial intelligence on users' information processing. *Information Systems Research, 34*(4), 1582–1602. https://doi.org/10.1287/isre.2023.1199
*Verification:* Crossref (row 46) + Consensus abstract (row 18). *Read status:* **abstract only** (the Mannheim accepted-version PDF did not download).
In two experiments, "state-of-the-art explainability methods evoke mental model adjustments that are subject to confirmation bias, allowing misconceptions and mental errors to persist and even accumulate." These adjustments "create spillover effects that alter users' behavior in related but distinct domains where they do not have access to an AI system" (abstract).
*Role in the DXD argument:* counterevidence to the literacy remedy (interpreting) and an algorithmacy-cognitive-issue (keeping track). The explanation is itself a channel of influence that outlasts the interaction.

### Mental models of AI

**18. kulesza2012tell**
Kulesza, T., Stumpf, S., Burnett, M., & Kwan, I. (2012). Tell me more? The effects of mental model soundness on personalizing an intelligent agent. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 1–10). ACM. https://doi.org/10.1145/2207676.2207678
*Verification:* Crossref (row 7) + OpenAlex abstract (row 15). *Read status:* **abstract only**.
Participants given structural knowledge of a music recommender "were able to quickly build sound mental models of the recommender system's reasoning." Those "who most improved their mental models ... were significantly more likely to make the recommender operate to their satisfaction" (abstract).
*Role in the DXD argument:* counterevidence (the pro-literacy case) bearing on specifying intent. When the system is stable and the user is its only principal, understanding does help people steer it.

**19. kulesza2013too**
Kulesza, T., Stumpf, S., Burnett, M., Yang, S., Kwan, I., & Wong, W.-K. (2013). Too much, too little, or just right? Ways explanations impact end users' mental models. In *2013 IEEE Symposium on Visual Languages and Human Centric Computing* (pp. 3–10). IEEE. https://doi.org/10.1109/VLHCC.2013.6645235
*Verification:* Crossref (row 8) + OpenAlex abstract (row 15). Miller (2019) summarises the paper in card `.../algorithmacy_design_ethics/literature/library/miller2019.md`. *Read status:* **abstract only**.
Kulesza and colleagues found that "completeness is more important than soundness," but that when "soundness was very low, participants experienced more mental demand and lost trust in the explanations, thereby reducing the likelihood that users will pay attention to such explanations at all" (abstract). Miller (2019, p. 45 of the arXiv copy) reports the principles that came out of this work, "Be sound; Be complete; but Don't overwhelm," and notes that principles 1 and 2 conflict with 3.
*Role in the DXD argument:* UX-cognitive-foundation (bridge). The explanation's design problem turns into a mental-demand problem, which is where UX's cognitive-load tradition re-enters.

**20. bansal2019beyond**
Bansal, G., Nushi, B., Kamar, E., Lasecki, W. S., Weld, D. S., & Horvitz, E. (2019). Beyond accuracy: The role of mental models in human-AI team performance. *Proceedings of the AAAI Conference on Human Computation and Crowdsourcing, 7*(1), 2–11. https://doi.org/10.1609/hcomp.v7i1.5285
*Verification:* Crossref (row 6) + OpenAlex (row 15) + AAAI OJS PDF (row 16). *Read status:* **read in full**.
Bansal and colleagues define the mental model that matters as a model of the AI's *error boundary*: "knowing 'When does the AI err?'" (abstract). On the CAJA platform (25 MTurk workers per condition), regret fell with more rounds of interaction as workers learned the boundary (p. 5). A more parsimonious boundary (one conjunction rather than two) produced higher team performance, and team performance "generally decreases as the number of human-visible features increases" (p. 6). Even with one-sided errors, "increased stochasticity makes it difficult for participants to trust Marvin and learn a correct mental model" (p. 7). One design goal follows: "Minimize the stochasticity of system errors."
*Role in the DXD argument:* algorithmacy-cognitive-issue (interpreting). The user needs to know *when it fails*, not *how it works*, and people learn that from experience, not from exposition. How learnable the boundary is depends on properties the designer controls.

**21. bansal2019updates**
Bansal, G., Nushi, B., Kamar, E., Weld, D. S., Lasecki, W. S., & Horvitz, E. (2019). Updates in human-AI teams: Understanding and addressing the performance/compatibility tradeoff. *Proceedings of the AAAI Conference on Artificial Intelligence, 33*(1), 2429–2437. https://doi.org/10.1609/aaai.v33i01.33012429
*Verification:* Crossref (row 21) + Consensus abstract (row 18) + AAAI OJS PDF (rows 34–35); found by snowballing from entry 20. *Read status:* **read in full**.
Bansal and colleagues updated the classifier at cycle 75 of 150 to a version 5% more accurate (80% → 85%) (p. 2433). "Compatible updates improve team performance, while incompatible updates hurt team performance despite improvements in AI accuracy." They also found that "a more accurate but incompatible classifier results in lower team performance than a less accurate but compatible classifier (no update)" (p. 2434). On three high-stakes datasets, the compatibility score of standard retraining fell "as low as 40%. That is, 60% of the instances where h1 was correct are now violated" (p. 2435).
*Role in the DXD argument:* algorithmacy-cognitive-issue (keeping track), the anchor study. A shift in the intermediary's rule breaks the user's hard-won model, and accuracy gains do not compensate.

**22. mohanty2025lies**
Mohanty, V., Lim, J., & Luther, K. (2025). What lies beneath? Exploring the impact of underlying AI model updates in AI-infused systems. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–21). ACM. https://doi.org/10.1145/3706598.3713751
*Verification:* Crossref (row 46) + Consensus (row 18) + arXiv 2311.10652v6 (row 29). *Read status:* **read in full** (arXiv v6, CHI '25 camera-ready; page cites are arXiv pagination).
Mohanty, Lim and Luther ran 252 Prolific participants through a facial-recognition task. "Out of 1764 pairwise model comparisons across 252 participants, the overall accuracy in detecting whether models had changed was 48.87%, close to random guessing." Participants spotted a real change 56.98% of the time but recognised an unchanged model only 38.38% of the time (§3.9.1, p. 8). A two-week diary study with 10 real users found that updates led users "to develop divergent folk theories" (abstract).
*Role in the DXD argument:* algorithmacy-cognitive-issue (keeping track). People cannot tell from outputs alone whether the rule has changed, and Amershi et al.'s G18 ("Notify users about changes") assumes a notice that silent updates do not give.

### Folk theories and algorithmic awareness

**23. eslami2015always**
Eslami, M., Rickman, A., Vaccaro, K., Aleyasen, A., Vuong, A., Karahalios, K., Hamilton, K., & Sandvig, C. (2015). "I always assumed that I wasn't really that close to [her]": Reasoning about invisible algorithms in news feeds. In *Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems* (pp. 153–162). ACM. https://doi.org/10.1145/2702123.2702556
*Verification:* card `submissions/algorithmacy_scaffolding/literature/library/eslami2015.md`. *Read status:* **read in full**.
Of 40 Facebook users, 62.5% did not know the News Feed was curated. "Simple exposure to the algorithm output is not enough to gain information about the algorithm's existence. To learn about an algorithm without any outside information, active engagement is required." At a two-to-six-month follow-up (30 respondents), 83% reported changed behaviour after using the FeedVis probe.
*Role in the DXD argument:* algorithmacy-cognitive-issue (interpreting). Awareness of the intermediary does not come from use, and its absence was the majority case.

**24. eslami2016first**
Eslami, M., Karahalios, K., Sandvig, C., Vaccaro, K., Rickman, A., Hamilton, K., & Kirlik, A. (2016). First I "like" it, then I hide it: Folk theories of social feeds. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 2371–2382). ACM. https://doi.org/10.1145/2858036.2858494
*Verification:* card `submissions/coordinative_sovereignty/literature/library/cards/eslami2016first.md` (Crossref) + OpenAlex abstract retrieved this session (row 44). *Read status:* **abstract only** (the card withholds a summary).
Interviews with 40 Facebook users "revealed 10 'folk theories' of automated curation." Users given "seams," defined as "visible hints disclosing aspects of automation operations," "could quickly develop theories," and "users made plans that depended on their theories" (abstract).
*Role in the DXD argument:* precursor / design lever (interpreting → specifying intent). Seams are a DXD primitive: they expose the joints of the intermediary rather than its internals.

**25. devito2017algorithms**
DeVito, M. A., Gergle, D., & Birnholtz, J. (2017). "Algorithms ruin everything" [Title as recorded by Crossref and OpenAlex; see verification note]. In *Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems* (pp. 3163–3174). ACM. https://doi.org/10.1145/3025453.3025659
*Verification:* Crossref (row 9) + OpenAlex abstract (row 15). Both records give only the main title, "Algorithms ruin everything". The ACM version of record carries a subtitle that neither database supplies, and I have not verified its wording, so it is omitted here (**recheck against the ACM page before citing**). *Read status:* **abstract only** (the ACM gateway PDF was blocked).
DeVito, Gergle and Birnholtz ran a content analysis of 102,827 #RIPTwitter tweets. They found that "resistance to algorithmic change largely revolves around expectation violation, with folk theories acting as frames for reactions such that more detailed folk theories are expressed through more specific reactions to algorithmic change" (abstract).
*Role in the DXD argument:* algorithmacy-cognitive-issue (keeping track). A rule change reaches the user as a violated expectation, and the detail of the user's folk theory shapes the response.

**26. devito2018folk**
DeVito, M. A., Birnholtz, J., Hancock, J. T., French, M., & Liu, S. (2018). How people form folk theories of social media feeds and what it means for how we study self-presentation. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. https://doi.org/10.1145/3173574.3173694
*Verification:* Crossref (row 10) + OpenAlex abstract (row 15). *Read status:* **abstract only**.
In a 28-participant interview study, "people draw from diverse sources of information when forming folk theories, and ... folk theories are more complex, multifaceted and malleable than previously assumed" (abstract).
*Role in the DXD argument:* algorithmacy-cognitive-issue (interpreting). Users build their model of the intermediary from many sources, not from the interface alone.

**27. devito2021adaptive**
DeVito, M. A. (2021). Adaptive folk theorization as a path to algorithmic literacy on changing platforms. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW2), Article 339. https://doi.org/10.1145/3476080
*Verification:* card `submissions/coordinative_sovereignty/literature/library/cards/devito2021adaptive.md` (Crossref). Card `.../algorithmacy_design_ethics/literature/library/oeldorfhirsch2025.md` quotes DeVito's definition from full text. *Read status:* **abstract only** (the card's summary is paraphrased from the Crossref-served abstract).
DeVito defines algorithmic literacy as "the capacity and opportunity to be aware of both the presence and impact of algorithmically-driven systems on self- or collaboratively-identified goals, and the capacity and opportunity to crystalize this understanding into a strategic use of these systems to accomplish said goals" (quoted in Oeldorf-Hirsch & Neubaum 2025, p. 683). She argues that on platforms that keep changing, literacy has to be an ongoing capacity to re-theorize, not a fixed body of facts.
*Role in the DXD argument:* competing-construct. This is the closest rival to algorithmacy's "keeping track." It still frames the capacity as a *literacy* held by the user, which is the framing the lab's design-ethics arm rejects.

**28. bucher2017algorithmic**
Bucher, T. (2017). The algorithmic imaginary: Exploring the ordinary affects of Facebook algorithms. *Information, Communication & Society, 20*(1), 30–44. https://doi.org/10.1080/1369118X.2016.1154086
*Verification:* card `submissions/coordinative_sovereignty/literature/library/cards/bucher2017algorithmic.md` (S2 abstract). *Read status:* **abstract only**.
Drawing on tweets and interviews with 25 users, Bucher develops the "algorithmic imaginary," the ways of thinking about "what algorithms are, what they should be and how they function." She argues the imaginary plays "a generative role in moulding the Facebook algorithm itself," because users act on their beliefs and the system learns from those actions (card).
*Role in the DXD argument:* precursor / algorithmacy-cognitive-issue (keeping track). The user's model is an input to the intermediary, so the thing a user tracks is partly made by the user's own tracking.

**29. cotter2019playing**
Cotter, K. (2019). Playing the visibility game: How digital influencers and algorithms negotiate influence on Instagram. *New Media & Society, 21*(4), 895–913. https://doi.org/10.1177/1461444818815684
*Verification:* card `submissions/coordinative_sovereignty/literature/library/cards/cotter2019playing.md` (Sage abstract). *Read status:* **abstract only**.
Cotter finds that influencers' "pursuit of influence resembles a game constructed around 'rules' encoded in algorithms," and that "algorithms structure, but do not unilaterally determine user behavior" (abstract, via card).
*Role in the DXD argument:* algorithmacy-cognitive-issue (specifying intent). Producers specify intent to the intermediary indirectly, by changing their conduct to fit the rules they infer.

### Cognitive offloading and generative AI

**30. risko2016cognitive**
Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences, 20*(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002
*Verification:* Crossref (row 11) + PubMed abstract PMID 27542527 (row 38). *Read status:* **abstract only** (paywalled; the UCL deposit page yielded no PDF).
Risko and Gilbert define cognitive offloading as "the use of physical action to alter the information processing requirements of a task so as to reduce cognitive demand." They review "what mechanisms trigger cognitive offloading" and "what are the cognitive consequences," and they offer "a novel metacognitive framework" (abstract).
*Role in the DXD argument:* UX-cognitive-foundation. This is the cognitive-science base for delegating to an intermediary, and its metacognitive framing points to the decision *whether* to offload as itself a judgment people can get wrong.

**31. lee2025impact**
Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–22). ACM. https://doi.org/10.1145/3706598.3713778
*Verification:* Crossref (row 12) + OpenAlex (row 15) + S2 (row 39) + Microsoft Research author copy (row 35). *Read status:* **read in full** (the author PDF has minor extraction errors; tables were not parsed cleanly).
Lee and colleagues surveyed 319 knowledge workers. After cleaning, 936 of 957 examples remained, and participants reported enacting critical thinking for 555 (59.29%) of them (§3.3.1, p. 6). "Knowledge workers' confidence in AI doing the tasks indeed negatively correlates with their enaction of critical thinking (β=-0.69, p < 0.001)." Confidence in doing the task oneself (β=0.26, p = 0.026) and in evaluating AI responses (β=0.31, p = 0.046) correlate positively with it (§4.2.1, p. 9). General trust in GenAI had no significant correlation. Qualitatively, GenAI "shifts the nature of critical thinking toward information verification, response integration, and task stewardship" (abstract). The authors state: "Our analysis does not establish causation."
*Role in the DXD argument:* algorithmacy-cognitive-issue (all three). Verification maps onto interpreting, integration onto specifying intent, and stewardship onto keeping track. Task-level confidence, not trust in general, predicts disengagement.

**32. bastani2025generative**
Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences, 122*(26), e2422633122. https://doi.org/10.1073/pnas.2422633122
*Verification:* Crossref (row 26) + PubMed abstract PMID 40560616 (row 38). PubMed lists an erratum (PNAS 122(34), e2518204122) whose content I did not read (**check before citing numbers**). *Read status:* **abstract only**.
Bastani and colleagues ran a field experiment with "nearly a thousand high school math students." GPT-4 access improved practice grades by "48% ... for GPT Base and 127% for GPT Tutor," but when access was removed students "perform worse than those who never had access (17% reduction in grades for GPT Base)." The GPT Tutor safeguards largely mitigated the loss (abstract).
*Role in the DXD argument:* algorithmacy-cognitive-issue (keeping track of one's own competence), and design evidence. The interface design (the guardrails), not the model, decided whether offloading cost the user skill.

**33. fernandes2026smarter**
Fernandes, D., Villa, S., Nicholls, S., Haavisto, O., Buschek, D., Schmidt, A., Kosch, T., Shen, C., & Welsch, R. (2026). AI makes you smarter but none the wiser: The disconnect between performance and metacognition. *Computers in Human Behavior, 175*, Article 108779. https://doi.org/10.1016/j.chb.2025.108779
*Verification:* Crossref (row 46) + OpenAlex abstract (row 44), found by snowballing from Vaccaro (row 41). Crossref dates the issue 2026-02. *Read status:* **abstract only**.
Participants (Study 1, N = 246) used AI on 20 LSAT logical-reasoning problems. "While their task performance improved by three points compared to a norm population, participants overestimated their task performance by four points." "Higher AI literacy correlated with lower metacognitive accuracy." The Dunning-Kruger effect "ceased to exist with AI use." Study 2 (N = 452) replicated the findings (abstract).
*Role in the DXD argument:* counterevidence to the literacy remedy, and the facet's sharpest single datum for the thesis. More AI *literacy* went with *worse* monitoring of one's own performance through the AI.

**34. dellacqua2026navigating**
Dell'Acqua, F., McFowland, E., III, Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2026). Navigating the jagged technological frontier: Field experimental evidence of the effects of artificial intelligence on knowledge worker productivity and quality. *Organization Science, 37*(2), 403–423. https://doi.org/10.1287/orsc.2025.21838
*Verification:* card `submissions/lima_pdw/literature/cards/dellacqua2026.md` (Crossref + JATS abstract), reconfirmed by Crossref this session (row 24). *Read status:* **abstract only**.
In a preregistered experiment with 758 BCG consultants, those inside the frontier "completed 12.2% more tasks and completed them 25.1% more quickly." On a task "selected to be outside the frontier, subjects using AI were 19% less likely to produce correct solutions." The frontier is "the uneven impact of artificial intelligence (AI) capabilities ... even within the same knowledge workflow and with a seemingly similar level of difficulty" (abstract). The card warns that the 19% applies to a single task.
*Role in the DXD argument:* algorithmacy-cognitive-issue (interpreting). The capability boundary is invisible from the user's side, which makes it Bansal's error boundary in the field.

**35. glickman2025feedback**
Glickman, M., & Sharot, T. (2025). How human–AI feedback loops alter human perceptual, emotional and social judgements. *Nature Human Behaviour, 9*(2), 345–359. https://doi.org/10.1038/s41562-024-02077-2
*Verification:* Crossref (rows 25, 46; online 2024-12-18) + OpenAlex abstract (row 44). *Read status:* **abstract only** (the OA PDF exists, but I did not read it this session).
In a series of experiments (n = 1,401), human–AI interaction amplified human biases "significantly greater than that observed in interactions between humans." "Participants are often unaware of the extent of the AI's influence, rendering them more susceptible to it" (abstract).
*Role in the DXD argument:* algorithmacy-cognitive-issue (keeping track). People cannot track the intermediary's influence on their own judgment, and the loop compounds over time.

### Design guidelines and frameworks

**36. amershi2019guidelines**
Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for human-AI interaction. In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). ACM. https://doi.org/10.1145/3290605.3300233
*Verification:* Crossref (row 13) + OpenAlex (row 15) + Microsoft Research author copy (row 35). *Read status:* **read in full** (camera-ready).
Amershi and colleagues consolidated "more than 150 design recommendations" into 20 draft guidelines and then 18 (p. 4). They validated them with 49 design practitioners across 20 AI products (abstract). Among the 18 are G1 "Make clear what the system can do," G2 "Make clear how well the system can do what it can do," G11 "Make clear why the system did what it did," G14 "Update and adapt cautiously," G17 "Provide global controls" and G18 "Notify users about changes" (Table 1, p. 3).
*Role in the DXD argument:* precursor (DXD's closest practitioner ancestor). G1/G2/G11 are the literacy-paradigm remedies, and G14/G18 are the only keeping-track guidelines. Entries 21–22 show that G14/G18 depend on update practices the designer often does not control.

**37. shneiderman2020human**
Shneiderman, B. (2020). Human-centered artificial intelligence: Reliable, safe & trustworthy. *International Journal of Human–Computer Interaction, 36*(6), 495–504. https://doi.org/10.1080/10447318.2020.1741118
*Verification:* Crossref (row 14) + OpenAlex (row 15) + arXiv 2002.04087v2 (row 33). *Read status:* **read in full** (arXiv v2; the section cites below are safe, but IJHCI page numbers were not mapped).
Shneiderman replaces the "widely cited, but mind-limiting 1-dimensional Sheridan-Verplank levels of automation/autonomy" with a "two-dimensional framework ... that separates levels of automation/autonomy from levels of human control" (§1, Table 1). The goal is "high levels of human control AND high levels of automation" (§1).
*Role in the DXD argument:* precursor / competing-construct. The framework gives DXD a design space, but it treats control as a property of one user's relation to one system, not of coordination that runs through it.

---

## (c) Thematic synthesis

**Interpreting an opaque, adaptive intermediary.** The literature agrees that people interpret an intermediary through a lay model that forms before and outside the interface. Logg, Minson and Moore call it a "theory of machine," Eslami and colleagues and DeVito call it folk theory, and Bucher calls it the imaginary. That model often forms without help from what the system shows: most of Eslami's (2015) users did not know their feed was filtered. Bansal and colleagues (2019, HCOMP) redefine what interpretation must reach: the error boundary, "when does the AI err?", rather than the mechanism. People learn it from the consequences of their own decisions, and the designer controls how learnable it is through parsimony and stochasticity. Dell'Acqua and colleagues' "jagged frontier" is the same boundary in the field, and it is invisible from inside the workflow.

This is where the literacy paradigm makes its strongest prediction and fares worst. Dzindolet and colleagues (2003) showed that explaining why an aid errs raised reliance "even when the trust was unwarranted." Bansal and colleagues (2021) found that explanations raised acceptance whether the AI was right or wrong. Poursabzi-Sangdeh and colleagues made the model simulable, but not correctable; in two experiments a clear model *lowered* error detection. Vaccaro and colleagues' meta-analysis gives the aggregate: across 370 effect sizes, explanation and confidence displays did not moderate team performance, while task type and the human–AI skill ratio did.

The disagreement is live, not closed. Vasconcelos and colleagues show explanations cutting overreliance when checking them costs less than doing the task. Zhang, Liao and Bellamy show confidence scores calibrating trust. Kulesza and colleagues (2012) show that sound mental models help users steer a recommender. These are the facet's real counterevidence. Each works where the user is the intermediary's only principal, the system is stable, and verification is cheap, which marks the boundary of the literacy paradigm rather than refuting the thesis. When a transparency intervention works, it works through *interaction cost*: the Vasconcelos result is a cognitive-load finding, which puts it in UX's home territory rather than in reading comprehension.

**Specifying intent through the intermediary.** This operation has the thinnest direct evidence and the clearest design lever. Dietvorst and colleagues (2018) found that a trivial modification right, 2 percentiles, bought as much acceptance as 10. What moved people was the existence of a channel for intent, not its bandwidth. Buçinca and colleagues' forcing functions work on a different variable, *when* the human commits a judgment, and that timing changed outcomes where explanation did not. Vaccaro and colleagues found that more than 95% of the studied systems left the human the final decision, and only 3 experiments tested a predetermined division of labour. Cotter's influencers show people specifying intent indirectly, by adapting their conduct to the inferred rule.

**Keeping track as the rule shifts.** This is the operation the classic literature names but hardly measures. Lee and See's temporal specificity and Parasuraman and Manzey's complacency both describe tracking decay. Constant reliability is the worst case for monitoring, which implies that a *good* intermediary erodes tracking fastest. Bansal and colleagues (2019, AAAI) show that a more accurate but incompatible update lowers team performance. Mohanty, Lim and Luther show users detecting model changes at 48.87%, near chance. Glickman and Sharot show users unaware of the extent of the AI's influence on their own judgment. Fernandes and colleagues show users overestimating their AI-aided performance, with higher AI literacy going with *worse* metacognitive accuracy. DeVito's (2021) adaptive folk theorization is the nearest rival construct, and it still places the capacity in the user as a literacy. Amershi's G14 and G18 assume the platform announces rule changes.

**Where the facet leaves the thesis.** The evidence supports the claim that deciding through algorithms raises cognitive issues that reading-and-perception expertise does not address. The same evidence cuts against "make the algorithm legible" as the remedy. One gap matters most: Lai and colleagues, and the design-ethics cards built on this literature, note that the whole corpus studies one decider on the near side of the AI. None of these studies puts the second party of a coordination inside the experiment.

---

## (d) Gaps and unverified leads

**Gaps in the evidence**
- *No study puts two coordinating parties on either side of an intermediary.* Lai et al. (2023, §6) name this gap themselves. It is the construct's home ground and the empirical frontier for DXD.
- *Specifying intent is under-measured.* Vaccaro et al. found only 3 experiments with a predetermined division of labour. I found no experiment on prompt or preference specification as a cognitive task in this search. A targeted search on "prompt specification" or "intent articulation" is the next step (see leads).
- *Keeping track has one controlled study per claim* (Bansal 2019 AAAI; Mohanty 2025), and both use crowdworkers or small samples. There is no longitudinal field study of tracking across real platform rule changes except DeVito's qualitative work.
- *Read-status debt.* Burton 2020, Mahmud 2022, Risko & Gilbert 2016, Kulesza 2012/2013, DeVito 2017/2018, Bastani 2025, Bauer 2023, Glickman 2025 and Fernandes 2026 are abstract-only. Glickman, Bauer (Mannheim accepted version) and Zhang (arXiv 2001.02114) have OA full text I did not read. Parasuraman & Riley 1997 and Dzindolet 2003 remain abstract-only across the repo.

**Unverified or deferred leads** (DOIs from database records this session, but not carded or read)
- Steyvers, M., & Kumar, A. (2023). Three challenges for AI-assisted decision-making. *Perspectives on Psychological Science*. doi:10.1177/17456916231181102 (Consensus row 18; the author list beyond the first author is unverified). Its "mental models of the AI ... contain both expectations of the AI and reliance strategies" is a useful bridge.
- Hatherley, J. (2025). A moving target in AI-assisted decision-making: dataset shift, model updating, and the problem of update opacity. *Ethics and Information Technology*. doi:10.1007/s10676-025-09829-2 (Consensus row 18). "Update opacity" is a ready-made name for the keeping-track problem.
- Fügener, A., Grahl, J., Gupta, A. K., & Ketter, W. (2021). Will humans-in-the-loop become Borgs? *MIS Quarterly, 45*(3), 1527–1556. doi:10.25300/misq/2021/16553 (OpenAlex row 44). AI advice erodes "unique human knowledge" and crowd wisdom.
- Endsley, M. R. (2022). Supporting human-AI teams: Transparency, explainability, and situation awareness. *Computers in Human Behavior*. doi:10.1016/j.chb.2022.107574 (Consensus row 18). It separates transparency for situation awareness from explanation for mental models.
- Pataranutaporn et al. (2023). Priming beliefs about AI. *Nature Machine Intelligence*. doi:10.1038/s42256-023-00720-7 (Consensus row 18). A user's mental model and the AI reinforce each other.
- Gerlich, M. (2025). AI tools in society: Impacts on cognitive offloading and the future of critical thinking. *Societies*. doi:10.3390/soc15010006 (Consensus row 19). It is highly cited (1,153), but it is a cross-sectional survey in an MDPI journal; use with caution, if at all.
- Kosmyna et al. (2025). Your brain on ChatGPT (arXiv 2506.08872). An unrefereed preprint with a published comment (arXiv 2601.00856); do not cite as evidence.
- Jussupow, Benbasat & Heinzl (2020, ECIS) algorithm-aversion review. Crossref returned only their 2024 *MIS Quarterly* paper (doi:10.25300/misq/2024/18512), which is an integrative aversion/appreciation perspective and a possible substitute. The ECIS record was not retrieved.
- Hoff & Bashir (2015) already has a card (`.../algorithmacy_design_ethics/literature/library/hoffbashir2015.md`, abstract-only). I left it out as redundant with Lee & See, but it could replace entry 2 if a post-2004 map is wanted.
- Scholar Gateway failed with an identity error (row 20), so its full-text passage search did not contribute to this facet.
