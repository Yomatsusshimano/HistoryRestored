# Actual modern shoreline-reach records and unresolved island correspondence

2026-10-09. S272 was acquired through the public data application linked by Ecology's [monitoring page](https://www.ecology.wa.gov/research-data/monitoring-assessment/coastal-monitoring-analysis). The application's actual configuration identifies webmap df41877b209d42399819f11a716f2cbd and the preliminary November2021 EMD FeatureServer. This replaces reliance on a catalog title with actual geometry and attributes. It does not replace the missing 1950 photograph or 1953 field sheet.

The application describes comparison of 2006–2019 NAIP and oblique imagery, approximately metre-spaced transects and 50-metre alongshore averaging. It warns about imagery misalignment and ground-truth limits and recommends confirming the current version. No contact was made; this release is the accessed service snapshot, not a guarantee of the newest accepted assessment.

## Complete query and duplicate layers

The declared geographic acquisition envelope was [-124.3,46.4,-123.9,46.85]. Each layer returned 1,185 object IDs. Every requested ID was recovered without a transfer-limit flag through twelve 100-ID batches. The two layers have identical attributes and returned geometry; they are two displays of the same evidence.

An exact client polyline/rectangle intersection retains 1,148 records. A separate server polygon query using the same corner coordinates returns exactly those 1,148 IDs. The envelope query's 37 additional records remain preserved. Query-shape behavior is therefore consequential; its server implementation was not audited. Do not silently call all 1,185 exact geographic intersections or discard the discrepancy.

The [original-response archive](../sources/originals/cascadia/ecology-willapa-reaches.zip) preserves both layers, ID responses, metadata and the polygon response. URLs and hashes are in the [acquisition ledger](../data/willapa-ecology-acquisition.json). The [audit script](../analysis/willapa_ecology_reaches.py) checks source bytes, ID completeness, duplicate layers and agreement with the polygon query, then writes the [results](../data/willapa-ecology-reaches.json). No source imagery was inspected in this tranche.

## What the records actually provide

| Diagnostic window | Exact intersecting reaches | Source classifications | Reported rates |
| --- | ---: | --- | --- |
| Entire acquisition rectangle |1,148|719accreted;358erosion-hazard;62below-noise;9erosion without rate|1,047populated; -44.48to73.61m/year |
| Northern rectangle [-124.18,46.72,-123.95,46.8] |158|45accreted;101erosion-hazard;8below-noise;4erosion without rate|140populated; -35.53to63.02m/year |
| Prior island lookup [-124.050,46.625,-124.025,46.638] |2|Both below-noise|No populated rate, start/end year or feature type |

These are declared rectangular diagnostics, not authenticated study-area or island boundaries. The rate ranges mix different image intervals and vegetation-line/shoreline classes. They are source attributes, not recalculated displacements or independent uncertainty estimates. Nearby positive and negative values cannot establish either synchronous upheaval or a conserved sediment budget without the original boundaries, sampling and temporal controls.

The island-intersecting records are OBJECTID3299and3382. Both have rapid-assessment status, null boundary type, null years and null rate. The application defines its below-noise label to include undetected change or apparent image misalignment without erosion signs. Neither record supplies a numerical detection threshold. A classification therefore cannot be turned into measured zero movement, a dated stable shoreline or absence of substantial historical change. Their long reach geometry is not a homologous match to the 1922 marsh curves.

Native layer metadata declares EPSG2927 and geometry lengths in feet; queried geometry is EPSG4326 and rate aliases are metres/year. Do not interpret Shape__Length as metres or infer a surveyed tidal datum from the generic Shoreline label. Change and Average_Change attributes agree for these selected records, so those fields provide no independent confirmation.

## Consequence and next test

Modern mapped change is spatially heterogeneous, but the target island remains unquantified in this dataset. Retrieve original image pairs and source transects for3299/3382, determine whether the assessed vegetation/shoreline coincides with the historical boundary, and recover a numerical uncertainty threshold before computing a dated change. Northern records provide separate inputs to investigate channel/storm controls; they cannot substitute for southern island observations. This is retrospective source recovery, not a frozen prospective success, independently reviewed reconstruction or evidence of fabricated history.
