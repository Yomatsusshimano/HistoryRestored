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

## Conditional pooling check

The [reproducible calculation](../analysis/coyote_camel_pooling.py) and [result](../analysis/coyote-camel-pooling-result.json) use the error-weighted radiocarbon-age equations documented for [OxCal R_Combine (S100)](https://c14.arch.ox.ac.uk/oxcalhelp/hlp_analysis_inform.html). This is a retrospective check in BP age space, not an OxCal run or calendar recalibration. We conditionally treat the printed errors as independent Gaussian one-sigma standard errors around one true radiocarbon age. Original error definitions and covariance remain unavailable.

The mean is **20,882.79 +/- 50.28 radiocarbon BP**, close to but not exactly the reported 20,890 +/- 51. Unrounded inputs, original settings and the cause of this small difference are unknown. More consequentially, the consistency statistic is **Q=8.66093 on 2 degrees of freedom**, giving **p=0.01316** under those assumptions. Q exceeds the 5% chi-square critical value of 5.99146. The printed observations therefore fail this conventional homogeneity check; reproducing a mean alone does not justify its narrow uncertainty.

The two more precise determinations differ by 290 radiocarbon years, or 2.827 combined standard errors. This is an exploratory diagnostic, not an additional independent hypothesis test or a reason to discard either assay. Scaling every independent standard error by 1.2023 would place Q at the 5% boundary; that is only sensitivity arithmetic, not a measured correction. A shared systematic offset shifts the inferred age but does not remove between-assay disagreement.

Potential causes include understated uncertainties, preparation differences, contamination, transcription or model details. The present data cannot choose among them. The result does not demonstrate a different burial date, collapse the biological and sediment clocks, or support historical fabrication. Preserve all three dates; obtain certificates, collagen quality metrics, original calibration/model settings and any explanation of the combination before adopting a precise pooled calendar age.

The 2012 mammoth abstract search located an old University of Minnesota program URL, but direct retrieval failed. No individual mammoth assay values were inferred from that failure or from the later aggregate label.

## Exposure evidence: original gnaw-mark report

[S102, Wahl and Barton (2013)](https://cascadiaprairieoak.org/wp-content/uploads/2013/12/Program-and-Abstracts-2013-NWSA-CPOP-Conference_final.pdf), printed p.82 / PDF p.91, reports 11 examined ribs, 10 with gnaw marks and 148 measurable marks. Dominant widths were 0.3, 0.5 and 2.1 mm; the authors distinguish ungrooved rodent marks from grooved marks attributed to lagomorphs. This is a preliminary poster abstract, not the underlying specimen images or measurement sheet. [Structured observations and missing fields](../data/coyote-taphonomy.json) retain that distinction.

[S101, Last and Barton (2014)](https://depts.washington.edu/amqua14/amquafiles/AMQUA2014_Abstracts-Program.pdf), pp.80-82, reports bones spanning at least 50 cm vertically, flood sediment about 15 cm above them, and nearby section-1 beds about 28-46 cm thick. The authors infer at least two burial floods and use S102's gnawing as support for intervening exposure. This inference assumes the nearby thicknesses constrain deposition at the carcass. S101 also gives 17,146-17,795 cal BP for Coyote Canyon but cites the still-unrecovered 2012 report; this is no new assay, and its probability level is not specified here.

Our inference is narrower: if the gnaw diagnosis is correct, animals had access to the bone. That challenges uninterrupted inaccessibility from death through excavation, but does not by itself establish when or how long exposure occurred. Marks could precede transport, form during partial burial, or follow later re-exposure; these are alternatives to test, not findings. The mark count is not a count of exposure episodes. The 2014 report depends on the 2013 report and must not be counted as independent replication.

A discriminating follow-up needs rib IDs, their three-dimensional bed positions, mark images, and sediment/mark overprinting relationships. These can test whether gnawing actually lies between distinct deposits. Until then, neither a single immediate permanent burial nor a precisely counted sequence of floods is established by this taphonomic evidence alone.

## Sediment chemistry and the contact-validation gap

[S103, Last and Krogstad (2014)](https://northwestscience.org/web/default/files/resources/annual_meetings/older_annual_meetings/2014_NWSA_85thAnnMtg.pdf), printed p.74 / PDF p.76, describes portable and laboratory XRF. Reported Ca/Fe/Mn/Ti correlations range from 0.80 to 0.92; Ba-Ti plots best separated major units. Contact-depth adjustments improved separation. Further lateral testing and differentiation of flood events were prospective work. Raw measurements and plots are absent. The 15 cm thickness cited by S101 does not appear here; S101 cites p.73, whereas this retrieved contribution is on p.74. Version differences remain possible.

This narrows the evidentiary claim: preliminary chemical differentiation of major units is not an independently validated count of flood events. Correlation between instruments does not by itself establish accuracy or chronological separation. Revising contacts to improve chemical separation is a reasonable exploratory procedure, but testing those same revised contacts with the same measurements is not an independent confirmation.

To make the contact argument reproducible, retrieve the original profiles with sample IDs, depths, concentrations, instrument standards and uncertainty, plus both initial and revised contacts. Then freeze a classification rule on a designated training subset and test it against untouched profiles and separately recorded sedimentary observations. This is a proposed validation design, not a registered prediction or an executed test. A successful chemical classification would still need sedimentary evidence to establish separate depositional events.
