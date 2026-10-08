# Grand Coulee: terrain and validation audit

2026-10-08. C008; sourced draft, not independently reviewed.

[Lehnigk and Larsen (2022), S125](https://doi.org/10.1029/2021JF006135), section 3.1 and Table 1, report east-rim inundation at 2.6 million m³/s on reconstructed cataract terrain. Present-day terrain requires 17 million with Foster Coulee open, or 14 million closed. These are model outputs, not measured ancient discharges. The simulations assume clear water. High-water evidence constrains discharge; it is not a held-out validation target.

Our inference: the same mark can support different discharge estimates when terrain and routing assumptions change. This does not establish a worldwide catastrophe, resolve flood count, or validate the earlier reservoir proposal. Reproduction should compare paired terrain scenarios at identical boundary conditions, then assess controls not used to select discharge. No model was run here.

## Executable data lead

The [dataset README, S126](https://scholarworks.umass.edu/bitstreams/a06e913f-1976-4af0-8e2c-fa6fa0e6dbf1/download) was successfully downloaded despite web-tool failures. Its scenario inventory describes elevation grids, projections, boundaries, Python simulations, netCDF outputs and MATLAB processing. Sections K–L identify roughness-0.04 alternatives. Input files are shared at boundary-variation level, so individual discharge folders alone may be incomplete.

The [ZIP bitstream](https://scholarworks.umass.edu/bitstreams/e0eb9412-d19e-4ba6-9be5-e6ad46eeb90a/download) downloaded successfully (284,322 bytes). Its directory lists nested column-count and area-error archives plus macOS metadata, not a complete hydraulic package. The [acquisition record](../data/grand-coulee-acquisition.json) preserves its hash and listing; nested contents remain uninspected. The README specifies ANUGA 2.0, Python 2.7.10, ArcMap 10.4.1 and MATLAB R2019b. These environments were not installed or tested. Locate the remaining model files and inspect scripts before execution. The README hash is retained in S126; source files are not republished here.
