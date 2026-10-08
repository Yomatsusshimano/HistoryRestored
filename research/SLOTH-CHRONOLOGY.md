# Haitian sloth dating: specimen ages versus event ages

Research draft, 2026-10-08 (America/New_York). C011/S22; no independent review.

## Source and extracted evidence

[Steadman and colleagues (2005)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1187974/) report nine AMS bone dates in Table 4, from Haiti and Ile de la Tortue. The HTML table, caption, Figure 2 caption and relevant chronology discussion were inspected. The supplementary link returned a browser-check page; laboratory preparation details were not audited. No physical specimens or original lab worksheets were examined.

The complete nine-row Table 4 extraction is in [dating records](../data/dating-records.json), identified by laboratory and museum numbers. Radiocarbon ages and published calendar intervals remain separate; calendar ranges are reported at 95% confidence. Disjoint intervals remain disjoint. AA-58436 is a lower bound (>14,200 radiocarbon years BP), not an exact age; two rows lack calendar ranges. The publication uses OxCal 3.9. No recalibration was performed here.

The authors distinguish last appearances from actual extinction and state that their AMS dates alone do not demonstrate human causation. Their continental comparison compiles earlier studies; it is not independently re-audited here. This audit concerns the 2005 measurements, not a claim that the paper's broader archaeology or taxonomy represents current consensus.

## Tests this makes possible

The proposed catastrophe contains several separable temporal claims:

| Proposed claim | Required test | What these records supply |
| --- | --- | --- |
| These animals died in one short episode | Direct biological ages consistent with one declared window, after preparation and calibration audit | Identified bone samples with reported ages; no fitted common-death model |
| Older remains were moved together later | A separately dated depositional horizon, transport indicators and provenance connecting the remains | No verified common depositional horizon in this extraction |
| A regional population became extinct at a specified time | Sufficient geographic and temporal sampling, preservation/detection assessment and an extinction model | A purposive set of dated specimens; no census of final survivors |
| Geographic upheaval created the observed range | Dated terrain changes, feasible routes and habitat evidence linked to identified populations | Site names and reported elevations; no reconstructed corridor |

An older bone incorporated into a younger deposit would not require its biological age to equal the deposit age. That possibility must be supported with stratigraphy and taphonomy, rather than added solely to rescue a failed date match. Conversely, uncertainty about exact extinction cannot erase positive evidence of an animal living at the time represented by a reliable direct date.

Different species, localities and dated elements remain separate records. Multiple bones under one laboratory identifier are not automatically independent animals or independent measurements. All nine rows share a publication and laboratory context; copying them into this inventory does not create replication. Unknown coordinates remain null; a site name or elevation is insufficient for a precise plotted point.

## Executed interval comparison

The [calculator](../analysis/sloth_intervals.py) reads the structured rows and writes a [result file](../analysis/sloth-intervals-result.json), including a canonical input hash. Run `python analysis/sloth_intervals.py`; add `--plot` with matplotlib installed to regenerate the figure. The published figure used matplotlib 3.11.2. The numerical calculation itself uses only Python's standard library.

![Separate published calendar intervals for seven sloth bone samples](../analysis/sloth-intervals.png)

This is a retrospective descriptive check of a **simultaneous biological-death interpretation for these selected specimens**. It is not a test of every possible upheaval, and the sample set was not selected prospectively. Seven rows have published calendar intervals; AA-58436 and AA-58438 are excluded because they do not. Their radiocarbon dates/bounds cannot be substituted onto this calendar axis.

| Included set | Common intersection | Shortest window touching every sample's interval set |
| --- | --- | --- |
| All seven calibrated rows | Empty | 5,910 calendar years; endpoint witness 5,260–11,170 cal BP |
| Six calibrated *Neocnus comes* rows | Empty | 3,870 calendar years; endpoint witness 5,260–9,130 cal BP |

The first minimum has a simple independent arithmetic check: AA-58439's oldest allowed endpoint in this extraction is 5,260, while AA-58434's youngest is 11,170. Their gap is 5,910 years. A window with those endpoints also touches each intervening sample's set, so the lower bound is attained. For the same-species subset, AA-58431 supplies the 9,130 endpoint instead. Disjoint ranges are not filled in during intersection calculations.

**These numbers are not 95% lower confidence bounds on event duration.** Individually reported 95% sets have omitted probability tails and are not a joint probability model. The calculation uses neither likelihoods nor shared calibration/laboratory errors. It establishes only that an instantaneous common death cannot sit inside all the reported sets as transcribed. It does not infer the probability of simultaneous death, date a final extinction, or exclude later movement of older remains.

The result challenges treating this selected collection as a contemporaneous death assemblage. A single later depositional event remains a different proposition requiring its own stratigraphic evidence; no such common horizon has been demonstrated here. Preparation audits, current calibration and later redating could change the inputs and must be recorded as revisions rather than silently substituted.

## Next work

### Later evidence from one of the same sites

[Cooke and Crowley (2022), S36](https://doi.org/10.1177/09596836221101279) reports eight new rodent dates from Trouing Jérémie #5, the site of sloth AA-58431. These are different specimens, not sloth redeterminations. The [eight-row transcription](../data/haiti-rodent-dates.json) retains museum and UCIAMS identifiers, atomic C:N, radiocarbon results and the published two-sigma calendar ranges. Relevant methods/context were read in the [NSF-hosted article](https://par.nsf.gov/servlets/purl/10336169), and Table 2 was visually checked.

The methods describe acid demineralization, base treatment, gelatinization, filtration and collagen-quality assessment. Atomic C:N values are 3.3–3.6; individual collagen yields are not tabulated here and stay unknown. Calibration used IntCal20 and Calib 8.2. This documents reported procedures, not an independent contamination test.

The table's oldest range is 10,806–11,184 cal BP for UF 293822; the youngest is 289–429 cal BP for UF 293847. Their separation supports a collection containing biological material of different ages. It does not, by itself, prove uninterrupted sediment accumulation or date each specimen's entry into the sinkhole. The authors interpret prolonged accumulation; excavation positions and taphonomy are needed to discriminate that from later mixing.

Table 2 labels one summary column “Mean ± 1σ,” but its footnote describes rounding two-sigma ranges to construct that summary. Preserve the labeling discrepancy; do not treat the half-range as a Gaussian standard deviation or replace the original range with it. Calibration probability structure was not reproduced.

No later remeasurement of AA-58439, AA-58434 or AA-58431 was established by this limited search. Their original preparation audit remains open. These new measurements add site context without independently verifying the earlier sloth assays.

### Remaining checks

Retrieve preparation protocols, collagen-quality measures, original determinations and excavation context. Check later redating and taxonomic revisions by specimen identifier. Recalibrate only with an explicitly named curve, software/version and justified reservoir assumptions; retain the original published results beside any new calculation.

Extend coverage to directly dated continental material and additional island samples before estimating extinction timing. Keep tests of death, deposition, migration and extinction distinct. No global event, cause of extinction, or historical rewriting follows from this extraction.
