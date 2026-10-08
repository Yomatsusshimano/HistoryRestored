"""Audit transcribed elevations; this does not simulate floods or fit water stages."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def spherical_distance(a, b, radius=6371008.8):
    """Approximate distance; an explicitly assumed sphere, not a datum transformation."""
    lat1, lat2 = map(math.radians, [a['latitude'], b['latitude']])
    dlon = math.radians(b['longitude'] - a['longitude'])
    h = math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return 2*radius*math.asin(math.sqrt(max(0.0, min(1.0, h))))


def audit(data):
    rows = data['controls']
    assert len({r['id'] for r in rows}) == len(rows)
    result = []
    for r in rows:
        assert r['constraint'] in {'minimum', 'maximum'}
        assert -90 <= r['latitude'] <= 90 and -180 <= r['longitude'] <= 180
        terrain = r['terrain_elevation_m']
        delta = None if terrain is None else r['field_elevation_m'] - terrain
        result.append({'id': r['id'], 'field_minus_terrain_m': delta,
                       'terrain_comparison_available': terrain is not None})
    canonical = json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    indexed = {r['id']: r for r in rows}
    pairs = [('Long-10', 'Long-11'), ('Long-11', 'Long-12'), ('Long-10', 'Long-12'),
             ('Baker-5-uncrossed', 'Baker-5-crossed'), ('Baker-8-uncrossed', 'Baker-8-crossed')]
    distances = []
    for first, second in pairs:
        a, b = indexed[first], indexed[second]
        sphere = spherical_distance(a, b)
        projected = math.hypot(b['x_albers_m']-a['x_albers_m'], b['y_albers_m']-a['y_albers_m'])
        distances.append({'first':first, 'second':second, 'spherical_distance_m':sphere,
                          'projected_distance_m':projected, 'projected_over_spherical':projected/sphere})
    return {
        'input_sha256_canonical_json': hashlib.sha256(canonical.encode()).hexdigest(),
        'quantity': 'field elevation minus terrain elevation, not flood-stage residual',
        'results': result,
        'missing_terrain_ids': [r['id'] for r in rows if r['terrain_elevation_m'] is None],
        'distance_method': 'Haversine on assumed radius 6371008.8 m sphere versus Euclidean distance in printed projected coordinates; not a CRS transformation or formal error test.',
        'distance_pairs': distances,
        'simulation_executed': False,
        'independent_scientific_validation': False,
    }


if __name__ == '__main__':
    data = json.loads((ROOT / 'data/missoula-controls.json').read_text(encoding='utf-8'))
    output = ROOT / 'analysis/missoula-controls-result.json'
    output.write_text(json.dumps(audit(data), indent=2) + '\n', encoding='utf-8')
    print(f'Audited {len(data["controls"])} transcribed controls; no hydraulic model run.')
