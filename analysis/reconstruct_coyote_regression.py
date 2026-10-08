"""Candidate reconstruction from Figure 2 readings; not author-supplied inputs."""
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ages = np.array([20.87, 16.77, 14.01, 10.88])
levels = np.array([35., 26., 14., 11.])
y = -levels
# Center/scale age before solving to reduce conditioning effects.
center, scale = float(ages.mean()), float(ages.std())
z = (ages-center)/scale
design = np.column_stack([z*z, z, np.ones(4)])
beta, _, rank, _ = np.linalg.lstsq(design, y, rcond=None)
a = beta[0]/scale**2
b = beta[1]/scale - 2*center*a
c = beta[2] - beta[1]*center/scale + a*center**2
coef = np.array([a,b,c])
assert rank == 3
assert np.allclose(coef, np.polyfit(ages,y,2), rtol=1e-9, atol=1e-9)
residuals = y-np.polyval(coef,ages)
assert np.max(np.abs(design.T @ residuals)) < 1e-10
r2 = float(1-np.sum(residuals**2)/np.sum((y-y.mean())**2))
rounded = [round(float(a),4),round(float(b),4),round(float(c),3)]
assert rounded == [-0.0641,-0.5114,3.031]
assert round(r2,3) == .961
result = {
    'source_id':'S138',
    'locator':'Figure 2, printed p.4 / repository PDF p.6; ages from chronology text',
    'input_status':'Candidate integer levels read from plotted points; not recovered author input file.',
    'model':'Unweighted ordinary least squares of negative excavation level on age and age squared; age treated as exact for this reconstruction.',
    'rows':[{'sample_id':f'CCMS-OSL-{i+1}', 'age_ka':float(x),
             'candidate_level':float(l), 'residual_negative_levels':float(r)}
            for i,(x,l,r) in enumerate(zip(ages,levels,residuals))],
    'coefficients_descending':coef.tolist(),
    'coefficients_rounded_as_figure':rounded,
    'R_squared':r2,
    'residual_degrees_of_freedom':1,
    'checks':'Centered least squares agrees with numpy.polyfit; normal-equation orthogonality and printed rounding checks pass.',
    'numpy_version':np.__version__,
    'limits':[
        'Matching rounded coefficients and R squared supports this reconstruction but does not prove unique inputs or original settings.',
        'Sample levels need independent survey and bed correlation, including conversion from original OSL locations.',
        'No measurement-error model, shared error covariance, age confidence interval or geological validation reproduced.',
        'The two fossil ages are derived from the same four-point curve and cannot be treated as independent assays.',
    ],
}
(ROOT/'data/coyote-regression-reconstruction.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
