# Kino's route account: observations, reports and inference

Research draft, 2026-10-08. Source S39; case C005. No independent review.

## Source and inspected scope

Kino's *Historical Memoir of Pimería Alta*, volume I, translated and edited by Herbert Eugene Bolton (1919), is available as a [scan](https://www.fondazioneintorcetta.info/pdf/biblioteca-virtuale/documenti_1/PimeriaI.pdf) and [Internet Archive text](https://archive.org/download/kinoshistoricalm01kinouoft/kinoshistoricalm01kinouoft_djvu.txt). Printed pages 316-317, 341 and 343-344 were visually checked (PDF pages 320-321, 345 and 347-348). Adjacent route text on pages 315 and 340-342 and editorial discussion on pages 24-25 were read as OCR. The manuscript itself remains unchecked. Selected Spanish printed passages were subsequently compared below.

This is a later translation of a historical account attributed to a participant. It is not a newly authenticated field notebook. Bolton describes manuscript corrections, multiple hands and editorial changes, including modernized punctuation and capitalization. Those are the editor's reports, not manuscript observations made by this investigation.

## What the account actually distinguishes

| Reported date | Locator | Evidence in the translated account | What it does not establish |
| --- | --- | --- | --- |
| 21 November 1701 | pp. 316-317 | Kino describes crossing the Colorado on a raft with help from the Quiquima captain and others, then traveling about three leagues. River width is estimated at about 200 varas. | A measured modern coordinate, precise river width, or a complete traverse to the Pacific coast. |
| 21 November 1701 | p. 317 | Visitors bring blue shells and information about the opposite coast and the gulf's end. | Kino personally observing the shell source or completing their reported journey. |
| 3 March 1702 | pp. 340-341 | Noon solar altitude reported as 52 degrees; south declination 6.5 degrees; derived latitude 31.5 degrees. | Calibrated instrument accuracy, a historically validated solar declination, longitude, or an exact modern site. |
| 10 March 1702 | p. 343 | Another raft crossing is deferred because of illness and boggy banks that impede horses; the party spends the night near the estuary. | A successful crossing on this date. |
| 11 March 1702 | p. 344 | Kino reports sea to the east and continuous land visible south, west and north; he interprets this as proof of the land connection. | A surveyed coastline or independent verification of the claimed viewing distances. |

These distinctions matter. A successful crossing in 1701 and a deferred crossing in 1702 are different episodes, not necessarily a contradiction. Local knowledge, interpreters, navigation assistance and cultivated settlements are part of the account; the terrain was inhabited and known to its residents. The named group labels are those used by this edition, not newly verified modern identifications.

## Quantitative and chronological limits

The printed latitude arithmetic is internally consistent as `90 - (52 + 6.5) = 31.5` degrees. Bolton's footnote 467 comments on awkward English complement wording; the Spanish comparison below requires revising our earlier description of that footnote as simply a clarification. This checks arithmetic only: historical solar-table provenance, observation date/calendar, horizon correction, instrument error and site identification still require separate tests. No longitude or metric conversion of leagues/varas is invented. [Structured observations](../data/kino-route.json) preserve these limits.

The March 1702 observations are later than the 1698-1701 discovery period printed on the inspected map. They cannot silently be treated as observations underlying a map completed in 1701. Establish the map's revision/transmission history before assigning them that role.

## Consequence for the hypothesis

This supplies a specific observational account behind the peninsula interpretation and makes a purely pictorial comparison insufficient. A proposed historical strait must explain the dated route and sighting testimony as well as the map. However, Kino's map and Kino's narrative share an author; their agreement is not two independent observers. Residents' statements survive here through Kino and a translator, rather than as independently preserved interviews.

The next tests are manuscript comparison, broader edition collation, route identification with explicit spatial uncertainty, and independent dated terrain or coastal evidence. These pages do not report a strait closing, measure a catastrophic displacement, or establish a global chronology change. They also cannot rule out every geographically and temporally unspecified former waterway.

## Spanish printed comparison and a correction

