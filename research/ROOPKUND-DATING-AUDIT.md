# Roopkund: a test of simultaneous mortality

Research draft, 2026-10-11 (America/New_York). C031/R006; S407–S409. No independent review of this archive's analysis. [Sample and retrieval ledger](../data/roopkund-dating-audit.json), [reproducible interval check](../scripts/roopkund_interval_check.py).

## Retrieval and scope

The Reddit lake identification remains provisional: another direct thread request failed, and its original linked media were not authenticated. This follow-up tests Roopkund as the candidate site, without claiming that every circulating photograph is matched.

The [2019 original study](https://www.nature.com/articles/s41467-019-11357-9), by Éadaoin Harney and colleagues, was inspected in selected rendered HTML sections: results, dating methods and discussion. A native HTML download delivered a short page rather than a verified article copy, so no article-content hash is claimed. The publisher-advertised [Supplementary Data 4](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-019-11357-9/MediaObjects/41467_2019_11357_MOESM8_ESM.xlsx) was acquired normally after the web tool could not handle its content type. Sheet1 headers and all 45 data rows were read; 37 contain dating results, eight contain missing dating markers. Selected fields are transcribed with cell-row locators; markers are not zero ages. The workbook is unchanged.

The [37-page supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-019-11357-9/MediaObjects/41467_2019_11357_MOESM1_ESM.pdf) was acquired; PDF2/5/6 were rendered and visually inspected. Its calibration figure shows multimodal distributions. The earlier five-sample table has separate identifiers, with no established join to the genetically studied individuals. It is not added to the 37-record calculation.

## Dates and the hypothesis being tested

The study reports AMS dating of bone collagen from the same powder stocks used for genetic analysis, calibrated with OxCal4.3 and IntCal13; its figure specifies4.3.2. I3401 lacked sufficient powder and remains undated. Genetic similarity is not a dated travel itinerary or proof of birthplace. The authors discuss a disturbed assemblage and possible causes without identifying every person's death mechanism.

The retrospective test here is **R-M: all 37 dated individuals died within a specified common duration**, conditional on published bone-collagen ages serving as mortality proxies. Bone collagen reflects tissue formation rather than an exact death instant; turnover and systematic age offsets are not modeled here. This is an operational test, not a claim attributed verbatim to a Reddit participant or a prospective prediction. R-D, a later common redistribution of older remains, is a different hypothesis requiring dated depositional context.

The workbook labels its calendar columns as mean and 2σ low/high. Treat these as published outer bounds, not continuous uniform probabilities. Preserve raw radiocarbon BP ages separately from calibrated CE bounds. The worksheet's ± age column has no explicit confidence label in the inspected header; the ledger leaves that uncertainty convention unnormalized. No new calibration, reservoir correction or specimen-level quality validation was performed.

## Reproducible necessary-condition comparison

For outer intervals [lowᵢ, highᵢ], an event window of duration D can intersect every interval only if **max(lowᵢ) − min(highᵢ) ≤ D**. This tests permissive outer envelopes: actual calibration distributions may contain excluded gaps. Passing cannot establish simultaneity, and a mismatch is not a joint-confidence rejection probability.

| Selected set | Dated rows | Latest lower bound | Earliest upper bound | Minimum permissive span |
| --- | ---: | --- | --- | ---: |
| All | 37 | 1706 CE, I2870/I3404 | 769 CE, I6943 | 937 years |
| A | 23 | 894 CE, I6941 | 769 CE, I6943 | 125 years |
| B and C | 14 | 1706 CE, I2870/I3404 | 1915 CE, I2870/I3404 | 0 years; outer intersection 1706–1915 CE |

For all 37, the reported bone-age outer bounds do not fit a common 0-, 1-, 10- or 100-year window. Even A fails those duration choices. Interpreting this as a mortality test requires the proxy assumption above; the spans are not measured durations of dying. The B/C outer-envelope overlap is compatible with a shared date but cannot prove it; narrower disjoint calibrated ranges must be checked. These computations concern this sample, not every bone at the lake or every catastrophe proposition.

## What could change the assessment

Audit individual laboratory identifiers, preservation/pretreatment quality, reservoir effects and full calibrated probability components; reproduce dating with a declared current calibration model and retain the original version. Recover collection histories, skeletal associations, in-place sediment units and independent deposit dates before evaluating R-D. Trauma observations from a different bone set require an explicit specimen join before assigning a cause to a dated individual. Original travel or pilgrimage records could test identity accounts; inferred ancestry alone cannot name erased people.

This is adverse evidence for simultaneous mortality within the tested durations. It establishes neither a particular local death mechanism nor a dated mud-flood layer. No common global event, lost civilization or historical-rewriting mechanism follows. All twenty objectives remain active.
