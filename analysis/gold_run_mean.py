"""Check reported rounded age summaries; not a dating-method reproduction."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if __name__ == '__main__':
    data = json.loads((ROOT/'data/gold-run-dates.json').read_text(encoding='utf-8'))
    rows = [r for r in data['rows'] if r['include_in_check']]
    weights = [1/r['standard_error_Ma']**2 for r in rows]
    mean = sum(r['age_Ma']*w for r,w in zip(rows,weights))/sum(weights)
    se = (1/sum(weights))**0.5
    result = dict(mean_Ma=mean, standard_error_Ma=se,
                  included_samples=[r['sample_id'] for r in rows],
                  rounded_matches_report=(round(mean,2)==data['reported_weighted_mean_Ma'] and round(se,2)==data['reported_standard_error_Ma']),
                  assumption='Inverse variance weighting with zero covariance, using rounded input summaries.',
                  scientific_validation=False)
    (ROOT/'analysis/gold-run-mean-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
