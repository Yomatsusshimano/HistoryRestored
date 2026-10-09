# Candidate GF2 root-to-trunk comparison

2026-10-09. Relative-pattern audit using S61's manually transcribed GF2RTC and GF2RTB root series and S229's CPGF2A, CPGF2B and CPGF2NW trunk records. The GF2/CPGF2 specimen linkage is a candidate based on labels and published Copalis context; a complete physical specimen crosswalk remains unverified.

## Calculation

The [script](../analysis/cascadia_root_trunk.py) pairs each root with each trunk using raw widths, adjacent log-width differences and adjacent width differences. For each pair and transformation, every integer shift that keeps the complete trunk series inside the root record is tested by Pearson correlation. All candidates for a pair use the same observations. Root and trunk year labels remain those assigned in the sources.

The two root series end in1699; the longest trunk record ends in1675. That difference alone is compatible with lost outer trunk rings, as described in the published field account. No1699 death inference is made from the trunk endpoint. GF2RTA's ten transcribed terminal widths are excluded from this full-series comparison; no longer array is invented.

The [result ledger](../data/cascadia-root-trunk.json) stores the transcription hash, NOAA file hash, processing, all candidate shifts and rankings. Raw integer width scales differ between sources, but Pearson correlation and these difference transformations are invariant to a positive multiplicative unit conversion. No original spline, time-series model or per-tree average is reproduced.

## Results

| Root | Trunk | Raw-width rank at published placement | Log-difference rank | Width-difference rank |
| --- | --- | ---: | ---: | ---: |
| GF2RTC | CPGF2A | 1 | 1 | 1 |
| GF2RTC | CPGF2B | 88 | 1 | 1 |
| GF2RTC | CPGF2NW | 1 | 1 | 1 |
| GF2RTB | CPGF2A | 1 | 1 | 1 |
| GF2RTB | CPGF2B | 1 | 1 | 1 |
| GF2RTB | CPGF2NW | 1 | 1 | 1 |

Each trunk/root pair has44–228 tested placements depending on its available span. All12 annual-difference comparisons rank the published placement first. Their correlations range .3495–.5475. These are related wood measurements and repeated transformations, not12 independent dating confirmations.

The raw-width exception is retained: CPGF2B versus GF2RTC has r=.1749 at the published placement and ranks88th among196 shifts; its largest raw-width correlation is .4692 at shift+39. Both annual-difference transformations instead favor shift0. Growth trends and radius-specific behavior can influence raw correlations; this diagnostic does not establish the cause of the discrepancy. Against GF2RTB, the same short trunk record favors shift0 even in raw widths (r=.6236).

The earlier regional/local-reference exceptions for shorter CPGF2 records therefore do not imply an absence of within-wood pattern agreement. This comparison adds positive relative-pattern evidence for the candidate link while preserving the raw-width exception. It also focuses the next task: specimen identity, root/trunk field linkage and original processed averages.

## Limits and next evidence

The scans and numerical transcription have been inspected, but independent transcription review remains absent. Seven earlier GF2RTC digitization errors were corrected and recorded before this calculation. Source-assigned years and a shared shift of roots and trunks leave these correlations unchanged, so this test cannot establish the absolute calendar or detect a uniform chronology transformation.

The published S231 root/trunk statistic uses processed, combined radii and reports255-year overlap; our individual comparisons do not reproduce that statistic. No significance probability or earthquake-day estimate is supplied. Physical anatomy, bark preservation, chain of custody and the GF2-to-CPGF2 specimen crosswalk still require direct evidence. No corrected historical date, global catastrophe link or independent-review status follows.
