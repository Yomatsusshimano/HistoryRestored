"""Check exact project inclusion and alternative classes, without movement inference."""
from pathlib import Path
import collections,hashlib,json
import numpy as np
import pyproj,shapefile,shapely
from shapely import Point,LineString,Polygon,STRtree

project=pyproj.Transformer.from_crs(4269,26910,always_xy=True)
def projected(points):
    a=np.array(points);x,y=project.transform(a[:,0],a[:,1],errcheck=True);return np.column_stack((x,y))
folder=Path('tmp/research/WA0401D')
boundary_shape=shapefile.Reader(str(folder/'projbnd')).shape(0)
assert len(boundary_shape.parts)==1
boundary=Polygon(projected(boundary_shape.points));assert boundary.is_valid
groups=collections.defaultdict(list)
reader=shapefile.Reader(str(folder/'softcopyl1'))
for shape,record in zip(reader.shapes(),reader.records()):
    attrs=record.as_dict();starts=list(shape.parts)
    for a,b in zip(starts,starts[1:]+[len(shape.points)]):
        groups[attrs['ATTRIBUTE']].append((LineString(projected(shape.points[a:b])),attrs))
trees={label:STRtree([r[0] for r in records]) for label,records in groups.items()}
comparison_path=Path('data/willapa-marsh-comparison.json')
comparison=json.loads(comparison_path.read_text())
records=[]
for record in comparison['records']:
    if record['historical_id'] not in (49,51):continue
    samples=record['variants'][0]['samples'];points=[Point(s['xy_m']) for s in samples]
    classifications={}
    for label in ['Natural.Mean High Water','Source Data Limit','Depth Contour','Depth Contour.Approximate','Natural.Apparent.Marsh Or Swamp']:
        distances=[];candidates=[]
        for point in points:
            indices,values=trees[label].query_nearest(point,all_matches=True,return_distance=True)
            distances.append(float(values[0]));candidates.append(sorted({int(groups[label][i][1]['FEATURE_ID']) for i in indices}))
        candidate_ids={i for items in candidates for i in items}
        attrs_by_id={int(r[1]['FEATURE_ID']):r[1] for r in groups[label]}
        classifications[label]={'min_distance_m':min(distances),'median_distance_m':float(np.median(distances)),'max_distance_m':max(distances),'sample_distances_m':distances,'sample_candidate_ids':candidates,
                                'candidate_attributes':[attrs_by_id[i] for i in sorted(candidate_ids)]}
    records.append({'historical_id':record['historical_id'],'sample_count':len(points),
                    'samples_covered_by_project_polygon':sum(boundary.covers(p) for p in points),
                    'distance_to_project_boundary_min_m':min(p.distance(boundary.boundary) for p in points),
                    'classes':classifications})
out={'source_ids':['S253','S257'],'comparison_sha256':hashlib.sha256(comparison_path.read_bytes()).hexdigest(),
     'modern_archive_sha256':hashlib.sha256(Path('sources/originals/cascadia/WA0401D.zip').read_bytes()).hexdigest(),
     'versions':{'shapely':shapely.__version__,'pyproj':pyproj.__version__,'pyshp':shapefile.__version__},
     'method':'Same10m samples as previous diagnostic; exact covers predicate in projected NAD83UTM10, unsigned nearest full-table lines by stated label.',
     'limits':'Project polygon includes unsurveyed areas per metadata. Source limit proximity does not prove coverage or observation absence. Alternative classes not substituted as homologous marsh edge.',
     'records':records}
Path('data/willapa-island-coverage.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{**{k:v for k,v in r.items() if k!='classes'},'classes':{k:{a:b for a,b in v.items() if not a.startswith('sample_')} for k,v in r['classes'].items()}} for r in records],indent=2))
