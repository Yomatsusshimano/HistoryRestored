"""Acquire a locked-raster public service crop; not an original NOAA October frame."""
from pathlib import Path
import base64,hashlib,json,math,struct,urllib.parse,urllib.request
import numpy as np
import pyproj
from PIL import Image

root='https://imagery.geoplatform.gov/iipp/rest/services/NAIP/NAIP2006_CONUS/ImageServer'
base=Path('sources/originals/cascadia/naip2006');base.mkdir(exist_ok=True)
def fetch(endpoint,args,target):
    url=root+endpoint+'?'+urllib.parse.urlencode(args)
    with urllib.request.urlopen(url,timeout=25) as response:raw=response.read()
    target.write_bytes(raw);data=json.loads(raw);assert 'error' not in data,data
    return url,data
service_url,service=fetch('',{'f':'pjson'},base/'service.json')
query_args={'f':'pjson','where':'category=1','geometry':'-124.050,46.625,-124.025,46.638','geometryType':'esriGeometryEnvelope','inSR':4269,'spatialRel':'esriSpatialRelIntersects','outFields':'*','returnGeometry':'true','outSR':4269}
query_url,query=fetch('/query',query_args,base/'catalog-query.json')
items=[i for i in query['features'] if i['attributes']['name']=='n_4612424_se_10_1_20060624']
assert len(items)==1
item=items[0];object_id=item['attributes']['objectid']
assert item['attributes']['year']==2006 and item['attributes']['category']==1
rows=json.loads(Path('data/willapa-geodatabase-rows.json').read_text(encoding='utf-8-sig'))['tables']['wc46c03lines_83']
coords=[]
for row in rows:
    if row['OBJECTID'] not in (49,51):continue
    raw=base64.b64decode(row['Shape']['base64']);parts,n=struct.unpack_from('<2I',raw,36)
    coords.extend(np.array(struct.unpack_from('<'+'d'*(2*n),raw,44+4*parts)).reshape(-1,2).tolist())
coords=np.array(coords);project=pyproj.Transformer.from_crs(4269,26910,always_xy=True)
x,y=project.transform(coords[:,0],coords[:,1],errcheck=True)
bbox=[float(min(x)-400),float(min(y)-400),float(max(x)+400),float(max(y)+400)]
width=math.ceil(bbox[2]-bbox[0]);height=math.ceil(bbox[3]-bbox[1])
args={'f':'pjson','bbox':','.join(map(str,bbox)),'bboxSR':26910,'imageSR':26910,'size':f'{width},{height}',
      'format':'png','interpolation':'RSP_NearestNeighbor','adjustAspectRatio':'false',
      'mosaicRule':json.dumps({'mosaicMethod':'esriMosaicLockRaster','lockRasterIds':[object_id],'mosaicOperation':'MT_FIRST'})}
export_url,export=fetch('/exportImage',args,base/'export-response.json')
with urllib.request.urlopen(export['href'],timeout=25) as response:image_bytes=response.read()
image_path=base/'islands.png';image_path.write_bytes(image_bytes)
with Image.open(image_path) as image:assert image.size==(export['width'],export['height'])
files=[{'path':p.as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(base.iterdir()) if p.is_file()]
out={'source_id':'S261','acquired_date':'2026-10-09','service_url':service_url,'catalog_query_url':query_url,'export_request_url':export_url,
     'locked_item':item,'request_parameters':args,'returned_extent':export['extent'],'returned_size':[export['width'],export['height']],
     'files':files,'imagery_date_role':'year2006catalog field;20060624encoded in source name, not original exposure timestamp authentication',
     'limits':'Rendered public service crop, not native original raster or NOAA0605R10frame. Server reprojection/default datum operation not independently reproduced; tide, original exposure time and source-frame correspondence unknown. No field accuracy or displacement inferred.'}
Path('data/willapa-naip2006-acquisition.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'locked_item':item['attributes'],'extent':export['extent'],'dimensions':out['returned_size'],'files':files},indent=2))
