# Citation audit, batch 00 (30 keys)

Auditor: Claude (auditing-citations skill), 2026-09-30. Each entry was checked by hand against an external record
and, where a quote, number or specific claim is attached, against the source text. Line numbers refer to
`REVIEW.md` as of this audit. "Refs" = the generated References list in REVIEW.md.

Retraction check: for every entry carrying a quote or number I queried Crossref for notices that update the DOI
(`https://api.crossref.org/works?filter=updates:<DOI>`; this filter includes Retraction Watch data and was
validated against a known retracted DOI, which returned its correction and retraction). All 24 DOIs returned
no notices. The Crossref work records also carry no `update-to` field.

Status counts: **Verified 29 · Mismatch 1 · Not found 0 · Unreachable 0.**

| key | metadata status | what you checked (record URL) | claim check (each quote/number: OK / problem + source locator) | action needed |
|---|---|---|---|---|
| alfrink2023contestable | Verified (online 2022-08-13; vol. 33(4) 2023, 613–639) | https://api.crossref.org/works/10.1007/s11023-022-09611-z ; OpenAlex abstract | l. 599 "five system features and six development practices": OK per repo card `algorithmacy_design_ethics/literature/library/alfrink2023.md` §6 (S3 browser-verified) and the authors' own later summary ("framework comprises five system features and six development practices", Alfrink et al., arXiv 2302.04603). Springer PDF blocked to curl. l. 602–603 "All three also model one user and one system": **problem**. The card records an actor model of "developers, human controllers, decision subjects and third parties" | Reword l. 602–603 (see Problems #2) |
| allen2022algorithm | Verified | https://api.crossref.org/works/10.1287/orsc.2021.1554 | l. 256–258 inverted U among IT support staff: OK (LSE AAM, ms p. 3: "only workers with moderate levels of domain experience perform significantly better…"). "about 90%" correct: OK (AAM: "about 90% of top recommendations were correct"). Read myself: researchonline.lse.ac.uk/id/eprint/128784 | None |
| alvarado2017towards | Verified (DiVA: student thesis, Uppsala Univ., 2017, 94 pp.) | https://uu.diva-portal.org/smash/record.jsf?pid=diva2:1110570 ; full PDF read | l. 110–111 quote "should be opened to all kinds of technologies … that affect the user experience through the decisions and interventions of non-human actors" (p. 10): OK verbatim; the ellipsis replaces "(now and in the future)"; page 10 confirmed from the PDF's page footer | Refs entry omits the thesis type and institution that the .bib holds (Problems #10) |
| alvarado2018towards | Verified (Crossref title "Towards Algorithmic Experience" + subtitle "Initial Efforts for Social Media Contexts") | https://api.crossref.org/works/10.1145/3173574.3173860 ; OpenAlex abstract | l. 111–113 "five functional categories: profiling transparency and management, algorithmic awareness and control, and selective algorithmic memory": OK against the abstract. l. 601: OK | None |
| alvarez2026upskilling | Verified (Crossref "Alvarez, Ignacio"; OpenAlex profile "Ignacio Álvarez") | https://api.crossref.org/works/10.1145/3808045.3808059 ; OpenAlex abstract | l. 586–587 reading "AI literacy for designers" as skill with generative tools: the characterization is OK (abstract: curriculum "from foundational AI literacy through structured prompt engineering" to vibe coding). **Problem:** the quotation marks make "AI literacy for designers" look like a quote from Li et al. or Alvarez. The phrase is in neither Alvarez's abstract nor Li et al.'s title; it is the F1 facet's own gloss (F1 l. 328, 366). l. 620: OK | Remove the quotation marks (Problems #6) |
| amershi2019guidelines | Verified (13 authors, order matches) | https://api.crossref.org/works/10.1145/3290605.3300233 ; MSR camera-ready PDF read | l. 417–419 "eighteen guidelines": OK ("the 18 guidelines", §1 contributions). "update and adapt cautiously" (G14) and "notify users about changes" (G18): OK verbatim, Table 1, p. 3. l. 649 G18: OK | None |
| aneesh2009global | Verified | https://api.crossref.org/works/10.1111/j.1467-9558.2009.01352.x ; OpenAlex abstract | l. 445–446 algocracy as a mode of organization set beside bureaucracy and the market: OK (abstract: "bureaucracy (legal-rational), the market (price), and algocracy (programming or algorithm)"). **Problem:** "which Aneesh (2009) coined" is contradicted by the repo card `lima_pdw/literature/cards/aneesh2009.md` (Caution: the term appears in Aneesh's 2006 *Virtual Migration*; "Do not describe Aneesh as having coined the bare word"). The Lima manuscript itself says "uses" (F6 l. 49) | Change "coined" (Problems #1) |
| arnott2005critical | Verified | https://api.crossref.org/works/10.1057/palgrave.jit.2000035 | l. 203 "reviewed the field's research in 2005": OK against the record and abstract (1,020 DSS articles, 1990–2003; F3 entry 3) | None |
| arnott2014critical | Verified | https://api.crossref.org/works/10.1057/jit.2014.16 | l. 203 "and again in 2014": OK (abstract: sample extended to 2010, 1,466 articles; F3 entry 4) | None |
| audryNDdx | Verified (grey; page refetched 2026-09-30; `<title>` "Decision Experience Design — Andrew Audry"; no publication date in the HTML; the only timestamp in the page is the LinkedIn widget's `addedOn`, 2022-08-31, which dates the site's social link, not the page) | https://www.andrewaudry.com/dxdesign | l. 85–86 quote "the logic and structure that makes internal choices system-ready": OK verbatim ("Decision Experience Design creates the logic and structure that makes internal choices system-ready"). **Minor:** l. 30–32 places this undated page inside "between September 2023 and September 2026" | Qualify the date range (Problems #8); optionally add a retrieval date to the Refs entry |
| bainbridge1983ironies | Verified (Crossref title case "Ironies of automation") | https://api.crossref.org/works/10.1016/0005-1098(83)90046-8 ; OA copy read (ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf) | l. 237 "develops only through use and feedback about its effectiveness" (p. 775): OK. l. 246–247 "the human monitor has been given an impossible task" (p. 776): OK. l. 248–249 "using methods and criteria, and at a rate, which the operator can follow, even when this may not be the most efficient method technically" (p. 777): OK. "fail obviously" (p. 777): OK. l. 571–572 (p. 777): OK. I matched the wording in the OA copy myself; page numbers follow the repo card's S2 pass, which checked the paginated Pergamon PDF | None |
| banker2019algorithm | Verified (online 2019-07; print 38(4) 2019) | https://api.crossref.org/works/10.1177/0743915619858057 ; OpenAlex abstract | l. 258–259 "even when the recommendations are inferior": OK verbatim (abstract) | None |
| bansal2019beyond | Verified (Crossref gives no issue; OJS is v7i1, so number = 1 is fine) | https://api.crossref.org/works/10.1609/hcomp.v7i1.5285 ; OJS full text read | l. 361–363 "when does the AI err?": OK (§1: knowing "When does the AI err?"). Parsimonious boundary learnable: OK. Learning from the consequences of their own decisions: OK (S4 reward feedback "lets the human learn when to trust"). **Problem:** "stochasticity makes it hard to learn at all" overstates. Source: "increased stochasticity makes it difficult for participants to trust Marvin and learn a correct mental model" (Results) | Soften (Problems #4) |
| bansal2019updates | Verified | https://api.crossref.org/works/10.1609/aaai.v33i01.33012429 ; OJS full text read | l. 410–411 quote "a more accurate but incompatible classifier results in lower team performance than a less accurate but compatible classifier" (p. 2434): OK verbatim, printed p. 2434. l. 572–573: OK. **Problem:** l. 648 "Bansal and colleagues (2019)" is ambiguous between the two 2019 Bansal papers, which share all six authors | Disambiguate (Problems #5) |
| bansal2021whole | Verified; **incomplete**: Crossref and the ACM reference format give pp. 1–16 (16 pages); the .bib and Refs have no pages | https://api.crossref.org/works/10.1145/3411764.3445717 ; arXiv 2006.14779v3 read | l. 372–373 "increased the chance that humans will accept the AI's recommendation, regardless of its correctness": OK verbatim (abstract). l. 373–374 "no explanation condition beat simply showing the AI's confidence": OK ("none of the explanation conditions produced an accuracy significantly higher than the simple baseline of showing the AI's confidence") | Add pages (Problems #9) |
| bucher2017algorithmic | Verified (online 2016; print 20(1) 2017) | https://api.crossref.org/works/10.1080/1369118X.2016.1154086 ; OpenAlex abstract | l. 360–361 "algorithmic imaginary" feeding back into the system: OK (abstract: it "plays a generative role in moulding the Facebook algorithm itself") | None |
| bucinca2021trust | Verified (article 188, 21 pp., confirmed from the preprint's ACM footer "4-ART188") | https://api.crossref.org/works/10.1145/3449287 ; arXiv 2102.09692 read | l. 393–397 three forcing functions (on demand; update, i.e. after one's own decision; wait 30 s): OK (§3.2.2). Reduced overreliance more than simple explainable-AI designs: OK (abstract). Participants liked the most effective designs least: OK (abstract: "least favorable subjective ratings to the designs that reduced the overreliance the most") | None |
| buscher2009what | Verified (Crossref title + subtitle) | https://api.crossref.org/works/10.1145/1518701.1518705 ; OpenAlex abstract | l. 273–274 "20 users across 361 web pages": OK (abstract). "to predict salient regions": OK (subtitle; the abstract's predictive model) | None |
| callaway2022leveraging | Verified | https://api.crossref.org/works/10.1073/pnas.2117432119 ; OpenAlex abstract | l. 188 "transferred to a more challenging task and were retained over time": OK verbatim (abstract) | None |
| card1980keystroke | Verified | https://api.crossref.org/works/10.1145/358886.358895 | l. 269–270 keystroke-level model: OK against the title. Support: record only; the text was not read (F4) | None |
| card1983psychology | Verified: 1983 Erlbaum edition in Open Library (L. Erlbaum Associates, Hillsdale, N.J., 1983, ISBN 0898592437, LCCN 82021045); DOI is the CRC 2018 reissue | https://openlibrary.org/books/OL3500789M.json ; https://api.crossref.org/works/10.1201/9780203736166 | l. 269–271 Model Human Processor: support is the Crossref chapter records only ("The Human Information-Processor", pp. 23–97) plus Harrison et al.'s secondary description; the text was not read (disclosed at l. 667–668) | Optional: note the reissue or drop the DOI (Problems #11) |
| carsten2018how | **Mismatch (internal)**: record = online 2018-05-12, print 21(1) 2019-02; .bib and Refs = 2019; **in-text l. 254–255 = "Carsten and Martens (2018)"** | https://api.crossref.org/works/10.1007/s10111-018-0484-0 ; OpenAlex abstract | l. 254–255 "applied cognitive-engineering principles to drivers of automated cars": broadly OK. The abstract calls them "design principles for in-vehicle HMI"; "cognitive-engineering" is the F3 facet's gloss (abstract only) | Fix the in-text year (Problems #3); optional wording (Problems #12) |
| chalmersgalani2004seamful | Verified (Crossref venue: "Proceedings of the 5th conference on Designing interactive systems: processes, practices, methods, and techniques"; .bib shortens it, acceptable) | https://api.crossref.org/works/10.1145/1013115.1013149 ; repo card `algorithmacy_design_ethics/literature/library/chalmersgalani2004.md` (full text) | l. 597–598 seamful design "exposes the joins in a system so people can accommodate them": OK (card: "People accommodate and take advantage of seams"). **Problem:** l. 602–603 "All three also model one user and one system" is contradicted. The card records three co-visitors coordinating through heterogeneous media, with seams handled socially over a shared audio channel ("Parties modeled: … several co-present/remote humans") | Reword (Problems #2) |
| chandrashekar2023defaults | Verified (Meta-Psychology vol. 7, MP.2022.3108) | https://api.crossref.org/works/10.15626/MP.2022.3108 ; OA PDF read | l. 160–161 62.5% opt-in vs 73.5% opt-out: OK (Results, Part 1; Table 5: opt-in n = 488, 62.5%; opt-out n = 476, 73.5%). Original 42% vs 82%: OK (Introduction, p. 3: "to donate (82%) than when the default option was to not donate (42%)") | None |
| cheng2019explaining | Verified | https://api.crossref.org/works/10.1145/3290605.3300789 ; OpenAlex abstract | l. 531–532 "not affected by the explanation interface or their level of comprehension": OK verbatim (abstract; the source continues "…of the algorithm"). Improved comprehension of an admissions algorithm: OK | None |
| chernev2015choice | Verified (online 2014; print 25(2) 2015) | https://api.crossref.org/works/10.1016/j.jcps.2014.08.002 ; OpenAlex abstract | l. 157–159 the four factors: OK (complexity, difficulty, preference uncertainty, effort-minimizing goal). **Minor overstatement:** "recovered it only under four conditions". The abstract reports four moderators that "facilitate choice overload" at higher levels, and a significant overall effect once moderators are taken into account; it does not say the effect appears only under them. l. 656–657 regret, deferral, switching: OK (abstract lists them as measures) | Soften (Problems #7) |
| chignell2023evolution | Verified (Crossref "Li, Jamy"; OpenAlex profile "Jamy J. Li") | https://api.crossref.org/works/10.1145/3557891 ; OpenAlex abstract | l. 324–325 AI calls for HCI to rejoin human factors under human augmentation: OK (abstract) | None |
| commarford2008comparison | Verified | https://api.crossref.org/works/10.1518/001872008x250665 ; OpenAlex abstract | l. 307–309 a Miller-derived five-or-fewer guideline made performance worse, most of all for low working-memory users: OK (abstract: broad-structure users "performed better"; "effect was more pronounced for those with low working memory capacity") | None |
| cotter2019playing | Verified (online 2018; print 21(4) 2019) | https://api.crossref.org/works/10.1177/1461444818815684 ; OpenAlex abstract | l. 400–401 "game constructed around 'rules' encoded in algorithms": OK verbatim (abstract) | None |
| cowan2001magical | Verified (target article pp. 87–114) | https://api.crossref.org/works/10.1017/s0140525x01003922 ; Cambridge OA PDF read | l. 305 working-memory limit of three to five: OK ("a mean memory capacity in adults of three to five chunks", §5 Conclusion). The "over-generalized" quotation in the same sentence comes from Cowan 2015 (F4; not in this batch), and the sentence cites both | None for this key |

