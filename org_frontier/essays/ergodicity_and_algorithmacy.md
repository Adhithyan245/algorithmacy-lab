# Navigating a platform is a non-ergodic problem

*Literacy assumes that population norms transfer to the individual. Algorithmacy
begins where that transfer fails.*

---

A text does not change because it was read. The reader adapts; the page does
not. In the language of random dynamical systems that arrangement is a skew
product: a driven system whose driver evolves on its own. Under an ergodic
invariant measure, Birkhoff's theorem licenses a strong claim about such a
pair — the time average of a reading observable along one careful trajectory
equals the ensemble average over readers (Birkhoff 1931; Connaughton, Jeroen,
and Paillusson 2026 working notes). Literacy assessment lives on that license.
Nomothetic norms, grade bands, and "what a competent reader does" all treat the
individual as exchangeable with the ensemble for the observables that matter.

A platform is not a text. The feed that meets a user tomorrow depends on what
that user did today. Rankings, reputation, eligibility, and recommendations are
state variables of a mediator that couples back into the parties it coordinates.
The skew-product factorization fails: there is no exogenous driver that evolves
independently of the trajectories it drives. Stationarity is no longer free.
Ensemble metrics — A/B lifts, platform-wide averages, cohort success rates —
answer a different question from the one an individual creator, driver, or
worker needs answered. The ensemble mean of a multiplicative growth process is
dominated by rare trajectories; the time-average growth rate that a typical
trajectory actually lives is the logarithm's expectation, and Jensen's
inequality separates the two (Redner 1990; Peters and Gell-Mann 2016; Peters
2019). Optimizing expected reward is not optimizing the life the user leads.

That separation is the competence cut this lab already names in another
register. A coordination form is dyadic when its cause-effect structure factors
across the worker–system–counterpart partition (Φ_MIP = 0 under exact IIT-4.0);
it demands literacy. It is triadic when the structure stays irreducible
(Φ_MIP > 0); it demands algorithmacy. The ergodicity cut is the dynamical twin
of that structural cut. Literacy suffices when the environment is text-like:
exogenous driver, skew product, ensemble ≈ time average for the observables at
stake. Algorithmacy is required when the environment is platform-like:
back-coupled mediator, broken skew product, ensemble metrics that mislead the
individual trajectory. The claim is a candidate criterion, not a finished
theorem. It has to be tested — formally, on the lab's Boolean forms where
ergodic components are attractors and basins, and operationally, on logs where
Equality of Distributions and Equality of Averages are the testable rungs of a
weaker hierarchy (Connaughton et al. working notes §6).

Several consequences follow if the criterion holds. Creator success under
multiplicative reach is a Kelly problem, not an expected-value problem (Kelly
1956). Bans and demonetisation are absorbing boundaries; time-average decision
rules near ruin diverge from expected-utility rules that ignore absorption.
Filter bubbles are invariant sets; cold-start selects the component; the
recommender chooses which invariant measure makes a user look typical.
Infinite-scroll stickiness is a candidate neutral fixed point with heavy-tailed
return times. Recommender RL that maximises ensemble reward while users live
time averages is a structural misalignment, not a tuning error. Literacy exams
that assume exchangeability mis-assess learners in platform-like environments;
algorithmacy assessment has to be idiographic and longitudinal (Molenaar 2004;
Fisher 2026). Cross-sectional findings about "the average team" do not
automatically generalise to a given team's trajectory when coordination is
triadic.

The lab can begin where its instrument already reaches. Finite Boolean
coordination forms are deterministic maps; their invariant measures sit on
attractors; the ergodic components are those attractors and their basins. The
first cell asks whether triadic forms show different component and
time-vs-ensemble structure from dyadic forms, on panels the stoch–temporal arc
already knows how to run. Hypotheses are fixed first. The broader agenda —
forty questions across text vs platform, multiplicative growth, ruin, bubbles,
infinite ergodicity, operational tests, recommender RL, education, and
organizational coordination — lives under
[`../ergodicity/`](../ergodicity/).

## First results (in-silico only)

Computed on designed n=3 Boolean panels; evidence about models, not
organizations. Full tables in the study FINDINGS files.

- **B1–B3 / E4** (`studies/ergodic_components_vs_phi/`): verdict
  `NO_ERGODIC_SIGNATURE`. Mean components triadic 2.1429 vs dyadic 2.0000
  (H1 refuted); divergence fraction triadic 0.9333 vs dyadic 1.0000 (H3
  refuted). Coexistence cross-basin party split supported on 6/6 forms;
  multistable basins disagree on core or occupancy on 8/8 (E4).
- **A4** (`studies/ergodic_backcoupling_twins/`): `BACKCOUPLING_SPLITS` —
  skew-factor tracks convey vs accumulate; strong accumulating⇒triadic
  reading refuted (sticky is coupled and dyadic).
- **D4** (`studies/ergodic_absorbing_ejection/`): `ABSORBING_EJECTION` —
  ejected_latch hosts absorbing inactive dyadic `000` (basin 7) and triadic
  `111` (basin 1).
- **F4** (`studies/ergodic_sticky_returns/`): `HYSTERESIS_ONLY` — #109 gap
  0.0661 remains; sticky does not enlarge inactive-{000} mass or return
  times.
- **G2** (`studies/ergodic_eoa_vs_phi/`): `EOA_AGREES_PHI` — agreement 7/9;
  sticky is the FAIL×dyadic witness that EoA tracks multistability more
  tightly than Φ.

Theories: [`../ergodicity/THEORIES.md`](../ergodicity/THEORIES.md).
Experiments: [`../ergodicity/EXPERIMENTS.md`](../ergodicity/EXPERIMENTS.md).

## References

Birkhoff, G. D. 1931. Proof of the ergodic theorem. *Proc. Natl. Acad. Sci.
USA* 17(2): 656–660. doi:10.1073/pnas.17.2.656

Connaughton, C., Jeroen, and F. Paillusson. 2026. What is ergodicity? Working
notes (28/09/2026) for a *Phil. Trans. R. Soc. A* theme issue.
<https://github.com/colm-connaughton/ergodicity-intro>

Fisher, A. J. 2026. Beyond parametric ergodicity: A framework for structural
generalizability. *Phil. Trans. R. Soc. A* (theme issue; pagination pending).

Kelly, J. L., Jr. 1956. A new interpretation of information rate. *Bell Syst.
Tech. J.* 35(4): 917–926. doi:10.1002/j.1538-7305.1956.tb03809.x

Molenaar, P. C. M. 2004. A manifesto on psychology as idiographic science.
*Measurement* 2(4): 201–218. doi:10.1207/s15366359mea0204_1

Peters, O. 2019. The ergodicity problem in economics. *Nat. Phys.* 15:
1216–1221. doi:10.1038/s41567-019-0732-0

Peters, O., and M. Gell-Mann. 2016. Evaluating gambles using dynamics. *Chaos*
26(2): 023103. doi:10.1063/1.4940236

Redner, S. 1990. Random multiplicative processes: An elementary tutorial. *Am.
J. Phys.* 58(3): 267–273. doi:10.1119/1.16497
