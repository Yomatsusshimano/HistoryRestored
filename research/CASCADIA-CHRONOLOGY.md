# Cascadia: testing a link between trees and documents

## Correction and within-root comparison, 2026-10-08

**Our previous GF2RTC transcription contained seven wrong values.** Enlarged 200-dpi portions of S61 PDF page 3 exposed the errors. These are our digitization mistakes, not changes in the original measurements. The earlier statement that a visual check had been completed was insufficient assurance of accuracy. Commit 9426ad1 is superseded for these values:

| Source-assigned year | Previous width (µm) | Corrected width (µm) |
| --- | ---: | ---: |
| 1461 | 675 | 764 |
| 1463 | 1092 | 902 |
| 1586 | 1397 | 1239 |
| 1602 | 1539 | 1639 |
| 1618 | 411 | 657 |
| 1619 | 657 | 411 |
| 1676 | 556 | 956 |

The [data record](../data/cascadia-width-extract.json) retains old and corrected values and their locators. A renewed enlarged-image check covered the full GF2RTC series. Independent transcription review remains absent. No calendar-dating result was based on the erroneous values.

GF2RTB is now fully transcribed from PDF pages 3–4: 332 widths, source-assigned 1368–1699. Together with corrected GF2RTC and the ten GF2RTA values, the record contains 642 widths. The -9999 markers remain outside measurement arrays.

The executable [within-root comparison](../analysis/cascadia_radius_comparison.py) uses the shared 300 published year labels, 1400–1699. [Results](../analysis/cascadia-radius-result.json) give Pearson r=0.502930 for widths and r=0.473680 for their 299 successive annual differences. These are descriptive associations between related radii. They do not test calendar placement, supply independent tree evidence, or reproduce the article's comparison with Ozette. No significance probability is reported. Both calendars could shift together without changing either correlation.

The next useful dating step remains acquiring the external reference chronology and auditing all contributing radii and trunk measurements, with alternate placements and preprocessing explicitly preserved.

## Measurement supplement recovered, 2026-10-08

