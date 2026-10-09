"""Read modern source shapefiles and select declared comparable classes."""
from pathlib import Path
import collections,hashlib,json,math,zipfile
import shapefile
import pyproj
from pyproj import CRS

zip_path=Path('sources/originals/cascadia/WA0401D.zip')
folder=Path('tmp/research/WA0401D')
folder.mkdir(exist_ok=True)
with zipfile.ZipFile(zip_path) as z:
    assert all('/' not in n and '\\' not in n for n in z.namelist())
    z.extractall(folder)
    members=[{'name':i.filename,'bytes':i.file_size,'sha256':hashlib.sha256(z.read(i.filename)).hexdigest()} for i in z.infolist()]
historical=json.loads(Path('data/willapa-vector-audit.json').read_text())['tables']['wc46c03lines_83']['geometry_records']
bounds=[min(g['bounds'][0] for g in historical),min(g['bounds'][1] for g in historical),max(g['bounds'][2] for g in historical),max(g['bounds'][3] for g in historical)]
def intersects(b):
    return b[0]<=bounds[2] and b[2]>=bounds[0] and b[1]<=bounds[3] and b[3]>=bounds[1]
out={};selected=[]
for name in ['softcopyl1','softcopyp1','projbnd']:
    reader=shapefile.Reader(str(folder/name))
    crs=(folder/(name+'.prj')).read_text()
    parsed=CRS.from_wkt(crs)
    underlying=parsed.source_crs if parsed.is_bound else parsed
    assert underlying.equals(CRS.from_epsg(4269),ignore_axis_order=True)
    records=[r.as_dict() for r in reader.records()]
    shapes=reader.shapes()
    assert len(records)==len(shapes)
    for shape in shapes:
        assert all(math.isfinite(x) and math.isfinite(y) for x,y in shape.points)
        assert all(-180<=x<=180 and -90<=y<=90 for x,y in shape.points)
        if hasattr(shape,'bbox'):
            actual=[min(p[0] for p in shape.points),min(p[1] for p in shape.points),max(p[0] for p in shape.points),max(p[1] for p in shape.points)]
            assert all(abs(a-b)<1e-10 for a,b in zip(actual,shape.bbox))
    counts={}
    for key in ['FEATURE','ATTRIBUTE','CLASS','SRC_DATE','INFORM','HOR_ACC','SOURCE_ID']:
        if records and key in records[0]:counts[key]=dict(collections.Counter(str(r[key]) for r in records))
    overlap=[(shape,row) for shape,row in zip(shapes,records) if intersects(shape.bbox if hasattr(shape,'bbox') else [*shape.points[0],*shape.points[0]])]
    out[name]={'count':len(reader),'shape_type':reader.shapeType,'bounds':list(reader.bbox),'crs_wkt':crs,'is_bound_crs':parsed.is_bound,'underlying_crs_epsg':underlying.to_epsg(),'attribute_counts':counts,
               'historical_extent_bbox_overlap_count':len(overlap),
               'overlap_attribute_counts':{key:dict(collections.Counter(str(r[key]) for s,r in overlap)) for key in ['FEATURE','ATTRIBUTE','CLASS','SRC_DATE'] if records and key in records[0]}}
    if name=='softcopyl1':
        ids=[r['FEATURE_ID'] for r in records];assert len(ids)==len(set(ids))
        assert set(r['SOURCE_ID'] for r in records)=={'GC10747'}
        for s,r in overlap:
            code=int(r['FEATURE']);assert code==r['FEATURE']
            if code not in (15,20):continue
            assert r['CLASS']=='SHORELINE'
            assert r['ATTRIBUTE']=={15:'Natural.Apparent.Marsh Or Swamp',20:'Natural.Mean High Water'}[code]
            starts=list(s.parts);n=len(s.points)
            assert starts[0]==0 and all(a<b for a,b in zip(starts,starts[1:]))
            selected.append({'attributes':r,'bounds':list(s.bbox),'parts':[list(map(list,s.points[a:b])) for a,b in zip(starts,starts[1:]+[n])]})
summary={'source_id':'S257','pyshp_version':shapefile.__version__,'pyproj_version':pyproj.__version__,'archive_sha256':hashlib.sha256(zip_path.read_bytes()).hexdigest(),'members':members,'tables':out,
         'historical_bbox_wsen':bounds,'selection':'Bbox intersection with complete historical line extent, then exact Feature15/20; includes whole intersecting features, not clipped geometry.',
         'selected_count':len(selected),'selected_class_counts':dict(collections.Counter(str(r['attributes']['FEATURE']) for r in selected)),
         'selected_date_counts':dict(collections.Counter(r['attributes']['SRC_DATE'] for r in selected)),
         'limits':'Bbox intersection is coarse spatial eligibility, not source-frame or coast-segment identity. PRJ generic NAD83 does not encode report CORS96 epoch2002. No displacement or feature authenticity validation.'}
Path('data/willapa-modern-vector-audit.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
Path('data/willapa-modern-comparison-lines.json').write_text(json.dumps({'source_id':'S257','declared_crs':'NAD83 geographic, EPSG4269; report control CORS96 epoch2002 retained separately','selection':summary['selection'],'records':selected},indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k not in ['members','tables']},indent=2))
print(json.dumps(out['softcopyl1']['overlap_attribute_counts'],indent=2))
