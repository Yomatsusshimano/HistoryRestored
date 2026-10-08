# Could Bonneville and Electron represent one short episode?

## Direct duration-constrained calculation

The [executed likelihood comparison](../analysis/regional_duration_fit.py) now supplements the interval geometry below. It uses the existing [Bonneville](BONNEVILLE-LANDSLIDE.md) and [Electron](ELECTRON-MUDFLOW.md) simplified calibrations. For each duration D it maximizes `log L_B(T_B) + log L_E(T_E)` subject to `abs(T_B - T_E) <= D`, then subtracts that maximum from the unrestricted maximum. Either event order is allowed. [Inputs, fitted dates and results](../analysis/regional-duration-fit-result.json).

| Maximum separation D | Full-data log-likelihood loss | Omit Perham Creek | Omit ELE01 |
| ---: | ---: | ---: | ---: |
| 0 years | 20.91 | 18.51 | 12.86 |
| 1 year | 20.88 | 18.46 | 12.70 |
| 10 years | 20.68 | 17.63 | 12.25 |
| 25 years | 16.95 | 12.58 | 12.25 |
| 50 years | 3.26 | 2.00 | 5.33 |
| 100 years | 0.00 | 0.00 | 0.11 |

Zero means the constraint admits an unrestricted optimum; larger losses mean worse maximum fit under the stated model. `exp(-loss)` is the relative maximum likelihood for that variant. These are **not p-values, Bayes factors, posterior model probabilities or probabilities that the catastrophe claim is false**. Different omission columns use different data and are sensitivity analyses, not independent replications. The slight plateau in the two-assay comparison is retained; no smooth relation was imposed.

Short-episode assignments incur substantial fit loss across these variants. The full-data unconstrained modes are 1438.5 and 1509 CE, a 70.5-year separation; a 100-year allowance therefore imposes no loss. None of this establishes a shared cause or continuous activity. Shared calibration errors, offset uncertainty, within-sample averaging, relative-ring alignment and specimen context remain unresolved. Independent Gaussian likelihood factors are a simplifying assumption, including across sites. A common calendar shift cannot remove the relative separation, but evidence-based differential revisions could change the result.

Synthetic Gaussian tests verify a known constrained optimum and reverse event ordering. [Grid refinement](../analysis/regional-duration-grid-check.json) checks numerical discretization separately from scientific validity. This is retrospective and does not count as a prospective prediction or independent discovery.

## Earlier comparison of published marginal intervals

2026-10-08. Retrospective comparison of C019 and C020; sourced draft without independent review. No new source discovery or date recalibration.

The unknown-date catastrophe proposal needs candidate periods that can fail a test. These two regional cases offer reported calendar estimates tied to trees interpreted as victims of landscape change. Unlike comparing a fossil's death with host sediment, this comparison asks whether the **reported tree-death windows** could fit one short episode, conditional on the authors' event associations.

[Bonneville's audit](BONNEVILLE-LANDSLIDE.md) records the S68 model intervals of 1426–1448 CE at two sigma and 1421–1455 CE at three sigma. [Electron's audit](ELECTRON-MUDFLOW.md) preserves differing intervals from S72's release abstract and S73's Figure S2. We retain every recorded variant at the matching nominal coverage; we do not select the version that best supports either explanation.

| Nominal marginal coverage | Electron version | Bonneville CE | Electron CE | Smallest window touching both |
| --- | --- | --- | --- | --- |
| 95.4% | Figure A, five samples | 1426–1448 | 1485–1516 | 37 years |
| 95.4% | Figure B, seven samples | 1426–1448 | 1494–1520 | 46 years |
| 99.7% | Figure A, five samples | 1421–1455 | 1476–1522 | 21 years |
| 99.7% | Figure B, seven samples | 1421–1455 | 1486–1528 | 31 years |
| 99.7% | Release abstract | 1421–1455 | 1477–1522 | 22 years |

For closed intervals [a,b] and [c,d], the minimum touching-window duration is max(0, max(a,c) − min(b,d)). The [script](../analysis/regional_event_windows.py) reads the existing ledgers, hashes its inputs and writes [results](../analysis/regional-event-windows-result.json). Its tests check interval geometry, not the validity of the chronology.

An instantaneous, one-year or ten-year episode cannot touch both intervals in any recorded variant. A 25-year window fits two of the three wider-interval comparisons but neither narrower-interval comparison; a 50-year window fits all five. These statements describe the reported sets. They are **not** lower confidence bounds on elapsed time or a statistical rejection probability: marginal intervals omit tails, date models have shared dependencies, and the intervals have not been independently reproduced. Five rows are not five independent tests.

The comparison therefore challenges assigning both tree-death episodes to one year or decade under these dating models. A multi-decade sequence remains geometrically possible but is not evidence of one cause, continuous flooding or a worldwide event. Treating one episode as later redeposition would require positive evidence and a separate depositional chronology; it changes the tested proposition.

Moving every calendar date by the same number of years cannot close these gaps. A chronology-rewriting proposal that attempts to align the cases must specify a differential correction and justify it using evidence independent of the desired match. The unresolved Electron versions, Bonneville missing-ring estimates and specimen histories are reasons to test the chronology, not measured corrections that can simply be applied.

This is a discovery-set comparison using already inspected evidence, not a prospective forecast. Next discriminators are original model inputs and sample custody for both sites, sensitivity to inferred outer rings, and independent dating/context checks. The result does not date Seattle fill, Ozette burial, wildlife extinction or historical attribution changes. The full twenty-part investigation remains incomplete.
