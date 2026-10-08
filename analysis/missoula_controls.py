"""Audit transcribed elevations; this does not simulate floods or fit water stages."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def audit(data):
    rows = data['controls']
    assert len({r['id'] for r in rows}) == len(rows)
    result = []
    for r in rows:
        assert r['constraint'] in {'minimum', 'maximum'}
        assert -90 <= r['latitude'] <= 90 and -180 <= r['longitude'] <= 180
        delta = r['field_elevation_m'] - r['terrain_elevation_m']
        result.append({'id': r['id'], 'field_minus_terrain_m': delta})
    canonical = json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    return {
        'input_sha256_canonical_json': hashlib.sha256(canonical.encode()).hexdigest(),
        'quantity': 'field elevation minus terrain elevation, not flood-stage residual',
        'results': result,
        'simulation_executed': False,
        'independent_scientific_validation': False,
    }


if __name__ == '__main__':
    data = json.loads((ROOT / 'data/missoula-controls.json').read_text(encoding='utf-8'))
    output = ROOT / 'analysis/missoula-controls-result.json'
    output.write_text(json.dumps(audit(data), indent=2) + '\n', encoding='utf-8')
    print(f'Audited {len(data["controls"])} transcribed controls; no hydraulic model run.')
