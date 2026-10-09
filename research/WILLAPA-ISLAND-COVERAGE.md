# Willapa unmatched islands: coverage and photo-inventory test

2026-10-09. C004 / S253,S256-S260. This follow-up tests the possible coverage explanation for historical apparent-marsh traces49/51. Earlier crop-bounding-box overlaps did not locate the actual source-limit line.

## Exact geometry changes the next action

The [coverage script](../analysis/willapa_island_coverage.py) reuses the previous10m samples, projects all delivered source classes to generic NAD83UTM10, checks exact project-polygon inclusion and measures unsigned nearest distances by class. [Results](../data/willapa-island-coverage.json) preserve every distance, candidate ID/date/attributes and input hashes. The project polygon is valid; all96samples on49and63on51are inside it. This does not establish complete photographic or compilation coverage: the catalog expressly warns against that inference.

| Historical ID | Minimum to project boundary | Minimum to actual source-data-limit line | Median to nearest MHW | Median to nearest apparent-marsh |
| --- | ---: | ---: | ---: | ---: |
|49 |8772.6m |5854.8m |299.3m |6386.8m |
|51 |9375.8m |6435.9m |159.3m |5781.5m |

The source-limit line's large bounding box overlapped the crops, but its actual geometry is far away. A nearby mapped limit therefore does not explain the missing local apparent-marsh code. This narrows the candidate explanation; it does not prove the island was surveyed completely or disappeared.

Both traces' nearest MHW candidate is modern887366, dated20061009.51approaches it within1.81m at one sample, while49's minimum is215.56m. These are different-class associations, not replacements for marsh edges or signed displacement. A change in class, shoreline position, vegetation, source coding or coverage must be tested with imagery.

## Original frame inventory recovered

[NOAA's annual inventory page](https://www.ngs.noaa.gov/web/APOS2/sf2.shtml) links the [2006ZIP](https://www.ngs.noaa.gov/web/APOS2/download/shp/NOAA_NGS_IMAGERY_2006.ZIP), now preserved [unchanged](../sources/originals/cascadia/NOAA_NGS_IMAGERY_2006.ZIP). [The script](../analysis/willapa_photo_inventory.py) reads12,133national footprint records and selects430with exact projectWA0401. All eight historical marsh traces have candidate intersections. [The inventory ledger](../data/willapa-photo-inventory.json) preserves original frame fields, footprint coordinates and sample coverage counts. No coordinate or observation date was inferred from a webpage's publication label.

Each island trace has18candidate frame footprints. The October candidates include roll0605R10frames0004–0006and0016–0018, recorded09-OCT-2006and Black & White IR. These coincide with roll/date/frame ranges in the inspected WA0401D report and with887366's stored date. The report table gives different tide/time ranges across these frame groups; final selection requires the original images and stereo/feature correspondence. Matching date and footprint alone does not establish which frame generated a particular line.

Other candidates include April and May exposures. The wider project inventory can include other subprojects: for38it also includes September0605R09frames absent from WA0401D's table. The ledger flags report-listed ranges without deleting other candidates. These flags are documentary eligibility, not independent authentication or exact ground coverage. The source PRJ is generic geographic NAD83; footprint precision/accuracy and photo orientations remain unverified.

## Accessible evidence and remaining retrieval gap

[NGS's current notice](https://www.ngs.noaa.gov/web/APOS2/APOS.shtml) says analog-film holdings ceased being maintained/accessed/sold by NGS from October2022and were to transfer to NARA/FRC under Coast and Geodetic Survey records. That notice is a custody route, not confirmation of completed accession, digitization or availability of these specific frames. No photograph was ordered, downloaded, inspected or requested from another person.

Next recover those named October frames or a documented derivative with acquisition/tide/orientation metadata, inspect whether887366follows the same island feature, and compare vegetation with historical symbol meaning. Do not treat public unavailability, a class change or a distant nearest line as catastrophe evidence. Historical MHW audit, datum/map uncertainty and the full twenty-part objective remain open.
