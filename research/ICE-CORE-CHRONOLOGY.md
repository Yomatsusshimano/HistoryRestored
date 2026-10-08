# Ice-core corrections and independent checks

2026-10-08. C023 / S107. Sourced draft without independent review.

[Sigl and colleagues (2015)](https://doi.org/10.1038/nature14565), pp.544–545, reports ice-core isotope features placed seven years earlier than corresponding tree-ring markers on older timescales. Selected text and Figures 1–2 were visually inspected in the [institutional PDF mirror](https://www.whoi.edu/cms/files/sigl15nat_240284.pdf). The [structured ledger](../data/ice-core-anchor-audit.json) preserves the reported comparisons and marker roles; it contains no digitized concentration measurements.

Figure 2 identifies Greenland fixed markers at 536, 626, 775, 939 and 1258 CE. The authors also describe evaluating revised chronologies with historical observations, tephra and the 994 isotope event. The follow-up methods inspection below clarifies their reported separation from fitting; the underlying records remain unverified.

For this investigation, the key result is methodological. A marker used to assign an ice-layer date cannot then count as an independent confirmation of that assigned date. Independent measurement of different isotopes does not automatically mean independent calendar placement. Conversely, this dependency alone does not invalidate synchronization: a genuinely unused marker can test a model once its identity, uncertainty and exclusion from fitting are established.

This provides a concrete candidate for examining chronology disagreement under objective 10, without assuming a break affecting every historical record. It also supplies a traceable public correction process relevant to objective 16. Neither a global seven-year conversion nor a deliberate rewriting mechanism follows. Do not apply this correction to Bonneville, Electron, Seattle or fossil dates.

The [MacBlo audit](MACBLO-ANCHORS.md) already involves a tree-ring isotope-marker comparison. Counting that route and this ice-core route as entirely independent calendar confirmations would require auditing their shared reference chain first.

Next, retrieve the raw isotope series and documentary supplement. Reproduce the published model and its stated unused-marker checks. Because those markers and the paper's results are already known to us, reproduction would be retrospective, not a new successful forecast. We have not audited later replacements for this historical chronology or independently validated its precision.

## Follow-up: constraints and unused checks

Methods PDF p.9 and Extended Data Tables 2–3 (PDF pp.17–18) were visually inspected. The [ledger](../data/ice-core-anchor-audit.json) now includes all six Greenland marker rows from Table 2's lower panel, with separate depths and initial calendar estimates for the two cores. These estimates precede the second round of constraints; they must not be mistaken for final NS1-2011 dates. The estimated NEEM depth for the 775 marker is flagged.

The methods explicitly say the Tianchi tephra, second isotope event and pre-536 historical checks were excluded from chronology development. For the second isotope event, the ice increase is assigned to **993 CE**, compared with production between the 993 and 994 Northern Hemisphere growing seasons. The earlier 987-versus-994 comparison therefore must not be read as an exact seven-year correction to every final ice-layer label.

The reported historical check comprises 32 observations, with 24 matching ice events within ±3 years and eight unmatched. The authors report a Monte Carlo significance result, but we have not reproduced their selection or null model. Preserve the misses; neither treat 24 matches as 32 successes nor dismiss all checks as fitted anchors. Distinct observations can provide a useful test even though source authentication and model reproduction remain outstanding.

Table 3 identifies the historical works underlying the 536, 626 and 939 constraints. These are citations and translations inside this paper, not original manuscripts inspected by this investigation. A documentary audit must trace their dating and transmission before using them to adjudicate historical fabrication.

## Supplement recovered: window-count audit

[S108, historical supplement](https://www.whoi.edu/fileserver.do?id=240285&p=244409&pt=2), pp.9–10 and 13, was visually inspected. The [date/rank ledger](../data/ice-historical-validation.json) contains 32 rows: 24 classified Probable and eight Possible by the authors. Individual matched-event assignments remain null; aggregate counts cannot identify which rows missed.

The [denominator calculation](../analysis/ice_validation_windows.py) expands each printed date range by the specified margin, inclusively. Its [results](../analysis/ice-validation-windows-result.json) distinguish summed window years from unique calendar years. For all 32 rows, sums of 229, 165 and 101 reproduce the reported ±3, ±2 and ±1 totals. For the probable subset, 124 and 76 reproduce the ±2 and ±1 totals. At ±3, the sum is **172**, while the supplement reports **155**; the unique-year union is 138, so merely deduplicating overlap does not recover 155 either.

This is an unresolved denominator discrepancy under the explicit counting rule, not a demonstrated correction to the published statistic. Different input selection, implementation or reporting could explain it. Neither the six means nor their significance tests have been reproduced. Repeatedly counted overlapping years are also not independent observations; the simulation must preserve or otherwise account for its sampling structure. Obtain the original ice-event vector and exact sampling code before judging the effect on the result.
