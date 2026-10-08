"""Reproduce S5 example correction factors, not the fitted equivalent doses."""
import json
import math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def factor(de, lab_rate, soil_rate, delay_h, g, regen_s):
    modified_rate = de / ((de / lab_rate / 2 / 3600 + delay_h) / 24 / 365.25 / 1000)
    modified_g = g / (1 - g / 100 * math.log10((delay_h + regen_s / 2 / 3600) / 48))
    return 1 - modified_g / 100 * math.log10(modified_rate / soil_rate / math.e)

if __name__ == '__main__':
    data = json.loads((ROOT/'data/camp-century-fading-example.json').read_text(encoding='utf-8'))
    output=[]
    for step in data['steps']:
        calculated=[factor(step['de_Gy'],data['lab_rate_Gy_s'],data['soil_rate_Gy_ka'],step['delay_h'],step['g_percent_decade'],r) for r in data['regen_seconds']]
        errors=[abs(a-b) for a,b in zip(calculated,step['cached_factors'])]
        assert max(errors)<1e-12
        output.append({'temperature_C':step['temperature_C'],'factors':calculated,'max_absolute_cache_difference':max(errors)})
    assert factor(700,.095,2,.3,0,4000)==1
    result={'scope':'30 example worksheet factors reproduce cached cells within 1e-12. Zero-fading boundary gives factor 1. Not equivalent-dose fitting or age validation.','results':output}
    (ROOT/'analysis/camp-fading-worksheet-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
