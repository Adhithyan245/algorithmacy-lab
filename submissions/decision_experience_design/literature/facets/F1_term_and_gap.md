# F1 — The term, its near-synonyms, and the novelty gap check

Facet F1 of the Decision Experience Design (DXD) literature review. Built 2026-09-30 by a research agent in worktree `wt-dxd`. Every scholarly entry below is backed by a database record retrieved this session (Crossref, OpenAlex, Semantic Scholar, Unpaywall, Consensus) or by an existing verified card in this repo; the basis is stated per entry. The seven practitioner uses were verified by the lead agent in an earlier pass and are re-listed here from the brief without refetching.

**Scope question.** Does "decision experience design" exist as a scholarly term? Which near-synonyms have real literatures, and how does DXD differ from each? Has anyone already argued that designers must become experts in algorithmic literacy (or an equivalent), or proposed a design discipline organized around decisions in algorithmically mediated settings?

---

## (a) Search log

All searches were run on 2026-09-30. "Total" is the count the source reported. Semantic Scholar's `/paper/search` ranks by relevance and does not honour quotation marks, so its totals measure the index, not phrase hits; I inspected the top 8–20 results by hand. OpenAlex `title_and_abstract.search` honours quoted phrases but stems words, so its counts over-include loosely related work.

### Repository card libraries (grep, worktree)

| Source | Query | Result |
|---|---|---|
| repo grep (`submissions/*/literature`, `submissions/*/library`, `org_frontier/research/*/literature`) | `decision experience` | 0 files |
| repo grep | `decision-centered` / `decision centered` / `decision intelligence` / `decision journey` / `Kozyrkov` | 0 files each |
| repo grep | `choice architecture` | 3 files (`algorithmacy_design_ethics/literature/library/thaler2008.md`; `hospitality_phygital/library/cards/yeung2017hypernudge.md`; one LIBRARY index) |
| repo grep | `algorithmic experience` / `Alvarado` | 3 files each (`lima_pdw/literature/cards/shin2022.md`, `oeldorfhirsch2025.md`; unrelated survey card) |
| repo grep | `Magerko` | 30 files (incl. `lima_pdw/literature/cards/longmagerko2020.md`) |
| repo grep | `algorithmic literacy` / `AI literacy` | 70 / 59 files |
| repo grep | `Klein, G` | 3 files (`algorithmacy_design_ethics/literature/library/klein2004.md`) |

### Semantic Scholar (`api.semanticscholar.org/graph/v1/paper/search`, limit 20)

| Query | Total | Notes |
|---|---|---|
| `"decision experience design"` | 1,672,550 | Top 20 inspected; no work uses the phrase. Nearest: Mejtoft et al. 2019 (UX design + digital nudging in a decision process). |
| `"decision experience"` | 9,877,988 | Top 20: Peterson & Cheng 2020 uses "decision experience" as a psychological construct. |
| `DX design decision` | failed | HTTP 429 on 5 retries, twice (second attempt after 12 s spacing). |
| `decision UX` | 4,240,331 | Top 8: UI/UX of decision-support systems; no term use. |
| `designing for decisions` | 59,381 | Failed first pass; second pass OK. Top 7: AI-decision visualization, appropriate reliance; no term use. |
| `decision design` | 17,513,677 | Top 8: epidemiology "treatment decision design", enterprise-architecture "decision design graphs". |
| `decision-centered design` | 1,312,054 | Top 8 all in the cognitive-systems-engineering DCD lineage (Militello 2013; Thordsen 2003; Laughery 2002; Miller 2003). |
| `decision intelligence Pratt` | failed | HTTP 429, two passes. |
| `designers algorithmic literacy` | failed | HTTP 429, two passes. |
| `UX practitioners AI literacy competence` | failed | HTTP 429, two passes. |
| `designing for algorithmic experience` | failed | HTTP 429, two passes. |
| `human-AI interaction design competencies UX designers` | failed | HTTP 429, two passes. |
| batch lookup by DOI (`/paper/batch`) | 3 calls | Used for abstracts; one call returned a merged record for Weinmann 2016 / Schneider 2018 (S2 conflates them). |

Six of twelve Semantic Scholar searches never completed. I covered the same ground with OpenAlex and Consensus (below), but the Semantic Scholar leg of the gap check is incomplete.

### OpenAlex (`api.openalex.org/works`, `filter=title_and_abstract.search:`, sorted by citations)

