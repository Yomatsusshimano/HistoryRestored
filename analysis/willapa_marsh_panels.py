"""Render all eight stored apparent-marsh lines beside original raster crops."""
from pathlib import Path
import base64,hashlib,json,struct
import numpy as np
from PIL import Image,ImageDraw

rows=json.loads(Path('data/willapa-geodatabase-rows.json').read_text(encoding='utf-8-sig'))['tables']['wc46c03lines_83']
base=Path('sources/originals/cascadia/T-03921')
a,d,b,e,c,f=map(float,(base/'t03921_dd.jgw').read_text().split())
assert b==d==0
Image.MAX_IMAGE_PIXELS=200000000
im=Image.open(base/'t03921_dd.jpg')
selected=[r for r in rows if r['Feature']==15]
assert len(selected)==8
outdir=Path('research/figures');outdir.mkdir(exist_ok=True)
records=[]
for row in selected:
    raw=base64.b64decode(row['Shape']['base64']);parts,n=struct.unpack_from('<2I',raw,36)
    starts=list(struct.unpack_from('<'+'I'*parts,raw,44))
    pts=np.array(struct.unpack_from('<'+'d'*(2*n),raw,44+4*parts)).reshape(-1,2)
    pixels=np.column_stack(((pts[:,0]-c)/a,(pts[:,1]-f)/e))
    left=max(0,int(np.floor(pixels[:,0].min()))-100);top=max(0,int(np.floor(pixels[:,1].min()))-100)
    right=min(im.width,int(np.ceil(pixels[:,0].max()))+101);bottom=min(im.height,int(np.ceil(pixels[:,1].max()))+101)
    crop=im.crop((left,top,right,bottom)).convert('RGB');overlay=crop.copy();draw=ImageDraw.Draw(overlay)
    for start,end in zip(starts,starts[1:]+[n]):
        draw.line([(float(x-left),float(y-top)) for x,y in pixels[start:end]],fill=(220,0,140),width=3)
    scale=min(1,900/max(crop.size));size=(round(crop.width*scale),round(crop.height*scale))
    canvas=Image.new('RGB',(size[0]*2,size[1]+45),'white');canvas.paste(crop.resize(size),(0,45));canvas.paste(overlay.resize(size),(size[0],45))
    draw=ImageDraw.Draw(canvas);draw.text((10,8),f"Feature {row['OBJECTID']} | source crop (left); stored apparent-marsh trace (right)",fill='black')
    target=outdir/f"willapa-marsh-{row['OBJECTID']}.png";canvas.save(target)
    records.append({'id':row['OBJECTID'],'feature_code':15,'points':n,'crop_pixel_edges':[left,top,right,bottom],
                    'lon_lat_bounds':[float(pts[:,0].min()),float(pts[:,1].min()),float(pts[:,0].max()),float(pts[:,1].max())],
                    'panel':target.as_posix(),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
Path('data/willapa-marsh-panels.json').write_text(json.dumps({'source_ids':['S251','S252','S253'],
 'method':'World-file pixel-center inverse, 100-pixel context, all stored Feature15 records, paired unmarked/marked crops; no fit adjustment.',
 'limits':'Visual comparison only; no edge-distance or field classification validation. Rendering scales differ by crop; colored overlay is derived.',
 'records':records},indent=2)+'\n',encoding='utf-8')
print(json.dumps(records,indent=2))