## Problems found (proposed fixes; nothing has been changed)

1. **aneesh2009global, l. 445.** Old: "The term is not *algocracy*, which Aneesh (2009) coined for a mode of
   organization". New: "The term is not *algocracy*, which Aneesh (2009) uses for a mode of organization".
   Source: the repo card `submissions/lima_pdw/literature/cards/aneesh2009.md` (Caution: the term predates 2009,
   in *Virtual Migration*, 2006, and an earlier informal use exists; "do not describe Aneesh as having coined the
   bare word"). The Lima manuscript itself uses "uses" (F6 l. 49).

2. **chalmersgalani2004seamful + alfrink2023contestable, l. 602–603.** Old: "All three also model one user and one
   system." This is contradicted for Chalmers and Galani, whose Mack Room trial had three co-visitors
   coordinating through heterogeneous media and handling seams socially over a shared audio channel (card
   `algorithmacy_design_ethics/literature/library/chalmersgalani2004.md`, "What it argues" and "Parties
   modeled"). It also sits badly with Alfrink et al.'s actor model of "developers, human controllers, decision
   subjects and third parties" (card `alfrink2023.md`, header). A fix consistent with both cards: "None of the
   three models a counterpart whom the system reads and binds: Chalmers and Galani's co-visitors share a direct
   channel, and Alfrink and colleagues' third parties act for the decision subject." The author should choose
   the wording.

3. **carsten2018how, l. 254–255.** Old: "Carsten and Martens (2018)". New: "Carsten and Martens (2019)". This
   matches the .bib, the Refs entry and the F3 facet. Crossref gives online 2018-05-12 and volume 21(1) 2019
   (https://api.crossref.org/works/10.1007/s10111-018-0484-0).

4. **bansal2019beyond, l. 364.** Old: "while stochasticity makes it hard to learn at all." New: "while a
   stochastic boundary makes a correct model difficult to learn." Source: Bansal et al. 2019 (HCOMP), Results:
   "increased stochasticity makes it difficult for participants to trust Marvin and learn a correct mental
   model" (https://ojs.aaai.org/index.php/HCOMP/article/download/5285/5137).

5. **bansal2019updates, l. 648.** Old: "Bansal and colleagues (2019) and Mohanty and colleagues (2025) supply the
   paradigm". New: "Bansal, Nushi, Kamar, Weld, Lasecki and Horvitz (2019) and Mohanty and colleagues (2025)
   supply the paradigm". The two 2019 Bansal papers have the same six authors, so "Bansal and colleagues (2019)"
   cannot be resolved. Alternatively, adopt 2019a/2019b labels throughout and in the Refs.

6. **alvarez2026upskilling (and li2024user), l. 586–587.** Old: `read "AI literacy for designers" as skill with
   generative tools`. New: `read AI literacy for designers as skill with generative tools` (no quotation marks).
   The quoted phrase appears in neither Alvarez's abstract (OpenAlex, doi:10.1145/3808045.3808059) nor Li et
   al.'s title; it comes from the F1 facet's summary (F1 l. 328, 366).

7. **chernev2015choice, l. 158–159 (minor).** Old: "recovered it only under four conditions — a complex choice set,
   a difficult task, uncertain preferences and an effort-minimizing goal." New: "found that it depends on four
   moderators — a complex choice set, a difficult task, uncertain preferences and an effort-minimizing goal —
   and is reliable only once they are taken into account." Source: the abstract (four factors "moderate the
   impact of assortment size"; the overall effect is significant "when moderating variables are taken into
   account").

8. **audryNDdx, l. 30–32 (minor).** The page is undated but is cited inside "between September 2023 and September
   2026". Old: "…between September 2023 and September 2026 (Audry, n.d.; …)". New, for example: "…between
   September 2023 and September 2026, one of them in an undated page (Audry, n.d.; …)". Source: refetch of
   https://www.andrewaudry.com/dxdesign on 2026-09-30 found no publication date.

9. **bansal2021whole, .bib and Refs l. 712.** Add `pages = {1--16}` and "(pp. 1–16)". Source: Crossref page
   "1-16" (https://api.crossref.org/works/10.1145/3411764.3445717); the ACM reference format in arXiv
   2006.14779v3 gives "16 pages". The ACM article number is still unverified: DBLP returned a bot challenge.

10. **alvarado2017towards, Refs l. 688 (formatting).** The generated entry drops what the .bib holds. Old: "…Redesigning
    Facebook's News Feed. https://…". New: "…Redesigning Facebook's News Feed [Master's thesis, Uppsala
    University]. DiVA. https://…". Source: DiVA record diva2:1110570 ("Student thesis", Uppsala University, 2017).

11. **card1983psychology, Refs l. 724 (optional).** The entry pairs the 1983 Erlbaum edition with the 2018 CRC Press
    DOI. Either drop the DOI or cite the reissue explicitly, for example "(Original work published 1983)" with
    the 2018 CRC Press details. Sources: Open Library OL3500789M (Erlbaum, 1983); Crossref
    10.1201/9780203736166 (CRC Press, 2018-05-04).

12. **carsten2018how, l. 255 (optional).** "applied cognitive-engineering principles" is the F3 facet's gloss, and the
    source was read as abstract only. The abstract says the paper "proposes a set of design principles for
    in-vehicle HMI". A closer wording: "proposed HMI design principles for drivers of automated cars".
