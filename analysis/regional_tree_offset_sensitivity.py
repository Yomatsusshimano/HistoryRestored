"""Analyst-selected within-tree systematic-offset sensitivity, not measured errors."""
import argparse,hashlib,json,math
from pathlib import Path
from bonneville_calibration_check import interpolate
from regional_duration_fit import constrained_fit
ROOT=Path(__file__).resolve().parents[1]

def group_loglik(residuals,variances,tau):
    if tau<0 or len(residuals)!=len(variances) or not residuals or min(variances)<=0:
        raise ValueError('Invalid covariance inputs')
    precision=sum(1/v for v in variances)
    weighted=sum(r/v for r,v in zip(residuals,variances))
    factor=1+tau*tau*precision
    quadratic=sum(r*r/v for r,v in zip(residuals,variances))-tau*tau*weighted*weighted/factor
    logdet=sum(math.log(v) for v in variances)+math.log(factor)
    return -.5*(quadratic+logdet)

def run(curve):
    bp=ROOT/'data/bonneville-dates.json';ep=ROOT/'analysis/electron-calibration-check-result.json'
    bondata=json.loads(bp.read_text(encoding='utf-8'));eledata=json.loads(ep.read_text(encoding='utf-8'))
    if hashlib.sha256(curve.read_bytes()).hexdigest()!=eledata['curve_sha256']:raise ValueError('Curve hash mismatch')
    bon=[dict(tree=s['tree'],age=s['conventional_BP'],sigma=s['error_1sigma'],offset=s['offset_to_final_ring_years']) for s in bondata['samples']]
    ele=eledata['selected_inputs']
    rows=sorted(tuple(map(float,l.split(',')[:3])) for l in curve.read_text().splitlines() if l and not l.startswith('#'))
    xs,means,sigmas=map(list,zip(*rows));years=[1+i*.25 for i in range(7797)]
    def prepared(samples):
        groups={tree:[s for s in samples if s['tree']==tree] for tree in sorted({s['tree'] for s in samples})}
        output=[]
        for t in years:
            peryear=[]
            for group in groups.values():
                residuals=[];variances=[]
                for s in group:
                    calbp=1950-t+s['offset']
                    residuals.append(s['age']-interpolate(xs,means,calbp))
                    variances.append(s['sigma']**2+interpolate(xs,sigmas,calbp)**2)
                peryear.append((residuals,variances))
            output.append(peryear)
        return output
    pb,pe=prepared(bon),prepared(ele);out=[]
    for tau in [0,10,25,50,100]:
        a=[sum(group_loglik(rs,vs,tau) for rs,vs in g) for g in pb]
        b=[sum(group_loglik(rs,vs,tau) for rs,vs in g) for g in pe]
        out.append({'tree_offset_sigma_radiocarbon_years':tau,'unrestricted_modes_CE':[years[a.index(max(a))],years[b.index(max(b))]],'fits':[constrained_fit(years,a,b,d) for d in [0,10,50,100]]})
    return {'source_ids':['S68','S72','S128'],'input_hashes':{'bonneville':hashlib.sha256(bp.read_bytes()).hexdigest(),'electron':hashlib.sha256(ep.read_bytes()).hexdigest(),'curve':eledata['curve_sha256']},'method':'Each tree has an independent zero-mean Gaussian age offset b with SD tau; integrate b analytically. Covariance is diag(assay variance + curve variance) + tau^2 11T within each tree. Constants common within each tau comparison omitted.','tau_status':'Illustrative analyst-selected sensitivities, not measured errors or fitted corrections. Units are conventional radiocarbon years, not calendar years.','grid':'1–1950 CE every 0.25 year','results':out,'limitations':['Tree offsets independent across trees and sites; cross-tree calibration covariance not modeled.','No ring-offset uncertainty or within-sample averaging.','No mechanism or empirical prior for these systematic offsets established.','Compare constrained and unrestricted fits within each tau only; no model probabilities or statistical rejection calibration.'],'scientific_validation':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('curve',type=Path);a=p.parse_args();result=run(a.curve)
    (ROOT/'analysis/regional-tree-offset-sensitivity-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for r in result['results']:print(r['tree_offset_sigma_radiocarbon_years'],r['unrestricted_modes_CE'],[round(f['log_likelihood_loss'],4) for f in r['fits']])
