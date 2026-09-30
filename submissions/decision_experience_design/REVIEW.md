# Decision Experience Design: The Term, Its Precursors, and the Case for Algorithmacy Expertise

*[Draft 1, 2026-09-30. Written by Claude from the seven facet files in `literature/facets/` for the
author to revise and read aloud. Every citation resolves to `literature/references.bib`; each entry's
verification basis and read status sit in its facet file. Two author rulings govern the argument
(README): algorithmacy is not legibility, and the literacy→algorithmacy move is argued on the numeracy
model, not Ong's.]*

### Abstract

Since 2023, practitioners have begun calling their work "decision experience design," yet the phrase
has no scholarly footprint: I found no use of it in OpenAlex, Crossref, arXiv or Consensus. The label
has outrun its theory. In this review I trace the three literatures that already design decisions
under other names — choice architecture, decision support and cognitive systems engineering, and the
human–AI decision research of the last decade — and set them beside the history of how user
experience design became a cognitive profession. Each wave of interface knowledge took a new unit of
analysis, and a decision committed through an adaptive, opaque intermediary is plausibly the next
one. The cognitive problems at that unit differ from reading, load and perception:
people must interpret an intermediary whose rule they cannot see, specify intent through channels it
permits, and keep track of it as it changes. On the model the numeracy literature supplies, the
competence those problems demand — algorithmacy — should predict decision quality beyond general
ability, and decision experience designers should be expert in it. The evidence also shows what
that expertise is not: making the algorithm legible raises awareness without raising agency.

### Introduction

A product designer in Indonesia named the problem in December 2025. Ajeng Restu Putri's learning
platform for teachers had an activation rate stuck at 14.8%; her team removed a free trial and cut the entry price, activation rose to 50.6%, and she wrote that "[t]his was a decision experience design problem" (Putri,
2025). Five other practitioners and organizations used the phrase, or the acronym DX for "decision experience," between September 2023 and September 2026, one of them on an undated page (Audry, n.d.; Danish-Swiss Chamber of Commerce, 2026; Itera, 2025; Pastagia, 2026; Wilkinson, 2023). Only one of them, the Chilean consultancy Itera, cites any of the others — Magine Pro and Audry — and Itera concedes that the practice "carece aún de un framework
sólido equiparable a UX" — still lacks a framework comparable to user experience design's (Itera,
2025).

The scholarly record is empty. I found no use of "decision experience design" in OpenAlex, Crossref,
arXiv, or six Consensus searches, and the Semantic Scholar queries that completed returned none
(SEARCH_LOG.md). That silence does not mean the work is new. Designers, engineers and behavioural
scientists have designed the conditions of decisions for seventy years under other names, and a
review has to start by giving those names their due.

My argument has two halves. The first is historical. User experience design (UXD) became a profession
by importing findings from cognitive science and human factors — how quickly a hand reaches a target,
where an eye lands on a page, how much a person can hold in working memory — and turning each into a
design rule at the same grain. The field reorganized each time its object moved outward, from the
keystroke to the glance to the task to the work setting. The second half is prospective. When
coordination runs through an algorithm that reads both parties and commits decisions neither
controls, the object moves again, to the decision, and the cognitive problems that come with it are
not the ones UX learned to solve. The lab calls the competence those problems demand *algorithmacy*.
Decision experience design (DXD) is the practice that should be expert in it, the way UXD was expert
in reading and perception.

Two qualifications bound the argument. The claim is not that algorithmic mediation restructures
human cognition the way Ong (1982/2002) said writing did. It is the narrower claim that numeracy research
has already made good for numbers (Peters et al., 2006; Reyna & Brainerd, 2023): a competence can
predict the quality of decisions made through a medium, and that prediction can be tested. Nor is algorithmacy expertise skill at
making algorithms legible. The evidence reviewed below shows legibility raising awareness while
leaving agency unchanged, and the lab's design-ethics arm draws the design consequence.

The review proceeds in seven steps. I first survey the term and its near-synonyms, then two precursor
literatures, choice architecture and cognitive systems engineering. I then establish the left side of
the analogy, how UX became a cognitive profession, and the right side, the cognition of deciding
through an intermediary. The sixth step introduces algorithmacy on the numeracy model and separates it
from its rivals; the seventh argues that expertise in it is not legibility expertise. A gap check and
an agenda close the review.

**How I searched.** Seven facet searches ran on 30 September 2026 against OpenAlex, Crossref,
Semantic Scholar, arXiv and Consensus, with web fetches for grey literature, after a check of the
lab's existing card libraries (roughly 2,000 verified cards across its arms). The merged bibliography
holds 201 entries, each backed by a database record retrieved that day or by an existing verified
card; the facet files mark each entry read in full, read in part, abstract only, or not accessible.
Two tools failed: Scholar Gateway returned an identity error throughout, and Semantic Scholar's rate
limits cost six of twelve queries in the term search. The full log is in `SEARCH_LOG.md`.

### The Term and Its Near-Synonyms

**The practitioner uses point two ways.** Four face outward, at a customer choosing. Matthew
Wilkinson, CEO of Magine Pro, located the streaming problem in the menu, where "the more choices we
have, the harder it is to decide," and proposed "focusing on the Decision Experience (DX) through
UX/UI design choices" (Wilkinson, 2023). Putri's redesign, Keyur Pastagia's LinkedIn post ("That's no
longer UX. That's Decision Experience (DX).") and a Danish-Swiss Chamber of Commerce evening on "how
technology, AI and decision experience design are reshaping the future of decision-making" share the
outward orientation (Danish-Swiss Chamber of Commerce, 2026; Pastagia, 2026; Putri, 2025). Two face
inward. Andrew Audry defines the practice as creating "the logic and structure that makes internal
choices system-ready," and Itera defines DX as "el diseño deliberado del momento de decisión," the
deliberate design of the decision moment, measured by time-to-decision (Audry, n.d.; Itera, 2025).
Rupashree (2026) makes the same inward move under the name decision architecture.

