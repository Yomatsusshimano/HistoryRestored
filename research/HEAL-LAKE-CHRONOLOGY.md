# Heal Lake: a reported local chronology disagreement

2026-10-08. C021, sourced draft; no independent review.

[Black et al. 2023, S79](https://doi.org/10.1126/sciadv.adh4973) reports that matching earthquake-killed wood to Heal Lake yields 1055 CE, versus 923 CE with MacBlo: a 132-year difference. The authors suspect an older Heal Lake segment is misplaced. Their attempted reconstruction reached about 1400 CE but did not securely join earlier floating segments. This is a reported local reference problem, not evidence that historical calendars generally shifted.

Supplement S80, Figure S3 (PDF page 4), was visually checked. It shows shorter overlapping Heal Lake series, longer MacBlo series, and stronger recent than early correlation between the two. The caption specifies spline detrending and removal of remaining autocorrelation. The plotted result has not been independently reproduced, and no individual series has been redated here.

## Original construction and version limits

[Zhang and Hebda 2005, S81](https://doi.org/10.1029/2005GL022913), methods paragraphs 3–5, describes 150 samples in its continuous chronology: 29 recent-tree samples and 121 subfossil logs. It also describes separate floating chronologies, approximately positioned with radiocarbon. Those floating sequences must not be mistaken for a single fully calendar-anchored four-millennium record.

[Zhang's 1996 thesis, S82](https://hdl.handle.net/1828/20271) was retrieved from the university repository. Its crossdating chapter describes iterative statistical checking, pointer-year comparison, wood anatomy and radiocarbon assistance. Table 3.3 lists **155** sequences, versus **150** in the later article. Exact membership/version equivalence is unresolved; the thesis table cannot silently substitute for the dataset reanalyzed in 2023.

The thesis's five radiocarbon entries in Table 3.2 (printed p. 26, PDF 34) were visually inspected:

| Sample | Rings dated, counted outward | Radiocarbon BP | Printed calibrated BP entries |
| --- | --- | --- | --- |
| HLL001 | 38–49 | 330 ± 50 | 320; 390; 425 |
| HLL003 | 8–12 | 1880 ± 50 | 1822 |
| HLL035 | 30–39 | 410 ± 50 | 497 |
| HLL051 | 47–52 | 1650 ± 50 | 1545 |
| HLL548 | 50–59 | 1200 ± 50 | 1103 |

The table does not supply calibrated probability intervals or lab accession numbers. These printed calendar entries cannot be treated as exact independent year determinations. The text says radiocarbon assisted assembly, so agreement afterward would partly reflect selection rather than an untouched validation test.

Table 3.2 gives HLL035 a 287-year span; Table 3.3 on printed p. 29 gives 1424–1707 and 284 years. Both pages were visually checked. Preserve this discrepancy; its cause and relation to later revisions are unknown. [Structured records and access history](../data/heal-lake-audit.json) retain the five assays and version distinctions.

## What remains testable

Recover the exact raw series and membership used in 2005 and 2023. Reproduce both the reported 1055 placement and the more recent agreement before testing local segment shifts, alternative joins and radiocarbon constraints. Compare full calibrated distributions, not printed single dates. Original lab sheets, wood scans and independent reviews are still missing. Nothing here establishes deliberate fabrication, a worldwide catastrophe, or a universal 132-year chronology conversion.

## Potential joins in the 1996 table

The [overlap audit](../analysis/heal_lake_overlap.py) extracts Table 3.3 rows 1–100, covering all listed sequences ending at or after 700 CE. Printed pages 28–30 were visually inspected. Every extracted span agrees with its inclusive endpoint arithmetic; this does not resolve the separate Table 3.2 discrepancy. Twenty-two sequences end at the assigned year 1992. Those are candidate anchoring endpoints, not independently authenticated living trees.

The calculation treats each printed interval as a node and permits a link only when two intervals overlap by a chosen number of years. It asks whether a chain of such potential links reaches a 1992 endpoint. These links are opportunities for matching, **not measured pattern matches**; the thresholds are exploratory, not scientific acceptance criteria.

| Required overlap at every link | Connected rows of 100 | Earliest assigned year among connected rows |
| --- | --- | --- |
| 30 years | 100 | 588 |
| 50 years | 98 | 588 |
| 100 years | 50 | 1340 |
| 150 years | 47 | 1340 |

No sampled year from 700 through 1992 has fewer than four listed sequences in this subset. Nevertheless, annual sample depth does not guarantee long links between older and newer groups. HLL027's best possible route to a 1992 endpoint includes a link no longer than 77 years. One available bridge is HLL085 (1327–1416) to HLL372 (1340–1687) or HLL461 (1340–1702): both overlaps are 77 years. HLL548's widest possible route has a 62-year bottleneck.

An independent graph-traversal implementation reproduces all four threshold connectivity counts. [Full output](../analysis/heal-lake-overlap.json) preserves source rows, flags, reported correlations and computed capacities. These calculations neither recover the actual assembly order nor locate an error. They nominate sample pairs for direct anatomical and ring-width review. The 1996/2005/2023 version differences still prevent treating this as an audit of exactly the later dataset.

## Older floating groups: original assembly limits

[Zhang's 2000 dissertation, S83](https://dspace.library.uvic.ca/bitstreams/72450731-41fb-4eb9-bbc8-79df8bf2f900/download) supplies a separate history of the older floating groups. Printed pages 112–113, 134 and 136 were visually inspected. These BC groups must not be conflated with the later reported 132-year CE disagreement.

| Sample | Dated rings (middle) | Radiocarbon BP | Printed two-sigma bounds, BCE |
| --- | --- | --- | --- |
| HLL064 | 60–70 (65) | 3390 ± 50 | 1859–1517 |
| HLL020 | 10–20 (15) | 3450 ± 60 | 1918–1532 |
| HLL517 | 32–37 (35) | 3520 ± 50 | 2009–1663 |

Table 6.1 underlines 1660 BCE as HLL064's anchor intercept. Page 134 instead assigns ring 65 to the 1640 BCE intercept when combining groups IV and V: group IV moves 20 years forward and group V 180 years backward. The author reports compatibility with the two-sigma constraints of HLL020 and HLL517. This archive preserves that report without claiming an independent recalculation of the joins. The table's bounds summarize the older calibration; they are not uniform probability distributions or modern recalibrations. Laboratory names follow the table's underlining and footnote; accession numbers remain unknown.

Page 134 reports no confident bristlecone-pine match and no crossdated connection between the approximately 970–159 BCE combined sequence and the earlier thesis's 130 BCE–1992 CE chronology. Page 136 explicitly warns that the floating positions and connections may be incorrect. This is documented provisional assembly, not a demonstrated concealment or a correction to all historical dates.

The same page states an intention to submit measurements to ITRDB. A targeted search of public web results, named sample IDs, the 2023 data-availability statement and the RingDateR repository did not recover exact Heal Lake annual widths or original laboratory sheets. This bounded failure does not establish their absence elsewhere. Search terms, three assay transcriptions, calibration intercepts and the dissertation checksum are retained in the [audit record](../data/heal-lake-audit.json). Exact dataset accession/version recovery remains the next requirement for testing the CE conflict.
