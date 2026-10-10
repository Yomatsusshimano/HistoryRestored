# Modern terrain check of nearby Missoula controls

2026-10-09. C008 / S11, S27, S335. Sourced draft; no independent review or hydraulic simulation.

The [complete control audit](MISSOULA-COMPLETE-CONTROLS.md) found a crossing control at 433 m and a noncrossing control at 431 m, approximately 99 m apart. Their printed elevations cannot both constrain one exact level peak water surface. That conditional finding depends on their values, positions, event association and bound interpretation; it is not a general flood-model rejection.

Ten ordinary queries to the [USGS Elevation Point Query Service](https://epqs.nationalmap.gov/v1/json?x=-119.9674&y=47.2119&wkid=4326&units=Meters&includeDate=true) recover modern terrain at both nominal coordinates and four corners of each four-decimal-degree rounding cell. All responses identify raster 73965, resolution 1 m. Catalog metadata identifies **WA_CentralWildfire_D22**, NAVD 88, with source dates 20220823-20230628 and publication field 20250630. EPQS reports acquisition 5/3/2023, while the catalog AcquisitionDate represents June 28, 2023 UTC. Their date-field semantics are unverified; no exact point observation date is selected. Service update dates are not terrain observation dates.

| Control | S27 field elevation | S27 modeled terrain | Modern nominal terrain | Five queried values |
| --- | ---: | ---: | ---: | ---: |
| Crossing, row 12 | 433 m | 431 m | 431.602 m | 431.019-432.466 m |
| Noncrossing, row 45 | 431 m | Unspecified | 434.117 m | 433.375-434.922 m |

The nominal modern noncrossing point is **2.515 m higher**, reversing the printed field ordering of -2 m. All five queried noncrossing values also exceed all five crossing values, with a minimum separation of 0.909 m. These are sampled values, not extrema over either complete coordinate cell, confidence intervals or a proof of terrain preservation. Coordinate rounding need not describe the entire positional error. Reported 1 m resolution is not 1 m vertical accuracy.

This comparison is descriptive: the S27 vertical datum is unspecified, and neither original field observations nor ancient surfaces are authenticated here. Modern terrain cannot silently replace the study's dam-removed and otherwise modified grid. The result nominates the original elevations and site registration for checking; it does not establish that either published field value is wrong, identify the actual paleo-divide, validate noncrossing evidence or compute a flood stage.

## Original review context and dependencies

S11's original author-linked PDF Table 3, printed/PDF p. 40, was visually inspected. It labels the crossing **Babcock Ridge divide crossing**, at 47.21190 / -119.96744, 1420 ft / 433 m, and interprets Columbia Valley flow and Quincy Basin overflow. This corresponds to S27's row labelled Lynch Coulee divide crossing, with rounded longitude. A separate **Lynch Coulee erratic** has the same reported elevation but lies at 47.29992 / -119.95224; it is not this divide control. Do not join those sites by name or height alone.

The shared O'Connor interpretation, authors and field sources prevent counting S11 and S27 as independent confirmation. Selected-page inspection does not establish whether the noncrossing control is absent from every other part of S11. The original field notebook, quad edition, datum and geomorphic evidence remain needed.

Raw public-service [responses and acquisition ledger](../sources/originals/missoula/lynch-terrain/acquisition.json) are preserved unchanged with hashes. The [offline audit](../analysis/lynch_terrain_audit.py) verifies responses and reproduces [results](../analysis/lynch-terrain-audit-result.json). Copyrighted review PDF remains linked rather than redistributed. This is retrospective input investigation, not a successful held-out prediction.