**Four scholarly literatures already claim the decision as design's unit, and each puts a different
person at it.** *Decision-centered design* dates at least to Wolf, Klein and Thordsen (1991), who proposed that "decisions central to a task" should "serve as the focus of the design," with requirements elicited from decision makers by critical-decision interviews (see also O'Hare et al., 1998); the method reached the human-factors handbooks by 2003 and 2013 (Hutton et al., 2003; Militello & Klein, 2013). Its person is the expert operator. *Choice architecture* puts a benevolent human architect
in charge (Johnson et al., 2012; Thaler & Sunstein, 2008), and *digital nudging* makes the interface
designer that architect (Schneider et al., 2018; Weinmann et al., 2016). *Decision intelligence*
centres the organization, as process-and-decision modelling in peer-reviewed work and as a
data-to-action discipline in trade writing (Hasić et al., 2018; Pratt, 2019). The *consumer decision
journey* maps the firm's view of a buyer's path, and its own reviewers noted in 2021 that the effect
of AI on that path was untheorized (Santos & Gonçalves, 2021).

Psychology uses the phrase too, for something narrower. Peterson and Cheng (2022) treat *decision
experience* as the chooser's felt difficulty and satisfaction after a choice. Hyperchoice — sixteen
options against four — raised decision difficulty, and numeracy moderated the effect in a gamble task.
That construct gives DXD a measurable outcome and, in passing, a first instance of the argument this
review makes: a competence changed how a decision environment was experienced.

**The nearest precursor by name is algorithmic experience.** Oscar Alvarado Rodríguez's thesis proposed that the
concept "should be opened to all kinds of technologies … that affect the user experience through the
decisions and interventions of non-human actors" (Alvarado Rodríguez, 2017, p. 10), and Alvarado and Waern
(2018) carried it to CHI as five functional categories: profiling transparency and management,
algorithmic awareness and control, and selective algorithmic memory. Shin, Zhong and Biocca (2020)
titled their follow-up "beyond user experience." The move is the DXD move in name. The categories,
however, are remedies that make the algorithm visible and adjustable to one user, and Shin and
colleagues operationalize the construct as acceptance and satisfaction. Only Klumbytė, Lücking and
Draude (2020) target users' algorithmic literacy directly, through critical design.

What separates DXD from all five neighbours is the intermediary. In decision-centered design the
system is a tool the operator commands; in choice architecture the architect is a person; in decision
intelligence and the decision journey the analyst is the firm; in algorithmic experience the
algorithm faces one user. DXD, as this review uses the term, concerns decisions that run through an
adaptive, opaque intermediary that reads both parties to a coordination and can commit the outcome.
The designer is then no longer the only architect of the decision, and the person deciding is no
longer the only party to it.

### Choice Architecture and Its Algorithmic Turn

**Choice architecture is the precursor most practitioner uses re-describe without naming.** Its founding
premise is that no presentation of options is neutral. Simon (1956) located half of rational choice in "the structure of the environment" (p. 130), which can "permit further simplication [sic] of its choice mechanisms" (p. 129), and Tversky
and Kahneman (1981) showed that the frame in which options arrive shifts preferences between outcomes
that are formally identical. Thaler and Sunstein (2008) turned that finding into a role, the choice
architect, and Johnson and eleven coauthors (2012) sorted the architect's tools into two families,
those that structure the choice task and those that describe the options. Schneider, Weinmann and vom
Brocke (2018) then carried the role onto the screen: "the more decisions people make using digital
devices, the more the software engineer becomes a choice architect who knowingly or unknowingly
influences people's decisions." In other words, every UX designer who sets a default was already
doing decision design. Putri's removal of a free trial and Wilkinson's spotlighted title are
choice-architecture moves under a new name.

That lineage also supplies DXD's shadow. Gray and colleagues (2018) gave *dark patterns*, a practitioner's term, an academic definition —
interface designs that turn the architect's knowledge against the user — and Mathur and colleagues
(2019) found 1,818 instances of 15 types across roughly 11,000 shopping sites, along with 22
third-party vendors selling them "as a turnkey solution." Mathur, Kshirsagar and Mayer (2021) later
gave the category four normative lenses. The same toolkit serves both uses, which is the first reason
DXD needs a normative account and not only a technique.

**The evidence for the toolkit is weaker than the practitioner canon assumes.** Mertens, Herberz, Hahnel and Brosch (2022) pooled nudge experiments and, in a published correction, reported an average of d = 0.43 ("Correction for Mertens et al.," 2022), with
decision-structure interventions (d = 0.54) outperforming information (d = 0.34) and assistance
(d = 0.28). Three replies disputed the average. Maier and colleagues (2022) found no evidence for
nudging after adjusting for publication bias; Szaszi and colleagues (2022) obtained adjusted
estimates between d = 0.01 and d = 0.08; and DellaVigna and Linos (2022), comparing 126 trials run
by two U.S. nudge units against the academic literature, watched an 8.7-percentage-point academic
effect shrink to 1.4 points at scale. The design heuristics fare no better. Scheibehenne, Greifeneder
and Todd (2010) put the average choice-overload effect at "virtually zero"; Chernev, Böckenholt and Goodman (2015) found that it depends on four moderators — a complex choice set, a difficult task, uncertain preferences and an effort-minimizing goal — and is reliable only once they are taken into account. Even the canonical default replicates smaller:
Chandrashekar and colleagues (2023) found 62.5% participation under opt-in against 73.5% under
opt-out, where the original reported 42% against 82%. The camps now agree on one thing. The
heterogeneity, not the mean, is the finding, and a DXD that sells itself on nudge-sized wins inherits
the dispute.

**Choice architecture assumes an identifiable architect, a fixed menu and a single chooser, and
algorithmic intermediaries break the first two.** Yeung (2017) coined the *hypernudge* for choice
architecture that is "continuously reconfigured in real-time" from each person's data and from
"population-wide trends," with mechanisms buried in "highly opaque" models. Mills and Sætra (2024) went further and named the *autonomous choice architect*: an optimizer that selects "the design which
is most likely to maximise a pre-determined objective," behind which the human architect is
"increasingly obscured." That description fits an A/B-testing product team as well as a
recommender, which places the practitioners of DXD inside the phenomenon they propose to design.
Mills (2022) supplies the deflationary reading that matters most for a design discipline: a
hypernudge is an arrangement of nudges over time, so, on this review's reading, the unit of analysis moves from one screen to a sequence the chooser never sees whole.

The third assumption, the single chooser, survives almost untouched. Every study in this lineage
models one person facing one menu. The only glimpse of the coordination case in the facet's corpus is
an aside in which Mathur and colleagues (2021), relaying Calo and Rosenblat, note that sharing-economy marketplaces "can manipulate both the sellers … and the buyers." A system that reads both parties to an exchange and commits an outcome neither controls is
the case algorithmacy names, and choice architecture has no model of it.

**Boosting is the nearest existing program for building competence instead of steering behavior.**
Hertwig and Grüne-Yanoff (2017) distinguished *boosts*, whose objective "is to foster people's
competence to make their own choices," from nudges, which steer behavior while leaving competence
unchanged; a boost should persist once it is removed. Kozyreva, Lewandowsky and Hertwig (2020)
carried the program online, and Callaway and colleagues (2022) showed an AI tutor teaching decision
strategies whose benefits "transferred to a more challenging task and were retained over time." The
boosting line is the closest template for a DXD that builds algorithmacy in its users. Its online form,
however, frames the target competence as information literacy — the reading of sources and signals —
which is the paradigm the lab's design-ethics arm argues algorithmacy exceeds. Hertwig and
Grüne-Yanoff point past it in one respect: they note that competences can be fostered by teaching
people to redesign their own environments, which is close to specifying intent through an
intermediary. No boost in this literature addresses the third operation, keeping track of an
intermediary that keeps changing.

### Decision Support and Cognitive Systems Engineering

**Engineers designed decision experiences for professionals two decades before UX existed as a
field.** Gorry and Scott Morton (1971) defined the first one by what the machine could not structure:
where a decision resists specification, "the human decision maker must provide judgment and
evaluation." Keen and Scott Morton (1978) and Sprague (1980) then set out decision support systems (DSS) as a field, and Arnott and Pervan reviewed the field's research in 2005 and again in 2014. Cognitive systems engineering then supplied a theory of the person at the decision.
Klein's naturalistic decision making found that skilled deciders "rapidly categorize situations" (Klein, 2008), building on his recognition-primed model of rapid decision making (Klein, 1993); decision-centered design and cognitive task analysis built
support around those key judgments (Crandall et al., 2006; Hutton et al., 2003; Militello & Hutton, 1998); and ecological interface design (EID) mapped a domain's real constraints onto perceptual cues,
so that rule-following stays valid at the edges of the known (Vicente & Rasmussen, 1992).

Three commitments from this tradition transfer to DXD almost intact. The unit of design is the
decision, not the screen. The joint human–machine system, not the machine, is what gets evaluated
(Hollnagel & Woods, 1983; Woods & Hollnagel, 2006). And support should aid "the process of reaching a
decision, and not simply make or recommend solutions" (Woods, 1985, p. 86). Woods's warning about the
alternative reads as a description of platform coordination forty years early: in a system where "the
machine controls data gathering" and "offers a solution," the user becomes a "Data Gatherer" and
"Solution Filter," caught in "a responsibility/authority double-bind" when the only options are to
accept or reject (pp. 87–88).

**The tradition rests on four premises that the algorithmacy condition removes.** Vicente and
Rasmussen (1992) stated two outright: operators "are highly skilled and have extensive experience,"
and the interface serves "a single, specific application" (Sec. IV.A). A third sits in EID's own
limitation, which holds only "to the extent that designers understand the system they are building"
(Sec. V.B). A DXD designer rarely holds the intermediary's policy. The fourth premise is goal
alignment. Klein and colleagues (2004) made a "Basic Compact" with "some degree of goal alignment" a
precondition of joint activity and doubted any automation could enter it fully (pp. 91–92), and Lee
and See (2004) indexed trust to "an individual's goals." An intermediary that optimizes for a third
party's objective does not score low on these definitions; it falls outside them. Herath Pathirannehelage and colleagues (2025) reached the adjacent conclusion from information systems, that extrapolating design knowledge from conventional DSS is "problematic" once systems "learn, adapt, and act autonomously." They
leave out the objective axis, which is the one DXD adds.

**Kahneman and Klein's learning condition is the strongest candidate mechanism for why algorithmacy
is hard.** Kahneman and Klein (2009) made the quality of intuitive judgment depend on "the
predictability of the environment in which the judgment is made and … the individual's opportunity to
learn the regularities of that environment," and warned that "subjective experience is not a reliable
indicator of judgment accuracy." Bainbridge (1983) stated the automation-side version, that process
knowledge "develops only through use and feedback about its effectiveness" (p. 775), and Norman
(1990) explained why the feedback goes missing: systems omit it because "the automation itself doesn't need it" (p. 7 of the 1989 report version). An adaptive intermediary degrades both of Kahneman and Klein's conditions at
once. Its regularities drift as its policy is retrained, and its feedback is routed through a party
whose objective differs from the user's. On this reading algorithmacy is hard because the environment
has low validity, and experience in such an environment breeds confidence without accuracy. That
mechanism is this review's inference; no study in the corpus tests it on platform users.

Bainbridge also named the remedy that the design-ethics ruling below adopts. Where a computer uses
more dimensions and finer criteria than a person can follow, "the human monitor has been given an
impossible task" (p. 776). Her answer was not a better display. It was to make the system decide
"using methods and criteria, and at a rate, which the operator can follow, even when this may not be
the most efficient method technically," and to make it "fail obviously" (p. 777). That is a bound on
the machine, not a demand on the reader.

**Human–automation research already reaches ordinary users, which sets DXD's burden of distinctness.**
Janssen and colleagues (2019), reviewing fifty years of the *International Journal of
Human-Computer Studies*, found automation used increasingly "by non-professional users," and Carsten and Martens (2019) proposed interface design principles for drivers of automated cars. The two
literatures also disagree about which error ordinary users make. Allen and Choudhury (2022) found an
inverted U among IT support staff, with only workers of moderate experience gaining from a tool whose
top recommendations were "about 90%" correct; Banker and Khetani (2019) found consumers surrendering to
algorithmic recommendations "even when the recommendations are inferior." What the transfer cases
share is a system that still serves its user. The unclaimed ground is the triad, in which the system
reads two parties and commits outcomes for a third party's purposes.

### How User Experience Design Became a Cognitive Profession

**HCI imported cognitive science one unit at a time, and each import turned a finding measured at one
grain into a design rule at the same grain.** The first unit was the movement. Fitts (1954) measured
"the information capacity of the human motor system," and Hick (1952) and Hyman (1953) did the same
for choice reaction time; by 1992 MacKenzie could review six studies that used Fitts's law to compare
the mouse, trackball, joystick, touchpad and eye tracker. Card, Moran and Newell (1980, 1983) built a
whole applied science on that grain, the keystroke-level model and the Model Human Processor, and
Harrison, Tatar and Sengers (2007) later identified their information-processing premise as HCI's
second paradigm. The second unit was the glance. Healey and Enns (2012) surveyed attention and
visual-memory research "with direct relevance to visualization"; Buscher, Cutrell and Morris (2009)
tracked the eyes of 20 users across 361 web pages to predict salient regions; Dyson (2004) identified
"the number of characters per line as the critical variable" for reading from screen; and MacLean
(2008) did for touch what the others did for sight, relating perceptual, motor and attentional
capabilities to haptic interface design. The third unit was the task. Hutchins, Hollan and Norman
(1985) defined an interface's directness by the cognitive effort needed to cross two gulfs, execution
from goals to system state and evaluation from system state back to goals (pp. 318–319), and Hollender and colleagues (2010) found 65 publications in the ACM Guide with "cognitive load" in their titles or abstracts, concluded that the theory's concepts had been adopted in HCI, and recast the load "caused by software usage" as extraneous.

That sequence has a historian. Grudin (1990) traced the interface moving "farther and farther out from
the computer" through five foci — hardware, software, terminal, dialogue and work setting — and
observed that "as the focus shifts, … the skills required of practitioners" change. His Table 1 gives
each level its own specialist disciplines (at the terminal, human factors, cognitive psychology and graphic design; at the work setting, social psychology, anthropology and organizational fields), its
own methods, from the laboratory experiment to ethnography, and its own "duration of basic events studied," running from microseconds at the hardware level to days at the work setting (p. 265). Grudin's table is the best single warrant for the
historical half of this review's argument. It supports the general form of the claim, not only the UX
case: the field's knowledge base and its practitioners change whenever the interface reaches out to a
new object. Hollan, Hutchins and Kirsh (2000) made the same point about the unit of analysis, which
should be set by "functional relationships" among the elements of a cognitive process rather than by
the boundary of the individual or the device.

**Human factors predicted where the sequence would end.** The 1951 report behind the Fitts list, as de
Winter and Dodou (2014) quote it, forecast that once machines took over the major work, research on
the human would centre on "reasoning, judgment, planning, and decision making" (p. 7). Seventy-five
years later the forecast describes the object this review proposes. A decision committed through an algorithmic intermediary can be read along the rows of Grudin's table. Its time scale is that of his outermost level, where events run for days and social processes for weeks or months. What differs is the configuration of principals, since two parties coordinate through a system that reads both, and a science base that is, in Grudin's phrase for each new level, less mature than the last.

**Two cautions qualify the historical claim.** The first concerns how cognitive findings travelled.
Cowan (2001, 2015) put the working-memory limit for unchunked items at three to five and quoted Miller
complaining that his paper had been "over-generalized"; Doumont (2002) argued that practitioners cite Miller without having read him; and Commarford, Lewis, Smither and Gentzler (2008) showed that a Miller-derived
guideline of five or fewer menu items made performance worse, most of all for users with low
working-memory capacity. Pernice (2017) makes the parallel correction for reading: the F-shaped scan is a product of unformatted text meeting a hurried, uncommitted reader, not a law of the eye. Imported findings became design folklore when
practitioners detached them from their boundary conditions. A DXD that imports decision research will
face the same hazard, and the nudge-effect dispute above shows it has already begun.

The second caution concerns who held the expertise. I found no study measuring cognitive-psychology
knowledge as a core skill of working UX practitioners. González, Ghazizadeh and Smith (2014) found that
37% of requirements in 40 UX job postings emphasized design familiarity and programming, and
Lallemand, Gronier and Koenig (2015), surveying 758 practitioners and researchers from 35 nationalities, found that understandings of UX varied with background and that respondents wanted a definition they could translate into practice. The cognitive expertise lived in the field's research base, its
specialist roles and its guidelines, and practitioners drew on it through those channels. The analogy
this review draws holds at that level: DXD needs a research base in the cognition of deciding through
intermediaries, and specialists who carry it, not a profession in which every designer is a
psychologist.

**The historiography also disagrees about what comes next.** Chignell, Wang, Zare and Li (2023) argue
that AI calls for HCI to rejoin human factors under a frame of human augmentation; Forlizzi (2018)
argues for stakeholder-centred design, because "we are no longer designing one thing for one person."
Both rival framings claim the post-AI reorganization, and Forlizzi's comes close to the triad. Neither
makes the user's own competence with an intermediary the object of design expertise. Every earlier
unit also shared one assumption. The gulf of evaluation presumes a system whose state a display can
model for the user, and Norman's (1990) remedy for opaque automation was more feedback. That is the
literacy-paradigm move, and the evidence on deciding through algorithms, to which the review now
turns, shows where it stops working.

### The Cognition of Deciding Through an Intermediary

**Deciding through an algorithm poses cognitive problems that reading, load and perception research
do not reach, and the lab's three operations of algorithmacy sort them.** The lab defines algorithmacy
as "the ability to interpret an opaque, adaptive intermediary, to specify intent through it, and to
keep track of it, so that a person can participate in coordination that runs through a system which
reads both parties and commits decisions neither of them controls" (`submissions/lima_pdw/`;
`org_frontier/essays/literacy_or_algorithmacy.md`). *Interpreting* means reading the intermediary's
rule and the unseen counterpart's intentions from the same composite feedback; *specifying intent*
means getting meaning through the channels the intermediary permits; *keeping track* means noticing
when the rule shifts. The human–AI decision literature of the last decade speaks to each operation
unevenly, and its central finding is aggregate. Vaccaro, Almaatouq and Malone (2024) meta-analysed 370
effect sizes from 106 experiments and found that human–AI combinations did worse than the better of
human or AI alone (g = −0.23, 95% CI −0.39 to −0.07), with decision tasks losing most (g = −0.27) and creation tasks faring significantly better, though their own gain was not significant (p. 2295). The average team was worse than its best member. Explanation and
confidence displays did not moderate the result; task type and the relative skill of human and AI
did.

