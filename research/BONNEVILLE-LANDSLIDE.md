# Bonneville: testing whether landscape changes share a date

2026-10-08. C019, sourced draft; no independent review.

[Reynolds and colleagues (2022), S68](https://doi.org/10.1017/qua.2022.7) connect a landslide-buried tree with two upstream drowned trees. Their nine wood determinations and ring offsets are transcribed in [the sample ledger](../data/bonneville-dates.json), from visually inspected Table 1, p. 70. Methods and results on p. 78 were also visually checked.

Relative growth-pattern matching supports their same-death-year interpretation. Absolute placement uses IntCal20 and OxCal, moving calibrated sample distributions forward to the last growth ring before combining them. Perham Creek requires 25 inferred missing outer rings. The reported result is 1421–1455 CE at three sigma; nine assays do not constitute nine independent events.

Conditional on these assumptions, Bonneville was not caused by the 1700 earthquake. That narrows a proposed common regional catastrophe but neither dates Ozette nor identifies Bonneville's trigger. A hydrological trigger and earlier earthquakes remain alternatives.

Next: retrieve the ring-width supplement and model code, reproduce alignments and calibration, and test sensitivity to missing rings and sample treatment. Historical specimen custody and original laboratory records remain unaudited. No global-event conclusion follows from this comparison.

## Earlier determinations and sample treatment

[Nine older measurements](../data/bonneville-older-dates.json) are now transcribed from visually checked p. 69. These are the 2022 authors' compilation, not direct inspection of the older reports. Whole-round samples, fragments in underlying alluvium, reworked deposits and selected tree rings represent different dated objects. Their age spread cannot be treated as nine incompatible measurements of one burial instant.

The authors flag possible polyethylene glycol contamination for BON#1 and BON#2. Their new Powerhouse samples came from another section reported to show no preservative evidence. Chemical confirmation and treatment records have not been inspected here. A possible explanation is not a demonstrated correction.

Page 68 initially calls Minor's rejected determination 400 ± 70 BP, matching Table 1's Beta-9958 row, but later calls it 410 ± 50 BP. The latter matches BON#2's numerical result, assigned to different authors in the table. This discrepancy remains unresolved pending the originals. It does not establish intentional alteration of history.

## Correlation arithmetic audit

The publisher lists two supplementary workbooks, but the attempted download returned HTTP 403 and web retrieval could not access either file. Neither was analyzed. This limits reproduction, not evidence that the data are absent.

[The executable audit](../analysis/bonneville_correlation_audit.py) checks the 15 printed Table 3 rows using `t = r sqrt((n-2)/(1-r²))`. All are compatible with the displayed rounding of r and t. The visually inspected prose example on p. 75 instead gives n=50, r=0.3281 and t=3.5; the same formula produces 2.40635. This localized discrepancy does not invalidate the table or establish a different event date. No p-value, residual-autocorrelation or multiple-alignment significance audit has been completed. [Results](../analysis/bonneville-correlation-audit.json) retain that scope; raw-series alignment and calendar calibration remain unreproduced.
