# Campo Laborde: testing a chronology revision through chemical fractions

2026-10-08. C022 / S104. Sourced draft; no independent review.

[Politis and colleagues (2019)](https://doi.org/10.1126/sciadv.aau4546) re-examined the Argentine sloth specimen **FCS.CLA.154**, a *Megatherium americanum* metacarpal. We inspected the article's [Europe PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6402857/fullTextXML), including Table 1 and relevant methods. Supplement Tables S3-S4 have now been visually inspected; original laboratory certificates remain uninspected.

The original gelatin determination, AA-71665, is reported as 9,730 +/- 290 radiocarbon BP. Three later XAD-purified hydrolyzate measurements range from 10,570 to 10,690 BP; the authors select **CAMS-171852, 10,655 +/- 35 BP**, citing its larger processed bone mass and smaller uncertainty. The [seven-row table transcription](../data/campo-laborde-assays.json) preserves each fraction, bone/carbon mass, fraction-modern result and available calendar range. The selected published calendar interval is 12,547-12,677 cal BP (95.4%); it is not the same scale as the raw radiocarbon age.

The study also measured fulvic acids separated during purification. Their greater fraction-modern values support the authors' explanation that younger contaminant carbon biased previous results. Those apparent contaminant ages integrate accumulated material; they are not dates of other animals. Different aliquots and fractions of this bone are not independent animals or independently dated floods.

## What this changes in the wider investigation

This is a concrete example of chronology being revised through specimen identification, additional measurements and an explicit chemical mechanism. It gives the preparation audit something testable beyond generic doubts about radiocarbon. A 925-year shift between the original and selected central estimates is a difference in radiocarbon years, not a measured calendar displacement or a correction applicable elsewhere.

It does **not** redetermine Haitian specimens AA-58439, AA-58434 or AA-58431. Their chemistry and burial histories require their own evidence. Preserve their published intervals while flagging missing quality controls. Neither assuming all collagen dates are reliable nor discarding them all follows from Campo Laborde.

This audit also does not verify the paper's hunting-versus-scavenging conclusion. Archaeological association, causes of death, final deposition and population extinction are separate questions. The supplementary control audit below does not yet resolve how very small carbon masses were treated. The paper's choice of the most precise result has been recorded, not independently validated here.

## Supplementary controls and a preparation-label discrepancy

[S105, supplement Tables S3-S4](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6402857/supplementaryFiles), PDF pp.15-16, were rendered and visually checked. The [six control records](../data/campo-controls.json) retain estimates, approximate values and lower bounds as different reference types.

The TIRI whalebone results are 12,695 +/- 40 and 12,795 +/- 35 BP against 12,788 +/- 30. Their differences are about -1.86 and +0.15 combined standard errors, assuming independent uncertainties. This narrow comparison is compatible with the reference at approximately two standard errors; it is not a general validation of every sample or chemistry.

The EL control returns 53,180 +/- 300 and 49,450 +/- 200 BP against a stated >50,000 reference. One central result is below the bound, warranting the laboratory's background interpretation; the bound cannot be treated as an exact age with zero uncertainty. ACT III gives 8,305 +/- 35 and 8,300 +/- 35 BP against approximately 8,350, whose uncertainty is unspecified. The EL and ACT reference values derive from internal-standard communications, not certificates inspected here.

S4 omits control carbon masses, blank-correction details and sample-batch links. Consequently it cannot by itself show that controls matched the 22-410 microgram carbon masses in the specimen table. The required next evidence is the mass-dependent background model and run-level mapping, rather than converting old-bone apparent ages into a blanket pass/fail.

S3 labels AA-71665 as ABA-treated bone, while main Table 1 labels it gelatin. Both labels are retained in the assay record. They may describe different stages or a reporting mismatch; the original preparation worksheet is needed to decide. This discrepancy does not itself invalidate the measured date or explain the redating shift.

## Depositional context and an identified specimen position

The main geological-context text (article p.5) and supplement Figure S5 (PDF p.6) were visually inspected. The authors describe stratum 1 as a former swamp with silty-clay and sandy-mud layers affected by soil formation, resting unconformably on Guerrero Member sediment. The section shows several overlying soil horizons. These observations require a depositional history; they do not by themselves measure its duration or exclude every flood contribution.

Table S1 (header p.9; specimen p.10) places **FCS.CLA.154 in grid I6, north 0.75 m, west 0.98 m, 106.5 cm BGL**, a complete right metacarpal V. The [context record](../data/campo-context.json) preserves those local coordinates without inventing a global position. Figure S5 uses a cm BD axis; its conversion to the table's BGL reference is not established here. No hydraulic elevation has been inferred from either.

The paper reports refitted microflakes FCS.CLA.239/242 separated by about 3 m horizontally and recovered in intervals 1.30-1.35 and 1.20-1.25 m BGL, on opposite sides of the nominal lower stratum-1 boundary. The inspected paragraph does not assign each depth to an individual ID. The authors interpret vertical displacement and discuss soil processes and burrowing. These refits provide a concrete constraint against treating all artifact depths as untouched deposition surfaces. They do not demonstrate long-distance transport, quantify burial duration or identify a catastrophic current.

For the catastrophe comparison, Campo Laborde remains a documented local wetland/archaeological context with reported postdepositional movement. A common-flood proposal must separately explain sediment fabric, soil horizons, spatial refits and specimen ages; it cannot use the corrected sloth age as the age of every enclosing layer. Conversely, acceptance of localized disturbance does not establish complete mixing of the assemblage. Original three-dimensional field data and sediment descriptions are needed to test the extent of displacement.

## Original disclosure before the redating

[S106, Politis and Messineo (2008)](https://doi.org/10.1016/j.quaint.2007.12.003), pp.106-107, already discusses poor preservation and reported laboratory doubts. Table 3 gives AA-71665 **0.8% collagen and 5.3% carbon**. The [six-row quality transcription](../data/campo-original-quality.json) preserves the original column labels; their precise analytical denominators have not been independently established. The earlier authors preferred two other, better-preserved samples while warning that the chronology remained unresolved.

The same table lists FCS.CLA.154 at 98 from level 0; the 2019 supplement gives 106.5 cm BGL. Those differently labeled references cannot be converted or declared contradictory without survey records. The selected pages do not resolve the gelatin/ABA labeling issue.

This documentary sequence matters for the history audit: the earlier publication did not conceal all doubts and later present an unexplained date change. It recorded uncertainty before the subsequent chemical work. That finding does not establish the accuracy of every early measurement or prove any author's intentions. It identifies a public, traceable revision process for this case, with remaining measurement and metadata questions preserved.

## Fraction-modern arithmetic and conditional contamination amounts

Table 1 and methods on article pp.8-9 (combined CONICET PDF pp.9-10) were visually checked. The [reproducible audit](../analysis/campo_fraction_check.py) and [results](../analysis/campo-fraction-check-result.json) retain every printed value. Under the conventional conversion documented by [NOSAMS](https://www2.whoi.edu/site/nosams/calculations-and-reporting-of-results/) (S133), age = -8033 ln(Fm), with first-order uncertainty 8033 SD(Fm)/Fm. These are radiocarbon years, without calendar calibration.

Six central ages agree with the conversion to within five years. **CAMS-171874 does not:** printed Fm 0.3335 +/- 0.0021 gives approximately **8,821 +/- 51 BP**, whereas Table 1 prints **8,670 +/- 80 BP**. Both the visual table and XML contain this pair. The latter age also appears in CAMS-171873's row, whose different Fm does agree approximately. Duplication is a possible reporting explanation, not an established correction. Original certificates must determine which field, if either, is erroneous; this audit does not replace the reported age. Error-column differences are retained separately, without assuming identical reporting/rounding conventions across laboratories.

This is an internal arithmetic check, not an independent date comparison or a significance test. The selected collagen determination CAMS-171852 is not the discrepant fulvic-acid row. The discrepancy therefore does not by itself overturn the selected specimen chronology. The methods also explicitly describe AA-71665 as ABA-treated, reinforcing the previously recorded disagreement with its Table 1 gelatin label.

For an illustrative two-component carbon balance, let the original endmember equal CAMS-171852's Fm=0.2654 and the mixture equal AA-71665's Fm=0.298. Then f=(Fm_mixture-Fm_original)/(Fm_contaminant-Fm_original).

| Assumed contaminant endmember | Required share of mixture carbon, central values |
| --- | ---: |
| Illustrative Fm=1 | 4.44% |
| CAMS-171873, Fm=0.3397 | 43.88% |
| CAMS-171875, Fm=0.2983 | 99.09% |
| CAMS-171874, Fm=0.3335 | 47.87% |

These amounts are **not measured contamination fractions**. The original aliquot's contaminants were not characterized by these later extractions; comparable normalization and linear mixing are assumptions. We have not propagated uncertainty, corrected isotope fractionation in mixtures, or reproduced mass-dependent blank corrections. In particular, the near-99% scenario is sensitive to uncertain endmembers and is not a precise estimate. Carbon masses dated are not complete extraction yields and cannot independently verify the balance.

The calculation shows that contamination composition matters as well as quantity. It neither verifies nor rules out the authors' chemical explanation. Required next evidence is original fraction/blank worksheets and yield balances linking the relevant aliquots. No correction is transferred to Haitian sloth dates or to a common catastrophe timeline. Three analytic software tests check conversion, mixture endpoints/interior and unidentifiable endmembers; they do not validate the sample chemistry.
