# Danville and Ohlson Ranch reference analyses

2026-10-09. C005/S327. Read-only original workbook extraction; no workbook layout inspection or independent review.

The original [TableS3workbook](https://ndownloader.figshare.com/files/29107476) in the publisher-linked2021supplement contains four neutron-activation analyses of two reference sample identifiers. Its publisher MD5 matches. Header rows1-3, group141 and rows143-146 were read with bounded32column extraction. Full raw cells and descriptive comparisons are retained in [data](../data/danville-inaa-comparison.json), with a [reproducible extractor](../analysis/danville_inaa_check.py) requiring the original workbook as its argument.

| Workbook row | Sample | Analysis number | Laboratory code | Laboratory identifier |
| ---: | --- | ---: | --- | --- |
|143|758-328|303|D|D-245150|
|144|758-328|119|L|1007 N|
|145|OH-2A|333|D|D-245128|
|146|OH-2A|6|L|851 J|

The header identifies D as the USGS Lakewood laboratory and L as Lawrence Berkeley Laboratory. The [main Table2Atext](https://www.researchgate.net/publication/354421087_Late_Cenozoic_tephrochronology_of_the_Mount_Diablo_area_within_the_evolving_plate-tectonic_boundary_zone_of_northern_California), printed421, identifies758-328as Danville and OH-2Aas the Ohlson Ranch ash. It attributes analyses to James Budahn and Harry Bowman. Two analyses of a named sample are not two new field localities; physical aliquot custody and laboratory uncertainty remain unverified.

## Preserve units and missing values

The workbook explicitly specifies ppm concentrations except iron, reported in percent. Its iron values0.63-0.70are retained in those stated units. The main table's exposed note broadly describes INAA concentrations as ppm without that exception; the explicit supplement convention is recorded, and no silent percent-to-ppm substitution is made. The missing Dy entry in row143 is-1in the workbook and ND in the main text. It remains raw-1 in retained cells and becomes unavailable in comparisons, never a negative concentration or zero.

The main Table2Atext omits the workbook's first analysis number303 and rounds the final OH-2A Dy value1.62to1.6. These differences are preserved rather than treated as new assays. No original main scan has been inspected.

## What the numerical check does and does not establish

Nineteen elements are reported. Same-laboratory cross-sample comparisons have18available elements for D and19for L, owing to the missing Dy value. The calculation records each paired value and the symmetric percentage difference200|a-b|/(a+b). It also compares the two laboratory results for each sample, so laboratory variation remains visible beside cross-locality variation.

This is a descriptive calculation. There are no supplied per-element measurement errors or covariance in these selected rows, no declared source-specific acceptance threshold, and no authentication of sample custody. Neither the number of available elements nor a small percentage difference is a statistical acceptance test. No unweighted grand average is substituted for the original measurements.

The authors' Danville/Ohlson correlation judgment is therefore traceable to specific numerical reference analyses, but has not been independently validated. These rows do not supply a trace-element fingerprint for either FLV-119-WW population, do not reproduce the2001lower-Nomlaki rare-earth separation, and do not directly date the Willow Wash bed. The two locality records are also not automatically the exact zircon/biotite aliquots quoted from2012.

Next recover analytical uncertainties and the dated Ohlson sample identifiers, plus trace-element data for the separate Willow Wash glass populations. Compare identified units under a declared correlation model before transferring any eruption age or interpreting later deposition.
