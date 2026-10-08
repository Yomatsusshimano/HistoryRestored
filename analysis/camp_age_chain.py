"""Trace central ages through published stored dose summaries and rate variants."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
aliquots=json.loads((ROOT/'data/camp-century-aliquots-250.json').read_text(encoding='utf-8'))
rates=json.loads((ROOT/'data/camp-century-drac-crosswalk.json').read_text(encoding='utf-8'))
residual=json.loads((ROOT/'data/camp-century-residual-test.json').read_text(encoding='utf-8'))['adopted_residual_Gy']
fine=aliquots['groups'][0]['source_summary_Gy'][0]
coarse=aliquots['groups'][1]['source_summary_Gy'][0]
rows=[]
for name,de,rate,locator in [
 ('fine_highlight',fine,rates['rows'][0]['highlight_rate_Gy_ka'],'S4 J31; S11 T12'),
 ('fine_detailed',fine,rates['rows'][0]['detailed_rate_Gy_ka'],'S4 J31; S11 JQ12'),
 ('coarse_mixture',coarse,rates['mixture']['rate'],'S4 J57; S11 T17')]:
 rows.append({'variant':name,'input_DE_Gy':de,'residual_Gy':residual,'dose_rate_Gy_ka':rate,'age_ka':(de-residual)/rate,'locator':locator})
out={'source_id':'S146','formula':'(stored fading-corrected DE - adopted residual) / stored dose rate','results':rows,'scope':'Central-value arithmetic only. Does not reconstruct source weighting, dose-response fits, uncertainty or pooled age. Variant matches do not establish processing provenance.'}
(ROOT/'analysis/camp-age-chain-result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
