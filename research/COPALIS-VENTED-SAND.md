# Copalis vented sand: observations that a physical model must explain

2026-10-09. C004 / S244. Selected original compiled field tables extend the regional sediment investigation. Reported intrusion geometry is separated from the cause of venting and the age of deposition.

## Inputs and scope

The unchanged USGS2022 [plain archive](../sources/originals/cascadia/field-release-2022/plain.zip) contains Table18 observations, Table3 stratigraphy and Table6 radiocarbon records. Its guide explains the fields and treats the Copalis venting as about1,000 years old. The [script](../analysis/copalis_vented_sand.py) checks the acquired ZIP hash, preserves source rows and calculates only descriptive counts and coordinate separations. [Results](../data/copalis-vented-sand.json) retain all68 observations, the nine exact-label stratigraphic matches, depth exceptions and ten soil-Ws assays. [GeoJSON](../data/copalis-vented-sand.geojson) preserves source WGS84 points with reported/unknown fields; it is not a new field survey or a reconstructed event footprint.

The1992 paper cited by the guide remains a retrieval target for its original figures and note added in proof, DOI10.1029/91JB02346. A bounded search located publisher abstract/metadata, not an inspected full paper. Its unavailable figures are not treated as visually checked here.

## What was observed or reported

Table18 has **68 named records**:46 borings,18 trenches and4 bank observations. The guide's overview says67 observations; the actual file has67 numeric thickness entries and one unknown entry. Whether the guide counted only numeric entries is unverified. The records span1986–1992 rather than exclusively the1991 work described in the brief section.

- Thickness is recorded numerically in67 rows:64 positive, three zero, and one additional unknown row **E22**. Recorded values range0–115cm; median20cm includes the three zeros. These are selected locality values, not an areal mean or measured sediment volume.
- **11 rows mark a vent observed.** The other57 have blank Vent fields, which cannot be read as vent absence. The guide defines Observed as one or more dikes cutting soil Ws.
- **T7 and SL86-66** have observed venting with zero recorded sheet thickness. A vent/dike can therefore be reported without a positive extruded-sheet thickness at that observation. **E26** is another recorded zero but lacks a vent flag; **E22** has an observed vent and unknown thickness, explicitly requiring a pit/trench to estimate thickness away from probable venting.
- **D21, E31** reports a sill and crater over a dike containing rounded wood; **A31** reports sills/dikes; **SL86-66** reports irregular intrusions. **T11** reports mud clasts up to10cm, and **A40** clasts up to25cm.
- Several trench values are approximate or summarize ranges: T10 records35cm but comments0–35cm; T5 records31 with0–31; T16 records20 with10–20. A point maximum is not uniform sheet thickness. No measurement error is invented.

These are compiled observations checked against field notes by the source compiler. This investigation has not inspected the original outcrop drawings, trench photographs or physical exposures.

## Intrusion and surface deposition are different model requirements

The guide describes soil **Ws** at the stratigraphic position of W. Ws was observed beneath vented sand and reportedly merges with Y where that sand is absent. This led the source to infer little or no subsidence during venting. The guide separately labels Y's later subsidence as1700. Field correlation and that chronology are inherited claims to audit, not independent dates established here.

At T5 and T15, Table3 reports continuity between a sand dike and extruded sand. At T6 it reports a dike continuous with a crater and extruded sand. If these relationships are authenticated, a model that supplies only sediment transported across the surface is incomplete: it must also explain the reported subsurface intrusion, vent/crater geometry and entrained material. Intrusion does not uniquely identify an earthquake trigger.

The guide explicitly treats faulting or folding of aquifers deeper than35m as **speculative** and says the sand was difficult to explain by shaking-induced liquefaction. Neither a confirmed deep aquifer source nor a confirmed alternative flood mechanism follows. Competing models need source sediment, pressure/head, permeability, confinement, rupture/vent geometry and timing. None has been fitted here.

## Do not build a section from unreconciled coordinates and depths

