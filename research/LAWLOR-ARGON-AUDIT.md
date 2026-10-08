# Lawlor argon dating: recovered steps and unresolved calibration

2026-10-08. Source audit, not a reproduced eruption age or independent scientific review.

The original 2011 study's [USGS abstract record](https://pubs.usgs.gov/publication/70036324) (S197) explicitly reports the Lawlor result as 4.834 ± 0.011 Ma at one sigma. This specifies a previously unresolved uncertainty convention; it is not a hard youngest/oldest possible age. The abstract also reports revised ages older than previous K-Ar results. The full methods remain unrecovered: direct DOI access failed certificate validation, and the USGS page failed direct retrieval with HTTP 403. The institutional abstract was read through web-indexed retrieval, not a full-paper inspection.

## Original supplemental workbook

[S198](https://doi.org/10.1130/GES00609.S1) resolves to Figshare article 12180951, file 22398423, `609_SuppT01.xls` (98,816 bytes). SHA256: `64d4ae344cc82962d5249513e96e23628437e931c9e915de8cf3c1f549f26299`. Figshare metadata gives CC BY-NC 4.0 and identifies this as the paper's supplemental Excel table. It is the same study as S197, not independent confirmation.

Read-only extraction found one sheet, `Table`, 108 rows by 41 columns. The [public data](../data/lawlor-argon-rows.json) preserve all 35 Lawlor analysis rows, headers 1–6, and associated summary rows. CHANDON-1 analyses are outside this extraction's scope. Original workbook cells were read programmatically; no rendered-sheet inspection or formula recalculation is claimed.

| Run prefix | Sample | Worksheet analysis rows | Ordinary / explicitly omitted rows | Ordinary-step age range (Ma) |
| --- | --- | --- | --- | --- |
| 20975-01 | LAWL-1 | 9–15, 19–23 | 7 / 5 | 5.14–6.71 |
| 20954-01 | LAWL-2 | 26–34 | 9 / 0 | 3.20–4.87 |
| 20955-02 | LAWL-2 | 39–51, 55 | 13 / 1 | 4.20–4.95 |

“Ordinary” here means outside the workbook's explicitly omitted block. It does not establish the points used in the paper's final isochron. Repeated LAWL-2 labels identify two run prefixes, not two newly demonstrated independent field samples. All Lawlor rows give the locality as Lawlor Ravine on Bailey Road and material code P; mineral interpretation and sample correspondence must be checked against the full methods.

## What matters before refitting

- Rows 18 and 54 mark omissions for less than 2% argon-39 release. All six omitted rows remain public. For 20975-01, their combined stored moles constitute about 2.403% of all listed moles; for 20955-02, about 1.198%. A per-step threshold can omit a combined amount exceeding 2%. This is not evidence that the rule was violated.
- Column U has internal key `Ar39_CumPct`, but row 5 labels it argon-39 percent and row 6 says of total. Its individual values are nonmonotonic and sum to 100 within each ordinary block, excluding omitted rows. Treating this column as a cumulative fraction of all released gas would be wrong.
- Header rows distinguish scaling. For example, H/I give J and its error in units of 10^-3. The stored LAWL-1 H9 value 0.2665 therefore corresponds to J = 0.0002665. V/W use the 10^-5 label for the isotope ratio/error. The JSON deliberately retains stored cells and header rows; it does not silently unscale them.
- AJ/AK carry age and its printed one-sigma error; AL separately supplies error including J. AM is labelled external-error-inclusive internally but contains numeric zeros in the Lawlor analysis rows. Preserve these zeros as source content; do not infer zero external uncertainty or choose that column as a fit weight.
- LAWL-1 ordinary step ages are substantially scattered; summary cell AN17 stores MSWD 271.148, versus AN36 2.860 and AN53 1.283 for the two LAWL-2 blocks. These are stored worksheet summaries whose precise estimator is not established here. They must not be relabelled final isochron goodness-of-fit statistics without the method description.

A simple weighted average of the age column would neither reproduce an isochron regression nor justify choosing a plateau. The slope/intercept model, correlated isotope-ratio errors, atmospheric/trapped argon treatment, blanks, irradiation corrections, monitor age, decay constants, exclusions and propagation of shared uncertainty must be recovered first. The table makes these questions concrete; it does not resolve them by itself.

## Consequence for the catastrophe test

The dated source locality and the Bouse deposit are different locations. Even after the eruption age is reproduced, transferring it requires the chemical/zircon correlation, evidence of primary ash deposition rather than later reworking, and the measured stratigraphic relationship to the target fossil bed. The [oxygen audit](ZIRCON-OXYGEN-CHECK.md) advances the correlation link. Primary deposition and bed-specific transfer remain open in the [chronology audit](BOUSE-CHRONOLOGY.md).

Run `python analysis/extract_lawlor_argon.py path/to/609_SuppT01.xls` with xlrd 2.0.2 installed to reproduce the hash-checked extraction and descriptive accounting. This reads stored cell values, including cached formula results where present; it does not recover or execute workbook formulas. No eruption-age recalibration, physical historical coastline, global event date or independent validation is claimed.
