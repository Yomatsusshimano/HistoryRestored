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

## Later contract: in-place and loose volume are different quantities

[Nelson v. Seattle](https://www.casemine.com/judgement/us/5914ccb6add7b0493480c998), Washington Supreme Court, December 14, 1934, docket 25136 (S48), concerns the **second** Denny regrade, LID 4818, under a September 14, 1928 contract. The inspected opinion text describes excavation by Nevada Contracting Company, Nelson's conveyor transport to Wall Street dock, and Vigilant's scow disposal. This is a judicial account of contract evidence, not inspection of the original signed instruments or daily logs.

Section [11] distinguishes a **4.2-million-cubic-yard estimate in place**, a planned **14,400 cubic yards/day**, and no more than **2.7 million cubic yards** reportedly moved after one year. These are estimate, target and reported progress respectively. The target times 300 working days gives 4.32 million cubic yards, about 2.9% above the rounded estimate; it is not a new final measurement.

Nelson's cited testimony gives 30–40% expansion on excavation. Applying that claim to 4.2 million gives 5.46–5.88 million loose cubic yards. The opinion's approximate 5.4-million comparison is retained separately; no measured expansion factor is established. Crucially, this later quantity must not be identified with S47's similarly sized **1908** contract.

The court favors inspector Harry C. Scott's reconciled delay records over conflicting party accounts, offering a specific next archival target. The underlying records remain uninspected. The opinion describes equipment failures and coordination delays; published capacity alone cannot establish actual throughput.

**Archival caution:** UW files the circa-1910 Piper excerpt under LID 4818, which this opinion associates with later work. An earlier report could be retained in a later project file. Without the file arrangement and full report, neither a catalog error nor a revised report date is established. Preserve the supplied locator, but do not use it as a date or phase identifier.

## Complaints, production and transcription limits

[UW Document 52](https://www.washington.edu/uwired/outreach/cspn/Website/Classroom%20Materials/Curriculum%20Packets/Building%20Nature/Documents/52.html) (S49) presents 1929 letters from the Uptown Seattle Association and engineer W. D. Barkhuff. The association distinguishes overall completion from earth removal; its suspicion about contractor motives remains an allegation. Barkhuff credits **543,466 cubic yards**, including conveyor quantities estimated at **300 cubic yards per scow**. This is reported production with an explicit estimation basis, not a recovered survey.

The [reproducible check](../analysis/denny_progress_check.py) finds:

- Component quantities sum exactly to the reported total.
- His capacity factors yield 2,521,200 cubic yards, versus 2,521,000 printed; reported daily/hourly averages are approximate.
- June 25, 1928 to October 7, 1929 spans **469 calendar days**, versus **371 elapsed days** stated. Inclusive counting does not resolve this. An unstated cutoff, transcription error or original error remains possible.

Do not repair the text silently or treat a date discrepancy as evidence of rewritten chronology. The original letter, reporting cutoff and scow-to-in-place conversion remain pending. The later opinion's volume basis cannot automatically be imposed on these estimates.

[UW Document 48](https://www.washington.edu/uwired/outreach/cspn/Website/Classroom%20Materials/Curriculum%20Packets/Building%20Nature/Documents/48.html) (S50) preserves George F. Cotterill's May 17, 1928 objection to sacrificing Denny Park. The excerpt values its cemetery history, vegetation and public use. It establishes a named contemporary objection, not the project's final impact or an erased civilization. Preserve this dissent alongside favorable engineering accounts; inspect the full letter and park plans before evaluating its claims.
