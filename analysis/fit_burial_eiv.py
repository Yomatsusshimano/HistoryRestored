"""Independent profile chi-square diagnostic; not the source Bayesian model.

Run from repository root using Python 3 (standard library only).
"""
import json
import math
from pathlib import Path


def profile(rows, m):
    variances = [r['Al_column_one_sigma']**2 + m*m*r['Be10_one_sigma']**2 for r in rows]
    offsets = [r['Al_column_atoms_g'] - m*r['Be10_atoms_g'] for r in rows]
    b = sum(d/v for d, v in zip(offsets, variances))/sum(1/v for v in variances)
    residuals = [(d-b)/math.sqrt(v) for d, v in zip(offsets, variances)]
    return sum(r*r for r in residuals), b, residuals


def golden(f, a, b):
    ratio = (math.sqrt(5)-1)/2
    c, d = b-ratio*(b-a), a+ratio*(b-a)
    fc, fd = f(c), f(d)
    for _ in range(100):
        if b-a < 1e-11:
            break
        if fc < fd:
            b, d, fd = d, c, fc
            c = b-ratio*(b-a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a+ratio*(b-a)
            fd = f(d)
    return (a+b)/2


def fit(rows, grid_n=4096):
    # Examine every grid-local minimum, then refine; retain both endpoints.
    grid = [6.75*i/grid_n for i in range(grid_n+1)]
    f = lambda m: profile(rows, m)[0]
    values = [f(m) for m in grid]
    candidates = [0., 6.75]
    for i in range(1, grid_n):
        if values[i] <= values[i-1] and values[i] <= values[i+1]:
            candidates.append(golden(f, grid[i-1], grid[i+1]))
    m = min(candidates, key=f)
    q, b, residuals = profile(rows, m)
    return {'samples': [r['id'] for r in rows], 'n': len(rows),
            'slope': m, 'intercept_atoms_g': b, 'Q': q,
            'nominal_degrees_of_freedom': len(rows)-2, 'Q_over_n_minus_2': q/(len(rows)-2),
            'at_slope_boundary': m in (0., 6.75),
            'standardized_residuals': dict(zip([r['id'] for r in rows], residuals))}


def verify():
    # Equal errors permit an independent closed-form Deming-regression check.
    points = [(1, 4), (2, 5), (3, 8), (5, 10), (7, 16)]
    rows = [{'id': str(i), 'Be10_atoms_g': x, 'Al_column_atoms_g': y,
             'Be10_one_sigma': .5, 'Al_column_one_sigma': 1.} for i, (x, y) in enumerate(points)]
    xb = sum(x for x, y in points)/len(points)
    yb = sum(y for x, y in points)/len(points)
    xx = sum((x-xb)**2 for x, y in points)
    yy = sum((y-yb)**2 for x, y in points)
    xy = sum((x-xb)*(y-yb) for x, y in points)
    delta = 4.
    exact = (yy-delta*xx + math.sqrt((yy-delta*xx)**2+4*delta*xy*xy))/(2*xy)
    actual = fit(rows)['slope']
    assert abs(actual-exact) < 1e-6, (actual, exact)
    for r in rows:
        r['Al_column_atoms_g'] = 1.25 + 2.5*r['Be10_atoms_g']
    line = fit(rows)
    assert abs(line['slope']-2.5) < 1e-6 and abs(line['intercept_atoms_g']-1.25) < 1e-6
    return {'closed_form_Deming_slope': exact, 'computed_slope': actual,
            'exact_synthetic_line_recovered': True}


if __name__ == '__main__':
    checks = verify()
    rows = json.loads(Path('data/colorado-burial-rows.json').read_text(encoding='utf-8'))['rows']
    groups = []
    max_delta = 0.
    for prefix, name, published in [('TPK', 'Topock', 2.39), ('BC', 'Bat Cave', 2.47),
                                    ('CHM', 'Santa Fe Railway', .79), ('PVD', 'Palo Verde', 1.63)]:
        all_rows = [r for r in rows if r['id'].startswith(prefix)]
        retained = [r for r in all_rows if not r['excluded_in_source']]
        selections = [('source_retained', retained), ('all_measured', all_rows)]
        if prefix == 'PVD':
            selections.append(('restore_PVD021', [r for r in all_rows if not r['excluded_in_source'] or r['id']=='PVD021']))
        results = {}
        for label, selected in selections:
            result = fit(selected)
            finer = fit(selected, 8192)
            difference = abs(finer['slope']-result['slope'])
            assert difference < 1e-6
            max_delta = max(max_delta, difference)
            results[label] = result
        groups.append({'site': name, 'published_rounded_slope': published, 'selections': results})
    checks['max_slope_change_on_grid_doubling'] = max_delta
    output = {
        'source_id': 'S216',
        'model': 'Profile latent-coordinate Gaussian chi-square: Q=sum((y-m*x-b)^2/(sy^2+m^2*sx^2)); at each m, b is weighted mean(y-m*x).',
        'assumptions': ['Al column conditionally interpreted as26Al despite printed27Al header.',
                        'Independent Gaussian measurement errors with supplied one-sigma magnitudes; covariance set to zero because unavailable.',
                        'Slope constrained to [0,6.75] as a declared comparison range; unconstrained intercept.',
                        'No intrinsic scatter, shared systematic errors, erosion correction or full post-burial production model.'],
        'limits': 'Not a Bayesian posterior or marginalized likelihood; no log-variance term. Not reproduction of original MATLAB code. Q/(n-2) and residuals are descriptive, not calibrated p-values. No new exclusion decisions or burial ages.',
        'optimizer': '4096 grid intervals; golden-section refinement at each grid-local minimum; endpoints compared; checked at8192 intervals.',
        'numerical_checks': checks, 'groups': groups}
    Path('data/burial-eiv-fit.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    for group in groups:
        for label, r in group['selections'].items():
            print(group['site'], label, 'n=',r['n'], 'slope=',round(r['slope'],6),
                  'intercept=',round(r['intercept_atoms_g'],2), 'Q/(n-2)=',round(r['Q_over_n_minus_2'],3))
    print('Numerical checks:', checks)
