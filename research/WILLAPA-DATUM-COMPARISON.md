# Willapa paired-coordinate transformation diagnostic

2026-10-09. C004 / S253. The recovered database contains two coordinate copies of the same survey features. This comparison advances spatial preparation for the geography test; it does not measure coast change.

The [script](../analysis/willapa_datum_comparison.py) decodes the published [row export](../data/willapa-geodatabase-rows.json), checks identical geometry types, part starts and vertex counts by feature ID, and transforms the declared NAD27 UTM zone 10N coordinates to the declared NAD83 geographic coordinates. Residual distances use the GRS80 ellipsoid. All 129 line and 54 polygon features match point-for-point: 10,275 vertex entries, including repeated polygon closure and shared vertices.

Initially no non-ballpark operation was available locally because transformation grids were missing. Two open grids were downloaded with normal TLS verification from the official PROJ CDN into a task-local directory. PROJ network access remained disabled and ballpark operations prohibited. The [result ledger](../data/willapa-datum-comparison.json) preserves grid URLs, byte counts, SHA256 hashes, software versions, full pipelines, per-feature summaries and every point residual. Reproduction requires downloading those exact grid versions and comparing their hashes; a changed CDN file must not silently be treated as the same input.

| Operation | Median residual | RMS residual | Maximum residual |
| --- | ---: | ---: | ---: |
| NAD27 to NAD83 (1), older NADCON CONUS grid | 0.000003865 m | 0.000004172 m | 0.000009422 m |
| NAD27 to NAD83 (7), NADCON5 CONUS grid | 0.111174 m | 0.115117 m | 0.161398 m |

Both operations declare 0.15 m accuracy in the installed operation database. That metadata is not a measured accuracy of this historical map. A proposed 0.001 m forward/inverse round-trip check failed for NADCON5: its maximum round-trip residual is 0.059593 m. The older NADCON operation's maximum is 0.000000003167 m. The ledger retains both per-feature results; no submillimetre inverse-consistency pass is claimed for NADCON5. The cause of its inverse discrepancy is unresolved and needs operation-specific investigation before using that pipeline for precision bidirectional work. Script versions are pyproj 3.8.0 and PROJ 9.8.1. Coordinate axis order is explicitly longitude/easting first.

The exceptionally close older-grid agreement strongly supports coordinate consistency with that transformation. It does not identify the original GIS software, authenticate every digitized source line, or independently establish which processing workflow was used. Choosing the newer operation would introduce a small systematic difference relative to the stored geographic copy; publishing both prevents that difference from being mistaken for physical movement.

[PROJ's operation-computation documentation](https://proj.org/en/stable/operations/operations_computation.html) explains grid availability, operation selection and ballpark alternatives. Its [cs2cs documentation](https://proj.org/en/stable/apps/cs2cs.html) identifies the NADCON5 grid requirement. Current online documentation is newer than the installed runtime; the ledger records what actually executed. The grid resources are [older CONUS NADCON](https://cdn.proj.org/us_noaa_conus.tif) and [CONUS NADCON5](https://cdn.proj.org/us_noaa_nadcon5_nad27_nad83_1986_conus.tif).

No tolerance here validates the field survey, tidal datum, vegetation-edge classification, rectification accuracy or source date. The paired tables share a source and are not independent geographical observations. Next authenticate comparable shoreline classes against the raster and survey revisions, then obtain a dated modern comparison with its uncertainties. The missing earlier marsh sheets remain a separate retrieval task. No worldwide event, chronology break, independent review or completion of the twenty-part objective follows.
