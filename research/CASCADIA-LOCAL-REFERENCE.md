# Copalis local-reference test

2026-10-09. Follow-up to the [Long Island sensitivity audit](CASCADIA-ALIGNMENT-SENSITIVITY.md). Retrospective analyst processing, using S229 measurements and S231's named reference trees. No new calendar or root death date is assigned.

## Method and scope

The S231 supplement's Table S1 footnote identifies CP-791, CP-793 and CP-794 as a local master used for CP-789, CP-790 and CP-GF2. We use raw identifiers CP791, CP793 and CP794 from wa130. Our [script](../analysis/cascadia_local_reference.py) retains the previous sensitivity transformations: adjacent log-width or width differences, normalization across each series, then annual averaging of available reference series. These are not the original decay-curve, spline and time-series calculations.

All eight wa130 series are retained. When testing one of the three reference trees, it is omitted from its own master. Three CPGF2 series remain individual measurements of one tree; their agreement cannot count as independent trees. Reference year labels are inherited from the archive.

The initial calculation required each target's complete span to fit within the local reference. CP790, CP791 and CP794 lacked complete reference coverage at their published placements, leaving their rank unknown under that rule. After identifying this coverage limit, we added an explicitly retrospective second scope: trim each target to the years shared at its published placement, freeze that subset, then scan shifts. Both scopes and every candidate score are preserved in the [results](../data/cascadia-local-reference.json). Within a scope, all candidate scores use the same target observations. This is a diagnostic response to missing coverage, not a prospective test or recovery of the authors' exact overlap rule.

## Results for the fixed shared-year subset

| Raw series | Differences used | Tested shifts | Published rank, log differences | Published rank, width differences |
| --- | ---: | ---: | ---: | ---: |
| CP7892 | 347 | 8 | 1 | 1 |
| CP790 | 306 | 49 | 1 | 1 |
| CP791 | 268 | 71 | 1 | 1 |
| CP793 | 327 | 28 | 1 | 1 |
| CP794 | 262 | 82 | 1 | 1 |
| CPGF2A | 166 | 189 | 2 | 2 |
| CPGF2B | 104 | 251 | 9 | 11 |
| CPGF2NW | 256 | 99 | 1 | 1 |

CPGF2NW's published placement rises from fourth against Long Island to first against the local master, with correlations .2396 and .2165 for the two transformations. CPGF2A still ranks second; CPGF2B remains weaker. These short series contain fewer than200 differences and should not be judged as though they supplied the same information as the long series.

CP790's local correlations are .2288 and .2420 over306 differences. S231 reports303 years and r=.25 under its original processing. This proximity is not reproduction: time-series fitting removes some observations, and our transformation and averaging differ. No precision or significance is inferred from resemblance.

## Consequence for chronology testing

The weaker Long Island match alone is insufficient to assess CP-GF2's date. Its longest recovered trunk measurement agrees better with the source-selected local reference, while shorter radii retain exceptions. This supports local relative-pattern agreement under the declared calculation; it does not establish absolute years independently.

The comparison domain is narrower than the Long Island scan and contains varying reference depth, including years supported by one reference. A distant alternative excluded by the local span has not thereby been disproved. Local trees share climate and dating relationships. Jointly shifting the local master and target would preserve their relative match; therefore this calculation cannot test a common calendar shift.

Next recover original per-tree processed indices and the root-to-trunk anatomical/measurement crosswalk. The original published statistics and the exceptions in both diagnostic calculations remain preserved. No global chronology break, independent-review status or common catastrophe date follows.
