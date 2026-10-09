"""Audit reported sediment observations; no event-age or hydraulic fit."""
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import statistics
import zipfile

ROOT = Path(__file__).resolve().parents[1]
acq = json.loads((ROOT/'data/cascadia-field-acquisition.json').read_text())
item = next(f for f in acq['files'] if f['name']=='plain.zip')
raw = (ROOT/item['file']).read_bytes()
assert hashlib.sha256(raw).hexdigest()==item['sha256']
z = zipfile.ZipFile(io.BytesIO(raw))
def read(name):
    return list(csv.DictReader(io.StringIO(z.read(name).decode('cp1252'))))
def clean(r):
    return {k: v for k,v in r.items() if k and v.strip()}
def distance(a,b):
    # Explicit spherical diagnostic, not a survey or datum conversion.
    lat1,lat2=map(math.radians,[float(a['Latitude']),float(b['Latitude'])])
    dl=math.radians(float(b['Longitude'])-float(a['Longitude']))
    h=math.sin((lat2-lat1)/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dl/2)**2
    return 6371008.8*2*math.asin(math.sqrt(h))

names=['18_Copalis_vented_sand.csv','03_Soil_stratigraphy.csv','06_Radiocarbon_ages.csv']
records=[clean(r) for r in read(names[0]) if r['FieldID'].strip()]
assert len(records)==68
assert len({r['FieldID'] for r in records})==68
known=[int(r['Sand_cm']) for r in records if 'Sand_cm' in r]
null_ids=[r['FieldID'] for r in records if 'Sand_cm' not in r]
zero_ids=[r['FieldID'] for r in records if r.get('Sand_cm')=='0']
assert null_ids==['E22']
assert set(zero_ids)=={'T7','E26','SL86-66'}
assert len(known)==67 and len([n for n in known if n>0])==64
methods={m:sum(r['Method']==m for r in records) for m in ['Boring','Trench','Bank']}
vents=[r['FieldID'] for r in records if r.get('Vent')=='Observed']

soil_rows=[clean(r) for r in read(names[1]) if r['Estuary']=='Copalis River']
groups={}
for r in soil_rows:
    groups.setdefault(r['FieldID'],[]).append(r)
crosswalk=[]
for r in records:
    # Exact source labels only. Composite labels are retained without guessing.
    if r['FieldID'] not in groups:
        continue
    linked=sorted(groups[r['FieldID']],key=lambda x:int(x['LocSeq']))
    coordinates={(x['Longitude'],x['Latitude']) for x in linked}
    assert len(coordinates)==1
    crosswalk.append({'field_id':r['FieldID'],'table18_row':r,'table3_rows':linked,
                      'coordinate_separation_metres':distance(r,linked[0])})
inversions=[]
for field,linked in groups.items():
    linked=sorted(linked,key=lambda x:int(x['LocSeq']))
    for a,b in zip(linked,linked[1:]):
        if 'Depth' in a and 'Depth' in b and float(b['Depth'])<float(a['Depth']):
            inversions.append({'field_id':field,'upper_sequence_row':a,
                               'lower_sequence_row':b,
                               'depth_difference_metres':float(b['Depth'])-float(a['Depth'])})
assert {r['field_id'] for r in inversions}=={'T6','T1','A31'}
assays=[clean(r) for r in read(names[2]) if r['Estuary']=='Copalis River' and r['CorrSoil']=='Ws']
assert len(assays)==10
assert sum(r.get('Disc')=='yes' for r in assays)==1
for r in assays:
    assert math.isclose(float(r['Err_rep'])*float(r['Err_mult']),float(r['Err_used']))

out={'status':'SOURCE_SEDIMENT_CONTEXT_AUDIT_NOT_PHYSICAL_OR_AGE_REPRODUCTION',
     'source_id':'S244','zip_sha256':item['sha256'],
     'member_sha256':{n:hashlib.sha256(z.read(n)).hexdigest() for n in names},
     'summary':{'records':len(records),'known_thickness_records':len(known),
                'positive_thickness_records':64,'zero_thickness_ids':zero_ids,
                'unknown_thickness_ids':null_ids,'thickness_cm_min':min(known),
                'thickness_cm_max':max(known),'thickness_cm_median':statistics.median(known),
                'method_counts':methods,'observed_vent_ids':vents,
                'observed_vent_records':len(vents),'unmarked_vent_records':len(records)-len(vents),
                'exact_label_crosswalk_count':len(crosswalk),
                'copalis_ws_assays':len(assays)},
     'table18_records':records,'exact_label_stratigraphy_crosswalk':crosswalk,
     'table3_depth_order_inversions':inversions,'table6_ws_assays':assays,
     'distance_model':'Haversine, sphere radius6371008.8m; WGS84 source coordinates, no datum correction; diagnostic only',
     'limits':['Blank Vent is not absence; unknown thickness is not zero.',
               'Representative depth values with inversions are not silently repaired.',
               'Table6 dates are inherited material ages with limiting relations, not ten direct event dates.',
               'Sampling is purposive; thickness statistics do not estimate areal volume or prevalence.',
               'No duration, absolute date, fluid source, discharge or global correlation established.']}
(ROOT/'data/copalis-vented-sand.json').write_text(json.dumps(out,indent=2)+'\n')
features=[]
for r in records:
    features.append({'type':'Feature','geometry':{'type':'Point','coordinates':[
        float(r['Longitude']),float(r['Latitude'])]},'properties':{
        'source_id':'S244','source_table':18,'field_id':r['FieldID'],
        'reported_method':r['Method'],'reported_date':r['Date'],
        'reported_sand_cm':int(r['Sand_cm']) if 'Sand_cm' in r else None,
        'reported_vent':'Observed' if r.get('Vent')=='Observed' else None,
        'source_comments':r.get('Comments'),
        'status':'REPORTED_NOT_INDEPENDENTLY_SURVEYED_OR_DATED'}})
(ROOT/'data/copalis-vented-sand.geojson').write_text(json.dumps(
    {'type':'FeatureCollection','features':features},indent=2)+'\n')
print(json.dumps(out['summary'],indent=2))
print('Nonzero coordinate separations:',[(r['field_id'],round(r['coordinate_separation_metres'],2))
      for r in crosswalk if r['coordinate_separation_metres']>0])
