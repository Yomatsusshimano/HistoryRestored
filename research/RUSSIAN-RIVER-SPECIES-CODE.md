# A recovered species key and the limits of single-taxon depth inference

2026-10-09. C005/S332-S334. Follow-up to the [modern calibration controls](RUSSIAN-RIVER-FAUNAL-CALIBRATION.md).

The [original1983companion report83-83](https://pubs.usgs.gov/of/1983/0083/report.pdf), Table2, printed8/PDF11, explicitly expands **CIBFLT = Cibicides fletcheri**. Title and key scans inspected; other54-page PDF contents not audited. This replaces a guessed abbreviation expansion with a documented related-study key. It does not independently reidentify the specimens or establish every later taxonomic convention.

The1984report cites this companion and uses the same token. Its complete Table9CIBFLTcolumn, printed31/PDF32, has21L1-81sample rows. Joined to Table1printed6/PDF7, five nonzero entries occur at uncorrected depths21,26,40,53and68m; the other16entries are printed0.0. The previously retained five rows were therefore all positive entries in this particular column, not a random selection of the full modern data. All21rows, including zeros, are now retained in [structured controls](../data/russian-river-faunal-controls.json).

The53and68m occurrences demonstrate why presence alone must not be converted into an exclusive depth<50m rule. The1987abstract lists this species among several that characterize its inner-shelf **assemblage**. It does not state that every isolated occurrence is limited to that assemblage. These entries therefore challenge the exclusive single-taxon shortcut, not the original multi-species factor analysis. Sample processing, possible transport, rounded percentages and uncorrected depths remain source limits; no specific transport explanation is proved.

The [executed summary](../analysis/russian_river_cibflt_check.py) counts the21entries and reports the five positive depths without fitting a model, estimating prevalence outside this cruise, or predicting Ohlson depth. Printed zeros remain rounded reported zeros, not proof of absolute biological absence. No counts are reverse-engineered from percentages.

The exact71sample matrix in the1987study and quantitative Ohlson assemblages remain unrecovered. Next establish the original sample selection and complete species dictionary, transcribe the full matrix, and test a declared assemblage predictor against held-out modern samples. An ecological code match and isolated occurrence do not date a fossil bed or measure tectonic uplift.
