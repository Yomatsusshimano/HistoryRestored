# Wind Caves: traceable grains, unresolved bed chronology

SOURCED_DRAFT, 2026-10-08. No independent review or field verification.

The original [Crow et al. supplement, S210](https://doi.org/10.1130/GEOL.S.13530698.v1) contains enough information to reproduce the selected-group arithmetic for sample **04PW30**. This checks a central young-age result in the [2021 chronology dispute](COLORADO-2021-DEBATE.md), without deciding the disputed structural reconstruction.

## Sample and analytical crosswalk

Table4, Sheet1 row6 places 04PW30 in the Wind Caves Member at **32.989544, −116.119412, NAD83**. That row does not give elevation or measured-section height; both remain unknown here. Table2, data row1211 identifies sanidine, lab66649, irradiation NM-300A, Argus VI, and J=0.0038874 ±0.03%. Coordinates are source-reported, not a recovered field survey or custody record.

Table2 summary rows66–70 match the following data-sheet entries exactly in both age and one-sigma uncertainty:

| Summary row | Data row | Run ID | Age (Ma) | One sigma (Ma) |
|---|---|---|---:|---:|
|66|1212|66649-73|4.491606|0.0691623|
|67|1213|66649-04|4.547619|0.0329174|
|68|1214|66649-46|4.549008|0.0539169|
|69|1215|66649-79|4.582996|0.0394479|
|70|1216|66649-64|4.601784|0.0565763|

All57 stored sample rows, including the52 outside the selected group, are preserved in [the extracted record](../data/wind-caves-audit.json). The next age in the ordered list is run66649-48, **9.071091 ±0.0163235 Ma (one sigma)**. Thus the five selected youngest ages are separated in this stored dataset from the next older result. That separation is a descriptive observation, not an independent justification of preparation, screening or age validity.

## Reproduced calculation

Using weights w=1/sigma², the five-row weighted mean is **4.559311369951691 Ma**, internal two-sigma uncertainty **0.04056396307620786 Ma**, and MSWD **0.5112639609084443**. These reproduce summary C71/D71 and the rounded MSWD0.51 in C72; C73 reports5of57. MSWD below1 does not call for upward scatter inflation under the stated method. The calculation does not demonstrate that all uncertainty components are independent or correctly propagated.

Reproduce with `python analysis/audit_wind_caves.py tmp/research data/wind-caves-audit.json`, placing original Supplement Tables2 and4 in that directory. SHA256 hashes are recorded in the output. Workbooks were read for stored values, not rendered, executed or saved. The script cross-matches the authors' selection; it does not discover a new selection, refit isotopes, recalculate J, or reproduce calibration covariance. A successful arithmetic check is not an independent age determination.

## What this constrains

If these young ages are reliable and their grains belong to the deposited assemblage, the host sediment cannot have been deposited before those crystals formed. This is a **maximum depositional age**, as Table4 labels it. An older depositional model for the same bed would then need revision or a demonstrated failure of one of those conditions. Reworking older crystals into younger sediment does not, by itself, explain crystals younger than their proposed host deposit.

The converse does not follow: these measurements alone do not give a minimum sediment age, prove deposition exactly4.56Ma ago, or exclude every much later reworking scenario. Nor does that logical opening provide evidence for a historical catastrophe. A later-event model still needs positive sedimentary and chronological evidence. No fault geometry, repeated thickness, regional arrival time, or global event is established by this computation.

Next recover the original measured-section placement and custody of04PW30, compare marker beds and mapped faults against the older chronology, and inspect the complete main paper and Reply. Those observations distinguish disputed bed correlation from an analytical-age problem; additional arithmetic on the same five stored ages would not.
