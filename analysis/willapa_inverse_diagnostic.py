"""Test whether NADCON5's documented one-pass inverse explains residuals."""
from pathlib import Path
import base64, hashlib, json, struct
import numpy as np
import pyproj

pyproj.network.set_network_enabled(False)
pyproj.datadir.append_data_dir(str(Path('tmp/research/proj-grids').resolve()))
path=Path('data/willapa-geodatabase-rows.json')
tables=json.loads(path.read_text(encoding='utf-8-sig'))['tables']
points=[]
for name in ['wc46c03lines','wc46c03polys']:
    for row in tables[name]:
        raw=base64.b64decode(row['Shape']['base64'])
        parts,count=struct.unpack_from('<2I',raw,36)
        points.extend(np.array(struct.unpack_from('<'+'d'*(2*count),raw,44+4*parts)).reshape(-1,2).tolist())
points=np.array(points)
utm=pyproj.Proj(proj='utm',zone=10,ellps='clrk66')
lon,lat=utm(points[:,0],points[:,1],inverse=True)
geod=pyproj.Geod(ellps='clrk66')
results=[]
for interpolation in ['biquadratic','bilinear']:
    pipeline='proj=gridshift grids=us_noaa_nadcon5_nad27_nad83_1986_conus.tif interpolation='+interpolation
    t=pyproj.Transformer.from_pipeline(pipeline)
    outlon,outlat=t.transform(lon,lat,errcheck=True)
    backlon,backlat=t.transform(outlon,outlat,direction='INVERSE',errcheck=True)
    # Forward evaluation at output coordinates supplies shift for one-pass subtraction.
    twice_lon,twice_lat=t.transform(outlon,outlat,errcheck=True)
    guess_lon=2*np.array(outlon)-np.array(twice_lon)
    guess_lat=2*np.array(outlat)-np.array(twice_lat)
    _,_,agreement=geod.inv(backlon,backlat,guess_lon,guess_lat)
    _,_,roundtrip=geod.inv(lon,lat,backlon,backlat)
    assert np.isfinite(agreement).all() and np.isfinite(roundtrip).all()
    results.append({'interpolation':interpolation,'pipeline':pipeline,
                    'max_inverse_vs_one_pass_m':float(np.max(agreement)),
                    'max_roundtrip_m':float(np.max(roundtrip))})
assert results[0]['max_inverse_vs_one_pass_m']<1e-7
assert results[1]['max_roundtrip_m']<1e-6
code=Path('tmp/research/proj-gridshift-9.8.1.cpp')
assert hashlib.sha256(code.read_bytes()).hexdigest()=='e995b384e9a2509df574fcbf0ea7c16e68ac48a222b802f813875a645a12a78b'
out={'source_id':'S253','point_count':len(points),
     'row_export_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
     'pyproj_version':pyproj.__version__,'proj_version':pyproj.proj_version_str,
     'source_code_url':'https://github.com/OSGeo/PROJ/blob/9.8.1/src/transformations/gridshift.cpp#L649',
     'source_code_sha256':hashlib.sha256(code.read_bytes()).hexdigest(),
     'results':results,
     'limits':'Interpolation alternative isolates numerical inverse behavior, not an improved official datum or historical field accuracy. No bilinear replacement of NADCON5 results is made.'}
Path('data/willapa-inverse-diagnostic.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
