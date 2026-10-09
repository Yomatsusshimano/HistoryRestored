# Regional observations in Halley's 1715 report

2026-10-09. The remaining PDF6-18/printed250-262 pages of the [preserved report](../sources/originals/astronomy/halley1715/halley1715.pdf) were rendered and visually inspected. Together with the previously inspected pages, this completes visual inspection of the18-page article. This does not authenticate its physical age, original manuscript or individual observers' records.

The [input ledger](../data/halley1715-regional-inputs.json) transcribes the duration column of all26 synopsis rows on PDF18/printed262 and the available totality endpoints. Brace-linked Broadway/Carmarth. and Llanidan/Anglesey labels remain combined rows. Historical place tokens are not modern coordinates. Partial contacts and sunspot timings are not comprehensively transcribed. Blank duration cells remain null.

## Arithmetic and conflicting levels of evidence

The [executed audit](../analysis/halley1715_regional.py) produces [26 row results](../data/halley1715-regional-results.json):19 printed durations, seven blanks, and11 pairs of totality endpoints. All11 endpoint differences match the printed durations exactly. This is a transcription/arithmetic check, not independent confirmation that the measurements are accurate.

Halley's prose on PDF10/printed254 distinguishes approximate reports of four minutes or longer, whose timing methods were not supplied, from John Bridges at Barton (233seconds) and John Whiteside at King's Walden (232seconds), whom he describes as using good pendulum clocks. He then infers a greatest duration of about237seconds from geography and eclipse geometry. Four synopsis durations exceed that inference:

|Synopsis place/observer|Printed duration|Excess over inferred237s|
| --- | ---: | ---: |
|Exon / L. Bishop|240s|3s|
|Northampt. / M. Hawkins|242s|5s|
|Plymouth / M. Heines|270s|33s|
|Weymouth / M. Hobbs|240s|3s|

These tensions are preserved. The source's preference for particular clocks is its own assessment, not independent instrument validation. The inferred maximum cannot be used to silently discard or shorten contrary table entries. Nor can those entries, with unresolved calibration and locations, be used to infer extra eclipses or a chronology break.

On PDF9/printed253, Halley reports that clouds limited John Keill's Oxford observation and that its approximate210second darkness estimate was, in his assessment, too short. He reports Roger Cotes at Cambridge missed the beginning and totality onset amid distracting company. That incomplete Cambridge row is not a zero-duration event. On PDF12/printed256, a non-totality report at Bost[a/o]n is relayed through inhabitants to Stephen Gray, rather than supplied as a separately authenticated observer log; the spelling and exact location require further work. Other inferred shadow limits and routes must be kept separate from measured contacts.

## Additional London contacts and shared witnesses

PDF7/printed251 supplies Halley's final partial contact: clock10:20:15, corrected10:20:00. The later clock check says one quarter minute fast, differing from the earlier14seconds. The [London ledger](../data/halley1715-observations.json) now records that separately; the existing modeled contact10:19:19.978 local apparent time is about40.022seconds earlier. No new orbital search or fitted clock adjustment was needed: the already calculated fourth contact was compared with the newly inspected source value. The calculation script now reads that endpoint from the ledger on reproduction.

PDF7-8/printed251-252 also reports de Louville's observations made with the London party: totality202seconds, one second shorter than Halley's203seconds, and eclipse end10:20:04. His spot-occultation times are additional observations, but spot geometry and individual clock calibration have not been reconstructed. The same venue, event and compiled article prevent treating these as a separate astronomical date anchor.

James Pound at Wanstead has a fuller contact series on PDF8/printed252 and200seconds of totality. Derham at Upminster has188seconds on PDF9/printed253. Greenwich is summarized as191seconds. These provide candidate spatial checks once original site and clock information are authenticated. Different local apparent times cannot be compared directly as simultaneous universal-time measurements. No regional model residuals or revised coordinates are claimed here.

## Next discriminating work

Retrieve original observer correspondence and instrument/calibration records, resolve historical sites, then calculate a declared regional comparison with positional and Earth-rotation sensitivity. Separately sourced astronomical records are still needed to challenge a common chronology transformation. This article's multiple places do not become26 independent document lineages or prospective discoveries. All twenty original objectives remain active; no independent review, worldwide event or chronology divergence is established.

Reproduce the arithmetic with `python analysis/halley1715_regional.py`. The model-date experiment remains separately documented in the [London chronology audit](HALLEY-1715-ECLIPSE.md).
