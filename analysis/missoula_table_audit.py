"""Screen the complete published control table; no hydraulic model or CRS fit."""
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from missoula_controls import spherical_distance

ROOT = Path(__file__).resolve().parents[1]


def audit(data):
    rows = data['controls']
    assert [r['table_row'] for r in rows] == list(range(1, 48))
    assert len({r['id'] for r in rows}) == 47
    vertical = []
    conversions = []
    pairs = []
    nearby_opposed = []
    for row in rows:
        assert row['constraint'] == ('maximum' if row['source_shaded_nonexceedance'] else 'minimum')
        z = row['terrain_elevation_m']
        vertical.append(dict(id=row['id'], table_row=row['table_row'],
                             field_minus_terrain_m=None if z is None else row['field_elevation_m']-z))
        ft = row['field_elevation_ft']
        if ft is not None:
            delta = row['field_elevation_m'] - 0.3048*ft
            conversions.append(dict(id=row['id'], metres_minus_03048_feet=delta,
                                    outside_half_metre_rounding=abs(delta)>0.5000001))
    for i, a in enumerate(rows):
        for b in rows[i+1:]:
            sphere = spherical_distance(a, b)
            if sphere > 15000:
                continue
            if a['constraint'] != b['constraint'] and sphere < 250:
                lower, upper = (a,b) if a['constraint']=='minimum' else (b,a)
                nearby_opposed.append(dict(lower_id=lower['id'], upper_id=upper['id'],
                    spherical_separation_m=sphere,
                    upper_minus_lower_field_elevation_m=upper['field_elevation_m']-lower['field_elevation_m'],
                    interpretation='Different sites; not a measured water-level interval. No common event or level-water assumption established.'))
            if a['x_albers_m'] is None or b['x_albers_m'] is None:
                continue
            assert sphere > 0
            projected = math.hypot(b['x_albers_m']-a['x_albers_m'], b['y_albers_m']-a['y_albers_m'])
            ratio = projected/sphere
            pairs.append(dict(first_id=a['id'], second_id=b['id'], spherical_distance_m=sphere,
                              projected_distance_m=projected, projected_over_spherical=ratio,
                              projected_minus_spherical_m=projected-sphere,
                              outside_screen_band=not 0.95 <= ratio <= 1.05))
    canonical = json.dumps(data,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    return dict(input_sha256_canonical_json=hashlib.sha256(canonical.encode()).hexdigest(),
        row_count=len(rows), bound_counts=dict(Counter(r['constraint'] for r in rows)),
        missing_projected_or_terrain_ids=[r['id'] for r in rows if any(r[k] is None for k in ('x_albers_m','y_albers_m','terrain_elevation_m'))],
        vertical_comparisons=vertical, feet_metres_diagnostics=conversions,
        nearby_coordinate_pairs=pairs, nearby_opposed_constraints=nearby_opposed,
        screen_definition='All pairs within 15 km on an assumed 6371008.8 m sphere; flag projected/spherical ratio outside 0.95-1.05. Retrospective diagnostic thresholds, not statistical errors, source CRS parameters, validation or rejection criteria.',
        opposed_constraint_screen='All opposite-bound pairs separated by less than 250 m on the same assumed sphere. Retrospective proximity selection, not proof of shared stage, event or uncertainty.',
        conversion_definition='Literal m minus 0.3048 times literal ft; half-metre screen assumes nearest whole-metre conversion only. Differing source precision/rounding may explain small flags. No field elevations corrected.',
        hydraulic_simulation_executed=False, independent_scientific_validation=False)


if __name__ == '__main__':
    data=json.loads((ROOT/'data/missoula-table1.json').read_text(encoding='utf-8'))
    result=audit(data)
    (ROOT/'analysis/missoula-table-audit-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Complete table:', result['row_count'], 'rows;', result['bound_counts'])
    print('Missing registration:',result['missing_projected_or_terrain_ids'])
    print('Coordinate flags:',[(p['first_id'],p['second_id'],round(p['projected_over_spherical'],6)) for p in result['nearby_coordinate_pairs'] if p['outside_screen_band']])
    print('Conversion flags:',[(r['id'],round(r['metres_minus_03048_feet'],6)) for r in result['feet_metres_diagnostics'] if r['outside_half_metre_rounding']])
    print('Nearby opposed bounds:',result['nearby_opposed_constraints'])
