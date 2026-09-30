# F2 — The decision-science and choice-architecture lineage

*Facet F2 of the Decision Experience Design (DXD) literature review. Agent-drafted on 2026-09-30 (a parallel research agent working in the `wt-dxd` worktree). The author has not reviewed it, and none of the text below is the author's.*

**What this facet covers.** Simon's bounded rationality and its environmental half; framing; the nudge and choice-architecture program; defaults; choice overload; the nudge-effectiveness and publication-bias dispute; boosting; sludge; digital nudging as the Information Systems (IS) bridge to interface design; dark patterns; and the algorithmic turn (the hypernudge, the autonomous choice architect). **The question the synthesis answers:** what does choice architecture already give DXD, and what does it miss once the choice architect is itself an adaptive, opaque algorithm rather than a fixed menu?

**Legend for read status.** *Read in full* = I read the open-access (OA) full text this session, or the entry reuses an existing repo card built from full text. *Read in part* = OA full text obtained and the cited passages located and read, but not the whole paper. *Abstract only* = database abstract or record only. *Not accessible* = no OA text, and the record carries no abstract. Page locators marked "pdf p." are pages of the OA PDF when that PDF is not paginated like the version of record.

---

## (a) Search log

All searches ran on 2026-09-30. "Hits" is the count the source reported. For DOI lookups a hit is one record.

| # | Source | Exact query / request | Hits | Notes |
|---|---|---|---|---|
| 1 | repo grep | `grep -ril` over `submissions/*/literature submissions/*/library org_frontier/research/*/literature` for: Thaler, Sunstein, nudge, Hertwig, boost, hypernudge, Yeung, "dark pattern", Mathur, "Gray, C", Weinmann, "digital nudg", "choice architect", Scheibehenne, Chernev, Iyengar, "Johnson, E", Goldstein, Mertens, Maier, DellaVigna, Tversky, "Simon, H", sludge, "bounded rationality" | 7, 4, 19, 0, 11, 5, 11, 3, 0, 2, 0, 0, 3, 0, 1, 0, 1, 8, 0, 8, 0, 0, 2, 3, 2 files | Reusable cards: `thaler2008.md`, `sunstein2021.md`, `gray2018.md` (design-ethics library), `yeung2017hypernudge.md` (hospitality_phygital), `simon1997.md` (lima_pdw). The "Goldstein"/"Maier" hits were other authors. No card existed for Hertwig, Mathur, Mertens, Weinmann or DellaVigna. |
| 2 | Crossref `/works/{doi}` | 18 seed DOIs (Simon 1955, 1956; Tversky & Kahneman 1981; Johnson et al. 2012; Johnson & Goldstein 2003; Scheibehenne et al. 2010; Chernev et al. 2015; Iyengar & Lepper 2000; Mertens et al. 2022; Maier et al. 2022; DellaVigna & Linos 2022; Hertwig & Grüne-Yanoff 2017; Weinmann et al. 2016; Schneider et al. 2018; Gray et al. 2018; Mathur et al. 2019; Mathur et al. 2021; Yeung 2017) | 18/18 resolved | All brief-supplied DOIs matched title, venue, volume and pages. |
| 3 | OpenAlex `/works/https://doi.org/{doi}` | the 17 seed DOIs above (Gray excluded) | 17/17 | Abstracts and OA locations. Closed: Simon 1955, 1956; T&K 1981; Johnson 2012; Chernev 2015; Iyengar 2000; Mathur 2019 (the arXiv copy was found separately). |
| 4 | Consensus | `boosting versus nudging: building decision competences in digital environments` | 20 | Surfaced Kozyreva et al. 2020, Herzog & Hertwig 2025, Lorenz-Spreen et al. 2020, Hertwig 2017, Grüne-Yanoff 2025 |
| 5 | Consensus | `digital nudging user interface design online choice architecture` | 20 | Schneider et al. CACM abstract, Caraban et al. 2019, Bergram et al. 2022, Jesse & Jannach 2021 |
| 6 | Consensus | `algorithmic nudging personalized choice architecture autonomy manipulation` | 20 | Mills & Sætra 2022, Mills 2020, Lanzing 2019, Michaelsen et al., Zhu & Wang 2026 |
| 7 | Scholar Gateway `semanticSearch` | `How do choice architecture tools such as defaults, the number of options, and decision aids shape consumer decisions, as reviewed in "Beyond nudges: tools of a choice architecture"?` | 0 | **Failed:** `INVALID_QUERY: Could not resolve user identity from CONNECT`. Not retried. Scholar Gateway could not be reached this session. |
| 8 | Consensus | `ethics of nudging autonomy manipulation libertarian paternalism critique` | 20 | Schmidt & Engelen 2020, Hansen & Jespersen 2013, Wilkinson 2013, Vugts et al. 2020 |
| 9 | Consensus | `meta-analysis of default effects when and why defaults influence decisions` | 20 | Jachimowicz et al. 2019, Chandrashekar et al. replication |
| 10 | Crossref `/works/{doi}` | 16 second-wave DOIs (Kozyreva; Lorenz-Spreen; Mills & Sætra; Jachimowicz; Caraban; Schmidt & Engelen; Lanzing; Herzog & Hertwig; Hertwig 2017; Susser et al.; Thaler 2018; Hansen & Jespersen; Bergram; Zhu & Wang; Mills 2020 BPP; Jesse & Jannach) | 16/16 | |
| 11 | Crossref `query.bibliographic` | `Szaszi No reason to expect large and consistent effects of nudge interventions` / `Mertens Reply to Maier Szaszi Bakdash present and future of choice architecture` / `Michaelsen Experiencing default nudges autonomy manipulation choice-satisfaction` | 2 / 2 / 2 shown | Resolved the PNAS letters, the Mertens reply and the BPP version of Michaelsen et al. |
| 12 | Crossref `query.bibliographic`, `filter=prefix:10.1073` | `Correction for Mertens effectiveness of nudging meta-analysis` | 5 shown | Found correction 10.1073/pnas.2204059119 (4 May 2022) |
| 13 | Europe PMC REST | `PMC8740589`, `PMC9351449`, `PMC9171817`, `PMC7745618` fullTextXML | 4 | Full text: Mertens et al., Mertens reply, the Mertens correction, Kozyreva et al. |
| 14 | Europe PMC search | `DOI:10.1126/science.1091721`, `DOI:10.1037/0022-3514.79.6.995`, `DOI:10.1037/h0042769`, `DOI:10.1126/science.7455683` | 1, 0, 1, 1 | Only the T&K 1981 record has an abstract |
| 15 | Semantic Scholar Graph API | `paper/DOI:{doi}?fields=title,openAccessPdf,abstract,tldr` for 9 DOIs | 6 found, 3 "not found" | 3-second sleeps; no rate-limit errors. Abstracts elided by publisher for Hertwig, Lorenz-Spreen and Johnson 2012 (machine TLDR only). |
| 16 | Direct OA fetch (curl) | PDFs from UvA-DARE (Maier), KCL Pure (Yeung AAM), arXiv 1907.07032 and 2101.04843 (Mathur), NBER w27594 (DellaVigna), MPG PuRe (Hertwig), LSE Research Online (Mills & Sætra), Cambridge Core OA (Jachimowicz; Michaelsen), Internet Policy Review (Susser), Glasgow eprints (Szaszi), DigitUMa (Caraban), open.lnu.se (Chandrashekar) | 13 obtained | Blocked or bot-walled (HTML returned): edoc.unibas (Scheibehenne), SSRN (Johnson & Goldstein), Springer (Weinmann), ACM DL and cacm.acm.org (Schneider), Nature and Bristol (Lorenz-Spreen), CityU repository (Weinmann). I did not try to get around any block. |
| 17 | WebFetch | `link.springer.com/article/10.1007/s12599-016-0453-1`; `cacm.acm.org/research/digital-nudging/`; `doi.org/10.15626/mp.2022.3108` | 0 / 0 / redirect | Springer redirected to login; CACM returned 403; Meta-Psychology was fetched instead by curl (row 16) |
| 18 | Consensus | `When choice is demotivating: can one desire too much of a good thing? jam display extensive versus limited choice` | 19 | Iyengar & Lepper abstract |
| 19 | Consensus | `Do defaults save lives? organ donation opt-out opt-in consent rates` | 20 | Johnson & Goldstein record; counterevidence from Dallacker et al. 2024 and Arshad et al. 2019 |
| 20 | Consensus | `sludge excessive friction administrative burden behavioral public policy` | 20 | Sunstein 2020 *Sludge Audits*, Mills 2020 nudge/sludge symmetry, Madsen et al. 2021 |
| 21 | Crossref `/works/{doi}` | Dallacker 2024; Arshad 2019; Mills 2020 BPP; Sunstein 2020 BPP; Michaelsen BPP; Chandrashekar 2023; Todd & Gigerenzer 2003; Mills 2022 TechSoc; Callaway 2022; Szaszi 2022; Mertens reply; Kahneman 2003; Grüne-Yanoff 2025 | 13/13 | |
| 22 | OpenAlex snowball | `filter=cites:W2396457900,title_and_abstract.search:boost OR literacy OR competence` (works citing Yeung 2017) | 23 | Surfaced Leaver 2020 (*BJET*), Mills 2022 *AI & Society* "user control" |
| 23 | OpenAlex snowball | `filter=cites:W2743157434,title_and_abstract.search:algorithm OR algorithmic OR recommender OR artificial intelligence` (works citing Hertwig & Grüne-Yanoff 2017) | 36 | Surfaced Callaway et al. 2022 *PNAS*, Lieder et al. 2019 *NHB* |
| 24 | OpenAlex snowball | `filter=cites:W3192963099,title_and_abstract.search:dark pattern` (works citing Weinmann et al. 2016) | 13 | Surfaced Gray et al. 2021 *PACM-HCI* "felt manipulation" |
| 25 | OpenAlex | `filter=title_and_abstract.search:hypernudge` | 20 | Surfaced Mills 2022 *Technology in Society* "Finding the 'nudge' in hypernudge" |
| 26 | Consensus | `Simon 1956 rational choice and the structure of the environment organism satisficing` | 19 | Extended opening text of Simon 1956; Todd & Gigerenzer 2003 |
| 27 | Consensus | `Simon 1955 a behavioral model of rational choice bounded rationality` | 20 | Kahneman 2003 abstract (secondary statement of Simon 1955) |

