"""Retrieve a named later tile at the prior recorded pixel-edge extent."""
from pathlib import Path
import base64,hashlib,json,struct,urllib.parse,urllib.request
import numpy as np
import datetime
from shapely.geometry import Polygon,Point
from PIL import Image

root='https://imagery.geoplatform.gov/iipp/rest/services/NAIP/NAIP2017_CONUS/ImageServer'
base=Path('sources/originals/cascadia/naip2017');base.mkdir(exist_ok=True)
def fetch(endpoint,args,target):
    url=root+endpoint+'?'+urllib.parse.urlencode(args)
    with urllib.request.urlopen(url,timeout=25) as r:b=r.read()
    target.write_bytes(b);d=json.loads(b);assert 'error' not in d,d
    return url,d
service_url,service=fetch('',{'f':'pjson'},base/'service.json')
query_url,query=fetch('/query',{'f':'pjson','where':'category=1','geometry':'-124.050,46.625,-124.025,46.638','geometryType':'esriGeometryEnvelope','inSR':4269,'spatialRel':'esriSpatialRelIntersects','outFields':'*','returnGeometry':'true','outSR':4269},base/'catalog-query.json')
items=[f for f in query['features'] if f['attributes']['name']=='m_4612424_se_10_1_20170827']
assert len(items)==1;item=items[0];assert item['attributes']['year']==2017
footprint=Polygon(item['geometry']['rings'][0]);assert footprint.is_valid
rows=json.loads(Path('data/willapa-geodatabase-rows.json').read_text(encoding='utf-8-sig'))['tables']['wc46c03lines_83']
covered=[]
for row in rows:
    if row['OBJECTID'] not in (49,51):continue
    raw=base64.b64decode(row['Shape']['base64']);parts,n=struct.unpack_from('<2I',raw,36)
    points=np.array(struct.unpack_from('<'+'d'*(2*n),raw,44+4*parts)).reshape(-1,2)
    assert all(footprint.covers(Point(p)) for p in points)
    covered.append({'historical_id':row['OBJECTID'],'vertices':n,'all_vertices_inside_catalog_polygon':True})
prior=json.loads(Path('data/willapa-naip2006-acquisition.json').read_text())
e=prior['returned_extent'];size=prior['returned_size']
args={'f':'pjson','bbox':','.join(str(e[k]) for k in ('xmin','ymin','xmax','ymax')),'bboxSR':26910,'imageSR':26910,'size':','.join(map(str,size)),'format':'png','bandIds':'0,1,2','interpolation':'RSP_NearestNeighbor','adjustAspectRatio':'false','mosaicRule':json.dumps({'mosaicMethod':'esriMosaicLockRaster','lockRasterIds':[item['attributes']['objectid']],'mosaicOperation':'MT_FIRST'})}
export_url,export=fetch('/exportImage',args,base/'export-response.json')
with urllib.request.urlopen(export['href'],timeout=25) as r:b=r.read()
(base/'islands.png').write_bytes(b)
with Image.open(base/'islands.png') as img:assert list(img.size)==size
assert export['extent']==e,(export['extent'],e)
date_root='https://imagery.geoplatform.gov/iipp/rest/services/NAIP/NAIP2017_CONUS_AcquisitionDates/MapServer/54'
date_args={'f':'pjson','where':'1=1','geometry':'-124.050,46.625,-124.025,46.638','geometryType':'esriGeometryEnvelope','inSR':4269,'spatialRel':'esriSpatialRelIntersects','outFields':'*','returnGeometry':'true','outSR':4269}
date_url=date_root+'/query?'+urllib.parse.urlencode(date_args)
with urllib.request.urlopen(date_url,timeout=25) as r:date_bytes=r.read()
(base/'acquisition-dates-query.json').write_bytes(date_bytes)
dates=json.loads(date_bytes);assert 'error' not in dates,dates
assert not dates.get('exceededTransferLimit')
date_features=[{'attributes':f['attributes'],'timestamp_utc_representation':datetime.datetime.fromtimestamp(f['attributes']['date']/1000,datetime.timezone.utc).isoformat()} for f in dates['features']]
files=[{'path':p.as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(base.iterdir()) if p.is_file()]
out={'source_id':'S273','acquired_date':'2026-10-09','service_url':service_url,'catalog_query_url':query_url,'export_request_url':export_url,'locked_item':item,'request_parameters':args,'returned_extent':export['extent'],'returned_size':size,'files':files,'coverage':covered,'prior_source_id':'S261','imagery_date_role':'Catalog year2017;20170827filename date, not independently authenticated exposure time','limits':'Rendered service crop, not native original. Returned extent identical to2006; not independent geolocation/registration accuracy. First three bands requested, tide/season/vegetation/class/epoch and exposure time unresolved. No manual image edit, alignment fit or displacement.'}
out.update({'acquisition_date_query_url':date_url,'acquisition_date_features':date_features,'imagery_date_role':'Catalog year2017 and20170827filename; separate acquisition-date field inspected. Timestamp representation is not authenticated exposure time.'})
Path('data/willapa-naip2017-acquisition.json').write_text(json.dumps(out,indent=2)+'\n')
print('extent identical',export['extent'],'size',size,'coverage',covered)
