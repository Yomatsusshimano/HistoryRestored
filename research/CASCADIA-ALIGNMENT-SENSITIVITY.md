# Alternative ring-alignment processing

2026-10-08. Retrospective diagnostic using S229 raw files. This does not reproduce S231's decay curves, splines, time-series models, tree averages, local references or anatomical comparisons. No root death date is changed.

## Declared calculation

[Script](../analysis/cascadia_alignment_sensitivity.py) checks input hashes and uses all27 non-Long-Island measurement series separately. All widths are positive in these inputs. It takes adjacent differences of either log widths or integer widths. Each reference series is centered and divided by its sample standard deviation across its complete differenced span. Reference values are averaged by assigned year. This reduces slow variation without claiming the original detrending method.

Two weighting versions use either all21 reference series equally or merge LI766I/O and LI767I/O before averaging19 groups. Those pairings are an identifier-based sensitivity assumption, not a verified specimen crosswalk. This retains the published Long Island calendar and all its dating dependencies.

Every integer shift with complete reference overlap is tested by Pearson correlation. Each target keeps the same number of observations across its candidate shifts. Separate summaries impose endpoint upper bounds1720 and1986; the lower endpoint follows available full overlap, not the original1192 bound. This is not an exhaustive test of every historically possible alignment. No p-values or independent-tree success fractions are calculated.

## Results

| Transformation | Reference weighting | Published placement ranks first, endpoint ≤1720 | Endpoint ≤1986 |
| --- | --- | --- | --- |
| Log differences | Equal series | 22/27 | 22/27 |
| Log differences | Paired IDs merged | 22/27 | 22/27 |
| Width differences | Equal series | 24/27 | 24/27 |
| Width differences | Paired IDs merged | 24/27 | 24/27 |

The [results](../data/cascadia-alignment-sensitivity.json) retain each published correlation/rank, candidate count, top five alternatives, overlap length and selected reference-depth diagnostics. These are dependent radii and repeated analyses, not27 independently dated trees or four replications.

For log differences, exceptions are CP794, CPGF2A, CPGF2B, CPGF2NW and PR7774. For width differences, exceptions are the three CPGF2 series. CP790 ranks first in all four versions (r≈.193–.235), whereas S231 reports fourth place under its original processing. The result shows method sensitivity; it does not overwrite the original reported statistic.

CPGF2NW ranks fourth in every version. Its best alternative shifts−392 years, to a trunk endpoint1283, with r≈.282–.284. That comparison uses a reference supported by as few as one series and a median of two. Sparse reference coverage, different signal processing, other radii, local-tree matches and the root/trunk evidence must be examined before interpreting this as a candidate date. It is not a proposed replacement chronology. The short CPGF2B series is also weakly placed by this diagnostic; its104 differences are below the original study's usual200-year reference-overlap criterion.

## What this tests

Most recovered series favor the published placement under these simple transformations. A claim that none has a matching signal is challenged within this test. Several individual series do not rank first, so uniform robustness is also unsupported. No conclusion about a worldwide chronology break follows: the reference calendar remains fixed, and the test changes relative placements only.

Synthetic checks recover a known shift with the correct sign and verify invariance to a tenfold unit rescaling. Published-position correlations are checked against NumPy's correlation calculation. These checks support implementation behavior, not historical dates. Next assess original per-tree averages, local-master dependencies and full processing settings, retaining these exceptions.