Snowballing (rule 7): I ran citing-work filters on the three most central hits for the DXD question — Yeung 2017, Hertwig & Grüne-Yanoff 2017, Weinmann et al. 2016 (rows 22–24) — and read the reference trail of Mertens et al. 2022 through its correction and the three PNAS letters (rows 11–13).

---

## (b) Entries

Entries follow the facet's argument, not the alphabet: bounded rationality → framing and the nudge → the choice-architecture toolkit → defaults → choice overload → the effectiveness dispute → boosting → sludge → digital nudging → dark patterns → the algorithmic choice architect → autonomy.

### B1. Bounded rationality: the environment half

**simon1955behavioral** — Simon, H. A. (1955). A behavioral model of rational choice. *The Quarterly Journal of Economics, 69*(1), 99–118. https://doi.org/10.2307/1884852
- *Verification:* Crossref record (vol. 69, issue 1, first page 99); OpenAlex W2148962857; Consensus record. The end page, 118, comes from the OpenAlex/Consensus table of contents ("Appendix, 115") together with the conventional citation; Crossref lists only "99". **Check the end page before print.**
- *Read status:* not accessible. The OpenAlex/Consensus "abstract" is the table of contents: "Introduction, 99. — I. Some general features of rational choice, 100.— II. The essential simplifications, 103. — III. Existence and uniqueness of solutions, 111. — IV. Further comments on dynamics, 113. — V. Conclusion, 114. — Appendix, 115."
- *What it establishes:* I did not read the paper. Kahneman's (2003) Nobel-lecture abstract, retrieved via Consensus, gives the canonical secondary statement: "Herbert A. Simon (1955, 1979) had proposed much earlier that decision makers should be viewed as boundedly rational, and had offered a model in which utility maximization was replaced by satisficing." Kahneman then describes the heuristics-and-biases program as an attempt "to obtain a map of bounded rationality, by exploring the systematic biases" — the reading that nudging later inherited.
- *Role in the DXD argument:* precursor (the founding claim that choice runs on limited computation, which is what makes the design of the choice environment matter at all).

