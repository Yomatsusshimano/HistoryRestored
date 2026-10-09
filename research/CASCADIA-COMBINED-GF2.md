# GF2: complete third root radius and declared tree averages

2026-10-09. C004 / S61, S229, S231. This adds missing measurements and tests combined-radius choices. It does not reproduce the original spline/time-series processing or establish a calendar date independently.

## Complete the input before combining it

S61 PDF4, printed killed-cedar Page2, supplies GF2RTA from assigned1370–1699:330 positive widths in33 ten-value rows. The1700 value−9999 is a terminator, not a measurement. The [transcription script](../analysis/cascadia_third_root.py) and [ledger](../data/cascadia-third-root.json) preserve every row, source hash and page. The1690–1699 values agree exactly with the earlier terminal-only extraction. The large1541 width5126 micrometres is retained as printed. This is manually read and has no independent transcription review.

All three GF2 root radii are now transcribed completely: RTA330, RTB332 and RTC300 widths, totaling962 related measurements. Earlier [extraction](../data/cascadia-width-extract.json), corrections and result ledgers remain unchanged as historical records. Completion concerns this tree's three root radii, not all45 source pages or independent physical authentication.

S231 TableS1 reports a combined255-year trunk/root comparison with r=.57. Recovered trunk radii contain257/167/105 raw widths. Its footnote explicitly says time-series fitting lost some innermost rings. Consequently, a257-width raw comparison is not the published255-observation calculation. Selecting255 observations alone cannot reproduce it.

## Declared diagnostic

The [combined-average script](../analysis/cascadia_combined_gf2.py) hash-checks measurement inputs and publishes [all averages, radius counts and candidate scores](../data/cascadia-combined-gf2.json). Three separately declared transformations precede arithmetic averaging of available radii:

- Each radius divided by its whole-series mean.
- Adjacent log-width differences, centered and divided by that radius's sample standard deviation.
- Adjacent width differences, centered and divided by that radius's sample standard deviation.

For each, roots are averaged using all three radii or omitting each one in turn. Trunks use either all three available radii or NW alone. The root reference span is fixed at1400–1699 for widths,1401–1699 for differences, across omission choices. No missing values are filled. Each trunk is tested over its full span and, separately, its final255 observations. The latter is a count-matching sensitivity choice, not an inferred original AR model.

Every integer shift preserving complete target overlap is tested:44–46 candidates per comparison, depending on scope. This restricted within-tree domain is much smaller than a regional-reference search. Assigned calendars and the candidate specimen association are inherited from the source records. No probabilities are calculated.

## Results and limits

| Transformation, all root and trunk radii | Full target n | r at source-relative placement | Final255 r |
| --- | ---: | ---: | ---: |
| Mean-divided widths |257 |.53673 |.56251 |
| Standardized log differences |256 |.60692 |.60724 |
| Standardized width differences |256 |.55206 |.55309 |

All48 declared combinations rank the source-relative placement first within their tested domain, including omission of each root radius and NW-only comparisons. This supports the relative growth-pattern association under these choices. It does not supply48 independent confirmations: radii share wood, climate, assigned years and transformations. Neither choosing the r closest to .57 nor rounding a nearby result constitutes original-method reproduction.

Contribution counts matter: the full257-year trunk average uses only NW for90 years, two radii for62 years and three for105 years. The roots contribute three radii across the fixed reference span before omission. A nominal combined-tree series therefore does not have constant independent support.

Known-shift recovery, independent centered-dot-product correlation checks, arithmetic-average/count checks and per-radius tenfold unit-rescaling invariance passed. These check implementation, not the source calendar or earthquake history. Manual transcription, original decay/spline/AR settings, processed indices, physical root/trunk custody and absolute reference anchoring remain unresolved. This local result neither removes the regional-reference exceptions nor establishes a new catastrophe date.

Next recover original per-radius processed outputs and model orders, then compare actual combined indices/statistics. Do not replace missing settings by selecting the diagnostic that best resembles the published number. Independent specimen/anatomical authentication remains a separate requirement.
