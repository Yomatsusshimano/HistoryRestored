# Shelbyville: modern survey records do not yet recover the courthouse mark

Research draft, 2026-10-11 (America/New_York). C030/R004; S400–S402. No independent review. [Query and record ledger](../data/shelbyville-mark-recovery.json).

The [1907 courthouse tablet](SHELBYVILLE-ELEVATION-CONTROLS.md) remains unmatched. A bounded search of the National Geodetic Survey's published controls returned two different stations. Their full datasheets narrow the next action: neither supplies a recovered courthouse height or a target street-grade measurement.

## Reproducible retrieval

The [official NGS API documentation](https://geodesy.noaa.gov/web_services/data-explorer.shtml) advertises a bounding-box service, a 500-record limit and a metadata endpoint. The exact [query](https://geodesy.noaa.gov/api/nde/bounds?minlat=39.400&maxlat=39.415&minlon=-88.805&maxlon=-88.780) used latitude 39.400–39.415 and longitude −88.805–−88.780. It returned two records, below the stated limit. These bounds were chosen to search the downtown vicinity; they are not a sediment footprint or a preregistered catastrophe prediction. Coordinates are catalog positions, with their own accuracy limits.

The [NGS map landing page](https://geodesy.noaa.gov/datasheets/ngs_map/) advertises its ArcGIS datasheet service. The published item configuration and actual service fields were read. A query for the two returned PIDs supplied their DATA_SRCE links. Those advertised HTTP links were retrieved using HTTPS on the same host and path. Both full HTML datasheets were read; their retrieval-complete markers were present. No recovery reports were submitted, and no field inspection occurred. API, hosted service and datasheets are one institutional delivery chain, not independent replication.

## KB0462 — A 88

The [A 88 datasheet](https://www.ngs.noaa.gov/cgi-bin/ds_mark.prl?PidBox=KB0462) describes a disk stamped **A 88 1935**, set in a concrete post near the railway station and old water-tower pillars. It is not the unstamped courthouse-step tablet described in Bulletin 421. The history records monumentation in **1935**, followed by **mark not found** reports in **1973**, **1979** and **November 18, 2004**. Failure to find a mark does not establish its destruction, movement, burial or cause of loss.

Its published orthometric height is **182.553 m / 598.93 ft, NAVD 88**, from differential leveling adjusted in **June 1991**. The superseded section gives **182.636 m / 599.20 ft, NGVD 29** and a partially specified 1992 date. These are values in different datums; the adjustment/date labels are not two documented field observations of uplift. No displacement is derived from their difference.

The horizontal position is map-scaled, with an estimated ±6 arcseconds in the datasheet. The monument's stability code C denotes a type commonly subject to surface motion. Neither its published height nor its decimal coordinate formatting establishes a currently recovered, stable control. Its raw field leveling notes and a modern in-place recovery were not acquired.

## KB1266 — Shelbyville municipal tank

The [tank datasheet](https://www.ngs.noaa.gov/cgi-bin/ds_mark.prl?PidBox=KB1266) identifies the station as the **vent atop the tank**, first observed in **1974**, with a good-condition recovery report on **June 18, 1994**. It describes a location one block east of the courthouse, north of State Highway 16. This is a separate structure and station point, not pavement or the courthouse tablet.

The record supplies an adjusted NAD 83(1997) horizontal position but **no published orthometric height**. The API's GEOID18 value of −32.272 m is geoid height, not the tank's ground or vent elevation. An approximate 125-foot structure height in the description cannot supply the missing surveyed height or a street datum. The 1994 condition report does not establish the station's present condition in 2026.

## Decision and remaining test

Do not subtract A 88's height from the courthouse height to obtain burial depth: these are different points, different datums and different histories. Do not turn the tank geoid value into a ground elevation. No returned record in this bounded query matches the courthouse description; this is not proof that its mark or records are absent from every archive. NGS's [FAQ](https://geodesy.noaa.gov/faq.shtml) notes that marks from other organizations may be absent when their records were not submitted.

The next documentary targets remain the courthouse tablet's recovery and original USGS/state leveling records, followed by a datum tie and measured offsets to 212/216 E Main. Street design and as-built profiles, plus dated sediment contexts, remain necessary to distinguish grading, construction fill and natural deposition. This batch narrows usable control selection; it does not establish or rule out a global catastrophe. All twenty objectives remain active.
