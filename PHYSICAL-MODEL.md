# Physical reconstruction: constraints before fitting

### 2026-10-09 — Compare shoreline features in declared coordinates

The [Willapa vector audit](research/WILLAPA-VECTOR-AUDIT.md) distinguishes mean-high-water, apparent vegetation edge, approximation, control and added boundaries. Model inputs must choose comparable classes, not all129lines. Unsuffixed feature tables declareNAD27UTM10N; geographic copies declareNAD83. Degree/square-degree measures cannot stand for metres/area. Stored-geometry agreement does not validate datum transformations, actual coast positions or historical displacement; no modern comparison run.

### 2026-10-09 — Historical shoreline comparison requirements

The [Willapa survey audit](research/WILLAPA-HISTORICAL-SURVEYS.md) adds an original1873map and1922revision-method context. Resolve footprint, dated annotations, legend and vertical reference before classifying marsh or calculating change. Survey scale limits detection, and low-water observations constrained by tide availability cannot substitute for high-marsh elevation. Catalog update/vectorization years are not landscape dates. No displacement or recovery-rate model executed.

### 2026-10-09 — Soil geometry and preservation constraints

The [1997 report audit](research/CASCADIA-SOIL-CORRELATIONS.md) distinguishes generalized regional columns from surveyed sections, inferred paleoenvironmental displacement from mud thickness, and speculative correlations from observed continuity. Preserve soil formation/decomposition, growth-position plants and local dredge-spoil context in candidate models.150years of ample marsh recovery is not a lower duration bound. Calendar-before2000 and BP1950 labels require explicit epochs; limiting material ages cannot be pooled as direct earthquake times. No new flow model or chronology correction is established.

2026-10-08. Proposed model specification; no site-specific hydraulic model has been run.

## Separate mechanisms

Compare river flooding, marine inundation, debris flows, glacial outbursts, engineered fill, and earthquake-related subsidence as different models. They do not predict identical sediment or geography. A nonmarine catastrophe need not leave marine fossils; a tsunami may erode some sites and leave thin sand in others.

Required inputs: pre-event and present terrain with a stated datum; basin boundaries; water/sediment sources; source ages and mineralogy; grain sizes; candidate event duration; deposit maps; dated stratigraphy; land deformation; preservation and sampling coverage. Site-specific values are mostly uncollected.

## Conservation checks

For depositional footprint F:

- Bulk deposit volume V = integral over F of h(x) dA.
- Dry solid mass M = rho_s (1 - porosity) V.
- Source erosion/export must supply that mass; account for downstream/out-of-domain losses and compaction.
- Water discharge Q = wetted cross-sectional area times mean velocity.
- Water volume W = integral Q(t) dt, subject to storage, inflow, and losses.
- Gravitational transport energy scale E = mass times g times elevation drop. This is a scale check, not the full dissipative flow solution.

All terms need units and uncertainty. Present-day elevation alone is insufficient if substantial deformation is proposed; that deformation requires independent geological evidence.

## Executed illustrative calculation

Assumed area: 1,000,000 square kilometres. Assumed mean thickness: 2 metres. Assumed grain density: 2,650 kg/m3. Assumed porosity: 0.40.

V = 2.0e12 m3 = 2,000 km3.
M = 3.18e15 kg.

This is arithmetic for explicitly invented inputs. It estimates neither a measured deposit nor a real catastrophe. It helps expose the source-volume obligation a model of that size would face. The supporting command output is summarized in RESEARCH-LOG.md.

## Spatial predictions to freeze later

Derive inundation and erosion envelopes from terrain and source conditions. Predict low-energy deposition, high-energy erosion, provenance changes, and grain-size sorting with location-specific tolerances. Use proximal and distal transects and preserved unimpacted controls. Separate later regrading from natural deposition.

For a former coastline, combine topography/bathymetry, uplift/subsidence indicators, dated in-place deposits, and independently sourced maps. Do not simply reverse the coastline until selected observations fit.

For wildlife, map specimen coordinates and contextual age distributions before connecting habitat corridors. Distinguish living habitat from transported/reworked remains. Ecological feasibility and simultaneous occupancy are required; lines connecting modern fossil localities are insufficient.

## Copalis intrusion and extrusion benchmark

[Source-format comparison](research/CASCADIA-FORMAT-COMPARISON.md) shows that CSVrounded depths and extents lose stored information;18 positive extent cells become zero. Future input preparation must declare stored values, units and uncertainty rather than equating CSVzero with no exposed extent. Copalis depth-order exceptions persist in stored XLSXvalues and still require original sections. No new field measurement or hydraulic reproduction is supplied by recovering decimals.

The [Copalis vented-sand audit](research/COPALIS-VENTED-SAND.md) supplies68 reported observations with source-linked [GeoJSON](data/copalis-vented-sand.geojson). It is a regional process benchmark, not a dated worldwide horizon. Eleven records report vents; two combine observed venting with zero sheet thickness. Thickness ranges and unknown entries preclude treating every observation as a uniform blanket.

