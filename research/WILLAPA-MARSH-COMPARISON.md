# Willapa apparent-marsh candidate comparison

2026-10-09. C004 / S251-S253,S257. Eight1922apparent-marsh features are compared with the same code in the2005-2006delivery. This exploratory association test does not establish signed coast movement, rates or a catastrophe.

The [script](../analysis/willapa_marsh_comparison.py) searches **all375modern apparent-marsh records**, not just the earlier rectangle subset. Stored geographic coordinates are projected into NAD83UTM10N, without datum-realization or epoch reconciliation. Each historical part is sampled every10m and20m, including endpoints. Exact nearest-distance ties are retained with modern IDs and dates. Distances are unsigned point-to-line distances; a nearest candidate is not an authenticated corresponding feature.25/100/500m thresholds are descriptive, not accuracy or matching gates. Sample fractions are not exact length fractions.

[Results](../data/willapa-marsh-comparison.json) retain every sample/candidate and both spacings. Independent explicit point-to-segment calculations agree at the first, middle and last samples for each feature/spacing to within1e-7m. Known20m offset and identical-line controls pass. These checks validate the numerical distance implementation, not the source maps. The method uses [Shapely's nearest-query API](https://shapely.readthedocs.io/en/stable/strtree.html); versions and input hashes are recorded.

| Historical ID | Median distance,10m sampling | Range,10m sampling | Interpretation limit |
| --- | ---: | ---: | --- |
|14 |525.2m |503.4–552.3m |Tiny source loop; nearest marsh candidate is distant |
|38 |184.9m |0.7–400.9m |Some overlap, substantial divergent portions; two candidates |
|41 |43.7m |0.006–874.6m |Long trace has nearby and distant portions; four candidates |
|42 |62.1m |0.7–113.9m |Nearby curve is a candidate, not validated displacement |
|44 |116.6m |97.8–133.4m |Tiny coded feature; two candidates |
|49 |6386.8m |6160.6–6580.0m |Grassy-island feature has no local same-class candidate |
|51 |5781.5m |5671.2–5987.8m |Other island portion has no local same-class candidate |
|125 |68.3m |58.4–121.1m |Short source feature; ecological identity unresolved |

At20mspacing, median distances range44.2–6382.7m across features; full values are in the ledger. Some minima change materially with sample spacing, so isolated closest approaches must not stand in for a whole-feature fit. No pooled regional mean or significance is assigned. To reproduce, first run `analysis/willapa_modern_vector_audit.py` to extract the hash-recorded modern package, then run this comparison script with the published historical row export, raster and world file.

## Visual comparison and unmatched observations

All eight source/overlay panels were visually inspected: [14](figures/willapa-marsh-comparison-14.png), [38](figures/willapa-marsh-comparison-38.png), [41](figures/willapa-marsh-comparison-41.png), [42](figures/willapa-marsh-comparison-42.png), [44](figures/willapa-marsh-comparison-44.png), [49](figures/willapa-marsh-comparison-49.png), [51](figures/willapa-marsh-comparison-51.png), [125](figures/willapa-marsh-comparison-125.png). Original crops are left; historical trace magenta and modern apparent-marsh lines blue are right. No translation, rotation or fitted alignment was applied; scales differ by crop.

38has a partly nearby trace with divergent portions.41has nearby southeastern portions and an unmatched northwestern portion.42has a broadly adjacent curve;44/125remain tiny-feature comparisons.14has no nearby same-class line.49/51have none visible in their panels. Their crop-bound overlap audit finds MHW, source-data-limit and depth-contour features, which cannot replace marsh-edge observations. These bounding-box overlaps do not establish exact feature crossings, completeness or ecological disappearance. The6km nearest distances are therefore **unmatched associations, not measured island movement**. Changed classification, coverage, genuine ecological/geographic change and historical digitization error remain alternatives requiring actual imagery and field context.

## Next discriminating evidence

Locate source imagery/frames and survey limits for38/41/42and49/51; compare the same physical boundaries across classes before deciding correspondence. Audit historical MHW records separately. Use stable controls to estimate correlated historical map uncertainty, reconcile coordinate realization and tides, and then define signed transects for authenticated segments. Apparent vegetation-edge change would not itself measure crustal displacement or the event date. No prospective prediction, independent review, global geography or chronology reconstruction is completed.