**Interpreting.** People interpret an intermediary through a lay model that forms before and outside
the interface. Logg, Minson and Moore (2019) call it a "theory of machine": lay participants weighted
advice more heavily when it was labelled algorithmic (weight on advice .45 against .30 in their first
experiment), while national-security professionals discounted all advice and were less accurate.
Eslami and colleagues (2015) found that 62.5% of 40 Facebook users did not know their feed was curated,
and concluded that "simple exposure to the algorithm output is not enough to gain information about
the algorithm's existence." Folk theories fill the gap. Eslami and colleagues (2016) recorded ten of
them, DeVito and colleagues (2018) found them "more complex, multifaceted and malleable than
previously assumed," and Bucher (2017) showed the resulting "algorithmic imaginary" feeding back into
the system as users act on their beliefs. Bansal, Nushi, Kamar, Lasecki, Weld and Horvitz (2019)
redefined what interpretation has to reach. The mental model that matters is of the error boundary,
"when does the AI err?", not of the mechanism, and people learn it from the consequences of their own
decisions; a parsimonious boundary is learnable, while a stochastic one makes a correct model difficult to learn.
Dell'Acqua and colleagues (2026) found the same boundary in the field. Consultants working inside the "jagged technology frontier" of AI capability completed 12.2% more tasks, while on a task chosen to fall
outside it they were 19% less likely to be correct.

The literacy paradigm makes its strongest prediction about interpretation, and it fares worst there.
If users misread the intermediary, the literacy remedy is to explain it. Dzindolet and colleagues (2003)
found that explaining why an aid might err raised reliance "even when the trust was unwarranted."
Bansal and colleagues (2021) found that explanations "increased the chance that humans will accept the
AI's recommendation, regardless of its correctness," and that no explanation condition beat simply
showing the AI's confidence. Poursabzi-Sangdeh and colleagues (2021) made a model simple enough to
simulate and found participants "less able to detect and correct for the model's sizable mistakes,
seemingly due to information overload," although one later experiment did not replicate the effect.
In other words, explanation raises acceptance, not accuracy. The counterevidence is real and bounded.
Vasconcelos and colleagues (2023) showed explanations cutting overreliance when checking them cost
less than doing the task, and concluded that "overreliance is not an inevitability of cognition but a strategic decision" (p. 129:3); Zhang, Liao and Bellamy (2020) found confidence scores calibrating trust; and
Kulesza, Stumpf, Burnett and Kwan (2012) found that users who most improved their mental models were more likely to make a music recommender operate to their satisfaction. Each success occurs where the user is the system's only
principal, the system is stable, and verification is cheap. The Vasconcelos result is, at bottom, a
cognitive-load finding. It belongs to UX's home territory, and it marks the edge of the literacy
paradigm rather than refuting the thesis.

**Specifying intent.** This operation has the thinnest direct evidence and the clearest design lever.
Dietvorst, Simmons and Massey (2015) showed people abandoning an algorithm after seeing it err, even
though it outperformed them in every study; the same authors (2018) then found that a modification
right restored use. In their second study, 47% chose the model when they could not change it, against
71%, 71% and 68% when they could adjust its forecasts by 10, 5 or 2 percentiles — "willingness to use
the model was not detectably altered by imposing an 80% reduction" in the adjustment allowed (Study 2).
What moved people was the existence of a channel for their intent, not its bandwidth. Buçinca, Malaya
and Gajos (2021) worked on a different variable, when the human commits a judgment. Their cognitive forcing
functions — showing the AI's answer only on request, only after the participant's own decision, or
only after a wait — reduced overreliance on the AI's wrong answers more than simple explanation
designs did, though participants liked the most effective designs least. Vaccaro and colleagues (2024)
found that more than 95% of the systems studied left the human the final decision, which is the one
channel for intent the literature routinely provides. Outside the laboratory, Cotter's (2019)
influencers specify intent indirectly, playing a "game constructed around 'rules' encoded in
algorithms" by adapting their own conduct to an inferred rule.

**Keeping track.** The classic automation literature names this operation and barely measures it.
Lee and See (2004) required appropriate trust to have temporal specificity, so that trust follows
the system's capability as it changes over time (pp. 55–56). Parasuraman and Manzey (2010, p. 384) report the cost of a system that does not move: in Parasuraman, Molloy and Singh's (1993) study, operators detected 82% of automation failures under variable reliability but 33% under constant reliability. A reliable intermediary erodes tracking fastest. The recent studies turn from
reliability to change. Bansal, Nushi, Kamar, Weld, Lasecki and Horvitz (2019) found that an update
making a classifier more accurate lowered team performance when it was incompatible with what users
had learned, so that "a more accurate but incompatible classifier results in lower team performance
than a less accurate but compatible classifier" (p. 2434). Mohanty, Lim and Luther (2025) found users
detecting whether a model had changed at 48.87%, "close to random guessing." Glickman and Sharot
(2025) found participants "often unaware of the extent of the AI's influence" on their own judgments,
and Fernandes and colleagues (2026) found users overestimating their AI-aided performance, with
"higher AI literacy correlated with lower metacognitive accuracy." Lee and colleagues (2025) found the
same pattern in 319 knowledge workers: confidence in the AI went with less critical thinking
(β = −0.69), though the measure is self-reported enaction of critical thinking. The design guidelines assume the problem away. Amershi and colleagues' (2019) eighteen
guidelines ask the system to "update and adapt cautiously" and to "notify users about changes"
(G14, G18), which presumes a platform that announces its changes and a user who can use the notice.

**The whole corpus studies one decider on the near side of the AI.** Lai, Chen, Smith-Renner, Liao and
Tan (2023) surveyed more than 100 papers on human–AI decision making and closed by asking the
field to consider "what matters for different stakeholders instead of just the decision-makers" (§6).
No study in the facet's corpus puts the second party of a coordination inside the experiment. The
cognition of deciding through an intermediary is therefore documented only for the dyad; the triad,
where the intermediary also reads and binds the counterpart, is the case algorithmacy names and the
case no experiment yet models.

### Algorithmacy on the Numeracy Model

**The lab built algorithmacy on the pattern of literacy, numeracy and oracy, and the pattern licenses
a narrower claim than the one it is usually made to carry.** Wilkinson (1965) named oracy as the
speaking-and-listening ability that deserved the standing schooling already gave reading and counting,
and the lab's definition follows his template: literacy lets a person take part in communication that
runs through text, numeracy in situations that run through number, oracy in communication that runs
through speech, and algorithmacy in coordination that runs through a system which reads both parties
and commits decisions neither controls. The Lima manuscript draws the line the DXD argument needs:
"Literacy, numeracy, and oracy are competences for a medium. Algorithmacy is a competence for a
coordination" (`submissions/lima_pdw/manuscript/INTRODUCTION.md`). Three structural properties of the
intermediary produce the three operations. Its opacity means the rule cannot be observed, which demands
interpreting; its bindingness means one determination binds both parties at once, which demands
specifying intent to two audiences in one act; its adaptivity means the rule moves, which demands
keeping track. "*Keeping track* has no equivalent in traditional literacy frameworks, because
conventional media hold still and this rule does not" (`submissions/lima_pdw/manuscript/PAPER.md`).
The term is not *algocracy*, which Aneesh (2009) uses for a mode of organization — rule by code, set
beside bureaucracy and the market. Algocracy is a property of the system, algorithmacy a capacity of
the person inside it.

