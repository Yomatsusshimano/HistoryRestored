"""Conditional threshold and simple weighted-fit sensitivity, not published Bayesian fit."""
import json,math
from pathlib import Path
rows=json.loads(Path('data/colorado-burial-rows.json').read_text(encoding='utf-8'))['rows']
checks=[]
for r in rows:
    if not r['excluded_in_source']:continue
    b,al,sb,sa=[r[k] for k in ('Be10_atoms_g','Al_column_atoms_g','Be10_one_sigma','Al_column_one_sigma')]
    residual=al-6.75*b; sigma=math.hypot(sa,6.75*sb)
    checks.append({'sample':r['id'],'residual_atoms_g':residual,'sigma_residual_zero_covariance':sigma,'scaled_residual_fixed_ratio':residual/sigma,'scaled_residual_with_3percent_ratio_uncertainty':residual/math.sqrt(sigma*sigma+(.03*6.75*b)**2)})
def wls(rs):
    weights=[1/r['Al_column_one_sigma']**2 for r in rs];sw=sum(weights)
    xb=sum(w*r['Be10_atoms_g'] for w,r in zip(weights,rs))/sw;yb=sum(w*r['Al_column_atoms_g'] for w,r in zip(weights,rs))/sw
    slope=sum(w*(r['Be10_atoms_g']-xb)*(r['Al_column_atoms_g']-yb) for w,r in zip(weights,rs))/sum(w*(r['Be10_atoms_g']-xb)**2 for w,r in zip(weights,rs))
    return {'samples':[r['id'] for r in rs],'slope':slope,'intercept_atoms_g':yb-slope*xb}
pvd=[r for r in rows if r['id'].startswith('PVD')];ret=[r for r in pvd if not r['excluded_in_source']]
result={'source_id':'S216','assumptions':'Al column interpreted as26Al for this conditional calculation despite printed27Al header. Measurement covariance unavailable and set to zero only as an explicit assumption.','threshold_checks':checks,'threshold_limits':'Scaled residuals are diagnostics, not p-values. 3percent ratio term is a common model uncertainty, not independent evidence per sample.','palo_verde_WLS':{'retained_three':wls(ret),'restore_PVD021':wls(ret+[r for r in pvd if r['id']=='PVD021']),'all_five':wls(pvd)},'fit_limits':'WLS weights only Al errors, treats Be as exact, includes an intercept; no Bayesian priors, errors-in-variables, covariance, erosion or post-burial correction. Slopes are not new burial ages or independent validation.'}
Path('data/burial-exclusion-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result['palo_verde_WLS'],indent=2))
