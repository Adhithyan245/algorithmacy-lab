# F4 — The cognitive foundations of UX/HCI (left-hand side of the DXD analogy)

Facet agent F4 · built 2026-09-30 in worktree `wt-dxd` · 32 entries · companion BibTeX: `F4_ux_cognitive_foundations.bib`

**Scope.** This facet tests the historical claim behind DXD: UX design became a profession by importing cognitive science and human factors, and specific cognitive findings became design knowledge. It also asks what *unit* each wave of that knowledge took, and whether "a decision in an algorithmically mediated coordination" could be the next one.

**Read-status key.** *Read in full* means I read open-access full text this session, or an existing repo card built from full text. *Partial* means I read the full text only in the named sections. *Abstract only* means the database abstract or a publisher excerpt. *Not accessible* means only a bibliographic record exists, so the entry makes no claim about content beyond what its record or another read source states. Quotations are kept short. Page locators follow the version I read, which is flagged where it differs from the version of record.

---

## (a) Search log

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

## (b) Entries

Entries run in the order of the argument: human-factors origins, cognitive HCI, the memory and load findings (including the Miller caution), reading and perception, historiography, and the profession.

### Human-factors origins

**fitts1954information**
Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement. *Journal of Experimental Psychology, 47*(6), 381–391.
DOI: 10.1037/h0055392 · Basis: Crossref + OpenAlex W4239127880 (6,505 citations) · Status: **not accessible** (APA paywall; no abstract in any index).
Fitts treated aimed movement as the transmission of information. MacKenzie (1992; entry below) summarizes the law this paper founded and documents its adoption in HCI. I make no claim here about the paper's own data.
**Role:** UX-cognitive-foundation (motor channel; the keystroke/pointing unit).

**mackenzie1992fitts**
MacKenzie, I. S. (1992). Fitts' law as a research and design tool in human-computer interaction. *Human–Computer Interaction, 7*(1), 91–139.
DOI: 10.1207/s15327051hci0701_3 · Basis: Crossref; OpenAlex abstract · Status: **abstract only**.
MacKenzie reports that Fitts's model treats human movement "by analogy to the transmission of information" and has been adopted in kinematics, human factors and "(recently)" HCI. He reviews six Fitts's-law studies of cursor positioning across mouse, trackball, joystick, touchpad, helmet-mounted sight and eye tracker. He finds "tremendous inconsistencies" across studies, and he proposes a reformulated index of difficulty.
**Role:** UX-cognitive-foundation. It documents the import itself: a 1954 psychophysics result becomes a pointing-device design tool by 1992.

**hick1952rate**
Hick, W. E. (1952). On the rate of gain of information. *Quarterly Journal of Experimental Psychology, 4*(1), 11–26.
DOI: 10.1080/17470215208416600 · Basis: Crossref; OpenAlex abstract · Status: **abstract only**.
Hick applied information theory to choice reaction time, with up to ten alternatives. His principal finding is that the rate of gain of information is roughly constant within one perceptual-motor act, at "of the order of five 'bits' per second" (abstract). Reaction-time distributions tracked the objective uncertainty of the response.
**Role:** UX-cognitive-foundation (choice cost; the ancestor of "fewer options" heuristics).

**hyman1953stimulus**
Hyman, R. (1953). Stimulus information as a determinant of reaction time. *Journal of Experimental Psychology, 45*(3), 188–196.
DOI: 10.1037/h0056940 · Basis: Crossref; OpenAlex abstract (an opening-paragraph excerpt) · Status: **abstract only**.
The excerpt frames Merkel's finding, that reaction time rises with the number of equally probable alternatives, in communication-theory terms, where information grows with the number of possible messages. Hick and Hyman together give the "Hick–Hyman law"; I did not read Hyman's results.
**Role:** UX-cognitive-foundation.

**dewinter2014fitts**
de Winter, J. C. F., & Dodou, D. (2014). Why the Fitts list has persisted throughout the history of function allocation. *Cognition, Technology & Work, 16*(1), 1–11. (Online 2011.)
DOI: 10.1007/s10111-011-0188-1 · Basis: Crossref; OpenAlex; full text from the TU Delft repository (OA, CC) · Status: **read in full**.
De Winter and Dodou reproduce the original Fitts (1951, p. 10) list as their Table 1 (p. 2). It has 11 statements: humans surpass machines at detection, pattern perception, improvisation, long-term storage and recall, inductive reasoning and judgment, and machines surpass humans at speed and force, routine repetition, brief storage, deductive computation and multitasking. They argue that the list meets six criteria for appraising theories, from plausibility to generalisability, even after heavy criticism, including Jordan's 1963 complementarity and Dekker and Woods's 2002 attack (pp. 3–6). They also show that the 1951 report anticipated the "ironies of automation" (p. 7). On p. 7 they quote the 1951 report's forecast (its p. 5) that, if machines take over the major work, research on human functions would centre on "reasoning, judgment, planning, and decision making."
**Role:** precursor. The founding document of human factors already names decision making as the residual human function once machines take over the work, which is the hinge of the DXD argument.

