# Direct Nomlaki argon dating: a new control, separate from age transfer

2026-10-09. C005/S327; selected primary-methods audit without independent review.

Sarna-Wojcicki, Sullivan, Deino, Walkup, Wagner and Wan2021 report new Nomlaki and Putah analyses in GSA Memoir217, pp393-441, DOI10.1130/2021.1217(16). The main chapter was accessed as an [author-uploaded text portion](https://www.researchgate.net/publication/354421087_Late_Cenozoic_tephrochronology_of_the_Mount_Diablo_area_within_the_evolving_plate-tectonic_boundary_zone_of_northern_California); no main-page scan inspection is claimed. Its publisher-linked [original supplemental package](https://doi.org/10.1130/MWR.S.15149043.v2) supplies methods and data. AppS1PDF pages21-24 were visually inspected. TableS1XLSX header rows3/4, ROSER block86-95 and notes99-109 were read without editing, including the lab-ID font flags. Other workbook analyses and the full chemical-correlation database were not audited. No workbook layout rendering is claimed.

## What was dated

The methods describe pumice sample ROSER-2a from Dry Creek on the western Sacramento Valley margin, corresponding to DCNT-1 throughDCNT-3 chemical samples. Plagioclase grains, not a southern Bouse sediment sample, were separated and incrementally heated. One ROSER aliquot was analyzed; nine heating steps are nine measurements within that aliquot, not nine independent samples.

AppS1p21 identifies irradiation191, a Fish Canyon sanidine monitor at28.201±0.023Ma (1sigma) and multi-grain plagioclase aliquots. TableS1notes cite atmospheric40Ar/36Ar=298.56±0.31 and Min2000decay constants. Thus this direct analytical route differs from the older section-rate extrapolations, while retaining calibration and reduction assumptions. The experiment was not independently repeated here.

## Bounded plateau reproduction

The original workbook uses bold lab IDs to mark plateau inclusion. Rows90-94, steps20947-01D throughH, are marked; A/B/C/I remain retained in the [raw-cell record and calculation](../data/nomlaki2021-plateau.json). The [extractor](../analysis/nomlaki2021_plateau.py) checks the original MD5, preserves all nine rows and both header rows, then uses the marked subset. It does not select a more convenient subset.

| Quantity | Diagnostic from published derived values | Source comparison |
| --- | ---: | --- |
| Inverse-variance mean of selected step ages |3.314396Ma | AppS1Figure3f reports3.314Ma |
| Modified standard error, expanded by sqrt(MSWD) when needed |0.010769Ma | Rounds to Figure3f's0.011Ma |
| MSWD from these step ages/errors |1.154927 | Calculation only; not a reproduction of Figure4isochron MSWD |
| Selected39Ar fraction |76.169295% | Five consecutive steps meet the reported count/fraction requirements |
| First-order sharedJ contribution |0.004573Ma | Diagnostic; not five independentJ errors |
| Internal error plus that shared contribution in quadrature |0.011700Ma | Not asserted to reproduce the figure's uncertainty convention |

This reproduces rounded plateau summaries from already derived step ages. It does not redo raw gas extraction, interference corrections, decay calculations, or the search for the maximal acceptable plateau. The workbook's negative apparent age in the lowest-power step is retained rather than silently repaired or treated as a physical negative eruption age.

## The preferred age remains a different calculation

AppS1pp23-24 prefer inverse isochrons because they allow departure from assumed atmospheric trapped argon. Figure4e reports ROSER-2a age3.339±0.015Ma, trapped40Ar/36Ar intercept286.1±5.8, MSWD0.13, P0.94 andn5. The main chapter's exposed Table4instead reports3.339±0.016Ma under its1s-sem heading. The central age agrees; the uncertainty difference remains unresolved here. These are reports of the same analytical study, not independent confirmations.

At this audit stage, the preferred inverse-isochron calculation was not reproduced. The subsequent [correlated-error fit](NOMLAKI-ISOCHRON-CHECK.md) closely reproduces the reported intercept, scatter and error while retaining a small central-age conversion discrepancy. A matched plateau summary cannot substitute for that calculation. Its source probability and small scatter also do not independently authenticate the sample's emplacement, correlation or regional age transfer.

## Consequence for the reconstruction

The archive now has an original direct-dating control for a named Nomlaki sample, beyond the older indirect estimate. This is adverse evidence for assigning that sampled volcanic material a historical crystallization age while retaining the stated analytical premises. A younger deposit containing old volcanic material remains a different hypothesis requiring specimen-linked emplacement evidence.

The direct Dry Creek result does not resolve which [Willow Wash candidate](WILLOW-WASH-NOMLAKI.md) was selected, verify the Mohave Valley ash correlation or date Hart Mine Wash fossils. No target-bed age is assigned. The subsequent inverse-ratio fit advances the calculation check. Next recover original calibration/reduction settings and the correlation and primary-emplacement evidence linking the named controls to the northern sequence and exact southern target.
