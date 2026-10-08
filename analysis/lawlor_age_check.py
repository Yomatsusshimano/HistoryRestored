"""Retrospective arithmetic check on rounded, published zircon ages; not new dating."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def summarize(rows):
    weights = [1 / row['age_sigma_ma'] ** 2 for row in rows]
    total = math.fsum(weights)
    mean = math.fsum(w * row['age_ma'] for w, row in zip(weights, rows)) / total
    return {
        'n': len(rows),
        'weighted_mean_ma': mean,
        'internal_standard_error_ma': math.sqrt(1 / total),
        'mswd': math.fsum(w * (row['age_ma'] - mean) ** 2
                         for w, row in zip(weights, rows)) / (len(rows) - 1),
    }

def main():
    data = json.loads((ROOT / 'data/harvey-zircon-rows.json').read_text(encoding='utf-8'))
    rows = data['rows']
    assert len(rows) == 103 and len({r['id'] for r in rows}) == 103
    assert sum(r['group'] == 'Bouse' for r in rows) == 51
    lawlor = sorted((r for r in rows if r['group'] == 'Lawlor'), key=lambda r:r['age_ma'])
    assert len(lawlor) == 52 and all(r['age_sigma_ma'] > 0 for r in rows)
    # Implement the eight-oldest rule explicitly, without tuning to the desired mean.
    kept, removed = lawlor[:-8], lawlor[-8:]
    assert kept[-1]['age_ma'] < removed[0]['age_ma'], 'Ambiguous exclusion boundary'
    result = {
        'source_id': 'S196',
        'scope': 'Published rounded ages and one-sigma errors; assumed diagonal weights. No covariance or systematic-error propagation.',
        'all_lawlor': summarize(lawlor),
        'eight_oldest_removed': summarize(kept),
        'removed_ids': [r['id'] for r in removed],
        'retained_ids': [r['id'] for r in kept],
        'limits': 'Not an eruption age or a reproduction of ion measurements, corrections, full uncertainty, or geological selection rationale. Bouse rows are preserved without fitting a single age to their mixed population.',
    }
    (ROOT / 'data/lawlor-age-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['all_lawlor','eight_oldest_removed']},indent=2))

if __name__ == '__main__':
    main()
