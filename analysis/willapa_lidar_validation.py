"""Reproduce24 printed NOAA control residuals; separate calibration from held-out validation."""
import hashlib,json,math,statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/willapa-lidar-validation-inputs.json').read_text())
pdf=ROOT/'tmp/research/willapa-lidar/surveyreport.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==d['original_sha256']
x=[r['delta_GCP_minus_lidar_m'] for r in d['rows']]; correction=d['reported']['correction_added_to_lidar_m']
corrected=[v-correction for v in x]
out=dict(source_id='S277',n=len(x),mean_raw_delta_m=statistics.mean(x),sample_sd_raw_m=statistics.stdev(x),
    raw_rmse_m=math.sqrt(statistics.mean(v*v for v in x)),
    corrected_mean_delta_m=statistics.mean(corrected),corrected_rmse_m=math.sqrt(statistics.mean(v*v for v in corrected)),
    normal_assumption_1_96_times_corrected_rmse_m=1.96*math.sqrt(statistics.mean(v*v for v in corrected)),
    max_absolute_raw_delta_m=max(map(abs,x)),max_absolute_corrected_delta_m=max(map(abs,corrected)),
    minimum_GCP_z_m=min(r['gcp_z_m'] for r in d['rows']),maximum_GCP_z_m=max(r['gcp_z_m'] for r in d['rows']),
    corrected_row_rounding_checks=[dict(site=r['site'],passes=abs(v-r['printed_corrected_delta_m'])<=.00055) for r,v in zip(d['rows'],corrected)],
    limitations='Same24controls estimate bias and assess corrected residuals; no held-out assessment.1.96factor assumesnormal errors, not a reproduced Shapiro-Wilk test. Does not validate inundated/vegetated flats, later transformations or each core point.')
(ROOT/'data/willapa-lidar-validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
