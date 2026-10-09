# Snag alignment against archived Long Island reference versions

2026-10-09. Retrospective diagnostic using S229's27 snag measurement series and S233's standard, ARSTAN and residual chronologies. This adds actual archived processed reference outputs to the earlier raw-derived reference comparison. It does not reproduce the original study's per-radius target processing, authenticate the exact1997 reference version, or independently establish calendar dates.

## Declared calculation

The [script](../analysis/cascadia_archived_reference.py) hash-checks all inputs. For each reference version it compares each snag series separately using adjacent log differences and adjacent linear differences of both widths and reference indices. Positive values and contiguous year coverage are checked. Reference indices are already processed; this additional differencing is an analyst's diagnostic, not the original spline/autoregressive procedure.

Every integer placement retaining complete target overlap is evaluated by Pearson correlation. Two separate upper bounds restrict assigned endpoints to1720 and1986; the lower bound comes from available full overlap, not the original study's full selection protocol. The1720 bound inherits radiocarbon chronology. No minimum-length or reference-count exclusion is imposed; short records remain visible. Every candidate correlation is stored as an ordered array with its initial shift in the [result ledger](../data/cascadia-archived-reference.json), alongside ranks, top-five alternatives and input hashes.

Reference-count diagnostics take the smaller of the two reported annual counts contributing to each difference. These are archive count fields, not independently established tree identities. They do not affect rankings. Known-shift recovery checks direction/alignment; published-position correlations are independently checked with NumPy's correlation formula, and a tenfold width conversion leaves the GF2NW scans unchanged. These verify calculation behavior, not dating.

## Results

| Archived reference | Transformation | Published placement ranks first, endpoint≤1720 | Endpoint≤1986 |
| --- | --- | ---: | ---: |
| Standard | Log differences | 23/27 | 23/27 |
| Standard | Linear differences | 24/27 | 24/27 |
| ARSTAN | Log differences | 23/27 | 23/27 |
| ARSTAN | Linear differences | 24/27 | 24/27 |
| Residual | Log differences | 21/27 | 21/27 |
| Residual | Linear differences | 21/27 | 21/27 |

These are dependent series and repeated transformations, not independent trees or six replications. The identical counts across bounds do not establish identical candidate ranks everywhere; all ranks are retained in the ledger.

Selected ranks under the1720 bound:

| Series | Standard log | Standard linear | ARSTAN log | ARSTAN linear | Residual log | Residual linear |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| CP790 | 1 | 1 | 1 | 1 | 3 | 1 |
| CPGF2A | 6 | 12 | 6 | 12 | 4 | 15 |
| CPGF2B | 66 | 40 | 70 | 41 | 98 | 94 |
| CPGF2NW | 7 | 6 | 7 | 7 | 10 | 6 |

Standard/ARSTAN log exceptions are CP794 and the three CPGF2 records; their linear exceptions are the three CPGF2 records. Residual log exceptions are CP790, CP794, CPGF2A/B/NW and PR7774. Residual linear exceptions are CP7892, CPGF2A/B/NW, CC5821 and PR7772. No exception is removed to improve the count.

CP790's residual-log rank3 contrasts with rank1 in the earlier raw-derived diagnostics and in five current variants. S231 reports rank4 under original processing. This reinforces method sensitivity; it does not reproduce the source statistic.

CPGF2NW again has a best shift−392, giving a diagnostic assigned endpoint1283, in all six variants. The best correlations are .2544-.2889; their reference count minimum is1 and median2. This alternative persists with archived outputs, but the outputs derive from the same reference collection. It is not independent evidence of a replacement date. The local-reference and root/trunk tests remain relevant additional constraints.

Sparse reference support is not a universal explanation for exceptions. CPGF2A's residual-linear best shift is+6, assigned endpoint1654, with r=.25345 and reference count minimum12/median14. The published position has r=.17650 and rank15 in that variant. This is a consequential retained exception under the declared method, not proof of its cause or a revised calendar assignment. CPGF2B has only104 annual differences, below the original study's usual200-year reference-overlap threshold; its individual-series ranks cannot stand in for a combined-tree analysis.

## What changes in the broader investigation

Most series continue to favor source-relative placement under these declared transformations. Uniform robustness across processing variants is not established. Choosing the best-performing version after observing these results would exaggerate agreement; all versions are published together.

Archived reference outputs narrow the access gap, but applying simple differences to unprocessed target widths and already processed indices remains a hybrid diagnostic. Original target indices, averaging and version identity are needed to reproduce the published method. Same-tree roots/trunks and published anatomical tracing reports also constrain correspondence separately from these width ranks.

No test here shifts the absolute reference calendar, dates root death directly, identifies a chronology break, or connects Cascadia to distant urban fill or fossils. No significance probability or combined confidence is assigned. Next obtain or reconstruct fully declared per-radius processing and combined-tree averages, checking that they reproduce source values before interpreting calendar alternatives.
