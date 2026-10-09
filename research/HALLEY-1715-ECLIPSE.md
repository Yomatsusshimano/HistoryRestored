# Halley's eclipse account and a conditional chronology test

2026-10-09. C026 adds an astronomical chronology case. The [preserved18-page scan](../sources/originals/astronomy/halley1715/halley1715.pdf) of Halley's report is1707230bytes, SHA256`a344be5d98d0206566d6a752fe5fefaed2ab88647ae5c2243bcd0b3c2a6a52bd`. PDF1-5/printed245-249 were visually inspected; the first page's printed number is clipped. Other regional observations remain unaudited. The [acquisition manifest](../data/halley1715-acquisition.json) records the [Archive download](https://archive.org/download/paper-doi-10_1098_rstl_1714_0025/paper-doi-10_1098_rstl_1714_0025.pdf) and publisher-deposited metadata.

Crossref identifies volume29, issue343, pp.245-262 and publication May31,1715. The DOI`10.1098/rstl.1714.0025` contains1714; that identifier substring is not an observation-year measurement. The article title says April22, last past. Neither metadata nor this digital surrogate independently authenticates the original manuscript's age or custody.

## Observations and time conventions

The report places the observation at the Royal Society house in Crane Court, Fleet Street, London. It describes a mean-time pendulum clock followed by checks against apparent solar time using a quadrant. On the eclipse morning it reports the clock14seconds fast. The [observation ledger](../data/halley1715-observations.json) keeps corrected values separate from clock readings.

|Contact|Reported corrected local apparent time|Model local apparent time|Model minus report|
| --- | --- | --- | ---: |
|First partial contact|08:06:00|08:05:05.193|−54.807s|
|Totality begins|09:09:03|09:08:12.180|−50.820s|
|Totality ends|09:12:26|09:11:38.374|−47.626s|

The source's totality endpoints differ by203seconds, agreeing with its stated3minutes23seconds. Its first-contact account is internally less straightforward: noticing a depression at08:06:30 clock time, estimating onset no more than5seconds earlier and subtracting the stated14second clock error yields08:06:11–08:06:16, rather than its printed08:06:00. This11–16second discrepancy remains unresolved; no source value is corrected to fit the model. The clock correction at totality's beginning,09:09:17minus14seconds, does reproduce09:09:03.

April22 is interpreted in the Julian calendar used in England before reform. The [official calendar-act text](https://www.legislation.gov.uk/apgb/Geo2/24/23) specifies the1752 change of year commencement and September date labels. This observation falls after March25, so the earlier year-start convention does not introduce an extra year here. [USNO calendar rules](https://aa.usno.navy.mil/faq/calendars) distinguish the leap-year systems. Executed Julian-day arithmetic gives **April22,1715Julian = May3,1715Gregorian**. Eleven days of label difference do not constitute eleven missing physical days.

## Executed model and sensitivity

The [calculation script](../analysis/halley1715_eclipse.py) uses [Astronomy Engine](https://github.com/cosinekitty/astronomy)2.1.19, retaining a module hash and all results in [the numerical ledger](../data/halley1715-eclipse.json). Its fixed observer is51.515°N,0.110°W,height0m: an approximate Crane Court-area diagnostic coordinate, not an authenticated survey. No location or clock offset is fitted to the observations.

Predicted totality is206.173seconds. Eighteen combinations of latitude51.505/51.515/51.525, longitude−0.130/−0.110/−0.090 and height0/50m all remain total, with durations204.315–208.027seconds. These are chosen sensitivity ranges, not measured positional confidence bounds. Contact residuals of roughly a minute remain visible; precise agreement has not been demonstrated.

Local apparent time is calculated as12hours plus the Sun's hour angle: Greenwich apparent sidereal time plus longitude/15 minus topocentric apparent right ascension, reduced modulo24hours. This avoids comparing a solar-clock reading directly with model universal time. The software's `Z`-formatted labels are modern representations of modeled historical UT; atomic UTC did not operate in1715.

The default Espenak-Meeus ΔT is10.325seconds at this event. A declared ±30/±60second stress test perturbs that model and restores the library function afterward. These offsets are not confidence bounds or calibrated corrections. Historical rotation models can themselves depend on historical observations; this calculation is not asserted independent of the eclipse-observation tradition. The [NASA catalog](https://eclipse.gsfc.nasa.gov/SEcat5/SE1701-1800.html) supplies a modern May3,1715total-eclipse cross-check but shares the ΔT approach. Its09:36:30TD greatest-eclipse entry describes the global event, not a London contact time or second historical witness.

|Added ΔT offset|Model duration|Totality-start residual|
| --- | ---: | ---: |
|−60s|194.028s|+28.712s|
|−30s|200.413s|−11.221s|
|0s|206.173s|−50.820s|
|+30s|211.369s|−90.114s|
|+60s|216.057s|−129.130s|

All five variants retain totality on the same converted date. Some perturbations improve the contact fit; none is adopted as a measured correction. The zero-offset variant reproduces the baseline duration to within0.001seconds, a software consistency check only.

## What the year-shift test establishes

For401integer offsets from−200through+200, the script preserves April22 in the Julian calendar and converts each shifted year normally. At the fixed observer, **only zero offset** produces a modeled local eclipse on the converted date. All other400offsets fail this specific day-and-place condition. The standard date therefore fits substantially better than these simple relabelings under the retained model assumptions.

This is a retrospective, selected test. It does not establish every historical date, exclude shifts outside the tested range, authenticate the printed report, or test transformations that also alter month/day, location or narrative. Other contacts, regional reports and model variations are dependent; they are not hundreds of independent confirmations. No worldwide event or historical-fabrication mechanism follows.

Next recover original custody and the remaining regional observation accounts, compare a higher-precision ephemeris, and test additional separately sourced astronomical records against explicit transformations. A chronology claim should identify its conversion and explain these anchors together. The full twenty objectives remain active; no independent review or prospective success is claimed.

Reproduce with `pip install astronomy-engine==2.1.19`, then `python analysis/halley1715_eclipse.py`. Source and observation hashes are retained; no external ephemeris download is required by this model.
