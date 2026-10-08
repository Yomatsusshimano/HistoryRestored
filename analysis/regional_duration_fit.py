"""Conditional maximum-likelihood cost of limiting two event dates' separation."""
import argparse,hashlib,json,math
from pathlib import Path
from bonneville_calibration_check import interpolate
ROOT=Path(__file__).resolve().parents[1]

def constrained_fit(years,a,b,duration):
    if duration<0 or len(years)!=len(a) or len(a)!=len(b):raise ValueError('Invalid fit inputs')
    step=years[1]-years[0];radius=int(duration/step)
    best=(-math.inf,None,None)
    for i,first in enumerate(a):
        lo=max(0,i-radius);hi=min(len(b),i+radius+1)
        j=max(range(lo,hi),key=b.__getitem__)
        if first+b[j]>best[0]:best=(first+b[j],i,j)
    unrestricted=max(a)+max(b)
    loss=unrestricted-best[0]
    return {'maximum_separation_years':duration,'best_Bonneville_CE':years[best[1]],'best_Electron_CE':years[best[2]],'log_likelihood_loss':loss,'relative_maximum_likelihood':math.exp(-loss)}

def run(curve,step=.25):
    paths=[ROOT/'data/bonneville-dates.json',ROOT/'analysis/electron-calibration-check-result.json',curve]
    hashes={str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    bon=json.loads(paths[0].read_text(encoding='utf-8'))['samples']
    eledata=json.loads(paths[1].read_text(encoding='utf-8'))
    if hashlib.sha256(curve.read_bytes()).hexdigest()!=eledata['curve_sha256']:raise ValueError('Curve mismatch')
    ele=eledata['selected_inputs']
    rows=sorted(tuple(map(float,l.split(',')[:3])) for l in curve.read_text().splitlines() if l and not l.startswith('#'))
    xs,means,sigmas=map(list,zip(*rows));years=[1+i*step for i in range(round(1949/step)+1)]
    def likelihood(samples):
        out=[]
        for t in years:
            total=0
            for s in samples:
                bp=1950-t+s['offset'];v=s['sigma']**2+interpolate(xs,sigmas,bp)**2
                total-=.5*((s['age']-interpolate(xs,means,bp))**2/v+math.log(v))
            out.append(total)
        return out
    bon=[dict(tree=s['tree'],age=s['conventional_BP'],sigma=s['error_1sigma'],offset=s['offset_to_final_ring_years']) for s in bon]
    variants={}
    for name,bs,es in [('all',bon,ele),('omit_Perham', [s for s in bon if s['tree']!='Perham Creek'],ele),('omit_ELE01',bon,[s for s in ele if s['tree']!='ELE01'])]:
        a=likelihood(bs);b=likelihood(es)
        variants[name]={'assay_counts':[len(bs),len(es)],'unrestricted_modes_CE':[years[a.index(max(a))],years[b.index(max(b))]],'fits':[constrained_fit(years,a,b,d) for d in [0,1,10,25,50,100]]}
    return {'input_hashes':hashes,'step_years':step,'domain_CE':[1,1950],'variants':variants,'limits':['Conditional maximum-likelihood comparison only; neither p-value nor Bayes factor nor probability of catastrophe.','Independent Gaussian errors and fixed offsets inherited from prior simplified checks; covariance and within-sample averaging omitted.','Event association and relative rings assumed; no independent chronological validation.','Duration permits either date order and constrains separation only, not continuous activity or common cause.'],'scientific_validation':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('curve',type=Path);a=p.parse_args()
    result=run(a.curve)
    (ROOT/'analysis/regional-duration-fit-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for k,v in result['variants'].items(): print(k,[(f['maximum_separation_years'],round(f['log_likelihood_loss'],4)) for f in v['fits']])
