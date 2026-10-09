"""Check published pixel-count arithmetic without reconstructing a coastline."""
import json,hashlib
from pathlib import Path
p=Path('data/bat2015-supplement-audit.json'); d=json.loads(p.read_text(encoding='utf-8'))
rows=[]
for r in d['groups']:
    loss=100*(r['LGM_relative_area']-r['current_relative_area'])/r['LGM_relative_area']
    ratio=r['LGM_relative_area']/r['current_relative_area']
    rows.append({'group':r['name'],'loss_percent_LGM_denominator':loss,'LGM_to_current_pixel_count_ratio':ratio,'printed_percent':r['reported_loss_percent'],'nearest_integer_matches':round(loss)==r['reported_loss_percent']})
assert all(r['nearest_integer_matches'] for r in rows)
out={'date':'2026-10-09','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'formula':'100*(LGM-current)/LGM','results':rows,'limits':['Pixel-count arithmetic only; no bathymetry, equal-area correction or raster classification reproduced.','No rate, event date, habitat-loss cause or sudden geography change inferred.']}
Path('analysis/bat-island-area-check-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
