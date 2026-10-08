# Colorado River burial dating: an independent measurement route

SOURCED_DRAFT, 2026-10-08. No independent review or reproduced isochron fit.

[Seong et al., S216](https://doi.org/10.18814/epiiugs/2024/024015) uses cosmogenic10Be–26Al burial dating on22 cobbles. The13-page [publisher PDF](https://pdf.medrang.co.kr/IUGS/2025/048/IUGS048-01-51.pdf) was recovered (SHA256 `144a94d32e26d41796c07f97e1b8976fcba5c5dd4285eda7de81e02f7781142c`). Online publication was2024-07-01; the issue is Episodes48(1),2025. Table2/printed57 was visually inspected; selected methods/results were text-read.

## Preserve source differences before fitting

| Site | Table2 age±1σ, Ma | Nearby prose/abstract age±1σ, Ma | Retained/total |
|---|---|---|---|
|Topock|2.02±0.24|2.12±0.26|4/6|
|Bat Cave|2.08±0.31|2.05±0.31|4/5|
|Santa Fe Railway|4.25±0.68|4.37±0.71|6/6|
|Palo Verde|3.03±0.26|3.03±0.26|3/5|

Table2 excludesTPK001/004, BC009 andPVD020/021 because their reported ratios exceed6.75. Its aluminium concentration header reads27Al although its title and ratio concern26Al. All22 rows and both age versions are preserved in [structured records](../data/colorado-burial-rows.json). Numeric concentration quotients correspond to the listed ratios, but that is not authority to silently change the isotope header.

The method assumes source-basin steady-state erosion, rapid transport and common post-burial history among cobbles at equal depth. Those assumptions and post-burial production matter to the fitted ages.

## Relevance to the catastrophe test

This is a different measurement route from zircon or sanidine crystallization dating. It targets burial history through cosmogenic nuclide concentrations, so it can address a gap left by inherited mineral ages. It is not automatically an independent confirmation of every regional age: some authors overlap with the earlier studies, geological unit assignments share previous mapping, and the model has physical assumptions to test. Distinct measurements, shared interpretation and independent replication are different properties.

The published million-year burial results, if their sample contexts and model hold, challenge a recent single-burial interpretation for these sampled deposits. A hypothesis of recent movement of previously buried cobbles must instead specify whether that process could preserve the observed inter-cobble relationship, shielding history and sedimentary context. Merely observing that a cobble can be reworked does not reproduce those measurements; merely obtaining a linear fit would not prove a unique burial history either.

The three table/prose differences are reproducibility issues, not demonstrated fraud or evidence for a young chronology. Neither version will be silently selected as the correct one. The source's exclusions also require explicit sensitivity analysis, especially where only three points remain. They must not disappear from the public record.

Next trace Figure4 slopes, correction equations, concentration errors and covariance; reproduce both retained-sample fits and declared exclusion sensitivity; then evaluate each site's burial context. No regressions, original AMS validation, historical-age rejection probability or global-event model are claimed in this first audit.


## Figure and equation check

S216 printed56/PDF6 and Fig4 printed59/PDF9 were visually inspected. Figure4 agrees with the prose for Topock, Bat Cave and Santa Fe, but gives **Palo Verde3.04±0.34Ma**, versus3.03±0.26 in both table and prose. Thus all four sites now have a documented age-summary difference somewhere in the paper. The figure describes a Bayesian fit using100,000 simulations, retained points, propagated measurement/production uncertainty and an erosion-corrected initial ratio. Those implementation details have not been reproduced.

Equation5 prints `t = tau ln(Rm/Rinh)`, with tau positive at approximately2.07Ma. Every plotted slope is below the stated nominal initial ratio6.75, so literal substitution gives a negative age. From `Rm = Rinh exp(-t/tau)`, algebra instead gives `t = tau ln(Rinh/Rm)`. This identifies a sign/ratio-order inconsistency in the printed equation, not proof that the unpublished calculation used the wrong sign.

| Site | Figure slope | Literal printed equation, Ma | Decay-consistent nominal calculation, Ma |
|---|---:|---:|---:|
|Topock|2.39|−2.149|2.149|
|Bat Cave|2.47|−2.081|2.081|
|Santa Fe Railway|0.79|−4.441|4.441|
|Palo Verde|1.63|−2.941|2.941|

[The script](../analysis/check_burial_slope_ages.py) and [output](../data/burial-slope-age-check.json) preserve both calculations. These use rounded slopes, approximate tau and a fixed6.75 initial ratio; they intentionally do not pretend to reproduce the erosion correction or Bayesian fit. Their differences from reported ages must not be called failed reproductions of an algorithm that has not been recovered.

For diagnosis only, solving the decay-consistent relation backward from the figure ages yields implied initial ratios6.656,6.650,6.523 and7.079 respectively. Those numbers are algebraically fitted to the published answers. They are not independent estimates of source erosion or validation of any correction. In particular, the Palo Verde value merits checking against the actual correction parameters rather than silently selecting a different age version to make it fit.

The physically meaningful audit remains open: recover the MATLAB implementation, priors and post-burial/erosion corrections, reproduce Figure4 from the22 preserved measurements, then examine exclusion sensitivity and field histories. Documentation discrepancies narrow the reproducibility task; they do not by themselves establish a different burial time or historical catastrophe.


## Exclusion sensitivity: point cutoff versus uncertainty

The source excludes five points because their measured ratios exceed6.75. We tested that rule against the published errors without changing the source selection. For each point define `D = N26 - 6.75*N10`. With measurement covariance set to zero, `sigma_D = sqrt(sigma26² + 6.75²*sigma10²)`. This uses the aluminium column as26Al conditionally, preserving its printed-header warning.

| Excluded sample | D/sigma_D, fixed6.75 | Including a3% initial-ratio uncertainty term |
|---|---:|---:|
|TPK001|4.56|4.41|
|TPK004|2.88|2.62|
|BC009|4.84|4.69|
|PVD020|2.74|2.43|
|PVD021|0.49|0.47|

PVD021 is not well separated from the cutoff under these assumptions: the threshold lies within one propagated measurement standard deviation. That is a reason to examine the exclusion's effect, not proof that the grain shares the modeled history. The other four are farther above the cutoff. These scaled residuals are not calibrated rejection probabilities; covariance and full analytical error structure remain unknown. The3% production-ratio term is shared model uncertainty, not five independent additional measurements.

For a transparent sensitivity diagnostic, we fitted `N26 = intercept + slope*N10` using inverse aluminium-error variance weights. The Palo Verde source-retained three points yield slope1.63558. Restoring PVD021 gives1.42366; including all five gives2.29957. [Code](../analysis/check_burial_exclusions.py) and [results](../data/burial-exclusion-check.json) retain every membership choice.

These are deliberately limited weighted least-squares calculations: they treat10Be as exact and omit covariance, Bayesian priors, erosion correction and full post-burial modeling. The three-point slope's proximity to the published1.63 is a useful arithmetic comparison, not replication of the authors' method. No ages are inferred from these diagnostic slopes. The membership choices materially change the slope, so a robust age assessment must carry the selection alternatives through the complete model rather than report only the retained fit.

Next prioritize recovery of the original fitting implementation and the sample-specific reason for rejecting PVD021 beyond its central ratio. Keep physically different histories and analytical uncertainty as separate possible explanations until tested.
