# Melamchi elevation data: available inputs and what alignment can test

2026-10-11. S446–S448. Sourced draft; no independent archive review. [Acquisition ledger](../data/melamchi-dsm-acquisition.json).

[OpenTopography dataset](https://portal.opentopography.org/dataspace/dataset?opentopoID=OTDS.102024.32645.1) provides twelve1m DSMs and a four-page metadata report. PDF1/3/4 were visually inspected. Table1 lists different acquisition dates within several stereo pairs. The candidate P05/P06 comparison brackets January11/18 to October11,2021 (273/266days). Its horizontal CRS is EPSG:32645. Processing uses an ellipsoidal ALOS reference and stable-terrain rigid alignment; the final independent vertical reference remains unverified.

[HydroShare mapping catalog](https://www.hydroshare.org/resource/b6da096000284d5882d13b085b7669ac/) describes mapped river/landslide features and obscured-area controls. Its event-related mapping interval is November2020–October2021. Publication2024, update2026 and current citation2026 are separate metadata dates, not event dates. Actual polygons remain unacquired.

[The indexed article record](https://www.nature.com/articles/s41561-024-01596-x) identifies Supplementary Table3 for DSM-difference uncertainty and a source-data workbook. Neither workbook was retrieved; no uncertainty or volume result was adopted from an excerpt.

## A material limit for the upheaval hypothesis

Fitting a rigid translation and rotation to terrain designated stable changes which displacement components remain observable. A shared offset can be absorbed by that fit. Thus local relative surface change may be measurable, while a claim of region-wide displacement needs independent absolute control and access to the transformations or unaligned inputs. This is our methodological inference from the reported registration procedure; it is not a measured uplift result or an allegation of data manipulation.

The interval comparison also spans processes before and after June. Assigning all change to one flood would require additional timing evidence. DSM pixels may include canopy and buildings;1m spacing must not be substituted for1m vertical accuracy. Stereo imagery taken days apart can include real surface or viewing changes, requiring checks beyond filenames.

## Concrete path to a quantitative comparison

The ledger identifies public P05/P06 file URLs and transcribes all twelve pair dates. Next acquire and hash the actual rasters, masks and uncertainty workbook; inspect spatial overlap and valid pixels; verify vertical reference and transformations; evaluate residuals on independent stable controls. Only then calculate masked erosion/deposition with uncertainty propagation and compare source and sink volumes. A computation without these controls remains exploratory.

No raster pixels, new sediment budget, hydraulic reconstruction, field validation or independent replication was completed this turn. The metadata narrows the next acquisition and prevents testing absolute upheaval with data that remove overall offsets. This dataset is a local modern control; it does not date the historical Reddit buildings.31core case drafts/448sources; all twenty objectives remain active.


### 2026-10-11 — Actual raster acquisition and execution

[Executed local surface comparison](MELAMCHI-RASTER-INSPECTION.md): earlier non-acquisition statements above are historical snapshots. P05/P06 acquired; selected window processed. Masks, uncertainty workbook and vertical confirmation remain missing; no validated deposit thickness/volume. Same448sources,31case drafts.


### 2026-10-11 — Selected mapping-file acquisition

[Author-mapped channel comparison](MELAMCHI-CHANNEL-COMPARISON.md) acquires four KML files and processes them in the same window. Earlier missing-mask statements are historical snapshots; remaining masks/uncertainty/independent stable controls still missing. Outside selected channels is not a validated stable control. Same448sources/31case drafts.
