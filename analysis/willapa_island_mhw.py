"""Select historical MHW by exact recorded image-extent intersection."""
from pathlib import Path
import base64,hashlib,json,struct
import numpy as np
import pyproj,shapefile
from shapely import LineString,box
from PIL import Image,ImageDraw

rows=json.loads(Path('data/willapa-geodatabase-rows.json').read_text(encoding='utf-8-sig'))['tables']['wc46c03lines_83']
ledger=json.loads(Path('data/willapa-naip2006-acquisition.json').read_text());e=ledger['returned_extent']
region=box(e['xmin'],e['ymin'],e['xmax'],e['ymax'])
project=pyproj.Transformer.from_crs(4269,26910,always_xy=True)
inverse=pyproj.Transformer.from_crs(26910,4269,always_xy=True)
def xy(points):
    p=np.asarray(points);x,y=project.transform(p[:,0],p[:,1],errcheck=True);return np.column_stack((x,y))
def decode(row):
    raw=base64.b64decode(row['Shape']['base64']);parts,n=struct.unpack_from('<2I',raw,36)
    starts=list(struct.unpack_from('<'+'I'*parts,raw,44));points=np.array(struct.unpack_from('<'+'d'*(2*n),raw,44+4*parts)).reshape(-1,2)
    return [points[a:b] for a,b in zip(starts,starts[1:]+[n])]
selected=[];all_mhw=[r for r in rows if r['Feature']==20];assert len(all_mhw)==40
for row in all_mhw:
    parts=decode(row);lines=[LineString(xy(p)) for p in parts]
    if not any(line.intersects(region) for line in lines):continue
    selected.append({'id':row['OBJECTID'],'parts':parts,'lines':lines,'attributes':{k:v for k,v in row.items() if k!='Shape'}})
assert selected
base=Path('sources/originals/cascadia/T-03921');a,d,b,factor,c,f=map(float,(base/'t03921_dd.jgw').read_text().split());assert b==d==0
Image.MAX_IMAGE_PIXELS=200000000;original=Image.open(base/'t03921_dd.jpg')
# Corner-derived rectangular historical crop: placement not an image warp.
corners=[inverse.transform(x,y) for x,y in [(e['xmin'],e['ymin']),(e['xmin'],e['ymax']),(e['xmax'],e['ymin']),(e['xmax'],e['ymax'])]]
pix=[((x-c)/a,(y-f)/factor) for x,y in corners]
left=max(0,int(np.floor(min(x for x,y in pix))));top=max(0,int(np.floor(min(y for x,y in pix))))
right=min(original.width,int(np.ceil(max(x for x,y in pix)))+1);bottom=min(original.height,int(np.ceil(max(y for x,y in pix)))+1)
old=original.crop((left,top,right,bottom)).convert('RGB');new=Image.open('sources/originals/cascadia/naip2006/islands.png').convert('RGB')
oldmark=old.copy();newmark=new.copy();od=ImageDraw.Draw(oldmark);nd=ImageDraw.Draw(newmark)
def oldpix(p):return [(float((x-c)/a-left),float((y-f)/factor-top)) for x,y in p]
def newpix(p):return [(float((x-e['xmin'])*new.width/(e['xmax']-e['xmin'])),float((e['ymax']-y)*new.height/(e['ymax']-e['ymin']))) for x,y in xy(p)]
for row in rows:
    if row['OBJECTID'] not in (49,51):continue
    for p in decode(row):od.line(oldpix(p),fill=(230,0,150),width=4);nd.line(newpix(p),fill=(230,0,150),width=4)
for r in selected:
    for p in r['parts']:
        od.line(oldpix(p),fill=(240,100,0),width=4);nd.line(newpix(p),fill=(240,100,0),width=4)
    for draw,pp in [(od,oldpix),(nd,newpix)]:
        for line in r['lines']:
            anchor=line.intersection(region).representative_point();lonlat=inverse.transform(anchor.x,anchor.y)
            draw.text(pp([lonlat])[0],str(r['id']),fill='black',stroke_width=1,stroke_fill='white')
reader=shapefile.Reader('tmp/research/WA0401D/softcopyl1');modern=[]
for shape,record in zip(reader.shapes(),reader.records()):
    attrs=record.as_dict()
    if attrs['FEATURE']!=20:continue
    starts=list(shape.parts);parts=[shape.points[a:b] for a,b in zip(starts,starts[1:]+[len(shape.points)])]
    if not any(LineString(xy(p)).intersects(region) for p in parts):continue
    modern.append({'id':int(attrs['FEATURE_ID']),'source_date':attrs['SRC_DATE']})
    for p in parts:nd.line(newpix(p),fill=(0,120,255),width=3)
panels=[]
for im in (old,oldmark,new,newmark):
    scale=min(1,900/im.width);panels.append(im.resize((round(im.width*scale),round(im.height*scale))))
oldheight=max(im.height for im in panels[:2]);newheight=max(im.height for im in panels[2:])
canvas=Image.new('RGB',(1800,oldheight+newheight+110),'white');draw=ImageDraw.Draw(canvas)
for i,im in enumerate(panels):canvas.paste(im,((i%2)*900,55 if i<2 else oldheight+110))
draw.text((10,8),'1922 source raster | unmarked left; historical MHW orange, apparent marsh magenta right',fill='black')
draw.text((10,oldheight+63),'2006 NAIP service | unmarked left; historical vectors right plus modern MHW blue | no fit; different raster grids',fill='black')
target=Path('research/figures/willapa-island-mhw.png');canvas.save(target)
out={'source_ids':['S251','S252','S253','S257','S261'],'selection':'All40historical Feature20 records tested against exact EPSG26910 returned image rectangle; intersecting whole features retained, no proximity selection.',
     'extent':e,'historical_crop_pixel_edges':[left,top,right,bottom],'selected_historical':[{'id':r['id'],'attributes':r['attributes'],'length_inside_extent_m':sum(line.intersection(region).length for line in r['lines'])} for r in selected],
     'modern_mhw_in_extent':modern,'figure':target.as_posix(),'figure_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
     'limits':'Historical raster rectangle uses inverse-projected corners and its own grid; panels not pixel-corresponding warps. Boundary code/source trace visual check is not field authentication. No signed displacement, error budget, ecology, exact tide or catastrophe inference.'}
Path('data/willapa-island-mhw.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'historical_ids':[r['id'] for r in selected],'modern':modern},indent=2))
