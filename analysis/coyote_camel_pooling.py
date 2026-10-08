"""Retrospective consistency check of S99; not an OxCal run or recalibration."""
import hashlib
import json
import math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def combine(values, sigmas):
    if len(values) != len(sigmas) or len(values) < 2 or any(s <= 0 for s in sigmas):
        raise ValueError('Need matching observations and positive standard errors')
    weights = [1/s**2 for s in sigmas]
    mean = sum(x*w for x,w in zip(values,weights))/sum(weights)
    error = math.sqrt(1/sum(weights))
    q = sum(((x-mean)/s)**2 for x,s in zip(values,sigmas))
    return mean,error,q

if __name__ == '__main__':
    data = json.loads((ROOT/'data/coyote-camel-assays.json').read_text())
    values = [r['radiocarbon_BP'] for r in data['assays']]
    errors = [r['plus_minus_BP'] for r in data['assays']]
    mean,error,q = combine(values,errors)
    assert len(values) == 3 # df=2 gives the exact upper tail exp(-Q/2)
    result = {
      'input_sha256_canonical_json': hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
      'source_id':'S99',
      'method_source_id':'S100',
      'assumptions':['Printed uncertainties treated conditionally as one-sigma standard errors','Independent Gaussian measurement errors, common true radiocarbon age, no additional offsets or variance','Same bone does not establish independence of preparation or contamination errors'],
      'weighted_mean_radiocarbon_BP':mean,
      'standard_error_BP':error,
      'reported_mean_BP':data['reported_combination']['radiocarbon_BP'],
      'reported_error_BP':data['reported_combination']['plus_minus_BP'],
      'chi_square_Q':q,
      'degrees_of_freedom':2,
      'upper_tail_probability':math.exp(-q/2),
      'reference_5_percent_threshold':-2*math.log(.05),
      'uniform_error_multiplier_to_5_percent_boundary':math.sqrt(q/(-2*math.log(.05))),
      'pairwise':[],
      'limits':'Retrospective diagnostic, not preregistered. No calibration curve, original laboratory certificates, OxCal model or error covariance recovered. Does not identify a faulty assay or invalidate radiocarbon dating.',
      'scientific_validation':False
    }
    for i in range(3):
      for j in range(i+1,3):
        result['pairwise'].append({'labels':[data['assays'][k]['label_as_printed'] for k in (i,j)],'difference_BP':abs(values[i]-values[j]),'difference_in_combined_standard_errors':abs(values[i]-values[j])/math.hypot(errors[i],errors[j])})
    (ROOT/'analysis/coyote-camel-pooling-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
