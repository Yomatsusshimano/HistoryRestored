# Willow Wash: the original control has unresolved layer identity

2026-10-09. C005/S326; selected scan audit without independent review.

The [original USGS Open-File Report91-290](https://pubs.usgs.gov/of/1991/0290/report.pdf) contains Reheis, Sarna-Wojcicki, Burbank and Meyer's Willow Wash chapter, printed46-66. Its chapter heading says **west-central California**; the later S325 reference says east-central. PDF pages47/58-64, printed46/57-63, were visually inspected. Other report pages were text-searched only; chemistry tables and original field/laboratory data were not fully audited.

This is one of the sections cited for the [2008 Nomlaki extrapolation estimate](NOMLAKI-AGE-CONTROLS.md). It supplies observations and provisional correlations, but the inspected passages do not recover the particular individual age, weights or error propagation used in2008.

## Evidence to retain together

| Original locator | Reported observation or interpretation | Consequence for reproduction |
| --- | --- | --- |
| Printed46 | Introductory description calls the succession's tephra layers mostly reworked. | Retain this broad warning, while resolving the specific dated candidate's emplacement rather than assigning all layers the same history. |
| Printed57 | FLV-97-WW/21-WW provisionally represent Nomlaki; FLV-96-WW/20-WW represent Putah. The interval between them thins between Ash Butte and Playa. | A single constant accumulation rate cannot be transferred between sections without thickness/contact controls. |
| Printed58 | Black Hole layers FLV-119-WW and117-WW also have Nomlaki-like chemistry. A physically traced FLV-49-WW tie leads authors to recognize multiple similar layers and leave the authentic Nomlaki unresolved. | Recover the later decision selecting a particular layer; compositional resemblance alone is insufficient. |
| Printed58-61, Figures3-6 |66magnetic sampling sites are reported; some short zones have fewer than three sites. Demagnetization examples and a polarity profile are shown. Chron correlations use tephra information. | Local magnetic observations are additional evidence, but their assigned ages are not independent of the tephra-assisted correlation. Raw measurements, sampling and alternative chron matches remain unreplicated. |
| Printed59, Figures4/6 | The lower normal-polarity zone includes a major unconformity, with at least100m of erosion reported. | A continuous age-depth line across that contact requires an explicit missing-time treatment. |
| Printed59 | Approximately500m accumulated over an interpreted3.4-to2.0Ma interval, giving a reported average36cm/kyr. | Arithmetic can be checked; the rate is derived from assumed age assignments, not an independent clock. |
| Printed62 | A later reversed zone requires slow accumulation or unconformities under the proposed correlations; reported rate2-3cm/kyr. Bishop-like ash may have been episodically reworked. | Rates and ash emplacement vary within the succession. Reworking in one named upper interval does not establish reworking of the Nomlaki candidate. |
| Printed62-63 | An older K-Ar biotite estimate4.3±0.4Ma for the capping Rimrock ash conflicts with the authors' younger sequence. The authors also discuss tension between the approximate3.4Ma tuff age and polarity-boundary interpretation. | Retain the conflicting measurements and conditional interpretation. Neither automatically establishes a young historical age or fabrication. |

The [structured ledger](../data/willow-wash-controls.json) separates quoted numerical inputs from audit status. The [arithmetic diagnostic](../analysis/willow_wash_rate_check.py) computes35.714286cm/kyr from500m/1.4million years, consistent with rounding to36. It reproduces a dimensional calculation only. It does not reproduce a measured accumulation history, an individual Nomlaki age or the2008weighted mean. No source-age correction is fitted.

## What changes the next test

The earlier plan to recover an extrapolation recipe must now first establish **which Willow Wash layer was selected and how the1991ambiguity was resolved**. Then recover its measured height, bounding controls, hiatus treatment, reference-timescale version and2008weight/error inputs. The report's provisional correlations and explicit conflicts should not be hidden behind the later precise estimate.

These are disclosed technical uncertainties in an ancient regional chronology. They do not supply a common historical chronology break, a date for southern Bouse fossils or a continuous marine passage. Supporting observations also remain: physical bed tracing, repeated compositional comparisons and demagnetized polarity measurements. A competing reconstruction must explain them along with the conflicts.


Follow-up: [direct Nomlaki dating](NOMLAKI-DIRECT-DATING.md) adds a separate Dry Creek plagioclase analysis; it does not resolve the original Willow Wash layer selection or transfer an age to the southern target.


Follow-up: [chemical crosswalk](NOMLAKI-CHEMICAL-CROSSWALK.md) identifies a later Danville assignment for the light-coloured FLV119fraction and a lower-Nomlaki CaO prose-table discrepancy; neither supplies a whole-bed age transfer.
