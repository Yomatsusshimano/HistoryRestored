# Wildlife locality coverage

2026-10-08. Retrospective source audit; no independent scientific review.

Open the [locality map](../data/wildlife-localities.geojson) and select a point for its source, coordinate role and dating audit. The [coverage ledger](../data/wildlife-map-coverage.json) includes all nine selected cases, including those without points. Rebuild both with `python analysis/build_wildlife_map.py`.

This is a map of reported research locations, not a map of contemporary animal ranges, places of death, a shared flood deposit or reconstructed coastlines. No migration or transport paths have been drawn. Age labels are kept in the linked audits because mineral deposition, bone mortality, DNA-bearing sediment and collection dates cannot be plotted as equivalent event ages.

| Case | What the plotted coordinates represent | Number of features | Principal boundary |
| --- | --- | ---: | --- |
| C003 Arctic camel | Published regional approximation shared by Beaver Pond and Fyles Leaf Bed (S13, Table S3 caption) | 1 | Not a precise camel specimen location or two independently surveyed sites |
| C013 Arctic hyena | CRH 11A collection locality (S24, p.3) | 1 | Reworked river-bar collection, not original source bed or death location |
| C014 Camp Century plants | CC 63-66 catalog drill site (S134) | 1 | Not individual plant growth positions or the specimens' present storage location |
| C015 Coyote Canyon | Seven OSL sediment sampling positions (S32, Tables 2-4) | 7 | Includes flood and loess contexts; not seven animal findspots or seven proven events |

The ten features represent four cases. Some Coyote coordinates coincide and will overlap at map scale. Point count does not measure independent evidence. Reported decimal places are preserved without interpreting them as measured precision. Source geodetic datums and horizontal uncertainties are unresolved; the display uses the supplied longitude/latitude without transformation. Do not use this map for metre-scale distances, excavation planning or hydraulic elevation controls.

## Missing coordinates remain visible

C009 Yukon sedimentary DNA, C011 Haitian sloths, C012 muskox, C016 Thistle Creek horse and C022 Campo Laborde have no audited global coordinates in this map. Their named localities remain in the coverage ledger. They have not been geocoded to town centres, country centres or nearby dated samples. Lack of a plotted point means missing metadata in this audit, not absence of fossils in that region.

In particular, the Dominion Creek ash-study coordinates must not be substituted for the Thistle Creek horse. Campo Laborde's excavation-grid offsets likewise cannot become global coordinates without an established survey origin and orientation. Muskox geographic groups require specimen-level recovery before they can support corridors.

## Camp Century location and custody

The [NSF Ice Core Facility catalog](https://icecores.org/inventory/camp-century) (S134) lists CC 63-66 at 77.1666667, -61.1333333. It distinguishes its retained ice sections from deep basal material held at the Niels Bohr Institute, Copenhagen. This provides a concrete custody lead for the plant-bearing sediment; it does not authenticate the complete chain of handling or imply that a new sample has been obtained.

## Consequence for a common-event model

The mapped sites establish geographic separation only at the stated resolution. They do not establish a connected depositional horizon. A common later-deposition explanation still needs sediment provenance, age and transport evidence at each site; a mortality explanation must use specimen ages rather than these site coordinates. The [wildlife comparison](WILDLIFE-COMPARISON.md) retains those separate tests.

Next recover missing original locality tables and survey metadata, then attach dated environmental evidence to the same stratigraphic units. No preservation exception, former shoreline or common event is inferred from the present gaps.
