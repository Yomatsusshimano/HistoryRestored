# Zircon oxygen comparison: Bouse, Lawlor and Pre-Kilgore

2026-10-08. Retrospective descriptive audit; no independent scientific review or new dating.

The oxygen measurements in [Harvey's supplement, S196](https://doi.org/10.1130/GES00904.S1) provide a compositional test beyond age similarity. Bouse values overlap the Lawlor range and are generally higher than Pre-Kilgore values. This supports investigating the proposed Lawlor correlation, but neither range overlap nor a contrast with one alternative uniquely identifies an eruption.

## Inputs and provenance

Pages 1–3 supply the previously [transcribed Bouse and Lawlor rows](../data/harvey-zircon-rows.json). Page 5 supplies all 24 [Pre-Kilgore rows](../data/harvey-prekilgore-rows.json), now visually checked. The retained seven-page PDF has SHA256 `f8471d7875cd50542ad1f99af53581512f739e76063316933ef17b5340100e46`.

Nine Pre-Kilgore rows bear the table's double-star attribution to Watts et al. (2011); fifteen are unmarked. This is a source-marker split, not proof of independent experimental batches. HS14-2 occurs twice, once in each category; both entries remain with distinct row keys. Do not interpret 24 rows as 24 proven independent crystals. Three oxygen pairs are missing: HS14-1 and the prior HS14-2 use dashes, while HS14-24 is blank. These remain null, never zero.

## Descriptive results

All summaries are unweighted and include every available oxygen value within each listed group. Values are in per mil. No missing measurements are estimated and no high or low values are excluded.

| Group | Table rows | Oxygen values | Missing | Mean | Median | Minimum–maximum |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Bouse | 51 | 12 | 39 | 6.923 | 7.080 | 5.92–7.47 |
| Lawlor | 52 | 20 | 32 | 6.628 | 6.660 | 5.77–7.59 |
| Pre-Kilgore, all | 24 | 21 | 3 | 2.409 | 1.960 | 0.44–5.52 |
| Pre-Kilgore, unmarked | 15 | 13 | 2 | 2.143 | 1.880 | 0.44–5.52 |
| Pre-Kilgore, prior-source marked | 9 | 8 | 1 | 2.840 | 2.205 | 0.89–5.45 |

Both Pre-Kilgore subsets retain a lower descriptive mean than Bouse. Thus the broad contrast is not created solely by including the marked prior-source rows. These selected analyses and unequal missingness do not estimate unbiased population distributions.

## Where the separation weakens

The point-value gap between the closest Bouse and Pre-Kilgore measurements is 0.40 per mil: Amboy_r2-4 is 5.92 ± 0.15 and unmarked HS14-19 is 5.52 ± 0.18, with printed one-sigma errors. Their value ± two-sigma intervals are [5.62, 6.22] and [5.16, 5.88], which overlap. Four Bouse/Pre-Kilgore pairs overlap by this interval rule:

| Bouse row | Pre-Kilgore row |
| --- | --- |
| Amboy_r2-4 | HS14-8, prior-source marked |
| Amboy_r2-4 | HS14-19, unmarked |
| Buzzard_R3-15 | HS14-8, prior-source marked |
| Buzzard_R3-15 | HS14-19, unmarked |

This is a transparent sensitivity check, not a joint confidence calculation, statistical equivalence test or source-assignment probability. It prevents an overstatement that every grain is separated beyond its printed measurement error. Conversely, a few overlapping intervals do not erase the overall distribution contrast.

The all-row Bouse–Pre-Kilgore mean difference is 4.515 per mil. It does not exactly reproduce the approximately 4.8 difference reported in the main-paper material previously retrieved as S195. The paper's precise selection and summary method must be recovered before treating those two differently defined summaries as a contradiction or a replication.

## Implication for the geography claim

A compositional match can strengthen a tephra correlation without establishing primary deposition, its eruption age, the age of every fossil bed, or a historical coastline. This audit challenges an argument that similar zircon ages alone make Lawlor and Pre-Kilgore indistinguishable. It does not establish a unique source among all possible eruptions, a global chronology, or the historical map's proposed waterway.

Run `python analysis/zircon_oxygen_check.py` to reproduce the [saved output](../data/zircon-oxygen-check.json). The script uses the published one-sigma fields as printed; analytical covariance, standards, calibration and the full main-paper selection discussion remain unaudited. Other candidate groups remain pending. Next connect source discrimination to the eruption-age calibration and bed-specific primary-deposition evidence in the [Bouse chronology audit](BOUSE-CHRONOLOGY.md).
