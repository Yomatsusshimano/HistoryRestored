# Missoula: model constraints and unresolved mismatches

2026-10-08. C008 / S27. Sourced draft; no independent review or simulation rerun.

[Denlinger et al. (2021), author PDF](https://dlgeorge.github.io/pubs/DenlingerGeorgeEtAl2021.pdf), DOI [10.1130/2021.2548(17)](https://doi.org/10.1130/2021.2548(17)). Printed page numbers below exclude the PDF's preliminary profile sheet. Relevant methods/results text inspected; Table 1 page 5 and scenario paragraph page 11 visually checked. Copyrighted PDF is linked, not republished.

## Source audit

The study uses GeoClaw, terrain reduced from 30 to 185 m spacing, removed modern dams, adaptive refinement and instantaneous dam removal (p. 8). Six blockage scenarios are compared. Figure 5 specifies initial Lake Missoula elevation 1265 m. This is not the older study's 1250 m case.

Table 1 supplies field controls, not exact water levels. Erratics are minimum constraints; uncrossed divides supply upper constraints (pp. 7–8). The seven selected rows in [the data file](../data/missoula-controls.json) retain separate field and terrain elevations.

Long site 11 lists 476 m field elevation versus 379 m terrain elevation. Page 11 reverses the 2a/2b open/blocked labels defined on page 10. Neither discrepancy is silently corrected. Figure 10's sediment-volume adjustment is explicitly awaiting dynamic erosion/transport/deposition testing (p. 16).

## What we can test now

The [executable audit](../analysis/missoula_controls.py) subtracts terrain elevation from field elevation for each transcribed row. The [result](../analysis/missoula-controls-result.json) checks the arithmetic and retains the 97 m discrepancy. This is **not a model-stage residual**: terrain height and floodwater height are different quantities. It does not establish which column or location is wrong, if either is wrong. Inspecting the original site record and coordinate transformation is the next way to distinguish transcription, registration and topographic explanations.

Selection was retrospective and purposive: three adjacent Wenatchee records to retain the apparent outlier, and two Grand Coulee crossing/noncrossing pairs to preserve contrasting constraint types. It is neither the full table nor a held-out validation set. No date ties these controls to one common flood. No Gaussian measurement uncertainty is assigned from map contour spacing. Source datums and null uncertainties remain explicit.

## Required before a predictive run

Obtain the actual modified terrain, blockage geometry, numerical configuration, solver version, refinement criteria and output gauges. Preserve hashes and reproduce one scenario before proposing a new one. A terrain raster downloaded today cannot silently substitute for the published modified surface.

Compare modeled stage at each coordinate with the appropriate one-sided bound and its measurement/context uncertainty. Do not average a lower and upper constraint from different places into one alleged measured water level. Assess positional and vertical datum compatibility first. Search the unextracted table and underlying field records for further discrepancies before using the seven rows as representative.

Then test conservation, resolution sensitivity, sediment entrainment and changes in ancient terrain. Keep calibration sites separate from genuinely uninspected validation sites. A model tuned to known scars cannot count those same scars as new successful predictions. Obtaining a regional fit would still leave the proposed worldwide event, wildlife chronology and historical-rewriting claims to be tested separately.
