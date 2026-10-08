# Touchet magnetic measurements and the duration question

Research draft, 2026-10-08. C008. Retrospective analysis; no independent review.

The recovered measurements provide a test of a constant recorded magnetic direction without first assigning ages to beds. Converting directional change into elapsed years is a separate inference. This audit concerns southern Washington sections, not a reproduction of Steele's Sanpoil study.

## Source and transcription

[Clague and colleagues' supplement, S167](https://doi.org/10.1130/2003023), Tables DR1–DR2, was downloaded from publisher Figshare file 22743938. All three pages were rendered and visually checked. SHA-256: `35ad5758393d737a48b4ef6029d5b387310d1939f2e7fbfb3d33088b62ff94ff`. Publisher metadata licenses it CC BY-NC 4.0. The [numeric transcription](../data/touchet-magnetic-directions.json) credits the authors and retains printed tokens: 33 Touchet, 33 Burlingame and 16 Zillah rows. These are bed summaries, not 82 independently dated floods.

Two zero-labelled rows occur at both Touchet and Zillah. Zillah prints positive 16 among negative labels. Three rows print N=1 despite supplying dispersion statistics. These are source ambiguities, not silently corrected transcription errors. Specimen-level vectors and demagnetization data are absent from this supplement. Table DR2 contains chemical summaries and shard counts, not eruption ages.

## A limited direction test

We selected the printed -5 and 0 rows retrospectively to examine the pre-ash trend discussed by the authors. Both zero rows are retained. This selection does not test every adjacent pair, reproduce the full correlation, or constitute a preregistered prediction.

The [reproduction script](check_touchet_directions.py) converts declination and inclination to unit-vector angular separation. For each pair it compares that angle with the sum of the two printed alpha95 cone radii. This checks whether those two spherical caps overlap; it is not a calibrated joint significance test.

| Section / zero row | Separation, degrees | Sum of radii, degrees | Caps disjoint? |
| --- | ---: | ---: | --- |
| Touchet / 23 | 10.370 | 6.9 | Yes |
| Touchet / 24 | 6.788 | 6.9 | No |
| Burlingame / 11 | 18.760 | 16.3 | Yes |
| Zillah / 02 | 28.208 | 17.6 | Yes |
| Zillah / 03 | 24.613 | 16.6 | Yes |

All five comparisons increase declination and decrease inclination; one retains overlapping caps. The duplicate comparisons share their lower row and are not independent replications. The result challenges a constant-direction model conditional on reliable original-field recording and horizon labels. Orientation bias, depositional alignment, deformation and later recording would need explicit testing before assigning every change to secular variation. Missing such tests does not itself demonstrate any of those alternative mechanisms.

## Where the elapsed years enter

The [main paper, S166](https://www.researchgate.net/publication/232608029_Paleomagnetic_and_tephra_evidence_for_tens_of_Missoula_Floods_in_southern_Washington), pp.248–250, reports demagnetization and an approximate lower-Zillah correlation. Its dating step smooths combined directions and fits external Fish Lake–Mono Lake reference curves. One model assumes equal bed intervals and yields 60 years, with ash at 13,350 radiocarbon BP; another permits changed spacing and gives 14,400 radiocarbon BP for the ash. These are alternative fits, not two direct ash dates.

The proposed decades-long So–Sg interval instead draws on 7 mm of sediment between two Sg layers at Little Boulder Lake, assigned about 40 years through core radiocarbon chronology. The paper reasons that compositionally different So and Sg eruptions probably had at least that separation. We inspected article text, not its figures or the original core assays.

That last transfer is not a demonstrated lower bound: a time between two Sg eruptions does not logically bound the interval from Sg to So without additional eruption-order or sedimentation evidence. Chemical distinction identifies differences; it does not by itself supply years. Nor does similarity among flood beds prove identical recurrence intervals.

Consequently, neither “all beds formed during one short event” nor “every bed is independently dated and separated by decades” follows from this audit. The directional changes remain evidence requiring explanation. The next discriminating work is to recover the reference curves with age models and the Little Boulder Lake core/assay context, then compare explicit recording and timing models. No new minimum duration is assigned here.

Reproduce from the repository root: `python research/check_touchet_directions.py`. Output is a conditional geometrical calculation, not scientific validation.
