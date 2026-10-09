"""Unsigned nearest same-class distances are candidate associations, not change."""
from pathlib import Path
import base64,collections,hashlib,json,struct
import numpy as np
import pyproj,shapefile,shapely
from shapely import LineString,Point,STRtree
from PIL import Image,ImageDraw

rows_path=Path('data/willapa-geodatabase-rows.json')
historical=[r for r in json.loads(rows_path.read_text(encoding='utf-8-sig'))['tables']['wc46c03lines_83'] if r['Feature']==15]
assert len(historical)==8
folder=Path('tmp/research/WA0401D')
reader=shapefile.Reader(str(folder/'softcopyl1'))
project=pyproj.Transformer.from_crs(4269,26910,always_xy=True)
def projected(points):
    p=np.asarray(points);x,y=project.transform(p[:,0],p[:,1],errcheck=True);return np.column_stack((x,y))
modern=[];all_records=[]
for shape,record in zip(reader.shapes(),reader.records()):
    attrs=record.as_dict()
    all_records.append({'bounds':list(shape.bbox),'attributes':attrs})
    if attrs['FEATURE']!=15:continue
    starts=list(shape.parts)
    parts=[list(map(list,shape.points[a:b])) for a,b in zip(starts,starts[1:]+[len(shape.points)])]
    for part in parts:modern.append({'attributes':attrs,'points':part,'geometry':LineString(projected(part))})
assert len({r['attributes']['FEATURE_ID'] for r in modern})==375
tree=STRtree([r['geometry'] for r in modern])
segments=np.array([(a,b) for r in modern for a,b in zip(list(r['geometry'].coords),list(r['geometry'].coords)[1:])])
def analytic_distance(point):
    a=segments[:,0];v=segments[:,1]-a;q=np.asarray(point)-a;den=np.sum(v*v,axis=1)
    t=np.divide(np.sum(q*v,axis=1),den,out=np.zeros_like(den),where=den>0);t=np.clip(t,0,1)
    return float(np.min(np.linalg.norm(q-t[:,None]*v,axis=1)))