[Jacoby, Bunker and Benson (1997), S60](https://web.njit.edu/~dbunker/publications/Jacoby%20etal%2097%20Geology.pdf), printed pp. 1001–1002, reports 15 disturbed trees, five apparently undisturbed trees and fourteen unclassified trees. Responses vary in direction and timing; the narrowest ring need not date the disturbance. Its killed-cedar comparison searched placements from 1400 to 1740 against an Ozette chronology, reporting r=0.21 over 300 years and t=3.7. Other alignments had slightly higher correlations but shorter overlaps and lower t values. Those comparisons have not been rerun here. The article identifies GSA repository item 9756 as its measurement supplement.

The [original supplement, S61](https://doi.org/10.1130/9756) was located through the public Figshare API and downloaded. The file contains **45 PDF pages**, while both cover and catalog describe 37. This discrepancy is retained, not interpreted as missing or fabricated measurements. The PDF has no extracted text in its opening pages. Cover, methods, killed-cedar tables on PDF pp. 3–4, and selected later tables on pp. 43 and 45 were visually inspected. This is not a full-page audit.

The methods note specifies micron units and decadal layout, with site/tree/core identifiers. It describes within-tree, within-site and between-site crossdating using anatomy as well as widths. Thus these are published, already calendar-assigned measurements, not blind calendar-independent observations.

[Selected transcription and acquisition record](../data/cascadia-width-extract.json) preserves complete GF2RTC and GF2RTB series and the 1690s row of GF2RTA, with the following printed -9999 marker kept separately. It is not a negative width or an additional 1700 observation. These three related root-radius series must not be counted as three independent trees. Their precise crosswalk to S19 specimen identifiers remains to be verified.

The full GF2RTC transcription was checked visually against PDF page 3. Each of its thirty decadal rows contains ten measurements; the last decade matches our earlier extraction. These are transcription checks, not dating verification. That earlier stage contained 320 stored widths; the correction and extension above supersede it.

A [bounded reference-data search](../data/cascadia-reference-search.json) retrieved the first three header lines from 92 Washington chronology files in NOAA’s public USA chronology directory (filenames matching `wa` + digits + `.crn`). None contained Ozette, Jozsa or Parker, case-insensitively. This excludes neither suffix variants nor renamed deposits, other directories or alternate archives. No substitute reference was selected merely because it is geographically nearby.

Next: transcribe and check all killed-cedar series and obtain the Ozette reference measurements; preserve alternate placements, overlap lengths, preprocessing, serial correlation and multiple-placement testing. A date assigned in the source table does not independently reproduce the original crossdating. Anatomy, bark preservation and field association require their own evidence. The supplement is linked rather than redistributed; Figshare lists CC BY-NC 4.0. Local retrieval hashes preserve file identity.

Research draft, 2026-10-08. C004 remains without independent review.

[Yamaguchi et al. (1997)](https://doi.org/10.1038/40048), accessed through an [author-hosted copy](https://web.njit.edu/~dbunker/publications/Yamaguchi%20etal%2097%20N.pdf), provides a sample-level test. Table 1 on printed page 923 was visually checked. The [transcription](../data/cascadia-rings.json) retains all eight usable root dates: seven end in 1699; CP-791 ends in 1708. Six preserve latewood supporting death between August 1699 and May 1700. The authors suggest that the exceptional root's height delayed mortality; that explanation is not independently tested here.

This is a seasonal constraint, not a tree-ring determination of January 26. Matching uses shared reference trees and a latest possible date constrained by radiocarbon. Independent replication must test the correlations and those assumptions, not merely count agreeing trees.

The [published correction](https://doi.org/10.1038/37029) clarifies a conditional argument about maximum rupture length if the dates excluded January 1700. It does not supply new tree measurements. Both versions remain linked; the original final paragraph should not be used uncorrected.

## What remains to establish

The exact-day inference requires a separate audit of Japanese documents, calendar conversion, arrival-time uncertainty and tsunami propagation. Raw ring widths, field context and delayed mortality also need checking. The accessible evidence supports investigating a regional earthquake/tsunami; it cannot transfer the same date to unrelated urban fill or fossil deposits.

This case can anchor a comparison cohort only with its scope preserved. For each proposed additional site, require its own dated event horizon and a feasible physical connection. A common-event claim must survive those comparisons rather than acquire an event date merely by resemblance.

Initial USGS report downloads returned 403; the attempted supplement timed out. The author-hosted article allowed progress despite those failures. No full-paper copy is redistributed here. Rendering emitted font-substitution warnings; the inspected table's sample IDs, years and latewood marks remained legible. Raw-statistical replication has not been performed.

## Japanese records: selected reproductions now inspected

Source S44 is the **2015 second edition** of *The orphan tsunami of 1700*, retrieved from a [Miami University hosted copy](https://moodle.glg.miamioh.edu/brudzimr/classes/pp1707.pdf). This is distinct from the 2005 publication metadata in S04. The PDF includes duplicated/off-page text from spreads; visual inspection controls our core page locators. Printed pages **38-39, 42-43 and 52-53** were rendered and checked (PDF pages 48-49, 52-53 and 62-63). These contain reproductions with supplied transliteration and translation. Physical manuscripts and independent Japanese paleography remain unreviewed. The book identifies separately owned images, which are not republished here.

The Kuwagasaki entry in **Morioka-han Zassho** reports nighttime waves, escape to hills, 13 houses destroyed by water, and 20 burned. It also records relief rice for 159 people and requests for shelter timber. These are specific reported losses and responses, not sediment measurements. Its eighth-day nighttime “hour of nine” is interpreted by the report as around midnight. The surrounding year/month context is needed; the excerpt alone is not a modern timestamp.

### Preserve the month discrepancy

The **Moriai-ke Nikki kakitome cho** account for Tsugaruishi, reproduced on page 52, gives Genroku year 12, **month 11**, days 8-9. It describes coastal flooding and explicitly says no earthquake occurred. That absence concerns local shaking, not earthquakes everywhere. Its account of the Kuwagasaki fire is hearsay, so it is not another independent direct observation of that fire.

Page 53 argues that month 11 should be **month 12**. The argument is more specific than simply making tsunami reports agree: an adjacent heavy-snow entry is also one month early relative to the report's cited Morioka and Hachinohe weather records. This makes a repeated copying error a testable explanation. Those underlying snow records have not been independently inspected here. We retain the original month, proposed correction and rationale separately in the [document ledger](../data/cascadia-japanese-records.json). Neither silent correction nor automatic inference of deliberate fabrication is justified.

### Calendar arithmetic and earthquake inference are separate

Page 42 describes an intercalary ninth month in Genroku 12. It gives Genroku 12.11.1 as Gregorian 21 December 1699 and month 11 as 30 days. Conditional date addition is consistent: 30 days plus seven elapsed days gives **27 January 1700** for month 12 day 8, followed by January 28 for day 9. This arithmetic was executed; the historical anchor and calendar table have not been independently reconstructed.

Page 43 explains that the numbered day began at dawn and the nighttime hour of nine corresponds to midnight. It then derives an approximate **9 p.m. January 26** Cascadia origin from Japanese arrival near midnight January 27-28, about ten hours of ocean travel, and a 17-hour difference expressed in modern time zones. This is an inferred earthquake time, not a date directly observed in Japan. The report allows an earlier origin if damaging waves lagged the leading wave by one or two hours. It also explicitly notes ambiguity in Tanabe's dawn-of-eighth wording; agreement with the ninth is an interpretation, not identical wording across every account.

The seasonal tree window and documentary timing can therefore be compared, but the exact-day claim carries calendar, transmission, arrival-time and propagation assumptions. Next inspect the snowstorm comparison entries and historical calendar references, then reproduce the travel-time calculation with uncertainty. Nothing in this tranche dates unrelated fossil deposits or establishes a worldwide mud-flood horizon.

## Tanabe: the arrival-order conflict remains visible

Printed pages **84 and 86-87** of S44 have now been visually inspected (PDF pages 94, 96-97). Page 86 reproduces the *Tanabe-machi daichō* entry with transliteration and supplied translation. Its first column says the eighth day and dawn; its opening word inherits the year and month from a preceding entry. That preceding entry has not been inspected here. The passage reports water entering a government storehouse in Shinjō, damage to fields and crops in Atonoura, and water reaching Horidobashi along a moat near the writer. Some clauses explicitly relay reports, so these are not all established eyewitness observations.

The note to the word **abiki** warns that it describes unusual seas without identifying a cause. The word alone cannot decide between tsunami, tide or weather-related water movement. Page 87 shows water damage to the volume; neither its date nor its cause is independently established. It would be circular to treat the damaged paper as physical evidence of this particular tsunami.

| Reading retained | Conditional Gregorian date | Consequence under the report's nominal earthquake time |
| --- | --- | --- |
| Dawn at the start of the eighth day | January 27, 1700 | Earlier than the proposed earthquake after conversion to Japan time; cannot be its arriving tsunami under these assumptions. |
| Following dawn, interpreted as the ninth for agreement | January 28, 1700 | Later than the proposed earthquake; causal ordering is possible, but source and travel-time fit are not established by order alone. |

The arithmetic is explicit: January 26 at 21:00 in the report's illustrative Cascadia time, plus its 17-hour offset, is January 27 at 14:00 in Japan. Dawn that same January 27 precedes even noon, hence precedes the nominal source earthquake. No exact dawn minute or confidence interval is assigned. An origin a few hours earlier, as discussed on page 43, does not by itself move the source before that morning's dawn. The discrepancy requires investigation of wording, dating or the proposed event association; it must not be erased by automatically selecting the agreeing branch.

Page 84 identifies official *Daichō* and private *Mandaiki* records connected to the Tadokoro family. It reports a librarian's assessment that extant *Mandaiki* volumes including 1700 are later copies, probably produced under a mayor born in 1758 and deceased in 1818. These life dates are not precise copy dates. Two series within that transmission history cannot automatically be counted as two independent observers. The parallel passage itself and the preceding dated entry are next retrieval targets, alongside independent linguistic assessment of the day-boundary wording. This conflict narrows the precision of the documentary argument; it does not on its own overturn the separate tree-ring evidence or establish intentional fabrication.

## Flood heights: conditional scenarios, not measured watermarks

S44 printed pages 88 and 90-91 were visually checked (PDF pages 98, 100-101). Six illustrated reconstructions convert reported flooding into heights **above ambient tide**. The [component ledger](../data/tanabe-height-scenarios.json) preserves each scenario; [the arithmetic script](../analysis/tanabe_height_check.py) can be run with `python analysis/tanabe_height_check.py`.

| Scenario | Component sum, metres | Printed total, metres | Main condition |
| --- | --- | --- | --- |
| Shinjō A | 2.1 | 2.1 | Minimal foundation and assumed storehouse freeboard above highest tides |
| Shinjō B | 4.0 | 4 | Inland low-ground storehouse and 1.2 m inland decline inferred by analogy with 1960 |
| Shinjō C | 5.4 | 5.4 | Orally remembered site at 4.1 m above TP, plus 1 m net subsidence and tide adjustment |
| Tanabe A | 1.6 | 1.6 | Assumed field elevation and 0.3 m flow depth sufficient to damage grain |
| Tanabe B | 2.6 | 3 | Greater flow depth and freeboard; printed total is compatible with whole-metre rounding, not explicitly explained |
| Tanabe C | 3.3 | 3.3 | Flood assumed near moat rim, modern ground about 2 m above TP, plus net subsidence and tide adjustment |

The original components are assumptions or later survey/context values, not direct measurements of the 1700 crest. All six add 0.3 m because the source assumes ambient tide 0.3 m below contemporary mean sea level. The tide calculation uses modern coefficients and astronomical components (p. 83, extracted text); it has not been rerun. Arrival-time interpretation and tide correction therefore are not independent evidence. TP is described as near mean sea level, not an exact identity of every historical datum.

The 5.4 m estimate depends on whether the high-ground site remembered in oral tradition held the building flooded in 1700. The report explicitly questions that identification: records of the 1707 tsunami mention two government storehouses lost in Shinjō (p. 89, extracted text). Likewise, water reaching Horidobashi does not itself measure its height against the moat rim; page 90 calls the rim-based estimate speculative. These alternatives must not be averaged into a measured height or treated as a confidence interval.

The one-metre land-level correction also has mixed provenance. Page 91 presents about 0.4 m of subsidence measured for 1946, an estimate for 1854, and subsidence reported for 1707 with unknown amount. It extrapolates an uplift rate of 0.8 mm/year from 1967-1995 tide-gauge data at Shirahama to earlier intervals. Regional maximum earthquake displacements shown on the same page are not Tanabe measurements. Original levelling, tide coefficients and the full land-motion history remain unchecked here.

Before using these heights to calibrate a physical catastrophe model, establish building identity, historic ground geometry, datum relationships and plausible land-motion/tide uncertainty. A source can supply evidence of flooding while leaving substantial uncertainty in the reconstructed height and cause. No global event footprint or new hydraulic reconstruction follows from these six arithmetic checks.
