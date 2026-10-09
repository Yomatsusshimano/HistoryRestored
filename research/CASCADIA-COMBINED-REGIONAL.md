# Combined GF2 trunk versus archived regional references

2026-10-09. C004 / S229, S231, S233. This extends the [combined-radius audit](CASCADIA-COMBINED-GF2.md) to Long Island. Local root/trunk agreement and regional calendar matching are different comparisons.

## Controlled comparison

The [script](../analysis/cascadia_combined_regional.py) reuses the already-declared trunk averages: each radius normalized before averaging, with mean-divided widths or standardized log/linear differences. It tests the combined three-radius target and NW alone against the three recovered standard/ARSTAN/residual reference outputs. Reference indices receive the corresponding transformation. This is still a hybrid of raw-derived target transformations and already processed regional indices, not the original decay/spline/AR method.

Full trunk observations and the final255 observations are retained separately. Every integer shift allowing full target overlap is scored. Endpoint bounds1720 and1986 are separate;1720 inherits radiocarbon information. No candidate is excluded because its reference count is small. [Results](../data/cascadia-combined-regional.json) preserve every candidate correlation, ranks, leading alternatives, reference-count diagnostics and input hashes.

## Results

Published-position ranks for the **combined three-radius trunk**, under endpoint≤1720:

| Transformation | Standard full / final255 | ARSTAN full / final255 | Residual full / final255 |
| --- | ---: | ---: | ---: |
| Mean-divided widths |3 /1 |2 /1 |1 /1 |
| Standardized log differences |5 /5 |3 /2 |3 /3 |
| Standardized width differences |4 /4 |4 /4 |4 /3 |

The placement ranks first in4/18 combined-target variants under each endpoint bound. NW alone ranks first in0/18. These repeated variants are dependent sensitivity checks, not independent dates or success rates in a random sample. The complete1986-bound rankings are retained in the ledger; equality of the first-place count does not establish equality of all rankings.

The full mean-divided standard comparison has r=.29536 at source placement, versus .29702 at shift−8. Taking only the final255 observations changes its source r to .29889 and rank1. ARSTAN similarly changes from rank2 to1. Small score differences and scope changes matter; they do not supply the missing original detrending or justify selecting255 merely to improve rank.

The combined log-difference standard comparison has r=.19342 at source placement, rank5, versus .20207 at shift−90. The alternative's reference counts have minimum4/median11. Thus even after combining radii, stronger alternatives cannot all be attributed to minimally populated reference years. Other variants retain low-count alternatives: combined ARSTAN log differences favor shift−392 with minimum1/median2. None is designated a replacement date.

## What this resolves

The earlier individual-radius exceptions do not directly describe a combined-tree result. Explicit averaging materially improves ranks relative to NW-only comparisons, but does not produce uniform regional robustness. Conversely, all48 local root/trunk variants favoring relative alignment do not force one unique alignment with Long Island. Shared wood patterns can be clear while comparison to a distant reference remains weaker and method-sensitive.

Known-signal recovery, independent NumPy checks of source-position correlation and positive-rescaling invariance passed. Every candidate correlation in six full NW-only difference scans agrees with the earlier, separately implemented [archived-reference diagnostic](CASCADIA-ARCHIVED-REFERENCE-TEST.md), not just its winning shift. These are calculation checks, not independent scientific review.

Original target indices, decay/spline fits, time-series model orders and exact historical reference version remain missing. The2006 QC model settings are not automatically the1997 analysis. No significance probability, chronology break, independently dated root death, or global-event link is established. The next useful evidence is the original processing output and its reproduction against the published statistic, rather than selecting a favorable diagnostic or accumulating more copies of the same data.

Subsequent [field-release audit](CASCADIA-FIELD-RELEASE.md) recovers a specific root identifier, sampling dates and approximate survey context, with a tag-number conflict. It also maps19 Long Island trees to21 reference series and preserves range/count discrepancies. This improves specimen-record retrieval; it does not supply the missing processing outputs or independently authenticate calendar assignments.