The strongest version of the literacy analogy is Ong's. Ong (1982/2002) held that "more than any other single invention, writing has transformed human consciousness" (p. 77), and Goody and Watt (1963) drew
the same great divide between oral and literate societies. Street (1984) answered that literacy's
consequences follow the practices through which it is acquired and the purposes it serves, not the
technology itself; the lab's design-ethics dossier accepts that answer and concludes that the analogy
can claim only that institutions came to require the new competence. A DXD argument routed through
Ong would have to show that algorithmic mediation restructures cognition, and nothing in the evidence
reviewed here shows that.

**Numeracy supplies the defensible form of the argument.** Peters and colleagues (2006) found across
four studies that highly numerate people were "less susceptible to framing effects" and that "the
effect of numeracy was not due to general intelligence." Sobkow, Olszewska and Traczyk (2020), in a large general-population sample, found that multiple numeric competencies "predicted decision making
beyond fluid intelligence and cognitive reflection." Reyna and Brainerd (2023), reviewing the field,
found numerical competencies predicting "informed and accurate risky decision making in business and
engineering …, medicine and health communication … and civil and criminal law," and life outcomes in
health, finance and law (§"Objective and subjective numeracy"; §"Summary and future directions").
Numeracy, in other words, earns its name by incremental validity: it predicts the quality of decisions
made through numbers over and above general ability, without any claim that numbers rewired the mind.
Algorithmacy can be held to the same test. The claim this review carries forward is that algorithmacy
should predict the quality of decisions made through an algorithmic intermediary beyond general
ability and beyond the dyadic literacies below. That claim is testable, and it is not yet tested.

Reyna and Brainerd add a second point the DXD argument can use with care. Skilled numeracy, they
argue, is not "a literal focus on objective numbers and mechanical number crunching," which treats
"numbers as data as opposed to information," but gist extraction — organizing numbers meaningfully and
interpreting them in context — and "gist training facilitates transfer to new contexts and, because it
is more durable, longer-lasting improvements in decision making" (abstract). If algorithmacy has the
same shape, its skilled form is not reading the intermediary's rule more exactly. That parallel is this
review's inference, and it fits the second ruling developed below.

**Every rival competence construct places one person against one system.** Four literatures will be
raised against algorithmacy. *Algorithmic literacy* has competing definitions: DeVito (2021) defines
it as awareness of algorithmic systems plus the capacity to turn that awareness into strategic use,
and Dogruel, Masur and Joeckel (2022) validated a scale of 11 awareness and 11 knowledge items on
1,041 German internet users. *Algorithmic awareness* is Gran, Booth and Bucher's (2021) construct,
measured by a single self-report item in a representative Norwegian survey of 1,624 people. *AI literacy* is Long and Magerko's (2020) set of competencies for evaluating, communicating with and using AI, compressed by Ng and colleagues (2021) into four aspects. *Algorithm skills*
belong to Hargittai and colleagues (2020), who named the measurement problem that proprietary rules
create, and to Klawitter and Hargittai (2018), whose informant, a knitwear seller struggling with Instagram hashtags, called it "like learning a whole other language." The field's own audits find none of these
settled. Oeldorf-Hirsch and Neubaum (2025) reviewed 50 studies and found that even the most
comprehensive scale does "not measure algorithmic literacy as one cohesive construct"; Gagrčin, Naab
and Grub (2026) reviewed 169 studies and found the field "lacks a cohesive framework."

The distinction that holds is structural. The lab does not claim algorithmacy is the only
non-knowledge construct: Zhou and colleagues' (2025) algorithmic-competency scale for ride-hailing
drivers and couriers is three-quarters conduct and attitude, and DeVito's (2021) adaptive folk
theorization already covers adaptation to a moving rule. The Lima manuscript concedes both and claims
novelty only for "mutual bindingness and interdependent joint work." Its Table 1 tests eight candidate
constructs against one question — where does each put the human counterpart? — and finds that
constructs admitting the counterpart demote the system to a conduit, while constructs modelling the
system as opaque and binding demote the counterpart to a rating source. Kalantzis and Cope (2024)
state the live alternative outright: generative AI is "more than anything a technology of writing,"
so literacy, redesigned, absorbs it. Their argument holds wherever the intermediary only carries a
message. It fails where the intermediary reads both parties and commits a decision.

**The lab's formal models tell those two cases apart.** The lab represents a coordination form —
worker, system, counterpart — as a small Boolean system and computes exact integrated information
(Φ) over its minimum-information partition. When some cut factors the form (Φ_MIP = 0), the system is
a moderator and literacy suffices; when no cut does (Φ_MIP > 0), the system mediates and algorithmacy
is demanded (`org_frontier/essays/studying_algorithmacy.md`). The models yield three results a
designer can use. The surface misleads: party count and interface do not settle the verdict, and in
the complete 256-form strict-mediation family at three nodes only 9.4% of forms are triadic. Any
substitutable party, such as a swappable counterpart or a multi-homed platform, collapses the triad to
a dyad. And "disclosure of the agent is a label, not a read, and leaves the verdict unchanged"
(`org_frontier/essays/algorithmacy_outreach_paper.md`). These results are in silico and binary, and a
validation gap separates them from real organizations. They nonetheless give a DXD professional a
principled first question: is this system a moderator or a mediator? The remedy depends on the
answer.

### Why Algorithmacy Expertise Is Not Legibility Expertise

**Making an algorithm legible raises users' awareness of it and leaves their agency where it was.**
Seven studies make the pattern hard to miss once they are read together. On
awareness, the revealing interfaces work. Eslami and colleagues' (2015) FeedVis probe showed users
what their feed had hidden, and 83% of respondents at follow-up reported changing their behaviour;
Fouquaert and Mechant's (2022) Instawareness tool raised cognitive media literacy (ηp² = .13). Every
stronger outcome fails or reverses. Fouquaert and Mechant's tool did not raise critical concern.
Rader, Cotter and Cho (2018) gave 681 Facebook users four kinds of explanation; all four raised the belief that the *system* shapes the feed, and none changed participants' belief that their own behaviour does. Cheng and colleagues (2019) improved
comprehension of an admissions algorithm and found trust "not affected by the explanation interface
or their level of comprehension." Vaccaro, Sandvig and Karahalios (2020) found that no appeal design
improved perceptions of fairness, accountability, trustworthiness or control over a no-appeal
baseline. Moon and colleagues (2025) found that algorithmic literacy made no difference when neither explainability nor user control was present but shaped perceptions once either was, so that transparency's benefits were "unequally experienced" — a new axis of the divide it was meant to close. Fernandes and colleagues (2026), as noted above, found higher AI
literacy going with worse metacognitive accuracy.

The lab's formal result predicts this pattern. Disclosure "is a label, not a read": telling a person
that an intermediary is present changes nothing about whether the coordination factors into dyads.
In other words, a legible triad is still a triad. The transparency successes in the previous section —
explanations that pay off when checking is cheap, confidence scores that calibrate trust — all occur
where the system is stable, verification costs little, and the user is its only principal. Those are
conditions on the *system*, not on the reader. They describe an intermediary whose behaviour is
predictable, and they point to where the design effort belongs.

**The lab's design-ethics arm names three remedies that act on the coordination instead of on the
reader, and each gives DXD expertise a concrete object.** Its draft calls for abandoning "the ambition
of creating 'better readers' of automated systems" in favour of counter-delegation, structural refusal
and bounded outputs (`submissions/algorithmacy_design_ethics/DRAFT.md`).

*Counter-delegation* means a party's own agent acting inside the coordination — the micro-instrument
that Viljoen's (2021) relational account of data governance and Delacroix and Lawrence's (2019)
bottom-up data trusts imply at the scale of institutions. Its minimal empirical form is already in
the decision literature. Dietvorst and colleagues' (2018) modification right showed that a channel for
intent, however narrow, changes whether people will act through an algorithm at all, and Woods's
(1985) double-bind showed what happens without one: a user who can only accept or reject either
rejects everything or abdicates. A DXD professional's expertise here is in designing the channels
through which a party's intent enters the mediation, which is the operation of specifying intent
turned into a design object.

*Structural refusal* means the capacity to say no on one's own terms. Zong and Matias (2024) treat
refusal as design and warn that "some offers to refuse are designed to placate instead of create change" (§5.3.1): an opt-out that penalizes the one who takes it is a choice in name only. The lab's formal
result gives refusal a structural role. Substitutability of any party collapses the triad to a dyad,
so a low-cost exit — to another platform, or directly to the counterpart — converts a mediator back
into a moderator, where literacy suffices. Designing refusal and exit is thus a way of changing which
competence a coordination demands.

*Bounded outputs* means predictable, declared operating envelopes in place of black-box legibility.
Bainbridge's (1983) remedy was the first statement of it: make the system decide "using methods and
criteria, and at a rate, which the operator can follow" (p. 777). Bansal, Nushi, Kamar, Weld, Lasecki
and Horvitz (2019) supply the modern form, backward-compatible updates that preserve what users have
learned, and Parasuraman and Manzey (2010) show why it matters: monitoring fails fastest under
constant reliability, so an intermediary that changes silently after a long stable run is the worst
case for keeping track. Kahneman and Klein's (2009) conditions for skilled intuition — a predictable
environment and an opportunity to learn it — are conditions a designer can create by bounding the
system. A DXD professional's expertise here is in declaring and holding the envelope, which serves
interpreting and keeping track without asking the user to read the rule.