Source S40 is [*Las misiones de Sonora y Arizona*](https://www.fondazioneintorcetta.info/pdf/biblioteca-virtuale/documenti_1/Favores.pdf), Archivo General de la Nación, volume VIII, paleographic version and index by Francisco Fernández del Castillo, with biographical material by Emilio Böse. Its title page prints México, Editorial Cvltvra, 1913-1922; retain that imprint range rather than invent a single publication date. The title and printed pages 148, 161-162 were visually checked (PDF pages 7, 232, 245-246).

| Passage | Spanish printed text | Comparison with S39 |
| --- | --- | --- |
| Latitude calculation, p. 161 | “el cumplimiento a 90 grados son 31 grados y medio” | Literally the completion **to** 90 degrees is 31.5 degrees. English p. 341 says “The complement of ninety degrees,” then footnote 467 criticizes that wording as Kino's. The Spanish edition already expresses the arithmetically sensible relation. |
| Informants' journey estimate, March 9, p. 162 | “no distava mas que 8 o 9 o 10 dias” | English p. 343 gives “not more than eight or nine days distant.” Preserve the extra ten-day alternative; neither version supplies a surveyed distance. This is distinct from the November report on English p. 317. |
| Crossing, p. 148; deferred crossing and sighting, p. 162 | Raft crossing, Indigenous assistance, later deferral and sea-to-east/land-to-other-directions claims present | Selected core observations agree in substance. This is an edition comparison, not a second witness to the events. |

Short transcriptions normalize line breaks only. Interpretation of the Spanish has not received independent linguistic review. The latitude wording differs at the edition/translation level; without the manuscript and editorial production records, responsibility cannot be assigned definitively. Our previous wording gave too little attention to this distinction. Neither discrepancy changes the reported 31.5-degree result or establishes intentional alteration, a chronology break, or geographic upheaval.

## Retrospective solar-declination calculation

Source S43: [JPL Horizons manual, quantity 2](https://ssd.jpl.nasa.gov/horizons/manual.html) and [API documentation](https://ssd-api.jpl.nasa.gov/doc/horizons.html). The request uses Sun (10), Earth center (500@399), airless apparent declination of date, Gregorian calendar and hourly UT samples from 3 March 1702 00:00 through 4 March 00:00. The response identifies DE441; its historical UT labels mean UT1. This is an explicitly assumed calendar and a sampled one-day window, not an identified local noon or historical observer location.

The 25 samples range from **-7.07571 to -6.69282 degrees**, versus the account's **-6.5 degrees**. Absolute differences are **0.19282 to 0.57571 degrees**. Those bounds describe the selected samples, not a confidence interval or a measured instrument error. No sampled value exactly reproduces the reported declination. The historical value is nevertheless in the same broad seasonal neighborhood; that qualitative observation is not a statistical acceptance decision.

The original solar table, calendar convention, observation time, instrument uncertainty, horizon/refraction treatment and use of solar limb versus center remain unresolved. Do not treat the model output's printed precision as historical measurement precision, or silently correct the reported 52-degree altitude or 31.5-degree latitude. A geocentric declination calculation is not a reconstruction of the field observation. Seasonal similarity also cannot establish the year, manuscript authenticity, geographic upheaval or intentional rewriting.

The [saved response](../data/kino-horizons-response.json) preserves the returned text inside JSON; its SHA-256 refers to that extracted UTF-8 text. [Structured results](../data/kino-solar-check.json) retain every sample and exact request parameters. Run `python analysis/kino_solar_check.py` to verify parsing and arithmetic against the saved response; `--fetch` requests a new response and replaces these two generated artifacts. This retrospective check is not a public preregistration or independent historical review.

## Subsequent transmission comparison

The [1776 geographical article](ENCYCLOPEDIE-CALIFORNIE.md), S189 p.133, denies Kino crossed the Colorado. This conflicts with the reported November 1701 crossing above; recover the report available to that writer and the underlying manuscript before assigning cause or intent.

## Gobien passage now recovered

The [1705 epistle audit](GOBIEN-CROSSING.md) finds Rio Azul in the explicit crossing clause where Buache writes Hila. The following Colorado crossing is strongly indicated by context, placing the claim in an early printed account, with no exact day or independently authenticated route. Alcazar is named as map intermediary; custody and original itinerary remain open.

## Map-label cross-check

The [river-network inspection](KINO-RIVER-NETWORK.md) finds Azul/Bleue and Hila/filasse on separate joining branches. This corroborates the distinction in Gobien at the level of shared depiction, not independent terrain observation. Buache changes the named branch; actual itinerary, modern identification and reason for substitution remain open.

## Manuscript retrieval path

The [manuscript audit](KINO-MANUSCRIPT.md) records S192 institutional reproduction locators and Bolton's explicit editorial interventions. Original pages remain uninspected; differing extent descriptions do not establish missing pages.

## Provisional manuscript lookup anchors

The Spanish edition explicitly supplies original-foja markers. The [checked concordance](KINO-MANUSCRIPT.md#edition-provided-manuscript-markers-recovered) locates the November crossing around 165-166 and March observations around 183-186. These markers await verification against original images. March 2 text recalls the previous November crossing; local river information is separately scoped in the [network audit](KINO-RIVER-NETWORK.md#march-1702-narrative-adds-an-information-source-limit).
