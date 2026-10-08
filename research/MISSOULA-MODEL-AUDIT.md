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

### Coordinate diagnostic added 2026-10-08

The executable audit now compares pairwise distances in the two printed coordinate representations. It uses an explicitly assumed sphere for latitude/longitude and Euclidean distances for projected metres. These calculations require no invented Albers projection parameters, but they are a screening diagnostic, not a complete datum transformation.

| Pair | Spherical distance (km) | Projected distance (km) | Projected / spherical |
| --- | ---: | ---: | ---: |
| Long 10–11 | 3.406 | 12.707 | 3.731 |
| Long 11–12 | 1.514 | 8.316 | 5.492 |
| Long 10–12 | 4.914 | 4.894 | 0.996 |
| Baker 5 uncrossed–crossed | 1.656 | 1.661 | 1.003 |
| Baker 8 uncrossed–crossed | 0.516 | 0.517 | 1.002 |

Our inference: Long 11 warrants a coordinate/row-registration audit before interpreting its 97 m field–terrain difference as topographic error. The pattern is not explained by a uniform scale adjustment shared by these nearby Wenatchee rows. It does not identify the correct coordinate or prove which data entered the authors' simulations. Keep the printed values; flag the row for investigation rather than deleting it or substituting a guessed correction. These selected comparisons do not establish that the remaining table is error-free.

### Executable-package search

The [availability record](../data/missoula-model-availability.json) pins a separate GeoFlood example and records missing inputs. No equivalence to S27 has been established. Its referenced lake-input filename contains 1295; file contents and actual initialized stage remain unverified. This cannot replace S27's reported 1265 m initial stage by assumption.

The inspected repository tree lacks the three referenced Missoula raster files. The linked Zenodo archive's complete central-directory listing contains 548 entries and no Missoula-named paths. Only its directory was retrieved, not all compressed file contents; this is not proof that no relevant data exist anywhere. The author-associated repositories inspected yielded no Missoula/Columbia/scabland path-name matches. These limited searches document a reproduction gap, not misconduct or a refutation of the floods.

Obtain the actual modified terrain, blockage geometry, numerical configuration, solver version, refinement criteria and output gauges. Preserve hashes and reproduce one scenario before proposing a new one. A terrain raster downloaded today cannot silently substitute for the published modified surface.

Compare modeled stage at each coordinate with the appropriate one-sided bound and its measurement/context uncertainty. Do not average a lower and upper constraint from different places into one alleged measured water level. Assess positional and vertical datum compatibility first. Search the unextracted table and underlying field records for further discrepancies before using the seven rows as representative.

Then test conservation, resolution sensitivity, sediment entrainment and changes in ancient terrain. Keep calibration sites separate from genuinely uninspected validation sites. A model tuned to known scars cannot count those same scars as new successful predictions. Obtaining a regional fit would still leave the proposed worldwide event, wildlife chronology and historical-rewriting claims to be tested separately.

### Four additional bounds with incomplete model registration

The continuation of Table 1, printed p. 6 / PDF p. 7, was visually inspected. Its final four rows expand the extracted set from seven to eleven:

| Local label | Latitude / longitude | Field elevation (m) | Constraint |
| --- | --- | ---: | --- |
| Evergreen-Babcock-1 | 47.0956 / -119.9602 | 419 | Noncrossing, upper bound |
| Evergreen-Babcock-2 | 47.2118 / -119.9687 | 431 | Noncrossing, upper bound |
| Camden-saddle | 48.0808 / -117.1970 | 880 | Noncrossing, upper bound |
| Camden-gap | 48.0813 / -117.2239 | 795 | Crossing, lower bound |

The source leaves projected x/y and terrain elevation blank for all four. Feet and contour interval are also unspecified. The executable audit now reports null field-minus-terrain comparisons and lists these unavailable rows. These blanks do not prove that the authors omitted the sites from their simulation; actual input/gauge files are still needed. The two Camden values refer to different locations and cannot be treated as an 85 m uncertainty interval around a single water-level measurement.

The first two rows cite Waitt interpretation; the last two cite Waitt et al. (2019). This extraction is another portion of S27, not independent field confirmation. Noncrossing interpretation, event correlation and terrain registration must be checked before these become quantitative model rejection thresholds. This purposive extension was selected for missing-data diagnosis, not as an untouched validation set.

Attempts to retrieve the underlying Wenatchee table and a separate USGS Willamette spatial-data package remained unsuccessful. Neither dataset is claimed as inspected. Long-11's discrepancy remains unresolved, and the regional hydraulic run remains pending its actual inputs.
