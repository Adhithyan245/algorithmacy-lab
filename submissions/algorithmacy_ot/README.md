# Algorithmacy for *Organization Theory*

A submission arm for a theory article at *Organization Theory*: algorithmacy as the sensibility a
person needs to coordinate with another person when the exchange runs through an opaque, adaptive
algorithmic intermediary that evaluates and binds them both. Target: a submission-ready draft before
the end of 2026.

**Status, 2026-10-07 — the arm opens.** The paper comes out of the OS/OT Paper Development Workshop in
Lima (5–7 October 2026), where the workshop version drew the comment that it read like an essay. That
version is frozen at
[`../lima_pdw/archive/2026-09-10_PAPER_submitted.md`](../lima_pdw/archive/2026-09-10_PAPER_submitted.md).
The author began the rebuild the same week: an introduction of their own, and a second section first
drafted with another AI assistant, which the author rules is their working draft. Both are seated in
[`manuscript/PAPER.md`](manuscript/PAPER.md), wording unchanged — 961 words of an 8,900-word body.
Claude carded the six sources the new text cites that the library lacked, re-read Stark and Vanden
Broeck, and checked the draft against all of them; the result is
[`manuscript/FLAGS_2026-10-07.md`](manuscript/FLAGS_2026-10-07.md), five claims the cited source does
not support and seven that drift from it. None is applied. Sections 3–6 are unwritten; the author
drafts them from the packets in [`manuscript/OUTLINE.md`](manuscript/OUTLINE.md).

## Rules for this arm

1. **`manuscript/PAPER.md` is the author's prose.** Claude edits what the author writes: citation
   checks, cohesion reading, structural notes, length. Claude does not generate manuscript prose and
   does not run review-then-rewrite loops over it. The author's read-aloud is the last gate.
2. **Wrong facts are flagged, not fixed.** A flag gives the correct value and its source; the author
   rules; only ruled fixes go in.
3. **Anything Claude writes inside the manuscript is marked** `[CLAUDE: …]`.
4. **A source is quotable only at full-text depth.** See
   [`manuscript/CITATION_DEPTH.md`](manuscript/CITATION_DEPTH.md).
5. **[`JOURNAL_SPEC.md`](JOURNAL_SPEC.md) wins on format.** 11,000 words including references;
   double-anonymized.
6. **The repo is public.** No publisher PDF or extracted full text is committed. No agent contacts the
   journal.

## Contents

| Path | What it is |
| --- | --- |
| [`JOURNAL_SPEC.md`](JOURNAL_SPEC.md) | The journal's requirements, extracted from its guidelines, with the word budget |
| [`AGENDA.md`](AGENDA.md) | Open questions, the author's first |
| [`FEEDBACK.md`](FEEDBACK.md) | What the Lima reviewers said. Mostly empty: the author's to fill |
| [`RESEARCH_PLAN.md`](RESEARCH_PLAN.md) | The six lines of new reading the unwritten sections need |
| [`manuscript/PAPER.md`](manuscript/PAPER.md) | **The live draft** |
| [`manuscript/OUTLINE.md`](manuscript/OUTLINE.md) | The architecture: budget, each section's job, a packet per section |
| [`manuscript/FLAGS_2026-10-07.md`](manuscript/FLAGS_2026-10-07.md) | Source checks on sections 1 and 2, awaiting rulings |
| [`manuscript/MODEL_PAPERS.md`](manuscript/MODEL_PAPERS.md) | How five OT theory articles are built, and a check of the six-phase table |
| [`manuscript/CARRYOVER.md`](manuscript/CARRYOVER.md) | Which of the Lima paper's sections fit which new section, by line |
| [`manuscript/CITATION_DEPTH.md`](manuscript/CITATION_DEPTH.md) | What may be quoted |
| [`manuscript/process/`](manuscript/process/) | The two Google Doc texts as pulled, and the Stark and Vanden Broeck re-read. Not a source of truth |
| `reviews/` | Review rounds, when there are any |

## The library is shared

This arm keeps no literature of its own. Cards live in
[`../lima_pdw/literature/cards/`](../lima_pdw/literature/cards/) (415 as of today), with the seven
construct hearings in `../lima_pdw/literature/steelmans/` and the naming hazards in
`../lima_pdw/literature/TRAPS.md`. New cards go there, in that format, and the index is rebuilt with
`python3 _build_index.py` from `../lima_pdw/literature/`.

## Related arms

- [`../lima_pdw/`](../lima_pdw/) — the workshop paper and the library.
- [`../proposals/`](../proposals/) — a different paper due at the same journal on 2027-01-31.
- [`../triadic_reduction/`](../triadic_reduction/) — the Peirce, Simmel and Quine sources behind the
  introduction's "irreducible triads".
