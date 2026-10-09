"""Literal age/elevation comparison; no calibration or error-distribution assumptions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data/willapa-2007-age-inputs.json').read_text())
later=json.loads((ROOT/'data/willapa-tidalflat-inputs.json').read_text())
# Find the existing source row without assuming the outer ledger's list key.
lists=[v for v in later.values() if isinstance(v,list)]
old=next(r for rows in lists for r in rows if isinstance(r,dict) and r.get('printed_site_type')=='KI11/pf')
early=next(r for r in data['radiocarbon'] if r['site']=='KI-11')
assert early['depth_cm']/100==old['depth_m']==5
assert early['printed_age']==old['conventional_age_yr_bp']==1590
assert early['printed_plus_minus']==old['conventional_error_1sigma_yr']==40
differences=[dict(site=r['site'],depth_cm=r['depth_cm'],TL_minus_IRSL_years=r['TL_age']-r['IRSL_age']) for r in data['luminescence'] if r['IRSL_age'] is not None]
pairs=[]
for site in ['KI-13','TS-4']:
    a,b=sorted([r for r in data['luminescence'] if r['site']==site],key=lambda r:r['depth_cm'])
    pairs.append(dict(site=site,deeper_minus_shallower_depth_cm=b['depth_cm']-a['depth_cm'],deeper_minus_shallower_IRSL_years=b['IRSL_age']-a['IRSL_age'],deeper_minus_shallower_TL_years=b['TL_age']-a['TL_age']))
out=dict(source_ids=['S274','S281'],table_counts=dict(radiocarbon=len(data['radiocarbon']),luminescence=len(data['luminescence'])),KI11_comparison=dict(depth_equal=True,printed_age_error_equal=True,material_2007=early['material'],material_method_2018=old['material_method'],age_label_2007=early['age_label'],age_label_2018='conventional yr BP ±1sigma',calibrated_median_2018=old['reported_median'],elevation_2007_m_MLLW=early['elevation_m_MLLW'],elevation_2018_m_MTL=-4.7,conversion_authenticated=False,lab_id_2018=old['beta_number'],lab_id_2007=None),luminescence_method_differences=differences,adjacent_depth_differences=pairs,limitations='Literal arithmetic only. Unequal ages are not event counts, sedimentation durations or statistical significance. No independent-error assumption, recalibration, authenticated sample identity or vertical datum conversion.')
(ROOT/'data/willapa-2007-age-crosswalk.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
