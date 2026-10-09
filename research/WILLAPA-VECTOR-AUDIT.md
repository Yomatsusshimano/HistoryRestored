# Willapa vector audit: feature meaning, coordinate systems and dates

2026-10-09. C004 / S253-S255. Read-only audit of the personal geodatabase in NOAA's recovered T-03921 package. This prepares physical comparison inputs; it does not measure shoreline change, authenticate the ecological classification or recover the missing1870s marsh sheets.

## Original package and extraction

The [unchanged vector ZIP](../sources/originals/cascadia/T-03921/WC46C03.zip) contains one5,308,416-byte file, WC46C03.mdb. The [original vector metadata](../sources/originals/cascadia/T-03921/wc46c03vector.met) is separately preserved. Both came from the [current NOAA package](https://nsde.ngs.noaa.gov/downloads/T-03921.zip); the [acquisition ledger](../data/willapa-vector-acquisition.json) retains original hashes and archive-member identities.

The installed64-bit Access ODBC driver opened a local extracted copy with ReadOnly=1. [The exporter](../analysis/export_willapa_geodatabase.ps1) uses SELECT statements only and verifies the database hash is unchanged. It exports four feature tables and selected spatial-reference/domain tables into [rows](../data/willapa-geodatabase-rows.json), preserving binary geometry/domain values as base64. Driver column-schema restrictions were unavailable; direct SELECT reader fields supplied the actual schema. No database schema or record was changed.

Reproduction requires extracting WC46C03.mdb from the preserved ZIP and a compatible Windows Access ODBC driver. The Python [audit](../analysis/willapa_vector_audit.py) can independently run on the published row export without that driver. Its simple binary-domain interpretation is checked by complete byte consumption and entry counts; it is not a general personal-geodatabase implementation.

## Different lines have different evidential roles

The actual line tables use Feature codes and a stored CCoast domain, rather than the legacy F-code values described in the accompanying vector metadata. The following labels are decoded from that stored domain; source spelling is retained in the result ledger.

| Feature code | Stored meaning | Line records |
| --- | --- | ---: |
|15 |Natural apparent marsh or swamp |8 |
|20 |Natural mean high water |40 |
|26 |Undetermined, approximate |12 |
|57 |Undetermined alongshore feature |12 |
|139 |Control point |41 |
|202 |Feature limit |12 |
|205 |User-added line |4 |

These total129 line records, matching the metadata's stated count. They are not129 independent observations of natural coastline. In particular, control symbols, feature limits and added boundaries cannot become coast segments merely because they share a geometry table. The48 apparent-marsh/MHW records are likewise neither48 independent survey campaigns nor48 changes through time.

[NOAA's entity description](https://www.fisheries.noaa.gov/inport/item/60809) distinguishes C-COAST Feature from legacy F_CODE. It does not supply a complete historical crosswalk for this particular database. The [NOAA glossary](https://www.ngs.noaa.gov/RSD/shoredata/c_coast_def.htm) treats apparent shoreline as vegetation's visible outer boundary and ordinary tidal shoreline as an interpreted water-level intersection. These definitions explain why marsh-edge movement and waterline movement are different quantities; they do not independently verify these1922assignments.

Polygon tables contain54 records:35land,16water and3manmade. Their partition is a digitized map classification, not a measured distribution of catastrophe sediment or independently authenticated human construction. No full topology/polygon-closure model or correspondence to each raster line is validated here.

## Coordinate-system and unit audit

| Table family | Rows per table | Database reference | Stored measure units |
| --- | ---: | --- | --- |
|wc46c03lines / polys |129 /54 |NAD1927 UTM Zone10N |Projected metres and square metres |
|wc46c03lines_83 / polys_83 |129 /54 |NAD1983 geographic |Degrees and square degrees |

The database geometry registration links each table to its declared spatial reference. The vector metadata's general NAD83 wording is not sufficient to interpret the unsuffixed projected tables: they explicitly declare NAD27. Nor can the geographic Shape_Length or Shape_Area be treated as metres or square metres.

[Results](../data/willapa-vector-audit.json) preserve each shape's type, parts, point count, bounds, recalculated length/area and difference from stored values. Every exported shape passes byte-size, part-boundary and stored-bounds checks. Recalculated Euclidean lengths and signed-ring areas agree with stored measures under declared numeric tolerances. Corresponding projected/geographic records share IDs and nongeometry attributes.

This verifies internal geometry/attribute consistency, not an independently correct datum transformation. No transformation between NAD27 and NAD83 has been reproduced, no distance to a modern coast calculated, and no shoreline-change significance assigned. The paired versions derive from the same data; they are not independent maps.

## Dates and extraction descriptions

All129line records have source date1922-01-01, source ID T03921, scale20000 and GIS date2006-04-24. The [raster title](WILLAPA-RASTER-CONTEXT.md) gives Jan-June1922. Retain this period rather than interpreting January1 as an exact observation day for every feature.

Stored domains define P as planetable for data source and extraction technology, and M as mono for extraction method; all line records use those values. The generic online entity's listed source/technology options omit planetable P, so that modern description alone cannot decode this historical package.

The database's date-domain descriptions mention June18,2003, although the actual line values are1922and2006. The original vector metadata separately gives GIS capture20060424, vectorization process20070406 and metadata20070418. The stale-looking2003descriptions are not silently substituted for record values, nor explained as deliberate manipulation. Original workflow/version history would be needed to establish their cause.

## Consequences for the full reconstruction

Future coast-change tests must choose comparable feature types, retain approximation limits, identify surveyed/revised segments, reproduce coordinate transformations and account for tides and cartographic uncertainty. Added/control boundaries and apparent vegetation edges must not be blended into one observed waterline.

These recovered inputs make a quantitative comparison more feasible, but no modern comparison or predictive physical model is completed. Earlier target marsh sheets and original Copalis section/sample controls remain separate gaps. The database, raster, metadata and report share a survey lineage. All twenty objectives stay active; no independent review, worldwide catastrophe or chronology break is established.
