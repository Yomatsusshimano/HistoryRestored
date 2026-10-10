# Complete Missoula control table and limits on model comparison

2026-10-09. C008 / S27. Sourced draft; no hydraulic simulation or independent review.

The complete Table 1 of [Denlinger et al. (2021)](https://dlgeorge.github.io/pubs/DenlingerGeorgeEtAl2021.pdf), printed pp. 5-6 / PDF pp. 6-7, contains **47 rows**, not just the eleven previously selected in this archive. Both table scans were re-inspected. All numeric cells, contour intervals, reference labels and gray nonexceedance shading are now retained in [the complete transcription](../data/missoula-table1.json), with the original PDF hash. Local row identifiers are not original field identifiers. The earlier eleven-row file remains an explicitly selected historical extraction; its numerical entries agree with the corresponding complete-table rows.

Seventeen rows are shaded as nonexceedance controls, interpreted as upper bounds; thirty other rows describe crossing, deposits or erosion. Those thirty have differing evidential strength. An erratic or eroded surface is not an exact maximum water level. The source's pp. 7-8 discussion also treats groups of erratics as evidence for broader flood limits. Original context and event association are still required before assigning any row a precise peak-stage constraint. These authors' selected controls are not a census of every field observation and are not an independent held-out set.

## Numerical and spatial diagnostics

The [executed audit](../analysis/missoula_table_audit.py) and [results](../analysis/missoula-table-audit-result.json) preserve the following findings:

| Diagnostic | Complete-table result | What remains unresolved |
| --- | --- | --- |
| Field versus terrain elevations | 43 comparisons; Long-11 differs by +97 m, row 42 by +16 m, row 39 by -11 m; all other absolute differences are at most 8 m | These are field-minus-terrain differences, not flood-stage errors. Actual numerical inputs and terrain registration remain unavailable. |
| Missing registration | Final four rows retain blank projected coordinates and terrain heights | Publication blanks do not establish whether the authors used these controls elsewhere in their simulations. |
| Printed feet/metres conversion | Row 40 prints 1360 ft and 420 m; literal conversion gives 414.528 m, a 5.472 m difference | No value is corrected. Original field/source records must distinguish transcription, approximation or different elevation conventions. |
| Smaller conversion differences | Row 41: 1660 ft / 505 m; row 42: 1670 ft / 510 m | Differences of -0.968 and +0.984 m exceed nearest-whole-metre conversion rounding, but these rows use 5 m contour maps. A conversion screen does not establish measurement error. |
| Nearby opposite controls | Lynch Coulee crossing, 433 m, and Evergreen-Babcock noncrossing, 431 m, lie approximately 98.8 m apart in geographic coordinates | They are different locations, not one measured stage interval. Original relief, positional precision, datum, interpretation and event correlation must be checked. |

The last pair cannot constrain a single *level* peak water surface if both field elevations and bound interpretations are taken as exact. That is a conditional incompatibility of an additional level-surface assumption, not a contradiction of every moving flood: spatially varying stage, source uncertainty or differing event associations require their own evidence. The crossing row cites an O'Connor interpretation and a 20 ft contour map; the noncrossing row cites a Waitt interpretation, with no contour interval specified. Treating them as two exact measurements of the same event would add unsupported precision and correlation. Contour spacing is not a statistical uncertainty or a demonstrated correction.

The proximity diagnostic retains every opposite-bound pair separated by less than 250 m on the assumed sphere, yielding four pairs. This is a retrospective search radius, not a measured uncertainty or a hydrological criterion for a shared water surface.

## Coordinate screening and a rounding-sensitive flag

For every pair within 15 km in the printed geographic representation, the audit compares spherical distance against distance in the printed projected coordinates. The sphere radius is explicitly assumed, 6371008.8 m. The retrospective ratio band 0.95-1.05 is a screening choice, not the source projection, a confidence interval or a pre-registered rejection threshold. Albers parameters remain unrecovered; no datum transformation is claimed.

Among sixty eligible pairs, five fall outside that band. Four involve Long-11, extending the previously noted geographic/projected mismatch to both Burch Mountain Road records. The fifth is the two Burch Mountain rows: 18.69 m spherical versus 19.72 m projected, only 1.03 m apart in distance despite a 5.5% ratio difference. Integer projected coordinates and four-decimal-degree geographic tokens make ratios at this separation sensitive to rounding. This fifth flag must not be given the same interpretation as kilometre-scale Long-11 discrepancies. The complete screening does not identify corrected coordinates or prove what entered the authors' model.

## Verification and model consequence

All 47 coordinate pairs, printed feet/metres pairs, contour values and projected/terrain triples were checked against a separate PDF text extraction after scan inspection. Gray shading was checked visually. All eleven legacy numerical records agree, including nulls. This verifies transcription and arithmetic; the original survey data, model surfaces and flood chronology remain unvalidated.

Before a physical reconstruction is judged against these controls, recover its actual stage outputs, modified terrain and projection definition. Compare stage locally with one-sided bounds of justified uncertainty and context. Do not replace missing coordinates with a fitted projection, average nearby limits into an alleged observation, treat terrain height as water height, or turn these inspected discovery controls into successful prospective predictions. Original Waitt/Long/Stanton field context remains a retrieval target; the USGS abstract record supplies no Long-11 table or correction.

The complete table strengthens the input audit for objective 5. It establishes neither a common flood date, an alternative discharge, a worldwide deposit nor the historical-rewriting propositions.
