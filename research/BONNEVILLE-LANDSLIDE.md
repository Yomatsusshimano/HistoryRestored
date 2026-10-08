# Bonneville: testing whether landscape changes share a date

2026-10-08. C019, sourced draft; no independent review.

## External calendar placement

[Pringle and colleagues' 2021 abstract, S69](https://gsa.confex.com/gsa/2021AM/webprogram/Paper369596.html) reports a provisional final ring in 1446 and death during the following dormant season. It adds external chronology comparisons to the relative three-tree alignment, including Big Lava Beds, a nearby old tree, two unpublished Oregon chronologies and Electron Mudflow trees. These are reported comparisons, not newly reproduced results.

[NOAA study 2900, S70](https://www.ncei.noaa.gov/access/paleo-search/study/2900) supplies a candidate: Brubaker's WA027 Lava Beds. Three files were downloaded and hashed in [the acquisition record](../data/bonneville-reference-candidate.json). The measurement template spans 1397–1976 with 30 series columns; the chronology header ends in 1975. Six series have values for 1446; series must not be counted as independent trees. The abstract supplies no archive identifier, so exact reference identity remains unconfirmed. This is a concrete route toward replication, not confirmation of 1446.

[Coverage analysis](../analysis/bonneville_reference_coverage.py) gives at most 50 years ending in 1446. Only one series spans all 50; five others supply 49, 39, 28, 6 and 3 years. This does not establish the strength of a match.

[NOAA's 1994 quality report, S71](https://www.ncei.noaa.gov/pub/data/paleo/treering/measurements/correlation-stats/wa027.txt) flags 29 problem segments and two potentially misdated series. It explicitly concerns raw measurements, not the chronology. Series 731091 has weak early correlations; a comment's row-17 identifier disagrees with the table. Details and scope are retained in [the quality ledger](../data/bonneville-reference-quality.json). The next test must establish which reference version and exclusions were used before interpreting these flags as affecting the Bonneville result. No automatic removal, redating or rejection is justified here.

[Reynolds and colleagues (2022), S68](https://doi.org/10.1017/qua.2022.7) connect a landslide-buried tree with two upstream drowned trees. Their nine wood determinations and ring offsets are transcribed in [the sample ledger](../data/bonneville-dates.json), from visually inspected Table 1, p. 70. Methods and results on p. 78 were also visually checked.

Relative growth-pattern matching supports their same-death-year interpretation. Absolute placement uses IntCal20 and OxCal, moving calibrated sample distributions forward to the last growth ring before combining them. Perham Creek requires 25 inferred missing outer rings. The reported result is 1421–1455 CE at three sigma; nine assays do not constitute nine independent events.

Conditional on these assumptions, Bonneville was not caused by the 1700 earthquake. That narrows a proposed common regional catastrophe but neither dates Ozette nor identifies Bonneville's trigger. A hydrological trigger and earlier earthquakes remain alternatives.

Next: retrieve the ring-width supplement and model code, reproduce alignments and calibration, and test sensitivity to missing rings and sample treatment. Historical specimen custody and original laboratory records remain unaudited. No global-event conclusion follows from this comparison.

## Earlier determinations and sample treatment

[Nine older measurements](../data/bonneville-older-dates.json) are now transcribed from visually checked p. 69. These are the 2022 authors' compilation, not direct inspection of the older reports. Whole-round samples, fragments in underlying alluvium, reworked deposits and selected tree rings represent different dated objects. Their age spread cannot be treated as nine incompatible measurements of one burial instant.

The authors flag possible polyethylene glycol contamination for BON#1 and BON#2. Their new Powerhouse samples came from another section reported to show no preservative evidence. Chemical confirmation and treatment records have not been inspected here. A possible explanation is not a demonstrated correction.

Page 68 initially calls Minor's rejected determination 400 ± 70 BP, matching Table 1's Beta-9958 row, but later calls it 410 ± 50 BP. The latter matches BON#2's numerical result, assigned to different authors in the table. This discrepancy remains unresolved pending the originals. It does not establish intentional alteration of history.

## Simplified radiocarbon implementation check

The [executed calculation](../analysis/bonneville_calibration_check.py) uses the nine preserved assays and ring offsets with the [official IntCal20 curve, S128](https://intcal.org/curves/intcal20.14c). For each candidate death year T, the sample centroid has calendar BP `1950 - T + offset`. Curve means and standard deviations are linearly interpolated. Gaussian likelihoods use assay variance plus curve variance and are multiplied over samples, with a uniform prior on 1–1950 CE. Offsets are fixed. [Hash-pinned results](../analysis/bonneville-calibration-check-result.json).

| Omitted tree | Assays retained | Mode CE | Equal-tail 95.4% interval CE |
| --- | ---: | ---: | --- |
| None | 9 | 1438.50 | 1426.50–1446.00 |
| Powerhouse | 7 | 1439.25 | 1423.75–1447.00 |
| Wyeth | 5 | 1433.50 | 1422.25–1446.75 |
| Perham Creek | 6 | 1440.75 | 1427.25–1450.25 |

Decimals identify numerical grid positions, not dating precision. The full-data 99.7% equal-tail interval is 1422–1451 CE. Halving grid spacing from 0.25 to 0.125 year changes reported interval endpoints by no more than 0.25 year ([grid check](../analysis/bonneville-calibration-grid-check.json)); interpolation and a synthetic Gaussian summary also pass numerical tests.

This approximate placement agrees broadly with the published mid-fifteenth-century result. Its persistence without Perham Creek shows that this simplified fit is not driven solely by that tree's inferred outer rings. **This is not an OxCal reproduction or an independent chronology.** It omits offset uncertainty, within-sample ring averaging, curve covariance and assay dependence. Equal-tail intervals need not match the authors' interval construction. Raw ring alignment, specimen context and calibration-curve validity remain inputs, not results of this check. No probability of a worldwide catastrophe is computed.

## Earlier correlation arithmetic audit

The publisher lists two supplementary workbooks, but the attempted download returned HTTP 403 and web retrieval could not access either file. Neither was analyzed. This limits reproduction, not evidence that the data are absent.

[The executable audit](../analysis/bonneville_correlation_audit.py) checks the 15 printed Table 3 rows using `t = r sqrt((n-2)/(1-r²))`. All are compatible with the displayed rounding of r and t. The visually inspected prose example on p. 75 instead gives n=50, r=0.3281 and t=3.5; the same formula produces 2.40635. This localized discrepancy does not invalidate the table or establish a different event date. No p-value, residual-autocorrelation or multiple-alignment significance audit has been completed. [Results](../analysis/bonneville-correlation-audit.json) retain that scope; raw-series alignment and calendar calibration remain unreproduced.
