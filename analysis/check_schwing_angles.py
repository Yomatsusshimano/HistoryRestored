"""Check angular separation of published Schwing mean directions, not reversal significance."""
import json,math
from pathlib import Path
p=Path('data/schwing-source-comparison.json');d=json.loads(p.read_text());t=d['reversal_test']
def separation(di,ii,dj,ij):
 di,ii,dj,ij=map(math.radians,(di,ii,dj,ij))
 return math.degrees(math.acos(max(-1,min(1,math.sin(ii)*math.sin(ij)+math.cos(ii)*math.cos(ij)*math.cos(di-dj)))))
out={}
for kind in ('uncorrected','corrected'):
 out[kind+'_separation_degrees']=separation(t['normal_declination_degrees'],t[kind+'_normal_inclination_degrees'],(t['reverse_declination_degrees']+180)%360,-t[kind+'_reverse_inclination_degrees'])
out['scope']='Mean-direction geometry only. Critical angle, E/I correction, individual inputs and test significance not reproduced. Do not reuse corrected critical angle for the uncorrected calculation.'
assert round(out['corrected_separation_degrees'],2)==t['observed_gamma_degrees']
d['mean_direction_geometry']=out
p.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(out,indent=2))
