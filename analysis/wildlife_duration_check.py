"""Retrospective duration compatibility within published sets, not a statistical test."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if __name__ == '__main__':
    path = ROOT/'analysis/sloth-intervals-result.json'
    raw = path.read_bytes()
    sloths = json.loads(raw)
    groups = {
        'seven_calibrated_sloth_rows': sloths['all_included_cover']['minimum_span_calendar_years'],
        'six_Neocnus_comes_rows': sloths['same_taxon_sensitivity']['minimum_span_calendar_years'],
    }
    out = {
        'input_sha256_canonical_json': hashlib.sha256(json.dumps(sloths,sort_keys=True,separators=(',', ':')).encode()).hexdigest(),
        'status': 'RETROSPECTIVE_DESCRIPTIVE_COMPATIBILITY',
        'scenarios': [dict(group=group, duration_years=d, minimum_cover_years=m,
                           fits_within_reported_sets=d >= m)
                      for group,m in groups.items() for d in (0,1,10,100)],
        'limits': 'No probability model, recalibration or deposition/extinction inference. Published sets are not hard age bounds.',
        'scientific_validation': False,
    }
    (ROOT/'analysis/wildlife-duration-result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
