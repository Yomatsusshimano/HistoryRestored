# Can one reported steady discharge satisfy the selected controls?

2026-10-11. C008 / S125–S127. Published model-output audit, not hydraulic reproduction or independent field validation.

The [article's Table1](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021JF006135) reports steady-discharge thresholds for east-rim, Hartline and Lenore indicators. Four common-roughness scenarios are [transcribed separately](../data/grand-coulee-thresholds.json). Figure3/4 caption text gives Lenore upper values differing from the table; graphics and raw outputs were not inspected. The difference might distinguish last non-inundating from first inundating simulated discharge, but that explanation is unverified. No source value is corrected.

The [executed arithmetic](../analysis/grand_coulee_threshold_audit.py) asks a conditional question: if these indicators apply to one steady flow in a fixed terrain scenario, and the reported Lenore maximum is an upper envelope, does it overlap the largest of the three lower constraints? Units below are millions of cubic metres per second. These are reported model thresholds, not measured ancient discharges or statistical confidence limits.

| Terrain / Foster outlet | Largest lower constraint | Table upper envelope | Caption alternative | Conditional overlap |
| --- | ---: | ---: | ---: | --- |
| Reconstructed cataract / open | 2.6 | 7.0 | 7.5 | Yes under both |
| Reconstructed cataract / closed | 2.6 | 5.0 | Not extracted | Yes using table |
| Present-day / open | 17 | 7.5 | 8.0 | No under either |
| Present-day / closed | 14 | 7.5 | Not extracted | No using table |

All four printed discharge-sequence counts reproduce:23,21,23,19. The ice-occupied scenario has incomplete comparable constraints and is excluded rather than assigned guessed bounds. [Results and input hash](../analysis/grand-coulee-threshold-audit-result.json). Endpoint inclusion is a permissive diagnostic; the present-terrain gaps persist regardless of strict versus inclusive equality.

## What this changes and what it does not

The selected present-terrain thresholds cannot all describe one constant discharge under the stated interpretation. Different terrain, separate episodes, field interpretation or model error remain distinct explanations. The test cannot select among them. In particular, it does not reject a time-varying flood, establish that indicators are contemporaneous, or prove the reconstructed cataract is the historical surface.

Overlap on reconstructed terrain establishes arithmetic compatibility only. It does not verify that water followed those routes, that the terrain existed, that sediment moved as assumed, or that the maximum bound is correctly interpreted. Treating compatibility as successful reconstruction would skip the physical evidence and reproduction requirements.

The article's steady tests were designed to identify inundation thresholds, not reconstruct a complete event hydrograph. A decisive comparison needs raw stages at the actual controls, the input terrain, boundary conditions, roughness and the field records. Only then can a time-dependent flow and its sediment effects be compared with an authenticated event sequence.

## Access and next test

The current ScholarWorks item metadata still directs the full hydraulic package to Globus with sign-in required. Normal publisher supplement download returned a security challenge; no DOCX contents were acquired or inspected. Neither access result proves data are absent. There is no new source record for an uninspected supplement, no authentication bypass, and no third-party contact.

Obtain the actual package through an authorized access route; resolve table/caption threshold semantics against its outputs; reproduce one scenario before varying terrain. Preserve the [original outlet-age inference](SANPOIL-OUTLET-INFERENCE.md) as a separate stratigraphic test. No common catastrophe chronology, independent review or prospective prediction success is established.

Reproduce the conditional arithmetic with `python analysis/grand_coulee_threshold_audit.py` from the repository root; standard library only. Source access is HTML portions and caption text, not original figure-scan inspection.
