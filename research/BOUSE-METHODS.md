# Hart Mine Wash: measurements, timing and boundary exceptions

Research draft, 2026-10-08. S184/S185; no independent review.

The Bright et al. study supports testing a local hydrochemical transition. Its proposed 3-300-year duration is conditional on assumed sedimentation rates, and its supplementary table contains exceptions to two categorical descriptions in the article. Neither observation establishes a historical California strait or a worldwide catastrophe.

## What was measured

[S184, Bright et al. (2016)](https://pages.uoregon.edu/rdorsey/Downloads/BrightEtal2016.pdf), printed pp.87-88, gives the Hart Mine Wash location as 33.2907 N, 114.6364 W. The coordinate datum is unspecified in the inspected passage. This is an explicitly reported locality, not a position inferred from its regional map. It is not the location of the younger Cahuilla sections.

The authors counted microfauna in the >120 micrometre fraction, counted an ostracode carapace as two valves, and examined concentrated aliquots of the 45-120 micrometre fraction for relative foraminifer abundance. These columns have different denominators and must not be added as interchangeable counts. The <45 micrometre sediment fraction and selected ostracode valves were analyzed separately. Reported analytical precision is 0.1 per mil for oxygen and 0.08 per mil for carbon (one sigma), referenced to VPDB using NBS-18/19 standards. That precision does not include uncertainty in ecological interpretation, sample representativeness or age.

Their interpretation assumes fine carbonate formed in upper water and ostracode valves formed in place at the bottom. They did not identify their foraminifers taxonomically: the assignment of 99% of biserial forms to Streptochilus comes from McDougall and Miranda Martinez (2014). Thus this identity is a shared input, not a new independent identification. The authors also acknowledge that they did not analyze the subsurface Blythe material used in the broader marine interpretation (p.87).

## Supplement recovered and discrepancies retained

[S185, publisher supplement entry 207](https://www.sepm.org/supplemental-materials/207/view), provides an [Excel download](https://www.sepm.org/supplemental-materials/207/download). Its three sheets are READ ME, Supplement 1 and Supplement 2. The first data sheet contains 24 sample rows, HM45-HM64 with additional HM90/HM89/HM88/HM87 in stratigraphic order. The second has 53 ostracode isotope rows, with repeated sample names and no separate specimen identifiers. These are reported results, not newly inspected specimens. The workbook contains no formulas.

Selected factual cells and their exact locators are retained in [the measurement record](../data/bouse-methods.json). The downloaded workbook remains unchanged; its hash identifies the inspected version. A complete raw-laboratory or specimen audit has not been performed.

| Comparison | Article, p.88 | Supplement 1 | Consequence |
| --- | --- | --- | --- |
| Fossils in the distinctive clay layer (DCL) | Describes it as devoid of fossils | HM52, row 13: spiraled foraminifers 0.2 tests/g in O13; finer-fraction spiraled relative entry 1 in R13 | Strict absence is inconsistent with the table. Identification, contamination, rounding or other explanations remain untested |
| First Candona | Groups its abrupt appearance with continental ostracodes above the DCL | HM51 pre-DCL, row 12: juvenile Candona 0.1 valves/g in K12; HM53 above, K14 = 0.5 and J14 = 0.1 | An increase may remain, but literal first occurrence above the layer is not supported by this table |
| DCL position | Approximately 111 m above sea level | HM52 B13 = 111.2 m | Compatible with rounded prose; no discrepancy in absolute dating follows |

Preserve those small nonzero entries. Do not round them to absence or call them proof that the overall environmental transition failed. Conversely, do not explain them away without specimen and processing evidence. The distinction matters if a reconstruction requires an instantaneous ecological replacement.

## Duration is an assumption-dependent estimate

The reported DCL thickness is 3 cm (p.88). On p.89 the authors explicitly leave its duration unknown, then use sedimentation rates of 0.1-10 mm/year, attributed to Cohen (2003), to suggest 3-300 years. The arithmetic is:

`duration = thickness / rate = 30 mm / (10 to 0.1 mm/year) = 3 to 300 years`.

This calculation has no direct dates bracketing the layer and supplies no probability distribution. It is not a measured confidence interval or an independently verified minimum duration. The applicability of those rates to this particular clay layer, including a proposed catastrophic process, remains to be established. Reproducing the division does not validate the rate assumptions. Neither a one-year episode nor a centuries-long episode is settled by this arithmetic alone.

The article's 4.2-6.4 Ma interval for Pacific isotope comparison material (Fig.6 and p.89) dates the selected analog material, not a new assay of HM52. Figure 7 sketches competing lake-spillover and estuary-flood sequences; it is not a fitted hydraulic simulation. The Bonneville analogy does not synchronize the two events.

## Next discriminating work

The [sample/genus isotope comparison](BOUSE-ISOTOPES.md) now reproduces all 53 reported rows and preserves their within-sample spread. Next reconcile HM51/HM52 entries with the original counting sheets, specimen images and sample processing. Obtain the marine study's full identifications and subsurface context, original isotope aliquot/specimen records, and independent age controls for this section. Separately define a map-derived channel route and test its continuity. No geological-to-historical date conversion is justified by the present audit.
