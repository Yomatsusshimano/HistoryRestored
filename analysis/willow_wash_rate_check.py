"""Reproduce the reported average-rate arithmetic, not a tephra age."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
record=json.loads((root/'data/willow-wash-controls.json').read_text(encoding='utf-8'))
x=record['reported_average_rate']
duration_kyr=(x['older_age_ma']-x['younger_age_ma'])*1000
rate=x['thickness_m']*100/duration_kyr
result={
 'source_id':record['source_id'],'input_locator':x['locator'],
 'duration_kyr':duration_kyr,'computed_rate_cm_per_kyr':rate,
 'reported_rounded_rate_cm_per_kyr':x['reported_rate_cm_per_kyr'],
 'agrees_when_rounded_to_integer':round(rate)==x['reported_rate_cm_per_kyr'],
 'scope':'Dimensional arithmetic on rounded reported inputs; not independent dating or reproduction of2008Nomlaki extrapolation.'}
(root/'analysis/willow-wash-rate-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
