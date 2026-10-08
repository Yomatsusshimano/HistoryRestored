"""Simplified fixed-offset likelihood check; NOT an OxCal reproduction."""
import argparse,bisect,hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def interpolate(xs,ys,x):
    if x<xs[0] or x>xs[-1]: raise ValueError('Outside calibration curve')
    i=bisect.bisect_left(xs,x)
    if xs[i]==x:return ys[i]
    w=(x-xs[i-1])/(xs[i]-xs[i-1])
    return ys[i-1]*(1-w)+ys[i]*w

def summarize(years,logs):
    peak=max(logs); weights=[math.exp(v-peak) for v in logs]; total=sum(weights)
    def q(p):
        acc=0
        for year,w in zip(years,weights):
            acc+=w/total
            if acc>=p:return year
        return years[-1]
    return {'mode_CE':years[logs.index(peak)],'equal_tail_95_4_CE':[q(.023),q(.977)],'equal_tail_99_7_CE':[q(.0015),q(.9985)],'edge_mass_first_last_10_years':sum(w for y,w in zip(years,weights) if y<=11 or y>=1940)/total}

def run(curve,step):
    raw=curve.read_bytes(); rows=sorted(tuple(map(float,l.split(',')[:3])) for l in raw.decode().splitlines() if l and not l.startswith('#'))
    xs,means,sigmas=map(list,zip(*rows))
    source=ROOT/'data/bonneville-dates.json'; data=json.loads(source.read_text(encoding='utf-8'))
    years=[1+i*step for i in range(round(1949/step)+1)]
    variants={}
    for omitted in [None,'Powerhouse','Wyeth','Perham Creek']:
        samples=[s for s in data['samples'] if s['tree']!=omitted]
        logs=[]
        for death in years:
            log=0
            for s in samples:
                calbp=1950-death+s['offset_to_final_ring_years']
                mean=interpolate(xs,means,calbp); sigma=interpolate(xs,sigmas,calbp)
                variance=s['error_1sigma']**2+sigma**2
                log+=-.5*((s['conventional_BP']-mean)**2/variance+math.log(variance))
            logs.append(log)
        variants[omitted or 'all_trees']=dict(samples=len(samples),**summarize(years,logs))
    return {'source_ids':['S68','S128'],'assay_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'curve_sha256':hashlib.sha256(raw).hexdigest(),'curve_rows':len(rows),'grid_step_years':step,'prior':'Uniform death year 1 to 1950 CE, discrete grid.','method':'Product of Gaussian radiocarbon likelihoods at fixed ring-centroid offsets; linearly interpolated curve mean and sigma; assay and curve variances added.','limitations':['Not OxCal; no Offset uncertainty integration or Combine algorithm reproduction.','No within-sample ring averaging.','Shared calibration-curve covariance and assay dependence omitted.','Reported equal-tail intervals may differ from published interval construction.','Omitting a tree is sensitivity, not independent validation.','Source unit and sample context assumptions retained.'],'variants':variants,'scientific_validation':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('curve',type=Path);p.add_argument('--step',type=float,default=.25)
    a=p.parse_args()
    if a.step<=0 or 1949/a.step!=round(1949/a.step):raise ValueError('Step must exactly divide grid span')
    result=run(a.curve,a.step)
    (ROOT/'analysis/bonneville-calibration-check-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result['variants'],indent=2))
