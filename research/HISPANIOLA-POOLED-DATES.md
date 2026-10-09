# One cave assemblage does not supply one event date

2026-10-09. C028/S316; retrospective sourced draft without independent review. This comparison supplements the [wildlife investigation](WILDLIFE-COMPARISON.md) without changing the Haitian sloth assays.

[Valenzuela, Torres-Roig and Alcover (2026)](https://journals.sagepub.com/doi/10.1177/09596836261458223) report three pooled bone-collagen assays from Pozimán Cadena, Dominican Republic. Publisher HTML methods, tables, results and discussion were read, with selected PDF text cross-checks. PDF screenshot calls supplied no viewable images, downloads returned403, and the supplementary DOCX was not inspected. This is **FULL_TEXT_PORTION**, not SCAN_INSPECTED. Source images are not reproduced.

The [ledger](../data/hispaniola2026-pooled-dates.json) preserves results and rounded table variants, quality indicators, pool descriptions, locality roles and missing data. The site coordinate is not an individual specimen position. Twelve reported fragments in the Nesophontes pool are not twelve independently dated animals.

| Pooled assay | Taxon | Reported 95.4% calendar envelope CE | Original Results radiocarbon BP |
| --- | --- | --- | --- |
| RICH-24986 | Nesophontes hypomicrus | 1406–1453 | 486 ±29 |
| RICH-24977 | Rattus rattus | 1680–1940 | 120 ±28 |
| RICH-27406 | Rattus rattus | 1660–1950 | 160 ±22 |

Table2 rounds these radiocarbon pairs to490±30,120±30 and160±20. Both versions remain; they are not six assays. The reported calendar envelopes are retained without reconstructing omitted probability segments or recalibrating the dates.

## Executed comparison and its boundaries

The [calculator](../analysis/hispaniola_pool_windows.py) and [results](../analysis/hispaniola-pool-windows-result.json) calculate closed-envelope geometry. The minimum window touching the Nesophontes envelope and each rat envelope is227 and207years; all three require227years. A0-,1-,10-,100- or200-year window cannot touch all three envelopes;250years can. These are conditional descriptions of reported pool-age sets, not confidence bounds on mortality duration. The input hash and small arithmetic checks support reproducibility, not assay validity.

Pooling prevents interpreting these as individual death dates. A pooled measurement combines material contributions; no contribution weights or specimen-specific determinations were recovered. Under a valid homogeneous-age pooling assumption it can constrain that assignment, but it cannot locate the youngest individual or extinction. The dated material is biological collagen, not the final deposit.

Consequently, different biological ages challenge treating the assemblage as a demonstrated simultaneous death event. They do **not** alone exclude later co-deposition of older remains. Conversely, being in one cave is insufficient positive evidence for that later movement. Neither sequential accumulation nor catastrophic redeposition is independently demonstrated here. Both require sample-linked positions, contacts and transport indicators; extinction causation needs additional evidence.

The authors report no clear stratification, with rats uppermost and slightly offset from much of the endemic material. That is relevant context but supplies no directly measured depositional age. Their later-deposition interpretation remains separate from the pool-age measurements.

## A citation discrepancy retained

S316 cites UCIAMS-191028 as1435–1468CE. Our existing [S36 transcription](../data/haiti-rodent-dates.json) records490–515calBP: subtracting from1950 gives1435–1460CE arithmetically. Both refer to435±15radiocarbonBP. The original S36 scan was not freshly inspected this turn; differing calibration, endpoint convention or transcription cannot yet be distinguished. Neither range replaces the other.

Both versions overlap the new Nesophontes envelope at1435–1453CE. That is regional envelope compatibility across different localities, not direct coexistence or interaction at Pozimán Cadena. An interval preceding the expected1492rat introduction must remain adverse evidence until an actual specimen-identification or dating explanation is established. Calibration complexity and historical expectation alone do not supply an observed correction. This also does not establish pre-contact introduction: the specimen/context and calibration still need independent scrutiny.

## Checks that remain open

The reported Nesophontes starting mass0.27g falls below the methods' nominal0.4–0.5g minimum. A Table1minimum of1.99mm falls below the stated2.0mm comparison boundary, despite prose describing all measurements as within range. These are audit flags, not demonstrated assay failure or taxonomic misidentification. Protocol exceptions, rounding, multiple characters and individual measurements need checking in the supplement and original records.

Quality indicators are now available for these pools, unlike the still-incomplete earlier Haitian sloth quality audit. They do not validate the sloth assays or establish absence of contamination in the new pools. No original lab certificates, blanks or repeat dating were inspected.

Next recover the supplementary specimen measurements, laboratory records and excavation positions, then resolve the S36citation against its original table/calibration output. No common flood horizon, exact extinction date, historical fabrication mechanism or independent review is established. All twenty original objectives remain active.


## Rat citation follow-up

The [original-table and calibration follow-up](HAITI-RAT-CALIBRATION.md) now confirms S36Table2visually and supplies a separate two-segment diagnostic. The publication-summary cause remains unresolved; no empirical date correction or pre-contact arrival is established. The no-offset model retains the early result as a challenge to investigate. Original sloth dates and mortality comparisons are unchanged.


## Specimen-linked enamel measurements recovered

The [2018supplement audit](RODENT-ISOTOPE-SPECIMEN-LINK.md) now matches all eight dated museum identifiers, includingUF293844. Its carbon/oxygen measurements are incisor enamel, not collagen. The general absence-of-isotope-values claim requires that distinction; no dietary correction or radiocarbon result is changed. Full methods, tissue identity and specimen-specific collagen records remain needed.