**The designer's expertise lies on the user's side of the intermediary, not inside it.** The
literature on designers and AI mostly asks for the opposite. Dove, Halskov, Forlizzi and Zimmerman
(2017) described machine learning as a difficult design material; Szlachta (2024) listed technical
competences for UX designers by analogy with the web era's expectation that designers know "HTML i
CSS"; Flechtner and Stankowski (2023) and Shalamova, Richards and Miller (2026) outlined curricular content; Li and colleagues (2024) define designers' AI literacy as understanding how AI works and questioning its outputs; and Alvarez (2026) proposes a pedagogy for upskilling UX designers for AI-native work. Yang, Scuito, Zimmerman, Forlizzi and Steinfeld (2018) found the counterevidence to
that line. Their 13 experienced designers of ML-enhanced products did not "view themselves as ML experts, nor do they think learning more about ML would make them better designers," and appeared most successful when they collaborated with data scientists. That finding supports the thesis when the thesis is stated precisely. UX designers did
not become vision scientists; they became experts in what readers perceive and can hold in working
memory. DXD designers need not become machine-learning engineers; they need expertise in what people
can interpret, specify and track through an intermediary, and in the structure — moderator or
mediator, exit or lock-in, stable or drifting — that sets those demands.

**Three design literatures sit between the paradigms, and none yet places the counterpart inside the
design.** Seamful design, from Chalmers and Galani (2004) to Ehsan and colleagues' (2024) seamful
explainable AI, exposes the joins in a system so people can accommodate them. Contestability by design
gives people routes to intervene; Alfrink, Keller, Kortuem and Doorn (2023) derived five system
features and six development practices for it. Algorithmic experience, as noted earlier, extends UX
to algorithms by name (Alvarado & Waern, 2018). All three design *for* a user's competence rather than
steering around it, which aligns them with boosting and with this review's thesis. None of the three models a counterpart whom the system reads and binds: Chalmers and Galani's co-visitors share a direct channel, and Alfrink and colleagues' third parties act for the decision subject. The lab's own arms divide over the first of them: the dial-response
arm treats widening seams as the remedy, and the design-ethics arm treats any aid to reading the
mediator as the literacy trap. This review follows the design-ethics arm. Seams that help a user see a
moderator are useful; seams that help a user read a mediator leave the mediation intact.

### What the Literature Has Not Done

The gap statements below are bounded by where I looked: OpenAlex, Crossref, arXiv, Consensus and the
Semantic Scholar queries that completed, on 30 September 2026, plus the lab's card libraries.

1. I found no scholarly use of "decision experience design." The phrase lives in practitioner writing
   from September 2023 onward. OpenAlex also returns no hits for "algorithmacy," so the lab's
   construct has no indexed external use.
2. I found no work arguing that designers should become experts in users' competence for
   interpreting, instructing and tracking adaptive intermediaries, by analogy with UX expertise in
   reading, load and perception. The nearest claims concern designers' own technical knowledge of AI
   (Flechtner & Stankowski, 2023; Shalamova et al., 2026; Szlachta, 2024) or their use of AI tools (Li
   et al., 2024; Alvarez, 2026).
3. I found no work proposing a design discipline organized around decisions that an algorithmic
   intermediary commits in a multi-party coordination. Decision-centered design serves expert
   operators of non-adaptive tools; choice architecture assumes a human architect; decision
   intelligence models the organization; human–AI decision research studies dyadic advice.
4. I found no experiment on human–AI decision making that places the second party of a coordination
   inside the design, consistent with Lai and colleagues' (2023) closing call.
5. I found no study measuring cognitive-psychology knowledge as a core skill of working UX
   practitioners, so the historical half of the thesis rests on the field's research base and
   historiography, not on practitioner surveys.

### An Agenda for Decision Experience Design

The review supports four propositions. Each is stated so that it can fail.

**Proposition 1: incremental validity.** A measure of algorithmacy should predict the quality of
decisions made through an algorithmic intermediary beyond fluid intelligence, cognitive reflection and
algorithmic literacy as currently scaled. The test is the one Sobkow and colleagues (2020) passed for
numeracy. If algorithmacy adds nothing over Dogruel and colleagues' (2022) scale, the construct is a
relabelling and DXD should build on algorithmic literacy instead.

**Proposition 2: the triad changes the cognition.** The three operations should be harder, and
explanation less useful, when the intermediary also reads and binds a counterpart than when it serves
the decider alone. The contrast requires the two-party experiment that point 4 above records as
missing; the lab's moderator/mediator distinction specifies which forms to compare.

**Proposition 3: bounding beats explaining for keeping track.** Declared envelopes and compatible
updates should improve users' detection of change and their calibration after change more than
explanations or change notices do. Bansal, Nushi, Kamar, Weld, Lasecki and Horvitz (2019) and Mohanty and colleagues (2025) supply the paradigm; the comparison with notification (Amershi et al., 2019, G18) has not been run.

**Proposition 4: a channel for intent matters more than its width.** Following Dietvorst and colleagues
(2018), a minimal counter-delegation channel should raise both willingness to coordinate through an
intermediary and the quality of the resulting decisions, and widening it should add little. If quality
does not rise with willingness, the channel is a placation device in Zong and Matias's (2024) sense.

The outcome measures exist. Peterson and Cheng's (2022) decision difficulty and satisfaction, Chernev
and colleagues' (2015) regret, deferral and switching, Vaccaro and colleagues' (2024) comparison
against the better of human or AI alone, and a measure of the counterpart's outcome, which none of
the reviewed studies records, would together give DXD the evaluation that time-to-decision and
activation cannot.

### Limitations of This Review

The search ran on one day and depends on the tools that worked that day. Scholar Gateway failed
throughout, and Semantic Scholar's rate limits cost six of twelve queries in the term search; both
should be rerun before the review is used in a submission. Read depth varies: the facet files mark
each entry, and many load-bearing classics — Tversky and Kahneman (1981), Thaler
and Sunstein (2008), Card, Moran and Newell (1983), Kahneman and Klein (2009) — are cited from records,
abstracts or existing cards, not full texts read this session. Peters and colleagues (2006) was
reachable only as an abstract; Reyna and Brainerd (2023) carries the numeracy argument's detail.
Street (1984) was not accessible and is cited through the design-ethics dossier's reading, and Wilkinson (1965) through a card built from metadata and secondary sources. Lai and colleagues' (2023) closing quotation was checked against the arXiv preprint, not the FAccT version cited. The decision-centered design chapter in the *Handbook of Cognitive Task Design* was not accessible beyond its table of contents, which lists its authors as Hutton, Miller and Thordsen against the Crossref order. The practitioner sources are web pages and posts, fetched on 30 September 2026, and
may change. The lab's formal results are in silico. Finally, the Kahneman–Klein mechanism for why
algorithmacy is hard, the gist parallel from numeracy, and the mapping of the design-ethics remedies to
the three operations are this review's inferences, and no study in the corpus tests them.


### References

*Generated by `literature/build_references.py` from `literature/references.bib` for the keys in `literature/cited_keys.txt` (APA 7). Each entry's verification basis and read status are in its facet file; the citation audit is in `literature/audit/`.*

Alfrink, K., Keller, I., Kortuem, G., & Doorn, N. (2023). Contestable AI by Design: Towards a Framework. *Minds and Machines*, *33*(4), 613–639. https://doi.org/10.1007/s11023-022-09611-z

Allen, R., & Choudhury, P. (2022). Algorithm-Augmented Work and Domain Experience: The Countervailing Forces of Ability and Aversion. *Organization Science*, *33*(1), 149–169. https://doi.org/10.1287/orsc.2021.1554

Alvarado Rodríguez, O. L. (2017). *Towards Algorithmic Experience: Redesigning Facebook's News Feed* [Master's thesis, Uppsala University, Department of Informatics and Media]. https://www.diva-portal.org/smash/get/diva2:1110570/FULLTEXT01.pdf

Alvarado, O., & Waern, A. (2018). Towards algorithmic experience: Initial efforts for social media contexts. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. https://doi.org/10.1145/3173574.3173860

Alvarez, I. (2026). Upskilling UX designers for AI-native work: A pedagogical framework and empirical evaluation. In *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work* (pp. 1–19). ACM. https://doi.org/10.1145/3808045.3808059

Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for Human-AI Interaction. In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). ACM. https://doi.org/10.1145/3290605.3300233

Aneesh, A. (2009). Global Labor: Algocratic Modes of Organization. *Sociological Theory*, *27*(4), 347–370. https://doi.org/10.1111/j.1467-9558.2009.01352.x

Arnott, D., & Pervan, G. (2005). A Critical Analysis of Decision Support Systems Research. *Journal of Information Technology*, *20*(2), 67–87. https://doi.org/10.1057/palgrave.jit.2000035

Arnott, D., & Pervan, G. (2014). A Critical Analysis of Decision Support Systems Research Revisited: The Rise of Design Science. *Journal of Information Technology*, *29*(4), 269–293. https://doi.org/10.1057/jit.2014.16

Audry, A. (n.d.). Decision Experience Design. https://www.andrewaudry.com/dxdesign

Bainbridge, L. (1983). Ironies of Automation. *Automatica*, *19*(6), 775–779. https://doi.org/10.1016/0005-1098(83)90046-8

Banker, S., & Khetani, S. (2019). Algorithm Overdependence: How the Use of Algorithmic Recommendation Systems Can Increase Risks to Consumer Well-Being. *Journal of Public Policy & Marketing*, *38*(4), 500–515. https://doi.org/10.1177/0743915619858057

Bansal, G., Nushi, B., Kamar, E., Lasecki, W. S., Weld, D. S., & Horvitz, E. (2019). Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance. *Proceedings of the AAAI Conference on Human Computation and Crowdsourcing*, *7*(1), 2–11. https://doi.org/10.1609/hcomp.v7i1.5285

Bansal, G., Nushi, B., Kamar, E., Weld, D. S., Lasecki, W. S., & Horvitz, E. (2019). Updates in Human-AI Teams: Understanding and Addressing the Performance/Compatibility Tradeoff. *Proceedings of the AAAI Conference on Artificial Intelligence*, *33*(1), 2429–2437. https://doi.org/10.1609/aaai.v33i01.33012429

Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M. T., & Weld, D. (2021). Does the Whole Exceed Its Parts? The Effect of AI Explanations on Complementary Team Performance. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM. https://doi.org/10.1145/3411764.3445717

Bucher, T. (2017). The Algorithmic Imaginary: Exploring the Ordinary Affects of Facebook Algorithms. *Information, Communication & Society*, *20*(1), 30–44. https://doi.org/10.1080/1369118X.2016.1154086

Buscher, G., Cutrell, E., & Morris, M. R. (2009). What do you see when you're surfing? Using eye tracking to predict salient regions of web pages. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '09)* (pp. 21–30). ACM. https://doi.org/10.1145/1518701.1518705

Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making. *Proceedings of the ACM on Human-Computer Interaction*, *5*(CSCW1), 188:1–188:21. https://doi.org/10.1145/3449287

