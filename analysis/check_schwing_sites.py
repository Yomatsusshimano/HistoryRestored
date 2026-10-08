"""Conditional checks of three visually inspected Table2 blocks, including a matching control."""
import json,math
from pathlib import Path
rows=json.loads(Path('data/schwing-direction-candidates.json').read_text())['rows']
results=[]
for prefix,page,reported in [('WC 1-',48,(172.2,-51.4)),('WC 2-',48,(174.7,-47.1)),('LCW 28-',44,(9.4,39.1))]:
 a=[x for x in rows if x['sample'].startswith(prefix)]
 v=[]
 for x in a:
  di,inc=map(math.radians,(x['declination'],x['inclination']))
  v.append((math.cos(inc)*math.cos(di),math.cos(inc)*math.sin(di),math.sin(inc)))
 x,y,z=[sum(q[i] for q in v) for i in range(3)]
 dec=math.degrees(math.atan2(y,x))%360;inc=math.degrees(math.atan2(z,math.hypot(x,y)))
 results.append({'sample_prefix':prefix,'printed_page':page,'specimens':[x['sample'] for x in a],'reported_declination':reported[0],'reported_inclination':reported[1],'equal_weight_declination':dec,'equal_weight_inclination':inc,'matches_one_decimal':(round(dec,1),round(inc,1))==reported})
assert results[0]['matches_one_decimal']
Path('data/schwing-site-checks.json').write_text(json.dumps({'source_id':'S211','selection':'Three inspected blocks: WC1 control, WC2 and LCW28. Not a prevalence sample or exhaustive site audit. All numeric rows in each block weighted equally, no correction or exclusions.','results':results,'limits':'A mismatch establishes failure under this calculation, not the actual author method or cause. Original inputs/process needed.'},indent=2)+'\n')
print([(x['sample_prefix'],x['matches_one_decimal']) for x in results])
