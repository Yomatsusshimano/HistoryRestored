# Lawlor zircon calculation and Bouse sampling history

2026-10-08. Retrospective arithmetic audit, not new dating or independent scientific review.

S196, [Harvey's analytical supplement](https://doi.org/10.1130/GES00904.S1), was recovered through Figshare. Pages 1-3 were visually inspected. [Transcribed data](../data/harvey-zircon-rows.json) preserve 51 Bouse and 52 proximal Lawlor analyses, including older grains, printed errors, isotope fields and page locators. Dashes remain null. Other sample groups are not audited here.

The preparation note describes a 2009 Amboy sieve step removing material below about 50 micrometers; that fraction was subsequently examined and yielded 24 additional analyzed zircons in 2012. Another note reports 99 additional Amboy survey analyses older than 7 Ma, without individual results here. The table is not an unselected census of all grains. Methods also state a preference for adhering glass and a disequilibrium correction using DTh/U = 0.2. These procedures need evaluation before inferring population frequencies or geological age.

## Reproduction from rounded ages

Using printed one-sigma age errors, set w = 1/sigma²; mean = sum(w × age)/sum(w); internal standard error = sqrt(1/sum(w)); MSWD = sum(w × (age−mean)²)/(n−1). These calculations assume diagonal weights, omit shared systematic errors and do not reconstruct corrections from original ion measurements.

| Selection | n | Weighted mean (Ma) | Internal standard error (Ma) | MSWD |
| --- | --- | --- | --- | --- |
| All proximal Lawlor rows | 52 | 5.00320 | 0.01442 | 2.87749 |
| Eight oldest rows removed | 44 | 4.93915 | 0.01611 | 1.42929 |

The second mean rounds to the reported 4.94 Ma in the previously retrieved S195 passage. Its reported MSWD is 1.41, not exactly our 1.42929. Rounded inputs are a possible explanation, not a demonstrated reconciliation. Our internal standard error is not the paper's reported ±0.04 Ma uncertainty; full uncertainty conventions and source precision remain to be checked.

Removed IDs: LAWL2-106, Lawlor2_z1-1, Lawlor1_z1-1, LAWL1-119, LAWL2-107, LAWL2-120, LAWL2-130 and LAWL1-109. There is no tied age at the boundary. All removed values remain public. Improved agreement with a single-age model does not independently justify a geological exclusion rule. No single-age fit is assigned to the mixed Bouse population.

Run `python analysis/lawlor_age_check.py`; [saved output](../data/lawlor-age-check.json) includes retained and removed IDs. This concerns zircon crystallization, not the eruption or a historical shoreline. Next recover the full selection discussion and analytical covariance/standards, audit remaining candidate-tephra rows, and test primary deposition and stratigraphic transfer described in [the chronology audit](BOUSE-CHRONOLOGY.md).
