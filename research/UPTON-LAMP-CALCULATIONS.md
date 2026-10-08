# Upton's lamp observations and power calculations

Research draft, 2026-10-08. C007 remains SOURCED_DRAFT without independent review.

All five images of [N085171, S180](https://edisondigital.rutgers.edu/document/N085171), notebook N-79-08-22, microfilm 35:868, were visually inspected. Right-hand pages are 171, 173, 175, 177 and 179. Original images, public manifest and hashes are preserved in [structured records](../data/upton-lamp-records.json). The archive attributes the notes to Francis Robbins Upton and displays CC0 licensing. Page 171 is dated October 22, 1879; this does not establish when every later annotation was inscribed.

## Measurements and calculations are different evidence

Page 171 reports a thread initially 45 ohms when cold, about four candles in high vacuum, and apparently steady behavior for two or three hours before resistance became localized; it subsequently records 800 ohms cold. No numerical vacuum pressure, calibration, uncertainty or continuous trace appears here. This should not be merged with the later 113-ohm entry as though all numbers described one specimen.

Pages 173 and 175 contain thread-lamp voltage/resistance values, logarithmic arithmetic and estimates of lamps per horsepower. Page 175 explicitly associates 140 ohms with half an hour and approximately half a candle. These match the distinctive resistance sequence in Batchelor's [trial record](LAMP-TRIAL-RECORDS.md), making a shared test a strong possibility. No unique specimen identifier or independent experimental setup has been established. Agreement between two staff notebooks can corroborate reporting without constituting replicated experiments.

| Locator | Written voltage across/on lamp | Written resistance | Written output of calculation |
| --- | --- | --- | --- |
| p.173 | 26.5 volts | 113 ohms | 288 in the intermediate calculation; 114 per horsepower |
| p.175 | 31.3 volts | 140 ohms after half an hour | 310 ft lbs; 106 per horsepower; light about half a candle |

The separate 1.5- and 1.4-volt entries and factor 6.26 participate in earlier arithmetic on each page; their complete instrument/circuit interpretation remains unresolved. They are not silently treated as ampere readings. The values labelled across/on the lamp permit a conditional electrical-power check using P = V²/R, assuming paired operating readings and an effectively resistive load. That is a reconstruction, not a new measurement.

## Recalculation exposes a local discrepancy

Using the handwritten conversion factor 44.3 and horsepower denominator 33,000 inferred from the logarithmic calculations, the reconstruction is:

`lamp_count = 33000 / (44.3 * voltage**2 / resistance)`

The numerical constants are used as a historical calculation reconstruction, not a calibration of the instruments. They correspond approximately to foot-pounds per minute per watt and foot-pounds per minute per mechanical horsepower. The handwritten intermediate unit on p.175 omits a time denominator; that omission is retained rather than quoted as a complete power unit.

- Page 173 inputs give 6.215 watts conditionally, 275.31 in the reconstructed intermediate units, and 119.87 lamps per horsepower. They do not reproduce the written 288 and 114. Its two voltage logarithms appear as 1.4332, whereas log10(26.5) is 1.423246. That local difference could account for most of the discrepancy. It is not evidence that the actual voltage was another value, and other small handwritten/log-table differences have not been corrected silently.
- Page 175 inputs give 6.998 watts conditionally, 310.002 in the same intermediate units, and 106.451 lamps per horsepower, consistent with a rounded 310 and a whole-number 106. This arithmetic agreement does not validate the measurements or the assumed supply efficiency.

These estimates describe power allocation at low reported light output; they are not a demonstration that a complete generating/distribution system powered that many useful lamps. Generator and wiring losses, useful brightness standards and manufacturing yield remain outside this calculation. No candle-to-lumen conversion or commercial efficiency is inferred.

## Failures and attribution remain visible

### Follow-up: resistance may be calculated from the same inputs

The logarithmic layout before each written resistance is consistent with `R = V * 6.26 / u`, where u is the separate voltage entry (1.5 on p.173; 1.4 on p.175). This gives 110.593 and 139.956 respectively. The latter closely reproduces the written 140; the former again differs from 113. This supports a calculation-dependence interpretation but does not identify the physical 6.26 component, its units or the circuit. A 6.26-ohm reference resistance is a candidate explanation, not an established apparatus identification.

The [reproducible calculation](check_upton_calculations.py) saves [both conditional routes](../analysis/upton-calculation-dependence.json). Holding the written resistance fixed gives the earlier 119.87 and 106.45 estimates. Recomputing resistance from the apparent preceding ratio instead gives 117.31 and 106.42 lamps per horsepower. The different first-page results are not an uncertainty interval: they answer different conditional questions. Neither is a corrected measurement of the historical lamp. In the ratio reconstruction, P = V*u/6.26, so the two voltage readings and inferred resistance cannot be counted as three independent observations.

### Adjacent context: vacuum faults and other carbon tests

[N085165, S181](https://edisondigital.rutgers.edu/document/N085165), both images visually inspected, includes a Pump No.5 heading dated October 17 and a discussion of mercury handling, bubbles and vacuum loss on p.167. The archive cautiously associates that discussion with the pump; a continuous instrument history through October 22 is not established. These notes demonstrate recorded troubleshooting, not a numerical pressure for the later lamp.

[N085169A, S182](https://edisondigital.rutgers.edu/document/N085169A), its single image visually inspected, actually contains entries dated October 19 and October 21 on p.169, plus preceding text. The latter records a carbon stick, 9 ohms cold and 4 incandescent, followed by a melted platinum-wire failure. A bare number 23 is not assigned an inferred unit here. The October 19 entry describes light in vacuum and a pump break. These are different recorded tests, not an extension of the 13.5-hour thread-lamp duration. Catalog date October 21 does not replace the other visible date. [Image provenance](../data/upton-adjacent-records.json) preserves all three scans and manifests.

Page 177 records breakage and burnt leading wires for thread/lampblack experiments. Page 179 reports that the carbon spirals did not blacken the glass, without a defined observation duration or specimen denominator. The two statements can coexist: absence of visible blackening does not imply long life or freedom from electrical failure.

Upton adds a named participant and quantitative work to the development record. This is evidence of recorded experimentation and calculation, not proof of exclusive invention or an ownership chain. It does not validate the March metal-wire patent assertions. Next recover the circuit and instrument descriptions underlying the 6.26 factor and voltage entries, and establish specimen correspondence before pooling notebook observations. The date correction proposed for Batchelor's page 111 remains separate and unproven by these pages alone.
