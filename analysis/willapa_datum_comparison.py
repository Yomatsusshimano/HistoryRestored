"""Compare paired stored coordinates; does not measure historical displacement.

Download the two named open grids from https://cdn.proj.org/ into
tmp/research/proj-grids before running. Network transformations are disabled.
"""
from pathlib import Path
import base64, hashlib, json, math, struct
import numpy as np
import pyproj
from pyproj.aoi import AreaOfInterest
from pyproj.transformer import TransformerGroup

def geometry(row):
    raw = base64.b64decode(row['Shape']['base64'])
    kind = struct.unpack_from('<I', raw)[0]
    parts, count = struct.unpack_from('<2I', raw, 36)
    starts = struct.unpack_from('<' + 'I' * parts, raw, 44)
    offset = 44 + 4 * parts
    assert kind in (3, 5) and len(raw) == offset + 16 * count
    return kind, starts, np.array(struct.unpack_from('<' + 'd' * (2 * count), raw, offset)).reshape(-1, 2)

source = Path('data/willapa-geodatabase-rows.json')
tables = json.loads(source.read_text(encoding='utf-8-sig'))['tables']
audit = json.loads(Path('data/willapa-vector-audit.json').read_text())
grids = Path('tmp/research/proj-grids')
grid_records = []
for name in ['us_noaa_nadcon5_nad27_nad83_1986_conus.tif', 'us_noaa_conus.tif']:
    path = grids / name
    raw = path.read_bytes()
    grid_records.append({'name': name, 'url': 'https://cdn.proj.org/' + name,
                         'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
pyproj.network.set_network_enabled(False)
pyproj.datadir.append_data_dir(str(grids.resolve()))
group = TransformerGroup(audit['tables']['wc46c03lines']['stored_crs'],
                         audit['tables']['wc46c03lines_83']['stored_crs'],
                         always_xy=True, allow_ballpark=False,
                         area_of_interest=AreaOfInterest(-124.2, 46.6, -123.8, 46.8))
assert group.best_available and len(group.transformers) >= 2
geod = pyproj.Geod(ellps='GRS80')
results = []
for transform in group.transformers:
    records = []
    residuals = []
    for name, key in [('wc46c03lines', 'OBJECTID'), ('wc46c03polys', 'OID')]:
        counterpart = {r[key]: r for r in tables[name + '_83']}
        for row in tables[name]:
            kind, starts, points = geometry(row)
            otherkind, otherstarts, stored = geometry(counterpart[row[key]])
            assert kind == otherkind and starts == otherstarts and points.shape == stored.shape
            lon, lat = transform.transform(points[:, 0], points[:, 1], errcheck=True)
            backx, backy = transform.transform(lon, lat, direction='INVERSE', errcheck=True)
            roundtrip = np.hypot(backx - points[:, 0], backy - points[:, 1])
            assert np.isfinite(roundtrip).all()
            _, _, distances = geod.inv(lon, lat, stored[:, 0], stored[:, 1])
            assert np.isfinite(distances).all()
            residuals.extend(distances.tolist())
            records.append({'table': name, 'id': row[key], 'point_count': len(points),
                            'max_residual_m': float(np.max(distances)),
                            'rms_residual_m': float(np.sqrt(np.mean(distances ** 2))),
                            'max_roundtrip_m': float(np.max(roundtrip)),
                            'point_residuals_m': distances.tolist()})
    values = np.array(residuals)
    results.append({'operation': transform.description, 'pipeline': transform.definition,
                    'declared_operation_accuracy_m': transform.accuracy,
                    'point_count': len(values), 'feature_count': len(records),
                    'max_residual_m': float(np.max(values)),
                    'median_residual_m': float(np.median(values)),
                    'rms_residual_m': float(np.sqrt(np.mean(values ** 2))),
                    'max_roundtrip_m': max(r['max_roundtrip_m'] for r in records),
                    'records': records})
out = {'source_id': 'S253', 'row_export_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
       'pyproj_version': pyproj.__version__, 'proj_version': pyproj.proj_version_str,
       'network_enabled': False, 'ballpark_allowed': False, 'best_available': group.best_available,
       'grids': grid_records, 'results': results,
       'limits': 'Same-source paired vertices; repeated closure/shared vertices are not independent observations. Residuals test coordinate consistency, not survey accuracy, original workflow identity, coast change or historical displacement.'}
Path('data/willapa-datum-comparison.json').write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
print(json.dumps([{k: v for k, v in r.items() if k != 'records'} for r in results], indent=2))