### Cognitive HCI: the information-processing wave

**card1980keystroke**
Card, S. K., Moran, T. P., & Newell, A. (1980). The keystroke-level model for user performance time with interactive systems. *Communications of the ACM, 23*(7), 396–410.
DOI: 10.1145/358886.358895 · Basis: Crossref; OpenAlex (flagged OA via ACM); CACM metadata page viewed · Status: **not accessible** (ACM DL behind a bot challenge; browser extension denied).
The record confirms venue, pages and date. Operator times and prediction-error figures are **not** reported here because I could not read the paper. They must be taken from the source before anyone cites them.
**Role:** UX-cognitive-foundation. The keystroke is the unit.

**card1983psychology**
Card, S. K., Moran, T. P., & Newell, A. (1983). *The psychology of human-computer interaction*. Lawrence Erlbaum. (Reissued 2018, CRC Press.)
DOI (2018 reissue): 10.1201/9780203736166 · Basis: Crossref book and chapter records, which confirm the chapters "The Human Information-Processor" (pp. 23–97), "The Keystroke-Level Model" (pp. 259–311) and "Applying Psychology to Design" (pp. 403–424) · Status: **not accessible**.
Harrison, Tatar and Sengers (2007, ms. p. 4; read) describe the book as starting from the premise that human information processing is "deeply analogous" to computational signal processing, so that modelling both person and computer lets designers "predict and optimize the relationship." The chapter titles confirm that the Model Human Processor and the KLM sit in the same volume as a chapter on applying psychology to design.
**Role:** UX-cognitive-foundation. It is the canonical statement that cognitive psychology should *be* the science of interface design.

**norman1986cognitive**
Norman, D. A. (1986). Cognitive engineering. In D. A. Norman & S. W. Draper (Eds.), *User centered system design: New perspectives on human-computer interaction* (pp. 31–62). Lawrence Erlbaum.
DOI: 10.1201/b15703-3 (volume: 10.1201/b15703) · Basis: Crossref chapter record · Status: **not accessible**.
The record confirms the chapter and volume. Hutchins, Hollan and Norman (1985, p. 311 footnote; read) state that a version of their paper appears in the same volume. Their paper carries the gulfs of execution and evaluation (next entry), so the gulfs reached the 1986 volume by that route. I did not verify the wording of Norman's own chapter.
**Role:** UX-cognitive-foundation (the naming of "cognitive engineering" and user-centred design).

**hutchins1985direct**
Hutchins, E. L., Hollan, J. D., & Norman, D. A. (1985). Direct manipulation interfaces. *Human–Computer Interaction, 1*(4), 311–338.
DOI: 10.1207/s15327051hci0104_2 · Basis: Crossref; full text from Hollan's author page (hci.ucsd.edu/hollan/Pubs/direct-manip.pdf) · Status: **read in full**.
The authors seek "a cognitive account" of direct manipulation (abstract, p. 311). They define distance as the gulf of execution, running from goals to system state, and the gulf of evaluation, running from system state back to goals. Execution is bridged by matching commands to the user's goals. Evaluation is bridged by displays that present "a good conceptual model" of the system. Both bridges aim "to minimize cognitive effort" (p. 318; Fig. 3, p. 319). Two qualifications matter for DXD. First, automated skill makes an interface *feel* direct without reducing semantic distance (pp. 326–327). Second, the authors warn against equating directness with ease of use. If the interface is "really invisible," difficulties in the task domain pass straight to the user (p. 336).
**Role:** UX-cognitive-foundation. It is also a precursor of algorithmacy's "specifying intent" and "interpreting," because the gulfs *are* specification and interpretation, but against a deterministic system whose state the display can model.

