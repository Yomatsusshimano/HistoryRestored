"""Diagnostic aggregation comparisons; not replacement published estimates."""
import json,math,statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/camp-century-aliquots-250.json').read_text(encoding='utf-8'))
results=[]
for group in d['groups']:
    accepted=[r for r in group['aliquots'] if not r['rejected_by_cell_fill']]
    x=[r['dose_Gy'] for r in accepted];e=[r['error_Gy'] for r in accepted]
    weights=[v**-2 for v in e]
    results.append({'fraction_um':group['fraction_um'],'accepted_n':len(x),
        'arithmetic_mean_Gy':statistics.mean(x),
        'arithmetic_sampling_SE_Gy':statistics.stdev(x)/math.sqrt(len(x)),
        'inverse_variance_mean_Gy':sum(a*b for a,b in zip(x,weights))/sum(weights),
        'inverse_variance_formal_SE_Gy':1/math.sqrt(sum(weights)),
        'source_summary_Gy':group['source_summary_Gy']})
out={'scope':'Exploratory comparison of two explicit aggregation rules. Inverse-variance calculation assumes independent errors; shared error omitted. Neither rule is asserted to be the authors method.','results':results}
(ROOT/'analysis/camp-aliquot-summary-result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