| Filter value | Total | Notes |
|---|---|---|
| `"decision experience design"` | **0** | |
| `"decision experience"` | 409 | Mostly "decisions from experience" (description–experience gap) and incidental co-occurrence. |
| `"decision experience" AND (algorithm OR algorithmic OR "artificial intelligence")` | 25 | None uses the phrase as a design concept. |
| `"decision UX"` | 3 | None relevant. |
| `"decision-centered design"` / `"decision centered design"` | 38 / 38 | DCD lineage (Militello, Thordsen, Porat, Harle). |
| `"decision-centric design"` | 13 | Includes O'Hare et al. 1998 ("decision centred"). |
| DCD variants, sorted by year ascending | 51 | Earliest indexed 1996; Wolf, Klein & Thordsen (NAECON 1991) is misdated 2002 in OpenAlex. |
| `"decision intelligence"` | 1,645 | Engineering/ML control and business-process papers; Hasić et al. 2018. |
| `"decision architecture"` | 1,752 | Software architecture, multi-UAV, dark patterns, defaults. |
| `"designing for decisions"` | 857 | Stemmed; includes Jonassen 2012 (instructional design). |
| `"decision design"` | 2,209 | Clinical and marketing co-occurrence. |
| `"algorithmic experience"` | 294 | Shin 2020 (×2), Alvarado & Waern 2018, Lomborg 2019. |
| `"algorithmic experience" AND (designer OR designers OR "design practice")` | 5 | Olsson & Väänänen 2021; Szlachta 2024. |
| `"designers" AND "algorithmic literacy"` | 16 | Dasgupta 2023, MIT Press chapter "Designing for critical algorithmic literacies" (designing *for* learners' literacies). |
| `"UX practitioners" AND "AI literacy"` | **0** | |
| `"AI literacy" AND ("UX designers" OR "design practitioners" OR "UX practitioners")` | 4 | Li et al. 2024 (×2); Álvarez 2026; a KTH thesis. |
| `"designers" AND "AI literacy"` | 305 | Mostly K-12 AI-literacy education; Li et al. 2024. |
| `"human-AI interaction" AND "design competencies"` | 2 | Szlachta 2024. |
| `"human-algorithm interaction" AND (designer OR designers)` | 4 | Agner et al. 2020 (UX of recommenders). |
| `"machine learning" AND "design material"` | 240 | Dove et al. 2017. |
| `algorithmacy` | **0** | The lab's construct has no indexed uses outside the lab. |
| `"choice architecture" AND "user experience"` | 31 | Jesse 2021; Egelman 2013. |
| `"choice architect" AND (designer OR designers) AND (algorithm OR algorithmic)` | **0** | |
| `"digital nudging"` | 756 | Weinmann 2016; Schneider 2018; Hummel 2019. |
| `"consumer decision journey"` | 156 | Marketing; Hamilton et al. 2018; Santos & Gonçalves 2021. |
| `"consumer decision journey" AND Court` | 3 | Santos & Gonçalves 2021. |
| `"decision journey" AND (algorithm OR algorithmic OR recommender)` | 35 | Classification of UGC into journey stages; none design-oriented. |
| `"decision support" AND "user experience design"` | 20 | Mejtoft 2019; Gao et al. 2022/2024 (clinical decision support UX); Yang 2021 thesis. |

### OpenAlex snowball (citing works and references)

| Seed | Filter | Total | Notes |
|---|---|---|---|
| Alvarado & Waern 2018 (W2795636034) | `cites:` | 128 | Top-cited citers: Sundar 2019 (HAII), Holstein 2019, Shin 2020, Oeldorf-Hirsch 2023, Alvarado 2020. |
| Alvarado & Waern 2018 | `cites:` + `designer OR designers` | 6 | Sun et al. 2023 (UX value framework for ML products); none argues for designer expertise in users' algorithmic competence. |
| Shin, Zhong & Biocca 2020 (W3000616040) | `cites:` + `designer OR designers OR design` | 84 | Dominated by Shin's own acceptance-model papers. |
| Yang et al. 2020 (W3032875465) | `cites:` | 603 | |
| Yang et al. 2020 | `cites:` + `competency OR competencies OR curriculum OR literacy OR education` | 63 | Li et al. 2024; Flechtner & Stankowski 2023; Yildirim 2023. |
| Dove et al. 2017 (W2611748211) | `cites:` + same terms | 27 | Yang et al. 2018 (DIS); Flechtner & Stankowski 2023; Wärnestål 2022. |
| Lemon & Verhoef 2016 (W2422895071) | `cited_by:` + title `decision journey` | 0 | Court et al. 2009 is not an OpenAlex work. |
| Santos & Gonçalves 2021 (W3196010490) | `cited_by:` + title `consumer decision journey` | 5 | 125 references in all; Court et al. 2009 again absent as a work. |

### arXiv (`export.arxiv.org/api/query`)

| Query | Total | Notes |
|---|---|---|
| `all:"decision experience design"` | **0** | |
| `all:"decision experience" AND all:design` | 17 | None relevant (agent memory, RL). |
| `all:"algorithmic experience"` | 325 | Top 8 are algorithm-performance papers; no AX-design hit in top 8. |
| `all:"decision intelligence"` | 37 | IoT/power systems/enterprise AI. |
| `all:"decision-centered design"` | **0** | |
| `all:"AI literacy" AND all:designers` | 154 | Top 8 education-focused. |
| `all:"algorithmic literacy" AND all:designers` | 5 | "Designing for Critical Algorithmic Literacies" (arXiv 2008.01719, 2020); end-user audit tools. |

### Consensus (`mcp__claude_ai_Consensus__search`, 6 calls)

| Query | Shown | Notes |
|---|---|---|
| `decision experience design as a design discipline` | 20 | No work uses the term. Returned experience-design and design-decision work (Trischler 2021; Suri 2003; Mortati 2022). |
| `UX designers need competence in algorithmic literacy or AI literacy to design human-algorithm interaction` | 19 | Long & Magerko 2020; Szlachta 2024; Yang 2020; Liao 2023; Muralikumar 2024; Feng 2023; Shalamova 2026. |
| `algorithmic experience design framework beyond user experience` | 20 | Shin 2020; Alvarado & Waern 2018; Klumbytė 2020; Alvarado 2019; Verganti 2020; Baumer 2017. |
| `choice architecture as a design discipline for user interface designers digital nudging` | 20 | Mertens 2021 meta-analysis; Schneider et al. (preprint record); Caraban 2019; da Cunha 2020 ("software designers as choice architects"). |
| `Beyond nudges: tools of a choice architecture Johnson` | 20 | Johnson et al. 2012 abstract. |
| `decision intelligence as a discipline definition human decision making and AI` | 20 | O'Callaghan 2023 (CRC book); Lai et al. 2023; Steyvers & Kumar 2023; Shrestha 2019. |

### Scholar Gateway

| Query | Result |
|---|---|
| "Should user experience designers become experts in how users interpret, instruct and monitor opaque adaptive algorithms…" | **Error:** `INVALID_QUERY: Could not resolve user identity from CONNECT`. Scholar Gateway could not be reached; the connector may need reconnecting. |
| "decision-centered design in cognitive systems engineering…" | Same error. |

### Crossref, Unpaywall, and web

| Source | Query | Result |
|---|---|---|
| Crossref `query.bibliographic` | 28 record-verification lookups (one per candidate) | Each matched its target record at rank 1; totals are relevance counts and not meaningful. |
| Unpaywall | 11 DOIs | OA copies found: Verganti 2020 (Padova repository), Caraban 2019, Weinmann 2016 (Springer, bot-challenged); closed: Alvarado & Waern 2018, Dove 2017, Shin 2020, Thordsen 2003, Johnson 2012. |
| WebSearch | `"decision experience design" OR "decision experience designer"` | 10 results; none uses the phrase as a discipline or job title. |
| WebSearch | `"Towards Algorithmic Experience" Alvarado Waern pdf five functional categories` | Led to Alvarado's 2017 Uppsala master's thesis on DiVA (read). |
| WebSearch | `Cassie Kozyrkov "decision intelligence" definition…` | 9 results (speaker bios, Fast Company, LinkedIn); primary text not retrieved. |
| WebFetch | Fast Company (Kozyrkov); McKinsey (Court et al. 2009); ACM DL PDFs; Springer; Oxford Academic | 403 / timeout / Cloudflare or bot challenge / navigation-only. Not accessible. |
| WebFetch | repositorio.ulisboa.pt (Santos & Gonçalves 2021) | Abstract retrieved. |

---

## (b) Entries

Read-status key: **read in full** = OA full text read this session, or a card built from full text; **read in part** = OA full text accessed and specific sections read (sections named); **abstract only**; **record only** = bibliographic record without abstract; **not accessible**.

### Cluster 1 — The exact term and its practitioner uses

#### G1–G7 · Practitioner uses of "Decision Experience (DX)" (grey literature, 2023–2026)

- **Verification basis:** verified by the lead agent in an earlier pass (brief of 2026-09-30); not refetched by F1. Titles, full author names and URLs should be carried from the lead's verification log. I found no additional practitioner uses in my WebSearch for the exact phrase (10 results, none relevant).
- **Read status:** per the lead's log.

| Key | Source as given in brief | What it shows |
|---|---|---|
| G1 `wilkinson2023dx` | Wilkinson, Magine Pro, 2023-09-14, "Decision Experience (DX)" | Earliest dated practitioner use in the set. |
| G2 `audryNDdx` | Audry, andrewaudry.com/dxdesign, undated, "Dx designer" | Frames DX around making internal (organizational) decisions "system-ready". |
| G3 `itera2025dx` | Itera (itera.cl), 2025-07-04, Spanish, "DX" | Decision canvas; "time-to-decision" as the metric. |
| G4 `putri2025dx` | Putri, Medium, 2025-12-02, "decision experience design problem" | Reports activation 14.8% → 50.6% (figures as given in the brief, not re-checked by F1). |
| G5 `pastagia2026dx` | Pastagia, LinkedIn, ~2026-06, "Decision Experience (DX)" | Practitioner framing. |
| G6 `dscc2026dx` | Danish-Swiss Chamber of Commerce event, Saxo Bank HQ, 2026-09-03 | Evidence that the label reaches business-association programming. |
| G7 `rupashree2026decision` | Rupashree, Medium, 2026-07-26, "decision architecture" | Near-synonym in practitioner writing. |

**Role in the DXD argument:** term-use (grey). The label is live in practice, but in these sources DX means designing *organizational* decision processes or *conversion* decisions. None, on the brief's summary, frames DX around an opaque adaptive intermediary.

#### `peterson2022decision`
Peterson, N., & Cheng, J. (2022). Decision experience in hyperchoice: The role of numeracy and age differences. *Current Psychology, 41*(8), 5399–5411. https://doi.org/10.1007/s12144-020-01041-3 (published online 14 Sep 2020)
- **Verification:** Crossref record (print 2022-08; online 2020-09-14); Semantic Scholar batch record with full abstract.
- **Read status:** abstract only.
- **What it establishes:** This is the one scholarly use of "decision experience" that I found treating it as a construct: the chooser's post-choice *difficulty* and *satisfaction*. The sample was 116 older and 112 younger adults from Amazon Mechanical Turk, with a hyperchoice condition of "sixteen options" against a simple-choice condition of "four options" in consumer and gamble tasks. "Hyperchoice was related to greater decision difficulty in both choice tasks." Numeracy moderated the effect in the gamble task only, and older adults "reported greater decision difficulty and lower decision satisfaction, regardless of choice condition" (abstract).
- **Role in the DXD argument:** term-use / UX-cognitive-foundation. It gives DXD a ready outcome measure (experienced difficulty and satisfaction) and a precedent that individual competence (numeracy) moderates the decision experience, which is structurally the claim DXD makes about algorithmacy.

### Cluster 2 — Near-synonyms with scholarly literatures

#### `wolf1991decision`
Wolf, S. P., Klein, G. A., & Thordsen, M. L. (1991). Decision-centered design requirements. In *Proceedings of the IEEE 1991 National Aerospace and Electronics Conference (NAECON 1991)* (pp. 800–805). IEEE. https://doi.org/10.1109/naecon.1991.165845
- **Verification:** Crossref record (event: NAECON 1991, Dayton, OH; Crossref issued-date field is empty); OpenAlex abstract (OpenAlex misdates it 2002).
- **Read status:** abstract only.
- **What it establishes:** This is the earliest dated use of "decision-centered design" I found. The authors propose a method that "would ensure that decisions central to a task are identified and that those decisions would serve as the focus of the design," with requirements coming "from the decision makers". The method uses critical decision method (CDM) interviewing and concept mapping, applied to a surveillance-aircraft crew position and naval anti-air-warfare stations (abstract).
- **Role in the DXD argument:** precursor. This is the strongest scholarly precedent for making the *decision* design's unit of analysis, and it dates the idea to 1991.

#### `ohare1998cognitive`
O'Hare, D., Wiggins, M., Williams, A., & Wong, W. (1998). Cognitive task analyses for decision centred design and training. *Ergonomics, 41*(11), 1698–1718. https://doi.org/10.1080/001401398186144
- **Verification:** Crossref record; OpenAlex abstract.
- **Read status:** abstract only.
- **What it establishes:** Three case studies apply "a modification of the critical decision method of Klein et al." to white-water rafting guides, general-aviation pilots and emergency ambulance dispatchers. Two produce training tools; the third redesigns "the VDU display requirements for the ambulance dispatchers" (abstract).
- **Role in the DXD argument:** precursor. It shows DCD already moving into interface redesign by 1998, but always for trained experts in naturalistic settings.

#### `thordsen2003decision`
Thordsen, M., Hutton, R., & Miller, T. (2003). Decision-centered design: Leveraging cognitive task analysis in design. In E. Hollnagel (Ed.), *Handbook of cognitive task design* (pp. 383–416). CRC Press. https://doi.org/10.1201/9781410607775.ch17
- **Verification:** Crossref chapter record (authors, pages 383–416, ISBNs 9780805840032 / 9781410607775) and Crossref book record (editor Hollnagel, CRC Press, June 2003); Semantic Scholar supplies the subtitle.
- **Read status:** not accessible (closed; no OA copy per Unpaywall).
- **What it establishes (from record only):** This is the handbook chapter the brief names, and it confirms that DCD was consolidated as a cognitive-task-design method in the human-factors canon by 2003. I cannot report its content.
- **Role in the DXD argument:** precursor.

#### `militello2013decision`
Militello, L. G., & Klein, G. (2013). Decision-centered design. In J. D. Lee & A. Kirlik (Eds.), *The Oxford handbook of cognitive engineering*. Oxford University Press. https://doi.org/10.1093/oxfordhb/9780199757183.013.0016
- **Verification:** Crossref chapter record (online 2013-02-12) and Crossref book record (editors Lee & Kirlik).
- **Read status:** not accessible (Oxford Academic returned navigation only; closed).
- **What it establishes (from record and citing works):** DCD had its own chapter in the field's reference handbook by 2013. OpenAlex and Semantic Scholar show continuing clinical applications, such as colorectal-cancer screening decision support (Militello et al. 2016, 2017) and chronic-pain visualizations (Harle et al. 2019).
- **Role in the DXD argument:** precursor / competing construct. DXD must distinguish itself from DCD explicitly.

#### `hasic2018augmenting`
Hasić, F., De Smedt, J., & Vanthienen, J. (2018). Augmenting processes with decision intelligence: Principles for integrated modelling. *Decision Support Systems, 107*, 1–12. https://doi.org/10.1016/j.dss.2017.12.008
- **Verification:** Crossref record; OpenAlex (green OA at lirias.kuleuven.be).
- **Read status:** read in part (abstract and §1 of the author preprint, 16 Jan 2018).
- **What it establishes:** In the peer-reviewed decision-support literature, "decision intelligence" labels *organizational process-and-decision modelling*. The paper formalizes the Decision Model and Notation (DMN) standard alongside BPMN and proposes "Five Principles for integrated Process and Decision Modelling (5PDM)", validated "on a case of a Belgian accounting company" (abstract). A text search of the preprint finds "decision intelligence" only in the title.
- **Role in the DXD argument:** competing construct. The scholarly DI literature concerns how organizations model and automate their decisions, not how a person experiences a decision.

#### `pratt2019link`
Pratt, L. (2019). *Link: How decision intelligence connects data, actions, and outcomes for a better world*. Emerald Publishing. https://doi.org/10.1108/9781787696532
- **Verification:** Crossref monograph record; OpenAlex publisher description.
- **Read status:** abstract only (the publisher's description, not an abstract).
- **What it establishes:** The book presents DI as going "beyond AI", "connecting human decision makers in multiple areas like economics, optimization, big data, analytics, psychology, simulation, game theory", and as a way to "design solutions that change the way problems are considered" (publisher description via OpenAlex). This is a trade monograph, not peer-reviewed research.
- **Role in the DXD argument:** competing construct (practitioner-scholarly boundary). DI claims the "decision" territory from the data-science side; its subject is the organization's decision model, not the lay user's experience of an intermediary.

#### `thaler2008nudge` (existing card)
Thaler, R. H., & Sunstein, C. R. (2008). *Nudge: Improving decisions about health, wealth, and happiness*. Yale University Press.
- **Verification:** existing card `submissions/algorithmacy_design_ethics/literature/library/thaler2008.md`. The card records that no ISBN was verified.
- **Read status:** secondary per the card. Its author did not open *Nudge*, and the card is built from Thaler's 2018 *Science* editorial (doi:10.1126/science.aau9241) and Sunstein's "Sludge and Ordeals" draft.
- **What it establishes:** Per the card, the framework's one-sentence statement is "By improving the environment in which people choose—what we call the 'choice architecture'—they can make wiser choices without restricting any options," with the normative test "as judged by themselves."
- **Role in the DXD argument:** precursor / competing construct. Choice architecture is the most established "designing decisions" discipline, and it assumes an architect who shares or serves the chooser's ends.

#### `johnson2012beyond`
Johnson, E. J., Shu, S. B., Dellaert, B. G. C., Fox, C., Goldstein, D. G., Häubl, G., Larrick, R. P., Payne, J. W., Peters, E., Schkade, D., Wansink, B., & Weber, E. U. (2012). Beyond nudges: Tools of a choice architecture. *Marketing Letters, 23*(2), 487–504. https://doi.org/10.1007/s11002-012-9186-1
- **Verification:** Crossref record (12 authors); abstract via Consensus.
- **Read status:** abstract only.
- **What it establishes:** Choice architecture is treated as a toolkit for "anyone who present[s] people with choices", divided into tools "used in structuring the choice task" (what to present) and tools "used in describing the choice options" (how to present it). It also addresses "individual differences and errors in evaluation of choice outcomes" (abstract).
- **Role in the DXD argument:** precursor. It turns nudging into a design toolkit, the nearest analogue to the cognitive-science toolkit that professionalized UX.

#### `schneider2018digital`
Schneider, C., Weinmann, M., & vom Brocke, J. (2018). Digital nudging: Guiding online user choices through interface design. *Communications of the ACM, 61*(7), 67–73. https://doi.org/10.1145/3213765
- **Verification:** Crossref record (vol. 61, issue 7, pp. 67–73). The definition quoted below comes from the abstract of a Consensus record titled "Digital Nudging–Guiding Choices by Using Interface Design" (same authors, dated 2017, venue given as CACM), which I take to be the preprint. The companion piece Weinmann, Schneider & vom Brocke (2016), *Business & Information Systems Engineering 58*(6), 433–436 (doi:10.1007/s12599-016-0453-1), is Crossref-verified, but I could not read it: Springer served a bot challenge.
- **Read status:** abstract only (preprint abstract).
- **What it establishes:** "The more decisions people make using digital devices, the more the software engineer becomes a choice architect who knowingly or unknowingly influences people's decisions." The authors define "'digital nudging' as the use of user-interface design elements to guide people's behavior in digital choice environments" and present "a digital nudge design process" for "online choice architects" (preprint abstract).
- **Role in the DXD argument:** precursor. This is the explicit claim that interface designers are choice architects, the step just before DXD. The influence still runs from designer to user, and the architect is human.

#### `caraban2019ways`
Caraban, A., Karapanos, E., Gonçalves, D., & Campos, P. (2019). 23 ways to nudge: A review of technology-mediated nudging in human-computer interaction. In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (pp. 1–15). ACM. https://doi.org/10.1145/3290605.3300733
- **Verification:** Crossref record; OpenAlex abstract.
- **Read status:** abstract only (the gold OA PDF sits behind a Cloudflare challenge).
- **What it establishes:** The review found "23 distinct mechanisms of nudging, grouped in 6 categories, and leveraging 15 different cognitive biases," presented "as a framework for technology-mediated nudging". It also reports that the idea "was eagerly adopted in HCI" after Thaler and Sunstein (abstract).
- **Role in the DXD argument:** UX-cognitive-foundation. It shows HCI already importing decision science (biases) as design knowledge, the way UX imported perception and cognitive load. Every mechanism targets the user's biases, not the user's model of an adaptive system.

#### `santos2021consumer`
Santos, S., & Gonçalves, H. M. (2021). The consumer decision journey: A literature review of the foundational models and theories and a future perspective. *Technological Forecasting and Social Change, 173*, Article 121117. https://doi.org/10.1016/j.techfore.2021.121117
- **Verification:** Crossref record; abstract read at repositorio.ulisboa.pt (green OA handle 10400.5/25098).
- **Read status:** abstract only.
- **What it establishes:** "Although the term originally emerged with Court et al. in 2009," the consumer journey draws on "distinct literature and theoretical roots". The review covers "74 relevant papers" from SCOPUS plus backward and forward citation analysis, and names "the lack of academic studies reflecting on the influence of more recent technologies based on artificial intelligence on the consumer journey" (abstract).
- **Role in the DXD argument:** competing construct. It dates the CDJ term to Court et al. 2009 (a McKinsey grey source, see Gaps) and confirms that the marketing literature had not yet theorized AI's effect on the journey as of 2021. CDJ maps the path from the firm's side; it is not a design discipline for the chooser.

#### `verganti2020innovation`
Verganti, R., Vendraminelli, L., & Iansiti, M. (2020). Innovation and design in the age of artificial intelligence. *Journal of Product Innovation Management, 37*(3), 212–227. https://doi.org/10.1111/jpim.12523
- **Verification:** Crossref record; published-version PDF from the University of Padova repository (research.unipd.it).
- **Read status:** read in part (abstract p. 212 and the sensemaking discussion).
- **What it establishes:** The authors equate design with decision-making: "This 'decision making' side of innovation is what scholars and practitioners refer to as 'design.'" They argue that "as creative problem-solving is significantly conducted by algorithms, human design increasingly becomes an activity of sensemaking," and that "AI enables the creation of solutions that are more highly user centered than human-based approaches (i.e., to an extreme level of granularity, designed for every single person)" (p. 212).
- **Role in the DXD argument:** competing construct / counterevidence. On this account AI moves the *designer* toward sensemaking and problem framing. It says nothing about the *user's* new cognitive work; DXD argues the complement.

#### `lai2023science`
Lai, V., Chen, C., Smith-Renner, A., Liao, Q. V., & Tan, C. (2023). Towards a science of human-AI decision making: An overview of design space in empirical human-subject studies. In *Proceedings of the 2023 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1369–1385). ACM. https://doi.org/10.1145/3593013.3594087
- **Verification:** Crossref record; abstract via Consensus.
- **Read status:** abstract only.
- **What it establishes:** The survey covers "over 100 papers" of empirical human-subject studies on AI-assisted decisions and organizes the "design space" into "(1) decision tasks, (2) AI assistance elements, and (3) evaluation metrics". It calls for "common frameworks to account for the design and research spaces of human-AI decision making" (abstract).
- **Role in the DXD argument:** competing construct. This is the closest *current* scholarly field that combines decision, algorithm and design. It is framed as a research science, not a design profession, and its setting is dyadic: one human decides with AI advice. DXD's setting is one where the intermediary commits the decision for two parties.

### Cluster 3 — Gap check: algorithmic experience and designer competence

#### `alvarado2017towards`
Alvarado Rodríguez, O. L. (2017). *Towards algorithmic experience: Redesigning Facebook's news feed* [Master's thesis, Uppsala University, Department of Informatics and Media]. DiVA. https://www.diva-portal.org/smash/get/diva2:1110570/FULLTEXT01.pdf
- **Verification:** full-text PDF retrieved from DiVA (title page: 30 hp, VT 2017, supervisor Annika Waern).
- **Read status:** read in part (abstract; background §2, p. 10; research-question section).
- **What it establishes:** This is the origin of the AX concept. "The concept of algorithmic experience should be opened to all kinds of technologies (now and in the future) that affect the user experience through the decisions and interventions of non-human actors" (p. 10). Alvarado calls the target algorithms "experience worthy" (p. 10). The five areas are "algorithmic profiling transparency, algorithmic profiling management, algorithmic awareness, algorithmic user-control and selective algorithmic remembering" (abstract).
- **Role in the DXD argument:** precursor (key). AX already ties the successor-to-UX idea to *decisions by non-human actors*.