**simon1956rational** — Simon, H. A. (1956). Rational choice and the structure of the environment. *Psychological Review, 63*(2), 129–138. https://doi.org/10.1037/h0042769
- *Verification:* Crossref; OpenAlex W1989388297; Consensus record carrying the paper's opening text.
- *Read status:* abstract only. What I read is the opening paragraphs as the Consensus and OpenAlex records reproduce them (these sit on p. 129; I have no page image to confirm the break).
- *What it establishes:* Simon states that "organisms adapt well enough to 'satisfice'; they do not, in general, 'optimize,'" and draws the design-relevant consequence: "a great deal can be learned about rational decision making by taking into account, at the outset, the limitations upon the capacities and complexity of the organism, and by taking account of the fact that the environments to which it must adapt possess properties that permit further simplication [sic] of its choice mechanisms." Todd and Gigerenzer (2003, abstract, via Consensus) later render this as the two blades of a scissors — internal and environmental bounds that "may fit together like the blades in a pair of scissors."
- *Role in the DXD argument:* precursor (the environment-shapes-choice half of bounded rationality, which is DXD's ancestral premise; the ecological-rationality reading is what boosting builds on).

**todd2003bounding** — Todd, P. M., & Gigerenzer, G. (2003). Bounding rationality to the world. *Journal of Economic Psychology, 24*(2), 143–165. https://doi.org/10.1016/S0167-4870(02)00200-3
- *Verification:* Crossref; Consensus record with abstract.
- *Read status:* abstract only.
- *What it establishes:* Todd and Gigerenzer argue that Simon's internal and external bounds are not independent; the mind can "take advantage of this fit to make good decisions, by using mental mechanisms whose internal structure exploits the external information structures available in the environment" (abstract). They thereby separate a third reading of bounded rationality from both "optimization under constraints" and "cognitive illusions."
- *Role in the DXD argument:* competing-construct (the ecological-rationality reading of Simon, set against the biases reading; it is the theoretical root of boosting).

### B2. Framing and the nudge

**tversky1981framing** — Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science, 211*(4481), 453–458. https://doi.org/10.1126/science.7455683
- *Verification:* Crossref; Europe PMC PMID 7455683 (abstract); OpenAlex.
- *Read status:* abstract only.
- *What it establishes:* The abstract reports that "the psychological principles that govern the perception of decision problems and the evaluation of probabilities and outcomes produce predictable shifts of preference when the same problem is framed in different ways," with reversals "in choices regarding monetary outcomes, both hypothetical and real, and in questions pertaining to the loss of human lives." Tversky and Kahneman explicitly compare "the effects of frames on preferences … to the effects of perspectives on perceptual appearance" — the bridge from perception research to decision research that UX later travelled.
- *Role in the DXD argument:* UX-cognitive-foundation (presentation alone moves choice; the perceptual analogy links the literacy-era UX canon to decision design).

**thaler2008nudge** — Thaler, R. H., & Sunstein, C. R. (2008). *Nudge: Improving decisions about health, wealth, and happiness*. Yale University Press.
- *Verification:* existing card `submissions/algorithmacy_design_ethics/literature/library/thaler2008.md` (S2-verified 2026-09-18 against the Semantic Scholar record of Thaler, 2018, *Science* 361(6401), 431, doi:10.1126/science.aau9241). No ISBN was verified for the book.
- *Read status:* not accessible (the book is not OA). The card rests on Thaler's (2018) editorial.
- *What it establishes:* Thaler's own later summary (quoted on the card): "By improving the environment in which people choose—what we call the 'choice architecture'—they can make wiser choices without restricting any options," and the conscientious architect helps people choose "'as judged by themselves.'" **Two definitions of a nudge circulate, and DXD should cite deliberately.** Yeung (2017, abstract) gives the widely used one — "a particular form of choice architecture that alters people's behaviour in a predictable way without forbidding any options or significantly changing their economic incentives" — as do Caraban et al. (2019, p. 2). Mathur et al. (2021, p. 12) quote a different formula: "private or public initiatives that steer people in particular directions but that also allow them to go their own way." Neither was checked against the book.
- *Role in the DXD argument:* precursor / term-use (the source of "choice architect" and "choice architecture," and of the "as judged by themselves" criterion).

### B3. The choice-architecture toolkit

**johnson2012beyond** — Johnson, E. J., Shu, S. B., Dellaert, B. G. C., Fox, C., Goldstein, D. G., Häubl, G., Larrick, R. P., Payne, J. W., Peters, E., Schkade, D., Wansink, B., & Weber, E. U. (2012). Beyond nudges: Tools of a choice architecture. *Marketing Letters, 23*(2), 487–504. https://doi.org/10.1007/s11002-012-9186-1
- *Verification:* Crossref (12 authors, 23(2), 487–504); Semantic Scholar record.
- *Read status:* not accessible. The publisher elides the abstract in Semantic Scholar; OpenAlex marks the paper closed.
- *What it establishes:* I could verify only the paper's organizing move, and that through Semantic Scholar's machine-generated TLDR rather than the authors' words: it "outlines the tools available to choice architects, that is anyone who present people with choices, and divides these tools into two categories: those used in structuring the choice task and those used in describing the choice options." Treat the structure/description split as the paper's frame only once someone checks it against the text. Mertens et al.'s (2022) meta-analytic categories ("decision structure," "decision information," "decision assistance") descend from this taxonomy.
- *Role in the DXD argument:* precursor (the practitioner toolkit that UX designers already use — defaults, option count, attribute translation — named as choice architecture).

### B4. Defaults

**johnson2003defaults** — Johnson, E. J., & Goldstein, D. (2003). Do defaults save lives? *Science, 302*(5649), 1338–1339. https://doi.org/10.1126/science.1091721
- *Verification:* Crossref; OpenAlex (abstract); Consensus record. Consensus attaches a book-chapter reprint DOI (10.1017/cbo9780511618031.038); the version of record is the *Science* DOI above.
- *Read status:* abstract only. The OA copy on SSRN was blocked ("Content Blocked").
- *What it establishes:* The OpenAlex abstract says the authors "use natural and experimental data to examine the impact of simple policy defaults on the decision to become an organ donor, finding large effects that significantly increase donation rates." The famous online-experiment figures reach me only secondhand: Chandrashekar et al. (2023, pdf p. 3) report that participants were more likely to agree "to donate (82%) than when the default option was to not donate (42%)." **I have not verified the country-level consent rates against the Science text.**
- *Role in the DXD argument:* UX-cognitive-foundation (the single most-cited demonstration that a no-action option is itself a design decision).

**chandrashekar2023defaults** — Chandrashekar, S. P., Adelina, N., Zeng, S., Chiu, Y. Y. E., Leung, G. Y. S., Henne, P., Cheng, B. L., & Feldman, G. (2023). Defaults versus framing: Revisiting default effect and framing effect with replications and extensions of Johnson and Goldstein (2003) and Johnson, Bellman, and Lohse (2002). *Meta-Psychology, 7*. https://doi.org/10.15626/MP.2022.3108
- *Verification:* Crossref; Consensus record (abstract); OA PDF from open.lnu.se.
- *Read status:* read in part (abstract and the combined-results table, pdf p. 8).
- *What it establishes:* In "two well-powered samples (N = 1920)" the authors "successfully replicated Johnson and Goldstein (2003)" but "failed to replicate" Johnson, Bellman and Lohse (2002), finding a framing effect instead (abstract). The replicated gap is far smaller than the original. Participation ran at opt-in 62.5% (n = 488), opt-out 73.5% (n = 476) and no-default 69.7% (n = 482) (pdf p. 8, combined replication table), against the 82% vs 42% they report for the original. They conclude that "default effects depend on framing and context" (abstract).
- *Role in the DXD argument:* counterevidence (the flagship default effect survives replication at a fraction of its original size).

**jachimowicz2019defaults** — Jachimowicz, J. M., Duncan, S., Weber, E. U., & Johnson, E. J. (2019). When and why defaults influence decisions: A meta-analysis of default effects. *Behavioural Public Policy, 3*(2), 159–186. https://doi.org/10.1017/bpp.2018.43
- *Verification:* Crossref; Consensus; OA PDF (Cambridge Core).
- *Read status:* read in part (abstract p. 159; introduction p. 161; funnel and trim-and-fill section, pdf p. 8).
- *What it establishes:* Across "58 default studies (pooled n = 73,675)" the authors find "a considerable influence of defaults (d = 0.68, 95% confidence interval = 0.53–0.83)" with "substantial variation," including "two [that] even demonstrate negative effects" (p. 159). Defaults work better in consumer domains than in environmental ones, and better "when they operate through endorsement (defaults that are seen as conveying what the choice architect thinks the decision-maker should do) or endowment" (p. 159). On publication bias they report that "if anything – larger effect sizes are underreported" (p. 161).
- *Role in the DXD argument:* algorithmacy-cognitive-issue (the *endorsement* channel — users read a default as a message from the architect — is exactly the inference that becomes hard when the architect is an opaque, adaptive system).

*Counterevidence on outcomes (brief, abstract only via Consensus, Crossref-verified):* Dallacker, Appelius, Brandmaier, Morais and Hertwig (2024, *Public Health*, 236, 436–440, doi:10.1016/j.puhe.2024.08.009) found in five countries that switched to opt-out that "switching from an opt-in to an opt-out default did not result in an increase in donation rates when averaged across countries." Arshad, Anderson and Sharif (2019, *Kidney International*, 95(6), 1453–1460, doi:10.1016/j.kint.2019.01.036), comparing 35 OECD countries, report opt-out countries had "fewer living donors per million population (4.8 versus 15.7, respectively) with no significant difference in deceased donors (20.3 versus 15.4, respectively)." A default can move the recorded choice without moving the outcome the choice was meant to serve.

### B5. Choice overload

**iyengar2000choice** — Iyengar, S. S., & Lepper, M. R. (2000). When choice is demotivating: Can one desire too much of a good thing? *Journal of Personality and Social Psychology, 79*(6), 995–1006. https://doi.org/10.1037/0022-3514.79.6.995
- *Verification:* Crossref; Consensus record (abstract).
- *Read status:* abstract only.
- *What it establishes:* Across three studies "conducted in both field and laboratory settings," people were "more likely to purchase gourmet jams or chocolates or to undertake optional class essay assignments when offered a limited array of 6 choices rather than a more extensive array of 24 or 30 choices," and reported "greater subsequent satisfaction" and "wrote better essays" (abstract). The famous 30% vs 3% jam-purchase figures do not appear in the abstract; I saw them only in a low-tier secondary source (Tung et al., 2014, conference abstract via Consensus) and have **not** verified them.
- *Role in the DXD argument:* UX-cognitive-foundation (the origin of "fewer options" as design folklore).

**scheibehenne2010choice** — Scheibehenne, B., Greifeneder, R., & Todd, P. M. (2010). Can there ever be too many options? A meta-analytic review of choice overload. *Journal of Consumer Research, 37*(3), 409–425. https://doi.org/10.1086/651235
- *Verification:* Crossref; OpenAlex abstract; Consensus.
- *Read status:* abstract only. The OA copies at edoc.unibas.ch and archive-ouverte.unige.ch returned bot-wall HTML.
- *What it establishes:* "In a meta-analysis of 63 conditions from 50 published and unpublished experiments (N=5,036), we found a mean effect size of virtually zero but considerable variance between studies." They could name "no sufficient conditions" for overload (abstract).
- *Role in the DXD argument:* counterevidence (a canonical UX heuristic averages to zero).

**chernev2015choice** — Chernev, A., Böckenholt, U., & Goodman, J. (2015). Choice overload: A conceptual review and meta-analysis. *Journal of Consumer Psychology, 25*(2), 333–358. https://doi.org/10.1016/j.jcps.2014.08.002
- *Verification:* Crossref; OpenAlex abstract; Consensus.
- *Read status:* abstract only.
- *What it establishes:* In "a meta-analysis of 99 observations (N = 7202)," four moderators — "choice set complexity, decision task difficulty, preference uncertainty, and decision goal" — each have "a reliable and significant impact on choice overload." Once these are modelled, "the overall effect of assortment size on choice overload is significant—a finding counter to the data reported by prior meta-analytic research" (abstract).
- *Role in the DXD argument:* UX-cognitive-foundation (overload is conditional, and its conditions — complexity, difficulty, preference uncertainty — are properties the designer controls).

### B6. Does choice architecture work? The effectiveness dispute

**mertens2022effectiveness** — Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. *Proceedings of the National Academy of Sciences, 119*(1), e2107346118. https://doi.org/10.1073/pnas.2107346118 — with Correction, *PNAS, 119*(19), e2204059119 (2022), https://doi.org/10.1073/pnas.2204059119
- *Verification:* Crossref (article and correction); Europe PMC full text PMC8740589 (the original as archived) and PMC9171817 (the correction).
- *Read status:* read in full (the original) and read in full (the correction notice and its corrected Table 2).
- *What it establishes:* The original reports "455 effect sizes from 214 publications (N = 2,149,683)" and "Cohen's d = 0.45, 95% CI [0.39, 0.52]" (Results). Egger's test gave b = 2.28, 95% CI [1.31, 3.25]; the effect attenuated to d = 0.31 under moderate and d = 0.03 under severe one-tailed publication bias, an assumption the authors say "was only partially supported by the funnel plot." **The correction changes these numbers.** The authors removed "four observations from a paper by Shu et al. (2012) that now has been retracted," fixed two erroneous values and "several coding errors," and reported in corrected Table 2 an overall d = 0.43 [0.38, 0.48] (k = 447, n = 2,148,439). By category the corrected estimates are decision structure d = 0.54, decision information d = 0.34 and decision assistance d = 0.28; by technique, defaults d = 0.62 and commitment d = 0.23; by domain, food d = 0.65 and finance d = 0.24. The reply letter (below) gives the corrected Egger coefficient as b = 2.10 and the severe-bias estimate as d = 0.08. **Cite the corrected figures.**
- *Role in the DXD argument:* precursor / counterevidence (the strongest pooled case that choice architecture moves behavior, and that structure beats information, qualified by a correction and a bias dispute).

**maier2022noevidence** — Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No evidence for nudging after adjusting for publication bias. *Proceedings of the National Academy of Sciences, 119*(31), e2200300119. https://doi.org/10.1073/pnas.2200300119
- *Verification:* Crossref; OA PDF (UvA-DARE, CC BY).
- *Read status:* read in full (a two-page letter).
- *What it establishes:* Maier and colleagues re-analyzed Mertens et al.'s corrected data with robust Bayesian meta-analysis (RoBMA). Table 1 gives the unadjusted random-effects estimate as 0.43 [0.38, 0.48]. RoBMA-PSMA gives 0.04 [0.00, 0.14], BF01 = 0.95, and 0.11 [0.00, 0.24], BF01 = 0.31, using only the most precise estimates. For "structure" interventions the adjusted estimate is 0.12 [0.00, 0.43], BF01 = 1.12 ("the evidence is undecided"). They find "strong evidence for publication bias across all subdomains (BFpb > 10), apart from food" and conclude that "after correcting for this bias, no evidence remains that nudges are effective as tools for behaviour change" (p. 2). They add that "all intervention categories and domains apart from 'finance' show evidence for heterogeneity, which implies that some nudges might be effective" (p. 1).
- *Role in the DXD argument:* counterevidence.

**szaszi2022noreason** — Szaszi, B., Higney, A., Charlton, A., Gelman, A., Ziano, I., Aczel, B., Goldstein, D. G., Yeager, D. S., & Tipton, E. (2022). No reason to expect large and consistent effects of nudge interventions. *Proceedings of the National Academy of Sciences, 119*(31), e2200732119. https://doi.org/10.1073/pnas.2200732119
- *Verification:* Crossref; OA PDF (Glasgow eprints 332831).
- *Read status:* read in full (letter).
- *What it establishes:* Three bias-correcting methods applied to Mertens et al.'s data give "much smaller effect sizes (Andrews–Kasy, d = 0.01, SE = 0.02; weighted average of the adequately powered [WAAP], d = 0.07, SE = 0.03; Trim and fill, d = 0.08, SE = 0.03)." Assuming severe bias, "95% of these studies' effects would be ±1.00 around the average." The letter's co-author list includes Daniel G. Goldstein of the 2003 defaults paper.
- *Role in the DXD argument:* counterevidence (heterogeneity, not the average, is the finding a designer needs).

**mertens2022reply** — Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). Reply to Maier et al., Szaszi et al., and Bakdash and Marusich: The present and future of choice architecture research. *Proceedings of the National Academy of Sciences, 119*(31), e2202928119. https://doi.org/10.1073/pnas.2202928119
- *Verification:* Crossref; Europe PMC full text PMC9351449.
- *Read status:* read in full.
- *What it establishes:* Mertens and colleagues concede the bias ("We agree that the publication bias observed in the current choice architecture literature is problematic") and restate the corrected figures (d = 0.43; Egger b = 2.10, 95% CI [1.31, 2.89]; d = 0.31 moderate and d = 0.08 severe). They endorse Szaszi et al.'s call to "understand when and where some nudges have huge positive effects and why others are not able to repeat those successes."
- *Role in the DXD argument:* counterevidence (the parties converge on heterogeneity and moderators as the research program).

