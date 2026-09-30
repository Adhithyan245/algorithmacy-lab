# F6 — From literacy to algorithmacy: the lab's construct, its lineage, and the competing competence constructs

Facet agent F6, 2026-09-30. Worktree `wt-dxd`. Every external entry below is backed either by a database
record I retrieved this session (Crossref, OpenAlex, Semantic Scholar, Europe PMC, Consensus) or by an
existing verified card in this repo; the basis is named per entry. Read status is stated as the card or my
own read gives it, not upgraded.

---

## 0. The lab's own construct (Step 1 — repo sources, not literature entries)

These are the lab's definitional texts. They are summarized here so the DXD arm borrows the construct as the
lab states it; they are not entered in the `.bib`.

**Canonical definition.** The live Lima manuscript's introduction gives the form the brief quotes:
"Algorithmacy is the ability to interpret an opaque, adaptive intermediary, to specify intent through it, and
to keep track of it, so that a person can participate in coordination that runs through a system which reads
both parties and commits decisions neither of them controls" (`submissions/lima_pdw/manuscript/INTRODUCTION.md`,
l. 12 and l. 26). The same paragraph builds the definition on the oracy/literacy/numeracy template ("so that a
person can participate in communication that runs through text … number … speech") and draws the line the DXD
thesis needs: "Literacy, numeracy, and oracy are competences for a medium. Algorithmacy is a competence for a
coordination" (l. 26).

**Three structural properties, three operations.** `submissions/lima_pdw/manuscript/PAPER.md`, §"Algorithmacy:
A Construct for Coordinative Co-optation" and §"Constitutive Operations: The Tripartite Model" (l. 149–171),
names *opacity* (the rule cannot be observed), *adaptivity* (the rule moves), and *bindingness* (the
intermediary's determination binds the focal actor and her counterpart at once). Each property imposes one
deficit and each deficit demands one operation: **interpreting** (reconstructing from one composite signal both
the intermediary's rule and the counterpart's intention), **specifying intent** ("dual-audience encoding" —
one act must satisfy the intermediary's parsing and the counterpart's expectations), and **keeping track**
(detecting unannounced recalibration, often only through shifted counterpart behaviour). The paper frames the
three as a recursive loop, not a trait inventory, and states: "*Keeping track* has no equivalent in traditional
literacy frameworks, because conventional media hold still and this rule does not." It also anchors the
deficit logic in Daft and Lengel's uncertainty/equivocality distinction: the participant lacks not data but a
way to settle which reading of the data is right.

An earlier public essay names the same three parts *inferential, translational, temporal*
(`org_frontier/essays/literacy_or_algorithmacy.md`, Part three). The mapping is one-to-one; the DXD arm should
use the Lima vocabulary.

**Scope and status.** Algorithmacy is an individual *competency* (PAPER.md §"Competency, Not Skill or
Capability"), acquired through participation rather than instruction ("the classroom instruction Laupichler et
al.'s (2023) SNAIL scale evaluates cannot alone cultivate the capacity," §"Acquisition and Distribution"), and
predicted — not assumed — to be unevenly distributed among formally equivalent participants. The paper locates
interventions explicitly: "transparency mandates modify the information environment, whereas cultivating
algorithmacy enhances an actor's capacity to act within it whatever its transparency" (§"Theoretical
Implications").

**Not algocracy.** "The term is not algocracy: Aneesh (2009) uses that word for a mode of organization — rule by
code, set beside bureaucracy and the market — whereas algorithmacy names the individual capacity a person
exercises inside such an arrangement (see also Danaher, 2016)" (PAPER.md, Introduction, l. ~21). Cards:
`submissions/lima_pdw/literature/cards/aneesh2009.md`, `…/danaher2016.md`.

**The eight candidate constructs.** PAPER.md §"Extant Constructs", Table 1, evaluates human–machine
communication (Guzman & Lewis, 2020), AI-mediated communication (Hancock et al., 2020), CMC competence
(Spitzberg, 2006), social information processing / hyperpersonal model (Walther, 1992, 1996), AI literacy (Long &
Magerko, 2020), algorithmic competency (Zhou et al., 2025), reactivity under opaque evaluation (Rahman, 2021), and
gig literacies (Sutherland et al., 2020) against one question — where does the construct put the human
counterpart? — and four conditions (individual capacity; an active interdependent counterpart; an intermediary
that evaluates and binds both; a real vacancy, not a label dispute). The shared finding (§"What These Boundaries
Share"): where a construct admits the counterpart it demotes the system to a conduit, channel, delegate or
obstacle; where it models the system as opaque and binding it demotes the counterpart to a rating source or
outcome variable. Novelty is claimed on "*mutual bindingness* and *interdependent joint work*, not on
adaptation, opacity, or the folk-theoretic capacity itself" — a concession to DeVito (2021) the DXD arm should
keep.

**The dyadic/triadic structural reading, at design-reader level.** The lab models a coordination form (worker,
system, counterpart) as a small Boolean system and computes exact integrated information over the
minimum-information partition. Φ_MIP = 0 means some cut factors the form (dyadic; literacy suffices);
Φ_MIP > 0 means no cut does (triadic; algorithmacy is demanded)
(`org_frontier/essays/studying_algorithmacy.md`, §"The instrument"). Four results matter to a designer:
(i) *the surface lies* — party count and interface do not settle the verdict; "whether the two humans can reach
each other directly comes closer, and still misses"; (ii) in the complete 256-form strict-mediation family at
three nodes "only **9.4%** are triadic," because triadicity needs the mediator to determine jointly from all
parties *and* each party to stay live to the mediator's commit; (iii) substitutability of any party (a
swappable counterpart, a multi-homed platform) collapses the triad to a dyad; (iv) "Disclosure of the agent is
a label, not a read, and leaves the verdict unchanged" (`org_frontier/essays/algorithmacy_outreach_paper.md`,
§"The outreach program", Q63). Every one of these is in-silico, binary (Φ magnitude is not a difficulty scale),
and separated from real organizations by an acknowledged validation gap (studying_algorithmacy.md, §"What the
method cannot do").

**The design-ethics arm's position.** "Algorithmacy is not literacy extended to a new medium — the way literacy
was not oracy extended to a new medium" (`submissions/algorithmacy_design_ethics/README.md`). A *moderator*
carries a message (Φ = 0, literacy suffices); a *mediator* interprets both parties and commits (Φ > 0). The three
principles: agentic parity via **counter-delegation**, not legibility; **structural refusal**, not
hermeneutics; **bounded outputs / operational predictability**, not mechanistic interpretability
(README; `RESEARCH_DOSSIER.md` §4; `DRAFT.md` §"The Category Error" and §"The Design Challenge Ahead"). The
dossier's census found that 0 of 15 cards for the critiqued accounts locate the remedy in "the relation between
the two coordinated people" (RESEARCH_DOSSIER.md §1). DRAFT.md's table puts the disagreement in one row:
"Comprehension is Decoupled from Power."

**Sibling arms.** `submissions/algorithmacy_scaffolding/` frames algorithmacy as a novice/expert shift parallel to
literacy, oracy and numeracy and closes on HCI scaffolding; its dossier recommends algorithmic feed controls
(Eslami et al., 2015; Rader, Cotter & Cho, 2018) as the primary design anchor and reports that confidence
highlighting in an AI interface *worsened* calibration (`RESEARCH_DOSSIER.md` §3, card `bo2025.md`).
`submissions/dial_response_algorithmacy/SOURCE.md` maps the argument onto the PHD1750-3 human-factors course
(perception, cognition, human factors and design), and its `draft.md` §7 proposes to "widen the engagement layer"
through seamful design (Chalmers, 2003; Ehsan et al., 2024) rather than abstract the steering surface away from
novices.

**Flags for the author (conflicts I found, not fixed).**
1. *Definition drift across arms.* At least five wordings circulate: the Lima INTRODUCTION ability-definition
   (above); Lima PAPER.md's "sensibility required to interpret …" (l. 9, l. 151); the essay's "integrated
   competence through which a worker coordinates with another human through an algorithmic third party";
   design-ethics DRAFT.md's "communication competency through which a human worker or citizen navigates,
   negotiates, and coordinates …"; and the Lima README's "communication competency required to coordinate with
   a human counterpart through an opaque, adaptive intermediary." `OVERVIEW.md` l. 14 further writes "A form is
   triadic (irreducible; the lab's name for it is *algorithmacy*)", which names the *form* rather than the
   *competence*. The DXD arm should pick one (the brief's, which is INTRODUCTION.md's) and cite its path.
2. *Intra-lab disagreement on the remedy.* The scaffolding README's closing aim is "moving novices toward
   algorithmic literacy," and the dial-response draft's remedy (expose seams, widen who can read and write the
   mediator) sits close to legibility. The design-ethics arm rejects legibility as a literacy-paradigm remedy.
   These are reconcilable (see synthesis) but they are not yet reconciled in the repo.
3. The scaffolding dossier already flags that Wilkinson (1965) is cited there for a print-history claim he does
   not make, and the design-ethics dossier (§3) reports that the scaffolding essay's "scribal monopoly shattered
   by print" story is contradicted by Clanchy, Goody, Johns and Innis. A DXD draft that reaches for the same
   history inherits both problems.

---

## 1. Search log

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

## 2. Entries

Ordered by theme: (A) lineage, (B) competing competence constructs, (C) design for competence.

### A. Lineage: oracy, literacy, numeracy, digital divides

**wilkinson1965concept**
Wilkinson, A. (1965). The concept of oracy. *Educational Review, 17*(4), 11–15. https://doi.org/10.1080/0013191770170401a
- Basis: card `submissions/lima_pdw/literature/cards/wilkinson1965.md` (Crossref-verified; duplicate at `algorithmacy_scaffolding/literature/library/wilkinson1965.md`).
- Read status: **not accessible** (card is metadata-only; no full text read).
- Wilkinson named "oracy" as the speaking-and-listening ability that deserved the standing schooling already gave literacy and numeracy. The card's secondary sources report his own modest framing that the construct had "merely been given a name." A second Crossref record under the same title (an *English in Education* back-assigned DOI) is a metadata artifact, resolved in the card (2026-08-30).
- **Role in the DXD argument:** precursor — the naming template ("-acy" competence for a medium) the Lima definition copies. Cite only for the coinage, not for print history (scaffolding dossier §2).

**goodywatt1963consequences**
Goody, J., & Watt, I. (1963). The consequences of literacy. *Comparative Studies in Society and History, 5*(3), 304–345. https://doi.org/10.1017/S0010417500001730
- Basis: card `submissions/algorithmacy_design_ethics/literature/library/goodywatt1963.md`.
- Read status: **abstract only** (opening paragraph, p. 304, plus Ong's page-cited uses of the 1968 reprint).
- The opening sentence already draws the "great divide": "man as talking animal primarily by the anthropologist, and man as talking and writing animal primarily by the sociologist" (p. 304). Via Ong, the card records the "homeostatic" character of oral societies and "direct semantic ratification."
- **Role in the DXD argument:** precursor — the strong claim that a new medium of coordination demands and produces a new competence.

**ong1982orality**
Ong, W. J. (1982). *Orality and literacy: The technologizing of the word*. Methuen.
- Basis: card `submissions/algorithmacy_design_ethics/literature/library/ong1982.md`.
- Read status: **read in full** for chs. 3–5 (pp. 31–135) per the card; chs. 1–2, 6–7 skimmed.
- Ong states the cognitive thesis without hedging: "More than any other single invention, writing has transformed human consciousness" (p. 77), and lists nine characteristics of orally based thought (pp. 36–57), which he himself calls "suggestive" rather than "exclusive or conclusive" (p. 36).
- **Role in the DXD argument:** precursor (and the strongest version of the analogy DXD draws); must be paired with the Street entry.

**street1984literacy**
Street, B. V. (1984). *Literacy in theory and practice*. Cambridge University Press.
- Basis: card `submissions/algorithmacy_design_ethics/literature/library/street1984.md` (also `scribner1981.md`, `graff1991.md`).
- Read status: **not accessible** (secondary only; Armer 1992's statement of the two models is the only verbatim formulation in the library).
- Street's "autonomous" vs "ideological" models, as Armer restates them: the autonomous model holds that literacy "produces uniform consequences for individuals"; the ideological model that "consequences vary … depending upon the processes through which literacy is acquired and the purposes for which it is intended." Scribner and Cole's (1981) Vai study (card `scribner1981.md`, secondary, not opened) is the empirical companion; the card reports its standard reading — general cognitive effects track schooling, not literacy as such — but flags that it could not verify this from the text.
- **Role in the DXD argument:** counterevidence to a cognitive great-divide reading. The design-ethics dossier (§3) concludes the lab's claim survives only at the institutional register ("institutions came to *require* literacy"), not the cognitive one. DXD's "new cognitive issues" framing must make the same concession.

**newlondon1996pedagogy**
The New London Group. (1996). A pedagogy of multiliteracies: Designing social futures. *Harvard Educational Review, 66*(1), 60–93. https://doi.org/10.17763/haer.66.1.17370n67v22j160u
- Basis: Crossref record (retrieved this session); OpenAlex (5,560 citing works); Semantic Scholar (closed access).
- Read status: **abstract only** (OpenAlex holds a truncated abstract: "a theoretical overview of the connections between the changing social environment facing students and teachers and a new approach to literacy pedagogy").
- The founding statement of multiliteracies — the move that pluralized literacy across modes and treated meaning-making as design. Its later elaboration into a theory of "meaning as design" is documented in Kalantzis & Cope (2024) (card below). I did not read the article and make no claim about its internal "design" vocabulary.
- **Role in the DXD argument:** competing-construct lineage — the strongest route by which a reviewer will argue algorithmacy is "just another literacy."

**peters2006numeracy**
Peters, E., Västfjäll, D., Slovic, P., Mertz, C. K., Mazzocco, K., & Dickert, S. (2006). Numeracy and decision making. *Psychological Science, 17*(5), 407–413. https://doi.org/10.1111/j.1467-9280.2006.01720.x
- Basis: Crossref record with abstract (retrieved this session); OpenAlex (1,181 citing works).
- Read status: **abstract only**.
- Four studies found "highly numerate individuals being more likely to retrieve and use appropriate numerical principles, thus making themselves less susceptible to framing effects," and that "the effect of numeracy was not due to general intelligence" (abstract). The highly numerate also drew "more precise" affective meaning from numbers, which "may sometimes lead to worse decisions."
- **Role in the DXD argument:** UX-cognitive-foundation / precursor — the clearest evidence that an "-acy" competence moderates *decision* quality, independent of intelligence. It is the numeracy leg of the Lima template and the natural model for how a DXD programme would measure an algorithmacy effect on decisions.

**hargittai2002second**
Hargittai, E. (2002). Second-level digital divide: Differences in people's online skills. *First Monday, 7*(4). https://doi.org/10.5210/fm.v7i4.942
- Basis: card `submissions/lima_pdw/literature/cards/hargittai2002.md`.
- Read status: **read in full** (author-deposited PDF, per card).
- Among 54 observed adult users, 27/54 completed all five search tasks, and completion time among the fully successful varied up to twelvefold (2.5 to 30.3 minutes); age was negatively and experience positively associated with skill. Access does not equal effective use.
- **Role in the DXD argument:** precursor — the structural logic the Lima paper borrows for "stratified fluency": formally equal access, unequal competence, unequal outcomes.

### B. Competing competence constructs

**aneesh2009global**
Aneesh, A. (2009). Global labor: Algocratic modes of organization. *Sociological Theory, 27*(4), 347–370. https://doi.org/10.1111/j.1467-9558.2009.01352.x
- Basis: card `submissions/lima_pdw/literature/cards/aneesh2009.md` (duplicate in `algorithmacy_scaffolding`); companion `danaher2016.md` (Danaher, 2016, *Philosophy & Technology* 29(3), 245–268).
- Read status: **abstract only**.
- Aneesh names algocracy a third organizing principle beside bureaucracy (legal-rational authority) and the market (price): code embedded in the work platform structures what dispersed programmers can do. The card notes the coinage predates this article (*Virtual Migration*, 2006) but could not verify the book's wording.
- **Role in the DXD argument:** competing-construct (term collision). Algocracy is a property of the *system*; algorithmacy is a property of the *person* acting inside it.

**longmagerko2020ai**
Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (Paper 598, pp. 1–16). ACM. https://doi.org/10.1145/3313831.3376727
- Basis: card `submissions/lima_pdw/literature/cards/longmagerko2020.md` (and `algorithmacy_design_ethics/…/longmagerko2020.md`); definition quoted in Lima PAPER.md §"AI Literacy", verified against a camera-ready steelman per the card.
- Read status: **abstract only** (card); quotes verified against the camera-ready copy by an earlier pass; page numbers deliberately removed.
- AI literacy is "a set of competencies that enables individuals to critically evaluate AI technologies; communicate and collaborate effectively with AI; and use AI as a tool online, at home, and in the workplace," derived as seventeen competencies from five questions (what AI is, what it can do, how it works, how it should be used, how people perceive it). Lima PAPER.md: "No competency in the seventeen names another person as a party to the interaction."
- **Role in the DXD argument:** competing-construct — the one most UX/HCI readers will assume DXD means. It pairs *competencies* with *design considerations*, which makes it the nearest HCI precedent for "design for a competence."

**ng2021conceptualizing**
Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI literacy: An exploratory review. *Computers and Education: Artificial Intelligence, 2*, 100041. https://doi.org/10.1016/j.caeai.2021.100041
- Basis: card `submissions/lima_pdw/literature/cards/ng2021.md`.
- Read status: **abstract only**.
- From thirty peer-reviewed articles, Ng and colleagues compress Long and Magerko's competencies into four aspects — know and understand AI, use and apply AI, evaluate and create AI, ethical issues — by analogy with "classic literacies." The card traces how MAILS, AICOS and later questionnaires inherit these four cells.
- **Role in the DXD argument:** competing-construct; the transmission mechanism by which the literacy frame (person ↔ system, no second human) propagates into measurement.

**dogruel2022development**
Dogruel, L., Masur, P., & Joeckel, S. (2022). Development and validation of an algorithm literacy scale for internet users. *Communication Methods and Measures, 16*(2), 115–133. https://doi.org/10.1080/19312458.2021.1968361
- Basis: card `submissions/lima_pdw/literature/cards/dogruel2022.md`; Crossref and Consensus abstract re-retrieved this session. Conceptual companion: `…/dogruel2021.md` (Dogruel, 2021, read in extended preview).
- Read status: **abstract only** (the 2021 chapter: extended preview, framework sections read in full per card).
- Study 1 tested 46 items (N = 331) → 32-item pool; Study 2 (N = 1,041 German internet users) → a final scale of 11 awareness + 11 knowledge items (abstract). The conceptual definition has four parts (awareness, knowledge, critical evaluation, coping/influencing skills) but the scale operationalizes only the first two. The 2021 chapter derives the dimensions by analogy from media, digital, code and privacy literacies.
- **Role in the DXD argument:** competing-construct (algorithmic literacy). Knowledge is scored against a researcher-supplied key — exactly what Hargittai et al. (2020) say cannot exist.

**oeldorfhirsch2025what**
Oeldorf-Hirsch, A., & Neubaum, G. (2025). What do we know about algorithmic literacy? The status quo and a research agenda for a growing field. *New Media & Society, 27*(2), 681–701. https://doi.org/10.1177/14614448231182662
- Basis: card `submissions/lima_pdw/literature/cards/oeldorfhirsch2025.md` (and design-ethics copy); Consensus record this session; snowball seed (row 19).
- Read status: **read in full** (author deposit and SAGE VoR, per card).
- The authors screened 96 candidates and reviewed 50 across eight neighbouring terms (including "algorithmic experience," "algorithmic skills," "algorithmic divide"). They find two competing definitions (DeVito's; Dogruel et al.'s), call Dogruel et al.'s scale "currently the most comprehensive attempt" that still "breaks into two sub-scales that together do not measure algorithmic literacy as one cohesive construct," and set a four-item agenda: balance user literacy against developers' transparency responsibility; methods for engaging users in raising their literacy; affective and behavioural facets; the new algorithmic divide.
- **Role in the DXD argument:** competing-construct (field audit). Agenda item 2 is the explicit call for design-for-literacy work; item 1 is the literacy paradigm's own admission that the burden may sit with developers.

**gagrcin2026algorithmic**
Gagrčin, E., Naab, T. K., & Grub, M. F. (2026). Algorithmic media use and algorithm literacy: An integrative literature review. *New Media & Society, 28*(1), 423–447. https://doi.org/10.1177/14614448241291137 (online 2024)
- Basis: card `submissions/lima_pdw/literature/cards/gagrcin2026.md`; Crossref (print 2026-01, online 2024-11-08) and OpenAlex abstract this session.
- Read status: **read in full** (SAGE VoR, per card).
- A systematic integrative review of 169 studies finds the field "lacks a cohesive framework" and proposes framing acquisition as **experiential learning cycles**, with an agenda of core competencies, standardized measures, integration of subjective and factual aspects, and task- and domain-specific approaches (abstract).
- **Role in the DXD argument:** competing-construct; its experiential-learning account of acquisition converges with Lima's "acquired through participation" and so supports in-situ scaffolding over instruction.

**gran2021algorithm**
Gran, A.-B., Booth, P., & Bucher, T. (2021). To be or not to be algorithm aware: A question of a new digital divide? *Information, Communication & Society, 24*(12), 1779–1796. https://doi.org/10.1080/1369118X.2020.1736124
- Basis: card `submissions/lima_pdw/literature/cards/gran2021.md` (and design-ethics copy); Crossref dates re-checked this session.
- Read status: **abstract only**.
- A representative Norwegian web survey (N = 1,624, November 2018) measured awareness by a single self-report item; awareness ran higher among men and the better educated and declined with age, and a cluster analysis produced six groups (the unaware, uncertain, affirmative, neutral, sceptic, critical).
- **Role in the DXD argument:** competing-construct (algorithmic awareness) and distributional evidence — even the bottom rung of the literacy ladder is unevenly held.

**hargittai2020black**
Hargittai, E., Gruber, J., Djukaric, T., Fuchs, J., & Brombach, L. (2020). Black box measures? How to study people's algorithm skills. *Information, Communication & Society, 23*(5), 764–775. https://doi.org/10.1080/1369118X.2020.1713846
- Basis: card `submissions/lima_pdw/literature/cards/hargittai2020.md`; OpenAlex hit this session (row 14).
- Read status: **abstract only**.
- The paper states the measurement problem that separates algorithm skill from other digital skills: platform details are proprietary, so the researcher cannot score a respondent's belief as correct. The definition later work uses — algorithm awareness as "knowing that a dynamic system is in place that can personalize and customize the information that a user sees or hears" — is quoted at p. 771 via Oeldorf-Hirsch & Neubaum.
- **Role in the DXD argument:** competing-construct ("algorithm skills") and methodological warrant — competence under opacity shows in conduct, not in correct answers, which supports measuring algorithmacy behaviourally.

**klawitter2018learning**
Klawitter, E., & Hargittai, E. (2018). "It's like learning a whole other language": The role of algorithmic skills in the curation of creative goods. *International Journal of Communication, 12*, 3490–3510.
- Basis: card `submissions/lima_pdw/literature/cards/klawitterhargittai2018.md` (junior slug of `klawitter2018.md`); OpenAlex record per card. No Crossref DOI exists.
- Read status: **abstract only** (the card is the weakest-verified in its cluster; volume/pages not confirmed against a registry).
- Interviews with creative entrepreneurs selling through algorithmically ranked marketplaces frame algorithmic skill as a distinct, unevenly held, informally acquired competence consequential for sales; the informant's "whole other language" metaphor names it.
- **Role in the DXD argument:** competing-construct ("algorithmic skills"); the earliest labelling of the phenomenon as a skill with a real counterpart (buyers), though the buyer is a ranking input, not a coordinated party.

**zhou2025algorithmic**
Zhou, L., Lei, X., Liu, M., Huang, X., & Hou, R. (2025). Algorithmic competency of on-demand labor platform workers: Scale development, antecedents, and consequences. *Asia Pacific Journal of Human Resources, 63*(2), e70004. https://doi.org/10.1111/1744-7941.70004
- Basis: card `submissions/lima_pdw/literature/cards/zhou2025apjhr.md` (do not confuse with `zhou2025.md`, a different HRM paper).
- Read status: **read in full** (VoR PDF, per card).
- Across five samples of Chinese ride-hailing drivers and couriers (99 interviews; EFA N = 275; CFA N = 213; validity N = 230; three-wave N = 225), the authors validate a 12-item, second-order, four-factor scale — Understanding, Embracing, Leveraging, Remediating AM; overall α = .85 — correlating r = .37 with digital competence. Only the Understanding triad is knowledge-like. No item measures coordination *with* the customer; the card singles out item 11 ("…such as in customers-workers matching") as the item a reviewer will cite against the vacancy claim.
- **Role in the DXD argument:** competing-construct — the most dangerous rival ("algorithmic competence"), because three of four dimensions are conduct and attitude, not knowledge. DXD cannot distinguish algorithmacy by calling rivals "knowledge tests."

**devito2021adaptive**
DeVito, M. A. (2021). Adaptive folk theorization as a path to algorithmic literacy on changing platforms. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW2), Article 339, 1–38. https://doi.org/10.1145/3476080
- Basis: card `submissions/lima_pdw/literature/cards/devito2021.md`.
- Read status: **read in part** (author-deposited PDF; framing, definition, findings and discussion read, per card).
- DeVito defines algorithmic literacy as "the capacity and opportunity to be aware of both the presence and impact of algorithmically-driven systems on self- or collaboratively-identified goals, and the capacity and opportunity to crystalize this understanding into a strategic use of these systems," argues that platforms changing under users demand a literacy "extensible by design," and derives a four-level Theorization Complexity Level from a 25-participant LGBTQ+ Facebook study.
- **Role in the DXD argument:** competing-construct — the closest rival to *keeping track*. Lima concedes adaptation and folk theorization to her and claims novelty only on mutual bindingness and joint work.

**kalantzis2024literacy**
Kalantzis, M., & Cope, B. (2024). Literacy in the time of artificial intelligence. *Reading Research Quarterly, 60*(1), Article e591. https://doi.org/10.1002/rrq.591
- Basis: card `submissions/coordinative_sovereignty/literature/library/cards/kalantzis2024literacy.md` (verified full via Scholar Gateway, 2026-08-23).
- Read status: **read in part** (abstract and the sections "Literacy, redefined" and "What is to be done?", per card).
- Two of the multiliteracies authors argue that generative AI is "before anything else a technology of writing," as momentous for literacy as movable type, and that literacy in the time of AI needs a revised grammar built on their theory of "meaning as design."
- **Role in the DXD argument:** competing-construct / counterevidence — the explicit "literacy extended to a new medium" position the design-ethics arm argues against, made by the field's most design-minded literacy theorists. DXD must answer it, not ignore it.

### C. Design for competence: seams, algorithmic experience, contestability, boosting

**alvarado2018towards**
Alvarado, O., & Waern, A. (2018). Towards algorithmic experience: Initial efforts for social media contexts. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. https://doi.org/10.1145/3173574.3173860
- Basis: Crossref, Semantic Scholar (closed), Consensus abstract (all this session); snowball seed (row 18).
- Read status: **abstract only**.
- From participatory workshops scrutinizing Facebook's News Feed, the authors "propose the concept of Algorithmic Experience (AX) as an analytic framing for making the interaction with and experience of algorithms explicit," with functional design categories named in the abstract as "profiling transparency and management, algorithmic awareness and control, and selective algorithmic memory."
- **Role in the DXD argument:** term-use / precursor — the nearest HCI precedent for extending UX to algorithms by name. Its categories are transparency and control over one's own profile: a dyadic, literacy-side framing with no counterpart.

**shin2020beyond**
Shin, D., Zhong, B., & Biocca, F. A. (2020). Beyond user experience: What constitutes algorithmic experiences? *International Journal of Information Management, 52*, 102061. https://doi.org/10.1016/j.ijinfomgt.2019.102061
- Basis: Crossref and Semantic Scholar (this session); abstract via Consensus.
- Read status: **abstract only** (closed).
- Shin and colleagues propose an Algorithm Acceptance Model and report that AX "is inherently related to human understanding of fairness, transparency, and other conventional components of user-experience," with transparency and fairness playing "heuristic roles" in trust and acceptance.
- **Role in the DXD argument:** term-use — "beyond user experience" is the DXD move in name; the construct measured is acceptance and trust of one user toward one system, so it stays on the literacy side of the lab's line.

**chalmersgalani2004seamful**
Chalmers, M., & Galani, A. (2004). Seamful interweaving: Heterogeneity in the theory and design of interactive systems. In *Proceedings of the 5th Conference on Designing Interactive Systems (DIS '04)* (pp. 243–252). ACM. https://doi.org/10.1145/1013115.1013149
- Basis: card `submissions/algorithmacy_design_ethics/literature/library/chalmersgalani2004.md`; companion card `submissions/dial_response_algorithmacy/literature/cards/chalmers-2003-seamful-design-ubicomp-workshop.md` (Chalmers, 2003, read in full, no DOI).
- Read status: **read in full** (author deposit, cited by section, per card).
- "People accommodate and take advantage of seams and heterogeneity, in and through the process of interaction" (abstract); "we have to expect that a new technology will be to some degree present-at-hand, no matter how well the designer aims towards embodied … interaction" (§ Heterogeneity and ubiquity). Chalmers (2003) adds the design rule: mechanisms "literally visible, effectively invisible," revealable "when the task is to understand or even change the tool."
- **Role in the DXD argument:** precursor (design for competence) — the alternative to the seamless-UX ideal, and the root of the dial-response arm's "widen the engagement layer" remedy.

**ehsan2024seamful**
Ehsan, U., Liao, Q. V., Passi, S., Riedl, M. O., & Daumé III, H. (2024). Seamful XAI: Operationalizing seamful design in explainable AI. *Proceedings of the ACM on Human-Computer Interaction, 8*(CSCW1), Article 119, 1–29. https://doi.org/10.1145/3637396
- Basis: card `submissions/dial_response_algorithmacy/literature/cards/ehsan-etal-2024-seamful-xai.md` (also `algorithmacy_scaffolding/…/ehsan2024.md`); OpenAlex hit this session (row 13).
- Read status: **abstract only** (card does not claim full text).
- A scenario-based co-design study with 43 AI practitioners and end-users reports that the seamful process helped participants foresee harms, name seams, locate them in the AI lifecycle, and use seamful information to improve explainability and user agency.
- **Role in the DXD argument:** precursor (design for competence) — seamful design carried into algorithmic systems; still framed as explainability, so it sits at the boundary of the legibility paradigm.

**eslami2015always**
Eslami, M., Rickman, A., Vaccaro, K., Aleyasen, A., Vuong, A., Karahalios, K., Hamilton, K., & Sandvig, C. (2015). "I always assumed that I wasn't really that close to [her]": Reasoning about invisible algorithms in news feeds. In *Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems* (pp. 153–162). ACM. https://doi.org/10.1145/2702123.2702556
- Basis: card `submissions/algorithmacy_scaffolding/literature/library/eslami2015.md` (also `lima_pdw/…/eslami2015.md`).
- Read status: **read in full** (author PDF, per card).
- Of 40 Facebook users, 62.5% did not know the feed was curated; the FeedVis tool (curated vs. unfiltered views, a "Friend View" binning friends into rarely/sometimes/mostly shown) changed how they reasoned about it. The authors' design conclusion: "simple exposure to the algorithm output is not enough … To learn about an algorithm without any outside information, active engagement is required."
- **Role in the DXD argument:** algorithmacy-cognitive-issue / design for competence — the canonical built-and-tested artifact for revealing a curating algorithm; the scaffolding arm's recommended primary anchor.

**rader2018explanations**
Rader, E., Cotter, K., & Cho, J. (2018). Explanations as mechanisms for supporting algorithmic transparency. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). ACM. https://doi.org/10.1145/3173574.3173677
- Basis: card `submissions/algorithmacy_scaffolding/literature/library/radercottercho2018.md`; Crossref pages checked this session.
- Read status: **read in full** (author PDF, per card).
- In a between-subjects experiment with 681 US Facebook users, four 200-word explanation types (What, How, Why, Objective) all raised belief that the *system* has agency and raised "Understand Why," but none shifted *user* agency; *How* made the feed seem more random and reduced belief that UI controls do anything; only *What* moved correctness beliefs and only *What* lowered perceived fairness.
- **Role in the DXD argument:** counterevidence to legibility — explanation raises awareness while lowering felt control.

**cheng2019explaining**
Cheng, H.-F., Wang, R., Zhang, Z., O'Connell, F., Gray, T., Harper, F. M., & Zhu, H. (2019). Explaining decision-making algorithms through UI: Strategies to help non-expert stakeholders. In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. https://doi.org/10.1145/3290605.3300789
- Basis: Crossref (this session); abstract via Consensus.
- Read status: **abstract only**.
- In an online experiment (199 participants) with explanation interfaces for a university-admissions algorithm, interactive and "white-box" explanations improved comprehension (interactive more so, at a time cost), but "users' trust in algorithmic decisions is not affected by the explanation interface or their level of comprehension" (abstract).
- **Role in the DXD argument:** counterevidence to legibility — comprehension and trust come apart, consistent with the design-ethics arm's "comprehension is decoupled from power."

**moon2025effects**
Moon, J. H., Kim, S., Jung, Y., Bang, J., & Sung, Y. (2025). The effects of explainability and user control on algorithmic transparency: The moderating role of algorithmic literacy. *Cyberpsychology, Behavior, and Social Networking, 28*(7), 497–504. https://doi.org/10.1089/cyber.2024.0525
- Basis: Crossref (this session); abstract via Consensus.
- Read status: **abstract only**.
- A 2 × 2 × 2 between-subjects experiment (N = 240) on a fictitious short-video platform found a three-way interaction on all outcomes: explainability and user control raised perceived transparency, legitimacy and satisfaction, but "when neither feature was present, algorithmic literacy had no significant impact," and when at least one was present literacy "significantly influenced" the outcomes. The authors conclude literacy "creates a new dimension of the digital divide."
- **Role in the DXD argument:** counterevidence to legibility as an equalizer — transparency features pay off mainly for the already-literate, so legibility can widen the divide Lima's Proposition 2 predicts.

**fouquaert2022making**
Fouquaert, T., & Mechant, P. (2022). Making curation algorithms apparent: A case study of 'Instawareness' as a means to heighten awareness and understanding of Instagram's algorithm. *Information, Communication & Society, 25*(12), 1769–1789. https://doi.org/10.1080/1369118X.2021.1883707 (online 2021)
- Basis: Crossref and OpenAlex (this session); OA accepted manuscript at biblio.ugent.be.
- Read status: **read in part** (OA accepted manuscript retrieved; methods and results §4 read).
- Sixty-four respondents aged 18–35 completed all three phases of a quasi-experiment. Using the tool raised cognitive media literacy (H1 accepted; F(1, 61) = 8.93, p = .004, ηp² = .13, §4.1) but did not significantly raise critical concern (H3 rejected; F(1, 61) = 1.63, p = .21, §4.3). The abstract's reading: "it is not cognitive understanding … but solely awareness" that tracks critical concern.
- **Role in the DXD argument:** design for competence (evidence) — a small, convenience-sample demonstration that a revealing interface moves awareness; the effect on anything beyond awareness is weak.

**alfrink2023contestable**
Alfrink, K., Keller, I., Kortuem, G., & Doorn, N. (2023). Contestable AI by design: Towards a framework. *Minds and Machines, 33*(4), 613–639. https://doi.org/10.1007/s11023-022-09611-z
- Basis: card `submissions/algorithmacy_design_ethics/literature/library/alfrink2023.md` (also `lima_pdw/…/alfrink2023.md`, `dial_response/…/alfrink-etal-2023-contestable-ai-by-design.md`).
- Read status: **read in full** (TU Delft OA deposit, cited by section, per card).
- Contestable systems are "open and responsive to human intervention throughout their lifecycle" (§1); the review yields five system features (built-in safeguards, interactive control over decisions, explanations, human review and intervention requests, tools for scrutiny) and six development practices (§6). The design-ethics card classes its remedy locus as "artifact and adoption."
- **Role in the DXD argument:** design for competence (contestability) — the nearest design framework to the design-ethics arm's "structural refusal," but it remedies at the artifact, not at the relation between the two coordinated people.

**vaccaro2020end**
Vaccaro, K., Sandvig, C., & Karahalios, K. (2020). "At the end of the day Facebook does what it wants": How users experience contesting algorithmic content moderation. *Proceedings of the ACM on Human-Computer Interaction, 4*(CSCW2), Article 167, 1–22. https://doi.org/10.1145/3415238
- Basis: card `submissions/lima_pdw/literature/cards/vaccaro2020.md`; companion `dial_response_algorithmacy/…/vaccaro-etal-2021-contestability-content-moderation.md` (users designing their own contestation mechanisms converged on representation, communication, compassion).
- Read status: **abstract only**.
- In a large online experiment, none of the appeal designs improved Fairness, Accountability, Trustworthiness or Control (FACT) perceptions relative to a no-appeal baseline; appeal texts contested the decision and also the goal of moderation, automation itself, and system inconsistency.
- **Role in the DXD argument:** counterevidence — adding a contest channel to the interface does not by itself change how the governed experience the system.

**hertwig2017nudging**
Hertwig, R., & Grüne-Yanoff, T. (2017). Nudging and boosting: Steering or empowering good decisions. *Perspectives on Psychological Science, 12*(6), 973–986. https://doi.org/10.1177/1745691617702496
- Basis: Crossref and Semantic Scholar (this session); abstract via Consensus; snowball seed (row 20). The OA green copy (MPG PuRe) sat behind a bot challenge I did not pass.
- Read status: **abstract only**.
- "The objective of boosts is to foster people's competence to make their own choices—that is, to exercise their own agency"; boosts and nudges differ in target, research roots, causal pathway, assumed cognitive architecture, reversibility, ambition and normative implications (abstract). Kozyreva et al. (2020) cite p. 977 for boosts targeting cognition, the environment, or both.
- **Role in the DXD argument:** precursor / competing design paradigm — "boosting" is behavioural science's name for designing *for* a competence; it is the most developed bridge between choice architecture (DXD's precursor field) and competence-building.

**kozyreva2020citizens**
Kozyreva, A., Lewandowsky, S., & Hertwig, R. (2020). Citizens versus the internet: Confronting digital challenges with cognitive tools. *Psychological Science in the Public Interest, 21*(3), 103–156. https://doi.org/10.1177/1529100620946707
- Basis: Crossref (this session); Europe PMC full text PMC7745618 (retrieved this session).
- Read status: **read in part** (OA full text retrieved; introduction, glossary and the nudging/technocognition/boosting section read).
- The authors identify four challenge types (persuasive and manipulative choice architectures, AI-assisted information architectures, false and misleading information, distracting environments) and three intervention types (nudges, technocognition, boosts). They write that boosts "specifically aim not only to preserve but also to foster and extend human agency and autonomy" and "are by necessity transparent because they require an individual's active cooperation," and that boosting responds to "rapidly changing digital environments by aiming to foster lasting and generalizable competencies in users."
- **Role in the DXD argument:** design for competence — the fullest map of competence-building interventions for algorithmic environments; its targets are individual cognition and the information environment, never the relation to a counterpart.

---

## 3. Thematic synthesis

**The analogy holds at the institutional register, not the cognitive one.** Wilkinson (1965) supplies the
naming template and Ong (1982) the strong claim that writing "transformed human consciousness." Street (1984),
as his testers restate him, answers that literacy's effects follow its practices, and the design-ethics
dossier concludes the lab can claim only that institutions came to *require* the new competence. That
concession bites DXD harder than the other arms, because the author's thesis runs through cognition: UX drew on
the psychology of reading and perception, so DXD is to draw on the cognition of algorithmacy. Peters et al.
(2006) show the safer form of the argument. Numeracy predicts decision quality independent of intelligence;
it does not rewire the mind. DXD should claim that algorithmacy moderates decisions made through
intermediaries, which is testable, and leave the great-divide claim to Ong.

**Every competing construct is dyadic, and the good ones are not knowledge tests.** Across the literature
Oeldorf-Hirsch and Neubaum (2025) and Gagrčin et al. (2026) audit, algorithmic literacy (Dogruel et al., 2022),
awareness (Gran et al., 2021), AI literacy (Long & Magerko, 2020; Ng et al., 2021) and algorithm skills
(Hargittai et al., 2020; Klawitter & Hargittai, 2018) place one person against one system. The lab does not
distinguish algorithmacy by calling these knowledge constructs, and it should not: Zhou et al.'s (2025) scale
is three-quarters conduct and attitude, and DeVito (2021) already owns adaptation to a moving rule. The only
distinction the Lima paper defends is structural — a counterpart whose intentions must be reconstructed, an
intermediary that binds both, work done jointly. Kalantzis and Cope (2024) state the live alternative outright:
AI is a writing technology, so literacy, redesigned, absorbs it. Algocracy (Aneesh, 2009) is a separate matter,
a property of the system.

**Legibility builds awareness, not agency.** The design-for-competence literature splits. Revealing interfaces
work on awareness: Eslami et al. (2015) and Fouquaert and Mechant (2022, ηp² = .13 on media literacy) show it.
Every stronger outcome fails or reverses. Rader et al.'s (2018) explanations raised system agency but not user
agency; Cheng et al. (2019) found comprehension without trust; Vaccaro et al.'s (2020) appeals moved no FACT
perception; Moon et al. (2025) found transparency pays off mainly for the already-literate. The lab's own model
predicts this. Disclosure "is a label, not a read, and leaves the verdict unchanged" (Q63). A legible triad is
still a triad.

**Seams, contestability and boosts sit between the paradigms.** Seamful design (Chalmers & Galani, 2004; Ehsan
et al., 2024), algorithmic experience (Alvarado & Waern, 2018; Shin et al., 2020), contestability (Alfrink et
al., 2023) and boosting (Hertwig & Grüne-Yanoff, 2017; Kozyreva et al., 2020) all design *for* a user's
competence rather than steering around it. None places the counterpart inside the design. Here the lab disagrees
with itself: the dial-response arm treats widening seams as the remedy, while the design-ethics arm treats
anything that helps a person read the mediator as the literacy trap.

**What this means for the DXD professional.** Three roles follow, and the review should keep them apart.
*Design with algorithmacy* is the designer's own expertise. It is the structural reading the Φ program formalizes:
does the system jointly determine from both parties, can they reach or exit to each other, is anyone
substitutable. Only 9.4% of three-node strict-mediation forms turn out triadic, so the expert's first job is to tell a
moderator from a mediator before choosing a remedy. *Design for algorithmacy* builds the user's three
operations in situ, because Lima and Gagrčin et al. agree the capacity is acquired through participation.
Change-notification serves keeping track; composite-feedback decomposition serves interpreting; dual-audience
previews serve specifying intent. *Legibility* is the remedy that fits the dyadic case. Applied to a triad, it
leaves the structure intact.

---

## 4. Gaps and unverified leads

**Gaps.**
- No study I found designs an interface to build a user's capacity to coordinate *with a counterpart* through an
  algorithm. Every design-for-competence study (Eslami, Rader, Fouquaert, Cheng, Moon, Alvarado) is one user and
  one system. That is the DXD arm's clearest empirical opening, and it matches the Lima vacancy claim.
- No boosting study targets algorithmic intermediaries that bind two parties; Kozyreva et al. target misinformation
  and attention.
- Data literacy was not searched in depth. The repo holds `coordinative_sovereignty/…/cards/gray2018data.md` (data
  infrastructure literacy) and `sander2020critical.md`, unread by me this session.
- Digital literacy's canonical framework (Eshet-Alkalai, 2004, *Journal of Educational Multimedia and Hypermedia*
  13(1), 93–106; OpenAlex W1560056355, no DOI) was located but not read; not entered.

**Unverified or deferred leads (records retrieved, not entered).**
- Lorenz-Spreen, Lewandowsky, Sunstein & Hertwig (2020), *Nature Human Behaviour* 4(11), 1102–1109,
  doi:10.1038/s41562-020-0889-7 — nudging vs. boosting for "the factors underlying algorithmic decisions";
  paywalled (preview only).
- Herzog & Hertwig (2025), *Annual Review of Psychology* 76, 851–881, doi:10.1146/annurev-psych-020924-124753 —
  boosting review.
- Becker, Skirzyński, van Opheusden & Lieder (2022), *Computational Brain & Behavior* 5(4), 467–490,
  doi:10.1007/s42113-022-00149-y — "AI-powered boosting" via automatically generated decision aids (abstract only;
  full-text fetch failed). Strong DXD lead: the algorithm builds the user's decision competence.
- Petrovčič, Reisdorf, Vehovar & Bartol (2024), *ICS* 28(4), 557–574, doi:10.1080/1369118X.2024.2363896 —
  algorithm awareness and knowledge in three-level digital inequality (N = 802, Slovenia).
- Silva, Chen & Zhu (2024), *New Media & Society* 26(5), 2992–3017, doi:10.1177/14614448221098042 — an algorithmic
  literacy intervention whose effect depended on technology use.
- Swart (2021), *Social Media + Society* 7(2) — card exists (`lima_pdw/…/swart2021.md`): knowing about algorithms
  does not prompt intervention.
- Ha & Kim (2024), *Telecommunications Policy* 48(3), 102682 — "digital platform literacy"; card exists
  (`lima_pdw/…/ha2024.md`). A further competing construct a reviewer may raise.
- Eslami (2017), CSCW Companion pp. 57–60, doi:10.1145/3022198.3024947 — "algorithm-aware design" (doctoral
  consortium abstract). The brief's "Eslami et al. 2017 seamful design for algorithms" did not resolve to a paper
  by that title; the seamful-algorithm search (row 13) returned only Ehsan et al. (2024).
- Scholar Gateway was unavailable all session (identity error), so no Wiley full-text passages were retrieved.