#### `alvarado2018towards`
Alvarado, O., & Waern, A. (2018). Towards algorithmic experience: Initial efforts for social media contexts. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. https://doi.org/10.1145/3173574.3173860
- **Verification:** Crossref record (CHI '18, Montréal); OpenAlex abstract; Consensus record. The brief's likely key precursor is confirmed.
- **Read status:** abstract only (closed; Unpaywall finds no OA copy).
- **What it establishes:** "Human-Computer Interaction research needs to develop analytical tools for describing the interaction with, and experience of algorithms." From participatory workshops on Facebook's news feed, the authors "propose the concept of Algorithmic Experience (AX) as an analytic framing" with "five functional categories … profiling transparency and management, algorithmic awareness and control, and selective algorithmic memory" (abstract). OpenAlex counts 128 citing works. Alvarado et al. (2019, INTERACT, doi:10.1007/978-3-030-29387-1_30, Crossref-verified, abstract via Consensus) extend the framework with "algorithmic usefulness and algorithmic social practices".
- **Role in the DXD argument:** precursor (key) / literacy-paradigm contrast. AX is the nearest prior proposal for an experience discipline built around algorithms. Its five categories are transparency, awareness and control remedies, which are exactly the "make the algorithm legible" moves that the lab's design-ethics arm calls literacy extended to a new medium.

#### `shin2020beyond`
Shin, D., Zhong, B., & Biocca, F. A. (2020). Beyond user experience: What constitutes algorithmic experiences? *International Journal of Information Management, 52*, Article 102061. https://doi.org/10.1016/j.ijinfomgt.2019.102061
- **Verification:** Crossref record; Semantic Scholar and OpenAlex abstract.
- **Read status:** abstract only (closed).
- **What it establishes:** The paper proposes "the Algorithm Acceptance Model to conceptualize the notion of AX as part of the analytic framework for human-algorithm interaction". It reports that "AX is inherently related to human understanding of fairness, transparency, and other conventional components of user-experience" (abstract). The abstract gives no sample or effect sizes. The existing card `submissions/lima_pdw/literature/cards/shin2022.md` records how Shin's later work absorbs algorithm literacy into acceptance modelling.
- **Role in the DXD argument:** precursor / competing construct. The title makes the "beyond UX" claim, but the construct is operationalized as acceptance of and satisfaction with algorithm services, not as a design competence.

#### `klumbyte2020reframing`
Klumbytė, G., Lücking, P., & Draude, C. (2020). Reframing AX with critical design: The potentials and limits of algorithmic experience as a critical design concept. In *Proceedings of the 11th Nordic Conference on Human-Computer Interaction: Shaping Experiences, Shaping Society* (pp. 1–12). ACM. https://doi.org/10.1145/3419249.3420120
- **Verification:** Crossref record (NordiCHI '20, Tallinn); OpenAlex abstract.
- **Read status:** abstract only.
- **What it establishes:** The authors argue "that critical design can and should be used for AX and human-algorithm interaction design in order to support algorithmic literacy and critical capacity of the users," reflecting on a critical artifact, the "Social Privilege Estimator" (abstract).
- **Role in the DXD argument:** precursor. This is the one AX paper that makes *users'* algorithmic literacy a design target. The designer's role is critical provocation; nothing here builds designer expertise in that literacy.

#### `dove2017ux`
Dove, G., Halskov, K., Forlizzi, J., & Zimmerman, J. (2017). UX design innovation: Challenges for working with machine learning as a design material. In *Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems* (pp. 278–288). ACM. https://doi.org/10.1145/3025453.3025739
- **Verification:** Crossref record; OpenAlex abstract.
- **Read status:** abstract only (closed; a submitted version is listed at pure.au.dk but not retrieved).
- **What it establishes:** ML "has not experienced a wealth of design innovation", possibly because "it is a new and difficult design material". The authors surveyed UX practitioners on "how ML may or may not have been a part of their UX design education" and propose "challenges for UX and interaction design research and education" (abstract).
- **Role in the DXD argument:** algorithmacy-cognitive-issue (designer side). This launched the "AI as design material" line, in which the designer's needed expertise concerns the *material*, not the user's cognition of it.

#### `yang2018investigating`
Yang, Q., Scuito, A., Zimmerman, J., Forlizzi, J., & Steinfeld, A. (2018). Investigating how experienced UX designers effectively work with machine learning. In *Proceedings of the 2018 Designing Interactive Systems Conference* (pp. 585–596). ACM. https://doi.org/10.1145/3196709.3196730
- **Verification:** Crossref record (DIS '18, Hong Kong); OpenAlex abstract.
- **Read status:** abstract only (the gold OA PDF sits behind a Cloudflare challenge).
- **What it establishes:** The study interviewed 13 designers with "many years of experience designing the UX of ML-enhanced products". "They shared they do not view themselves as ML experts, nor do they think learning more about ML would make them better designers." They "appeared to be the most successful when they engaged in ongoing collaboration with data scientists" and "embraced a data-centric culture" (abstract).
- **Role in the DXD argument:** **counterevidence.** Expert practitioners reject the premise that designers must acquire technical AI expertise. DXD must say that its expertise is in the *user's* interpretive and monitoring work, not in ML.

#### `yang2020reexamining`
Yang, Q., Steinfeld, A., Rosé, C., & Zimmerman, J. (2020). Re-examining whether, why, and how human-AI interaction is uniquely difficult to design. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). ACM. https://doi.org/10.1145/3313831.3376301
- **Verification:** Crossref record; OpenAlex and Consensus abstract.
- **Read status:** abstract only (ACM PDF returned 403 to WebFetch and a Cloudflare challenge to curl).
- **What it establishes:** The paper identifies "two sources of AI's distinctive design challenges: 1) uncertainty surrounding AI's capabilities, 2) AI's output complexity, spanning from simple to adaptive complex," and "four levels of AI systems", on each of which "designers encounter a different subset of the design challenges" (abstract). OpenAlex counts 603 citing works.
- **Role in the DXD argument:** algorithmacy-cognitive-issue. "Adaptive complex" output is the design-side name for the opaque, adaptive intermediary in the algorithmacy definition. The paper frames it as a difficulty for designers, not as a new cognitive task for users.

#### `szlachta2024navigating`
Szlachta, A. M. (2024). Nawigowanie wśród złożoności sztucznej inteligencji. Kluczowe kompetencje techniczne projektantów UX niezbędne w tworzeniu produktów cyfrowych opartych na sztucznej inteligencji (AI) [Navigating the AI complexity: Key technical competency of UX designers necessary to make AI-based digital products]. *Formy, 22*. Academy of Fine Arts in Kraków. https://doi.org/10.52652/fxyz.22.24.5
- **Verification:** Crossref record; OpenAlex (bronze OA PDF at formy.xyz); Consensus record.
- **Read status:** **read in full** (the Polish PDF, 14 pp., published 25 Oct 2024; locators use the PDF's "N/14" pages; English renderings below are my translations).
- **What it establishes:** This is the closest single precedent for the "designers must upskill for AI" claim, and it uses AX vocabulary ("doświadczenie algorytmiczne", "algorithmic experience", listed as a keyword on p. 1/14). Szlachta cites Zimmerman's "AI innovation gap" and lists its three causes, the first being "brak podstawowej wiedzy technicznej projektantów UX o technologiach AI" [UX designers' lack of basic technical knowledge of AI technologies] (p. 4/14). She draws the analogy to the web era, when designers were expected to know "HTML i CSS", "not so that they would replace programmers" (p. 7/14). Her competence list includes "umiejętność prowadzenia badań z zakresu algorithmic experience z użytkownikami" [the ability to run algorithmic-experience research with users] (p. 7/14). The competences are otherwise *technical*: AI types, terminology, and the data-science process.
- **Role in the DXD argument:** precursor (key). It makes the "designers must acquire new expertise, as they once learned HTML/CSS" argument, but the expertise is knowledge of the model, not of the user's algorithmacy.

#### `flechtner2023ai`
Flechtner, R., & Stankowski, A. (2023). AI is not a wildcard: Challenges for integrating AI into the design curriculum. In *Proceedings of the 5th Annual Symposium on HCI Education (EduCHI '23)* (pp. 72–77). ACM. https://doi.org/10.1145/3587399.3587410
- **Verification:** Crossref record (EduCHI, Hamburg); OpenAlex abstract.
- **Read status:** abstract only.
- **What it establishes:** Designers "are well-positioned to drive stakeholder-centered adaption of artificial intelligence (AI) technology," but "the structural implementation of AI technologies in the design curriculum remains an unsolved challenge." The authors outline "the knowledge and technical intuition on AI we believe students must engage meaningfully with" (abstract).
- **Role in the DXD argument:** precursor (design education). Again the expertise named is "technical intuition" about AI.

#### `li2024user`
Li, J., Cao, H., Lin, L., Hou, Y., Zhu, R., & El Ali, A. (2024). User experience design professionals' perceptions of generative artificial intelligence. In *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)* (pp. 1–18). ACM. https://doi.org/10.1145/3613904.3642114
- **Verification:** Crossref record; OpenAlex (green OA at ir.cwi.nl).
- **Read status:** read in part (abstract, §5.7.2, §6.3).
- **What it establishes:** The study interviewed 20 UX designers. §6.3, "AI Literacy and Participatory AI in UX Design," defines designer AI literacy as beginning "with a fundamental understanding of AI concepts, including how machine learning works, the types of AI systems, their capabilities, limitations, and implications," and adds that "UX Designers should be able to think critically and question AI-generated outputs." §5.7.2 reports participants' "hope for increased AI literacy through education".
- **Role in the DXD argument:** competing construct. "AI literacy for designers" here means designers as *users of GenAI tools*, a third sense distinct from both technical material knowledge and expertise in end-users' algorithmacy.

#### `shalamova2026ai`
Shalamova, N., Richards, K., & Miller, C. (2026). AI is here. Is UX ready? A four-dimension framework for curriculum design. In *Proceedings of the 8th Annual Symposium on HCI Education (EduCHI '26)* (pp. 1–7). ACM. https://doi.org/10.1145/3803869.3803888
- **Verification:** Crossref record (EduCHI '26, Toronto, 20 May 2026); OpenAlex and Consensus abstract.
- **Read status:** abstract only (the gold OA copy sits behind a Cloudflare challenge).
- **What it establishes:** "UX education remains structurally amorphous, lacking formal accreditation, unified standards, or shared visions for what AI readiness for UX students should look like." The framework's four dimensions are "1) Foundational knowledge of AI technologies 2) Practical application of AI tools … 3) Critical Evaluation of AI outputs and assumptions, and 4) Social Responsibility" (abstract).
- **Role in the DXD argument:** precursor (2026, very recent). It confirms that the UX-education field is asking the professionalization question now, with no dimension for the end-user's cognitive work with adaptive intermediaries.

#### `alvarez2026upskilling`
Álvarez, I. (2026). Upskilling UX designers for AI-native work: A pedagogical framework and empirical evaluation. In *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work (CHIWORK '26)* (pp. 1–19). ACM. https://doi.org/10.1145/3808045.3808059
- **Verification:** Crossref record (CHIWORK '26, Linz); OpenAlex abstract.
- **Read status:** abstract only.
- **What it establishes:** A six-module curriculum runs "from foundational AI literacy through structured prompt engineering" to "vibe coding". With n = 21 graduate UX students, students scored "93.4% mean, 58% perfect scores" on an 8-item AI-literacy quiz, but "only 8/21 respondents could be matched across pre/post surveys", so results are "descriptive evidence from a pilot deployment". The paper closes on designers shifting "from designing-for-users to designing-for-agents" (abstract).
- **Role in the DXD argument:** competing construct. The upskilling is toward designers building *with* AI; its closing provocation (designing for agents rather than users) runs opposite to DXD's user-side focus.

#### `longmagerko2020` (existing card)
Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (Paper 598, pp. 1–16). ACM. https://doi.org/10.1145/3313831.3376727
- **Verification:** existing card `submissions/lima_pdw/literature/cards/longmagerko2020.md` (Crossref-verified). Li et al. (2024, read this session) report the framework's counts: "16 core competencies" and "15 recommended design considerations" (Li et al. 2024, related-work section).
- **Read status:** abstract only (per card).
- **What it establishes:** It defines AI literacy as competencies for evaluating, communicating and collaborating with AI, *plus design considerations* for "learner-centered AI" (Consensus abstract). The card's diagnosis is that every competency relates one person to a technology, with no second party.
- **Role in the DXD argument:** competing construct. This is the one widely cited framework that pairs user competencies with designer considerations, the structural shape DXD needs. It is framed for educators and AI developers, not as a profession's expertise.

#### `oeldorfhirsch2025` (existing card)
Oeldorf-Hirsch, A., & Neubaum, G. (2025). What do we know about algorithmic literacy? The status quo and a research agenda for a growing field. *New Media & Society, 27*(2), 681–701. https://doi.org/10.1177/14614448231182662
- **Verification:** existing card `submissions/lima_pdw/literature/cards/oeldorfhirsch2025.md`.
- **Read status:** read in full (per card; SAGE version-of-record re-checked 2026-08-30).
- **What it establishes:** Per the card, the authors screened 96 candidates and reviewed 50 across Google Scholar, CMMC, PsycInfo and the ACM DL. "Algorithmic experience" was one of their seven neighbouring search terms. They find no cohesive construct, and the most comprehensive scale "breaks into two sub-scales that together do not measure algorithmic literacy as one cohesive construct." The first agenda item is to balance user literacy against "developers' responsibility for algorithmic transparency."
- **Role in the DXD argument:** counterevidence (to the professionalization analogy). UX could import a mature science of reading and cognitive load; DXD cannot yet import a settled science of user algorithmic competence.

---

## (c) Thematic synthesis

**The exact term has no scholarly footprint.** I found no scholarly work that uses "decision experience design" in OpenAlex (0 phrase hits), arXiv (0), the Semantic Scholar queries that completed, or six Consensus searches. The phrase survives only in practitioner writing from 2023 to 2026 (G1–G7). Where "decision experience" does appear in research, psychology uses it for the chooser's felt difficulty and satisfaction (Peterson & Cheng 2022). That construct gives DXD a measurable outcome and a precedent for competence moderating the experience, since numeracy buffered the effect of hyperchoice. The practitioner uses mostly point elsewhere, toward organizational decision flow (Audry; Itera's time-to-decision) or conversion (Putri). So DXD inherits a label, not a theory.

**Four near-synonym literatures each claim "the decision" as design's unit, and each assumes a different person at the decision.** Decision-centered design, dated to 1991 (Wolf, Klein & Thordsen), puts the *expert operator* at the centre and elicits requirements through critical-decision interviews (O'Hare et al. 1998; Thordsen et al. 2003; Militello & Klein 2013). It is the strongest precedent for organizing design around decisions, but its users are trained professionals and its systems are tools they command. Choice architecture puts a *benevolent human architect* in charge (Thaler & Sunstein 2008; Johnson et al. 2012). Digital nudging then makes the interface designer that architect (Schneider et al. 2018), and HCI catalogues 23 bias-leveraging mechanisms (Caraban et al. 2019). Decision intelligence puts the *organization* at the centre: in peer review it means process-and-decision modelling (Hasić et al. 2018), and in trade writing a data-to-action discipline (Pratt 2019). The consumer decision journey maps the *firm's* view of a buyer's path, and as of 2021 its own reviewers flagged that AI's effect on that path was untheorized (Santos & Gonçalves 2021). DXD differs from all four on the same axis. Its decision runs through an adaptive intermediary that reads both parties and can commit the outcome, so the designer is no longer the only architect.

**The live disagreement is about whose expertise must grow.** One line holds that designers need *technical* AI knowledge. It runs from ML as a "difficult design material" (Dove et al. 2017) and "adaptive complex" outputs (Yang et al. 2020) to competence lists modelled on the web era's HTML/CSS expectation (Szlachta 2024) and to curricula (Flechtner & Stankowski 2023; Shalamova et al. 2026). A second line reads "AI literacy for designers" as designers using GenAI tools well (Li et al. 2024; Álvarez 2026). Against both stands Yang et al. (2018). Their 13 experienced designers "do not … think learning more about ML would make them better designers." That finding is counterevidence to any DXD claim framed as technical expertise, and support for one framed otherwise. UX designers did not become vision scientists; they became experts in what readers perceive and can hold in working memory.

**Algorithmic experience is the key precursor, and it sits inside the literacy paradigm.** Alvarado's 2017 thesis and the CHI 2018 paper already tie a successor to UX to "decisions and interventions of non-human actors." Their five categories, however, are transparency, awareness, control and memory management, remedies that make the algorithm legible. Shin et al. (2020) operationalize AX as acceptance and satisfaction. Klumbytė et al. (2020) alone target users' algorithmic literacy through critical design. None moves to the three algorithmacy operations of interpreting, specifying intent and keeping track, nor to a second party whose outcome the intermediary also commits. The field's own audit adds a caution: user algorithmic literacy lacks a cohesive construct (Oeldorf-Hirsch & Neubaum 2025), so a DXD profession cannot yet import a settled science the way UX imported cognitive load.

**Closest prior art for the thesis.** Human-AI decision-making research (Lai et al. 2023) is the nearest field joining decision, algorithm and design space. It is a research science of dyadic AI advice, not a design profession, and not a setting in which the system commits.

---

## (d) Gaps and unverified leads

**Gap statements (phrased by source):**
- I found no work that uses "decision experience design" as a scholarly term in OpenAlex, arXiv, Consensus (6 queries), or the 6 of 12 Semantic Scholar queries that completed.
- I found no work that argues designers should become experts in *end users'* competence for interpreting, instructing and monitoring adaptive intermediaries, by analogy with UX expertise in reading, cognitive load and perception. I searched OpenAlex (e.g., `"UX practitioners" AND "AI literacy"`: 0; `"AI literacy" AND ("UX designers" OR …)`: 4), Consensus, arXiv, and OpenAlex snowballs from Alvarado & Waern 2018, Yang et al. 2020 and Dove et al. 2017. The nearest claims concern designers' own technical AI knowledge (Szlachta 2024; Flechtner & Stankowski 2023; Shalamova et al. 2026) or designers' use of AI tools (Li et al. 2024; Álvarez 2026).
- I found no work proposing a *design discipline* organized around decisions committed by algorithmic intermediaries in multi-party coordination, in the same sources. DCD (expert operators, non-adaptive tools), choice architecture (human architect), decision intelligence (organizational modelling) and human-AI decision making (dyadic advice, research science) each cover part of the ground.
- OpenAlex returns 0 hits for `algorithmacy`: the lab's construct has no indexed external uses.

**Coverage gaps in this facet:**
- Semantic Scholar: 6 of 12 searches failed on repeated HTTP 429 (`DX design decision`; `decision intelligence Pratt`; `designers algorithmic literacy`; `UX practitioners AI literacy competence`; `designing for algorithmic experience`; `human-AI interaction design competencies UX designers`). Rerun before submission.
- Scholar Gateway was unreachable (`Could not resolve user identity from CONNECT`), so no full-text-passage search was done. Suggest reconnecting the connector and rerunning.
- The DCD chapters (Thordsen et al. 2003; Militello & Klein 2013) were not accessible. A library copy is needed before DXD characterizes DCD beyond the Wolf 1991 and O'Hare 1998 abstracts.
- ACM DL PDFs (Yang 2018, 2020; Caraban 2019; Shalamova 2026) sit behind Cloudflare. All are gold or bronze OA and readable in a browser; worth a full read of Yang et al. 2018, the key counterevidence.

**Unverified leads (no record retrieved this session; not entries):**
- Court, D., Elzinga, D., Mulder, S., & Vetvik, O. J. (2009). The consumer decision journey. *McKinsey Quarterly* (June 2009). The origin claim is attested secondhand by Santos & Gonçalves 2021; the McKinsey page timed out and returned 0 bytes, and the source is not in OpenAlex.
- Kozyrkov, C., "decision intelligence" (Google, ~2018–2023). Web-search snippets only; the Fast Company article (fastcompany.com/90203073) returned 403. The snippet definition, "turning information into better action at any scale, in any setting", is unverified.
- Gartner "decision intelligence": not searched for a primary document. Szlachta 2024 cites Gartner's hype cycle and an "up to 85%" AI-project failure figure (p. 2/14), both secondhand.
- Weinmann, M., Schneider, C., & vom Brocke, J. (2016). Digital nudging. *Business & Information Systems Engineering, 58*(6), 433–436. The record is verified, but the text was bot-challenged; use it only via the record.

**Leads worth a follow-up entry (records retrieved, not carded here):**
- Mejtoft et al. (2019), *User experience design and digital nudging in a decision making process*, Bled eConference, doi:10.18690/978-961-286-280-0.23. OA at press.um.si; only a truncated abstract was seen.
- Jonassen (2012), *Designing for decision making*, *ETR&D 60*(2), 341–359, doi:10.1007/s11423-011-9230-5. Instructional design; record only.
- Sundar (2019 per OpenAlex), "Rise of machine agency: A framework for studying the psychology of human–AI interaction (HAII)", *JCMC*, doi:10.1093/jcmc/zmz026. The top-cited citer of Alvarado & Waern and a candidate cognitive-foundation source for F-facets on algorithmacy cognition.
- Olsson & Väänänen (2021), "How does AI challenge design practice?", *Interactions 28*(4), 62–64, doi:10.1145/3467479. OpenAlex holds only forum boilerplate as its abstract.
- Steyvers & Kumar (2023), "Three challenges for AI-assisted decision-making", *Perspectives on Psychological Science*, doi:10.1177/17456916231181102. It names human mental models of AI and cognitive overload as design variables, which bears directly on the "cognitive issues" half of the thesis.
- Yeung (2017), "Hypernudge", existing card `submissions/hospitality_phygital/library/cards/yeung2017hypernudge.md`. It supplies the "adaptive choice architect" point that separates DXD from choice architecture, so cross-reference it from F1's synthesis.
