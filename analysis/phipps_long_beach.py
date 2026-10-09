"""Selected published-table arithmetic, not new shoreline observations."""
from pathlib import Path
import json,hashlib
import numpy as np
raw={'Joe John (XB)':[500,570,600,580,600,580,None,620,640,None,600,640,590,650,630,680,730,640,670,760,None,None,760,925,954,740],
     'Klipsan (XA)':[400,440,490,460,510,480,500,580,580,550,620,620,690,700,670,670,720,680,650,790,806,825,670,760,790,670]}
records=[]
for name,values in raw.items():
    assert len(values)==26
    rows=[{'year':y,'distance_ft':None if y<1957 or y>1982 else values[y-1957]} for y in range(1951,1988)]
    results=[]
    for low in (1951,1977):
        valid=[r for r in rows if r['year']>=low and r['distance_ft'] is not None]
        x=np.array([r['year'] for r in valid],dtype=float);y=np.array([r['distance_ft'] for r in valid],dtype=float)
        slope=float(np.sum((x-x.mean())*(y-y.mean()))/np.sum((x-x.mean())**2))
        results.append({'nominal_start_year':low,'actual_first_year':int(x.min()),'actual_last_year':int(x.max()),'n':len(valid),
                        'ols_slope_ft_per_year':slope,'pearson_r_signed':float(np.corrcoef(x,y)[0,1])})
    records.append({'site':name,'reported_total_slope_ft_per_year':14,'reported_since1977_slope_ft_per_year':-3 if name.startswith('Joe') else -12,
                    'reported_total_R':0.83 if name.startswith('Joe') else 0.91,'reported_since1977_R':0.04 if name.startswith('Joe') else 0.36,
                    'rows':rows,'diagnostics':results})
out={'source_id':'S264','source_locator':'Printed TableA2p31 and TableA3p32; PDF37/38','method':'Manual selected-column transcription, null blanks/dashes, OLS against recorded years; signed Pearson r. No filled missing years.',
     'measurement':'Feet west of fixed monument to beach elevation +8feet (approximately high tide); vertical datum and monument coordinates not supplied in selected table.',
     'source_sha256':hashlib.sha256(Path('tmp/research/phipps90-mirror.bin').read_bytes()).hexdigest(),'records':records,
     'limits':'Two named ocean-side beach profiles, not GrassyIsland boundaries. ReportedRpositive with negative rates; signed diagnostic differs in sign. Original observations, full survey uncertainty and aerial photo plates unrecovered. Arithmetic reproduction not independent physical validation.'}
Path('data/phipps-long-beach.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{k:v for k,v in r.items() if k!='rows'} for r in records],indent=2))