Nine Table18 FieldIDs match Table3 exactly. Seven have identical source coordinates. Two do not:

| FieldID | Table18 longitude/latitude | Table3 longitude/latitude | Diagnostic separation |
| --- | --- | --- | ---: |
| A31 |−124.1609,47.1204 |−124.1627,47.1197 |156.9m |
| A40 |−124.1625,47.1203 |−124.1626,47.1198 |56.1m |

Distances use an explicitly assumed sphere of radius6,371,008.8m; both tables belong to a release specifying WGS84. They are checks of source consistency, not surveys or datum corrections. It is not established whether coordinates identify different exposures, misplaced points or another source convention. FieldID association alone must not make these positions identical. Composite D21/E31 is retained without guessing an exact section match.

The guide defines LocSeq as successive soils from youngest/closest to modern ground downward, and Depth as metres below modern ground to the upper soil contact. Three reported sequences have decreasing depths for a later numbered soil:

| Locality | Source sequence/depth | Consequence |
| --- | --- | --- |
| T6 |Ws soil2 at0.9m; U soil3 at0.4m |Cannot use as a single monotonic vertical profile without resolving representative sections/relief or errors |
| T1 |U soil2 at1.8m; S soil3 at0.3m |Same limitation |
| A31 |Y soil1 at0.9m; Ws soil2 at0.5m |Same limitation |

Depth values are representative, and the guide warns of relief and differential settlement. Those possible complications do not automatically resolve these particular inversions. Preserve the source rows, retrieve the actual drawings and do not invent corrected depths or compute layer thicknesses by subtracting them. Ground depth is also not a measured amount of coseismic subsidence.

## Material ages and event ages remain separate

Table6 has **ten Copalis Ws determinations**: seven coded maximum limits (`mx`), two close maximum/minimum limits (`Cmxmn`), and one not readily applicable (`na`). Table4 describes crater-floor detritus as potentially slightly older or younger than the event. None of these ten is coded nearly equivalent to event time.

Examples worth tracing to original laboratory/field records:

- **T17A1/Beta48234**:1070±60 conventional radiocarbon yearsBP; used error108 after source multiplier1.8. A15-ring stick from the crater floor, split lengthwise. **T17A2/QL4577**:890±70, used error112; about ten crater-floor sticks. Same locality and context do not supply two independent exact event dates.
- **T15C/GX17309**:983±49, used error49; bark only, from roots/sticks in the top2cm of soil beneath sand. **T15B/USGS3103**:430±90, used error162; source flags it discordant and says it was not marked on the outcrop sketch. The adverse determination remains in the ledger; do not silently discard it or equate it with proof that venting was recent.
- **A40D/Beta22897**:700±50, used error90; a nearly vertical wood piece interpreted as impaled/fallen, code`na`. It is not an automatically usable sediment-deposition age.

Conventional radiocarbon ages use BP=before1950CE and are not calendar ages. Source calibrated endpoints, errors, fractionation codes, materials and limiting relations are preserved unchanged. Reported-error multiplication agrees in all ten rows; this is arithmetic verification, not calibration reproduction, independent laboratory validation or a joint event interval. The regional Table7 W combination cannot be assigned to all Copalis Ws observations without testing correlation and sample context.

## Next discriminating work

Recover original1992 figures/sections and1991–1992 trench/boring logs; reconcile A31/A40 locations and the three depth-order exceptions. Inspect source-sediment grain size/composition and observed dike/sill/crater cross-sections before choosing a fluid-pressure mechanism. Audit material preparation and calibration for the ten Ws assays, including the flagged T15B and mixed crater-floor material. Keep this regional venting episode separate from Y-associated1700 sand, urban fill and fossil burial unless physical correlations and timing demonstrate a connection.

No worldwide event, precise venting date, pressure source, flow duration or chronology break is established. The gain is a more demanding, source-linked physical comparison that includes unresolved observations and adverse data.
