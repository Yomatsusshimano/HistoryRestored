# Arctic chronology: what the measurements date

Research draft, 2026-10-08. Cases C003 and C009 remain unreviewed independently.

The next useful comparison is between dated objects and their depositional histories. An age assigned to quartz or a sediment layer is not automatically the date an animal died, or the date of every later disturbance.

## Camel context audit

[The original paper](https://www.nature.com/articles/ncomms2516) and [its supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fncomms2516/MediaObjects/41467_2013_BFncomms2516_MOESM304_ESM.pdf) are now inspected beyond search excerpts. Tables S3-S4 were checked visually. The [dating records](../data/dating-records.json) preserve sample identifiers, asymmetric uncertainties, rejected ages, and source discrepancies.

Two details require care: the reported minimum-age interpretation depends on exposure/shielding assumptions, and the dated sediment lies below the fossil horizon. Extending the sediment result to the fossil requires the paper's stratigraphic association. Testing a later redeposition hypothesis requires separate evidence for that later event.

The main inline age image differs by 0.1 Ma from the methods and supplementary table. The record retains both values rather than silently choosing one. Another small ratio difference between Tables S3 and S4 is also recorded. Neither establishes deliberate falsification or a broad chronological break.

## A transparent arithmetic check

Run `python analysis/burial_clock.py` to regenerate the [calculation](../analysis/burial-clock-result.json). It uses the paper's parameters and one transcribed sample ratio. The result is about 3.72 Ma under the simplified assumption that the ratio starts at 6.75 and then changes only through radioactive decay.

This checks the scale and arithmetic. It does not reproduce the authors' full uncertainty model. If grains already had a low ratio before their final deposition, the calculation alone cannot date that final event. Independent stratigraphy and exposure-history modeling remain essential. No event date was selected for the investigation.

## Mammoth and horse context audit

[Murchie et al. (2021)](https://www.nature.com/articles/s41467-021-27439-6) provides a useful competing interpretation: potentially later survival inferred from sedimentary DNA, with reworking considered. Two Table 1 sediment-age records are transcribed; they are not new direct animal dates. Sample-specific taxonomic assignments have not been revalidated here.

Ancient molecular damage and controls against modern contamination cannot alone distinguish ancient DNA deposited contemporaneously from ancient DNA moved out of older material. Conversely, a gap in known bones does not by itself refute survival of a small population. The next discriminator is agreement between undisturbed sediment context, sample-level DNA assignment, and independently dated biological remains.

## Geographic coverage

C003 now records the authors' approximate regional location for the two Ellesmere sites, explicitly distinguished from exact specimen coordinates. C009 has named sites but no verified coordinates in this archive. These records are not yet a range map for all requested taxa.
