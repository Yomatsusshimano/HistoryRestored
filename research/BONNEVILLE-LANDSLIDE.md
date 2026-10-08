# Bonneville: testing whether landscape changes share a date

2026-10-08. C019, sourced draft; no independent review.

[Reynolds and colleagues (2022), S68](https://doi.org/10.1017/qua.2022.7) connect a landslide-buried tree with two upstream drowned trees. Their nine wood determinations and ring offsets are transcribed in [the sample ledger](../data/bonneville-dates.json), from visually inspected Table 1, p. 70. Methods and results on p. 78 were also visually checked.

Relative growth-pattern matching supports their same-death-year interpretation. Absolute placement uses IntCal20 and OxCal, moving calibrated sample distributions forward to the last growth ring before combining them. Perham Creek requires 25 inferred missing outer rings. The reported result is 1421–1455 CE at three sigma; nine assays do not constitute nine independent events.

Conditional on these assumptions, Bonneville was not caused by the 1700 earthquake. That narrows a proposed common regional catastrophe but neither dates Ozette nor identifies Bonneville's trigger. A hydrological trigger and earlier earthquakes remain alternatives.

Next: retrieve the ring-width supplement and model code, reproduce alignments and calibration, and test sensitivity to missing rings and sample treatment. Historical specimen custody, original laboratory records and earlier determinations remain unaudited. No global-event conclusion follows from this comparison.

## Correlation arithmetic audit

The publisher lists two supplementary workbooks, but the attempted download returned HTTP 403 and web retrieval could not access either file. Neither was analyzed. This limits reproduction, not evidence that the data are absent.

[The executable audit](../analysis/bonneville_correlation_audit.py) checks the 15 printed Table 3 rows using `t = r sqrt((n-2)/(1-r²))`. All are compatible with the displayed rounding of r and t. The visually inspected prose example on p. 75 instead gives n=50, r=0.3281 and t=3.5; the same formula produces 2.40635. This localized discrepancy does not invalidate the table or establish a different event date. No p-value, residual-autocorrelation or multiple-alignment significance audit has been completed. [Results](../analysis/bonneville-correlation-audit.json) retain that scope; raw-series alignment and calendar calibration remain unreproduced.