**norman2013design**
Norman, D. A. (2013). *The design of everyday things* (Rev. and exp. ed.). Basic Books. (First published 1988 as *The psychology of everyday things*.)
Basis: OpenAlex W2613049552 (2013 ed.) and W139507382 (1988 ed.); Crossref has only reviews and a 2016 German edition (10.15358/9783800648108) · Status: **not accessible**.
The records confirm both editions. The concepts the task names (affordances, signifiers, mental and conceptual models) are **not** described here from the book. A related verified record is Norman (1999), "Affordance, conventions, and design," *Interactions 6*(3), 38–43, DOI 10.1145/301153.301168, which I did not read (see Gaps).
**Role:** UX-cognitive-foundation (popular transmission of cognitive engineering to designers).

**norman1990problem** (existing card)
Norman, D. A. (1990). The "problem" with automation: Inappropriate feedback and interaction, not "over-automation." *Philosophical Transactions of the Royal Society of London B, 327*(1241), 585–593.
DOI: 10.1098/rstb.1990.0101 · Basis: repo card `submissions/algorithmacy_design_ethics/literature/library/norman1990.md` (built from the 1989 ICS Report 8904 preprint; S2 adversarial verification "confirmed") · Status: **read in full** (per card; preprint pagination).
The card documents Norman's diagnosis that "the culprit is not actually automation, but rather the lack of feedback" (preprint p. 5). He explains the missing feedback by the fact that the automation itself does not need it (p. 7). His three cases are aviation incidents in which an autopilot silently compensated for a fault.
**Role:** precursor. The cognitive engineer who defined the gulfs extends them to an opaque automated intermediary and prescribes feedback, which is a legibility remedy. The design-ethics arm flags that remedy as a literacy-paradigm move.

### Memory, load, and the Miller caution

**miller1956magical**
Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97.
DOI: 10.1037/h0043158 · Basis: Crossref; OpenAlex; Consensus record · Status: **abstract only** (Consensus excerpt of the closing passages).
In the closing passages, Miller holds that recoding into chunks lets people "break (or at least stretch)" the informational bottleneck. He withholds judgment on the recurring sevens, suspecting "a pernicious, Pythagorean coincidence." For what the paper reports (absolute judgment, memory span, subitizing), see Cowan 2015 below, who read it closely.
**Role:** UX-cognitive-foundation, and the source of the field's best-known misuse.

**cowan2001magical**
Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87–114 (with commentaries to p. 185).
DOI: 10.1017/s0140525x01003922 · Basis: Crossref; OpenAlex (OA via Cambridge) · Status: **partial** (full PDF retrieved; abstract, §1 and §5 Conclusion read).
The abstract says Miller's seven was "more as a rough estimate and a rhetorical device than as a real capacity limit." Under conditions that block rehearsal and chunking, a single central limit "averaging about four chunks" appears. The Conclusion (p. 114) gives a mean adult capacity of "three to five chunks," with individual scores from about two to about six, and treats 7 ± 2 as a valid *compound* limit for material that allows rehearsal and chunking. Several BBS commentaries dispute a fixed item limit. One commentary on p. 114 argues that the data reflect memory for events, not items.
**Role:** counterevidence to the folk UX reading of Miller; UX-cognitive-foundation (working-memory limit).

**cowan2015george**
Cowan, N. (2015). George Miller's magical number of immediate memory in retrospect: Observations on the faltering progression of science. *Psychological Review, 122*(3), 536–541.
DOI: 10.1037/a0039035 · Basis: Crossref; Europe PMC (PMC4486516, author manuscript) · Status: **read in full** (PMC HTML; no page numbers, so section locators are given).
In "Description of Miller (1956)," Cowan separates Miller's three limits: absolute judgment (about 5 to 9 categories), memory span (about 7 items), and subitizing. He argues that the chunk concept, not the number, "may be the most important specific contribution." He quotes a 2000 email in which Miller says he revisited the paper only when someone "over-generalized the conclusions," and says Miller "was stuck with 7" because of the absolute-judgment results. In "The Case for Returning…," Cowan puts the limit for items attended all at once at "about 3 for adults."
**Role:** counterevidence / cautionary tale. Miller himself disowned the over-generalization that UX folklore rests on.

**commarford2008comparison**
Commarford, P. M., Lewis, J. R., Smither, J. A.-A., & Gentzler, M. D. (2008). A comparison of broad versus deep auditory menu structures. *Human Factors, 50*(1), 77–89.
DOI: 10.1518/001872008x250665 · Basis: Crossref; OpenAlex; Consensus abstract · Status: **abstract only** (a UCF repository copy exists but I did not retrieve it).
The authors target the widely promoted interactive-voice-response guideline of five or fewer menu items, which is "commonly citing Miller's (1956) paper," and argue that Miller does not support it. In their experiment, users of a broad-structure IVR "performed better and were more satisfied" than users of a deep one. The effect was stronger for participants with low working-memory capacity (abstract).
**Role:** counterevidence. A guideline derived from a misread cognitive finding produced the opposite of the intended effect.

