# Electron Mudflow: buried forest and shared dating references

2026-10-08. C020, sourced draft; no independent review.

[USGS data release S72](https://doi.org/10.5066/P13WAVXH) was recovered through ScienceBase. All four downloaded files match repository MD5 checksums; unchanged originals are in [the preserved tree table](../sources/originals/electron/C14_data_S1.csv). Checksums establish file identity, not scientific accuracy.

The tables contain 21 tree records, 86 measurement transects, eight radiocarbon rows and 34 reference-chronology comparisons. Four references give their highest reported match at 1507; six include that year among their top five. Macblo/CAN682 has the highest listed statistic, t=8.0. WA027 Lava Beds instead peaks at 1926 and does not list 1507 among its top five. Different regional references do not all yield the same result.

The release summary reports seven ages and a 1477–1522 CE radiocarbon interval. [Supplement S73](https://doi.org/10.1130/GEOL.S.30689474), Figure S2, identifies the seven illustrated assays: Beta71969, WW3793, WW3794, WW3795, WW1875, WW3088 and Beta82791. The eighth table entry, KAP14a / D-AMS010693, is absent from that model; the subsequently recovered article text explains its separate treatment below. The caption names ELE001, ELE011 and ELE039. ELE11 in the assay table has a 1994 analysis date while S1 lists 2024 collection for ELE011. Earlier sampling could explain this, but the collection history is not established here. No identifiers or dates were corrected.

Visually inspected Figure S2 intervals differ from the release abstract:

| Reported model | 68.3% CE | 95.4% CE | 99.7% CE |
| --- | --- | --- | --- |
| Panel A: five ELE001 samples | 1495–1509 | 1485–1516 | 1476–1522 |
| Panel B: seven samples, three trees | 1501–1514 | 1494–1520 | 1486–1528 |
| Release abstract: seven ages | Not stated here | Not stated here | 1477–1522 |

No interval is adopted as the correction. Original model inputs, version history and reproduction are needed. All these ranges include 1507, so the discrepancy by itself does not refute that year. The figure's dashed 1507 line is a comparison marker, not an independent observation.

Table S3 identifies the raw widths as [NOAA WA171, S74](https://www.ncei.noaa.gov/access/paleo-search/study/43943). A [hash-pinned coverage script](../analysis/electron_measurement_coverage.py) reads 18,489 widths in 86 series grouped under 21 tree IDs, spanning 475 published calendar rows, 1033–1507. It compares each tree's series count and date bounds with USGS S1. Twenty tree summaries agree; ELE045 differs:

| Source | ELE045 first year | Last year | Transects |
| --- | --- | --- | --- |
| USGS S1 and supplement S1 | 1322 | 1475 | 2 |
| NOAA template and Tucson file | 1398 | 1506 | 2 |

Both NOAA series contain 109 annual observations with no internal missing values. This is a source discrepancy, not a justified redating. Published calendar labels are inputs to this coverage check; the check does not establish absolute dates or bark preservation. [Full coverage output](../analysis/electron-measurement-coverage.json) and [selection, interval and acquisition ledger](../data/electron-model-selection.json) support reproduction.

Bonneville's abstract uses an Electron chronology as one external comparison. These dates therefore require a shared-dependency audit. Raw annual widths have now been recovered separately from the USGS tables; external matching and the age model remain unreproduced. [Release audit and hashes](../data/electron-release-audit.json) preserve the earlier acquisition. The supplement, release and NOAA archive represent one research chain, not three independent confirmations.

## Article methods and archived diagnostics

[Author-uploaded article text S76](https://www.researchgate.net/publication/398469149_Forest-floor_burial_in_1507_by_the_largest_Mount_Rainier_lahar_of_the_past_millennium), advance-page 2, describes KAP14 as separately calibrated hemlock with missing outer rings that could not be crossdated. Its radiocarbon results agree with Figure S2, leaving an internal abstract/results discrepancy. Methods specify CDendro high-frequency comparisons against MacBlo, scanning annually with at least 30 years' overlap. Precise processing settings remain unrecovered. These are extracted-text findings; the article PDF could not be inspected visually.

[NOAA S75](https://www.ncei.noaa.gov/pub/data/paleo/treering/measurements/correlation-stats/wa171.txt), checked November 18, 2025, contains 19 flags in 744 overlapping segments. A means correlation below .3281 but highest as dated; B means a higher correlation at another placement. Four flags belong to ELE045's two series. Their reported correlations with the master are .481 and .487. These diagnostics identify review targets; they do not establish a corrected placement. All series spans and observation counts agree with the recovered raw file.

The [reproducible audit](../analysis/electron_quality_audit.py) also counts tree labels per year. The earliest interval, 1033–1049, contains only ELE039; 1050–1148 contains ELE039 and KAP015. Multiple radii are not independent trees. Removing ELE045 preserves the 1033–1507 coverage bounds, but this says nothing yet about the external correlation peak. [Results](../analysis/electron-quality-audit.json) preserve flags and coverage limits. Next, reproduce the actual processing and compare tree-weighted and leave-one-tree-out results without silently altering archive dates.

