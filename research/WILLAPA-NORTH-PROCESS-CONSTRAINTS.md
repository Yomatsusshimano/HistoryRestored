# North Willapa: dated shoreline synthesis and physical-model gaps

2026-10-09. S271 is the January 2024 [Pacific County North Willapa Shoreline Erosion Mitigation Master Plan](https://co.pacific.wa.us/dcd/images/Willapa%20Erosion%20Mitigation%20Master%20Plan%20Final%20Final.pdf), produced by Moffatt & Nichol. The 98-page county-hosted PDF was acquired through normal TLS. Pages 1,32,78,79,83 were visually inspected; selected additional appendix text was read. This is a selected audit, not review of the entire plan. The original remains in the local research cache; no full report or third-party photographs are republished. Its byte identity and inspected scope are in the [ledger](../data/willapa-north-plan.json).

## Reported observations versus forecasts

Page 32 depicts historical shorelines labeled 1884,1943,1989 and January 2023. Dashed lines for 2030 and 2060 are projections, not observations. Underlying survey vertices, historical source sheets, boundary definitions and uncertainty are not recovered here. The nearby prose discusses an 1880 chart and retreat from 1887; those dates must not be silently substituted for the map's 1884 line.

The prose reports 11,700 feet of northward Cape Shoalwater retreat during 1887–1971. Dividing by the 84 elapsed years yields approximately 139.29 feet/year (42.45 metres/year). This is arithmetic on a reported cumulative distance. It is not an independently measured rate, a constant annual history, a single-event displacement or a rate for Grassy Island. The [script](../analysis/willapa_north_plan.py) checks source identity and this arithmetic. It does not authenticate the original charts or reproduce a shoreline model.

## Mechanisms that must be compared

Pages 78–79 identify channel migration, wave erosion and changing sand supply. The proposed channel mechanism connects a deep channel approaching shore with reduced wave attenuation and bank erosion. The report describes localized stabilization near the SR105 groin built in 1998, with an approximate quarter-study-area scope; it does not establish systemwide stabilization.

The report itself identifies missing long-term channel-stability analysis, sparse or absent local wave measurements, incomplete sediment pathways/budget and poorly characterized sand bypassing. Its physical explanation is therefore a testable alternative with explicit missing inputs. Those gaps neither validate a catastrophe nor justify treating the conventional account as completely reproduced.

Appendix B discusses retreat of the High Tide Line. This label is not automatically equivalent to the mean-high-water boundaries or apparent-marsh traces used in the southern island comparison. North Cove, Cape Shoalwater and Tokeland are separate from Grassy Island/Leadbetter Point; no rate, protection performance or geological identity is transferred between them.

## Specific original-data targets

Page 83 lists 2008–2016 USACE thalweg-position graphics/shapefiles, 1911–2003 Ecology historical shorelines, 2014–2016 Shoalwater survey campaigns, 2018–2019 scarp positions and profiles, and WSDOT 1955 aerials. It also names 1956 tests T-677 through T-687 and 1957 Job 1636 borings/field notes. These are catalog leads within the plan, not acquired measurements; their locations and island coverage remain unknown.

Retrieve original shorelines and bathymetric surveys with dates, vertical datums, uncertainty and construction history. Then test whether channel approach and storm conditions predict spatially concentrated erosion, with sheltered or stabilized stretches as controls. No prospective prediction has been frozen or scored in this retrospective audit. An abrupt regional hypothesis must additionally identify synchronous dated changes beyond these local controls and satisfy sediment/flow budgets. No worldwide reconstruction or independent review is completed.

## Retrieval limits retained

UW's Aerial Finder page loads, but its named footprint and two raster services returned service-error 500 objects. Pacific County's linked orthophoto viewer identifies itself as a 2008 map, not a historical-photo index. The USGS OFR02-281 direct download remained 403; its indexed excerpts are not full-report inspection. The CiteSeer mirror returned 404; the coastal-network mirror of the county plan returned 406. The county-hosted plan download succeeded. No access controls or TLS checks were bypassed, and no archive request was sent.
