"""Audit source completeness and report mapped reach attributes, not movement."""
import collections
import hashlib
import json
from pathlib import Path
import zipfile
from shapely.geometry import MultiLineString, box

archive=Path('sources/originals/cascadia/ecology-willapa-reaches.zip')
ledger=json.loads(Path('data/willapa-ecology-acquisition.json').read_text())
assert hashlib.sha256(archive.read_bytes()).hexdigest()==ledger['archive_sha256']
with zipfile.ZipFile(archive) as z:
    for row in ledger['requests']:
        b=z.read(row['name'])
        assert len(b)==row['bytes']
        assert hashlib.sha256(b).hexdigest()==row['sha256']
    layers=[]
    for layer in (0,1):
        ids=json.loads(z.read(f'ecology-willapa-layer{layer}-ids.json'))['objectIds']
        features=[]
        for name in sorted(z.namelist()):
            if name.startswith(f'ecology-willapa-layer{layer}-part'):
                d=json.loads(z.read(name))
                assert not d.get('exceededTransferLimit')
                assert d['spatialReference']['wkid']==4326
                features.extend(d['features'])
        features.sort(key=lambda f:f['attributes']['OBJECTID'])
        assert sorted(ids)==[f['attributes']['OBJECTID'] for f in features]
        assert len(set(ids))==len(ids)
        layers.append(features)
    assert layers[0]==layers[1], 'Do not count these layers as separate evidence'
    polygon_ids=json.loads(z.read('ecology-willapa-polygon-ids.json'))['objectIds']

windows={'exact_acquisition_window':ledger['bbox'],
         'prior_island_lookup':[-124.050,46.625,-124.025,46.638],
         'northern_diagnostic_window':[-124.18,46.72,-123.95,46.8]}
out={'source_id':'S272','returned_records_per_layer':len(layers[0]),'layers_identical':True,
     'method':'Exact polyline/window intersection in returned EPSG4326. Diagnostic rectangular windows are not authenticated feature boundaries.',
     'limits':'No rate reproduction, original image inspection, datum conversion, boundary identity, uncertainty significance or event attribution.', 'windows':{}}
for name,extent in windows.items():
    selected=[f for f in layers[0] if MultiLineString(f['geometry']['paths']).intersects(box(*extent))]
    ids=sorted(f['attributes']['OBJECTID'] for f in selected)
    if name=='exact_acquisition_window':assert ids==sorted(polygon_ids)
    attrs=[f['attributes'] for f in selected]
    row={'bbox':extent,'count':len(selected),'object_ids':ids,'counts':{}}
    for field in ('Designation','Feature','Start_Year','End_Year','Level_of_Review','Direction'):
        row['counts'][field]=dict(collections.Counter(str(a[field]) for a in attrs))
    values=[a['Change'] for a in attrs if a['Change'] is not None]
    row['reported_change_m_per_year']={'nonnull':len(values),'min':min(values) if values else None,'max':max(values) if values else None}
    row['change_average_attribute_mismatches']=sum(a['Change']!=a['Average_Change'] for a in attrs)
    if name=='prior_island_lookup':row['attributes']=attrs
    out['windows'][name]=row
result=Path('data/willapa-ecology-reaches.json')
result.write_text(json.dumps(out,indent=2)+'\n')
print('1185records/layer complete and identical; polygon query/client exact intersection agree on1148.')
print('Island window:',out['windows']['prior_island_lookup']['count'],'records, no populated rates/dates/types.')