# Known parallel offset and identical-line controls, independent analytic formula.
control=LineString([(0,20),(100,20)])
assert abs(Point(50,0).distance(control)-20)<1e-12
assert Point(50,20).distance(control)==0
base=Path('sources/originals/cascadia/T-03921')
a,d,b,e,c,f=map(float,(base/'t03921_dd.jgw').read_text().split());assert b==d==0
Image.MAX_IMAGE_PIXELS=200000000;image=Image.open(base/'t03921_dd.jpg')
output=[]
for row in historical:
    raw=base64.b64decode(row['Shape']['base64']);parts,n=struct.unpack_from('<2I',raw,36)
    starts=list(struct.unpack_from('<'+'I'*parts,raw,44))
    points=np.array(struct.unpack_from('<'+'d'*(2*n),raw,44+4*parts)).reshape(-1,2)
    lines=[LineString(projected(points[x:y])) for x,y in zip(starts,starts[1:]+[n])]
    variants=[]
    for spacing in (10,20):
        samples=[]
        for part,line in enumerate(lines):
            positions=np.unique(np.append(np.arange(0,line.length,spacing),line.length))
            for distance in positions:
                point=line.interpolate(distance)
                indices,distances=tree.query_nearest(point,return_distance=True,all_matches=True)
                order=np.argsort([modern[i]['attributes']['FEATURE_ID'] for i in indices]);indices=indices[order];distances=distances[order]
                samples.append({'part':part,'along_part_m':float(distance),'xy_m':list(point.coords[0]),
                                'distance_m':float(distances[0]),
                                'nearest_candidates':[{'id':int(modern[i]['attributes']['FEATURE_ID']),'source_date':modern[i]['attributes']['SRC_DATE']} for i in indices]})
        for index in sorted(set([0,len(samples)//2,len(samples)-1])):
            sample=samples[index];assert abs(analytic_distance(sample['xy_m'])-sample['distance_m'])<1e-7
        distances=np.array([r['distance_m'] for r in samples])
        variants.append({'spacing_m':spacing,'samples':samples,'sample_count':len(samples),
                         'distance_min_m':float(distances.min()),'distance_median_m':float(np.median(distances)),
                         'distance_max_m':float(distances.max()),
                         'fractions_within_m':{str(threshold):float(np.mean(distances<=threshold)) for threshold in (25,100,500)},
                         'nearest_candidate_ids':sorted({r['id'] for s in samples for r in s['nearest_candidates']})})
    # Source and annotated panels have identical extents; no fit or datum shift.
    pixels=np.column_stack(((points[:,0]-c)/a,(points[:,1]-f)/e))
    left=max(0,int(pixels[:,0].min())-400);top=max(0,int(pixels[:,1].min())-400)
    right=min(image.width,int(np.ceil(pixels[:,0].max()))+401);bottom=min(image.height,int(np.ceil(pixels[:,1].max()))+401)
    crop=image.crop((left,top,right,bottom)).convert('RGB');overlay=crop.copy();draw=ImageDraw.Draw(overlay)
    west=c+a*left;east=c+a*right;north=f+e*top;south=f+e*bottom
    local=[r for r in all_records if r['bounds'][0]<=east and r['bounds'][2]>=west and r['bounds'][1]<=north and r['bounds'][3]>=south]
    for record in modern:
        pts=np.array(record['points']);bounds=[pts[:,0].min(),pts[:,1].min(),pts[:,0].max(),pts[:,1].max()]
        if bounds[0]>east or bounds[2]<west or bounds[1]>north or bounds[3]<south:continue
        draw.line([(float((x-c)/a-left),float((y-f)/e-top)) for x,y in pts],fill=(0,110,220),width=4)
    for start,end in zip(starts,starts[1:]+[n]):draw.line([(float(x-left),float(y-top)) for x,y in pixels[start:end]],fill=(220,0,140),width=4)
    scale=min(1,1000/max(crop.size));size=(round(crop.width*scale),round(crop.height*scale))
    panel=Image.new('RGB',(2*size[0],size[1]+55),'white');panel.paste(crop.resize(size),(0,55));panel.paste(overlay.resize(size),(size[0],55))
    draw=ImageDraw.Draw(panel);draw.text((10,8),f"Historical ID {row['OBJECTID']} | original (left); 1922 magenta, 2005-2006 apparent-marsh blue (right)",fill='black')
    target=Path(f"research/figures/willapa-marsh-comparison-{row['OBJECTID']}.png");panel.save(target)
    output.append({'historical_id':row['OBJECTID'],'historical_length_m':sum(x.length for x in lines),'panel':target.as_posix(),
                   'panel_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'crop_pixel_edges':[left,top,right,bottom],
                   'local_modern_bbox_candidates':[{'id':int(r['attributes']['FEATURE_ID']),'attribute':r['attributes']['ATTRIBUTE'],'source_date':r['attributes']['SRC_DATE']} for r in local],
                   'variants':variants})
out={'source_ids':['S251','S252','S253','S257'],'row_export_sha256':hashlib.sha256(rows_path.read_bytes()).hexdigest(),
     'modern_archive_sha256':hashlib.sha256(Path('sources/originals/cascadia/WA0401D.zip').read_bytes()).hexdigest(),
     'versions':{'shapely':shapely.__version__,'pyproj':pyproj.__version__,'pyshp':shapefile.__version__},
     'calculation_crs':'EPSG26910, NAD83 UTM10N, planar metres; no realization/epoch reconciliation',
     'method':'Unsigned point-to-line nearest Feature15 among all375modern apparent-marsh records;10m/20m samples with endpoints, all exact ties retained. Three independent analytic checks per feature/spacing.',
     'limits':'Nearest candidate is not authenticated homologous segment. No signed displacement, erosion/accretion, annual rate, catastrophe age or significance.25/100/500m are descriptive thresholds, not validated matching/accuracy gates. Sample fractions are not exact length fractions; repeated endpoints and dependency retained.',
     'records':output}
Path('data/willapa-marsh-comparison.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':r['historical_id'],'length':r['historical_length_m'],'variants':[{k:v for k,v in x.items() if k!='samples'} for x in r['variants']]} for r in output],indent=2))