Callaway, F., Jain, Y. R., van Opheusden, B., Das, P., Iwama, G., Gul, S., Krueger, P. M., Becker, F., Griffiths, T. L., & Lieder, F. (2022). Leveraging Artificial Intelligence to Improve People's Planning Strategies. *Proceedings of the National Academy of Sciences*, *119*(12), e2117432119. https://doi.org/10.1073/pnas.2117432119

Card, S. K., Moran, T. P., & Newell, A. (1980). The keystroke-level model for user performance time with interactive systems. *Communications of the ACM*, *23*(7), 396–410. https://doi.org/10.1145/358886.358895

Card, S. K., Moran, T. P., & Newell, A. (1983). *The Psychology of Human-Computer Interaction.* Lawrence Erlbaum Associates.

Carsten, O., & Martens, M. H. (2019). How Can Humans Understand Their Automated Cars? HMI Principles, Problems and Solutions. *Cognition, Technology & Work*, *21*(1), 3–20. https://doi.org/10.1007/s10111-018-0484-0

Chalmers, M., & Galani, A. (2004). Seamful Interweaving: Heterogeneity in the Theory and Design of Interactive Systems. In *Proceedings of the 5th Conference on Designing Interactive Systems (DIS '04)* (pp. 243–252). ACM. https://doi.org/10.1145/1013115.1013149

Chandrashekar, S. P., Adelina, N., Zeng, S., Chiu, Y. Y. E., Leung, G. Y. S., Henne, P., Cheng, B. L., & Feldman, G. (2023). Defaults versus Framing: Revisiting Default Effect and Framing Effect with Replications and Extensions of Johnson and Goldstein (2003) and Johnson, Bellman, and Lohse (2002). *Meta-Psychology*, *7*. https://doi.org/10.15626/MP.2022.3108

Cheng, H.-F., Wang, R., Zhang, Z., O'Connell, F., Gray, T., Harper, F. M., & Zhu, H. (2019). Explaining Decision-Making Algorithms through UI: Strategies to Help Non-Expert Stakeholders. In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. https://doi.org/10.1145/3290605.3300789

Chernev, A., Böckenholt, U., & Goodman, J. (2015). Choice Overload: A Conceptual Review and Meta-Analysis. *Journal of Consumer Psychology*, *25*(2), 333–358. https://doi.org/10.1016/j.jcps.2014.08.002

Chignell, M., Wang, L., Zare, A., & Li, J. J. (2023). The Evolution of HCI and Human Factors: Integrating Human and Artificial Intelligence. *ACM Transactions on Computer-Human Interaction*, *30*(2), 1–30. https://doi.org/10.1145/3557891

Commarford, P. M., Lewis, J. R., Smither, J. A.-A., & Gentzler, M. D. (2008). A Comparison of Broad Versus Deep Auditory Menu Structures. *Human Factors*, *50*(1), 77–89. https://doi.org/10.1518/001872008x250665

Correction for Mertens et al., The Effectiveness of Nudging: A Meta-Analysis of Choice Architecture Interventions across Behavioral Domains. (2022). *Proceedings of the National Academy of Sciences*, *119*(19), e2204059119. https://doi.org/10.1073/pnas.2204059119

Cotter, K. (2019). Playing the Visibility Game: How Digital Influencers and Algorithms Negotiate Influence on Instagram. *New Media & Society*, *21*(4), 895–913. https://doi.org/10.1177/1461444818815684

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, *24*(1), 87–114. https://doi.org/10.1017/s0140525x01003922

Cowan, N. (2015). George Miller's magical number of immediate memory in retrospect: Observations on the faltering progression of science. *Psychological Review*, *122*(3), 536–541. https://doi.org/10.1037/a0039035

Crandall, B., Klein, G., & Hoffman, R. R. (2006). *Working Minds: A Practitioner's Guide to Cognitive Task Analysis.* MIT Press. https://doi.org/10.7551/mitpress/7304.001.0001

Danish-Swiss Chamber of Commerce. (2026). @Saxo Bank HQ “The Future of Decision Making” w. Daniel Belfer, CEO, Saxo Bank. Event announcement. https://dshk.ch/events/at-saxo-bank-hq-denmark/

de Winter, J. C. F., & Dodou, D. (2014). Why the Fitts list has persisted throughout the history of function allocation. *Cognition, Technology & Work*, *16*(1), 1–11. https://doi.org/10.1007/s10111-011-0188-1

Delacroix, S., & Lawrence, N. D. (2019). Bottom-up data trusts: Disturbing the 'one size fits all' approach to data governance. *International Data Privacy Law*, *9*(4), 236–252. https://doi.org/10.1093/idpl/ipz014

Dell'Acqua, F., McFowland, E., Mollick, E., Lifshitz, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. *Organization Science*, *37*(2), 403–423. https://doi.org/10.1287/orsc.2025.21838

DellaVigna, S., & Linos, E. (2022). RCTs to Scale: Comprehensive Evidence from Two Nudge Units. *Econometrica*, *90*(1), 81–116. https://doi.org/10.3982/ECTA18709

DeVito, M. A. (2021). Adaptive Folk Theorization as a Path to Algorithmic Literacy on Changing Platforms. *Proceedings of the ACM on Human-Computer Interaction*, *5*(CSCW2), 339:1–339:38. https://doi.org/10.1145/3476080

DeVito, M. A., Birnholtz, J., Hancock, J. T., French, M., & Liu, S. (2018). How People Form Folk Theories of Social Media Feeds and What It Means for How We Study Self-Presentation. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. https://doi.org/10.1145/3173574.3173694

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm Aversion: People Erroneously Avoid Algorithms after Seeing Them Err. *Journal of Experimental Psychology: General*, *144*(1), 114–126. https://doi.org/10.1037/xge0000033

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2018). Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them. *Management Science*, *64*(3), 1155–1170. https://doi.org/10.1287/mnsc.2016.2643

Dogruel, L., Masur, P., & Joeckel, S. (2022). Development and Validation of an Algorithm Literacy Scale for Internet Users. *Communication Methods and Measures*, *16*(2), 115–133. https://doi.org/10.1080/19312458.2021.1968361

Doumont, J.-l. (2002). Magical numbers: The seven-plus-or-minus-two myth. *IEEE Transactions on Professional Communication*, *45*(2), 123–127. https://doi.org/10.1109/tpc.2002.1003695

Dove, G., Halskov, K., Forlizzi, J., & Zimmerman, J. (2017). UX design innovation: Challenges for working with machine learning as a design material. In *Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems* (pp. 278–288). ACM. https://doi.org/10.1145/3025453.3025739

Dyson, M. C. (2004). How physical text layout affects reading from screen. *Behaviour & Information Technology*, *23*(6), 377–393. https://doi.org/10.1080/01449290410001715714

Dzindolet, M. T., Peterson, S. A., Pomranky, R. A., Pierce, L. G., & Beck, H. P. (2003). The Role of Trust in Automation Reliance. *International Journal of Human-Computer Studies*, *58*(6), 697–718. https://doi.org/10.1016/S1071-5819(03)00038-7

Ehsan, U., Liao, Q. V., Passi, S., Riedl, M. O., & Daumé III, H. (2024). Seamful XAI: Operationalizing Seamful Design in Explainable AI. *Proceedings of the ACM on Human-Computer Interaction*, *8*(CSCW1), 119:1–119:29. https://doi.org/10.1145/3637396

Eslami, M., Karahalios, K., Sandvig, C., Vaccaro, K., Rickman, A., Hamilton, K., & Kirlik, A. (2016). First I “Like” It, Then I Hide It: Folk Theories of Social Feeds. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 2371–2382). ACM. https://doi.org/10.1145/2858036.2858494

Eslami, M., Rickman, A., Vaccaro, K., Aleyasen, A., Vuong, A., Karahalios, K., Hamilton, K., & Sandvig, C. (2015). “I Always Assumed That I Wasn't Really That Close to [Her]”: Reasoning about Invisible Algorithms in News Feeds. In *Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems* (pp. 153–162). ACM. https://doi.org/10.1145/2702123.2702556

Fernandes, D., Villa, S., Nicholls, S., Haavisto, O., Buschek, D., Schmidt, A., Kosch, T., Shen, C., & Welsch, R. (2026). AI Makes You Smarter but None the Wiser: The Disconnect between Performance and Metacognition. *Computers in Human Behavior*, *175*, 108779. https://doi.org/10.1016/j.chb.2025.108779

Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement. *Journal of Experimental Psychology*, *47*(6), 381–391. https://doi.org/10.1037/h0055392

Flechtner, R., & Stankowski, A. (2023). AI is not a wildcard: Challenges for integrating AI into the design curriculum. In *Proceedings of the 5th Annual Symposium on HCI Education* (pp. 72–77). ACM. https://doi.org/10.1145/3587399.3587410

Forlizzi, J. (2018). Moving beyond user-centered design. *Interactions*, *25*(5), 22–23. https://doi.org/10.1145/3239558

Fouquaert, T., & Mechant, P. (2022). Making Curation Algorithms Apparent: A Case Study of 'Instawareness' as a Means to Heighten Awareness and Understanding of Instagram's Algorithm. *Information, Communication & Society*, *25*(12), 1769–1789. https://doi.org/10.1080/1369118X.2021.1883707

Gagrčin, E., Naab, T. K., & Grub, M. F. (2026). Algorithmic Media Use and Algorithm Literacy: An Integrative Literature Review. *New Media & Society*, *28*(1), 423–447. https://doi.org/10.1177/14614448241291137

Glickman, M., & Sharot, T. (2025). How Human–AI Feedback Loops Alter Human Perceptual, Emotional and Social Judgements. *Nature Human Behaviour*, *9*(2), 345–359. https://doi.org/10.1038/s41562-024-02077-2

González, C. A., Ghazizadeh, M., & Smith, M. (2014). Perspectives on the Training of Human Factors Students for the User Experience Industry. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, *58*(1), 1807–1811. https://doi.org/10.1177/1541931214581378

Goody, J., & Watt, I. (1963). The Consequences of Literacy. *Comparative Studies in Society and History*, *5*(3), 304–345. https://doi.org/10.1017/S0010417500001730

Gorry, G. A., & Scott Morton, M. S. (1971). *A Framework for Management Information Systems* (Working Paper No. 510-71). Sloan School of Management, Massachusetts Institute of Technology. http://hdl.handle.net/1721.1/47936

Gran, A.-B., Booth, P., & Bucher, T. (2021). To Be or Not to Be Algorithm Aware: A Question of a New Digital Divide? *Information, Communication & Society*, *24*(12), 1779–1796. https://doi.org/10.1080/1369118X.2020.1736124

