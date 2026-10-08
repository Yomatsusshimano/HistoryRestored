# Electron–MacBlo exploratory alignment

2026-10-08. C020, sourced draft, no independent review.

The published 1507 placement remains the strongest positive match in this explicitly different, reproducible processing of the recovered measurements. It ranks first with equal series weights, equal tree-label weights, and each of 21 Electron tree groups omitted separately. The ELE045 table discrepancy therefore does not remove the match under this method. This is evidence against treating that discrepancy alone as a refutation of the published placement.

## Inputs and method

[Electron WA171](https://www.ncei.noaa.gov/access/paleo-search/study/43943), S74, supplies 86 series. [King, Harley and Jacoby's MacBlo CAN682 archive](https://www.ncei.noaa.gov/access/paleo-search/study/38202), S77, supplies 27 series spanning assigned years 715–1990. The archive code and range agree with the reference identified in Electron Table S3. Exact author processing/version equivalence remains unverified. Downloads are hash-pinned in the [script](../analysis/electron_macblo_comparison.py) and [results](../analysis/electron-macblo-comparison.json).

For each measurement series, calculate `width[y] / (width[y] + width[y-1])` where both adjacent years exist and their sum is positive. This is the unclipped P2 transformation described by [the developer's normalization documentation](https://cdendro.se/wiki/index.php/Proportion_of_last_two_years_growth), S78. It is not an assertion that the paper used this option; CDendro also offers other transformations.

Average transformed values annually, either weighting every series equally or averaging within tree-label groups before weighting groups equally. Group labels use the first six characters for Electron and five for MacBlo; these are transparent grouping assumptions, not independently authenticated tree identities. Missing values are omitted, not filled. Transforming adjacent pairs reduces Electron's full overlap from 475 widths to 474 transformed annual values.

Scan every relative annual shift with at least 30 paired observations. Rank positive agreement with `t = r * sqrt((n-2)/(1-r²))`, where `r` is Pearson correlation. This statistic is used for ranking, without a p-value or claim of search-adjusted significance. Published internal ring placements and the MacBlo calendar dates are accepted inputs. The known 1507 result was inspected before this analysis; this is retrospective sensitivity analysis, not a prospective prediction.

## Results

| Annual weighting | Best final year | Paired years | r | t | Next-best t |
| --- | --- | --- | --- | --- | --- |
| Equal series | 1507 | 474 | 0.313907 | 7.182873 | 3.751957 |
| Equal tree-label groups | 1507 | 474 | 0.318122 | 7.290089 | 3.764987 |
| Equal groups, ELE045 omitted | 1507 | 474 | 0.316714 | 7.254237 | 3.757084 |

Each full variant evaluates 1,690 placements; the runner-up is 772 with only 57 paired years. Requiring at least 100 or 300 paired years retains 1507 as the best placement. All 21 leave-one-Electron-group-out runs also retain 1507. These related runs are sensitivity checks, not independent discoveries. Full values and top-five alternatives are retained in JSON.

The Pearson result agrees with Python's separately implemented `statistics.correlation` within 1e-12, and a deterministic synthetic shifted-series check recovers the inserted +123-year displacement. Those checks verify arithmetic and shift direction, not the chronology. This result does not reproduce the paper's t=8.0 or its exact processing and overlap selection. Reference dating, specimen custody, competing normalizations, dependence, and multiple-search significance remain to audit.

## Additional transformations and reference omissions

A subsequent [sensitivity script](../analysis/electron_normalization_sensitivity.py) applies two further formulas from S78: Hollstein uses `ln(width[y]/width[y-1])`; Baillie–Pilcher uses the logarithm of the current width divided by the mean of its centered five-year window. Each is applied to individual series before annual tree-label means. Logarithms require positive arguments; incomplete windows are excluded and nothing is imputed. Formula fixtures check orientation, window edges and missing-value handling. The separately implemented Pearson function agrees within 1e-12 for all three full comparisons. Refactoring the common loader left the original P2 results unchanged.

| Transformation | Best final year | Paired years | r | t | Runner-up year / t |
| --- | --- | --- | --- | --- | --- |
| P2 | 1507 | 474 | 0.318122 | 7.290089 | 772 / 3.764987 |
| Hollstein | 1507 | 474 | 0.327916 | 7.541120 | 772 / 3.918214 |
| Baillie–Pilcher | 1507 | 471 | 0.336563 | 7.740312 | 1706 / 3.781264 |

For each transformation, omit each of 21 Electron groups and each of 15 MacBlo groups separately. All 108 runs retain 1507 as the leading placement. This tests sensitivity to individual label groups on both sides; it does not test removal of all related errors or authenticate the dates. The different runner-up placements show some processing sensitivity below the leading match. [Machine-readable results](../analysis/electron-normalization-sensitivity.json) retain all omission results, overlaps, top-five full comparisons, and input hashes.

This additional analysis narrows the processing uncertainty: the leading placement survives these three formulas and single-group omissions. It does not supply the authors' exact configuration, a search-adjusted false-match probability, an independent reference-calendar anchor, or a prospective success.

[Reference-anchor audit](MACBLO-ANCHORS.md) now traces the reported collection history and linked pulse measurements, distinguishing those source reports from independent calendar authentication.
