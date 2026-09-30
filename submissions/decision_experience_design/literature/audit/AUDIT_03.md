# Citation audit — batch 03 (30 keys)

Audited 2026-09-30 against `REVIEW.md` (Draft 1) and `literature/references.bib`. Each entry was checked by
reading, one at a time; no script decided any match. "Printed" = the entry as it appears in REVIEW.md's
References list. Crossref records are `https://api.crossref.org/works/<DOI>`. Retraction check: Crossref
`updated-by` on each record plus `filter=updates:<DOI>` for every DOI in the batch; web search for Mertens.
The only update notice found in the batch is the Mertens et al. Correction (no retractions).

## Summary table

| key | metadata status | what you checked (record URL) | claim check (each quote/number: OK / problem + source locator) | action needed |
|---|---|---|---|---|
| longmagerko2020 | Verified | Crossref 10.1145/3313831.3376727 (title, 2 authors, CHI '20, pp. 1–16); OpenAlex abstract | L486 "seventeen competencies for evaluating, communicating with and using AI": the abstract gives no count. Support: secondary only (Springer narrative review 10.1007/s40692-025-00354-1 per search snippet gives n = 17); the lab card is abstract-only; F1 records Li et al. (2024) giving "16 core competencies". The definition paraphrase matches the quoted definition in F6. | Confirm "seventeen" against the paper's full text (conflicting secondary counts). |
| maclean2008haptic | Verified | Crossref 10.1518/155723408x342826 (4(1), 149–194, 2008) | L275–277 "relating perceptual, motor and attentional capabilities to haptic interface design": OK, Crossref abstract ("relate perceptual, motor, and attentional capabilities to a selection of emerging application contexts"). | None. |
| maier2022noevidence | Verified | Crossref 10.1073/pnas.2200300119 (6 authors in order, 119(31), e2200300119); no update notices | L152 "found no evidence for nudging after adjusting for publication bias": OK, the article's title and F2 (read in full, p. 2 "no evidence remains"). | None. |
| mathur2019dark | Verified | Crossref 10.1145/3359183 (7 authors, 3(CSCW), 1–32); arXiv 1907.07032v2 shows Article 81 | L143–145 "1,818 instances of 15 types across roughly 11,000 shopping sites" OK; "22 third-party vendors selling them 'as a turnkey solution'" OK (abstract p. 1: "22 third-party entities that offer dark patterns as a turnkey solution"). | None. |
| mathur2021dark | **Mismatch** (printed) | Crossref 10.1145/3411764.3445610: title "What Makes a Dark Pattern... Dark?" + subtitle; authors Mathur, Kshirsagar, Mayer; pp. 1–18. Bib matches; **printed title reads "What Makes a Dark Patternłdots Dark?"** (the `\ldots` macro mis-rendered) | L145–146 "four normative lenses" OK (arXiv 2101.04843v1 §4, "four normative lenses—individual welfare, collective welfare, regulatory objectives, and individual autonomy"). L179 quote "can manipulate both the sellers … and the buyers" verbatim OK (pdf p. 13), **but it is Mathur et al. relaying Calo and Rosenblat's argument about "sharing economy marketplaces"**, not the authors' own finding about "platforms". | Fix bib/renderer title; attribute the L179 aside (see Problems). |
| mertens2022effectiveness | Verified (correction exists) | Crossref 10.1073/pnas.2107346118 (updated-by: correction 10.1073/pnas.2204059119); Correction full text Europe PMC PMC9171817 | L149–152 corrected d = 0.43 OK; structure 0.54, information 0.34, assistance 0.28 OK — all from the Correction's Table 2 (overall 0.43 [0.38, 0.48], k = 447; information 0.34 [0.27, 0.42]; structure 0.54 [0.46, 0.62]; assistance 0.28 [0.21, 0.35]). The printed References entry does not mention the Correction, though the text reports corrected figures. | Add the Correction to References (see Problems). |
| militello1998applied | Verified | Crossref 10.1080/001401398186108 (Ergonomics 41(11), 1618–1641) | L206 cited for CTA building support around key judgments: OK, OpenAlex abstract (CTA output "can be used to inform the design of interfaces and training systems"). | None. |
| militello2013decision | Verified | Crossref 10.1093/oxfordhb/9780199757183.013.0016 (Militello & Klein, "Decision-Centered Design", 2013) | L94 cited only for existence of a handbook chapter by 2013: OK (record). Content not accessible (F1). | None. |
| mills2022autonomous | Verified (bib); **in-text year mismatch** | Crossref 10.1007/s00146-022-01486-z (online 2022-06-22; print 2024, 39(2), 583–595) | L168–171 "the design which is most likely to maximise a pre-determined objective" OK; "increasingly obscured" OK (Crossref abstract). **In-text reads "Mills and Sætra (2022)"; References print 2024.** | Make the in-text year match (see Problems). |
| mills2022finding | Verified | Crossref 10.1016/j.techsoc.2022.102117 (71, 102117, 2022); printed title shows LaTeX quotes "`Nudge'" | L173–175 "a hypernudge is an arrangement of nudges over time": OK (OpenAlex abstract "a system of nudges which change over time … an arrangement of nudges"). "a sequence the chooser never sees whole" is the review's inference; support: abstract only. | Fix printed quote marks; optional: mark the inference. |
| mohanty2025lies | Verified | Crossref 10.1145/3706598.3713751 (3 authors, CHI '25, pp. 1–21); arXiv 2311.10652v6 | L411–412 "48.87%, 'close to random guessing'" OK verbatim (§3.9.1: "the overall accuracy in detecting whether models had changed was 48.87%, close to random guessing"). L648 paradigm citation OK. | None. |
| moon2025effects | Verified | Crossref 10.1089/cyber.2024.0525 (5 authors, 28(7), 497–504) | L534–536 "explainability and user control paid off mainly for users who were already algorithmically literate": **the abstract does not state the direction**; it says literacy "had no significant impact" with neither feature and "significantly influenced the dependent variables" when at least one was present, and that "transparency benefits are unequally experienced." Support: abstract only. "new axis of the divide" OK (abstract: "a new dimension of the digital divide"). | Soften to what the abstract states (see Problems). |
| ng2021conceptualizing | Verified | Crossref 10.1016/j.caeai.2021.100041 (4 authors, vol 2, 100041); OpenAlex abstract | L487 "four aspects" OK (abstract: four aspects from 30 articles). "compressed [Long & Magerko's competencies]": support is the repo card only; the abstract says the aspects come from "adaptation of classic literacies." | None required; the link to Long & Magerko is card-level only. |
| norman1990problem | Verified | Crossref 10.1098/rstb.1990.0101 (327(1241), 585–593, 1990); ICS Report 8904 full text via NASA NTRS (OpenAlex green OA) | L238–239 quote "the automation itself doesn't need it" verbatim OK, **but "(p. 7)" is the ICS Report 8904 pagination** (report p. 7; NTRS pdf p. 8), not a page in the cited *Phil. Trans. B* 585–593. L330 "remedy … was more feedback" OK. Printed title shows LaTeX quotes "`Problem'". | Fix the locator/version (see Problems); fix printed quote marks. |
| oeldorfhirsch2025 | Verified | Crossref 10.1177/14614448231182662 (online 2023-07, print 2025, 27(2), 681–701); OSF preprint 10.31235/osf.io/2fd4j | L491–492 "reviewed 50 studies" OK ("reviewed 96 articles … 50 of which are included"); quote "not measure algorithmic literacy as one cohesive construct" verbatim OK (preprint; card says VoR re-checked). | None. |
| ohare1998cognitive | Verified | Crossref 10.1080/001401398186144 (4 authors, Ergonomics 41(11), 1698–1718) | L94 cited in the sentence about DCD reaching "the human-factors handbooks by 2003 and 2013"; O'Hare is a 1998 journal article (OpenAlex abstract: three CTA case studies), so it supports the method's spread but not the "handbooks" clause. | Optional: move the cite (see Problems). |
| ong1982orality | Verified | Open Library work OL3798223W (Methuen, London, 1982; ISBN 0416713807); copyright page of the archive.org copy ("First published in 1982 by Methuen & Co. Ltd") | L55, L449–450 quote "More than any other single invention, writing has transformed human consciousness" verbatim OK. **Locator "(p. 77)" comes from the 2002 Routledge edition** (archive.org `OngWalterOralityAndLiteracy`, T&F e-Library 2005 printing: quote on the page after p. 76), which the card read. Secondary sources citing the 1982 text give **p. 78** (MIT 21H.418 assignment). The card's claim that pagination is identical is unverified. | Resolve edition/page (see Problems). |
| parasuraman2010complacency | Verified | Crossref 10.1177/0018720810376055 (Human Factors 52(3), 381–410); closed, no OA; card `algorithmacy_design_ethics/literature/library/parasuramanmanzey2010.md` (full text, adversarially verified) | L405–407 "82% … under variable reliability but 33% under constant reliability (p. 384)": numbers and page OK per card, **but the card states these are Parasuraman, Molloy and Singh's (1993) results as reviewed on p. 384**; "Parasuraman and Manzey (2010) showed" attributes a primary finding to a review. Support: repo card (not re-read; paywalled). L574 "monitoring fails fastest under constant reliability" same source. | Attribute to the 1993 study (see Problems). |
| pastagia2026dx | **Mismatch** (minor) | Live LinkedIn page fetched 2026-09-30: headline "UX is Dead. Decision Experience (DX) is the Future."; `datePublished` 2026-06-28T11:24:47Z. Bib/printed use a bracketed placeholder title "[LinkedIn post on Decision Experience (DX)]" and note "no title … circa June 2026" | L81–82 quote "That's no longer UX. That's Decision Experience (DX)." verbatim OK (articleBody). Outward/customer orientation OK (investing, refinancing, insurance, loans). | Replace placeholder title and date (see Problems). |
| pathirannehelage2024design | **Mismatch** (year) | Crossref 10.1080/0960085X.2024.2330402: online 2024-03-20, **print 2025-03, 34(2), 207–229**; surname "Herath Pathirannehelage" | L227–229 quote "learn, adapt, and act autonomously" verbatim OK (abstract). "design knowledge from conventional DSS does not extrapolate" overstates the abstract's "the extrapolation of prescriptive design knowledge from conventional DSS to AIADM is problematic." In-text surname "Pathirannehelage" vs reference "Herath Pathirannehelage". | Fix year convention, surname, and verb (see Problems). |
| pernice2017fshaped | Verified | Live NN/g page (title, Kara Pernice, 12 Nov 2017; last reviewed 19 Aug 2026) | L309–310 "the F-shaped scan is a symptom of unformatted text, not a law of the eye": broadly OK, but the page requires three conditions together — text with "little or no formatting," a user "trying to be most efficient," and a user "not so committed" as to read every word. "Symptom of unformatted text" drops two of the three. | Optional wording fix (see Problems). |
| peters2006numeracy | Verified | Crossref 10.1111/j.1467-9280.2006.01720.x (6 authors, 17(5), 407–413) with abstract | L458–460 "four studies" OK; "less susceptible to framing effects" OK; "the effect of numeracy was not due to general intelligence" verbatim OK (Crossref abstract). L669 "abstract only" disclosure consistent. | None. |
| peterson2022decision | Verified | Crossref 10.1007/s12144-020-01041-3 (online 2020-09-14; print 2022, 41(8), 5399–5411); Semantic Scholar abstract | L103–105 sixteen vs four options, hyperchoice raised difficulty, numeracy moderated in the gamble task: OK (abstract). L656 difficulty and satisfaction as outcomes OK. Note: OA copy exists (PMC7487285) though F1 lists abstract only. | None. |
| poursabzi2021manipulating | Verified | Crossref 10.1145/3411764.3445315 (5 authors, CHI '21, pp. 1–52); arXiv 1802.07810v5 | L374–376 quote "less able to detect and correct for the model's sizable mistakes, seemingly due to information overload" verbatim OK (abstract). "one later experiment did not replicate the effect" OK (§1, Experiment 3). | None. |
| pratt2019link | Verified | Crossref 10.1108/9781787696532 (Pratt, *Link*, Emerald Publishing Limited, 2019) | L99 DI "as a data-to-action discipline in trade writing": OK (publisher description via OpenAlex). | None. |
| putri2025dx | Verified | Medium RSS https://medium.com/feed/@ajengerp: title verbatim, pubDate Tue 02 Dec 2025, author Ajeng Restu Putri | L27–29: Indonesia, learning platform for teachers, 14.8% → 50.6%, free trial removed: OK. Quote: source reads "This was a decision experience design problem." (capital T; REVIEW lowercases without brackets). "converted 14.8% of sign-ups into members" paraphrases "activation rate was stuck at 14.8%." The redesign also cut the monthly plan's price from IDR 199,000 to IDR 50,000; REVIEW credits the rise to trial removal alone (L28, L139). | Minor wording fixes (see Problems). |
| rader2018explanations | Verified | Crossref 10.1145/3173574.3173677 (3 authors, CHI '18, pp. 1–13); author PDF emileerader.com/papers/rader_chi18.pdf | L529 "681 Facebook users" OK (p. 4, US); "four kinds of explanation" OK. "all four raised the belief that the *system* has agency" OK. "none raised the user's": literally OK, but Rader's **User Agency** variable is agreement that "their own behaviors can cause them to not see all of the available stories" — a belief about causal responsibility, not the user's agency or control. The abstract adds that all explanations "helped them to determine … if they can control what they see." The section thesis ("leaves their agency where it was") leans on a construct the study does not measure. | Reword (see Problems). |
| reyna2023numeracy | Verified | Crossref 10.1038/s44159-023-00188-7 (2(7), 421–439, 2023); full text Europe PMC PMC10196318 | L463–465 quote "informed and accurate risky decision making in business and engineering …, medicine and health communication … and civil and criminal law" OK (§"Objective and subjective numeracy"); life outcomes in health, finance, law OK (§"Summary and future directions"). L473–476 quotes "a literal focus on objective numbers and mechanical number crunching", "numbers as data as opposed to information", "gist training facilitates transfer to new contexts and, because it is more durable, longer-lasting improvements in decision making" all verbatim OK (abstract). | None. |
| rupashree2026decision | Verified | Medium RSS https://rupashree.medium.com/feed: title verbatim, pubDate Sun 26 Jul 2026, author RUPASHREE | L88 "decision architecture" OK. **L30–32 counts Rupashree among those who "used the phrase, or the acronym DX for 'decision experience'"; the full post (RSS body, ~780 words) contains neither "decision experience" nor "DX".** It uses "decision architecture" and "Decision Design." | Remove from the L30–32 list and fix the count (see Problems). |
| santos2021consumer | Verified | Crossref 10.1016/j.techfore.2021.121117 (2 authors, 173, 121117, 2021); Semantic Scholar abstract | L100–101 "noted in 2021 that the effect of AI on that path was untheorized": OK (abstract: "the lack of academic studies reflecting on the influence of more recent technologies based on artificial intelligence on the consumer journey"). | None. |

**Metadata counts:** Verified 27 · Mismatch 3 (mathur2021dark printed title; pastagia2026dx title/date; pathirannehelage2024design year) · Not found 0 · Unreachable 0.
**Retractions:** none. **Corrections:** Mertens et al. 2022 (PNAS 119(19), e2204059119), already reflected in the numbers.

## Problems found (proposed fixes; nothing has been changed)

1. **Rupashree miscounted as a "decision experience/DX" user (L30–32).** Old: "Six other practitioners and
   organizations used the phrase, or the acronym DX for "decision experience," between September 2023 and
   September 2026 (Audry, n.d.; Danish-Swiss Chamber of Commerce, 2026; Itera, 2025; Pastagia, 2026;
   Rupashree, 2026; Wilkinson, 2023)." New: "Five other practitioners and organizations used the phrase, or
   the acronym DX for "decision experience," between September 2023 and September 2026 (Audry, n.d.;
   Danish-Swiss Chamber of Commerce, 2026; Itera, 2025; Pastagia, 2026; Wilkinson, 2023)." L88 already
   covers Rupashree correctly. Source: full post via RSS (https://rupashree.medium.com/feed, item dated
   2026-07-26), which uses "decision architecture" and never "decision experience" or "DX." Also check
   whether "Only one of them, the Chilean consultancy Itera, cites the others" still reads right.
2. **Parasuraman & Manzey 82%/33% is a reported, not original, finding (L405–407).** Old: "Parasuraman and
   Manzey (2010) showed the cost of a system that does not move: operators detected 82% …" New:
   "Parasuraman and Manzey (2010, p. 384) report the cost of a system that does not move: in Parasuraman,
   Molloy and Singh's (1993) study, operators detected 82% …" and add to the bib: Parasuraman, R., Molloy, R.,
   & Singh, I. L. (1993). Performance consequences of automation-induced 'complacency'. *International
   Journal of Aviation Psychology, 3*(1), 1–23. https://doi.org/10.1207/s15327108ijap0301_1 (Crossref
   record checked). Source: card `parasuramanmanzey2010.md` line 7.
3. **Ong p. 77 is an edition-specific locator (L450).** The page comes from the 2002 Routledge edition (the
   archive.org copy the card read: "This edition first published 2002 … Taylor & Francis e-Library, 2005").
   Secondary citations of the 1982 Methuen text give p. 78 (MIT 21H.418 homework page). Either (a) cite the
   edition read: "Ong (1982/2002) … (p. 77)", with the bib entry adding the 2002 Routledge edition; or
   (b) check a Methuen 1982 copy and change to "(p. 78)" if it confirms. The author decides.
4. **Norman 1990 locator refers to a different version (L239).** "(p. 7)" is page 7 of ICS Report 8904
   (July 1989; NASA NTRS 19900004678), not of *Phil. Trans. R. Soc. B* 327, 585–593, which the reference
   cites. Either cite the report as the version read ("Norman, 1989/1990, ICS Report 8904, p. 7") or find
   the journal page. The quote itself is verbatim.
5. **Mertens correction missing from References.** The text reports corrected figures (all four verified
   against the Correction's Table 2), but the printed reference cites only the original. Add: "Mertens, S.,
   Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). Correction for Mertens et al., The effectiveness of
   nudging…. *PNAS, 119*(19), e2204059119. https://doi.org/10.1073/pnas.2204059119", and cite it at L150
   ("reported a corrected average" → "reported, after correction (Mertens et al., 2022b), an average").
   Source: Crossref 10.1073/pnas.2204059119; PMC9171817.
6. **Mills & Sætra year (L168).** Old: "Mills and Sætra (2022)". New: "Mills and Sætra (2024)" to match
   References (or "(2022/2024)" if the author prefers online-first year). Source: Crossref
   10.1007/s00146-022-01486-z (online 2022-06-22; 39(2) 2024).
7. **Mathur 2021 printed title (References).** Old: "What Makes a Dark Patternłdots Dark?" New: "What Makes a
   Dark Pattern... Dark? Design Attributes, Normative Considerations, and Measurement Methods." Fix the bib
   `\ldots` (use a literal "...") or the renderer. Source: Crossref 10.1145/3411764.3445610.
8. **Mathur 2021 aside attribution (L178–180).** Old: "an aside in Mathur and colleagues (2021), that
   platforms "can manipulate both the sellers … and the buyers."" New: "an aside in Mathur and colleagues
   (2021), relaying Calo and Rosenblat, that sharing-economy marketplaces "can manipulate both the sellers
   … and the buyers."" Source: arXiv 2101.04843v1, pdf p. 13.
9. **Herath Pathirannehelage et al.: year, surname, verb (L227–229; References).** (a) The year: Crossref
   gives online 2024 and issue 2025 (34(2)). The References list uses the issue year elsewhere (Mills &
   Sætra 2024, Oeldorf-Hirsch 2025, Peterson & Cheng 2022), so change "(2024)" to "(2025)" in the bib, the
   References and the text, for consistency. (b) The in-text surname: "Pathirannehelage and colleagues"
   → "Herath Pathirannehelage and colleagues." (c) The verb: "that design knowledge from conventional DSS
   does not extrapolate once systems…" → "that extrapolating design knowledge from conventional DSS is
   'problematic' once systems…" Source: Crossref and the OpenAlex abstract.
10. **Rader et al. "agency" (L529–530).** Old: "all four raised the belief that the *system* has agency,
    and none raised the user's." New: "all four raised the belief that the *system* shapes the feed, and
    none changed participants' belief that their own behaviour does." Source: rader_chi18.pdf, results
    ("the User Agency outcome variable showed no differences from the control condition"; the item asks
    whether "their own behaviors can cause them to not see all of the available stories").
11. **Moon et al. direction (L534–536).** Old: "found that explainability and user control paid off mainly
    for users who were already algorithmically literate". New: "found that algorithmic literacy made no
    difference when neither explainability nor user control was present but shaped perceptions once either
    was, so that transparency's benefits were "unequally experienced"". Support: abstract only (Crossref).
12. **Pastagia metadata.** Bib/References title "[LinkedIn post on Decision Experience (DX)]" → "UX is Dead.
    Decision Experience (DX) is the Future." Update the note to "posted 2026-06-28". Source: live page
    `datePublished` and headline, fetched 2026-09-30.
13. **Putri wording (L28–29, L139).** (a) "converted 14.8% of sign-ups into members" → "had an activation
    rate stuck at 14.8%". (b) Quote capitalisation: "she wrote that "this was …"" → "she wrote that "[t]his
    was a decision experience design problem"". (c) Optional: the redesign also cut the monthly plan's price
    from IDR 199,000 to IDR 50,000. "her team removed a free trial" could read "her team removed a free trial
    and cut the entry price," since L139 treats the trial removal alone as the choice-architecture move.
    Source: Medium RSS, item of 2025-12-02.
14. **Printed LaTeX quotes (References).** "Finding the `Nudge' in Hypernudge" → "Finding the 'Nudge' in
    Hypernudge"; "The `Problem' with Automation: … Not `Over-Automation'" → "The 'Problem' with Automation: …
    Not 'Over-Automation'". Source: Crossref titles.
15. **Long & Magerko count (L486), verify only.** The count "seventeen" rests on secondary sources. F1
    records Li et al. (2024) saying "16 core competencies." Check the CHI paper's competency list before
    submission.
16. **Minor or optional.** (a) Pernice (L309): "a symptom of unformatted text" → "a product of unformatted
    text meeting a hurried, uncommitted reader" (NN/g page: all three conditions must be present).
    (b) O'Hare et al. (1998) sits in a sentence about handbooks (L93–95). Moving it next to "requirements
    elicited … by critical-decision interviews" matches its abstract better. (c) Mills (2022), L174–175:
    "a sequence the chooser never sees whole" goes beyond the abstract; mark it as the review's inference
    if wanted.