Gray, C. M., Kou, Y., Battles, B., Hoggatt, J., & Toombs, A. L. (2018). The Dark (Patterns) Side of UX Design. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–14). ACM. https://doi.org/10.1145/3173574.3174108

Grudin, J. (1990). The computer reaches out: The historical continuity of interface design. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '90)* (pp. 261–268). ACM. https://doi.org/10.1145/97243.97284

Hargittai, E., Gruber, J., Djukaric, T., Fuchs, J., & Brombach, L. (2020). Black Box Measures? How to Study People's Algorithm Skills. *Information, Communication & Society*, *23*(5), 764–775. https://doi.org/10.1080/1369118X.2020.1713846

Harrison, S., Tatar, D., & Sengers, P. (2007). The Three Paradigms of HCI. In *alt.chi, CHI 2007 Conference on Human Factors in Computing Systems*. ACM.

Hasić, F., De Smedt, J., & Vanthienen, J. (2018). Augmenting processes with decision intelligence: Principles for integrated modelling. *Decision Support Systems*, *107*, 1–12. https://doi.org/10.1016/j.dss.2017.12.008

Healey, C. G., & Enns, J. T. (2012). Attention and Visual Memory in Visualization and Computer Graphics. *IEEE Transactions on Visualization and Computer Graphics*, *18*(7), 1170–1188. https://doi.org/10.1109/tvcg.2011.127

Herath Pathirannehelage, S., Shrestha, Y. R., & von Krogh, G. (2025). Design Principles for Artificial Intelligence-Augmented Decision Making: An Action Design Research Study. *European Journal of Information Systems*, *34*(2), 207–229. https://doi.org/10.1080/0960085X.2024.2330402

Hertwig, R., & Grüne-Yanoff, T. (2017). Nudging and Boosting: Steering or Empowering Good Decisions. *Perspectives on Psychological Science*, *12*(6), 973–986. https://doi.org/10.1177/1745691617702496

Hick, W. E. (1952). On the Rate of Gain of Information. *Quarterly Journal of Experimental Psychology*, *4*(1), 11–26. https://doi.org/10.1080/17470215208416600

Hollan, J., Hutchins, E., & Kirsh, D. (2000). Distributed cognition: Toward a new foundation for human-computer interaction research. *ACM Transactions on Computer-Human Interaction*, *7*(2), 174–196. https://doi.org/10.1145/353485.353487

Hollender, N., Hofmann, C., Deneke, M., & Schmitz, B. (2010). Integrating cognitive load theory and concepts of human–computer interaction. *Computers in Human Behavior*, *26*(6), 1278–1288. https://doi.org/10.1016/j.chb.2010.05.031

Hollnagel, E., & Woods, D. D. (1983). Cognitive Systems Engineering: New Wine in New Bottles. *International Journal of Man-Machine Studies*, *18*(6), 583–600. https://doi.org/10.1016/S0020-7373(83)80034-0

Hutchins, E. L., Hollan, J. D., & Norman, D. A. (1985). Direct Manipulation Interfaces. *Human–Computer Interaction*, *1*(4), 311–338. https://doi.org/10.1207/s15327051hci0104_2

Hutton, R. J. B., Miller, T. E., & Thordsen, M. L. (2003). Decision-centered design: Leveraging cognitive task analysis in design. In E. Hollnagel (Ed.), *Handbook of Cognitive Task Design* (pp. 383–416). Lawrence Erlbaum Associates. https://doi.org/10.1201/9781410607775.ch17

Hyman, R. (1953). Stimulus information as a determinant of reaction time. *Journal of Experimental Psychology*, *45*(3), 188–196. https://doi.org/10.1037/h0056940

Itera. (2025). La era post-BI: bienvenidos al DX (Decision Experience). https://itera.cl/2025/07/04/la-era-post-bi-bienvenidos-al-dx-decision-experience/

Janssen, C. P., Donker, S. F., Brumby, D. P., & Kun, A. L. (2019). History and Future of Human-Automation Interaction. *International Journal of Human-Computer Studies*, *131*, 99–107. https://doi.org/10.1016/j.ijhcs.2019.05.006

Johnson, E. J., Shu, S. B., Dellaert, B. G. C., Fox, C., Goldstein, D. G., Häubl, G., Larrick, R. P., Payne, J. W., Peters, E., Schkade, D., Wansink, B., & Weber, E. U. (2012). Beyond nudges: Tools of a choice architecture. *Marketing Letters*, *23*(2), 487–504. https://doi.org/10.1007/s11002-012-9186-1

Kahneman, D., & Klein, G. (2009). Conditions for Intuitive Expertise: A Failure to Disagree. *American Psychologist*, *64*(6), 515–526. https://doi.org/10.1037/a0016755

Kalantzis, M., & Cope, B. (2024). Literacy in the Time of Artificial Intelligence. *Reading Research Quarterly*, *60*(1), e591. https://doi.org/10.1002/rrq.591

Keen, P. G. W., & Scott Morton, M. S. (1978). *Decision Support Systems: An Organizational Perspective.* Addison-Wesley.

Klawitter, E., & Hargittai, E. (2018). “It's Like Learning a Whole Other Language”: The Role of Algorithmic Skills in the Curation of Creative Goods. *International Journal of Communication*, *12*, 3490–3510.

Klein, G. (2008). Naturalistic Decision Making. *Human Factors*, *50*(3), 456–460. https://doi.org/10.1518/001872008X288385

Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R., & Feltovich, P. J. (2004). Ten Challenges for Making Automation a “Team Player” in Joint Human-Agent Activity. *IEEE Intelligent Systems*, *19*(6), 91–95. https://doi.org/10.1109/MIS.2004.74

Klein, G. A. (1993). A Recognition-Primed Decision (RPD) Model of Rapid Decision Making. In G. A. Klein, J. Orasanu, R. Calderwood, & C. E. Zsambok (Eds.), *Decision Making in Action: Models and Methods*. Ablex.

Klumbytė, G., Lücking, P., & Draude, C. (2020). Reframing AX with critical design: The potentials and limits of algorithmic experience as a critical design concept. In *Proceedings of the 11th Nordic Conference on Human-Computer Interaction: Shaping Experiences, Shaping Society* (pp. 1–12). ACM. https://doi.org/10.1145/3419249.3420120

Kozyreva, A., Lewandowsky, S., & Hertwig, R. (2020). Citizens Versus the Internet: Confronting Digital Challenges With Cognitive Tools. *Psychological Science in the Public Interest*, *21*(3), 103–156. https://doi.org/10.1177/1529100620946707

Kulesza, T., Stumpf, S., Burnett, M., & Kwan, I. (2012). Tell Me More? The Effects of Mental Model Soundness on Personalizing an Intelligent Agent. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 1–10). ACM. https://doi.org/10.1145/2207676.2207678

Lai, V., Chen, C., Smith-Renner, A., Liao, Q. V., & Tan, C. (2023). Towards a science of human-AI decision making: An overview of design space in empirical human-subject studies. In *Proceedings of the 2023 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1369–1385). ACM. https://doi.org/10.1145/3593013.3594087

Lallemand, C., Gronier, G., & Koenig, V. (2015). User experience: A concept without consensus? Exploring practitioners' perspectives through an international survey. *Computers in Human Behavior*, *43*, 35–48. https://doi.org/10.1016/j.chb.2014.10.048

Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–22). ACM. https://doi.org/10.1145/3706598.3713778

Lee, J. D., & See, K. A. (2004). Trust in Automation: Designing for Appropriate Reliance. *Human Factors*, *46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392

Li, J., Cao, H., Lin, L., Hou, Y., Zhu, R., & El Ali, A. (2024). User experience design professionals' perceptions of generative artificial intelligence. In *Proceedings of the CHI Conference on Human Factors in Computing Systems* (pp. 1–18). ACM. https://doi.org/10.1145/3613904.3642114

Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm Appreciation: People Prefer Algorithmic to Human Judgment. *Organizational Behavior and Human Decision Processes*, *151*, 90–103. https://doi.org/10.1016/j.obhdp.2018.12.005

Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM. https://doi.org/10.1145/3313831.3376727

MacLean, K. E. (2008). Haptic Interaction Design for Everyday Interfaces. *Reviews of Human Factors and Ergonomics*, *4*(1), 149–194. https://doi.org/10.1518/155723408x342826

Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No Evidence for Nudging after Adjusting for Publication Bias. *Proceedings of the National Academy of Sciences*, *119*(31), e2200300119. https://doi.org/10.1073/pnas.2200300119

Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A. (2019). Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites. *Proceedings of the ACM on Human-Computer Interaction*, *3*(CSCW), 1–32. https://doi.org/10.1145/3359183

Mathur, A., Kshirsagar, M., & Mayer, J. (2021). What Makes a Dark Pattern... Dark? Design Attributes, Normative Considerations, and Measurement Methods. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–18). ACM. https://doi.org/10.1145/3411764.3445610

Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The Effectiveness of Nudging: A Meta-Analysis of Choice Architecture Interventions across Behavioral Domains. *Proceedings of the National Academy of Sciences*, *119*(1), e2107346118. https://doi.org/10.1073/pnas.2107346118

Militello, L. G., & Hutton, R. J. B. (1998). Applied Cognitive Task Analysis (ACTA): A Practitioner's Toolkit for Understanding Cognitive Task Demands. *Ergonomics*, *41*(11), 1618–1641. https://doi.org/10.1080/001401398186108

Militello, L. G., & Klein, G. (2013). Decision-centered design. In J. D. Lee & A. Kirlik (Eds.), *The Oxford Handbook of Cognitive Engineering*. Oxford University Press. https://doi.org/10.1093/oxfordhb/9780199757183.013.0016

Mills, S. (2022). Finding the 'Nudge' in Hypernudge. *Technology in Society*, *71*, 102117. https://doi.org/10.1016/j.techsoc.2022.102117

Mills, S., & Sætra, H. S. (2024). The Autonomous Choice Architect. *AI & Society*, *39*(2), 583–595. https://doi.org/10.1007/s00146-022-01486-z

Mohanty, V., Lim, J., & Luther, K. (2025). What Lies Beneath? Exploring the Impact of Underlying AI Model Updates in AI-Infused Systems. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–21). ACM. https://doi.org/10.1145/3706598.3713751

Moon, J. H., Kim, S., Jung, Y., Bang, J., & Sung, Y. (2025). The Effects of Explainability and User Control on Algorithmic Transparency: The Moderating Role of Algorithmic Literacy. *Cyberpsychology, Behavior, and Social Networking*, *28*(7), 497–504. https://doi.org/10.1089/cyber.2024.0525

Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI Literacy: An Exploratory Review. *Computers and Education: Artificial Intelligence*, *2*, 100041. https://doi.org/10.1016/j.caeai.2021.100041

