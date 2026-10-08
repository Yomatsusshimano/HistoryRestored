# RD-16: the underlying basalt citation recovered

2026-10-08. Three compilation entries, not three independent laboratory dates.

S206, [Reynolds et al.1986, Bulletin197, first PDF segment](https://data.azgs.arizona.edu/api/v1/collections/AGSB-1552426601054-677/bulletin_197_txt_1.pdf), printed24/PDF30, entry219, identifies the previously unresolved9.60 ±0.60 Ma control as **RD-16**, K-Ar whole-rock basalt in the western Buckskin Mountains, Black Peak quadrangle. The entry reports it below the Bouse base and labels Osborne Wash Formation with a question mark. It cites Fugro1975 and says the date was reported in Calzia and Morton1980. This identifies the compilation's sample; the original analysis and bed contact remain uninspected.

S205, [Schell and Wilson, Regional neotectonic analysis of the Sonoran Desert](https://pubs.usgs.gov/of/1982/0057/report.pdf), printed48/PDF49, entry417, also identifies **RD-16**, but reports9.3 ±0.6 Ma. Its dating-method cell is blank. Reference24, text-read on printed53/PDF54, points to Fugro1976, Sundesert PSAR Appendix2.5J. That year differs from S206's Fugro1975 citation; neither version is silently normalized.

| Field | S205 entry417 | S206 entry219 |
| --- | --- | --- |
| Reported age (Ma) | 9.3 ±0.6 | 9.60 ±0.60 |
| Latitude as printed | 34°13.50′ | 34°13.32′ |
| Longitude as printed | 114°05.60′ | 114°05.63′ |
| Material/method | Basalt; method blank | Basalt; K-Ar whole rock |
| Stratigraphic description | Buckskin Mountains | Below Bouse base; Osborne Wash Formation (?) |

[Structured transcriptions](../data/rd16-compilation-records.json) retain both entries. Datum, location precision, error convention and raw K/Ar measurements remain unknown. These positions should not be treated as precise modern survey coordinates or averaged.

S206 printed2/PDF8 explicitly describes recalculating ages using updated decay constants, or conversion tables when analytical data were absent, except where original constants were unknown. This provides a plausible explanation to test for the age change. It does **not** document which procedure was applied to RD-16: entry219 lacks laboratory, constant and analytical fields shown for many neighboring entries. We have not reproduced its9.60 Ma result. An age difference with a disclosed general recalculation policy is not evidence of deliberate historical fabrication.

The sample identifier, rock and region support a cross-compilation link. The coordinate and reference-year differences still require original report/version checks. Neither entry is the9.2 Ma sanidine tuff or the16.8 Ma basalt recovered in S203. Nor does the reported underlying position date Bouse deposition directly.

Inspection: S205 p.48 and S206 pp.2/24 visually checked; S205 reference24 text-read. S205 PDF SHA256 `3c24f2381a3a44bc6ef0b78cd8e721d05a8ae95e8d78ef2a71873383cfb9236f`; S206 first50-page segment SHA256 `8c793e92aaffdc51b3864ffa905a8bdf995185080ad559562273f13a90ef2a0d`. S205 cover reads1981 while report identifier is82-57. No entire-compilation review claimed.

Next retrieve Calzia and Morton1980 and the original RD-16 analytical page, reconcile the1975/1976 editions and coordinate changes, then verify the mapped contact. The accessible AZGS segment resolves the earlier compilation-access gap; original laboratory recovery remains pending.

## Reported-versus-recalculated pair recovered

S207, [Calzia and Morton1980, OFR80-1303](https://pubs.usgs.gov/of/1980/1303/plate-1.pdf), Table1, map entry **K41-4**, explicitly lists RD-16 as whole-rock basalt at the Bouse base with two labeled columns: **reported9.3 ±0.6 Ma; recalculated9.6 ±0.6 Ma**. The age change is now documented for this sample. The earlier discussion above records the uncertainty before this retrieval; the remaining gap is reproduction from original inputs, not whether the source labels a recalculation.

The sheet's Discussion attributes recalculated ages to the updated constants of Steiger and Jager1977. It says most K-Ar ages were recalculated from original-author isotopic data, naming selected exceptions converted with correction factors. The Fugro exception named there is **RD-1**, not RD-16; do not transfer its method to RD-16. Raw RD-16 isotope measurements are absent from this table, so no independent recalculation is claimed.

K41-4 gives34°13′19″N,114°05′38″W. Converting seconds to fractional minutes yields13.316666…′ and5.633333…′, which round to S206's13.32′ and5.63′. Thus those two coordinate representations agree at the printed rounding. S205's13.50′/5.60′ remains different. This arithmetic does not establish survey precision, datum or the actual collection point.

The sheet's bibliography explicitly identifies Fugro1975 as the Parker Valley alternate-site investigation, section2.5, pp.53–63. It strengthens that retrieval target beyond a generic matching author/year. S205's1976 Appendix2.5J citation may involve republication or another compilation pathway; that relationship is still unverified. None of these derivative entries counts as independent dating confirmation.

Access: single-sheet PDF had no extractable text. Enlarged table, Discussion and bibliography were visually checked; SHA256 `850174baf1c4f6a3d163dd473217feb268a3a3d174e93ff49b51b55f57d99583`. Next original RD-16 analytical inputs and field contact, then reconcile S205's coordinate/reference variant. The numerical discrepancy is explained at the published-document level without establishing the full depositional chronology.
