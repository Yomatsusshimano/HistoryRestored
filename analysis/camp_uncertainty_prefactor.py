"""Deterministic central-input check of S137 line 240; not full replication."""
import json, math, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def summary(values, errors):
    weights=[e**-.5 for e in errors]
    total=sum(weights)
    weights=[w/total for w in weights]
    mean=sum(w*x for w,x in zip(weights,values))
    spread=math.sqrt(sum(w*(x-mean)**2 for w,x in zip(weights,values)))
    return mean,spread

def main():
    path=ROOT/'data/camp-century-nuclide-inputs.json'
    d=json.loads(path.read_text())['values']; rows={}
    factor=math.exp(416000*(1/1.01e6-1/2.02e6))
    for suffix in ['up','lo']:
        al,sa=summary(d['al26_'+suffix],d['al26_err_'+suffix])
        be,sb=summary(d['be10_'+suffix],d['be10_err_'+suffix])
        rows[suffix]={'al_mean':al,'be_mean':be,'ratio_observed':al/be,
            'ratio_burial_corrected':al/be*factor,
            'relative_weighted_spread':math.hypot(sa/al,sb/be)}
    lower_relative=rows['lo']['relative_weighted_spread']
    legacy=rows['up']['ratio_burial_corrected']*lower_relative
    corresponding=rows['lo']['ratio_burial_corrected']*lower_relative
    ratio=legacy/corresponding
    assert math.isclose(ratio,rows['up']['ratio_observed']/rows['lo']['ratio_observed'])
    result={'source_id':'S137','input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'method':'Deterministic central arrays, inverse-square-root-error weights as in source; normalized weighted population spread. No Gaussian perturbations.',
        'central_values':rows,'legacy_prefactor_spread':legacy,
        'lower_ratio_prefactor_spread':corresponding,'multiplicative_effect':ratio,
        'limits':'Neither spread is a new total scientific uncertainty. This is not the mean Monte Carlo output, a corrected published error bar, or a rerun of the full MATLAB script. No raw assay identities or calibration verified. Mean ratios unchanged by substituting only the uncertainty prefactor.'}
    (ROOT/'analysis/camp-uncertainty-prefactor-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
