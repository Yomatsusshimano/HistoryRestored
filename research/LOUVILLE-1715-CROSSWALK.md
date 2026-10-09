# De Louville's separately printed London eclipse account

2026-10-09. A primary French account has been recovered through Bayerische Staatsbibliothek's [1715 reporting-year volume, cataloged as published in1718](https://www.digitale-sammlungen.de/en/view/bsb10500330?page=229). Its IIIF manifest identifies shelfmark4Acad.117-1715 and434 canvases. Memoir page89 is canvas229, while a different page89 occurs earlier in the volume; printed pagination alone would not uniquely locate this account.

Canvases229-231/printed89-91 were downloaded and visually inspected. The title explicitly identifies May3,1715, new style, and attributes the account to the Chevalier de Louville. A June5,1715 marginal date is present; its exact administrative meaning has not been authenticated. Neither that date nor the volume's reporting year is substituted for publication in1718. Only these three pages were inspected; the remaining article/volume, original notes and physical custody remain unaudited.

The [input ledger](../data/louville1715-inputs.json) retains official image URLs, byte lengths, SHA256 hashes and the manifest identifier/hash. Scans are linked rather than redistributed: the manifest declares NoC-NC1.0 rights. Attribution: München, Bayerische Staatsbibliothek. A Python TLS certificate-chain failure was followed by successful native Windows curl downloads with normal certificate verification; no verification override was used.

## Shared calibration is described explicitly

On printed89, de Louville describes Halley measuring solar altitudes with a two-foot-radius quadrant before the eclipse. He describes two pendulum clocks, one taken to the platform and another left below, and his own seconds watch being set to true time. De Louville says he observed from the platform with a seven-to-eight-foot telescope brought from Paris, fitted with a micrometer. This is a paraphrase of the French account, not instrument or calibration authentication.

The account gives a separately preserved narrative but explicitly shares the venue, eclipse and Halley's calibration work. It does not supply a wholly independent absolute chronology anchor. Nor does setting the clocks to true time eliminate the need to inspect later corrections.

## Executed printed-time comparison

The [crosswalk script](../analysis/louville1715_crosswalk.py) compares nine entries with the de Louville sequence quoted in Halley's article, PDF7-8/printed251-252. [Results](../data/louville1715-results.json) show six offsets of14seconds and three of15seconds, French minus English:

|Event|French printed time|English compilation|Difference|
| --- | --- | --- | ---: |
|Four digits eclipsed|08:28:34|08:28:20|14s|
|First spot ingress begins|08:33:11|08:32:57|14s|
|First spot fully hidden|08:33:32|08:33:18|14s|
|Second spot hidden|08:34:22|08:34:08|14s|
|Third spot hidden|08:35:12|08:34:58|14s|
|First spot emersion|09:36:15|09:36:01|14s|
|Second spot emersion|09:38:41|09:38:26|15s|
|Third spot emersion|09:40:40|09:40:25|15s|
|Eclipse ends|10:20:19|10:20:04|15s|

The French first-spot emersion refers to the spot's middle; equivalence with the English event label is provisional. Both original labels remain accessible. No geometry calculation uses these spot events yet.

Halley's own clock corrections are14seconds near the beginning and15seconds near the end. Their subtraction reproduces the scale and pattern of this printed crosswalk. This is **consistent with correction during compilation**, but the mechanism is not established: original notes, editorial correspondence and additional editions are needed. It is not evidence that either printed sequence is in universal time. No values have been altered to manufacture agreement.

French totality runs09:09:13-09:12:35, exactly202seconds, matching its printed duration and Halley's report of de Louville's duration. The French account also distinguishes a calculated prediction of225seconds from that observed duration. Halley's own203second duration belongs to a different observer record and must not be substituted for de Louville's endpoints.

The French first partial contact is08:06:13. That falls inside08:06:11-08:06:16, the interval obtained from Halley's own first-notice clock arithmetic and bounded delay, but de Louville's observation and clock are not identical to Halley's. It therefore does not resolve Halley's printed08:06:00 discrepancy or justify overwriting it.

## Consequences for chronology and attribution

The conventional calendar crosswalk is explicitly present in the French title, rather than inferred solely from a modern catalog. That is documentary evidence of the new-style label in this scanned edition, not independent proof of the observation's physical date or the edition's age.

This case supplies a concrete, reproducible publication difference and a candidate mundane transmission mechanism. A seconds-level correction is separate from a year-scale chronology shift or deliberate fabrication. The two accounts remain dependent through the observers' shared setting and calibration. The proposed worldwide catastrophe and historical-rewriting sequence remain unestablished.

Next inspect the rest of de Louville's account and additional editions, seek original observer/calibration notes, and add separately located astronomical observations before testing a common chronology transformation. All twenty objectives remain active; no independent review or prospective confirmation is claimed.

Reproduce with `python analysis/louville1715_crosswalk.py`.
