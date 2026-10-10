"""Declared correlated-error fit of published ROSER inverse-isotope ratios."""
import hashlib,json,math
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares,minimize_scalar
from scipy.stats import chi2

root=Path(__file__).resolve().parents[1]
path=root/'data/nomlaki2021-plateau.json'
d=json.loads(path.read_text(encoding='utf-8'))
LAMBDA=5.463e-10 # Declared Min-style constant, also explicit in S210; not fitted.

def fit(rows,ignore_correlation=False):
 raw=[r['raw_cells'] for r in rows]
 x=np.array([r[28] for r in raw]);y=np.array([r[26] for r in raw])
 sx=x*np.array([r[29] for r in raw])/100
 sy=y*np.array([r[27] for r in raw])/100
 rho=np.array([r[30] for r in raw])
 if ignore_correlation:rho=np.zeros_like(rho)
 assert np.all(sx>0) and np.all(sy>0) and np.all(abs(rho)<1)
 # Scale coordinates for conditioning, preserving their original covariance.
 X=x/.1;Y=y/.003;SX=sx/.1;SY=sy/.003
 covariance=np.array([[[a*a,c*a*b],[c*a*b,b*b]] for a,b,c in zip(SX,SY,rho)])
 chol=np.linalg.cholesky(covariance)
 def residual(p):
  a,b=p[:2];z=p[2:]
  return np.concatenate([np.linalg.solve(l,[xx-zz,yy-a-b*zz]) for l,xx,yy,zz in zip(chol,X,Y,z)])
 def jacobian(p):
  b=p[1];z=p[2:];J=np.zeros((2*len(rows),2+len(rows)))
  for i,(l,zz) in enumerate(zip(chol,z)):
   block=np.zeros((2,2+len(rows)));block[1,0]=-1;block[1,1]=-zz
   block[0,i+2]=-1;block[1,i+2]=-b
   J[2*i:2*i+2]=np.linalg.solve(l,block)
  return J
 trials=[least_squares(residual,[1.15,b,*X],jac=jacobian,xtol=1e-13,ftol=1e-13,gtol=1e-10,max_nfev=2000) for b in [-1.5,-.8,.2]]
 assert all(t.success for t in trials)
 solution=min(trials,key=lambda t:np.dot(t.fun,t.fun))
 q=float(np.dot(solution.fun,solution.fun));dof=len(rows)-2
 assert max(abs(float(np.dot(t.fun,t.fun))-q) for t in trials)<1e-8
 a=solution.x[0]*.003;b=solution.x[1]*.03
 # Independent parameterization of the same objective, profiling intercept/z.
 def profile(B):
  variance=SY**2+B**2*SX**2-2*B*rho*SX*SY
  w=1/variance;A=np.dot(w,Y-B*X)/w.sum()
  return float(np.dot(w,(Y-A-B*X)**2))
 alt=minimize_scalar(profile,bounds=(-2,.5),method='bounded',options={'xatol':1e-13})
 assert alt.success and abs(alt.fun-q)<1e-8 and abs(alt.x*.03-b)<1e-7
 C=np.linalg.inv(solution.jac.T@solution.jac)[:2,:2]*np.array([[.003**2,.003*.03],[.003*.03,.03**2]])
 R=-b/a;gradient=np.array([b/a**2,-1/a]);sR=math.sqrt(gradient@C@gradient)
 j=raw[0][3]/1000;sj=raw[0][4]/1000
 assert all(r[3:5]==raw[0][3:5] for r in raw)
 age=math.log1p(j*R)/LAMBDA/1e6
 sa=j/(1+j*R)/LAMBDA/1e6*sR
 sJ=R/(1+j*R)/LAMBDA/1e6*sj
 return {'rows':[r['row'] for r in rows],'n':len(rows),'dof':dof,
 'slope':b,'intercept':a,'parameter_covariance':C.tolist(),
 'radiogenic_ar40_ar39':R,'radiogenic_ratio_sem':sR,
 'trapped_ar40_ar36':1/a,'trapped_ratio_sem':math.sqrt(C[0,0])/a**2,
 'Q':q,'mswd':q/dof,'chi_square_upper_tail':float(chi2.sf(q,dof)),
 'age_ma':age,'analytical_sem_ma':sa,'shared_J_sem_ma':sJ,
 'analytical_plus_J_sem_ma':math.hypot(sa,sJ),'J':j,'J_sem':sj,
 'correlations_ignored':ignore_correlation,
 'numerical_checks':{'three_start_objective_agreement':True,'profile_objective_agreement':True}}

selected=[r for r in d['rows'] if r['lab_id_bold']]
base=fit(selected);all_rows=fit(d['rows']);no_rho=fit(selected,True)
# Compatibility diagnostic: implied J from source-derived step ages at fixedlambda.
# This is not a measured J and is never substituted into the fitted age.
implied=[{'row':r['row'],'implied_J':math.expm1(LAMBDA*r['raw_cells'][23]*1e6)/r['raw_cells'][20]} for r in d['rows']]
out={'source_id':'S327','input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'model':'Fixed point-specific bivariate Gaussian covariance; latent true x coordinates; weighted squared Mahalanobis residual minimization',
 'columns':{'x':'AC39Ar/40Ar','x_error':'ADpercent1sigma','y':'AA36Ar/40Ar','y_error':'ABpercent1sigma','rho':'AEerrorcorrelation'},
 'parameter_covariance_scope':'Local linearized covariance; no MSWD contraction or unmeasured calibration covariance',
 'lambda_per_year':LAMBDA,'lambda_basis':'Declared constant explicit in existing S210 methods, consistent with Min-style convention named by S327; exact S327 reduction implementation unverified',
 'baseline':base,'sensitivity_all_nine_steps':all_rows,'sensitivity_zero_point_correlations':no_rho,
 'source_figure4e':{'age_ma':3.339,'error_ma':.015,'trapped_ratio':286.1,'trapped_error':5.8,'mswd':.13,'P':.94,'n':5},
 'implied_J_diagnostic':implied,
 'limits':'Reuses reduced published ratios and author selection. Numerical checks verify this declared model only. No raw gas reduction, full systematic uncertainty, exact author implementation, primary emplacement or target-bed correlation.'}
(root/'data/nomlaki2021-isochron.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k in ['baseline','sensitivity_all_nine_steps','sensitivity_zero_point_correlations']},indent=2))