A candidate model must explain authenticated dike/sill/crater continuity as well as surface deposits, entrained wood/mud clasts and reported soil relationships. Compare surface inundation with groundwater venting, then distinguish possible shaking-induced liquefaction from speculative deformation of a deep aquifer. The latter's reported depth greater than35m is not a measured pressure head. Source sediment, hydraulic head, permeability, confinement, intrusion dimensions and dated sequence remain missing; no discharge, sediment volume or duration is computed.

Resolve A31/A40 coordinate differences and T6/T1/A31 depth-order inversions against original sections before fitting elevations or thickness gradients. Ten Ws material ages have limiting/not-applicable relations; do not use them as ten exact event ages or assign the regional W combination without checking correlation. A future held-out transect must be selected and publicly frozen before inspection; these already inspected points are discovery inputs.

## Model comparison

Start with local explanations and their published measured parameters. Fit a candidate catastrophe model on a declared discovery subset. Freeze parameters; predict held-out sites. Compare error, uncertainty, and number of unsupported adjustments. Do not use qualitative resemblance as a fit statistic.

The present cases include positive examples of catastrophic processes and alternatives to catastrophic burial. They supply methodological comparisons, not a unified reconstructed geography.

## Source-constrained regional benchmark

The [Missoula audit](research/MISSOULA-MODEL-AUDIT.md) now supplies eleven field controls, four lacking published projected/model values and separates observational bounds from modeled terrain. Its executable elevation check is not a hydraulic model. Obtain and reproduce the published terrain/configuration before extending it, and preserve unresolved source discrepancies. No worldwide fitted reconstruction follows from this benchmark.

The [published pulse alternative](research/MISSOULA-PULSE-ALTERNATIVE.md) now has an executed constant-discharge water-budget check. Its transcribed volume/discharge imply about 1,157 days, compared with about 100 days in the source. This is a consistency issue to resolve, not a reproduced hydrograph or a refutation of every pulse interpretation.

The [Moxee contact audit](research/MOXEE-FLOOD-COUNT.md) requires candidate models to explain sediment contacts and dike termination/crossing relationships. Unit count alone cannot set the number of hydrographs; a proposed deformation mechanism does not supply measured event duration.

The [regional flood discrimination](research/FLOOD-DISCRIMINATION.md) separates repeated units, independently initiated floods and elapsed time. It adds conditional magnetic recording thresholds: common rigid rotation preserves pairwise separation, while differential recording must be constrained before converting magnetic change into years. No validated field-rate bound or sediment-recording transfer model has been supplied.

The [Bouse mechanism comparison](research/BOUSE-DISCRIMINATION.md) specifies separate lake-outlet and marine-exchange requirements. Isotope change does not by itself supply salinity, basin storage, discharge or duration. Fit water and salt budgets to the same control volume and correlated horizons before comparing mechanisms. A historical through-going passage additionally requires a fixed map-derived route and chronology; no such fitted reconstruction exists here.

## Lower Colorado boulder-flood model requirements

The [original field accounts and burial audit](research/COLORADO-BURIAL-DATING.md) provide a second regional target. S220 reports a 22 km reach, projected roughly 45 m thickness and at least 20 m central-channel fill; its proposed extension toward Laughlin depends on correlation. These estimates are not a gridded deposit-volume measurement. S219's later projected thickness greater than 30 m must remain separately attributed until the sections and reconstruction conventions are reconciled. Do not multiply maximum thickness by the whole reach and an assumed width to report a measured volume.

| Required constraint | Evidence presently available | Input still needed before calculation |
| --- | --- | --- |
| Deposit geometry | Reported reach and thickness estimates; mapped surface units and selected photographs | Correlated basal/top contacts, cross-sections and erosion/preservation bounds with elevation datums |
| Sediment transport | Large mostly local boulders and smaller far-traveled quartzite; reported recycled clasts in younger units | Dimensions, density, source and position of each modeled clast; channel gradient and roughness; entrainment versus deposition conditions |
| Water budget | A regional flood interpretation | Source/storage mechanism, wetted geometry and boundary conditions sufficient to derive a hydrograph and integrate volume |
| Relative sequence | Inset units, tilted beds, cover, reported paleosols and separate younger terraces | Verified section correlations and exposure indicators; several direct unit relationships remain unobserved |
| Burial/exposure history | 22 isotope measurements, current sampling depths and diagnostic fits | Sample-specific provenance, time-varying overburden, erosion/exhumation and production/covariance inputs |
| Event date | Published model-dependent burial ages, with documented discrepancies | A reproduced physical age model and dates tied to the event unit; old clast signals must be distinguished from final redeposition |

The largest reported boulder and the longest reported transport distance are not measurements on one tracked clast. Combining them would invent a hydraulic constraint. Present sample depth similarly cannot substitute for past shielding. Until the missing inputs are obtained, no discharge, duration, sediment budget or historical event date is inferred from this target.

A useful discriminating observation is a measured Bat Cave cut section tying BC007–011 to the cover/base contact and mapped conglomerate. If the cobbles are in younger cover, model their inherited signal and final emplacement separately. If they are in continuous older conglomerate beneath cover, test its burial history in that context. Neither branch alone supplies a worldwide event. These are retrospective research decisions, not frozen predictions on uninspected sites.