Norman, D. A. (1990). The 'Problem' with Automation: Inappropriate Feedback and Interaction, Not 'Over-Automation'. *Philosophical Transactions of the Royal Society of London. B, Biological Sciences*, *327*(1241), 585–593. https://doi.org/10.1098/rstb.1990.0101

O'Hare, D., Wiggins, M., Williams, A., & Wong, W. (1998). Cognitive task analyses for decision centred design and training. *Ergonomics*, *41*(11), 1698–1718. https://doi.org/10.1080/001401398186144

Oeldorf-Hirsch, A., & Neubaum, G. (2025). What do we know about algorithmic literacy? The status quo and a research agenda for a growing field. *New Media & Society*, *27*(2), 681–701. https://doi.org/10.1177/14614448231182662

Ong, W. J. (2002). *Orality and Literacy: The Technologizing of the Word.* Routledge. (Original work published 1982)

Parasuraman, R., & Manzey, D. H. (2010). Complacency and Bias in Human Use of Automation: An Attentional Integration. *Human Factors*, *52*(3), 381–410. https://doi.org/10.1177/0018720810376055

Parasuraman, R., Molloy, R., & Singh, I. L. (1993). Performance consequences of automation-induced 'complacency'. *The International Journal of Aviation Psychology*, *3*(1), 1–23. https://doi.org/10.1207/s15327108ijap0301_1

Pastagia, K. (2026). UX is Dead. Decision Experience (DX) is the Future. LinkedIn. https://www.linkedin.com/posts/keyurpastagia_ux-is-dead-decision-experience-dx-is-the-activity-7476958776173060096-52kW

Pernice, K. (2017). F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant (Even on Mobile). Nielsen Norman Group. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/

Peters, E., Västfjäll, D., Slovic, P., Mertz, C.K., Mazzocco, K., & Dickert, S. (2006). Numeracy and Decision Making. *Psychological Science*, *17*(5), 407–413. https://doi.org/10.1111/j.1467-9280.2006.01720.x

Peterson, N., & Cheng, J. (2022). Decision experience in hyperchoice: The role of numeracy and age differences. *Current Psychology*, *41*(8), 5399–5411. https://doi.org/10.1007/s12144-020-01041-3

Poursabzi-Sangdeh, F., Goldstein, D. G., Hofman, J. M., Wortman Vaughan, J., & Wallach, H. (2021). Manipulating and Measuring Model Interpretability. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–52). ACM. https://doi.org/10.1145/3411764.3445315

Pratt, L. (2019). *Link: How Decision Intelligence Connects Data, Actions, and Outcomes for a Better World.* Emerald Publishing. https://doi.org/10.1108/9781787696532

Putri, A. R. (2025). How We Improved Activation by 242% by Redesigning Our Membership Decision Flow. Medium. https://medium.com/@ajengerp/how-we-improved-activation-by-242-by-redesigning-our-membership-decision-flow-7dd46911b194

Rader, E., Cotter, K., & Cho, J. (2018). Explanations as Mechanisms for Supporting Algorithmic Transparency. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). ACM. https://doi.org/10.1145/3173574.3173677

Reyna, V. F., & Brainerd, C. J. (2023). Numeracy, gist, literal thinking and the value of nothing in decision making. *Nature Reviews Psychology*, *2*(7), 421–439. https://doi.org/10.1038/s44159-023-00188-7

Rupashree. (2026). Organizational Design Is Just Decision Design. Medium. https://rupashree.medium.com/organizational-design-is-just-decision-design-9d8e9a59d418

Santos, S., & Gonçalves, H. M. (2021). The consumer decision journey: A literature review of the foundational models and theories and a future perspective. *Technological Forecasting and Social Change*, *173*, 121117. https://doi.org/10.1016/j.techfore.2021.121117

Scheibehenne, B., Greifeneder, R., & Todd, P. M. (2010). Can There Ever Be Too Many Options? A Meta-Analytic Review of Choice Overload. *Journal of Consumer Research*, *37*(3), 409–425. https://doi.org/10.1086/651235

Schneider, C., Weinmann, M., & vom Brocke, J. (2018). Digital nudging: Guiding online user choices through interface design. *Communications of the ACM*, *61*(7), 67–73. https://doi.org/10.1145/3213765

Shalamova, N., Richards, K., & Miller, C. (2026). AI is here. Is UX ready? A four-dimension framework for curriculum design. In *Proceedings of the 8th Annual Symposium on HCI Education* (pp. 1–7). ACM. https://doi.org/10.1145/3803869.3803888

Shin, D., Zhong, B., & Biocca, F. A. (2020). Beyond user experience: What constitutes algorithmic experiences? *International Journal of Information Management*, *52*, 102061. https://doi.org/10.1016/j.ijinfomgt.2019.102061

Simon, H. A. (1956). Rational Choice and the Structure of the Environment. *Psychological Review*, *63*(2), 129–138. https://doi.org/10.1037/h0042769

Sobkow, A., Olszewska, A., & Traczyk, J. (2020). Multiple numeric competencies predict decision outcomes beyond fluid intelligence and cognitive reflection. *Intelligence*, *80*, 101452. https://doi.org/10.1016/j.intell.2020.101452

Sprague, R. H., Jr. (1980). A Framework for the Development of Decision Support Systems. *MIS Quarterly*, *4*(4), 1–26. https://doi.org/10.2307/248957

Street, B. V. (1984). *Literacy in Theory and Practice.* Cambridge University Press.

Szaszi, B., Higney, A., Charlton, A., Gelman, A., Ziano, I., Aczel, B., Goldstein, D. G., Yeager, D. S., & Tipton, E. (2022). No Reason to Expect Large and Consistent Effects of Nudge Interventions. *Proceedings of the National Academy of Sciences*, *119*(31), e2200732119. https://doi.org/10.1073/pnas.2200732119

Szlachta, A. M. (2024). Nawigowanie wśród złożoności sztucznej inteligencji. Kluczowe kompetencje techniczne projektantów UX niezbędne w tworzeniu produktów cyfrowych opartych na sztucznej inteligencji (AI) [Navigating the AI complexity: Key technical competency of UX designers necessary to make AI-based digital products]. *Formy*(22). https://doi.org/10.52652/fxyz.22.24.5

Thaler, R. H., & Sunstein, C. R. (2008). *Nudge: Improving Decisions About Health, Wealth, and Happiness.* Yale University Press.

Tversky, A., & Kahneman, D. (1981). The Framing of Decisions and the Psychology of Choice. *Science*, *211*(4481), 453–458. https://doi.org/10.1126/science.7455683

Vaccaro, K., Sandvig, C., & Karahalios, K. (2020). “At the End of the Day Facebook Does What It Wants”: How Users Experience Contesting Algorithmic Content Moderation. *Proceedings of the ACM on Human-Computer Interaction*, *4*(CSCW2), 167:1–167:22. https://doi.org/10.1145/3415238

Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When Combinations of Humans and AI Are Useful: A Systematic Review and Meta-Analysis. *Nature Human Behaviour*, *8*(12), 2293–2303. https://doi.org/10.1038/s41562-024-02024-1

Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023). Explanations Can Reduce Overreliance on AI Systems During Decision-Making. *Proceedings of the ACM on Human-Computer Interaction*, *7*(CSCW1), 129:1–129:38. https://doi.org/10.1145/3579605

Vicente, K. J., & Rasmussen, J. (1992). Ecological Interface Design: Theoretical Foundations. *IEEE Transactions on Systems, Man, and Cybernetics*, *22*(4), 589–606. https://doi.org/10.1109/21.156574

Viljoen, S. (2021). A relational theory of data governance. *Yale Law Journal*, *131*(2), 573–654. https://www.yalelawjournal.org/article/a-relational-theory-of-data-governance

Weinmann, M., Schneider, C., & vom Brocke, J. (2016). Digital nudging. *Business & Information Systems Engineering*, *58*(6), 433–436. https://doi.org/10.1007/s12599-016-0453-1

Wilkinson, A. (1965). The Concept of Oracy. *Educational Review*, *17*(4), 11–15. https://doi.org/10.1080/0013191770170401a

Wilkinson, M. (2023). Enhancing Decision Experience (DX): A Path to Resolving Video Consumption's Paradox. Magine Pro blog. https://www.maginepro.com/enhancing-decision-experience-dx-a-path-to-resolving-video-consumptions-paradox/

Wolf, S. P., Klein, G. A., & Thordsen, M. L. (1991). Decision-centered design requirements. In *Proceedings of the IEEE 1991 National Aerospace and Electronics Conference (NAECON 1991)* (pp. 800–805). IEEE. https://doi.org/10.1109/naecon.1991.165845

Woods, D. D. (1985). Cognitive Technologies: The Design of Joint Human-Machine Cognitive Systems. *AI Magazine*, *6*(4), 86–92. https://doi.org/10.1609/aimag.v6i4.511

Woods, D. D., & Hollnagel, E. (2006). *Joint Cognitive Systems: Patterns in Cognitive Systems Engineering.* CRC Press. https://doi.org/10.1201/9781420005684

Yang, Q., Scuito, A., Zimmerman, J., Forlizzi, J., & Steinfeld, A. (2018). Investigating how experienced UX designers effectively work with machine learning. In *Proceedings of the 2018 Designing Interactive Systems Conference* (pp. 585–596). ACM. https://doi.org/10.1145/3196709.3196730

Yeung, K. (2017). 'Hypernudge': Big Data as a Mode of Regulation by Design. *Information, Communication & Society*, *20*(1), 118–136. https://doi.org/10.1080/1369118X.2016.1186713

Zhang, Y., Liao, Q. V., & Bellamy, R. K. E. (2020). Effect of Confidence and Explanation on Accuracy and Trust Calibration in AI-Assisted Decision Making. In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency* (pp. 295–305). ACM. https://doi.org/10.1145/3351095.3372852

Zhou, L., Lei, X., Liu, M., Huang, X., & Hou, R. (2025). Algorithmic Competency of On-Demand Labor Platform Workers: Scale Development, Antecedents, and Consequences. *Asia Pacific Journal of Human Resources*, *63*(2), e70004. https://doi.org/10.1111/1744-7941.70004

Zong, J., & Matias, J. N. (2024). Data refusal from below: A framework for understanding, evaluating, and envisioning refusal as design. *ACM Journal on Responsible Computing*, *1*(1), Article 10, 1–23. https://doi.org/10.1145/3630107
