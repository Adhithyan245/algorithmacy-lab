# F3 — Decision support systems and cognitive systems engineering

*Facet review for the Decision Experience Design (DXD) arm. Drafted by Claude (F3 research agent), 2026-09-30. All text below is Claude-drafted; none of it is the author's wording.*

**Scope.** This facet covers the engineering precursors that designed "decision experiences" for professionals before UX existed as a field: decision support systems (DSS) in information systems, naturalistic decision making (NDM), decision-centered design and cognitive task analysis (CTA), cognitive work analysis (CWA) and ecological interface design (EID), situation awareness (SA), joint cognitive systems (JCS), and the ironies-of-automation line. The guiding question: what transfers from these fields to DXD for ordinary people coordinating through platforms, and what breaks under the algorithmacy condition, where the "system" is an adaptive, opaque intermediary that reads both parties and serves a third party's objective?

**Read-status key.** *Read in full* = OA full text read this session, or an existing repo card built from full text. *Abstract only* = abstract (or table of contents) from a database record. *Not accessible* = bibliographic record verified, no text reachable through OA.

---

## (a) Search log

All searches run 2026-09-30. "Count" is the total the service reported (Crossref's `query.bibliographic` totals are relevance-ranked over the whole index and are not meaningful as hit counts; they are recorded because the brief asks for them). Consensus returns a fixed top-20.

| # | Source | Exact query / request | Count | Used |
|---|---|---|---|---|
| 1 | repo grep | `grep -ril` for bainbridge, endsley, klein, vicente, rasmussen, hollnagel, woods, sprague, gorry, keen, arnott, kahneman, militello, crandall, hoffman, "decision support", "naturalistic", "ecological interface", "cognitive work analysis", "situation awareness", "ironies of automation", "joint cognitive", "decision-centered", "cognitive task analysis", parasuraman, "lee.*see", "trust in automation" over `submissions/*/literature submissions/*/library org_frontier/research/*/literature` | 7 relevant cards found | bainbridge1983, endsleykiris1995, klein2004, norman1990, leesee2004 (all in `submissions/algorithmacy_design_ethics/literature/library/`); sarterwoods1995, parasuraman2000 read, not used as entries. No card exists for Rasmussen, Vicente (K. J.), Hollnagel, Sprague, Gorry, Arnott, Kahneman & Klein. `org_frontier/research/field/literature/references.bib` holds bib-only entries for militello1998applied and hoffman1998critical (no cards) |
| 2 | Crossref | `Gorry Scott Morton framework for management information systems 1971 Sloan Management Review` | 4,955,575 | no record of the 1971 article; Kirs et al. 1989 validation study found |
| 3 | Crossref | `Sprague framework for the development of decision support systems MIS Quarterly 1980` | 11,863,538 | Sprague 1980 |
| 4 | Crossref | `Kahneman Klein conditions for intuitive expertise a failure to disagree` | 1,556,589 | Kahneman & Klein 2009 |
| 5 | Crossref | `Klein naturalistic decision making Human Factors 2008` | 8,865,580 | Klein 2008 |
| 6 | Crossref | `Gorry Scott Morton A framework for management information systems` | 11,589,408 | none |
| 7 | OpenAlex | `search=framework for management information systems Gorry Scott Morton` | 543 | Arnott & Pervan 2005 surfaced |
| 8 | OpenAlex | `search=Keen Scott Morton decision support systems an organizational perspective` | 2,523 | Keen 1980 (ACM) seen |
| 9 | OpenAlex | `search=Arnott Pervan decision support systems research review` | 602 | Arnott & Pervan 2005, 2012 |
| 10 | OpenAlex | `filter=title.search:framework for management information systems,publication_year:1971` | 0 | — |
| 11 | OpenAlex | `filter=title.search:decision support systems organizational perspective,publication_year:1977-1979` | 1 | Keen & Scott Morton 1978 (W1569447401) |
| 12 | Crossref | `Rasmussen skills rules and knowledge signals signs and symbols IEEE Transactions Systems Man Cybernetics 1983` | 1,784,748 | Rasmussen 1983 |
| 13 | Crossref | `Vicente Rasmussen ecological interface design theoretical foundations 1992` | 5,594,545 | Vicente & Rasmussen 1992 |
| 14 | Crossref | `Endsley toward a theory of situation awareness in dynamic systems 1995` | 9,312,913 | Endsley 1995 |
| 15 | OpenAlex | `search=Gorry Scott Morton framework management information systems Sloan Management Review` + `publication_year:1971` | 0 | — |
| 16 | OpenAlex | `search=Vicente cognitive work analysis toward safe productive healthy computer-based work` | 618 | none relevant |
| 17 | OpenAlex | `search=Hollnagel Woods joint cognitive systems foundations of cognitive systems engineering` | 759 | book review record only |
| 18 | OpenAlex | `search=Woods Hollnagel joint cognitive systems patterns in cognitive systems engineering` | 1,061 | Naweed & Bye 2008 review |
| 19 | OpenAlex | `search=Crandall Klein Hoffman working minds practitioner's guide cognitive task analysis` | 368 | none direct |
| 20 | Crossref | `Hollnagel Woods Joint Cognitive Systems Foundations of Cognitive Systems Engineering` | 11,378,443 | Hollnagel & Woods 2005; Woods & Hollnagel 2006 |
| 21 | Crossref | `Woods Hollnagel Joint Cognitive Systems Patterns in Cognitive Systems Engineering` | 11,663,702 | same |
| 22 | Crossref | `Vicente Cognitive Work Analysis Toward Safe Productive and Healthy Computer-Based Work` | 2,041,517 | reviews only |
| 23 | Crossref | `Crandall Klein Hoffman Working Minds A Practitioner's Guide to Cognitive Task Analysis` | 107,688 | Crandall et al. 2006 |
| 24 | Crossref | `Hutton Miller Thordsen decision-centered design leveraging cognitive task analysis in design` | 2,728,683 | "Decision-Centered Design" chapter (Thordsen, Hutton, Miller) |
| 25 | Crossref | `Klein a recognition-primed decision (RPD) model of rapid decision making` | 5,422,469 | DTIC reports only |
| 26 | Crossref | `Keen Scott Morton Decision support systems an organizational perspective` | 7,066,228 | no book record |
| 27 | Crossref | works/`10.1201/9781410607775.ch17` and `10.1201/9781410607775` | 2 records | chapter + handbook metadata |
| 28 | Crossref | `Vicente 1999 Cognitive Work Analysis book CRC Lawrence Erlbaum` | 10,918,869 | Vicente 1999 (10.1201/b12457) |
| 29 | OpenAlex | `search=recognition-primed decision model rapid decision making Klein decision making in action models and methods` | 11,946 | none direct |
| 30 | Consensus | `conditions for intuitive expertise valid feedback high-validity environment` | 20 | Kahneman & Klein 2009; Peringa et al.; Klein 2015 |
| 31 | Consensus | `cognitive systems engineering decision support for algorithmic intermediaries opaque adaptive systems` | 20 | Pathirannehelage et al. 2024; Simkute et al. 2021; Smith et al. 2024 panel |
| 32 | Consensus | `Gorry Scott Morton framework management information systems structured unstructured decisions` | 20 | Gorry record (index year 2015); Keen & Scott Morton 1978 record; Phillips-Wren et al. 2022 |
| 33 | Crossref | `Hollnagel Woods cognitive systems engineering new wine in new bottles 1983` | 5,143,334 | Hollnagel & Woods 1983 (+1999 reprint) |
| 34 | Crossref | `Endsley ironies of artificial intelligence Ergonomics 2023` | 12,305,477 | Endsley 2023 |
| 35 | Crossref | `Strauch ironies of automation still unresolved after all these years` | 3,248,474 | Strauch 2018 |
| 36 | Crossref | `Woods cognitive technologies design of joint human-machine cognitive systems AI Magazine 1985` | 1,636,543 | not found in Crossref (found in OpenAlex, row 49) |
| 37 | Crossref | `Phillips-Wren support for cognition in decision support systems exploratory historical review` | 1,231,629 | Phillips-Wren et al. 2022 |
| 38 | Crossref | `Arnott Pervan eight key issues for the decision support systems discipline 2008` | 377,569 | Arnott & Pervan 2008 |
| 39 | Crossref | `Arnott Pervan a critical analysis of decision support systems research revisited 2014` | 2,106,753 | Arnott & Pervan 2014 |
| 40 | Crossref | `Militello Hutton applied cognitive task analysis ACTA practitioner's toolkit` | 12,026,293 | Militello & Hutton 1998 |
| 41 | OpenAlex | `works/doi:` OA-status check on 22 DOIs | 22 records | OA copies: Vicente & Rasmussen (DTU), Arnott & Pervan 2005 (Curtin), ACTA (UWE), Simkute (gold), Pathirannehelage (hybrid) |
| 42 | Semantic Scholar | `paper/DOI:` lookups for 9 DOIs (fields openAccessPdf, abstract) | 8 of 9 returned | only Kahneman & Klein flagged GREEN (a course-reading copy; not used, see Gaps) |
| 43 | WebSearch | `Kahneman Klein 2009 "Conditions for intuitive expertise" pdf` | 9 links | third-party reposts only; not used |
| 44 | WebSearch | `Klein 2008 "Naturalistic decision making" Human Factors 50th anniversary pdf` | 10 links | third-party reposts only; not used |
| 45 | Scholar Gateway | two natural-language queries (Kahneman & Klein conditions; RPD model) | error | `INVALID_QUERY: Could not resolve user identity from CONNECT` — Scholar Gateway could not be reached this session |
| 46 | Crossref + OpenAlex | abstract retrieval for 10 DOIs (`works/{doi}`; OpenAlex `abstract_inverted_index`) | 8 abstracts | see entries |
| 47 | WebFetch / curl | Curtin eSpace, ScienceDirect, Taylor & Francis, Springer, Wiley, ETH, UWE full-text links | 0 of 8 | all blocked (HTTP 202-empty, 403, JS challenge, or redirect to login); these items stay abstract-only |
| 48 | Semantic Scholar | `paper/search` for "A Framework for Management Information Systems", RPD chapter, "Decision making in action" | failed ×4 retries each | rate-limited; skipped |
| 49 | OpenAlex | `filter=title.search:decision making in action models and methods` | 6 | Klein et al. 1993 book record + three reviews (Eisenberger 1995 gives editors, Ablex, 480 pp.) |
| 50 | OpenAlex | `filter=title.search:recognition-primed decision model of rapid decision making` | 1 | Klein 1993 chapter record (W1623168575) |
| 51 | WebSearch | `Gorry Scott Morton "A Framework for Management Information Systems" Sloan Management Review 1971 volume 13` | 10 links | snippet gives SMR 13(1), Fall 1971, pp. 55–70 (not a database record) |
| 52 | MIT DSpace API | `discover/search/objects?query=framework management information systems Gorry Morton` | 8 | Sloan WP 510-71 (Feb 1971) and WP 458-70 — **OA full text, read** |
| 53 | OpenAlex (snowball) | `search=algorithm&filter=cites:W2140543255` (citing Kahneman & Klein 2009) | 360 | Allen & Choudhury 2022; Simkute et al. 2021 |
| 54 | OpenAlex (snowball) | `search=recommender platform algorithmic&filter=cites:W2140543255` | 51 | Simkute; nothing on consumer platforms |
| 55 | OpenAlex (snowball) | `search=platform workers algorithmic management&filter=cites:W2008653298` (citing Bainbridge 1983) | 44 | Parker & Grote; Janssen et al. 2019; Green 2022 |
| 56 | OpenAlex (snowball) | `search=consumer everyday users recommender&filter=cites:W2008653298` | 14 | Schuster & Lazar 2024 |
| 57 | OpenAlex (snowball) | `search=machine learning algorithm transparency&filter=cites:W2163322071` (citing Vicente & Rasmussen 1992) | 24 | Carsten & Martens 2018; Zou & Borst 2025 |
| 58 | OpenAlex (snowball) | `search=algorithm&filter=cites:W2169613734` (citing Klein 2008) | 253 | nothing central |
| 59 | repo grep | Parker/Grote, Janssen, Ganesh, Carsten/Martens, Allen/Choudhury, Schuster/Lazar, Kleinberg, Endsley 2023, Strauch, Simkute, Pathirannehelage, Phillips-Wren, Hollnagel, Rasmussen | 0 relevant | no existing cards |
| 60 | curl | LSE Research Online accepted manuscript of Allen & Choudhury | 1 PDF | **read** |
| 61 | Consensus | `Hollnagel Woods cognitive systems engineering new wine in new bottles man-machine system as cognitive system` | 20 | Hollnagel & Woods 1983 abstract; JCS book TOCs; Woods 1986 AI Magazine |
| 62 | Consensus | `decision-centered design cognitive task analysis designing decision support around critical decisions` | 20 | Militello et al. 2016; Klein et al. 1997; Arnott 2006 |
| 63 | Consensus | `ironies of automation algorithmic recommendation everyday users deskilling feedback` | 20 | Banker & Khetani 2019; Rinta-Kahila et al. 2023; Schuster & Lazar 2024 |
| 64 | Crossref | `works/{doi}` metadata for 17 DOIs | 16 of 17 | years, volumes, pages confirmed |
| 65 | OpenAlex + AAAI OJS | `works/W1726694533`; AAAI OJS article 511 | 1 PDF | Woods (1985) AI Magazine 6(4) — **OA full text, read** |
| 66 | curl | DTU Orbit accepted manuscript of Vicente & Rasmussen 1992 | 1 PDF | **read** |

---

## (b) Entries

Entries run by strand: DSS origins (1–7), NDM and expertise (8–13), decision-centered design and CTA (14–16), CWA/EID (17–18), SA, JCS and CSE (19–23), ironies of automation and their successors (24–30). Record-only items the brief named but no OA text reached are grouped at the end (31–35).

### DSS origins

**1. gorry1971framework**
Gorry, G. A., & Scott Morton, M. S. (1971). *A framework for management information systems* (Working Paper No. 510-71). Sloan School of Management, Massachusetts Institute of Technology. http://hdl.handle.net/1721.1/47936 — published as Gorry, G. A., & Scott Morton, M. S. (1971). A framework for management information systems. *Sloan Management Review, 13*(1), 55–70.
- **Verification:** MIT DSpace record (handle 1721.1/47936; authors, 1971, WP 510-71); Consensus record "A Framework for Management Information Systems" (Gorry et al.; index year wrongly given as 2015). The SMR volume/issue/pages come from a web-search snippet only and are **not** confirmed against a database record; no DOI exists.
- **Read status:** read in full (working-paper version dated February 1971, "A revision of 'Management Decision Systems: A Framework for Management Information Systems' Sloan School Working Paper 458-70"; page numbers below are the working paper's).
- **What it establishes:** The paper crosses Anthony's planning/control categories with Simon's programmed/nonprogrammed decisions, renamed "structured" and "unstructured" (WP p. 13). In the unstructured case "the human decision maker must provide judgment and evaluation as well as insights into problem definition" (p. 13). It borrows Simon's intelligence–design–choice phases and defines a "semi-structured" decision as one "with one or two of the intelligence, design and choice phases unstructured," the zone "where the interactive terminal systems have their greatest potential"; "When all phases are unstructured, we can only provide access to data and useful ways of displaying it" (pp. 15–16). Systems for the structured side are "structured decision systems (SDS)"; for the unstructured side, "Management Decision Systems (MDS)" (p. 16). The line between them "is moving down over time": inventory reordering has moved "from the unstructured operational control area to the structured" (p. 22).
- **Role in the DXD argument:** precursor / term-use. The first designed "decision experience" was defined by what the machine could not structure. Algorithmacy inverts the arrangement: the platform takes over the structured phases and hands the person an interpretive residue, without the person having chosen where the line falls.

**2. sprague1980framework**
Sprague, R. H., Jr. (1980). A framework for the development of decision support systems. *MIS Quarterly, 4*(4), 1–26. https://doi.org/10.2307/248957
- **Verification:** Crossref record (abstract included); OpenAlex W150775819.
- **Read status:** abstract only (JSTOR, closed).
- **What it establishes:** The abstract sets out a framework of "(a) three levels of technology which have been designated DSS, (b) the developmental approach that is evolving for the creation of a DSS, and (c) the roles of several key types of people in the building and use of a DSS," and a "descriptive model to assess the performance objectives and the capabilities of a DSS as viewed by three of the major participants."
- **Role in the DXD argument:** precursor. DSS was founded as multi-role (builders, intermediaries, users). That is the nearest DSS precedent for a triad, but every role in it works for the same organization's decision maker.

**3. arnott2005critical**
Arnott, D., & Pervan, G. (2005). A critical analysis of decision support systems research. *Journal of Information Technology, 20*(2), 67–87. https://doi.org/10.1057/palgrave.jit.2000035
- **Verification:** Crossref record with abstract; OpenAlex W1996654773; Unpaywall lists a Curtin submitted version.
- **Read status:** abstract only (the Curtin OA copy exists but the repository now redirects and blocked retrieval).
- **What it establishes:** The analysis covers "1,020 DSS articles published in 14 major journals from 1990 to 2003." DSS publication "has been falling steadily since its peak in 1994." "Almost half of DSS papers did not use judgement and decision-making reference research in the design and analysis of their projects and most cited reference works are relatively old." "A major omission in DSS scholarship is the poor identification of the clients and users," and the field "is facing a crisis of relevance" (abstract).
- **Role in the DXD argument:** counterevidence / cautionary precursor. DSS set out to design decision experiences yet, by its own leading reviewers' count, often did so without a cognitive theory of the decider and without naming the user. DXD must not repeat either omission.

**4. arnott2014critical**
Arnott, D., & Pervan, G. (2014). A critical analysis of decision support systems research revisited: The rise of design science. *Journal of Information Technology, 29*(4), 269–293. https://doi.org/10.1057/jit.2014.16
- **Verification:** Crossref record with abstract.
- **Read status:** abstract only.
- **What it establishes:** The sample extended to 2010 "now includes 1466 articles from 16 journals." Findings: "an overall decline in DSS publishing," declining relevance to IT professionals, no improvement in design rigor, but "a positive shift in judgment and decision-making foundations" and "a significant increase in DSS design-science research (DSR) to almost half of published articles" (abstract).
- **Role in the DXD argument:** precursor. The field's own trajectory runs toward design science. That is the methodological home a DXD research program would inherit.

**5. phillipswren2022support**
Phillips-Wren, G., Daly, M., & Burstein, F. (2022). Support for cognition in decision support systems: An exploratory historical review. *Journal of Decision Systems, 31*(sup1), 18–30. https://doi.org/10.1080/12460125.2022.2070946
- **Verification:** Crossref record; OpenAlex W4225149048 (abstract).
- **Read status:** abstract only.
- **What it establishes:** "Decision support systems (DSS) have been traditionally developed to assist with unstructured and semi-structured problems." "Cognition during decision making was viewed in terms of two competing, and sometimes cooperating, systems: one that was automatic and fast, and one that was deliberative and slow." The review traces "theoretical underpinnings of DSS support for cognition" and cites "the classical Gorry & Scott Morton (1989) framework" (abstract). The 1989 date presumably refers to a later SMR reprint of the 1971 article; this has not been verified.
- **Role in the DXD argument:** UX-cognitive-foundation (DSS branch). It is the explicit bridge from DSS to dual-process cognition, the same foundation UX drew on for cognitive load.

**6. pathirannehelage2024design**
Herath Pathirannehelage, S., Shrestha, Y. R., & von Krogh, G. (2024). Design principles for artificial intelligence-augmented decision making: An action design research study. *European Journal of Information Systems, 34*(2), 207–229. https://doi.org/10.1080/0960085X.2024.2330402
- **Verification:** Crossref record; OpenAlex W4393000854 (abstract); OA (hybrid, CC licence per OpenAlex).
- **Read status:** abstract only (publisher and ETH copies blocked retrieval).
- **What it establishes:** "Unlike traditional decision support systems (DSS) designed to support decisionmakers with fixed decision rules and models that often generate stable outcomes and rely on human agentic primacy, AI systems learn, adapt, and act autonomously." Hence "the extrapolation of prescriptive design knowledge from conventional DSS to AIADM is problematic." The setting is an action design research study in "an e-commerce company specialising in producing and selling clothing," supporting "marketing, consumer engagement, and product design decisions" (abstract).
- **Role in the DXD argument:** algorithmacy-cognitive-issue (what breaks). IS scholars already concede that DSS design knowledge does not carry over once the system adapts. The algorithmacy condition adds a further break the paper does not address: the adaptive system's objective belongs to a third party.

**7. keen1978decision** — see record-only list, item 31.

### Naturalistic decision making and expertise

**8. klein2008naturalistic**
Klein, G. (2008). Naturalistic decision making. *Human Factors, 50*(3), 456–460. https://doi.org/10.1518/001872008X288385
- **Verification:** Crossref record with structured abstract.
- **Read status:** abstract only (SAGE, closed; the copies found were third-party reposts, not used).
- **What it establishes:** "NDM research emerged in the 1980s to study how people make decisions in real-world settings." "The NDM framework emphasizes the role of experience in enabling people to rapidly categorize situations to make effective decisions." The approach "has been used to improve performance through revisions of military doctrine, training that is focused on decision requirements, and the development of information technologies to support decision making" (abstract).
- **Role in the DXD argument:** UX-cognitive-foundation. It supplies the recognition-based account of skilled deciding that decision-centered design is built on.

**9. kahneman2009conditions**
Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise: A failure to disagree. *American Psychologist, 64*(6), 515–526. https://doi.org/10.1037/a0016755
- **Verification:** Crossref record; OpenAlex W2140543255 (abstract); Consensus record.
- **Read status:** abstract only. Semantic Scholar flags a course-hosted copy and the web offers third-party reposts; I did not treat these as legitimate OA, so no body text was read and no page locators are given.
- **What it establishes:** The paper sets out to "map the boundary conditions that separate true intuitive skill from overconfident and biased impressions." It concludes that "evaluating the likely quality of an intuitive judgment requires an assessment of the predictability of the environment in which the judgment is made and of the individual's opportunity to learn the regularities of that environment. Subjective experience is not a reliable indicator of judgment accuracy" (abstract). A secondary restatement (Peringa, Niessen, Meijer, & den Hartigh, 2026, *Psychology of Sport and Exercise, 82*, 103022, https://doi.org/10.1016/j.psychsport.2025.103022; abstract via Consensus) glosses the two conditions as "(1) the availability of high-validity cues, and (2) sufficient learning opportunities, including timely, complete, and unambiguous feedback." That gloss is Peringa et al.'s, not a quotation of Kahneman and Klein.
- **Role in the DXD argument:** algorithmacy-cognitive-issue (candidate mechanism). An opaque, adaptive intermediary lowers both conditions at once. Its policy changes, so the regularities a user learns go stale. Its outcomes reach the user through the same intermediary, so feedback is neither complete nor unambiguous. The facet's inference, not a claim of the source: users of platforms operate in a low-validity environment by design, and their confidence is the unreliable signal the abstract warns of.

**10. simkute2021explainability**
Simkute, A., Luger, E., Jones, B., Evans, M., & Jones, R. (2021). Explainability for experts: A design framework for making algorithms supporting expert decisions more explainable. *Journal of Responsible Technology, 7–8*, 100017. https://doi.org/10.1016/j.jrt.2021.100017
- **Verification:** Crossref record; OpenAlex W3214883276 (gold OA; cites Kahneman & Klein 2009 per the OpenAlex `cites:` filter).
- **Read status:** abstract only (ScienceDirect and the Edinburgh repository both returned 403).
- **What it establishes:** Explainability "is often seen as a promising mechanism for enabling human-in-the-loop, however, current approaches are ineffective and can lead to various biases." The authors argue that "explainability should be tailored to support naturalistic decision-making and sensemaking strategies employed by domain experts and novices," and they propose "the conceptual Expertise, Risk and Time Explainability framework," illustrated in journalism (abstract).
- **Role in the DXD argument:** precursor / transfer case. This is the nearest existing attempt to carry NDM into algorithm design. It still assumes a professional decider served by the algorithm, and it treats explanation as the remedy, which is the literacy-paradigm move the design-ethics arm cautions against.

**11. allen2022algorithm**
Allen, R., & Choudhury, P. (2022). Algorithm-augmented work and domain experience: The countervailing forces of ability and aversion. *Organization Science, 33*(1), 149–169. https://doi.org/10.1287/orsc.2021.1554
- **Verification:** Crossref record (issued 2022-01; 33(1), 149–169); OpenAlex W4200429321; found by snowball from Kahneman & Klein 2009.
- **Read status:** read in full (LSE Research Online author's accepted manuscript; page numbers are the manuscript's).
- **What it establishes:** In a within-subjects experiment at a firm with "more than 100,000 employees," corporate IT support staff resolved help tickets both manually and with an ML tool whose top recommendations were "about 90%" correct. Five sessions ran with "about 30 participants" each (ms pp. 9, 12). "Only workers with moderate levels of domain experience perform significantly better using the algorithm than manually resolving tickets—confirming an inverted U-shape" (ms p. 3). Low-experience workers rejected correct advice for "lack of ability to assess and use algorithmic recommendations"; high-experience workers rejected it from "aversion," rooted in "belief in their own superior understanding" and "a greater sense of accountability for their actions" (ms p. 3).
- **Role in the DXD argument:** counterevidence / complication. Expertise in the domain does not translate monotonically into competence with the algorithm. Algorithmacy is a distinct capacity, not domain skill plus exposure.

**12. banker2019algorithm**
Banker, S., & Khetani, S. (2019). Algorithm overdependence: How the use of algorithmic recommendation systems can increase risks to consumer well-being. *Journal of Public Policy & Marketing, 38*(4), 500–515. https://doi.org/10.1177/0743915619858057
- **Verification:** Crossref record; Consensus record (abstract).
- **Read status:** abstract only.
- **What it establishes:** "Five experiments illustrate that, stemming from a belief that algorithms hold greater domain expertise, consumers surrender to algorithm-generated recommendations even when the recommendations are inferior." Consumers "frequently depend too much on algorithm-generated recommendations," which may lead them to "play a role in propagating systemic biases that can influence other users" (abstract).
- **Role in the DXD argument:** algorithmacy-cognitive-issue (ordinary users). It carries the automation-bias finding from cockpits to consumers, and its last clause makes the harm triadic: one user's reliance shapes what others are shown.

**13. klein1993recognition** — see record-only list, item 32.

### Decision-centered design and cognitive task analysis

**14. militello1998applied**
Militello, L. G., & Hutton, R. J. B. (1998). Applied cognitive task analysis (ACTA): A practitioner's toolkit for understanding cognitive task demands. *Ergonomics, 41*(11), 1618–1641. https://doi.org/10.1080/001401398186108
- **Verification:** Crossref record; OpenAlex W2158441396 (abstract); bib-only entry at `org_frontier/research/field/literature/references.bib` (`militello1998applied`).
- **Read status:** abstract only (UWE submitted version listed by Unpaywall; retrieval failed).
- **What it establishes:** "Cognitive task analysis (CTA) is a set of methods for identifying cognitive skills, or mental demands, needed to perform a task proficiently," but "CTA is resource intensive and has previously been of limited use to design practitioners." ACTA "consists of three interview methods" whose output "will translate more directly into applied products, such as improved training scenarios or interface recommendations"; the techniques "were found to be easy to use, flexible, and to provide clear output" (abstract).
- **Role in the DXD argument:** UX-cognitive-foundation (method). ACTA is the method DXD practitioners could adapt directly. Its precondition is a population of proficient experts to interview, and platform users coordinating through an opaque intermediary are rarely that.

**15. militello2016designing**
Militello, L. G., Saleem, J. J., Borders, M. R., Sushereba, C. E., Haverkamp, D., Wolf, S. P., & Doebbeling, B. N. (2016). Designing colorectal cancer screening decision support: A cognitive engineering enterprise. *Journal of Cognitive Engineering and Decision Making, 10*(1), 74–90. https://doi.org/10.1177/1555343416630875
- **Verification:** Crossref record; Consensus record (abstract).
- **Read status:** abstract only.
- **What it establishes:** Barriers to clinical decision support include "an emphasis on algorithmic approaches to decision support that do not align well with clinical work flow and human decision strategies." The team "applied decision-centered design," using "ethnographic observation and cognitive task analysis." Primary care providers using the resulting app "more accurately answered questions about patients and found relevant information more quickly" and "reported reduced mental effort" (abstract).
- **Role in the DXD argument:** precursor (worked example). Decision-centered design already positions itself *against* algorithm-first decision support. That opposition is the stance DXD inherits.

**16. thordsen2003decision** — see record-only list, item 33.

### Cognitive work analysis and ecological interface design

**17. rasmussen1983skills**
Rasmussen, J. (1983). Skills, rules, and knowledge; signals, signs, and symbols, and other distinctions in human performance models. *IEEE Transactions on Systems, Man, and Cybernetics, SMC-13*(3), 257–266. https://doi.org/10.1109/TSMC.1983.6313160
- **Verification:** Crossref record; OpenAlex W1983186110 (abstract).
- **Read status:** abstract only (IEEE, closed; no OA copy found).
- **What it establishes:** The paper argues for "different types of models for representing performance at the skill-, rule-, and knowledge-based levels, together with a review of the different levels in terms of signals, signs, and symbols," with attention to representing system properties "at several levels of abstraction—from the representation of physical form, through functional representation, to representation in terms of intention or purpose" (abstract).
- **Role in the DXD argument:** UX-cognitive-foundation. SRK is the CSE counterpart to UX's perception and cognitive-load foundations. The top level of the abstraction ladder, "intention or purpose," is exactly what a platform intermediary withholds.

**18. vicente1992ecological**
Vicente, K. J., & Rasmussen, J. (1992). Ecological interface design: Theoretical foundations. *IEEE Transactions on Systems, Man, and Cybernetics, 22*(4), 589–606. https://doi.org/10.1109/21.156574
- **Verification:** Crossref record; OpenAlex W2163322071 (green OA, DTU Orbit).
- **Read status:** read in full (DTU Orbit "peer reviewed version," i.e., the accepted manuscript; manuscript pagination, so section numbers are given as primary locators).
- **What it establishes:** EID's goal is "not to force processing to a higher level than the demands of the task require" and "to support each of the three levels of cognitive control" (abstract). Its target is the "unfamiliar and unanticipated" event, because "the set of events that is used as a basis for design does not constitute an exhaustive list" (Sec. I.A). Three principles follow (Sec. V.A). The rule-based principle is to "provide a consistent one-to-one mapping between the work domain constraints and the cues or signs provided by the interface." It is illustrated by Three Mile Island, where operators used pressurizer level as a cue without knowing "the boundary conditions under which the cue was valid." The knowledge-based principle is to represent the domain as an abstraction hierarchy serving as "an externalized mental model." Two premises carry the design choice. Operators "are highly skilled and have extensive experience," and the interface serves "a single, specific application; generality is not important" (Sec. IV.A). The stated limitation is that "if those constraints are unknown, an abstraction hierarchy cannot be developed. Thus, the approach will only succeed to the extent that designers understand the system they are building" (Sec. V.B). In the DURESS experiment, the functional (P+F) interface improved diagnosis "primarily for experts" (Sec. VII).
- **Role in the DXD argument:** precursor, and the clearest statement of what breaks. EID's cure for procedural traps is to show the domain's true constraints. Under algorithmacy those constraints are the intermediary's policy, which is proprietary, adaptive and set by a third party. The DXD designer usually does not know them, which is EID's own named failure condition, and both EID premises (trained operators, a single application) fail for platform users.

### Situation awareness, joint cognitive systems and cognitive systems engineering

**19. endsley1995toward**
Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. *Human Factors, 37*(1), 32–64. https://doi.org/10.1518/001872095779049543
- **Verification:** Crossref record with abstract. No repo card exists for this paper; the related card is endsleykiris1995 (entry 20).
- **Read status:** abstract only.
- **What it establishes:** The paper presents "a theoretical model of situation awareness based on its role in dynamic human decision making." "Attention and working memory are presented as critical factors limiting operators from acquiring and interpreting information," and "mental models and goal-directed behavior are hypothesized as important mechanisms for overcoming these limits." It addresses "the impact of design features, workload, stress, system complexity, and automation" and introduces "a taxonomy of errors in situation awareness" (abstract).
- **Role in the DXD argument:** UX-cognitive-foundation. SA is the CSE construct closest to algorithmacy's "keeping track." The model assumes the situation is observable, even if hard to perceive; under algorithmacy the relevant state (what the intermediary has inferred and committed) is hidden.

**20. endsleykiris1995out**
Endsley, M. R., & Kiris, E. O. (1995). The out-of-the-loop performance problem and level of control in automation. *Human Factors, 37*(2), 381–394. https://doi.org/10.1518/001872095779064555
- **Verification:** existing card `submissions/algorithmacy_design_ethics/literature/library/endsleykiris1995.md` (S2-verified 2026-09-18); Crossref reconfirmed today.
- **Read status:** abstract only (per card).
- **What it establishes:** The out-of-the-loop problem "leaves operators of automated systems handicapped in their ability to take over manual operations in the event of automation failure," attributed to "a shift from active to passive information processing, and change in feedback provided to the operator." In a navigation task with an expert system, "low SA corresponded with out-of-the-loop performance decrements in decision time"; "Level of operator control in interacting with automation is a major factor in moderating this loss of SA" (abstract, via card).
- **Role in the DXD argument:** algorithmacy-cognitive-issue. Passive processing erodes awareness. The card notes the paper's world is one where "being in the loop is available by design choice"; on platforms the user is not offered a loop to be in.

**21. hollnagel1983cognitive**
Hollnagel, E., & Woods, D. D. (1983). Cognitive systems engineering: New wine in new bottles. *International Journal of Man-Machine Studies, 18*(6), 583–600. https://doi.org/10.1016/S0020-7373(83)80034-0 (reprinted 1999, *International Journal of Human-Computer Studies, 51*(2), 339–356, https://doi.org/10.1006/ijhc.1982.0313)
- **Verification:** Crossref records for both printings; Consensus record (abstract).
- **Read status:** abstract only.
- **What it establishes:** CSE "operates on the level of cognitive functions" and "introduces the concept of a cognitive system: an adaptive system which functions using knowledge about itself and the environment in the planning and modification of actions." "Operators are generally acknowledged to use a model of the system (machine) with which they work. Similarly, the machine has an image of the operator. The designer of an MMS must recognize this, and strive to obtain a match between the machine's image and the user characteristics on a cognitive level" (abstract).
- **Role in the DXD argument:** precursor / term-use. CSE's founding text already names the reciprocal modelling that algorithmacy turns on, since the machine holds "an image of the operator." It assumes the designer tunes that image to serve the operator. A platform tunes its image of each party to serve its own objective.

**22. woods1985cognitive**
Woods, D. D. (1985). Cognitive technologies: The design of joint human-machine cognitive systems. *AI Magazine, 6*(4), 86–92. https://doi.org/10.1609/aimag.v6i4.511
- **Verification:** OpenAlex W1726694533 (6(4), 86–92; OpenAlex dates it 1986-01-01); AAAI OJS citation metadata (date 1985/12/15, DOI). Not in Crossref.
- **Read status:** read in full (AAAI OJS PDF, journal pagination, 7 pp.).
- **What it establishes:** "Effective decision support then requires that computational technology aid the user in the process of reaching a decision, and not simply make or recommend solutions" (abstract, p. 86). Woods analyses a "hypothetical computer consultant." In it "the machine controls data gathering; the machine offers a solution," and the human becomes "an interface between the machine and its environment" (p. 87; Fig. 1 labels the human "Data Gatherer" and "Solution Filter"). Because "the user's only practical options are to accept or reject system output, there is great danger of a responsibility/authority double-bind in which the user either always rejects machine output ... or abrogates his or her decision responsibility" (p. 88). "Very little is known about what factors affect human performance at filtering another decision maker's solutions" (p. 89).
- **Role in the DXD argument:** precursor, and a direct ancestor of the algorithmacy operations. "Filtering another decision maker's solutions" is interpreting. The data-gatherer role is the platform user's position. The double-bind is the platform user's condition, with the difference that on a platform no one grants the user authority to override in the first place.

**23. klein2004ten**
Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R., & Feltovich, P. J. (2004). Ten challenges for making automation a "team player" in joint human-agent activity. *IEEE Intelligent Systems, 19*(6), 91–95. https://doi.org/10.1109/MIS.2004.74
- **Verification:** existing card `submissions/algorithmacy_design_ethics/literature/library/klein2004.md` (full text, S2-verified); Crossref reconfirmed.
- **Read status:** read in full (per card).
- **What it establishes:** Joint activity requires a Basic Compact, mutual predictability, mutual directability and common ground (p. 91). The Compact "involves a commitment to some degree of goal alignment" (p. 91). "No form of automation today or on the horizon can enter fully into the rich forms of Basic Compact that are used among people" (p. 92), and "the agents must conform to the operators' needs rather than require operators to adapt to them" (p. 94) (quotes per card).
- **Role in the DXD argument:** algorithmacy-cognitive-issue (what breaks). JCS design presumes the agent has entered the Compact. As the card notes, an intermediary pursuing an objective neither party set has not entered it, and is by the paper's definition not a team player.

### Ironies of automation and successors

**24. bainbridge1983ironies**
Bainbridge, L. (1983). Ironies of automation. *Automatica, 19*(6), 775–779. https://doi.org/10.1016/0005-1098(83)90046-8
- **Verification:** existing card `submissions/algorithmacy_design_ethics/literature/library/bainbridge1983.md` (full text, all quotes S2-verified); Crossref reconfirmed.
- **Read status:** read in full (per card).
- **What it establishes:** Process knowledge "develops only through use and feedback about its effectiveness" (p. 775). When the computer uses more dimensions and finer criteria than a human can, "there is therefore no way in which the human operator can check in real-time that the computer is following its rules correctly. ... The human monitor has been given an impossible task" (p. 776). The remedy is for the computer to decide "using methods and criteria, and at a rate, which the operator can follow, even when this may not be the most efficient method technically" (p. 777), and automatic systems "should fail obviously" (p. 777). Ephrath (1980) found "system performance was worse with computer aiding, because the operator made the decisions anyway, and checking the computer added to his workload" (p. 777) (quotes per card).
- **Role in the DXD argument:** algorithmacy-cognitive-issue (central). Bainbridge's p. 775 feedback clause is the automation-side twin of Kahneman and Klein's learning condition, and her p. 776 "impossible task" is the ceiling on what "make the algorithm legible" can deliver. Her p. 777 remedy constrains the machine's *rate and criteria*, not its disclosure, and so is not a literacy remedy.

**25. norman1990problem**
Norman, D. A. (1990). The "problem" with automation: Inappropriate feedback and interaction, not "over-automation." *Philosophical Transactions of the Royal Society of London. B, Biological Sciences, 327*(1241), 585–593. https://doi.org/10.1098/rstb.1990.0101
- **Verification:** existing card `submissions/algorithmacy_design_ethics/literature/library/norman1990.md` (full text of the ICS Report 8904 preprint; report pagination 1–8); Crossref reconfirmed.
- **Read status:** read in full (preprint, per card).
- **What it establishes:** Automation's "level of intelligence is insufficient to provide the continual, appropriate feedback that occurs naturally among human operators" (p. 1). "The culprit is not actually automation, but rather the lack of feedback" (p. 5). Systems lack feedback because "the automation itself doesn't need it!" (p. 7) (quotes per card; report pagination).
- **Role in the DXD argument:** algorithmacy-cognitive-issue (mechanism). Norman gives the design-side reason valid feedback goes missing: what the system reports is set by what the system's own task needs. On a platform that task belongs to the platform.

**26. leesee2004trust**
Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392
- **Verification:** existing card `submissions/algorithmacy_design_ethics/literature/library/leesee2004.md` (full text, journal pagination); Crossref reconfirmed.
- **Read status:** read in full (per card).
- **What it establishes:** Trust is "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability" (p. 51). Calibration is "the correspondence between a person's trust in the automation and the automation's capabilities" (p. 55). The purpose basis of trust is "the degree to which the automation is being used within the realm of the designer's intent" (p. 59). The design rule is "Design for appropriate trust, not greater trust" (p. 74) (quotes per card).
- **Role in the DXD argument:** UX-cognitive-foundation / what breaks. Calibration is the right target for DXD, but the construct is indexed to the trustor's goals. When the designer's intent is a third party's, the purpose basis inverts, as the card argues.

**27. endsley2023ironies**
Endsley, M. R. (2023). Ironies of artificial intelligence. *Ergonomics, 66*(11), 1656–1668. https://doi.org/10.1080/00140139.2023.2243404
- **Verification:** Crossref record; OpenAlex W4385514929 (abstract; the record's abstract begins mid-sentence).
- **Read status:** abstract only.
- **What it establishes:** Bainbridge's paper "was a prescient description of automation related challenges." "Not only are Bainbridge's original warnings still pertinent for AI, but AI's very nature and focus on cognitive tasks has introduced many new challenges." "Five ironies of AI are presented including difficulties with understanding AI and forming adaptations, opaqueness in AI limitations and biases that can drive human decision biases, and difficulties in understanding the AI reliability, despite the fact that AI remains insufficiently intelligent for many of its intended applications" (abstract).
- **Role in the DXD argument:** algorithmacy-cognitive-issue. This is the SA field's own statement that AI adds cognitive problems beyond classic automation: understanding, forming adaptations, opacity of limits. The ironies are still framed for operators, not for two parties coordinating through the system.

**28. strauch2018ironies**
Strauch, B. (2018). Ironies of automation: Still unresolved after all these years. *IEEE Transactions on Human-Machine Systems, 48*(5), 419–433. https://doi.org/10.1109/THMS.2017.2732506
- **Verification:** Crossref record; OpenAlex W2748347163 (abstract).
- **Read status:** abstract only.
- **What it establishes:** Bainbridge's paper shows "prescience in predicting automation-related concerns that have led to incidents and accidents." "Rasmussen's work on operator performance in process systems has perhaps been most influential" on it. "Requiring the operator to oversee an automated system that could function more accurately and more reliably than he or she could, can affect system performance in the event that operator intervention is needed" (abstract).
- **Role in the DXD argument:** precursor (lineage). It documents the Rasmussen → Bainbridge line and its accident record, and shows the ironies are unresolved even inside professional aviation and process control.

**29. janssen2019history**
Janssen, C. P., Donker, S. F., Brumby, D. P., & Kun, A. L. (2019). History and future of human-automation interaction. *International Journal of Human-Computer Studies, 131*, 99–107. https://doi.org/10.1016/j.ijhcs.2019.05.006
- **Verification:** Crossref record; OpenAlex W2945433494 (abstract; cites Bainbridge 1983).
- **Read status:** abstract only (ScienceDirect blocked).
- **What it establishes:** Reviewing 50 years of *IJHCS*, the authors find that automated systems have been used more frequently "(1) in time-sensitive or safety-critical settings, (2) in embodied and situated systems, and (3) by non-professional users." Future needs include "issues of trust, incorrect use, and confusion," "regulation and explainability," "ethical and social dilemmas," and "allowing a human and humane experience" (abstract).
- **Role in the DXD argument:** competing construct / precursor. Human-automation research already records the move from professional to non-professional users. DXD must show what it adds beyond HAI research following that shift; the triadic, third-party-objective structure is the candidate answer.

**30. carsten2018how**
Carsten, O., & Martens, M. H. (2019). How can humans understand their automated cars? HMI principles, problems and solutions. *Cognition, Technology & Work, 21*(1), 3–20. https://doi.org/10.1007/s10111-018-0484-0
- **Verification:** Crossref record (online 2018; print volume 21, 2019); OpenAlex W2799403119 (abstract; cites Vicente & Rasmussen 1992).
- **Read status:** abstract only (Springer returned a JS challenge).
- **What it establishes:** "When the driver is decoupled from active control, the design of the HMI becomes even more critical. Without mutual understanding, the two agents (human and vehicle) will fail to accurately comprehend each other's intentions and actions." Current designs "fall short of best practice and have the potential to confuse the driver," producing "a mismatch between the operation of the automation ... and the driver's awareness of how well the automation is currently handling that situation" (abstract).
- **Role in the DXD argument:** transfer case. This is CSE applied to *untrained* members of the public: the closest precedent for DXD's population. The car still serves its driver; the platform case adds the third party.

### Record-verified, not accessible (named in the brief)

**31. keen1978decision** — Keen, P. G. W., & Scott Morton, M. S. (1978). *Decision support systems: An organizational perspective* [publisher not given in the retrieved record; to verify]. Verification: OpenAlex W1569447401 (book, 1978; the record's venue field is corrupt) and Consensus record (1978). No DOI. Read status: not accessible. The book's organizational framing of DSS is the canonical second pillar after Gorry & Scott Morton; I report no content because none was read. Role: precursor.

**32. klein1993recognition** — Klein, G. A. (1993). A recognition-primed decision (RPD) model of rapid decision making. In G. A. Klein, J. Orasanu, R. Calderwood, & C. E. Zsambok (Eds.), *Decision making in action: Models and methods* (pp. [not in record]). Ablex. Verification: OpenAlex W1623168575 (chapter); the book is verified through OpenAlex W1543210409 and the review record Eisenberger (1995), *Journal of Behavioral Decision Making, 8*(3), 218–219 (https://doi.org/10.1002/bdm.3960080307), whose title gives "Klein, G.A., Orasanu, J., Calderwood, R. and Zsambok, C.E. (eds). Norwood, NJ: Ablex, 1993, 480 pp." Read status: not accessible. Content is available here only through Klein (2008)'s abstract (entry 8). Role: UX-cognitive-foundation.

**33. thordsen2003decision** — Thordsen, M., Hutton, R., & Miller, T. (2003). Decision-centered design. In E. Hollnagel (Ed.), *Handbook of cognitive task design* (pp. 383–416). CRC Press. https://doi.org/10.1201/9781410607775.ch17. Verification: Crossref chapter record (ISBNs 9780805840032, 9781410607775) and handbook record (editor Hollnagel). **Author-order flag:** the brief cites this as "Hutton, Miller & Thordsen 2003"; the Crossref record lists Thordsen first (sequence "first"), then Hutton, then Miller. Check the printed chapter before citing. Read status: not accessible. Role: precursor (method); the work that names "decision-centered design."

**34. crandall2006working** — Crandall, B., Klein, G., & Hoffman, R. R. (2006). *Working minds: A practitioner's guide to cognitive task analysis*. MIT Press. https://doi.org/10.7551/mitpress/7304.001.0001. Verification: Crossref record (type edited-book). Read status: not accessible. Role: UX-cognitive-foundation (method).

**35. vicente1999cognitive / hollnagel2005joint / woods2006joint** — Vicente, K. J. (1999). *Cognitive work analysis: Toward safe, productive, and healthy computer-based work*. Lawrence Erlbaum Associates (publisher per the Duffy, 1999, and Sanderson, 2000, review records; the DOI is registered to the CRC Press reissue). https://doi.org/10.1201/b12457. Hollnagel, E., & Woods, D. D. (2005). *Joint cognitive systems: Foundations of cognitive systems engineering*. CRC Press. https://doi.org/10.1201/9781420038194. Woods, D. D., & Hollnagel, E. (2006). *Joint cognitive systems: Patterns in cognitive systems engineering*. CRC Press. https://doi.org/10.1201/9781420005684. Verification: Crossref book records; tables of contents via Consensus records. Read status: not accessible (TOC only). At TOC level only: the 2005 volume has sections titled "The Substitution Myth," "The Accidental User," and "Ironies of Automation"; the 2006 volume has "Goal Conflicts," "Adapting to Double Binds," "Literal-Minded Agents," "Failure of Machine Explanation," and "Laws That Govern JCSs at Work." A review record (Hollnagel et al., 2007, *Journal of Risk Research, 10*(3), 413–421, https://doi.org/10.1080/13669870600899091, via Consensus) states that the JCS "is a fundamental concept of CSE, through which a human-machine ensemble is seen as a single functional entity." Role: precursor. "The Accidental User" section is the one to read first for DXD.

---

## (c) Thematic synthesis

**Cognitive engineering already designs decision experiences, and it does so for a narrower human than DXD must serve.** Gorry and Scott Morton (1971) defined the first designed decision experience by what the machine could not structure: the manager supplies "judgment and evaluation" wherever intelligence, design or choice resists specification (WP p. 13). NDM, decision-centered design and CTA then supplied a cognitive theory of that residue. Skilled deciders "rapidly categorize situations" (Klein, 2008), and good support is built around their key judgments (Militello & Hutton, 1998; Militello et al., 2016). EID adds a representational rule, which is to map the domain's real constraints onto perceptual cues so that rule-following stays valid at the edges (Vicente & Rasmussen, 1992, Sec. V.A). Three pieces transfer to DXD almost intact: the unit of design is the *decision*, not the screen; the joint human-machine system, not the machine, is what gets evaluated (Woods, 1985; Hollnagel & Woods, 1983); and support should aid "the process of reaching a decision, and not simply make or recommend solutions" (Woods, 1985, p. 86).

**These methods rest on premises the algorithmacy condition removes.** Vicente and Rasmussen name two: operators "are highly skilled and have extensive experience," and the interface serves "a single, specific application" (Sec. IV.A). Platform users are untrained and move across many intermediaries. A third premise sits in EID's own limitation. The approach works only "to the extent that designers understand the system they are building" (Sec. V.B), yet a DXD designer rarely holds the intermediary's policy. Klein et al. (2004) and Lee and See (2004) add a fourth, goal alignment. The agent must enter a Basic Compact, and trust is indexed to "an individual's goals." An intermediary that serves a third party's objective fails both definitions instead of scoring low on them. Pathirannehelage et al. (2024) reach the adjacent conclusion from the IS side, that DSS design knowledge does not extrapolate once systems "learn, adapt, and act autonomously." The objective axis is what they leave out.

**Kahneman and Klein's learning condition is the strongest candidate mechanism for why algorithmacy is hard.** Their abstract makes intuitive skill depend on "the predictability of the environment" and "the individual's opportunity to learn the regularities of that environment." Bainbridge (1983) states the automation-side version, that knowledge "develops only through use and feedback about its effectiveness" (p. 775). Norman (1990) explains why that feedback goes missing: the automation does not need it (p. 7). An adaptive intermediary degrades both conditions together. Its regularities drift because the policy is retrained, and its feedback is routed through the party whose objective differs from the user's. On this reading the difficulty of algorithmacy is structural and not a skill deficit: the environment is a low-validity one, and experience in it breeds confidence without accuracy. That mechanism is the facet's inference. No source here tests it on platform users.

**The literature disagrees about how to respond, in three places.** The first dispute concerns transparency. EID and Simkute et al. (2021) answer opacity by showing more (constraints, tailored explanations). Bainbridge's p. 776 "impossible task" and Woods's filtering problem (pp. 88–89) suggest that showing more does not help a monitor who cannot follow the machine in real time. That split maps onto the design-ethics arm's distinction between literacy-paradigm remedies and remedies that bound the intermediary's rate and criteria (Bainbridge, p. 777). The second dispute concerns control. Endsley and Kiris (1995) find that intermediate levels of control preserve awareness, while Woods (1985) warns that accept/reject control produces a "responsibility/authority double-bind." The third concerns experience. Allen and Choudhury (2022) find an inverted U, with experts rejecting correct advice, whereas Banker and Khetani (2019) find consumers over-relying on inferior recommendations. Which error dominates may depend on who the user is and on whose objective the system serves, which is the variable DXD adds.

**Human-automation research is already moving toward ordinary users, which sets DXD's burden of distinctness.** Janssen et al. (2019) record automation's spread to "non-professional users," and Carsten and Martens (2019) apply CSE to drivers of automated cars. What these transfer cases share is a system that still serves its user. The unclaimed ground is the triad, where the system reads two parties and commits outcomes for a third party's purposes.

---

## (d) Gaps and unverified leads

**Not read, and worth an OA hunt or library copy (all record-verified):**
- Kahneman & Klein (2009): body not read. The widely circulated PDFs are third-party reposts (edbatista.com, scribd, a University of Idaho course directory); I did not use them. Page-located quotes on "high-validity environments" and feedback need a legitimate copy (APA PsycNet or library).
- Arnott & Pervan (2005): a Curtin eSpace submitted version exists per Unpaywall, but the repository has migrated to curate.curtin.edu.au and blocked retrieval. The companion *Eight key issues for the decision support systems discipline* (Arnott & Pervan, 2008, *Decision Support Systems, 44*(3), 657–672, https://doi.org/10.1016/j.dss.2007.09.003) is record-verified only; no abstract was retrievable, so it has no entry.
- Endsley (2023) and Strauch (2018): abstract only; the body would supply the five ironies by name.
- Hollnagel & Woods (2005), Woods & Hollnagel (2006), Vicente (1999), Crandall et al. (2006), Keen & Scott Morton (1978), Thordsen/Hutton/Miller (2003), Klein (1993): books and chapters, not accessible through OA.
- Militello & Hutton (1998) UWE copy and Simkute et al. (2021) gold-OA copy: both exist but were blocked (403). A browser session could retrieve them.

**Record discrepancies to resolve before citation:**
- Decision-centered design chapter author order (Crossref: Thordsen, Hutton, Miller; brief: Hutton, Miller, Thordsen).
- Gorry & Scott Morton SMR 13(1), 55–70 comes from a web-search snippet, not a database record. The read text is the MIT working paper 510-71. Phillips-Wren et al. (2022) cite a "(1989)" version, presumably the SMR reprint; not verified.
- Woods (1985): the AAAI page dates it 1985-12-15; OpenAlex gives 1986. The issue is AI Magazine 6(4), Winter 1985.
- Allen & Choudhury: the LSE cover page says "(2021)"; Crossref issues it 2022-01. Use 2022.

**Unverified leads (records seen this session, not assessed as entries):**
- Parker, S. K., & Grote, G. (2022). Automation, algorithms, and beyond. *Applied Psychology, 71*(4), 1171–1204. https://doi.org/10.1111/apps.12241 — abstract names "job feedback" and "job autonomy in the context of machine learning"; bridges CSE to work design.
- Rinta-Kahila, T., et al. (2023). The vicious circles of skill erosion. *JAIS, 24*(5), 1378–1412. https://doi.org/10.17705/1jais.00829 — Bainbridge's skill decay in knowledge work.
- Schuster, N., & Lazar, S. (2024). Attention, moral skill, and algorithmic recommendation. *Philosophical Studies, 182*(1), 159–184. https://doi.org/10.1007/s11098-023-02083-6 — carries deskilling to recommender users; cites Bainbridge.
- Klein, G., et al. (1997). Applying decision requirements to user-centered design. *IJHCS* (https://doi.org/10.1006/ijhc.1996.0080) — the decision-requirements link between CTA and UCD; Consensus record only, not Crossref-checked.
- Smith, P. J., et al. (2024). Cognitive systems engineering issues in the design of machine learning systems. *HFES Proceedings* (https://doi.org/10.1177/10711813241260307) — panel with a segment titled "The Ironies of AI Based on Machine Learning"; three citations.
- Lintern, G. (2010). A comparison of the decision ladder and the recognition-primed decision model. *JCEDM, 4*(4), 304–327. https://doi.org/10.1177/155534341000400404 — reconciles the Rasmussen and Klein lines.
- Kirs, P. J., et al. (1989). An experimental validation of the Gorry and Scott Morton framework. *MIS Quarterly, 13*(2), 183–197. https://doi.org/10.2307/248926.

**Substantive gaps.** I found no work in these sources that applies CWA, EID or decision-centered design to a platform user coordinating with another party through an intermediary that serves a third objective (searched: OpenAlex citing-works of Vicente & Rasmussen 1992, Bainbridge 1983, Kahneman & Klein 2009 and Klein 2008 with algorithm/platform/recommender terms; Consensus queries 31 and 63). No study tests Kahneman and Klein's validity and feedback conditions on platform users. That gap makes the mechanism in the synthesis testable rather than established. Scholar Gateway was unreachable this session and Semantic Scholar title search was rate-limited, so those two indexes were not searched for this facet.
