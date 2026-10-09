# Delisle's partial-eclipse account and a Paris diagnostic

2026-10-09. Canvases225-226/printed85-86 of the [BSB French Academy volume](https://www.digitale-sammlungen.de/en/view/bsb10500330?page=225) were downloaded with normal native Windows TLS and visually inspected. Printed85 attributes the account to Delisle le Cadet and describes observation at Luxembourg on May3,1715. A marginal May8,1715 date appears; its administrative meaning is not authenticated. The volume is cataloged as1715 reporting year,1718 publication. The page title itself does not explicitly say new style; Gregorian interpretation relies on French context and the same volume's separately explicit de Louville new-style label.

The Delisle account ends near the top of printed86, before Maraldi's next account starts. The latter has not been audited as a complete observation and is not added as another measured site here. Scans are linked and hashed in [the input ledger](../data/delisle1715-inputs.json), not publicly redistributed, following the manifest's NoC-NC1.0 designation. Attribution: München, Bayerische Staatsbibliothek; shelfmark4Acad.117-1715,bsb10500330.

## What the account reports

Delisle describes a seven-foot telescope projecting the solar image into a dark room onto a perpendicular surface, with circles dividing the image into digits and quarter-digits. He reports:

|Event|Printed account|What is retained|
| --- | --- | --- |
|First contact|08:12:15 or16seconds|Two alternative source seconds; no statistical confidence interval|
|Greatest obscuration|09:18,11¼digits|Seconds unspecified; digits not an area percentage|
|Final contact|A few seconds before10:29|Exact time and numerical bound remain null|
|Three spot emersions|09:45:22,09:47:35,09:48:38|Transcribed; spot geometry not modeled|

The first spot time is explicitly called true time. Extending local apparent solar time to the eclipse contacts is a diagnostic interpretation; no clock instrument/calibration error distribution is recovered in these two pages. The account also describes qualitative thermometer and barometer behavior, without numerical environmental readings. These are not converted into physical measurements.

## Fixed-location calculation

The [executed script](../analysis/delisle1715_eclipse.py) uses the same pinned Astronomy Engine2.1.19 and historical Earth-rotation model as the London audit. Its fixed point48.8462°N,2.3372°E,height0m is a selected approximate Paris Luxembourg-area location, not an authenticated historical instrument survey. Identification of the printed Luxembourg with this Paris site is retained as a contextual assumption. No location, clock offset or event date is fitted.

The [numerical results](../data/delisle1715-results.json) give a **partial** eclipse and these local apparent times:

|Contact|Model time|Comparison permitted by source|
| --- | --- | --- |
|First contact|08:11:47.295|27.705-28.705s earlier than the two printed alternatives|
|Peak|09:17:34.672|25.328s before the nominal09:18:00 label; source seconds/rounding unknown|
|Final contact|10:28:20.841|39.159s before10:29:00; source's actual endpoint remains unspecified|

Only the first comparison is a difference from reported seconds. The other two compare nominal reference labels; they do not establish measured residuals, uncertainty intervals or a successful precision fit. All18 declared site/height variants (latitude±0.010°,longitude±0.020°,height0/50m) remain partial. Those ranges are selected stress variants, not survey confidence bounds.

The model's obscuration is0.938960 of solar disc area. Delisle's11¼digits is a different quantity describing extent; dividing by12 would not provide an observed disc-area fraction. Their numerical resemblance is not used as validation. The script does not reconstruct spot positions, the historical projection geometry, a digit-to-area conversion or instrument accuracy.

## What this adds and does not add

The London model is total while this fixed Paris model is partial, matching the reports' qualitative distinction. Delisle supplies a different observer and context, rather than another account from the London platform. That advances spatial comparison, but the same eclipse, Academy volume and modern model remain shared dependencies. Original observation notes, instrument location, calendar/custody authentication and independent model validation remain outstanding.

The retrospective diagnostic does not prove all chronology, identify a timeline break or establish the catastrophe/rewriting sequence. The source times are not silently reconciled, and an imprecise endpoint is not converted into an exact observation. All twenty objectives remain active; no independent scientific review or prospective prediction success is claimed.

Next authenticate the Luxembourg observing position and clock convention, recover original notes, and inspect Maraldi's separate observation before adding it to a declared regional comparison. Separately sourced events and held-out chronology transformations are still required.

Reproduce with `python analysis/delisle1715_eclipse.py`. Historical UT labels use the library's modern `Z` formatting; atomic UTC did not exist in1715.