**doumont2002magical**
Doumont, J.-L. (2002). Magical numbers: The seven-plus-or-minus-two myth. *IEEE Transactions on Professional Communication, 45*(2), 123–127.
DOI: 10.1109/tpc.2002.1003695 · Basis: Crossref (volume and pages); OpenAlex; Consensus abstract · Status: **abstract only**.
Doumont reports that professional-communication specialists typically cite Miller for "seven" without having read the paper, "quoting it out of context." He re-reads Miller to put the limit in perspective (abstract).
**Role:** counterevidence. It documents the practitioner misuse.

**sweller2019cognitive**
Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292.
DOI: 10.1007/s10648-019-09465-5 · Basis: Crossref; OpenAlex abstract (OA, but the Springer, figshare and EUR copies were unretrievable by script) · Status: **abstract only**. Related records: Sweller 1988 (10.1207/s15516709cog1202_4, abstract read) and Sweller et al. 1998 (10.1023/a:1022193728205, metadata only).
The 2019 abstract says that cognitive load theory holds that all novel information is first processed by a "capacity and duration limited working memory" and then stored in an unlimited long-term memory, after which those limits "disappear." It also says that instructional design had previously proceeded as though working memory did not exist. In the 1988 abstract, Sweller argues that means-ends problem solving consumes processing capacity that is then "unavailable for schema acquisition."
**Role:** UX-cognitive-foundation (the load construct UX borrowed). Its home domain is instruction, not interfaces.

**hollender2010integrating**
Hollender, N., Hofmann, C., Deneke, M., & Schmitz, B. (2010). Integrating cognitive load theory and concepts of human–computer interaction. *Computers in Human Behavior, 26*(6), 1278–1288.
DOI: 10.1016/j.chb.2010.05.031 · Basis: Crossref; OpenAlex; Consensus abstract · Status: **abstract only**.
Searching the ACM Guide, the authors found 65 publications with "cognitive load" in the title or abstract and concluded that CLT concepts "have been adopted in HCI," though germane load received less attention. Their first model splits extraneous load into load from instructional design and load "caused by software usage."
**Role:** UX-cognitive-foundation. It gives direct evidence of the import, and shows that the imported construct locates interface cost as *extraneous* load.

### Reading, perception, haptics

**buscher2009what**
Buscher, G., Cutrell, E., & Morris, M. R. (2009). What do you see when you're surfing? Using eye tracking to predict salient regions of web pages. In *Proceedings of CHI 2009* (pp. 21–30). ACM.
DOI: 10.1145/1518701.1518705 · Basis: Crossref; OpenAlex abstract · Status: **abstract only** (not OA).
The authors tracked the eyes of 20 users viewing 361 web pages under information-foraging and page-recognition tasks. They describe location-based attention characteristics that depend on task and demographics, and they propose a predictive model plus a "fixation impact" mapping method (abstract).
**Role:** UX-cognitive-foundation. The screen or page is the unit.

**pernice2017fshaped** (grey)
Pernice, K. (2017, November 12). *F-shaped pattern of reading on the web: Misunderstood, but still relevant (even on mobile)*. Nielsen Norman Group. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ (page "last reviewed" 19 Aug 2026).
Basis: WebFetch of the live page (the WebFetch summary gave the quotations; I did not check them against page source) · Status: **read in full** (web article). The original 2006 Nielsen article was not retrieved.
Pernice revisits the 2006 finding. The F-pattern appears when text has little or no web formatting, the user is seeking efficiency, and the user is not committed enough to read everything. She presents it as a pattern to *design against*, since F-scanners "miss big chunks of content." She names alternative patterns (layer-cake, spotted, marking, bypassing, commitment) and cites samples such as 47 participants in one study.
**Role:** UX-cognitive-foundation, with a caution. The best-known "how people read the web" finding is conditional on bad formatting, not a law of reading.

