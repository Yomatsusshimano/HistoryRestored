# Melamchi preprint budget and uncertainty wording audit

2026-10-11. S449–S450. Sourced draft; no independent archive review.

Recovered [author preprint v1](https://doi.org/10.21203/rs.3.rs-2766739/v1), posted6April2023, and its [attached methods DOCX](https://assets-eu.researchsquare.com/files/rs-2766739/v1/ec0dbd724577f3d974cba019.docx). PDF1/5/6/14 were visually inspected. Selected supplement paragraphs and table cells were read from original OOXML; DOCX layout and equations were not visually reviewed. This is an earlier version, not a substitute for the final publication's missing uncertainty workbook. [Structured audit](../data/melamchi-preprint-budget-audit.json).

## Three unreconciled budget representations

| Location | Erosion, million m³ | Deposition, million m³ |
| --- | ---: | ---: |
| Preprint prose, PDF6 | 83.24 | 23.24 |
| Preprint Figure4, PDF14 | 83.54 | 22.73 |
| Sum of numeric TableS4 entries | 83.733139 | 22.833636 |

The sums transcribe source cells and add them; entries called negligible remain unquantified rather than being assigned zero. They are not corrected catchment totals. Different representations need version/scope reconciliation. None was selected as the true budget, and none replaces our null deposit-volume result.

## Uncertainty labels need clarification

The supplement describes surrounding stable regions, approximately350m radius, and a standard-deviation-based estimate with area error assumed absent. A variant restricts values to the10th–90th quantiles. These author choices require evaluation; trimmed distributions do not automatically establish a lower confidence bound, and a stated upper estimate is not a proven error bound.

Original TableS2 labels columns as mean and median absolute deviation, yet includes negative values: whole-catchment mean absolute deviation−0.11; A4 entries−11.2/−0.477; A7 entries−4.04/−0.887. A true absolute-deviation statistic cannot be negative. This establishes an inconsistency between labels and cells, **not what statistic was actually calculated**. We did not silently take absolute values, reinterpret the columns, infer intentional manipulation, or assume the final publication retains the problem.

The methods text defines active-channel margins by absence of vegetation. A mapped active channel is therefore not automatically a boundary of all deposited material. This helps explain why our channel overlay needs additional classification before volume estimation; it does not independently validate that overlay or identify every unmasked corridor.

## Effect on the investigation

The source supplement narrows what must be retrieved next: final-version uncertainty tables and definitions, actual stable-area masks, registration residuals, exact budget polygons and a version comparison. OOXML equations are stored as mathematical structures; flattened text is insufficient to reconstruct them, so no formula was adopted from that extraction. Numeric additions can be checked independently using the ledger; geological estimates still require original masks, data and uncertainty reproduction.

The current local height comparisons remain exploratory. These draft inconsistencies challenge using the preliminary numbers uncritically; they do not erase the evidence for a local flood, prove fabricated history, or establish a worldwide event.31core case drafts/450sources; all twenty objectives remain active.
