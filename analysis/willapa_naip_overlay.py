"""Place recorded vectors on the recorded service extent without fitting."""
from pathlib import Path
import base64, hashlib, json, struct
import numpy as np
import pyproj, shapefile
from shapely import Polygon, Point
from PIL import Image, ImageDraw

ledger=json.loads(Path('data/willapa-naip2006-acquisition.json').read_text())
for item in ledger['files']:
    assert hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256']
image=Image.open('sources/originals/cascadia/naip2006/islands.png').convert('RGB')
assert list(image.size)==ledger['returned_size']
extent=ledger['returned_extent'];w,h=image.size
project=pyproj.Transformer.from_crs(4269,26910,always_xy=True)
def pixels(coords):
    a=np.asarray(coords);x,y=project.transform(a[:,0],a[:,1],errcheck=True)
    return list(zip((x-extent['xmin'])*w/(extent['xmax']-extent['xmin']),
                    (extent['ymax']-y)*h/(extent['ymax']-extent['ymin'])))
overlay=image.copy();draw=ImageDraw.Draw(overlay)
rows=json.loads(Path('data/willapa-geodatabase-rows.json').read_text(encoding='utf-8-sig'))['tables']['wc46c03lines_83']
footprint=Polygon(ledger['locked_item']['geometry']['rings'][0]);assert footprint.is_valid
coverage=[]
for row in rows:
    if row['OBJECTID'] not in (49,51):continue
    raw=base64.b64decode(row['Shape']['base64']);parts,n=struct.unpack_from('<2I',raw,36)
    starts=list(struct.unpack_from('<'+'I'*parts,raw,44))
    points=np.array(struct.unpack_from('<'+'d'*(2*n),raw,44+4*parts)).reshape(-1,2)
    assert all(footprint.covers(Point(p)) for p in points)
    for a,b in zip(starts,starts[1:]+[n]):draw.line(pixels(points[a:b]),fill=(240,0,180),width=5)
    anchor=pixels(points)[len(points)//2];draw.text(anchor,str(row['OBJECTID']),fill='black',stroke_width=2,stroke_fill='white')
    coverage.append({'historical_id':row['OBJECTID'],'vertices':n,'all_vertices_inside_selected_catalog_footprint':True})
reader=shapefile.Reader('tmp/research/WA0401D/softcopyl1');found=[]
for shape,record in zip(reader.shapes(),reader.records()):
    attrs=record.as_dict()
    if int(attrs['FEATURE_ID'])!=887366:continue
    assert attrs['FEATURE']==20
    starts=list(shape.parts)
    for a,b in zip(starts,starts[1:]+[len(shape.points)]):draw.line(pixels(shape.points[a:b]),fill=(0,120,255),width=4)
    found.append(attrs)
assert len(found)==1
scale=0.65;size=(round(w*scale),round(h*scale))
panel=Image.new('RGB',(size[0]*2,size[1]+65),'white');panel.paste(image.resize(size),(0,65));panel.paste(overlay.resize(size),(size[0],65))
d=ImageDraw.Draw(panel);d.text((10,8),'NAIP service tile: filename date 2006-06-24 | unmarked left; recorded vectors right',fill='black')
d.text((10,30),'Magenta: historical apparent-marsh IDs 49/51 | Blue: modern MHW 887366 (2006-10-09) | no alignment fit',fill='black')
target=Path('research/figures/willapa-naip2006-islands.png');panel.save(target)
out={'source_ids':['S251','S252','S253','S257','S261'],'figure':target.as_posix(),'figure_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
     'placement':'Recorded returned pixel-edge extent EPSG26910; vector EPSG4269 to26910; no fitting, offset or epoch reconciliation.',
     'coverage':coverage,'modern_candidate':found[0],
     'limits':'Catalog polygon inclusion is not native valid-pixel or complete photographic coverage authentication. MHW and apparent marsh differ; tide and exposure time unknown. Visual comparison supplies no signed change, ecological identification or catastrophe date.'}
Path('data/willapa-naip2006-overlay.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(coverage))
