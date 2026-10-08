# Grand Coulee: terrain and validation audit

2026-10-08. C008; sourced draft, not independently reviewed.

[Lehnigk and Larsen (2022), S125](https://doi.org/10.1029/2021JF006135), section 3.1 and Table 1, report east-rim inundation at 2.6 million m³/s on reconstructed cataract terrain. Present-day terrain requires 17 million with Foster Coulee open, or 14 million closed. These are model outputs, not measured ancient discharges. The simulations assume clear water. High-water evidence constrains discharge; it is not a held-out validation target.

Our inference: the same mark can support different discharge estimates when terrain and routing assumptions change. This does not establish a worldwide catastrophe, resolve flood count, or validate the earlier reservoir proposal. Reproduction should compare paired terrain scenarios at identical boundary conditions, then assess controls not used to select discharge. No model was run here.

## Executable data lead

The [dataset README, S126](https://scholarworks.umass.edu/bitstreams/a06e913f-1976-4af0-8e2c-fa6fa0e6dbf1/download) was successfully downloaded despite web-tool failures. Its scenario inventory describes elevation grids, projections, boundaries, Python simulations, netCDF outputs and MATLAB processing. Sections K–L identify roughness-0.04 alternatives. Input files are shared at boundary-variation level, so individual discharge folders alone may be incomplete.

The [ZIP bitstream](https://scholarworks.umass.edu/bitstreams/e0eb9412-d19e-4ba6-9be5-e6ad46eeb90a/download) downloaded successfully (284,322 bytes). Its directory lists nested column-count and area-error archives plus macOS metadata, not a complete hydraulic package. The [acquisition record](../data/grand-coulee-acquisition.json) preserves its hash and listing; nested contents remain uninspected. The README specifies ANUGA 2.0, Python 2.7.10, ArcMap 10.4.1 and MATLAB R2019b. These environments were not installed or tested. Locate the remaining model files and inspect scripts before execution. The README hash is retained in S126; source files are not republished here.

## Repository and nested archive follow-up

The [current repository API, S127](https://scholarworks.umass.edu/server/api/core/items/f7ace593-37f4-4f14-ac2b-818abd0976dc) explicitly directs the full dataset to [Grand_Coulee_Repository on Globus](https://app.globus.org/file-manager?origin_id=b9120884-93ae-4a90-9f91-1556b01569e7&origin_path=%2FGrand_Coulee_Repository%2F), with sign-in required. The complete ORIGINAL bundle listing has two entries: README.txt and area_error_column_counts.zip. This does not indicate missing research data; it identifies separate storage. [Access record](../data/grand-coulee-repository-access.json). No authenticated listing was attempted.

Subsequent nested inspection recovered the path GC_dimensions.xls and eight polygon shapefile sets. All eight projection files declare NAD27 / UTM zone 11N with metre units. [Hashed nested inventory](../data/grand-coulee-nested-inventory.json) and [reproducible inventory script](../analysis/grand_coulee_archive_inventory.py). Workbook cells and polygon geometry remain uninspected. The projection declaration applies to these ancillary files, not automatically every model surface. Future coordinate comparisons must verify each input datum and transformation; raw coordinates must not be silently treated as WGS84. No geometry fit, hydraulic output or independent physical prediction is validated by this inventory.
