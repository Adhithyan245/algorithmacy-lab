# Search log — Decision Experience Design review

Merged 2026-09-30 from the seven facet files (`literature/facets/F*.md`). Each facet agent logged its own
queries; F7 and the Substack-essay verification were run by the lead session. Counts are as each tool
reported them on the day.

**Tool failures to rerun before submission:** Scholar Gateway failed in every facet ("Could not resolve
user identity from CONNECT"); Semantic Scholar rate-limited (HTTP 429) repeatedly — F1 lost 6 of 12
queries. The gap check therefore rests on OpenAlex, Crossref, arXiv and Consensus.

## Lead session (Substack essay verification and F7)

| Date | Source | Query | Result |
| --- | --- | --- | --- |
| 2026-09-30 | OpenAlex | `search="decision experience design"` | 0 |
| 2026-09-30 | OpenAlex | `filter=title_and_abstract.search:"decision experience design"` | 0 |
| 2026-09-30 | Semantic Scholar | `query="decision experience design"` | HTTP 429 (twice) |
| 2026-09-30 | Web (direct fetch) | the seven practitioner URLs in F1 cluster G | 5 fetched; 2 Medium posts via RSS |

## F1_term_and_gap — F1 — The term, its near-synonyms, and the novelty gap check

All searches were run on 2026-09-30. "Total" is the count the source reported. Semantic Scholar's `/paper/search` ranks by relevance and does not honour quotation marks, so its totals measure the index, not phrase hits; I inspected the top 8–20 results by hand. OpenAlex `title_and_abstract.search` honours quoted phrases but stems words, so its counts over-include loosely related work.

#### Repository card libraries (grep, worktree)

| Source | Query | Result |
|---|---|---|
| repo grep (`submissions/*/literature`, `submissions/*/library`, `org_frontier/research/*/literature`) | `decision experience` | 0 files |
| repo grep | `decision-centered` / `decision centered` / `decision intelligence` / `decision journey` / `Kozyrkov` | 0 files each |
| repo grep | `choice architecture` | 3 files (`algorithmacy_design_ethics/literature/library/thaler2008.md`; `hospitality_phygital/library/cards/yeung2017hypernudge.md`; one LIBRARY index) |
| repo grep | `algorithmic experience` / `Alvarado` | 3 files each (`lima_pdw/literature/cards/shin2022.md`, `oeldorfhirsch2025.md`; unrelated survey card) |
| repo grep | `Magerko` | 30 files (incl. `lima_pdw/literature/cards/longmagerko2020.md`) |
| repo grep | `algorithmic literacy` / `AI literacy` | 70 / 59 files |
| repo grep | `Klein, G` | 3 files (`algorithmacy_design_ethics/literature/library/klein2004.md`) |

#### Semantic Scholar (`api.semanticscholar.org/graph/v1/paper/search`, limit 20)

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

#### OpenAlex (`api.openalex.org/works`, `filter=title_and_abstract.search:`, sorted by citations)

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

#### OpenAlex snowball (citing works and references)

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

#### arXiv (`export.arxiv.org/api/query`)

| Query | Total | Notes |
|---|---|---|
| `all:"decision experience design"` | **0** | |
| `all:"decision experience" AND all:design` | 17 | None relevant (agent memory, RL). |
| `all:"algorithmic experience"` | 325 | Top 8 are algorithm-performance papers; no AX-design hit in top 8. |
| `all:"decision intelligence"` | 37 | IoT/power systems/enterprise AI. |
| `all:"decision-centered design"` | **0** | |
| `all:"AI literacy" AND all:designers` | 154 | Top 8 education-focused. |
| `all:"algorithmic literacy" AND all:designers` | 5 | "Designing for Critical Algorithmic Literacies" (arXiv 2008.01719, 2020); end-user audit tools. |

#### Consensus (`mcp__claude_ai_Consensus__search`, 6 calls)

| Query | Shown | Notes |
|---|---|---|
| `decision experience design as a design discipline` | 20 | No work uses the term. Returned experience-design and design-decision work (Trischler 2021; Suri 2003; Mortati 2022). |
| `UX designers need competence in algorithmic literacy or AI literacy to design human-algorithm interaction` | 19 | Long & Magerko 2020; Szlachta 2024; Yang 2020; Liao 2023; Muralikumar 2024; Feng 2023; Shalamova 2026. |
| `algorithmic experience design framework beyond user experience` | 20 | Shin 2020; Alvarado & Waern 2018; Klumbytė 2020; Alvarado 2019; Verganti 2020; Baumer 2017. |
| `choice architecture as a design discipline for user interface designers digital nudging` | 20 | Mertens 2021 meta-analysis; Schneider et al. (preprint record); Caraban 2019; da Cunha 2020 ("software designers as choice architects"). |
| `Beyond nudges: tools of a choice architecture Johnson` | 20 | Johnson et al. 2012 abstract. |
| `decision intelligence as a discipline definition human decision making and AI` | 20 | O'Callaghan 2023 (CRC book); Lai et al. 2023; Steyvers & Kumar 2023; Shrestha 2019. |

#### Scholar Gateway

| Query | Result |
|---|---|
| "Should user experience designers become experts in how users interpret, instruct and monitor opaque adaptive algorithms…" | **Error:** `INVALID_QUERY: Could not resolve user identity from CONNECT`. Scholar Gateway could not be reached; the connector may need reconnecting. |
| "decision-centered design in cognitive systems engineering…" | Same error. |

#### Crossref, Unpaywall, and web

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

## F2_choice_architecture — F2 — The decision-science and choice-architecture lineage

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

## F3_decision_support_cse — F3 — Decision support systems and cognitive systems engineering

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

## F4_ux_cognitive_foundations — F4 — The cognitive foundations of UX/HCI (left-hand side of the DXD analogy)

All searches ran on 2026-09-30. "Total" is the count the source reported. Crossref `query.bibliographic` totals count loose matches, so they measure recall, not relevance; in every row the top hit was the target record unless noted.

| # | Source | Exact query / call | Results |
|---|---|---|---|
| 1 | Repo grep | `grep -ril` for Fitts, Hick, Hyman, "Card, S", Moran, GOMS, Norman, Hutchins, Sweller, "Miller, G", Cowan, Buscher, Dyson, "Ware, C", Treisman, Healey, MacLean, Hollan, Grudin, Harrison, 9241, Nielsen, Kirsh, Draper, "cognitive load" over `submissions/*/literature submissions/*/library org_frontier/research/*/literature` | Relevant hits only: `algorithmacy_design_ethics/literature/library/norman1990.md` (full text, S2-verified), `hutchins1995.md` (secondary), `christoffersenwoods2002.md`. No cards for Fitts, Card/Moran/Newell, Sweller, Miller, Cowan, Grudin, Harrison, Hollan 2000, Buscher, Dyson, Healey, MacLean, ISO 9241 |
| 2 | Repo grep | `binns\|3557891\|Chignell` | `coordinative_sovereignty/.../binns2021that.md` (different Binns paper); no Chignell card |
| 3 | Crossref | `Fitts 1954 The information capacity of the human motor system…` | 654,440; top = 10.1037/h0055392 |
| 4 | Crossref | `Hick 1952 On the rate of gain of information…` | 7,168,927; top = 10.1080/17470215208416600 |
| 5 | Crossref | `Hyman 1953 Stimulus information as a determinant of reaction time…` | 8,252,741; top = 10.1037/h0056940 |
| 6 | Crossref | `Card Moran Newell 1980 The keystroke-level model…` | 1,216,313; top = 10.1145/358886.358895 |
| 7 | Crossref | `Card Moran Newell 1983 The Psychology of Human-Computer Interaction` | 8,163,765; top = 10.1201/9780203736166 (2018 CRC reissue) + chapter DOIs |
| 8 | Crossref | `Hutchins Hollan Norman 1985 Direct manipulation interfaces…` | 243,001; top = 10.1207/s15327051hci0104_2 |
| 9 | Crossref | `Sweller 1988 Cognitive load during problem solving…` | 1,612,655; top = 10.1207/s15516709cog1202_4 |
| 10 | Crossref | `Sweller van Merrienboer Paas 1998 …` / `… 2019 … 20 years later` | 847,014 / 630,745; tops = 10.1023/a:1022193728205, 10.1007/s10648-019-09465-5 |
| 11 | Crossref | `Miller 1956 The magical number seven…` | 220,209; top = 10.1037/h0043158 |
| 12 | Crossref | `Cowan 2001 The magical number 4…` | 458,521; top = 10.1017/s0140525x01003922 |
| 13 | Crossref | `Buscher Cutrell Morris 2009 What do you see when you're surfing?…` | 20,872; top = 10.1145/1518701.1518705 |
| 14 | Crossref | `Dyson 2004 How physical text layout affects reading from screen…` | 1,520,331; top = 10.1080/01449290410001715714 |
| 15 | Crossref | `Treisman Gelade 1980 A feature-integration theory of attention…` | 5,477,158; top = 10.1016/0010-0285(80)90005-5 |
| 16 | Crossref | `Healey Enns 2012 Attention and visual memory…` | 651,706; top = 10.1109/tvcg.2011.127 |
| 17 | Crossref | `MacLean 2008 Haptic interaction design for everyday interfaces…` | 515,014; top = 10.1518/155723408x342826 |
| 18 | Crossref | `Hollan Hutchins Kirsh 2000 Distributed cognition…` | 1,361,748; top = 10.1145/353485.353487 |
| 19 | Crossref | `Grudin 2012 A moving target…` / `Grudin 2017 From tool to partner…` | 11,621,192 / 21,424,920; found 10.1201/b11963-ch-101 (2012 Handbook intro), 10.1201/9781410615862.ch0 (2007), 10.1007/978-3-031-02218-0 (2017 book) |
| 20 | Crossref | `Harrison Tatar Sengers 2007 The three paradigms of HCI` | 4,419,568; target **not** indexed (alt.chi, no DOI); found 2011 successor 10.1016/j.intcom.2011.03.005 |
| 21 | Crossref | `Norman Draper 1986 User Centered System Design…` | 1,372,047; top = 10.1201/b15703 |
| 22 | Crossref | `Norman 1988 The Psychology of Everyday Things` / `Norman 2013 The Design of Everyday Things…` | 2,662,039 / 7,928,137; only reviews and a 2016 German edition (10.15358/9783800648108) |
| 23 | Crossref | `Fitts 1951 Human engineering for an effective air-navigation and traffic-control system` | 1,205,263; target **not** indexed |
| 24 | Crossref | `MacKenzie 1992 Fitts' law as a research and design tool…` | 1,281,528; top = 10.1207/s15327051hci0701_3 |
| 25 | Crossref | `Ware Information Visualization: Perception for Design` | 5,698,123; chapters only (10.1016/b978-0-12-381464-7.00007-7 etc.) |
| 26 | Crossref | `Norman 1999 Affordance, conventions, and design interactions` | 5,080,658; top = 10.1145/301153.301168 |
| 27 | Crossref | `John Kieras 1996 The GOMS family…` | 379,451; top = 10.1145/235833.236054 |
| 28 | Crossref (batch 2) | de Winter & Dodou; Dekker & Woods 2002; Cowan 2015; Hollender 2010; Oviatt 2006; Grudin 2005; Bannon 1991; Rogers 2004; Rogers 2012; Carroll 1997; Gray et al. 2014; Norman 2010; Hassenzahl & Tractinsky 2006; Newell & Card 1985; Carroll & Campbell 1986; Bødker 2006; Bødker 2015; Gibson 1979; Nielsen 2006 F-pattern; Pernice 2017; Shneiderman 1983 | 21 queries; all targets found except the two NN/g web articles (grey, not in Crossref) |
| 29 | Crossref | `Norman 1986 Cognitive engineering User Centered System Design` | 13,021,444; top = 10.1201/b15703-3 (pp. 31–62) |
| 30 | Crossref | `Gould Lewis 1985 Designing for usability…` | 107,465; top = 10.1145/3166.3170 |
| 31 | OpenAlex | `search=` for Harrison/Tatar/Sengers; Norman cognitive engineering; Fitts 1951; Psychology of Everyday Things; ISO 9241-210 | 334 / 5,962 / 280 / 17,177 / 3,958; none returned the target except via de Winter & Dodou (Fitts 1951) |
| 32 | OpenAlex | `filter=title_and_abstract.search:UX practitioners competencies cognitive psychology` | **0** |
| 33 | OpenAlex | `filter=title_and_abstract.search:usability professionals knowledge skills competencies` | 18,869 (off-topic top hits) |
| 34 | OpenAlex | `filter=title.search:design of everyday things` / `…psychology of everyday things` | 43 / 14; W2613049552 (2013 rev. ed.), W139507382 (1988) |
| 35 | OpenAlex | 40 `works/doi:` lookups for OA status, abstracts and citation counts | all resolved except 10.1145/800045.801579 (404) |
| 36 | OpenAlex snowball | `filter=cites:W2158035776` (Grudin 1990), `cites:W2016540947` (Hollan 2000), `cites:W1976080514` (de Winter & Dodou), each × `title_and_abstract.search:` {algorithm, artificial intelligence, decision} | citing totals 336 / 2,259 / 156; term-filtered n = 17/9/13, 113/125/228, 17/23/42 |
| 37 | Semantic Scholar | `POST /graph/v1/paper/batch` for 20 DOIs (abstract, openAccessPdf) | 17 of 20 resolved; first attempt succeeded, no rate limiting |
| 38 | Unpaywall | 18 DOIs | OA locations found for de Winter & Dodou, Sweller 2019, KLM, Grudin 1990, Commarford, Bødker 2015, Lallemand |
| 39 | Europe PMC | `DOI:10.1037/a0039035` | 1 (PMC4486516); fullTextXML endpoint returned HTTP 500, so I read the PMC HTML instead |
| 40 | Consensus | `UX practitioners competencies knowledge of cognitive psychology human factors in industry job skills` | 20 |
| 41 | Consensus | `history of human-computer interaction paradigms human factors to cognitive science to situated` | 20 |
| 42 | Consensus | `misuse of Miller's magical number seven in user interface menu design guidelines` | 20 |
| 43 | Consensus | `integrating cognitive load theory into human-computer interaction interface design extraneous load usability` | 20 |
| 44 | Consensus | `eye tracking web page reading scanning patterns users visual attention layout` | 20 |
| 45 | Scholar Gateway | `How do people read web pages and screens? Eye-tracking studies…` | **Failed**: "INVALID_QUERY: Could not resolve user identity from CONNECT". I did not retry and used Consensus (row 44) instead |
| 46 | WebSearch | `"The three paradigms of HCI" Harrison Tatar Sengers pdf alt.chi 2007` | 9 links; CiteSeerX copy retrieved |
| 47 | WebSearch | `Hollan Hutchins Kirsh "Distributed cognition: toward a new foundation…" pdf ucsd` | 9 links; author copy hci.ucsd.edu retrieved |
| 48 | WebSearch | `Grudin "The computer reaches out…" pdf` | 10 links; DAIMI PB-299 copy (tidsskrift.dk) retrieved and OCR'd |
| 49 | WebSearch | `Card Moran Newell 1980 "keystroke-level model…" pdf` | 10 links; none accessible (ACM DL behind a Cloudflare challenge; CACM page 403) |
| 50 | WebSearch | `Hutchins Hollan Norman "Direct manipulation interfaces" 1985 pdf "gulf of execution"` | 10 links; I used the author-hosted copy (hci.ucsd.edu/hollan/Pubs/direct-manip.pdf), not the course copies |
| 51 | WebSearch | Buscher/Cutrell/Morris pdf; Healey & Enns pdf; ISO 9241-210:2019; Norman 1999 affordance | 10 / 10 / 9 / 10 links; no author PDFs retrieved for Buscher or Healey |
| 52 | WebFetch | nngroup.com F-shaped pattern article; iso.org/standard/77520; jnd.org affordances; Springer article pages; PMC4486516 | NN/g and PMC read; ISO 403; jnd.org 404; Springer redirected to login (copy then retrieved from TU Delft repository) |
| 53 | Browser (Chrome) | cacm.acm.org KLM page; dl.acm.org/doi/10.1145/358886.358895 | CACM page had metadata only; dl.acm.org unreadable (extension permission denied) |

---

## F5_human_algorithm_cognition — F5 — The cognitive science of deciding with and through algorithms

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

## F6_literacy_to_algorithmacy — F6 — From literacy to algorithmacy: the lab's construct, its lineage, and the competing competence constructs

All searches 2026-09-30.

| # | Source | Exact query / call | Results |
|---|---|---|---|
| 1 | Repo grep | `grep -ril` over `submissions/*/literature`, `submissions/*/library`, `org_frontier/research/*/literature` for: wilkinson, Ong, Goody, New London, multiliterac, numeracy, Dogruel, Oeldorf, Gran Booth, Long & Magerko, Ng et al, Hargittai, Klawitter, data literacy, Chalmers, seamful, Alfrink, Karahalios, Alvarado, boosting/Hertwig, Aneesh, algorithmic awareness, Laupichler, Zhou, DigComp, Iyamu, Danaher | hits in 3–6 files each; "New London" 0; Alvarado 0 relevant; Hertwig 1 (incidental) |
| 2 | Repo grep | `"opaque, adaptive intermediary"`; `"eight candidate"`; `"specify intent through it"` | 20+; 8; 6 (definition located in `lima_pdw/manuscript/INTRODUCTION.md`) |
| 3 | Consensus | `designing interfaces that increase users' algorithmic awareness or algorithmic literacy intervention experiment` | 20 |
| 4 | Consensus | `algorithmic experience user experience design beyond usability` | 20 |
| 5 | Consensus | `boosting competences versus nudging online environments` | 20 |
| 6 | Scholar Gateway | `How do literacy scholars argue that AI or algorithmic literacy should be understood as an extension of multiliteracies or new literacies rather than a distinct competence?` | failed: "INVALID_QUERY: Could not resolve user identity from CONNECT" |
| 7 | Scholar Gateway | `Interface design features that help users learn how an algorithmic system works and build their competence over time, such as seamful design or algorithm-aware design` | failed (same error); tool not retried |
| 8 | Crossref `/works/{doi}` | 15 DOIs: New London Group 1996; Alvarado & Waern 2018; Shin et al. 2020; Hertwig & Grüne-Yanoff 2017; Lorenz-Spreen et al. 2020; Kozyreva et al. 2020; Gagrčin et al.; Fouquaert & Mechant; Silva et al. 2022; Swart 2021; Eslami 2017; Siles et al. 2022; Cheng et al. 2019; Moon et al. 2025; Herzog & Hertwig 2025 | 15/15 resolved |
| 9 | OpenAlex `/works/doi:` | OA status for 10 of the above | 5 OA (green/bronze/hybrid/gold), 5 closed |
| 10 | arXiv API | `search_query=ti:"promote truth autonomy"` | 0 |
| 11 | Europe PMC | `DOI:"…"` for Kozyreva 2020, Hertwig 2017, Swart 2021, Gagrčin | 1 PMC full text (PMC7745618) |
| 12 | Semantic Scholar `/paper/DOI:` | Alvarado & Waern 2018; New London Group 1996; Hertwig & Grüne-Yanoff 2017; Shin et al. 2020 | 4/4 resolved (no rate-limit failures); only Hertwig has an OA link |
| 13 | OpenAlex | `filter=title_and_abstract.search:seamful AND (algorithm OR algorithmic)` | 17 |
| 14 | OpenAlex | `filter=title_and_abstract.search:"algorithmic competence" OR "algorithmic skills"` | 306 (mostly off-topic; Hargittai et al. 2020 the only relevant top hit) |
| 15 | OpenAlex | `search=numeracy and decision making`, `filter=publication_year:2006` | 478 |
| 16 | OpenAlex | `filter=title.search:digital literacy conceptual framework` | 36 |
| 17 | Crossref | Peters et al. 2006; Ha & Kim 2024; Becker et al. 2022; Petrovčič et al. 2024 (DOI lookups) | 4/4 |
| 18 | OpenAlex snowball | `filter=cites:W2795636034` (Alvarado & Waern) `,title_and_abstract.search:literacy OR competence` | 12 |
| 19 | OpenAlex snowball | `filter=cites:W4382796112` (Oeldorf-Hirsch & Neubaum) `,title_and_abstract.search:design OR intervention` | 19 |
| 20 | OpenAlex snowball | `filter=cites:W2743157434` (Hertwig & Grüne-Yanoff) `,title_and_abstract.search:algorithm OR algorithmic` | 34 |
| 21 | Full-text fetch | nature.com PDF (Lorenz-Spreen) → paywall preview; SAGE PDF (Gagrčin) → blocked; MPG PuRe (Hertwig) → bot challenge, not attempted; UGent biblio (Fouquaert AAM) → retrieved; Europe PMC XML (Kozyreva) → retrieved; Springer PDF (Becker) → HTML, not retrieved | 2 read |
| 22 | Crossref `/works/{doi}` | author-name check for all 29 DOI entries in the `.bib` (two retries after HTTP 429) | 29/29; corrected Zhou et al. (2025) given names |

Snowballing (rule 7) ran on the three most central external hits for the design-for-competence question:
Alvarado & Waern (2018), Oeldorf-Hirsch & Neubaum (2025), and Hertwig & Grüne-Yanoff (2017) (rows 18–20). The
reference list of Oeldorf-Hirsch & Neubaum is already covered by its full-text card.

---

## F7_numeracy_framing — F7 — The numeracy framing (addendum, 2026-09-30)

| Date | Source | Query | Count / result |
| --- | --- | --- | --- |
| 2026-09-30 | OpenAlex | `doi:10.1111/j.1467-9280.2006.01720.x` (OA status) | closed; no repository full text |
| 2026-09-30 | Unpaywall | same DOI | `is_oa: false` |
| 2026-09-30 | OpenAlex | `filter=title_and_abstract.search:numeracy decision,is_oa:true,type:review` sorted by citations | 8 shown; Reyna & Brainerd 2023 selected |
| 2026-09-30 | Europe PMC | `DOI:10.1038/s44159-023-00188-7` | PMC10196318, open access; full-text XML read |
| 2026-09-30 | Crossref + OpenAlex | `10.1016/j.intell.2020.101452` (snowballed from Reyna & Brainerd ref. 113) | record + abstract; OA hybrid |
