# Fish Creek upper tuffs: grain selection and age transfer

SOURCED_DRAFT, 2026-10-08. No independent review.

## Source record

[S214, Dorsey et al.2011](https://pages.uoregon.edu/rdorsey/Downloads/DorseyEtal2011.pdf) Table1, printed777/PDF7, was visually checked; methods and results on printed777,780,782 were text-read. Samples02-440/02-441 occur at4454/4488m section height. SHRIMP zircon ages are reported as2.65±0.05 and2.60±0.06Ma, with95% confidence limits; individual table errors are one sigma. The authors interpret crystallization ages. They exclude grain6 from the lower sample; from the upper they exclude old grains7/10, approximately3Ma grains11/19, and younger grain3. Rounded and fresh-looking grains coexist in the upper sample. Table notes omit0.39% standard-calibration error from individual uncertainties; disequilibrium correction assumes magmaTh/U=2.25. The latter derives from proposed source analogues, not a measured melt in these samples.

The table labels its groups TAL6071/6073. Their order, counts and distinctive excluded ages support correspondence to02-440/02-441 in the prose; a laboratory custody crosswalk has not been recovered.

## Rounded-data reproduction

[Structured records](../data/fish-creek-tuff-ages.json) preserve all35 tabulated age/error pairs, including excluded rows. [The script](../analysis/audit_fish_creek_tuffs.py) uses inverse-variance weights on those rounded values.

| Calculation | Lower group | Upper group |
|---|---:|---:|
| Selected count |17|12|
| Calculated mean, Ma |2.647907|2.596631|
| Calculated MSWD |1.292324|0.976567|
| Reported mean, Ma |2.65|2.60|
| Reported MSWD |1.3|0.97|
| Internal two-sigma half-width, Ma |0.036137|0.053830|
| Reported95% half-width, Ma |0.05|0.06|

Means agree at reported precision. The upper calculated MSWD rounds to0.98 rather than0.97; original unrounded inputs have not been reproduced. Internal two-sigma errors are not substituted for the source's95% confidence limits. Calibration, covariance, scatter scaling and confidence-interval procedures need a separate complete audit before claiming exact uncertainty reproduction.

A narrowly defined sensitivity check restores only lower grain6 or upper grain3 to the respective selected group. Means become2.659224 and2.581322Ma, with MSWD1.811895 and1.294287. The shifts are about+11,317 and−15,309years. This tests those particular exclusions, not every possible grain-selection or correction model. It does not demonstrate a historical age or justify pooling obviously different populations. Selection should be justified by analytical and geological criteria independently of the preferred chronology.

## Consequence for the regional argument

These calculations strengthen traceability of the reported mineral-age anchors; they are not a new laboratory determination. Their use as sediment ages still requires the eruption-to-deposition link. Crystal appearance, a clustered population and an ash-like bed can inform that test, but this audit has not established a numerical maximum lag or verified the complete field setting. Reworking must be evaluated from the deposit, not invoked merely because a date is inconvenient.

If original depositional context establishes primary ash deposition close to crystallization, securely underlying strata acquire an older-than constraint from the overlying dated beds. If the grains are inherited into a substantially younger deposit, that inference needs revision. Neither conditional statement establishes the actual alternative. A model of repeated lower beds must preserve valid upper constraints and physical ordering rather than discard them by association with a disputed magnetic correlation.

Next inspect field descriptions/photos of both ash beds, the original sample/lab identifiers, and the full calculation of common-Pb, disequilibrium and calibration uncertainty. Keep the [age-model dependency audit](FISH-CREEK-AGE-MODEL.md) separate from this selected-grain arithmetic.
