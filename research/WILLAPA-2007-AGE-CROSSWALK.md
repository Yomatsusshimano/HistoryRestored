# Willapa age provenance: KI-11 and conflicting luminescence results

2026-10-09. S280's [exact dataset13384 catalog](https://cmgds.marine.usgs.gov/services/cmgds-dataset.php?id=13384) is available here only through indexed excerpts. Its public-file locator is DOI10.3133/ofr0246, the previously identified2002 report. This is not a newly acquired independent core-log file. The report remains403; no specimen custody or core geometry is authenticated.

S281 is Morton and colleagues'2007 paper, DOI10.1016/j.margeo.2007.07.008, verified against [USGS catalog70031632](https://pubs.usgs.gov/publication/70031632). Selected [author-uploaded exposed text](https://www.researchgate.net/publication/248461127_Forcing_of_large-scale_cycles_of_coastal_change_at_the_entrance_to_Willapa_Bay_Washington) was inspected. The PDF and figure/table images were not acquired; direct author-page retrieval returned403 and the PDF-link tool returned an error. The new [input ledger](../data/willapa-2007-age-inputs.json) is explicitly text-only, with unresolved glyphs and no invented laboratory IDs. Methods links the analysis to the2002 field report, so the publication is not an independent field replication.

## KI-11 crosswalk

| Field |2007 Table1, exposed text, printed35|2018 Table3, inspected PDF19, printed127|
| --- | --- | --- |
|Site/depth|KI-11,500cm|KI11/pf,5.0m|
|Material/method|Shell/AMS|Wood/AMS|
|Printed age and error|1590 ±40|1590 ±40|
|Age label|Calibrated age, yr BP|Conventional yr BP ±1σ|
|Calibrated output|No separate range/median|1392–1558 BP; median1474 BP|
|Elevation|−3.70m MLLW, Toke Point|−4.7m MTL|
|Laboratory ID|Not supplied in inspected table|Beta133387|

Matching depth and printed age supports a provisional record relationship, not authenticated specimen identity. Material and age-label conflicts remain unresolved. The one-metre elevation difference uses different tidal references; it is not measured physical movement or an authenticated datum conversion. Recalibrating the2007 number as raw radiocarbon, or treating its heading as authoritative calendar dating, would require choosing between unresolved accounts. The2018 scan was rechecked and confirms its wood entry.

## Literal luminescence comparisons

|Site/depth|IRSL age ± printed error, yr BP|TL age ± printed error, yr BP|TL minus IRSL, years|
| --- | ---: | ---: | ---: |
|KI-12,90cm|NA|17800 ±4500|—|
|KI-13,65cm|1160 ±140|7060 ±740|5900|
|KI-13,70cm|1030 ±160|5760 ±670|4730|
|TS-4,55cm|440 ±210|5680 ±950|5240|
|TS-4,60cm|3460 ±280|15960 ±1540|12500|

These Table2 values are text transcriptions, with errors left in their printed convention. At KI-13 the deeper IRSL value is130years younger. At TS-4, five centimetres separates IRSL values differing by3020years. Neither comparison establishes a sedimentation duration or a significance level. The [executed arithmetic](../analysis/willapa_2007_age_crosswalk.py) and [result ledger](../data/willapa-2007-age-crosswalk.json) impose no Gaussian model or independent-error assumption.

All six Table1 radiocarbon rows are retained. TS-3's exposed token `b 50` is not normalized into an inequality; its numerical age and inequality interpretation stay null until the scan is recovered. The KI-12 table says wood while nearby prose says charcoal, another source-level distinction to resolve.

## Mechanism and dating limits

The authors discuss incomplete luminescence resetting and composition effects, and acknowledge poor geometric correspondence between dated scarps and spits. They favor earthquake-linked sediment supply while retaining channel-recycling and storm alternatives. Age coincidence alone therefore does not authenticate a transport link or instantaneous deposition. None of these text-only observations establishes a worldwide flood or chronology break.

The next discriminating records are the2002 AppendixB logs,2007 original tables and laboratory certificates: particularly Beta133387's material, conventional result and calibration lineage. Exact sample-to-core association, bleaching/fading procedures, tidal surveys and correlated contacts are needed before event or accumulation modeling. Preserve all methods' results rather than selecting whichever age supports a preferred event. All twenty objectives remain active; no independent scientific review is claimed.
