# Physical reconstruction: constraints before fitting

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

## Model comparison

Start with local explanations and their published measured parameters. Fit a candidate catastrophe model on a declared discovery subset. Freeze parameters; predict held-out sites. Compare error, uncertainty, and number of unsupported adjustments. Do not use qualitative resemblance as a fit statistic.

The present cases include positive examples of catastrophic processes and alternatives to catastrophic burial. They supply methodological comparisons, not a unified reconstructed geography.

## Source-constrained regional benchmark

The [Missoula audit](research/MISSOULA-MODEL-AUDIT.md) now supplies seven mapped field controls and separates observational bounds from modeled terrain. Its executable elevation check is not a hydraulic model. Obtain and reproduce the published terrain/configuration before extending it, and preserve unresolved source discrepancies. No worldwide fitted reconstruction follows from this benchmark.
