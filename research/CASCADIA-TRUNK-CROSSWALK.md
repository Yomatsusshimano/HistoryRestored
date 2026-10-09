# Cascadia trunk measurement crosswalk

2026-10-09. Documentary and numerical correspondence between S61's original GF2 trunk tables and S229's NOAA records. This advances the earlier candidate label match; it does not authenticate physical specimens or supply an independent calendar date.

## Original records and inspection

The original [GSA supplement 9756](https://doi.org/10.1130/9756), by Jacoby, Bunker and Benson, prints root records GF2RTC, GF2RTB and GF2RTA followed by trunk records GF2TRB, GF2TRA and GF2TRNW. PDF pages 4-5, printed killed-cedar table pages 2-3, were rendered and visually inspected. All three trunk sequences were manually transcribed, including their end markers. S61's methods on PDF page 2 describe site/tree/core identifiers and widths in micrometres, and report that cores/samples were archived at the Lamont-Doherty Tree-Ring Laboratory. That is a published 1997 custody statement, not a verified current accession inventory.

The NOAA [wa130.rwl record](https://www.ncei.noaa.gov/pub/data/paleo/treering/measurements/northamerica/usa/wa130.rwl) names the corresponding trunk series CPGF2A, CPGF2B and CPGF2NW. Its -9999 end-marker convention denotes 0.001 mm measurement units, numerically equivalent to micrometres. The [archived methods supplement](https://www.ncei.noaa.gov/pub/data/paleo/treering/measurements/correlation-stats/wa130.txt), S231, explicitly identifies cores from the trunk of CP-GF2. Earlier root/trunk correlations are separate evidence about pattern agreement.

## Complete numerical comparison

| Original S61 ID | NOAA S229 ID | Source-assigned years | Widths compared | Differences after scan recheck |
| --- | --- | --- | ---: | ---: |
| GF2TRA | CPGF2A | 1482-1648 | 167 | 0 |
| GF2TRB | CPGF2B | 1515-1619 | 105 | 0 |
| GF2TRNW | CPGF2NW | 1419-1675 | 257 | 0 |

All 529 widths, year coverage and end-marker positions correspond exactly. The [script](../analysis/cascadia_trunk_crosswalk.py) preserves scan-read rows and compares every value by assigned year against the hash-checked NOAA file. The [ledger](../data/cascadia-trunk-crosswalk.json) records both source hashes, page locators, widths and corrections. The original PDF hash is also checked when the local cached PDF exists; it is not redistributed here.

The initial manual GF2TRNW reading contained seven errors. Comparison identified them, and an enlarged rendering confirmed the corrected readings: 1457 1656→1506; 1591 1547→1574; 1593 1353→1363; 1640 1793→1683; 1641 1683→1739; 1645 2026→2062; 1671 1440→1404. These are this investigation's transcription corrections, not changes to the historical measurements. The ledger retains both readings. The comparison-assisted recheck was performed by the same analyst; it is not independent transcription review.

## What changes, and what does not

The three NOAA trunk identifiers can now be linked to three original printed trunk series through complete numerical identity, rather than through similar prefixes alone. The root/trunk audit consequently has a stronger documentary basis for its candidate relationship. Source grouping and S231's explicit CP-GF2 trunk description support the interpretation, but matching files do not authenticate where the wood was collected or demonstrate that each root and trunk physically belonged to the same tree.

The exact matches also establish dependence: these are corresponding versions of measurements, not 529 new assays or two independent dating datasets. Assigned year labels are inherited. A uniform shift of all labels would leave this comparison unchanged. No absolute date, physical custody chain, bark-preservation assessment, final-ring anatomy, original processed root/trunk statistic, earthquake day or worldwide event is independently established.

Next discriminating evidence is the specimen inventory/field or laboratory crosswalk connecting root and trunk samples, followed by the original per-radius detrending and averaging needed to reproduce the combined statistic. Further duplicate measurement matches would add little to those questions.

The subsequent [root-linkage audit](CASCADIA-ROOT-LINKAGE.md) distinguishes explicit published field association from independent physical authentication. S60 reports root and trunk sampling from one Copalis tree; S19 marks tracing for five of its eight usable roots, but not CP-GF2. Those primary reports are evidence of association; this investigation has not inspected the physical continuity or custody itself.
