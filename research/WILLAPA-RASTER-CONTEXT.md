# Willapa1922 raster: recovered placement and metadata limits

2026-10-09. C004 / S251-S252. A [current NOAA download](https://nsde.ngs.noaa.gov/downloads/T-03921.zip) supplies the historical raster, its world file, metadata, a descriptive report and related vector files. The [acquisition ledger](../data/willapa-raster-acquisition.json) records archive and preserved-member hashes. This advances geographical input recovery without claiming a shoreline-change measurement or the missing1870s marsh maps.

## Acquisition and inspected content

NOAA's historical-chart search for WA T-sheets in1870-1873 did not list the targeted1261-1264 sheets. The current Shoreline Data Explorer page exposes a tiled survey index and a download route keyed by survey identifier. A single tile covering Willapa returned72 indexed features, none dated before1900. These bounded results do not demonstrate absence from other archives or indexes.

The tile's T-03921 record provided legacy raster/world/metadata addresses on the nosimagery host; ordinary requests failed DNS resolution. The current NSDE T-03921 ZIP download succeeded and contains seven members. Only the raster, world file and raster metadata are published unchanged in this tranche; the vector ZIP, vector metadata and package report are not fully audited. The previously inspected S248 report remains its own hash-recorded copy.

The [raster](../sources/originals/cascadia/T-03921/t03921_dd.jpg) is19299x8091 pixels. Its whole sheet was viewed at reduced scale, and its title identifies register3921, Willapa Bay, Jan-June1922 and1:20,000. It depicts selected shoreline segments around the bay, including Leadbetter and Toke areas. Full small annotations, line classifications and ecological symbols were not transcribed. This is a rectified digital derivative of the historical source, not an untransformed paper original.

The [1922 descriptive-report audit](WILLAPA-HISTORICAL-SURVEYS.md) remains relevant: selected segments were rerun, low-water line was observed where tides permitted, and small changes might not appear at the map scale. Blank/unrevised portions cannot automatically be classified as unchanged coast.

## What the placement calculation checks

The [world file](../sources/originals/cascadia/T-03921/t03921_dd.jgw) supplies six affine coefficients. [The script](../analysis/willapa_raster_context.py) uses the stored geographic NAD83 units, maps pixel centers, and places outer edges half a pixel beyond the corner centers. It does not trace linework, identify marsh, convert a tidal datum or estimate elevation.

The [result ledger](../data/willapa-raster-context.json) retains all coefficients, hashes and calculated bounds. Checks establish positive horizontal spacing, negative vertical spacing, zero stored rotation, and agreement within0.001degree with the metadata's rounded bounding box. This is a raster-placement consistency check; it is not independent geodetic authentication or proof that a particular shoreline point is accurately located.

## Date and accuracy fields must retain their roles

The [original metadata](../sources/originals/cascadia/T-03921/t03921.met) supplies these distinct fields:

| Field | Stored value | Interpretation boundary |
| --- | --- | --- |
| Citation publication |192201 |Source citation label; not exact observation day |
| Source publication |192206 |Separate source citation label |
| Source content interval |192201-192206 |Consistent with map's Jan-June1922 title |
| Content interval labeled ground condition |20060123-20060123 |Conflicts with using the field literally as historical survey date; preserve the mismatch |
| Georeferencing process |20060123 |Processing date, not coastline-change date |
| Metadata date |20060125 |Metadata preparation/review |

The source-content/title agreement supports1922 as the survey period. It does not explain why the outer ground-condition field uses the processing date, and no intent or calendar shift is inferred. Neither silently repairing the metadata nor treating2006 as a new historical survey is justified.

The metadata reports rectification RMS values of0.391m for x and0.628m for y. It describes coordinate-link fitting and rejection of pairs exceeding a threshold. These are reported fitting residuals, not complete uncertainty for original field observations, shoreline interpretation, selected control points or temporal comparisons. The original link/control residual report has not been recovered, and the calculation does not validate those numbers.

The raster is declared geographic NAD83 in decimal degrees. Metadata identifies mean high water, but tide times and range are unknown and no vertical accuracy is supplied. S248 also describes low-water line observations. These evidential roles cannot be collapsed into one universal line elevation or transferred to S245's high-marsh interpretation without tracing the actual mapped symbol and datum.

## Consequences for reconstruction

Subsequent [vector audit](WILLAPA-VECTOR-AUDIT.md) now reads the related personal geodatabase and vector metadata, distinguishing actual feature roles and coordinate-system versions. This supersedes the uninspected-vector-table gap, while datum-transform, topology and raster-line authentication remain unresolved.

The recovered raster offers a reproducible spatial reference for future line-by-line comparison. It does not yet supply a measured shoreline shift, land-level change, marsh formation time or correspondence with the northeastern Willapa buried-soil localities. Related metadata, vector products and reports reuse the same survey lineage and are not independent confirmations.

Next identify which mapped lines were surveyed/revised in1922, recover the original control and symbol definitions, and compare appropriate dated modern observations with uncertainty. Recover earlier target marsh sheets separately; this1922 package cannot replace them. Original Copalis profiles and sample chronology remain separate missing inputs. All twenty objectives stay active; no field authentication, independent review or global reconstruction is established.
