"""Scientific source/trace panels; no image registration or boundary fitting."""
from pathlib import Path
import base64,hashlib,json,struct
import numpy as np
import pyproj
from shapely.geometry import Point,Polygon
from PIL import Image,ImageDraw,ImageFont

ledgers=[json.loads(Path(f'data/willapa-naip{y}-acquisition.json').read_text()) for y in (2006,2017)]
assert ledgers[0]['returned_extent']==ledgers[1]['returned_extent']
assert ledgers[0]['returned_size']==ledgers[1]['returned_size']
for ledger in ledgers:
    for f in ledger['files']:assert hashlib.sha256(Path(f['path']).read_bytes()).hexdigest()==f['sha256']
e=ledgers[0]['returned_extent'];w,h=ledgers[0]['returned_size']
project=pyproj.Transformer.from_crs(4269,26910,always_xy=True)
rows=json.loads(Path('data/willapa-geodatabase-rows.json').read_text(encoding='utf-8-sig'))['tables']['wc46c03lines_83']
traces={}
date_source=json.loads(Path('sources/originals/cascadia/naip2017/acquisition-dates-query.json').read_text())
assert len(date_source['features'])==1
assert date_source['spatialReference']['wkid']==4269
date_rings=[Polygon(ring) for ring in date_source['features'][0]['geometry']['rings']]
for row in rows:
    if row['OBJECTID'] not in (49,51):continue
    raw=base64.b64decode(row['Shape']['base64']);parts,n=struct.unpack_from('<2I',raw,36)
    starts=list(struct.unpack_from('<'+'I'*parts,raw,44))
    coords=np.array(struct.unpack_from('<'+'d'*(2*n),raw,44+4*parts)).reshape(-1,2)
    assert all(sum(r.covers(Point(p)) for r in date_rings)%2==1 for p in coords), 'Date polygon coverage missing'
    x,y=project.transform(coords[:,0],coords[:,1],errcheck=True)
    px=(x-e['xmin'])*w/(e['xmax']-e['xmin']);py=(e['ymax']-y)*h/(e['ymax']-e['ymin'])
    traces[row['OBJECTID']]={'parts':[list(zip(px[a:b],py[a:b])) for a,b in zip(starts,starts[1:]+[n])],'vertices':n}
scale=0.65;sw,sh=round(w*scale),round(h*scale)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',20)
panel=Image.new('RGB',(sw*2,(sh+48)*2+45),'white');d=ImageDraw.Draw(panel)
for r,year in enumerate((2006,2017)):
    img=Image.open(f'sources/originals/cascadia/naip{year}/islands.png').convert('RGB')
    annotated=img.copy();draw=ImageDraw.Draw(annotated)
    for ident,t in traces.items():
        for line in t['parts']:draw.line(line,fill=(240,0,180),width=5)
        x,y=t['parts'][0][len(t['parts'][0])//2]
        draw.text((x,y),str(ident),fill='black',font=font,stroke_width=2,stroke_fill='white')
    top=r*(sh+48)
    d.text((12,top+10),f'{year}: unmarked service crop',font=font,fill='black')
    d.text((sw+12,top+10),f'{year}: historical marsh traces 49/51 (magenta)',font=font,fill='black')
    panel.paste(img.resize((sw,sh)),(0,top+48));panel.paste(annotated.resize((sw,sh)),(sw,top+48))
d.text((12,2*(sh+48)+10),'Same returned extent; no alignment fit. Filename dates: 2006-06-24 / 2017-08-27. Tide unknown.',font=font,fill='black')
p=Path('research/figures/willapa-naip2006-2017-pair.png');panel.save(p)
out={'source_ids':['S253','S261','S273'],'figure':p.as_posix(),'figure_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'same_returned_extent_and_dimensions':True,'historical_trace_vertices':{str(k):v['vertices'] for k,v in traces.items()},'all_historical_vertices_covered_by_2017_date_polygon':True,'date_polygon_objectid':date_source['features'][0]['attributes']['OBJECTID'],'method':'NAD83geographic historical vertices toUTM10; recorded pixel-edge extent; no registration fit/manual image adjustment/boundary extraction. Date polygon coverage uses even-odd ring inclusion.','limits':'Service reprojection not independently validated; source filename dates/date field not exposure-time authentication. Different tide/vegetation/season/radiometry. No displacement, homologous modern marsh boundary or cause established.'}
Path('data/willapa-naip-pair.json').write_text(json.dumps(out,indent=2)+'\n')
print(p)
