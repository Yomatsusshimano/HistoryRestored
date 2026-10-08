# Highwall Wash: reproducible age summary, provisional reversal

SOURCED_DRAFT, 2026-10-08. Source S210, [Crow2021 supplement](https://doi.org/10.1130/GEOL.S.13530698.v1). This audit inspects Table2 selected summary rows, all36 Table6 specimen rows, and visually checks methods PDF pp6-7. No independent review or raw-data refit.

## Age arithmetic reproduced

Table2, `summary data`, rows24-42 contains19 selected ages with explicitly **one-sigma** uncertainties. Rows43-45 report a weighted mean with **two-sigma** uncertainty, MSWD1.13, and selection19 of151. Those conventions override the general methods default of two sigma.

Using these exact stored values gives:

| Quantity | Recomputed | Workbook |
|---|---:|---:|
| Inverse-variance mean, Ma | 5.353182864010134 | 5.353182864010134 |
| MSWD | 1.1292379476884036 | 1.13 |
| Internal two-sigma uncertainty, Ma | 0.0683806705067924 | Not separately asserted here |
| Two-sigma uncertainty multiplied by sqrt(MSWD), Ma | 0.07266513537557796 | 0.072665135375578 |

The computation uses weights1/sigma², internal standard error1/sqrt(sum(weights)), and chi-square divided by18 for MSWD. It reproduces the stored summary to floating-point precision. D43's formula doubles a stored constant; the archive recomputation instead derives it from the19 rows.

This is concrete evidence against reading the questionable methods sentence as proof that the authors used the inverse-age quantity sqrt(sum(weights)) for this result. The [earlier methods audit](CROW-SUPPLEMENT-AUDIT.md) remains a record of the textual discrepancy, now narrowed by a successful numerical check.

This reproduces **summary arithmetic**, not151 crystal analyses, the selection of19, isotope corrections, shared J covariance or the depositional interpretation. Table1 row4 gives5.3541 ±0.07Ma, a slightly different stored summary; preserve that version rather than silently equating it with Table2. The rounded5.35 ±0.07Ma statement does not expose the difference. Table3 was inspected for headers and selected initial rows only; the full interlaboratory crosswalk remains pending.

## What the magnetic records actually say

Table6 contains36 specimens from11 numbered site groups:1,2,3,5,6,7,8,9,10,11,12. The missing group4 is not a fabricated null measurement. Stored labels total23 normal,5 reverse,3 ambiguous and5 N/A. These counts are descriptive, not an independence-weighted vote or a reversal significance test.

PDF p6 places groups1-6 below the ash,7 within it and8-12 above. Figure1 on p7 marks the ash and an interpreted reversal immediately above it; this is an annotated outcrop photograph, not an independently surveyed age boundary.

The specimen records retain complexity that the prose summary compresses:

- HWW7-1, in the ash, is reverse with rankC.
- HWW8-1, above the ash, is reverse with rankA using AF/LTD; HWW8-2 is normal with rankB using thermal treatment. Figure2 and its caption explicitly identify8-1 as reverse. Therefore group8 cannot be described as uniformly normal.
- Group6 includes two reverse, three normal and one N/A specimen across different demagnetization treatments. Counting them alone cannot adjudicate the characteristic component.

Most decisively, p6 states that **the Highwall Wash reversal test fails**. The authors favor a reversal interpretation because group means overlap those from a positive test at nearby Lost Cabin Wash, citing Schwing2019. They explicitly request a larger Highwall Wash sample to determine whether the reversal exists and is statistically valid. This supports recording their proposed C3r-to-C3n.4n correlation as an interpretation, not an independently confirmed local time marker. Their account of pyrrhotite and inadequate thermal step resolution provides a stated methodological limitation; it has not been experimentally retested here.

Table6's footnote reports a single-outcrop coordinate32.381873,-114.574136. It is preserved verbatim in the data, with no datum supplied or independent geolocation established here. It is not promoted into the locality map or silently repaired.

## Reproduction and implication

[Structured records](../data/highwall-audit.json) preserve all selected ages, specimen labels, ranks, missing values and the source footnote. [Read-only extraction](../analysis/audit_highwall.py), requiring openpyxl:

```text
python analysis/audit_highwall.py path/to/supplement-directory data/highwall-audit.json
```

The script asserts agreement of mean, scatter-scaled uncertainty and rounded MSWD. That check validates this arithmetic only. Workbooks were neither modified nor rendered; no original demagnetization vectors were fitted.

A statistically provisional magnetic correlation does not supply a historical-era age. Conversely, matching an age summary is insufficient to date every Bouse fossil bed or establish a single global event. Next obtain Schwing2019's original reversal analysis and location metadata, reconcile Table1/Table2/Table3 sample versions, and tie the dated material to specific sediment beds before imposing a regional chronology.
