# Crow2021 supplement: calibration and Lawlor table audit

SOURCED_DRAFT, 2026-10-08. No independent scientific review.

The [original supplemental package](https://doi.org/10.1130/GEOL.S.13530698.v1) (S210) provides an 11-page methods PDF and six workbooks. All seven files were recovered through the Figshare API with ordinary certificate validation. The [manifest](../data/crow-supplement-files.json) preserves download URLs, sizes, hashes and inspection depth. Main paper S209 remains abstract-only; supplemental access does not verify its proposed fault duplication or complete revised regional chronology.

## Calibration and uncertainty

PDF pages1-2 were visually inspected. The New Mexico laboratory section assigns Fish Canyon FC-2 sanidine 28.201 Ma and uses a total potassium-40 decay constant of 5.463e-10/year. It describes single-crystal fusion, flux-monitor fitting and selection of a youngest crystal group using dispersion. The authors acknowledge judgment in that selection. They report including J uncertainty, inflating errors by sqrt(MSWD) when MSWD exceeds one, and using two-sigma errors unless otherwise specified.

The prose describes the weighted-mean error as sqrt(sum(1/sigma²)). As written, that has inverse-age units. For independent age measurements, the standard internal error is instead 1/sqrt(sum(1/sigma²)). This is a dimensional inconsistency in the text, potentially an omitted reciprocal. It does **not** demonstrate which equation their software used or invalidate the reported ages. The two-sigma convention must also be respected when reproducing calculations.

## Lawlor recalculation is a distinct version

Table1, Sheet1 rows20-24 stores the following values in Ma. Both error columns are labeled two sigma. These are reported workbook values, not newly derived isotope ages.

| Sample / summary | Published-age column | Recalculated-age column |
|---|---:|---:|
| 20954-01p, Berkeley | 4.843 ±0.032 | 4.874 ±0.032 |
| 20955-02p, Berkeley | 4.833 ±0.026 | 4.864 ±0.026 |
| 758-318Xp, Menlo Park | 4.670 ±0.060 | 4.756 ±0.060 |
| Berkeley summary | 4.865 ±0.0212 | 4.865 ±0.0212 |
| All-ages summary | 4.8566 ±0.0483 | 4.8566 ±0.0483 |

Row23 is underlined; row64 explains that underlining identifies preferred ages. The identical summary entries in both columns should not be mistaken for two independent estimates or for an original unrecalibrated summary. These cells are stored numbers, not executable formulas. The source labels the sample suffix p as plagioclase. Its monitor column and footnote retain the original/recalculated standard distinctions; these have not been reconstructed from raw isotope measurements.

A deliberately limited inverse-variance calculation from H20:H21 and I20:I21 gives **4.86797647 Ma**, with internal two-sigma error **0.02017896 Ma** under independence. This does not reproduce row23's 4.865 ±0.0212. Shared calibration covariance, underlying unrounded inputs, selection and the actual summary calculation remain unaudited. Consequently the computed value is a diagnostic, not a replacement preferred date. The underlying sample relationship to S198 also needs an explicit crosswalk.

The auxiliary Sheet2 contains **17 formulas with broken #REF! references**, including the Lawlor plotting row10. These are not zeros or missing isotope measurements. This limits reproduction from that auxiliary sheet; it does not show that the published figure or underlying analyses used those broken references.

[Extracted cells and calculation](../data/crow-lawlor-recalibration.json) retain values, row addresses and underline metadata. [Read-only script](../analysis/audit_crow_table1.py) requires openpyxl:

```text
python analysis/audit_crow_table1.py path/to/G48080_SuppTab1.xlsx data/crow-lawlor-recalibration.json
```

No spreadsheet was recalculated or visually rendered. The six workbook layouts were inventoried; Table1 stored contents were read, while detailed numerical auditing was confined to these Lawlor rows and broken references. Tables2-6 analytical contents remain unaudited.

## Consequence for the hypothesis

A recalibrated age is not an independent new measurement or evidence of deliberate alteration. This supplement makes assumptions and several reproducibility questions inspectable. It neither supplies a historical-era date nor establishes a shared catastrophe. Transferring any eruption age to a named Bouse fossil bed still requires the stratigraphic tests in [the age-transfer audit](BOUSE-AGE-TRANSFER.md).

Next: reconcile the Lawlor summary with original inputs and covariance, audit the Highwall Wash sample across Tables2/3/6, and recover the main paper and Comment/Reply before evaluating the fault-duplication explanation. The PDF's magnetostratigraphy text has been read as a lead, but its diagrams and sample-level polarity results are not yet audited here.
