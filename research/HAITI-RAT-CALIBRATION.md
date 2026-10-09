# An early rat date remains a challenge to check

2026-10-09. S36/S316/S128; retrospective calibration diagnostic, not an independent specimen validation or rat-arrival model.

The original [Cooke and Crowley2022 article](https://par.nsf.gov/servlets/purl/10336169) was available in the local research cache despite renewed web access failure. Pages4and5 were visually reinspected. Table2 confirms UF293844/UCIAMS191028, Rattussp.,435±15radiocarbonBP,490–515calBP,atomicC:N3.4. Subtracting the calendar endpoints from1950 gives1435–1460CE. The [2026article](https://journals.sagepub.com/doi/10.1177/09596836261458223) cites1435–1468CE for the same assay. The [crosswalk](../data/haiti-rat-citation-crosswalk.json) records coverage, PDF hash and unresolved cause; neither result was overwritten.

## What the original source does and does not explain

The2022discussion describes both rat dates as contemporary with colonization and suggests rapid dispersal to the upland site. It does not reconcile the earlier490–515calBP range with its stated1492contact date. The table's summary502.5±12.5 is also not a Gaussian standard error: its footnote constructs summaries from rounded two-sigma endpoints, despite the column's one-sigma label. The diagnostic below therefore uses the original435±15radiocarbon assay and never the calendar summary as a likelihood.

The methods describe mandible selection, collagen extraction and quality assessment. Individual collagen yields are not tabulated. Multiple native and introduced taxa were recovered from the upper5cm, with sediment bags removed for later sorting. This is a coarse collection context, not an individual dated-mandible position or a demonstrated simultaneous deposit. Rattussp. in this source must not silently become an independently authenticated Rattusrattus specimen.

## Separate, executed calibration diagnostic

The [calculator](../analysis/haiti_rat_calibration_check.py) uses the existing IntCal20 source S128, fetched again from its [official data URL](https://intcal.org/curves/intcal20.14c). Its SHA256 matches the previously acquired9501-row curve. It linearly interpolates curve mean and sigma, adds assay and curve variances, and normalizes a Gaussian likelihood over a discrete uniform1000–1950CE calendar prior. No reservoir or contamination offset is imposed. This method is not a reproduction of CALIB8.2 or OxCal4.4.

At a0.25-year grid the [results](../analysis/haiti-rat-calibration-check-result.json) are:

| Diagnostic summary | Result |
| --- | --- |
| Mode | 1448.00CE |
| Equal-tail95.4% interval | 1437.00–1468.25CE |
| Highest-density95.4% segments | 1435.25–1460.25 and1463.75–1468.25CE |
| Conditional normalized mass at/after1492CE | 0.0003671, approximately0.0367% |

The second high-density segment gives a concrete candidate explanation for the differing published upper endpoints: one summary may describe the principal segment and another the full envelope. This is **not an authenticated explanation**; the original software outputs and interval settings have not been recovered. Both published records remain, with the difference unresolved.

The [grid check](../analysis/haiti-rat-calibration-grid-check.json) repeats0.5-,0.25- and0.125-year spacing. All retain a1448mode and two high-density segments; the conditional post1492mass varies from approximately0.0365% to0.0371%. Negligible boundary mass checks that the chosen calendar-domain edges are not cutting a material likelihood tail. These are numerical checks, not evidence that the specimen is correctly identified or unaffected by dietary or chemical biases.

## Consequence for the chronology test

Under this declared no-offset model, the assay is overwhelmingly assigned before1492. Generic calibration complexity therefore does not justify simply calling it a post-contact date. The calculation's conditional mass is **not** the probability that rats arrived before1492 or that historical chronology was fabricated. It conditions on an assay, model, prior and curve whose specimen-level applicability still needs testing.

Likewise, a surprisingly early result is not enough to discard the assay. Photographs and museum accession history, original laboratory certificates, independently repeated dating and specimen-specific dietary evidence would distinguish a genuinely early animal from identification, context or dating problems. No numerical correction is invented from the expected historical date. Different death and deposition times remain separate possibilities.

This source discrepancy now has a testable numerical lead rather than only a conflicting citation. It neither dates a catastrophe nor revises the sloth mortality intervals. Next recover exact calibration segments and the specimen/laboratory records; independent review and all twenty original objectives remain incomplete.


## Specimen-linked enamel measurements recovered

The [2018supplement audit](RODENT-ISOTOPE-SPECIMEN-LINK.md) now matches all eight dated museum identifiers, includingUF293844. Its carbon/oxygen measurements are incisor enamel, not collagen. The general absence-of-isotope-values claim requires that distinction; no dietary correction or radiocarbon result is changed. Full methods, tissue identity and specimen-specific collagen records remain needed.
