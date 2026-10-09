# Willapa shoreline comparison: original-line audit and modern survey lead

2026-10-09. C004 / S251-S253 and S256. All eight stored apparent-marsh features were rendered against the unchanged 1922 raster using its world file. [The script](../analysis/willapa_marsh_panels.py) preserves unmarked and marked crops side by side. No alignment was fitted or manually shifted. [The panel ledger](../data/willapa-marsh-panels.json) records original pixel bounds, geographic bounds, IDs and image hashes.

## Original map correspondence

All eight panels were visually inspected. The traces generally follow drawn features, supporting their association with this raster. This is a qualitative check, not a measured trace error, ecological authentication or independent survey.

| Feature ID | Visually inspected source context | Remaining qualification |
| --- | --- | --- |
|14 |Small loop/short trace beside a hachured boundary |Tiny feature; whether its code describes an ecological boundary is unclear |
|38 |Long boundary with repeated short horizontal marks near Cove Point |Symbol meaning and survey/revision coverage need original legend/context |
|41 |Long similarly marked boundary near Stump and Tideland labels |Qualitative line correspondence; no tidal elevation reconstructed |
|42 |Marked boundary near Bay Center |Feature identity supported; precise ecological classification unresolved |
|44 |Very short horizontal line near Bay Center coastal junction |Only three vertices; no independently established marsh edge |
|49 |Boundary enclosing part of a dotted area labeled Grassy |Vegetation context visible, but it does not establish mean-high-water elevation |
|51 |Boundary around part of a dotted island area |Vegetation-like depiction; field ecology and tidal level unverified |
|125 |Short bent line near Bay Center |Small-feature coding uncertain; requires survey legend and revision context |

Panels: [14](figures/willapa-marsh-14.png), [38](figures/willapa-marsh-38.png), [41](figures/willapa-marsh-41.png), [42](figures/willapa-marsh-42.png), [44](figures/willapa-marsh-44.png), [49](figures/willapa-marsh-49.png), [51](figures/willapa-marsh-51.png), [125](figures/willapa-marsh-125.png). Display scales vary by crop. Colored traces are derived annotations, not original ink. The forty mean-high-water records have not yet received this visual audit; do not extend the eight-feature result to them.

## Dated modern candidate

[NOAA's WA0401D report](https://www.ngs.noaa.gov/desc_reports/WA0401D.PDF), preserved [unchanged](../sources/originals/cascadia/WA0401D.pdf), identifies GC10747. All six pages were text-read; pages4 and6 were rendered and visually checked. Photography spans May2005–October2006; compilation/review is2008. Infrared photography was tide-coordinated; color imagery was not. The control reference is NAD83(CORS96), epoch2002; mapping uses UTM10. Predicted compiled accuracy is1.2m at95% for well-defined points, not independently measured marsh-edge accuracy. The image table supplies separate rolls, times and tide levels, referenced to MLLW and zoned Toke Point observations. Its coverage map broadly overlaps the historical area; no individual feature/frame match is established.

The attempted inferred current-package URL `https://nsde.ngs.noaa.gov/downloads/GC10747.zip` returned AccessDenied. No modern geometry was recovered and no displacement calculated. The report's product identifier is a retrieval lead, not proof that this guessed endpoint exists or that the source is unavailable elsewhere.

## What the geography test still requires

Compare vegetation edges with vegetation edges and MHW with MHW, retaining approximations, revisions, datum realization/epoch differences and correlated map errors. Recover GC10747 through an actual catalog/index link and inspect feature dates/classes; link historical traces to source legend and survey segments. A nearest line of a different tidal class would not measure temporal movement. Even a verified 1922-to-modern displacement would need timing and physical context before assignment to a catastrophe. Earlier1870s target marsh sheets remain missing; no chronology break or worldwide event is established.
