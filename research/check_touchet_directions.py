"""Retrospective cone geometry, not a duration fit or global significance test."""
import json, math
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'data/touchet-magnetic-directions.json').read_text(encoding='utf-8'))['rows']
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
        out.append(dict(site=site,lower_row=a['row_id'],upper_row=b['row_id'],angular_separation_deg=round(angle,3),sum_printed_cone_radii_deg=round(radii,3),cones_disjoint=angle>radii))
print(json.dumps(dict(selection='All three sites with printed -5 and 0 rows; every duplicate zero retained. Retrospective selection motivated by the authors\' pre-ash trend. Not all bed pairs.',assumptions='Printed directions and alpha95 cones represent original field directions without unmodelled systematic offsets; labels identify comparable horizons.',limits='Disjoint marginal cones are not a calibrated joint hypothesis test. No minimum duration or every-bed flood count follows.',comparisons=out),indent=2))
