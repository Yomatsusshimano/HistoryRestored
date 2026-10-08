# Denny regrade: image and engineering account

Research draft, 2026-10-08. Case C002; no independent review.

[Seattle Municipal Archives item 9349](https://www.flickr.com/photos/seattlemunicipalarchives/8699489754), source S45, is attributed to Engineering Department Photographic Negatives, series **2613-07**. The institutional page identifies a view northeast from Second Avenue taken June 27, 1910. Its lower-left **6-27-10** inscription agrees. The digital upload date, May 1, 2013, is a different event. This item is not automatically part of the **2613-22** album series located earlier through S02.

The displayed photograph was visually inspected in the browser. Buildings remain beside steep exposed earth faces and high remnants, surrounded by broad cleared ground; street infrastructure and advertising boards occupy the foreground. These observations are consistent with the attributed excavation context. They do not determine sediment age, original ground elevation, quantity removed, or the complete sequence of work. Location and viewing direction remain catalog attributions.

The [observation ledger](../data/denny-photo-observations.json) leaves coordinates, calibrated scale and excavation volume null. This frame and its caption are one source lineage. They are not a before/after comparison and do not date Pioneer Square's separate areaways. Next retrieve adjacent frames and grade plans, then register identifiable structures to survey control before measuring terrain change.

The former municipal permalink returns 404; the institutional Flickr copy remains accessible and displays CC BY 2.0. The image is linked rather than republished. Original-negative authentication remains pending.

## Engineering account: reported capacity versus achieved excavation

[UW Document 46](https://www.washington.edu/uwired/outreach/cspn/Website/Classroom%20Materials/Curriculum%20Packets/Building%20Nature/Documents/46.html) transcribes selected portions of assistant city engineer O. A. Piper's circa-1910 report (S46). Its archival locator is LID 4818, control 2615-03, Letters, Folder 3, pp. 2, 15–16, 33–34. The underlying microform and omitted passages remain uninspected.

Piper describes steam shovels, trains and hydraulic equipment; reports a February 1, 1907 pump start; and gives an 800-horsepower motor with a guaranteed 3,500-gallon/minute delivery. Continuous operation would yield **5,040,000 gallons/day**, consistent with his approximate daily figure. This is water capacity, not measured sediment removal. Downtime, slurry concentration and operating logs are absent.

He estimates nearly six million cubic yards removed and public/private spending probably above three million dollars. These are participant-reported aggregates, not an audited excavation budget. His favorable assessment also acknowledges initial design problems. The narrative strengthens the documented-earthmoving explanation, but cannot establish surveyed volume or authenticate every project date.

The [quantity ledger](../data/denny-engineering.json) preserves these distinctions. The [arithmetic check](../analysis/denny_capacity_check.py) tests only continuous-flow conversion. Next obtain the full report, contracts, pump logs and before/after surveys; distinguish the project's phases before comparing totals.

## Contemporary press comparison

S47, [The Hydraulic Jet for Railway Building](https://fraser.stlouisfed.org/files/docs/publications/cfc/cfc_19100430_supplement.pdf), *Commercial & Financial Chronicle*, Railway and Industrial Section, April 30, 1910, printed p. 6 (PDF page 4), was visually checked. It describes a nearly **5.4-million-cubic-yard** Denny contract dated August 1908, reportedly more than three-quarters complete. Its Lake Union plant has three turbine units totaling **1,950 horsepower**, rated at **12,600 gallons/minute**. It also describes hydraulic spoil discharge through a harbor tunnel and concurrent steam-shovel/railway work.

This is another contemporary publication, not demonstrated independent measurement: no underlying survey, contract, named informant or operational log is supplied in the passage. Its contract total and progress fraction must not be equated with Piper's approximate aggregate removed volume. Nor is this Lake Union installation automatically the earlier sound-water plant in S46. The article's preceding discussion of other projects does not supply Seattle-specific measurements.

The rated flow corresponds to **18,144,000 gallons/day** only at uninterrupted operation. Pressure is printed as “180 lbs.” without an explicit area unit in the Seattle passage; no energy-efficiency estimate is assigned. Exact work boundaries, achieved production and source dependence remain unresolved.
