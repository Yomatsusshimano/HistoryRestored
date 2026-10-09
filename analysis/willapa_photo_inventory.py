"""Inventory intersections locate candidate frames, not verified ground coverage."""
from pathlib import Path
import base64,hashlib,json,struct,zipfile
import numpy as np
import pyproj,shapefile
from shapely import LineString,Polygon,Point
from shapely.ops import unary_union

source=Path('sources/originals/cascadia/NOAA_NGS_IMAGERY_2006.ZIP')
folder=Path('tmp/research/apos2006');folder.mkdir(exist_ok=True)
with zipfile.ZipFile(source) as z:
    assert all('/' not in n and '\\' not in n for n in z.namelist());z.extractall(folder)
    members=[{'name':i.filename,'bytes':i.file_size,'sha256':hashlib.sha256(z.read(i.filename)).hexdigest()} for i in z.infolist()]
reader=shapefile.Reader(str(folder/'NOAA_NGS_Imagery_2006'))
assert reader.shapeType==5
crs=(folder/'NOAA_NGS_Imagery_2006.prj').read_text()
assert pyproj.CRS.from_wkt(crs).equals(pyproj.CRS.from_epsg(4269),ignore_axis_order=True)
project=pyproj.Transformer.from_crs(4269,26910,always_xy=True)
def projected(points):
    p=np.array(points);x,y=project.transform(p[:,0],p[:,1],errcheck=True);return np.column_stack((x,y))
frames=[]
report_ranges={('0605R02','22-APR-2006'):[(19,66),(76,88)],('0605R02','23-APR-2006'):[(118,178)],
               ('0605R03','04-MAY-2006'):[(23,30),(111,124)],('0605R10','09-OCT-2006'):[(1,6),(8,21)]}
for shape,record in zip(reader.shapes(),reader.records()):
    attrs=record.as_dict()
    if attrs['Project']!='WA0401':continue
    assert len(shape.parts)==1
    polygon=Polygon(projected(shape.points));assert polygon.is_valid
    frames.append({'attributes':attrs,'footprint_lon_lat':list(map(list,shape.points)),'polygon':polygon})
comparison=json.loads(Path('data/willapa-marsh-comparison.json').read_text())
by_id={r['historical_id']:r for r in comparison['records']}
rows=json.loads(Path('data/willapa-geodatabase-rows.json').read_text(encoding='utf-8-sig'))['tables']['wc46c03lines_83']
out=[]
for row in rows:
    if row['Feature']!=15:continue
    raw=base64.b64decode(row['Shape']['base64']);parts,n=struct.unpack_from('<2I',raw,36)
    starts=list(struct.unpack_from('<'+'I'*parts,raw,44));coords=np.array(struct.unpack_from('<'+'d'*(2*n),raw,44+4*parts)).reshape(-1,2)
    line=unary_union([LineString(projected(coords[a:b])) for a,b in zip(starts,starts[1:]+[n])])
    samples=[Point(s['xy_m']) for s in by_id[row['OBJECTID']]['variants'][0]['samples']]
    matches=[]
    for frame in frames:
        if not frame['polygon'].intersects(line):continue
        attrs=frame['attributes'];exposure=int(attrs['ExposeNum'])
        matches.append({'attributes':frame['attributes'],'footprint_lon_lat':frame['footprint_lon_lat'],
                        'listed_in_WA0401D_report_roll_date_frame_ranges':any(a<=exposure<=b for a,b in report_ranges.get((attrs['RollNumber'],attrs['ExposeDate']),[])),
                        'covered_sample_count':sum(frame['polygon'].covers(p) for p in samples),'sample_count':len(samples)})
    out.append({'historical_id':row['OBJECTID'],'candidate_frame_count':len(matches),'candidate_frames':matches})
result={'source_id':'S259','archive_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'members':members,
        'national_frame_count':len(reader),'WA0401_frame_count':len(frames),'inventory_crs_wkt':crs,
        'method':'Exact polygon-line intersection after genericNAD83UTM10 projection;10m sample covers counts are inventory checks only.',
        'limits':'Inventory footprint is not viewed aerial image or verified image ground coverage. Original frames, orientation/footprint accuracy, tide and source-vector correspondence remain unverified. No original photo downloaded or ordered.',
        'records':out}
Path('data/willapa-photo-inventory.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'id':r['historical_id'],'frames':[(f['attributes']['RollNumber'],f['attributes']['ExposeNum'],f['attributes']['ExposeDate'],f['covered_sample_count']) for f in r['candidate_frames']]} for r in out],indent=2))
