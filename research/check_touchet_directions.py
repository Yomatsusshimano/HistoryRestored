"""Retrospective cone geometry, not a duration fit or global significance test."""
import hashlib, json, math
from pathlib import Path
root=Path(__file__).resolve().parents[1]
input_path=root/'data/touchet-magnetic-directions.json'
rows=json.loads(input_path.read_text(encoding='utf-8'))['rows']
def separation(a,b):
    d1,i1,d2,i2=map(math.radians,[a['declination_deg'],a['inclination_deg'],b['declination_deg'],b['inclination_deg']])
    dot=math.sin(i1)*math.sin(i2)+math.cos(i1)*math.cos(i2)*math.cos(d1-d2)
    return math.degrees(math.acos(max(-1,min(1,dot))))
out=[]
for site in ['Touchet','Burlingame','Zillah']:
    lower=[x for x in rows if x['site']==site and x['couplet']==-5]
    upper=[x for x in rows if x['site']==site and x['couplet']==0]
    assert len(lower)==1 and len(upper)==(1 if site=='Burlingame' else 2)
    for b in upper:
        a=lower[0];angle=separation(a,b);radii=a['alpha95_deg']+b['alpha95_deg']
        gap=max(0.0,angle-radii)
        out.append(dict(site=site,lower_row=a['row_id'],upper_row=b['row_id'],angular_separation_deg=round(angle,3),sum_printed_cone_radii_deg=round(radii,3),cones_disjoint=angle>radii,minimum_additional_pairwise_angular_allowance_deg=round(gap,3),equal_per_endpoint_allowance_deg=round(gap/2,3)))
print(json.dumps(dict(input_sha256=hashlib.sha256(input_path.read_bytes()).hexdigest(),selection='All three sites with printed -5 and 0 rows; every duplicate zero retained. Retrospective selection motivated by the authors\' pre-ash trend. Not all bed pairs.',assumptions='Printed cones used as geometric regions, conditional on comparable horizon labels. Added allowance is arbitrary independent endpoint displacement, not an estimated systematic error.',geometry='Additional allowance=max(0, separation-radius1-radius2). Half that value at each endpoint permits contact along the shortest connecting arc. A common rigid rotation cannot alter separation.',limits='Disjoint marginal cones are not a calibrated joint hypothesis test. Allowances are sensitivity thresholds, not measured errors or probabilities. Separate pairwise allowances do not establish one joint model for all rows. No minimum duration or every-bed flood count follows.',comparisons=out),indent=2))
