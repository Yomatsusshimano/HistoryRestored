# Coyote Canyon: animal death, sediment burial and dating resolution

2026-10-08. C015 / S32. Sourced draft; no independent review.

Last and Rittenour (2021), *Chronology of Missoula Flood Deposits at the Coyote Canyon Mammoth Site, Washington State, USA*, [DOI](https://doi.org/10.3390/quat4030020). Relevant methods, Tables 1, 3–4 and results/discussion were inspected in the [publisher-provided full-text mirror](https://www.researchgate.net/publication/353041154_Chronology_of_Missoula_Flood_Deposits_at_the_Coyote_Canyon_Mammoth_Site_Washington_State_USA). Direct publisher/PDF retrieval failed. This is text inspection, **not visual verification of table or excavation figures**. The mirror includes duplicated layout/OCR text; a facsimile check remains necessary.

## Distinct objects and contexts

Seven OSL determinations date quartz-bearing sediment: two flood samples and two overlying loess samples at the mammoth site, plus three flood samples at the nearby camel site. The [transcription](../data/coyote-osl.json) retains field and laboratory IDs, depth, accepted/analyzed aliquot counts and the reported two-sigma age uncertainty. None is a direct animal-death measurement.

The paper reports a left-humerus radiocarbon result of about 17.4 ± 0.2 cal ka BP, citing earlier work and grouping laboratory identifiers as Wk-32731&2 in Table 1. This aggregate is not entered as two invented individual measurements. It also reports a Camelops metatarsal age of 25.2 ± 0.2 cal ka BP, older than the nearby flood sediment, supporting its interpretation of reworking. Original bone assay reports and preparation controls remain uninspected.

The mammoth's death in a flood and subsequent carcass deposition are the authors' interpretation of dating and context. Agreement of a bone age and sediment age does not by itself establish drowning. Conversely, an older fossil in younger sediment is not automatically evidence that its biological age is wrong. Taphonomy, articulation, abrasion and stratigraphic association must discriminate these possibilities.

## What the OSL measurements resolve

The [calculation](../analysis/coyote_intervals.py) constructs each reported age ± uncertainty interval and intersects the **five flood-sediment** intervals. Their common range is **18.32–19.05 ka**. Loess samples are excluded by depositional context, not because of their values. This retrospective descriptive check means these broad OSL intervals alone cannot distinguish one common age from multiple nearby ages.

It does **not** mean one event has been demonstrated, or that the common range has 95% joint probability. Marginal two-sigma intervals do not supply a joint distribution; dose-rate assumptions and analytical methods create dependence. The 20.87 versus 16.28 ka central estimates differ by 4.59 kyr, but that subtraction is not a proven minimum duration of flooding. Distinct graded beds, intervening surfaces and preservation must be examined separately. No radiocarbon age is folded into this OSL intersection; their time reference and calibration must first be reconciled.

## Method dependencies and remaining tests

The authors used small-aliquot quartz measurements and a Minimum Age Model for partial bleaching. Table 3 substitutes 9.8% moisture in dose calculations for five samples whose measured moisture was lower; CCMS-1 uses 9.8%, CCMS-2 uses 6.9%. These are reported modeling choices requiring sensitivity analysis, not proof of error. Raw dose distributions, rejection reasons and dose-rate histories have not been reproduced here.

Retrieve the table/section facsimiles and original bone dates; audit bleaching, aliquot selection and moisture corrections. Test death and sediment deposition as separate hypotheses. The named camel site is in Washington; it is not the older Arctic camel locality. This case provides a regional fossil–flood comparison without demonstrating a single global wildlife upheaval.
