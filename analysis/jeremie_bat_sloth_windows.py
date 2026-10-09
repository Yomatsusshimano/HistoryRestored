"""Conditional published-set separation; neither deposition date nor joint confidence."""
import json, hashlib
from pathlib import Path
def read(p): return json.loads(Path(p).read_text(encoding='utf-8'))
bat=read('data/jeremie-bat2015-date.json')['bat']
dating=read('data/dating-records.json')
rows=dating['samples']
ids=['AA-58432','AA-58433','AA-58431']
selected=[r for r in rows if r.get('field_id') in ids]
assert len(selected)==3
bat_old=max(b for a,b in bat['published_cal_BP_intervals_young_old'])
comparisons=[]
for r in selected:
    young=min(a for a,b in r['published_cal_BP_intervals_young_old'])
    comparisons.append({'sloth_lab_id':r['field_id'],'sloth_museum_id':r['museum_catalog_id'],'sloth_youngest_published_endpoint_cal_BP':young,'bat_oldest_published_endpoint_cal_BP':bat_old,'nearest_set_gap_years':young-bat_old})
result={'date':'2026-10-09','input_sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in ['data/jeremie-bat2015-date.json','data/dating-records.json']},'comparisons':comparisons,'minimum_pair_gap_years':min(x['nearest_set_gap_years'] for x in comparisons),'limits':['Conditional comparison of published calendar sets from different calibration contexts; no recalibration or likelihood fit.','Not a joint-confidence bound on mortality duration.','Author-associated site; accession-to-unit and exact locality identity unverified.','No sediment deposition, extinction or catastrophe date inferred.']}
result['locality_followup'] = read('data/jeremie-bat2015-date.json').get('locality_followup')
result['limits'].append('S324 labels the point matching the bat coordinates as Jeremie #1; sloth context is #5. These gaps do not establish an age mixture within one cave.')
Path('analysis/jeremie-bat-sloth-windows-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
