# Columbia Gorge paleotopography: reproduction lead

2026-10-08. Sourced draft; no independent review or model rerun.

## Published result and dependencies

[David, Larsen and Lamb (2022), S58](https://doi.org/10.1029/2022GL097861), sections 3–6, reports ANUGA simulations over modern and reconstructed canyon surfaces. The reconstruction assumes eroded lower slopes resembled adjacent preserved slopes and leaves the channel floor unchanged. Reported peak discharges are 8–9 million m³/s on modern terrain versus 6–7 million on reconstructed terrain. The paper's within-study reduction is 20–30%; its abstract's 30–40% compares with an earlier 10-million estimate. These are different comparisons.

Its sediment calculation partitions a reconstructed 7.4 km³ erosion volume among 25 previously constrained floods. A 33 cm sediment diameter yields a transported volume close to that reconstruction. The flood-frequency distribution, high-water evidence and hydrograph shapes depend on earlier work. This is not independent confirmation of the erosion volume, a new flood chronology, or a test of S27's proposed loess bulking. Text sections were inspected; figure graphics and supplement were not successfully inspected here.

## Actual data access

The [UMass deposit, S59](https://doi.org/10.7275/2d19-f718) resolves to a current repository record. Its public API describes Hydro_Models, Topo_Reconstruction and Analysis_Scripts, including ANUGA Python and reconstruction/analysis MATLAB files. It directs users to authenticated Globus access; the README is there too. The repository's ORIGINAL bundle returned zero bitstreams. This does **not** mean the data are absent: the designated storage is external.

[Designated Globus collection and folder](https://app.globus.org/file-manager?origin_id=b9120884-93ae-4a90-9f91-1556b01569e7&origin_path=%2FColumbia_Gorge_Repository%2F). No login, file listing, download, or execution was completed. The API observations and endpoints are recorded in [the availability supplement](../data/missoula-paleocanyon-availability.json). Dataset issue year 2021, article publication 2022 and repository accession 2024 are distinct metadata fields, not a demonstrated chronology contradiction.

## Next reproducibility test

Obtain the designated files through authorized access, inventory and hash them, inspect the README and scripts before execution, and identify solver/environment versions. Reproduce both terrain scenarios against the same controls before varying assumptions. Track which controls trained the reconstruction or constrained discharge; reserve genuinely uninspected targets for subsequent prediction. Check transport sensitivity without treating a size selected to match reconstructed volume as an independent validation. Until then, this is a concrete alternative modeling pathway, not a reproduced physical model of the proposed worldwide event.