**dellavigna2022rcts** — DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica, 90*(1), 81–116. https://doi.org/10.3982/ECTA18709
- *Verification:* Crossref; OpenAlex abstract (published version); NBER Working Paper 27594 (OA).
- *Read status:* read in full (NBER WP version); headline numbers taken from the published abstract.
- *What it establishes:* Across "126 RCTs covering 23 million individuals, including all trials run by two of the largest Nudge Units in the United States," the average academic-journal nudge has "an 8.7 percentage point take-up effect, which is a 33.4% increase over the average control," against "1.4 percentage points, an 8.0% increase" in Nudge Unit trials. "Selective publication in the Academic Journals sample, exacerbated by low statistical power, explains about 70 percent of the difference" (Econometrica abstract). The NBER draft's abstract page gives 33.5% and 8.1%; cite the published figures.
- *Role in the DXD argument:* counterevidence (at-scale design effects are real but roughly one-sixth of the published ones — the gap a DXD practice must price in).

### B7. Boosting: building competence instead of steering

**hertwig2017nudging** — Hertwig, R., & Grüne-Yanoff, T. (2017). Nudging and boosting: Steering or empowering good decisions. *Perspectives on Psychological Science, 12*(6), 973–986. https://doi.org/10.1177/1745691617702496
- *Verification:* Crossref; OA PDF via MPG PuRe (item_2513866, publisher version under Alliance licence).
- *Read status:* read in full.
- *What it establishes:* "The objective of boosts is to foster people's competence to make their own choices—that is, to exercise their own agency" (p. 973, abstract). Table 1 (p. 974) sets nudges and boosts apart on seven dimensions. The intervention target is "Behavior" for nudges and "Competences" for boosts. The assumed cognitive architecture is "Dual-system" against "Cognitive architectures are malleable." The reversibility criterion reads: nudges — "Once intervention is removed, behavior reverts to preintervention state"; boosts — "Implied effects should persist once (successful) intervention is removed." The normative rows read: nudges "Might violate autonomy and transparency"; boosts are "Necessarily transparent and require cooperation—an offer that may or may not be accepted." Two further points matter for DXD. Boosts need not be training: "competences are often best fostered by redesigning aspects of individuals' external environment or by teaching them how to redesign them" (p. 980). And they cite a tutorial-trained frequency-representation competence that was "robust after 15 weeks, with no drop in performance" (p. 977, citing Sedlmeier & Gigerenzer, 2001).
- *Role in the DXD argument:* competing-construct / precursor (the closest existing analogue of "DXD should build algorithmacy": an intervention whose target is the person's competence, not the choice).

**kozyreva2020citizens** — Kozyreva, A., Lewandowsky, S., & Hertwig, R. (2020). Citizens versus the internet: Confronting digital challenges with cognitive tools. *Psychological Science in the Public Interest, 21*(3), 103–156. https://doi.org/10.1177/1529100620946707
- *Verification:* Crossref; Consensus; Europe PMC full text PMC7745618 (CC BY).
- *Read status:* read in part (abstract; the introduction; Table 1 glossary).
- *What it establishes:* The authors describe online environments as "replete with smart, highly adaptive choice architectures designed primarily to maximize commercial interests." They identify "four major types of challenges": "persuasive and manipulative choice architectures, AI-assisted information architectures, false and misleading information, and distracting environments." They distinguish "nudges, technocognition, and boosts" (abstract). New features arrive "on a continuous basis, making it nearly impossible for most users, let alone regulators, to keep abreast of the inner workings of their digital surroundings" (Introduction). The Table 1 glossary defines a boost as a "Cognitive intervention that aims to foster people's competencies. Boosts target cognition (e.g., simple rules for online reasoning) and the environment (e.g., pop-ups with information about the online source)," and technocognition as "Cognitively inspired technological intervention in information architectures (e.g., introducing friction in the process of sharing offensive material)." Their remedy language is literacy language: "boosting their information literacy and their cognitive resistance to manipulation" (abstract).
- *Role in the DXD argument:* competing-construct (boosting ported to adaptive, algorithmic environments — and framed as *literacy*, which the design-ethics arm says algorithmacy is not).

**lorenzspreen2020behavioural** — Lorenz-Spreen, P., Lewandowsky, S., Sunstein, C. R., & Hertwig, R. (2020). How behavioural sciences can promote truth, autonomy and democratic discourse online. *Nature Human Behaviour, 4*(11), 1102–1109. https://doi.org/10.1038/s41562-020-0889-7
- *Verification:* Crossref (four authors, including Sunstein); Consensus abstract.
- *Read status:* abstract only (the Nature page served a paywall preview; the Bristol accepted manuscript was bot-walled).
- *What it establishes:* The current ecosystem "has been designed predominantly to capture user attention rather than to promote deliberate cognition and autonomous choice," with "finely tuned personalization and distorted social cues" paving "the way for manipulation." The authors propose surfacing cues about "the factors underlying algorithmic decisions" and "map out two classes of behavioural interventions—nudging and boosting" (abstract). Sunstein, co-author of *Nudge*, is among the authors.
- *Role in the DXD argument:* competing-construct (the nudge program's own authors accept boosting for algorithmic environments).

**callaway2022leveraging** — Callaway, F., Jain, Y. R., van Opheusden, B., Das, P., Iwama, G., Gul, S., Krueger, P. M., Becker, F., Griffiths, T. L., & Lieder, F. (2022). Leveraging artificial intelligence to improve people's planning strategies. *Proceedings of the National Academy of Sciences, 119*(12), e2117432119. https://doi.org/10.1073/pnas.2117432119
- *Verification:* Crossref; OpenAlex abstract (found by snowballing works that cite Hertwig & Grüne-Yanoff 2017, log row 23).
- *Read status:* abstract only.
- *What it establishes:* An AI system discovers optimal decision heuristics and an "intelligent tutor" teaches them. "Practice with our intelligent tutor was more effective than conventional approaches to improving human decision making," and the benefits "transferred to a more challenging task and were retained over time" (abstract).
- *Role in the DXD argument:* precursor (an algorithm deployed as a boost rather than a nudge — building the person's strategy instead of steering the choice; it trains competence *with* an algorithm, not competence *about* one).

### B8. Sludge

**sunstein2020sludge** — Sunstein, C. R. (2022). Sludge audits. *Behavioural Public Policy, 6*(4), 654–673. https://doi.org/10.1017/bpp.2019.32 (first published online 2020)
- *Verification:* Crossref (issued 2020-01-06; volume 6, issue 4); Consensus abstract. Related existing card: `submissions/algorithmacy_design_ethics/literature/library/sunstein2021.md` (Sunstein's *Sludge*, 2021; the card rests on the SSRN draft of "Sludge and Ordeals"; its S2 check could not re-verify the draft quotations).
- *Read status:* abstract only.
- *What it establishes:* Sludge is "excessive or unjustified frictions, such as paperwork burdens, that cost time or money; that may make life difficult to navigate; that may be frustrating, stigmatizing or humiliating; and that might end up depriving people of access to important goods, opportunities and services." Because of "behavioral biases and cognitive scarcity, sludge can have much more harmful effects than private and public institutions anticipate," and institutions "should regularly conduct Sludge Audits" (abstract). Mathur et al. (2021, p. 12) quote this definition as the nudge authors' own turn toward "nudges that induce excessive or unjustified friction."
- *Role in the DXD argument:* precursor (friction as a designed quantity with a valence set by whose goal it serves).

### B9. Digital nudging: the IS bridge to interface design

**weinmann2016digital** — Weinmann, M., Schneider, C., & vom Brocke, J. (2016). Digital nudging. *Business & Information Systems Engineering, 58*(6), 433–436. https://doi.org/10.1007/s12599-016-0453-1
- *Verification:* Crossref; OpenAlex (OA status "hybrid," but every OA copy was bot-walled).
- *Read status:* not accessible. OpenAlex's "abstract" is a keyword list: "Nudging, Information systems design, Human–computer interaction, Online choice architecture." Semantic Scholar conflates the record with the CACM piece.
- *What it establishes:* Only the bibliographic fact that BISE ran a four-page "Digital Nudging" piece by these authors in 2016. Its definition could not be verified from the BISE text; the definition below comes from the CACM article.
- *Role in the DXD argument:* term-use (the IS field's coinage of "digital nudging").

**schneider2018digital** — Schneider, C., Weinmann, M., & vom Brocke, J. (2018). Digital nudging: Guiding online user choices through interface design. *Communications of the ACM, 61*(7), 67–73. https://doi.org/10.1145/3213765
- *Verification:* Crossref (title recorded as "Digital nudging," 61(7), 67–73); Consensus record for "Digital Nudging–Guiding Choices by Using Interface Design" (Schneider et al., *CACM*), which carries the abstract.
- *Read status:* abstract only (ACM DL and cacm.acm.org returned 403).
- *What it establishes:* "No choice is made in a vacuum, as there is no neutral way to present choices." "The more decisions people make using digital devices, the more the software engineer becomes a choice architect who knowingly or unknowingly influences people's decisions." They define "'digital nudging' as the use of user-interface design elements to guide people's behavior in digital choice environments" and "present a digital nudge design process" (abstract).
- *Role in the DXD argument:* precursor / term-use (the explicit move from choice architect to UI designer — the step DXD extends from interface element to adaptive intermediary).

**caraban2019ways** — Caraban, A., Karapanos, E., Gonçalves, D., & Campos, P. (2019). 23 ways to nudge: A review of technology-mediated nudging in human-computer interaction. In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (Paper 503, pp. 1–15). ACM. https://doi.org/10.1145/3290605.3300733
- *Verification:* Crossref (pp. 1–15); Consensus; OA PDF (DigitUMa repository, hdl 10400.13/4638).
- *Read status:* read in part (abstract; contributions, p. 2). The OA PDF's running head reads "CHI 2019 Paper" / "Paper 503."
- *What it establishes:* From HCI venues the authors identify "23 distinct mechanisms of nudging developed within HCI, clustered in 6 overall categories," which "combat or leverage 15 different cognitive biases and heuristics." They analyze ethical risk along two axes: "the mode of thinking they engage (i.e. automatic vs. reflective) and the transparency of the nudge (i.e. if the user can perceive the intentions and means behind the nudge)" (p. 2).
- *Role in the DXD argument:* UX-cognitive-foundation (HCI's own catalogue of choice architecture; its transparency axis assumes that intentions are perceivable, which adaptive systems undercut).

### B10. Dark patterns: DXD's shadow

**gray2018dark** — Gray, C. M., Kou, Y., Battles, B., Hoggatt, J., & Toombs, A. L. (2018). The dark (patterns) side of UX design. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (Paper 534, pp. 1–14). ACM. https://doi.org/10.1145/3173574.3174108
- *Verification:* existing card `submissions/algorithmacy_design_ethics/literature/library/gray2018.md` (built from the NSF PAR accepted manuscript; S2-verified 2026-09-18, verdict "confirmed"); Crossref.
- *Read status:* read in full (per card).
- *What it establishes:* Gray and colleagues define dark patterns as "instances where designers use their knowledge of human behavior (e.g., psychology) and the desires of end users to implement deceptive functionality that is not in the user's best interest" (p. 1). From 118 artifacts they derive five strategies: nagging, obstruction, sneaking, interface interference and forced action (p. 5). They observe that "some instances of dark patterns test well from a usability perspective (e.g., forced action, nagging), but do so at the expense of user choice" (p. 8).
- *Role in the DXD argument:* counterevidence / precursor (the UX discipline's own evaluation metrics fail to catch decision harm — the gap a DXD evaluation practice must close).

**mathur2019dark** — Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A. (2019). Dark patterns at scale: Findings from a crawl of 11K shopping websites. *Proceedings of the ACM on Human-Computer Interaction, 3*(CSCW), Article 81, 1–32. https://doi.org/10.1145/3359183
- *Verification:* Crossref (3, CSCW, 1–32); OA arXiv:1907.07032v2 (article number 81 shown in the running head).
- *Read status:* read in part (abstract p. 1; contributions p. 2; taxonomy passages p. 17).
- *What it establishes:* "Analyzing ∼53K product pages from ∼11K shopping websites, we discover 1,818 dark pattern instances, together representing 15 types and 7 broader categories … 183 websites that engage in such practices. We also uncover 22 third-party entities that offer dark patterns as a turnkey solution" (p. 1). The authors found "the majority are covert, deceptive, and information hiding in nature," and "many patterns exploit cognitive biases, such as the default and framing effects" (p. 2).
- *Role in the DXD argument:* counterevidence (choice architecture as a commodity sold by third parties, running on the same default and framing effects as B2–B4).

**mathur2021dark** — Mathur, A., Kshirsagar, M., & Mayer, J. (2021). What makes a dark pattern… dark? Design attributes, normative considerations, and measurement methods. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–18). ACM. https://doi.org/10.1145/3411764.3445610
- *Verification:* Crossref (pp. 1–18); OA arXiv:2101.04843v1. The arXiv ACM reference line says "27 pages," and the arXiv author order is Mathur, Mayer, Kshirsagar; Crossref orders them Mathur, Kshirsagar, Mayer. **Use the Crossref order.**
- *Read status:* read in part (§1; §2.4, pdf p. 9; §3.1, pdf p. 12; §4, pdf pp. 13–18).
- *What it establishes:* Mathur and colleagues recast the dark-patterns literature as choice architecture: attributes that are "asymmetric, covert, or restrictive, or that involve disparate treatment, attempt to influence user decisions by modifying the set of choices," while "deceptive or information hiding" ones manipulate "the information that is available to users. Ultimately, both of these themes reflect how dark patterns modify the underlying choice architecture for users" (§2.4, pdf p. 9). They add "disparate treatment" for interfaces where users do not "know why they are shown a limited set of choices" (pdf p. 9) — a personalization attribute. They propose four normative lenses: individual welfare, collective welfare, regulatory objectives and individual autonomy. Under the autonomy lens, "a dark pattern is a user interface that undermines individual decision-making" (§4.4, pdf p. 18). They also note that sharing-economy marketplaces "can manipulate both the sellers (e.g., Airbnb hosts) and the buyers" (pdf p. 13).
- *Role in the DXD argument:* precursor / algorithmacy-cognitive-issue (it names choice architecture as the common substrate of dark patterns, adds personalization, and flags two-sided manipulation — the coordination case algorithmacy targets).

### B11. The algorithmic choice architect

**yeung2017hypernudge** — Yeung, K. (2017). 'Hypernudge': Big Data as a mode of regulation by design. *Information, Communication & Society, 20*(1), 118–136. https://doi.org/10.1080/1369118X.2016.1186713
- *Verification:* existing card `submissions/hospitality_phygital/library/cards/yeung2017hypernudge.md` (full text, crossref-verified 2026-08-08); Crossref; OA accepted manuscript (KCL Pure), re-read this session.
- *Read status:* read in full (accepted manuscript; the page numbers below are pdf pages of the AAM, not journal pages).
- *What it establishes:* "Unlike the static Nudges popularised by Thaler and Sunstein … Big Data analytic nudges are extremely powerful and potent due to their networked, continuously updated, dynamic and pervasive nature (hence 'hypernudge')" (abstract). The mechanism is a "recursive feedback loop" that reconfigures "an individual's choice architecture … continuously … in real-time in three directions." The three directions are (a) refinement "in response to changes in the target's behaviour," (b) "data feedback to the choice architect," and (c) refinement "in light of population-wide trends" (AAM pdf p. 7). Yeung also argues that "the critical mechanisms of influence utilized by hypernudging are embedded into the design of complex, machine-learning algorithms, which are highly opaque" (pdf p. 9), and that legitimacy concerns "are not satisfactorily resolved through reliance on individual notice and consent" (abstract).
- *Role in the DXD argument:* algorithmacy-cognitive-issue (the bridge: choice architecture that is personal, adaptive, recursive and opaque — exactly the intermediary algorithmacy is defined against).

**mills2022finding** — Mills, S. (2022). Finding the 'nudge' in hypernudge. *Technology in Society, 71*, 102117. https://doi.org/10.1016/j.techsoc.2022.102117
- *Verification:* Crossref; OpenAlex abstract (found by the hypernudge search, log row 25).
- *Read status:* abstract only.
- *What it establishes:* Mills conceptualizes "a hypernudge as a system of nudges which change over time and in response to feedback. In this sense, a hypernudge is not a type of nudge, but an arrangement of nudges" (abstract).
- *Role in the DXD argument:* competing-construct (a behavioral-science deflation of Yeung: the unit of design is the arrangement over time, not the single nudge).

**mills2022autonomous** — Mills, S., & Sætra, H. S. (2024). The autonomous choice architect. *AI & Society, 39*(2), 583–595. https://doi.org/10.1007/s00146-022-01486-z (first published online 2022)
- *Verification:* Crossref (issued online 2022-06-22; 39(2), 583–595); Consensus abstract; OA PDF (LSE Research Online eprint 115293).
- *Read status:* read in part (abstract and introduction, pdf pp. 1–4).
- *What it establishes:* "Increasingly, however, this role of architecting choice is not performed by a human choice architect, but an algorithm or artificial intelligence, powered by a stream of Big Data and infused with an objective it has been programmed to maximise. We call this entity the autonomous choice architect." Choice architects "at a most basic level select, from a range of designs, the design which is most likely to maximise a pre-determined objective," and the human architect is "increasingly obscured behind algorithmic, artificially intelligent systems" (abstract). The authors connect this to A/B testing as design practice (pdf p. 4, n. 2) and conclude that responsibility "remains firmly one human beings must bear" (abstract).
- *Role in the DXD argument:* algorithmacy-cognitive-issue (the architect is now the optimizer; the DXD practitioner's A/B loop is itself an autonomous choice architect).

### B12. Autonomy, manipulation and the ethics of steering

**susser2019technology** — Susser, D., Roessler, B., & Nissenbaum, H. (2019). Technology, autonomy, and manipulation. *Internet Policy Review, 8*(2). https://doi.org/10.14763/2019.2.1410
- *Verification:* Crossref; OA PDF (policyreview.info, diamond OA).
- *Read status:* read in part (abstract; §1 definition, pdf pp. 3–4).
- *What it establishes:* "Manipulating someone means intentionally and covertly influencing their decision-making, by targeting and exploiting their decision-making vulnerabilities. Covertly influencing someone … means influencing them in a way they aren't consciously aware of, and in a way they couldn't easily become aware of were they to try" (pdf p. 4). Online manipulation's "deeper, more insidious harm is its challenge to individual autonomy" (abstract).
- *Role in the DXD argument:* algorithmacy-cognitive-issue (the "couldn't easily become aware of were they to try" clause marks where interpretation fails — algorithmacy's first operation).

**lanzing2019strongly** — Lanzing, M. (2019). "Strongly recommended": Revisiting decisional privacy to judge hypernudging in self-tracking technologies. *Philosophy & Technology, 32*(3), 549–568. https://doi.org/10.1007/s13347-018-0316-4 (first published online 2018)
- *Verification:* Crossref; Consensus abstract.
- *Read status:* abstract only.
- *What it establishes:* "The real-time personalization of choice architectures requires continuous surveillance," and "hypernudging self-tracking technologies compromise autonomy because they violate informational and decisional privacy" (abstract).
- *Role in the DXD argument:* algorithmacy-cognitive-issue (hypernudging requires that the system read the person — the "reads both parties" clause of algorithmacy, from the single-user side).

**schmidt2020ethics** — Schmidt, A. T., & Engelen, B. (2020). The ethics of nudging: An overview. *Philosophy Compass, 15*(4), e12658. https://doi.org/10.1111/phc3.12658
- *Verification:* Crossref; Consensus abstract.
- *Read status:* abstract only.
- *What it establishes:* Schmidt and Engelen split the autonomy worry into "freedom of choice, volitional autonomy, rational agency, and freedom as nondomination." They also treat manipulation, dignity and the claim that nudging "prevents more important structural reform," and conclude that "the objections fail to establish that the nudge program as a whole should be rejected" while giving "guidance … on a case-by-case basis" (abstract).
- *Role in the DXD argument:* precursor (the standard map of nudge-ethics objections, all posed about a human architect and a static intervention).

**michaelsen2024experiencing** — Michaelsen, P., Johansson, L.-O., & Hedesström, M. (2024). Experiencing default nudges: Autonomy, manipulation, and choice-satisfaction as judged by people themselves. *Behavioural Public Policy, 8*(1), 85–106. https://doi.org/10.1017/bpp.2021.5 (first published online 2021)
- *Verification:* Crossref; Consensus; OA PDF (Cambridge Core).
- *Read status:* read in part (abstract, p. 85).
- *What it establishes:* In "three between-group experiments (N = 2083)," participants given "a prosocial opt-out default nudge made more prosocial choices but did not report lower autonomy or choice satisfaction than participants in opt-in default or active-choice conditions. This was the case even when the presence of the nudge was disclosed" (p. 85). With monetary stakes, "participants perceived the threat to freedom of choice as slightly higher in the nudge condition," but objection did not differ (p. 85).
- *Role in the DXD argument:* counterevidence (experienced autonomy is insensitive to steering, even disclosed steering, so self-report cannot be DXD's success metric — and disclosure, the literacy remedy, changes little).

---

## (c) Thematic synthesis

**What choice architecture already gives DXD.** Choice architecture gives DXD four things, and the most practitioner-ready is a premise. Schneider, Weinmann and vom Brocke put it plainly: "there is no neutral way to present choices," so "the software engineer becomes a choice architect" whether she knows it or not. That premise runs back through Tversky and Kahneman's (1981) frames — which they likened to perceptual perspectives — to Simon's (1956) point that environments "permit further simplication" of choice. The UX designer who sets a default is already doing decision design; DXD names the practice rather than inventing it. The second gift is a toolkit and a ranking. Johnson et al.'s (2012) tools, sorted into structuring the task and describing the options, reappear in Mertens et al.'s corrected meta-analysis, where decision structure (d = 0.54) outperforms decision information (d = 0.34) and decision assistance (d = 0.28), and defaults lead the techniques (d = 0.62). Third comes a normative vocabulary: "as judged by themselves," sludge, dark patterns and Mathur, Kshirsagar and Mayer's four lenses. Fourth, and most important for the thesis, is a competing program. Hertwig and Grüne-Yanoff's boosts target "competences" rather than behavior and should persist once removed, which is the nearest existing template for a design discipline that builds algorithmacy.

**What the evidence licenses.** The evidence licenses less than the practitioner canon assumes, and here the literature is openly divided. Mertens et al. report d = 0.43 after correction. Maier et al. find "no evidence … after correcting for this bias," Szaszi et al. find adjusted estimates between d = 0.01 and 0.08, and DellaVigna and Linos watch an 8.7-point academic effect shrink to 1.4 points at scale. All three camps now agree that heterogeneity, not the mean, is the finding. The design heuristics fare the same. Scheibehenne et al. put the average overload effect at "virtually zero," while Chernev et al. recover it once complexity, task difficulty, preference uncertainty and goal are modelled. Chandrashekar et al. replicate the organ-donation default at 62.5% versus 73.5%, not 42% versus 82%. Dallacker et al. and Arshad et al. find that opt-out moves recorded consent more reliably than donation. A DXD that sells itself on nudge-sized wins inherits that dispute.

**What it misses once the architect is an algorithm.** The canon assumes three things that algorithmic intermediaries break: an identifiable architect, a fixed menu and a single chooser. Yeung's hypernudge breaks the first two. The architecture is "continuously reconfigured in real-time" from each target's data and from "population-wide trends," and its mechanisms sit in "highly opaque" models. Mills and Sætra break the first outright: the architect is now an optimizer selecting whichever design "is most likely to maximise a pre-determined objective," which is also a description of an A/B-testing product team. Mills's deflation — a hypernudge is "an arrangement of nudges" over time — tells DXD what its unit of analysis must become. The third assumption survives almost untouched. Every study above models one chooser facing one menu. Only Mathur et al.'s aside that platforms "can manipulate both the sellers … and the buyers" glimpses the coordination case in which a system reads both parties and commits a decision neither controls.

**Why the familiar remedies are literacy remedies.** The standard fixes — disclosure, transparency, notice and consent — assume the chooser can read the architecture once it is shown. Yeung argues that notice and consent fail for hypernudges. Susser, Roessler and Nissenbaum locate manipulation in influence one "couldn't easily become aware of were they to try." Michaelsen et al. find that disclosing a default leaves experienced autonomy unchanged. Even boosting, ported online by Kozyreva, Lewandowsky and Hertwig, is framed as "boosting … information literacy." That is the paradigm the design-ethics arm says algorithmacy exceeds. Two openings point past it. Hertwig and Grüne-Yanoff note that competences are "often best fostered by redesigning aspects of individuals' external environment or by teaching them how to redesign them" — close to specifying intent through the intermediary. Callaway et al. show an algorithm teaching durable decision strategies. Neither reaches the third operation, keeping track of an intermediary that keeps changing. That is DXD's open problem, and it is the one this lineage leaves unaddressed.

---

## (d) Gaps and unverified leads

**Gaps in this facet**
- *No text of the classics.* Simon 1955 and 1956, Tversky & Kahneman 1981, Johnson & Goldstein 2003, Iyengar & Lepper 2000, Johnson et al. 2012 and *Nudge* itself are closed; I used records and abstracts only. Before any of their specific numbers enter a draft, pull the version of record through library access: J&G's country consent rates, Iyengar & Lepper's 30%/3% jam figures, and Simon's page-specific passages.
- *Weinmann et al. (2016, BISE) and Schneider et al. (2018, CACM) unread.* The digital-nudging definition comes from a Consensus abstract of the CACM piece, whose record carries a 2017 date and a slightly different title ("Digital Nudging–Guiding Choices by Using Interface Design"). Confirm the wording against the 2018 CACM text.
- *No meta-analysis of digital or algorithmic nudges read.* Bergram et al. (2022, CHI, doi:10.1145/3491102.3517638; "73 peer-reviewed papers containing 109 separate studies where 231 digital nudges have been evaluated," Consensus abstract) and Jesse & Jannach (2021, *Computers in Human Behavior Reports*, 3, 100052, doi:10.1016/j.chbr.2020.100052; "87 nudging mechanisms," Consensus abstract) are Crossref-verified but abstract-only. They are the next reads if DXD needs effect evidence from digital settings.
- *Two-sided choice architecture is essentially unstudied in this lineage.* I found no study that models a system steering both parties of a coordination at once. The gap is a candidate contribution, not a finding; it rests on my searches here, not on a systematic review.
- *Scholar Gateway was unreachable* (identity error), so full-text passage search for the closed classics did not run.

**Unverified or lightly verified leads (not entries)**
- Herzog, S. M., & Hertwig, R. (2025). Boosting: Empowering citizens with behavioral science. *Annual Review of Psychology, 76*, 851–881. doi:10.1146/annurev-psych-020924-124753 — Crossref-verified, Consensus abstract only; the current state of boosting and the obvious next read.
- Grüne-Yanoff, T. (2025). Boosts are not educative or System-2 nudges. *Mind & Society, 24*(2), 549–561. doi:10.1007/s11299-025-00324-1 — Crossref-verified. Its abstract argues that competences "are distinct from either knowledge and skills" and that boosts "need not be slower or more effortful," which bears directly on whether algorithmacy is a competence in the boosting sense.
- Mills, S. (2020). Nudge/sludge symmetry. *Behavioural Public Policy, 7*(2), 309–332. doi:10.1017/bpp.2020.61 — Crossref-verified. Its abstract claims that "where a nudge decreases the frictions associated with a specific option, sludge is simultaneously imposed on all other options," a useful corrective to "nudge good, sludge bad."
- Gray, C. M., Chen, J., Chivukula, S. S., & Qu, L. (2021). End user accounts of dark patterns as felt manipulation. *PACM-HCI, 5*(CSCW2), 1–25. doi:10.1145/3479516 — OpenAlex abstract (n = 169, English and Mandarin); user-side evidence on dark patterns.
- Zhu, Z., & Wang, K. (2026). Multimodal perceptual curation for cognitive autonomy in Generation Z decision making. *Frontiers in Psychology, 17*. doi:10.3389/fpsyg.2026.1868429 — Crossref-verified, 0 citations. Its abstract reports that "metacognitive awareness of algorithmic influence was not significantly associated with actual behavioral resistance, supporting a literacy paradox." If that holds up it is directly relevant counterevidence to literacy remedies, but it is a new, uncited, single-country student sample; **do not rely on it without reading it.**
- Hansen, P. G., & Jespersen, A. M. (2013). Nudge and the manipulation of choice. *European Journal of Risk Regulation, 4*(1), 3–28. doi:10.1017/S1867299X00002762 — Crossref-verified. The four-type (System 1/2 × transparent/non-transparent) nudge framework is the likely source of Caraban et al.'s ethics axes; unread.
- Johnson, E. J., Bellman, S., & Lohse, G. L. (2002) — the default/framing study whose replication failed (Chandrashekar et al., 2023). Not retrieved.
- Sunstein's *Sludge* (2021) and "Sludge and Ordeals" (*Duke Law Journal*, 2019): see the existing card `sunstein2021.md`. Its quotations are from an SSRN draft and were not re-verified at S2.
