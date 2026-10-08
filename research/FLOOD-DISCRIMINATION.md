# What distinguishes repeated flooding from a short pulsed event?

2026-10-08. Retrospective synthesis of C008/C024. Proposed tests and conditional geometry; no independent review or new field observations.

**Repeated sedimentary units, independently initiated floods and elapsed years are three different quantities.** The present archive contains evidence of changing deposition and recorded magnetic directions. It does not yet independently reproduce the inferred millennial chronology. That gap neither validates one short event nor removes the observations a short-event model must explain.

## Evidence that each model must explain

| Observation or reported relationship | Obligation for a short pulsed-inundation model | Obligation for a separated-flood model | Present discriminating power |
| --- | --- | --- | --- |
| Sanpoil intervening sediment, opposed current indicators and correlated sections | Account for settling, flow reversals, lateral correlations and erosion with a physically specified hydrograph | Demonstrate the correlations and seasonal interpretation instead of equating every lamina with a year | Distinct depositional conditions reported; numerical duration still conditional on annuality and correlation ([audit](MISSOULA-STRATIGRAPHY.md)) |
| Touchet pre-ash magnetic-direction changes | Explain the changes through field evolution, changing recording conditions or bed-specific disturbance, with measurements | Demonstrate original-field recording and independently constrain the direction-to-time conversion | Quantified angular contrast; no reproduced age bound ([audit](TOUCHET-MAGNETIC-AUDIT.md)) |
| Chemically different Sg/So ash layers | Explain emplacement and preservation in the nominated sequence | Establish the relevant eruption interval and its transfer to the flood sections | Chemical distinction does not itself measure years; original core chronology pending ([audit](SET-S-TEPHRA-AUDIT.md)) |
| Moxee gradational contacts and terminating/crossing dikes | Explain changing deposition and deformation within inundation | Distinguish actual truncation and exposure from propagation arrest or later reactivation | Relative sequence, without an independently resolved count of lake drainings ([audit](MOXEE-FLOOD-COUNT.md)) |
| Water volume, discharge and duration in the published pulse proposal | Reconcile all three at the same control section, including other routes/storage | Supply equally explicit routed volumes and hydrographs for repeated events | Existing capacity inequality challenges a specified parameter combination, not all pulse models ([audit](MISSOULA-PULSE-ALTERNATIVE.md)) |

These are requirements for competing explanations, not declarations that one missing measurement favors the other account. Site-specific observations cannot be transferred to another section without a correlation argument.

## A quantitative target for the magnetic recording question

For two unit-vector directions separated by angle `theta`, with printed cone radii `a` and `b`, the uncovered separation is:

`g = max(0, theta - a - b)`.

If the cones are treated as geometric regions, arbitrary extra endpoint displacements with total allowance `g` permit them to touch along the shortest connecting arc. Splitting the allowance equally requires `g/2` at each endpoint. This is an investigator-derived sensitivity calculation, **not an estimate of actual error**, a confidence interval, or a model of sediment magnetization.

| Selected pair | Additional total allowance, degrees | Equal allowance per endpoint, degrees |
| --- | ---: | ---: |
| Touchet -5 to zero row 23 | 3.470 | 1.735 |
| Touchet -5 to zero row 24 | 0.000 | 0.000 |
| Burlingame -5 to zero row 11 | 2.460 | 1.230 |
| Zillah -5 to zero row 02 | 10.608 | 5.304 |
| Zillah -5 to zero row 03 | 8.013 | 4.006 |

All duplicate zero rows are retained. Repeated comparisons share rows, and a separate displacement chosen for each pair need not be compatible with a single joint model. Printed alpha95 cones are marginal statistical summaries, not guaranteed error bounds. An overlapping pair is not proof of equal directions.

A common rigid rotation `R` cannot remove any gap: `(R u) dot (R v) = u dot v`. Thus a single orientation rotation applied equally to both beds cannot explain their separation. Differential core rotation, deformation or recording effects could alter it, but their magnitude and pattern need evidence. This distinction does not dismiss all orientation problems; it identifies which kind is relevant.

Even after establishing genuine geomagnetic change, elapsed time needs an external rate constraint or a dated reference trajectory. No maximum field-change rate is established here. A pointwise instantaneous-recording model with validated maximum angular rate `omega` and valid error bounds could imply `duration >= g/omega`; neither those premises nor the effect of delayed/averaged sedimentary recording have been validated. Do not insert a modern typical rate as an upper bound or report a numerical duration from this formula.

Run `python research/check_touchet_directions.py`; [saved output](../analysis/touchet-direction-sensitivity.json) pins the existing S167 transcription. No additional source measurements are introduced.

## Priorities that could change the assessment

1. Recover specimen orientations, demagnetization trajectories and deformation observations at the selected horizons. Evaluate whether a physically justified *differential* recording model explains all three sections, including the overlapping pair.
2. Recover the exact extended Fish Lake input and dated-material controls used in 2003. The [NOAA series](NOAA-LAKE-RECOVERY.md) is too short for the described overlap; [later recalibrated versions](FISH-LAKE-REFERENCE-AUDIT.md) are not interchangeable substitutes.
3. Recover the Little Boulder Lake core and the eruption-order evidence required to transfer an Sg–Sg interval to Sg–So. A plausible separation is not a measured lower bound.
4. Test annuality and physical event separation against original section fabrics and independently dated intervening material, while distinguishing reworked material from in-place growth or deposition.

This comparison does not establish a recent worldwide catastrophe or historical fabrication. It keeps local observations usable while making the unresolved model assumptions explicit. It is retrospective; none of these already-inspected observations is a held-out prediction.
