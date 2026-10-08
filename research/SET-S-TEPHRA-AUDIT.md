# Set S ash: stratigraphy, chemical discrepancy and timing limits

Research draft, 2026-10-08. C008. No independent review.

The original Little Boulder Lake core logs, assay identifiers and age model behind the approximately 40-year interval in S166 remain unrecovered. Targeted searches for the lake name with core, radiocarbon, tephra and author terms recovered repetitions of the claim but no inspectable original dataset. That is an access limit, not evidence that such records never existed.

## What the volcano-side record adds

[Mullineaux (1996), S168](https://pubs.usgs.gov/pp/1563/report.pdf), describes Sg below So. Its measured section S-1 places 1–2 cm of brown pumiceous ash between them. The described strongly weathered surface is at the top of So; Figures 24 and 26 show disturbance of that upper layer. This is not evidence for the same weathering interval between Sg and So.

Table 2 supplies contextual organic dates: W-3133, peat above upper set S, 12,120 ±100 radiocarbon BP; W-3141, charcoal beneath part of S, 12,910 ±160; W-3136, peat beneath upper S, 13,650 ±120. The report attributes these to Crandell and colleagues (1981). They are not three new direct eruption dates. In particular, W-3141 already appears elsewhere in this inventory. The source warns that organic dates constrain deposits and that laboratory uncertainty can underrepresent correlation uncertainty.

These data do not identify a decades-long So–Sg separation. Subtracting two contextual central ages would manufacture a precise eruption interval from materials with different stratigraphic relationships. Equally, absence of a quantified interval does not prove simultaneous eruption or deposition.

## A reproducible chemical discrepancy

S168 pp.34 and 36 describe Sg glass as having lower calcium and iron relative to potassium than So. However, ratios calculated from the published means in [S167 Table DR2](https://doi.org/10.1130/2003023) have the opposite ordering, both for the reference standards and for the paired deposits. Table DR2 was visually inspected in the preceding audit; the disputed prose is confirmed in the original USGS PDF, not just its HTML transcription.

| Comparison | Fe2O3/K2O, So | Fe2O3/K2O, Sg | CaO/K2O, So | CaO/K2O, Sg |
| --- | ---: | ---: | ---: | ---: |
| Reference standards | 0.5446 | 0.6028 | 0.6429 | 0.7430 |
| Zillah | 0.5368 | 0.5848 | 0.6580 | 0.7054 |
| Burlingame | 0.5408 | 0.5808 | 0.6094 | 0.6987 |

[Transcribed inputs](../data/set-s-tephra-check.json) and [calculation](check_set_s_ratios.py) preserve the published labels. These are ratios of means, not individual-shard ratios or significance tests. Converting the same oxides to elemental mass consistently would multiply each ratio by a fixed positive factor, preserving the ordering; it would not resolve this discrepancy. Raw shard covariance is unavailable, so no confidence interval is assigned.

The discrepancy does **not** show which source is wrong, demonstrate switched labels, erase the stratigraphic order, or prove the deposits are identical. Differences in reference specimens, within-eruption variability, analytical treatment and reporting errors remain possibilities requiring evidence. The next source to recover is the 1978 glass analysis and specimen linkage cited by the 1996 report, followed by any published corrections. Until that comparison is possible, preserve both records and avoid treating the prose diagnostic as independently verified.

The [magnetic audit](TOUCHET-MAGNETIC-AUDIT.md) remains a separate observation and inference chain. Neither this chemical discrepancy nor the missing core record supplies positive evidence of a single global event or fabricated chronology.

Inspection: S168 printed pp.8,34,36 visually checked; p.9 dating discussion and publisher HTML set S/section S-1 read as text. Remaining report pages and original assay certificates are not claimed as audited. Reproduce the ratio arithmetic with `python research/check_set_s_ratios.py`.
