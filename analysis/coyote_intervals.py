"""Descriptive intersection of reported OSL ranges, not joint statistical inference."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == '__main__':
    data = json.loads((ROOT/'data/coyote-osl.json').read_text(encoding='utf-8'))
    included = [r for r in data['samples'] if r['context'] == 'flood sediment']
    assert included
    low = max(r['age_ka']-r['reported_2sigma_ka'] for r in included)
    high = min(r['age_ka']+r['reported_2sigma_ka'] for r in included)
    result = {
        'input_sha256_canonical_json':hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',', ':')).encode()).hexdigest(),
        'included_ids':[r['field_id'] for r in included],
        'excluded_ids':[r['field_id'] for r in data['samples'] if r not in included],
        'exclusion_reason':'Overlying loess is a different depositional context.',
        'intersection_ka': [round(low, 8), round(high, 8)] if low <= high else [],
        'inference':'Overlap is not proof of synchrony or a joint confidence interval. No radiocarbon result combined.',
        'scientific_validation':False,
    }
    (ROOT/'analysis/coyote-intervals-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(result['intersection_ka'])