**dyson2004how**
Dyson, M. C. (2004). How physical text layout affects reading from screen. *Behaviour & Information Technology, 23*(6), 377–393.
DOI: 10.1080/01449290410001715714 · Basis: Crossref; OpenAlex abstract · Status: **abstract only**.
Dyson critically reviews studies of line length, columns, window size and interlinear spacing on screen. Her synthesis identifies "the number of characters per line as the critical variable" for line length and calls for studies of its interaction with eye movements and scrolling (abstract).
**Role:** UX-cognitive-foundation (typographic reading research transferred to screens).

**healey2012attention**
Healey, C. G., & Enns, J. T. (2012). Attention and visual memory in visualization and computer graphics. *IEEE Transactions on Visualization and Computer Graphics, 18*(7), 1170–1188.
DOI: 10.1109/tvcg.2011.127 · Basis: Crossref; OpenAlex abstract · Status: **abstract only**.
The authors survey attention and visual-perception research "with direct relevance to visualization." They build from low-level perception theories (preattentive processing among them, per the paper's framing) to visual memory and attention, and they note that visualization problems now drive psychophysics research. That feedback runs from design back to science.
**Role:** UX-cognitive-foundation (the glance/preattentive unit).

**maclean2008haptic**
MacLean, K. E. (2008). Haptic interaction design for everyday interfaces. *Reviews of Human Factors and Ergonomics, 4*(1), 149–194.
DOI: 10.1518/155723408x342826 · Basis: Crossref; OpenAlex abstract · Status: **abstract only**.
MacLean orients novice designers to haptics by integrating "human capabilities" with device technology. She relates perceptual, motor and attentional capabilities to notification, GUI augmentation, expressive control, affective communication, and mobile use (abstract).
**Role:** UX-cognitive-foundation (touch channel).

### Historiography: the field reorganizes when its object changes

**grudin1990computer**
Grudin, J. (1990). The computer reaches out: The historical continuity of interface design. In *Proceedings of CHI '90* (pp. 261–268). ACM. (Also DAIMI PB-299, Aarhus University, Dec. 1989.)
DOI: 10.1145/97243.97284 · Basis: OpenAlex W2158035776; Crossref (pages); full text of DAIMI PB-299 (tidsskrift.dk, OCR'd) · Status: **read in full** (DAIMI report version; pdf-page locators).
Grudin tracks the interface moving "farther and farther out from the computer" through five foci: hardware, software, terminal, dialogue, and work setting. "As the focus shifts," he writes, "the skills required of practitioners" change (abstract). His Table 1 (pdf p. 11) is the closest thing in the literature to a history of *units*. It gives each level's principal users, specialist disciplines (level 3: human factors, cognitive psychology, graphic design; level 4: cognitive psychology, cognitive science, "dramatic arts?"; level 5: social psychology, anthropology, organizational science), methods (laboratory experiment → think-aloud and Wizard of Oz → ethnography), and "duration of basic events studied" (microseconds/hours, milliseconds/hours, seconds, minutes, days). Each level has its own practitioners and rests on a "less mature" science base (Summary).
**Role:** term-use / precursor. It gives the strongest documentary support for the thesis that design expertise reorganizes around a new unit when the interface moves outward.

**harrison2007three**
Harrison, S., Tatar, D., & Sengers, P. (2007). The three paradigms of HCI. *alt.chi, CHI 2007*. ACM. (No DOI.)
Basis: Consensus record (628 citations); full text from CiteSeerX, a manuscript marked "NOT FOR CIRCULATION" · Status: **read in full** (manuscript pagination; check wording against the alt.chi version before quoting). Successor paper verified: Harrison, Sengers & Tatar (2011), *Interacting with Computers 23*(5), 385–392, DOI 10.1016/j.intcom.2011.03.005.
Following Agre, the authors trace paradigm shifts through changes in the central "metaphor of interaction" (ms. p. 2). Human factors treats interaction as "man-machine coupling" and seeks to optimize fit (p. 3). Classical cognitivism treats mind and computer as "coupled information processors," with Card, Moran and Newell as its premise (p. 4). The third paradigm treats interaction as "phenomenologically situated" meaning-making (p. 6). Each paradigm carries its own questions and criteria for knowledge (p. 14).
**Role:** term-use / precursor (reorganization of the field's object).

**hollan2000distributed**
Hollan, J., Hutchins, E., & Kirsh, D. (2000). Distributed cognition: Toward a new foundation for human-computer interaction research. *ACM Transactions on Computer-Human Interaction, 7*(2), 174–196.
DOI: 10.1145/353485.353487 · Basis: Crossref; author "final revision" at hci.ucsd.edu (dated 23 Apr 2000) · Status: **read in full** (manuscript pagination).
The authors argue that HCI is leaving the single-computer desktop for "a complex networked world" (abstract). Their first principle concerns "the boundaries of the unit of analysis": traditionally those of individuals, but cognitive processes should be located by the "functional relationships" among participating elements (ms. p. 2). They name three distributions: across group members, between internal and external structure, and through time (p. 3).
**Role:** precursor. HCI's own theorists already proposed moving the unit past the individual to a coordinating system, the move DXD makes for algorithmically mediated coordination.

**bodker2015third**
Bødker, S. (2015). Third-wave HCI, 10 years later—participation and sharing. *Interactions, 22*(5), 24–31.
DOI: 10.1145/2804405 · Basis: Crossref; OpenAlex; Consensus full-text excerpt (ACM OA copy blocked) · Status: **abstract only** (Consensus excerpt of the opening). Related verified record: Bødker (2006), NordiCHI keynote, DOI 10.1145/1182475.1182476 (abstract read).
In the excerpt, Bødker characterizes the first wave as "cognitive science and human factors," model-driven and built on formal methods and systematic testing. The second wave centres on groups in work settings, drawing on situated action, distributed cognition and activity theory. In the third wave, use spreads beyond the workplace.
**Role:** term-use (wave historiography).

**chignell2023evolution**
Chignell, M., Wang, L., Zare, A., & Li, J. J. (2023). The evolution of HCI and human factors: Integrating human and artificial intelligence. *ACM Transactions on Computer-Human Interaction, 30*(2), 1–30. (Crossref: issued 17 Mar 2023; OpenAlex dates it 2022.)
DOI: 10.1145/3557891 · Basis: OpenAlex (found by snowball: cites Grudin 1990) · Status: **abstract only** (closed).
The authors review HCI's 1980s split from human factors. They propose human augmentation, rather than user friendliness, as the frame for human-AI interaction, which raises trust and situation awareness. They call for HCI and human factors to rejoin to meet AI's challenges (abstract).
**Role:** competing-construct / precursor. It is the field's own proposal for the post-AI reorganization, framed as augmentation, not as a new cognitive competence of the user.

**forlizzi2018moving**
Forlizzi, J. (2018). Moving beyond user-centered design. *Interactions, 25*(5), 22–23.
DOI: 10.1145/3239558 · Basis: OpenAlex; Crossref (volume and pages); Semantic Scholar and Consensus text excerpt · Status: **abstract only** (excerpt).
Forlizzi argues for "stakeholder-centered design," saying "we are no longer designing one thing for one person." She simplifies the histories (Harrison et al.; Grudin) into three lenses: human factors, user-centred design, and user experience design.
**Role:** competing-construct. It moves the unit from one user to many parties, close to DXD's coordination framing, but without a cognitive account of what each party must do.

### The profession

**iso2019hcd** (standard; grey)
International Organization for Standardization. (2019). *Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems* (ISO Standard No. 9241-210:2019, 2nd ed.).
Basis: WebSearch result summarizing the iso.org catalogue page (iso.org returned 403 to direct fetch) · Status: **not accessible** (paywalled standard).
The catalogue text describes human-centred design as making systems usable "by focusing on the users" and "applying human factors/ergonomics, and usability knowledge and techniques." The standard runs to 33 pages, and edition 2 was published July 2019.
**Role:** UX-cognitive-foundation (institutionalization). The international standard makes human-factors knowledge constitutive of the design process.

**gonzalez2014perspectives**
González, C. A., Ghazizadeh, M., & Smith, M. (2014). Perspectives on the training of human factors students for the user experience industry. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 58*(1), 1807–1811.
DOI: 10.1177/1541931214581378 · Basis: OpenAlex; Crossref (volume and pages); Consensus abstract · Status: **abstract only**.
In a survey of 140 HFES student members, "nearly 80%" were considering a UX career, but "only 12%" felt extremely well prepared. In 40 UX job postings, 37% of requirements emphasized design familiarity and programming (abstract).
**Role:** counterevidence (partial). Industry UX hiring weighs design and programming heavily, so human-factors knowledge is necessary but not sufficient, and not the whole job.

**lallemand2015user**
Lallemand, C., Gronier, G., & Koenig, V. (2015). User experience: A concept without consensus? Exploring practitioners' perspectives through an international survey. *Computers in Human Behavior, 43*, 35–48.
DOI: 10.1016/j.chb.2014.10.048 · Basis: Crossref (volume and pages); Semantic Scholar abstract · Status: **abstract only** (OA copy in ORBilu not retrieved).
The authors surveyed 758 UX professionals from 35 nationalities. Understanding of UX varied with domain, role, language and seniority, and respondents wanted a definition that translates into practice (abstract).
**Role:** counterevidence (partial). The profession's self-definition is unsettled, so "UX = applied cognitive psychology" is one view among several.

---

## (c) Thematic synthesis

**The import is real, and it was an import of units.** Every wave of HCI knowledge I verified took a cognitive finding measured at one grain and turned it into a design rule at the same grain. Fitts's law and Hick's rate of information gain made the *keystroke and pointing movement* the object of design. MacKenzie shows that the transfer ran from 1954 psychophysics to mouse and trackball evaluation by 1992. Card, Moran and Newell then built a whole science on that grain, and Harrison, Tatar and Sengers identify their information-processing premise as the second paradigm of HCI. Perceptual research moved the unit up to the *glance*: preattentive features and visual attention in Healey and Enns, eye-tracked page regions in Buscher and colleagues, characters per line in Dyson. Cognitive load theory and the gulfs of execution and evaluation moved it again, to the *task*. Hutchins, Hollan and Norman define interface quality as the cognitive effort needed to carry a goal into system state and back. Hollender and colleagues show that HCI absorbed CLT by recasting software friction as extraneous load.

**Grudin makes the unit explicit.** His 1990 Table 1 lists, for each level of interface focus, the duration of the basic event studied: milliseconds for the terminal, seconds for perceptual-motor work, minutes for dialogue, days for the work setting. It also pairs each level with a new specialist discipline and a new method. This table is the best single warrant for the thesis's historical claim, and it supports the *general* form of that claim, not only the UX case. The field's practitioners and knowledge base change whenever the interface "reaches out" to a new object. Harrison and colleagues, Bødker, and Hollan and colleagues tell the same story as paradigms, waves and units of analysis. Hollan, Hutchins and Kirsh insist that functional relations, not the skin, set the unit's boundary.

**The historiography disagrees about what drives the change, and where it ends.** Grudin reads each outward step as the computer colonizing its environment, with a science base that grows weaker at every level. Harrison and colleagues read the third paradigm as a change of epistemology, from optimization to meaning-making, not a new object at the same epistemology. Chignell and colleagues argue that AI calls for a reunion of HCI with human factors under an "augmentation" frame. Forlizzi argues it calls for stakeholder-centred design. Two rival constructs — augmentation, and stakeholder-centred design — already claim the post-AI reorganization, and neither makes the *user's* interpretive competence the object of expertise.

**The cautionary tale is also real.** Cowan (2001, 2015) shows that Miller's seven was partly rhetorical: the defensible limit for unchunked items is three to five, and Miller himself complained of over-generalization. Doumont documents practitioners quoting Miller unread. Commarford and colleagues show that a Miller-derived menu guideline made performance *worse*, especially for low-capacity users. Pernice's revision of the F-pattern makes the same point about reading, since the pattern is a symptom of unformatted text, not a law. Imported cognitive findings became design folklore when practitioners detached them from their boundary conditions. DXD should build that lesson in from the start.

**Does a decision in algorithmically mediated coordination qualify as the next unit?** On Grudin's criteria, plausibly yes. It has a distinct duration: a decision whose consequences unfold over days to months as the intermediary adapts. It involves a new principal-user configuration, since two parties coordinate through a system that reads both. And it has an immature science base. Two findings sharpen the case. The 1951 Fitts report, as de Winter and Dodou quote it, already predicted that once machines did the major work, human-factors research would centre on "reasoning, judgment, planning, and decision making." Hutchins, Hollan and Norman warned that an invisible interface passes task-domain difficulty straight to the user. Yet every prior unit assumed an intermediary whose state a display could *model* (the gulf of evaluation), and Norman's 1990 remedy for opaque automation was more feedback. That is the literacy-paradigm move the design-ethics arm rejects. So the historical pattern supports a new unit, but it does not show that the new unit can be served by the old remedy. That gap is the DXD argument's burden, not its premise.

---

## (d) Gaps and unverified leads

**Verified records, content not read (do not cite for content until read).**
- Card, Moran & Newell (1980) KLM: operator times and accuracy figures are unread; try the ACM open-archive PDF from a non-scripted browser.
- Fitts (1954); Treisman & Gelade (1980), DOI 10.1016/0010-0285(80)90005-5, 12,543 citations; Sweller et al. (1998); Norman (1986) "Cognitive engineering"; Norman (1988/2013); Norman (1999) "Affordance, conventions, and design," DOI 10.1145/301153.301168. The 1999 piece is the natural companion to the Miller caution, since it is Norman's own complaint about designers' misuse of "affordance"; a course-hosted copy exists at cseweb.ucsd.edu but is not author-posted.
- Grudin (2005) "Three faces of human-computer interaction," *IEEE Annals 27*(4), 46–62, DOI 10.1109/mahc.2005.67 (abstract: three foci of computer operation, information-systems management, discretionary use). Grudin (2012), "A moving target," Handbook intro, DOI 10.1201/b11963-ch-101. Grudin (2017), *From tool to partner*, DOI 10.1007/978-3-031-02218-0. All closed; the 2017 book's title alone signals the tool→partner shift and deserves a full read.
- Carroll (1997), *Annual Review of Psychology 48*, 61–83, DOI 10.1146/annurev.psych.48.1.61 (abstract read: HCI "progressively integrated" psychology with the engineering goal of usability). A strong candidate entry if F-series needs one more import source.
- Hassenzahl & Tractinsky (2006), DOI 10.1080/01449290500330331 (abstract read: UX as a move beyond products-as-tools).
- Oviatt (2006), DOI 10.1145/1180639.1180831 (abstract read: human-centred design minimizing cognitive load). Pan et al. (2004), DOI 10.1145/968363.968391 (abstract read: 30 subjects, 22 pages; task instruction had no significant effect on viewing).
- Newell & Card (1985) and Carroll & Campbell (1986), DOIs 10.1207/s15327051hci0103_1 and 10.1207/s15327051hci0203_3: the "hard science" debate over whether psychology can be HCI's science. This is highly relevant to the DXD analogy and unread.
- Petrick (2020), "A historiography of HCI," DOI 10.1109/mahc.2020.3009080 (abstract read; says there is no consensus on what HCI or an interface is).
- Bannon (1991/1995), "From human factors to human actors," DOI 10.1016/b978-0-08-051574-8.50024-8.

**Not found / not verified.**
- Fitts (1951) report: no DOI record; known only through de Winter & Dodou's quotations and Table 1.
- Nielsen (2006) original F-pattern article: not retrieved; only the 2017 Pernice revisit was read.
- Ware, *Information Visualization: Perception for Design*: only chapter DOIs from the 2004, 2013 and 2021 editions surfaced (e.g., 10.1016/b978-0-12-381464-7.00007-7); no book-level record retrieved.
- ISO 9241-210 full text: paywalled; catalogue text only.

**Practitioner-competency evidence is thin and mixed.** OpenAlex returned 0 for the most direct query. The Consensus hits (Winter et al. 2024, 25 UX-manager interviews, DOI 10.1145/3670653.3670656; Rose et al. 2020, 71 senior professionals, DOI 10.1145/3380851.3416774; Branch et al. 2021, 34 degree courses and 50 UK job adverts, DOI 10.1080/14606925.2021.1930935; Gray 2014, DOI 10.1145/2556288.2557264; Inal et al. 2020, 422 professionals, no DOI found) mostly stress methods, communication and business skills over cognitive psychology. A Consensus-listed book blurb for Johnson (2010) *Designing with the Mind in Mind* claims "early UI practitioners were trained in cognitive psychology" (no DOI; the related 2021 CHI course is DOI 10.1145/3411763.3444997). **I found no study that measures cognitive-psychology knowledge as a core competence of working UX practitioners.** The thesis's claim that UX professionals *became experts in* cognition rests on historiography and on standards like ISO 9241-210, not on competency surveys. Surveys (González et al. 2014) cut partly against it.

**Snowball leads for other facets.**
- Binns (2022), "Human judgment in algorithmic loops," *Regulation & Governance 16*(1), 197–211, DOI 10.1111/rego.12358 (OA; cites de Winter & Dodou). It links the Fitts-list tradition to human-in-the-loop algorithmic decision-making.
- Dekker & Woods (2002), DOI 10.1007/s101110200022, critique of MABA-MABA.
- The existing `christoffersenwoods2002.md` card (observability/directability) in `algorithmacy_design_ethics`.

**Tool failures to note.** Scholar Gateway returned an identity error on its first call and was not used. ACM DL and Springer blocked scripted downloads throughout, which explains the high abstract-only share among ACM-published entries.
