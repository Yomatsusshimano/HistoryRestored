# Willapa modern shoreline geometry recovered

2026-10-09. C004 / S257-S258. NOAA credit: these source data were produced and distributed by the National Geodetic Survey. This acquisition replaces the earlier modern-geometry access gap; it does not establish shoreline change or a catastrophe.

## Retrieval and source identity

The [current NOAA viewer](https://nsde.ngs.noaa.gov/cmp.html) constructs download URLs using the project identifier, not the geographic-cell identifier. Its index tile at `https://nsde.ngs.noaa.gov/cmp/cmpidx/8/39/90.pbf` contains project WA0401D, cell GC10747 and start date20050524. The resulting [WA0401D ZIP](https://nsde.ngs.noaa.gov/downloads/WA0401D.zip) downloaded successfully with normal TLS verification. The earlier inferred GC10747 ZIP URL returned AccessDenied; that was an endpoint mistake, not absence of the data.

The [unchanged public package](../sources/originals/cascadia/WA0401D.zip) contains thirteen members: a readme and three shapefile sets. The readme links to NOAA's project metadata search. [Acquisition provenance](../data/willapa-modern-vector-acquisition.json) preserves package/member hashes, viewer/index URLs, index match and hashes. [The audit script](../analysis/willapa_modern_vector_audit.py) uses pyshp and pyproj and extracts only named flat members to a task-local directory.

## What is actually in the package

| Shapefile | Records | Meaning |
| --- | ---: | --- |
|softcopyl1 |2,082 |Lines of many cartographic classes |
|softcopyp1 |141 |Point features |
|projbnd |1 |Project boundary |

All line source IDs are GC10747. The full line table includes453mean-high-water features,375apparent-marsh/swamp shoreline features,262marsh/swamp extent lines and294depth contours. These are different feature types. Counting them together would conflate vegetation, waterline, habitat extent and low-water geometry. Feature identifiers are unique; coordinate finiteness/range, stored bounds and record/shape counts pass declared checks. These checks do not independently authenticate the classifications or field accuracy.

Actual line source dates include20050524,20050525,20060422,20060423,20060504and20061009. All stored HOR_ACC entries are1.2; that inherited field is not a separate accuracy observation for each segment. Original imagery/frame custody and ecological interpretation remain unverified.

## Comparison inputs and selection limits

The [audit ledger](../data/willapa-modern-vector-audit.json) preserves complete attribute counts for all tables and for bounding-box overlap with the historical line extent.480modern line bounding boxes overlap that rectangle. Exact Feature15/20 selection retains188whole features:91apparent-marsh and97MHW.184have source date20060423and4have20061009. [Their attributes and coordinates](../data/willapa-modern-comparison-lines.json) are published with explicit NAD83 labeling. No river, lake, artificial boundary, marsh-extent or depth-contour line is substituted into this selection.

This is coarse spatial eligibility. Features are not clipped, and rectangle overlap is not proof that their actual geometry crosses the historical surveyed coast. Segment/frame matching and historical40MHW-line visual inspection remain needed.188modern features versus48historical features does not measure coast growth, loss, survey frequency or independent confirmation: digitization segmentation and coverage differ.

## Coordinate and metadata qualifications

The PRJ files declare geographic NAD83 with GRS80 and a zero TOWGS84 clause. pyproj reads this as a bound CRS; a direct EPSG lookup fails, while the underlying CRS is equivalent to EPSG4269 with axis order ignored. The script retains the original WKT and that distinction. It does not reinterpret longitude/latitude as WGS84 or perform a zero-shift conversion. The report separately specifies CORS96epoch2002 control and UTM10 mapping; the delivered shapefiles are geographic. Exact realization/epoch reconciliation with the historical derivative remains needed for precision change work.

[NOAA's catalog](https://www.fisheries.noaa.gov/inport/item/61817) confirms the imagery interval and geographic NAD83 delivery. It explains artificial boundaries added for continuity and warns that rectangular limits do not imply complete surveyed coverage. Its process date2010-07-09 is later than the report's2008final review. These are retained as distinct workflow dates; exact intervening export/version history remains unknown. Neither is substituted for photography dates.

Next match homologous apparent-marsh and MHW segments against the historical raster and modern metadata, reconcile datum/tide uncertainty, and calculate declared exploratory offsets with unmatched segments retained. Any measured displacement still requires temporal and physical context before a catastrophe attribution. The earlier1870s sheets remain a separate gap. No independent review or twenty-part completion follows.
