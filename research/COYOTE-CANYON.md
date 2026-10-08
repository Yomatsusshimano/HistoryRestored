# Coyote Canyon: animal death, sediment burial and dating resolution

2026-10-08. C015 / S32, S99. Sourced draft; no independent review.

Last and Rittenour (2021), *Chronology of Missoula Flood Deposits at the Coyote Canyon Mammoth Site, Washington State, USA*, [DOI](https://doi.org/10.3390/quat4030020). Publisher PDF access is now resolved: [preserved CC BY 4.0 original](../sources/originals/coyote/quat4030020.pdf), with checksum in S32. Figures 4-7 and Tables 2-4 were rendered and visually inspected (pp.6-8,10). This supersedes the earlier text-only access limit; it is not independent field validation.

## Distinct objects and contexts

Seven OSL determinations date quartz-bearing sediment: two flood samples and two overlying loess samples at the mammoth site, plus three flood samples at the nearby camel site. The [transcription](../data/coyote-osl.json) retains field and laboratory IDs, depth, accepted/analyzed aliquot counts and the reported two-sigma age uncertainty. None is a direct animal-death measurement.

The paper reports a left-humerus radiocarbon result of about 17.4 ± 0.2 cal ka BP, citing earlier work and grouping laboratory identifiers as Wk-32731&2 in Table 1. This aggregate is not entered as two invented individual measurements. It also reports a Camelops metatarsal age of 25.2 ± 0.2 cal ka BP, older than the nearby flood sediment, supporting its interpretation of reworking. Original bone assay reports and preparation controls remain uninspected.

The mammoth's death in a flood and subsequent carcass deposition are the authors' interpretation of dating and context. Agreement of a bone age and sediment age does not by itself establish drowning. Conversely, an older fossil in younger sediment is not automatically evidence that its biological age is wrong. Taphonomy, articulation, abrasion and stratigraphic association must discriminate these possibilities.

## What the OSL measurements resolve

The [calculation](../analysis/coyote_intervals.py) constructs each reported age ± uncertainty interval and intersects the **five flood-sediment** intervals. Their common range is **18.32–19.05 ka**. Loess samples are excluded by depositional context, not because of their values. This retrospective descriptive check means these broad OSL intervals alone cannot distinguish one common age from multiple nearby ages.

It does **not** mean one event has been demonstrated, or that the common range has 95% joint probability. Marginal two-sigma intervals do not supply a joint distribution; dose-rate assumptions and analytical methods create dependence. The 20.87 versus 16.28 ka central estimates differ by 4.59 kyr, but that subtraction is not a proven minimum duration of flooding. Distinct graded beds, intervening surfaces and preservation must be examined separately. No radiocarbon age is folded into this OSL intersection; their time reference and calibration must first be reconciled.

## Method dependencies and remaining tests

The authors used small-aliquot quartz measurements and a Minimum Age Model for partial bleaching. Table 3 substitutes 9.8% moisture in dose calculations for five samples whose measured moisture was lower; CCMS-1 uses 9.8%, CCMS-2 uses 6.9%. These are reported modeling choices requiring sensitivity analysis, not proof of error. Raw dose distributions, rejection reasons and dose-rate histories have not been reproduced here.

Retrieve original field logs and laboratory certificates; audit bleaching, aliquot selection and moisture corrections. Test death and sediment deposition as separate hypotheses. The named camel site is in Washington; it is not the older Arctic camel locality. This case provides a regional fossil–flood comparison without demonstrating a single global wildlife upheaval.

## Excavation geometry and event counting: facsimile audit

Figure 4 shows excavation floors at different heights. Figure 5 projects bones and erratics from those levels onto one plan; proximity on that plan is not proof of one depositional surface. Its legend also distinguishes in-situ and ex-situ mapped bones. Figure 6 projects background/foreground walls onto the section and marks uncertain contacts. It places paleosol, loess and slope wash above the flood sequence; the soil horizon is not a demonstrated hiatus between every flood bed.

The section labels seven mammoth-site beds (A-G); Figure 7 labels thirteen camel-site beds (a-m), along with covered areas, clastic dikes and lower/upper paleosols. These are published interpretations, not thirteen independently dated floods. Section 2.1 explicitly warns that deformation obscures contacts and slope wash during waning flow can create repeat beds. Thus the evidence supports a stratified, modified deposit, while an exact count of separate floods requires contact-level field evidence. Neither the OSL interval overlap nor the drawn bed count alone resolves this.

Table 2 supplies sample coordinates and NAVD 88 elevations, now transcribed with horizontal datum left unknown. Table 4 values agree with the existing age/aliquot transcription. Table 3 corrects our earlier CCCS-OSL-6 measured moisture transcription from 1.0% to 1.9%; its modeled moisture remains 9.8%, so no published age is recalculated here. The Figure 6 vertical axis distinguishes local grid elevations from parenthesized NAVD 88 elevations; these must not be interchanged in a hydraulic reconstruction.

## Earlier camel measurements recovered

[S99, Barton, Mara and Adams (2019)](https://gsa.confex.com/gsa/2019CD/webprogram/Paper329689.html) reports three samples from the same metatarsal. [Structured transcription](../data/coyote-camel-assays.json):

| Printed identifier | Radiocarbon BP | Printed uncertainty |
| --- | ---: | ---: |
| D-AMS 016465 | 20,720 | 75 |
| Beta 45508 | 21,010 | 70 |
| NOSAMS CCSH 03 | 21,100 | 270 |

The reported combination is 20,890 +/- 51 BP, calibrated to 25,020-25,450 cal BP at 95.4%. The abstract names collagen extraction, gelatinization, filtration and OxCal 4.3. Laboratory certificates, quality metrics, calibration curve and pooling diagnostics are absent. Preserve the printed identifiers pending verification. These are replicate samples of one animal, not three independently dated burial events. The mammoth's original 2012 assay report remains unrecovered.
