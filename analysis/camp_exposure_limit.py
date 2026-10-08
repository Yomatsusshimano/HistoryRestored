"""Upper-sediment nonnegative-inventory limit under S137's equations."""
import hashlib,json,math,random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def crossing(inventory,production,decay):
    if inventory < 0: return None
    if inventory*decay >= production: return math.inf
    return -math.log1p(-inventory*decay/production)/decay

def weighted_normal(values,errors):
    weights=[e**-.5 for e in errors]; s=sum(weights); weights=[w/s for w in weights]
    return sum(w*x for w,x in zip(weights,values)),math.sqrt(sum((w*e)**2 for w,e in zip(weights,errors)))

def limits(al,be,age,p26=30.3):
    return (crossing(al*math.exp(age/1.01e6),p26,math.log(2)/717000),
            crossing(be*math.exp(age/2.02e6),4.15,math.log(2)/1387000))

def main():
    p=ROOT/'data/camp-century-nuclide-inputs.json'; d=json.loads(p.read_text())['values']
    am,asd=weighted_normal(d['al26_up'],d['al26_err_up']); bm,bsd=weighted_normal(d['be10_up'],d['be10_err_up'])
    seed=20261008; n=100000; rng=random.Random(seed); thresholds=[]; rejected=0; al_limited=0
    for _ in range(n):
        al=rng.gauss(am,asd); be=rng.gauss(bm,bsd); age=rng.gauss(416000,38000)
        if al<0 or be<0 or age<0: rejected+=1; continue
        a,b=limits(al,be,age)
        if not math.isfinite(min(a,b)): rejected+=1; continue
        thresholds.append(min(a,b)); al_limited+=a<=b
    thresholds.sort()
    def q(v):
        pos=v*(len(thresholds)-1); lo=int(pos); hi=min(lo+1,len(thresholds)-1)
        return thresholds[lo]+(pos-lo)*(thresholds[hi]-thresholds[lo])
    out={'source_ids':['S26','S137'],'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'central_crossings_years':dict(zip(['Al26','Be10'],limits(am,bm,416000))),
        'central_alternative_P26_27_8_crossings_years':dict(zip(['Al26','Be10'],limits(am,bm,416000,27.8))),
        'seed':seed,'draws':n,'excluded_draws':rejected,'Al26_limiting_draws':al_limited,
        'threshold_quantiles_years':{str(v):q(v) for v in [.025,.5,.975]},
        'fraction_threshold_above_16000':sum(x>16000 for x in thresholds)/len(thresholds),
        'assumptions':'Independent Gaussian measurement entries, isotopes and luminescence input; source inverse-square-root-error weights and fixed production/decay constants. Linear Gaussian aggregation exactly matches the weighted-mean sampling distribution, not the source finite simulation or random stream.',
        'equation':'N_produced=P/lambda*(1-exp(-lambda*t)); threshold at N_produced=N_observed*exp(age/tau), taking the smaller isotope crossing.',
        'limits':'Threshold distribution is not an actual-exposure posterior or confidence bound. No production uncertainty, shielding, correlated errors, erosion, full MATLAB execution or luminescence reproduction. The isolated lower-sediment uncertainty prefactor is not used.'}
    (ROOT/'analysis/camp-exposure-limit-result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
