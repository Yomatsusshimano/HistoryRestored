"""Locate published WGS84 controls using pinned historic GeoPDF registration.
Requires pypdf and pyproj; no survey, contour interpolation or hydraulic model.
"""
from pathlib import Path
import json,math,hashlib
from pypdf import PdfReader
from pyproj import CRS,Transformer,datadir
from pyproj.transformer import TransformerGroup,AreaOfInterest
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'data/babcock-quad-acquisition.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    source=(root/item['path']).read_bytes()
    assert len(source)==item['bytes'] and hashlib.sha256(source).hexdigest()==item['sha256'], item['path']
datadir.append_data_dir(str(root/'sources/originals/missoula/babcock-quads'))
datadir.append_data_dir(str(root/'sources/originals/cascadia/proj-harn'))
group=TransformerGroup(4326,4267,always_xy=True,area_of_interest=AreaOfInterest(-120,47.125,-119.875,47.25))
assert group.best_available
geo=group.transformers[0]
proj=Transformer.from_crs(4267,CRS.from_proj4('+proj=poly +lat_0=0 +lon_0=-119.938 +datum=NAD27 +units=m +no_defs'),always_xy=True)
table=json.loads((root/'data/missoula-table1.json').read_text(encoding='utf-8'))
records=[]
for suffix,identifier in [('239888','239888'),('239889','239889')]:
    p=PdfReader(root/f'sources/originals/missoula/babcock-quads/{suffix}.pdf').pages[0]
    g=p['/LGIDict'][0].get_object(); a,b,c,d,e,f=map(float,g['/CTM'])
    points=[]
    for row in [r for r in table['controls'] if r['table_row'] in (12,45)]:
        lon,lat=geo.transform(row['longitude'],row['latitude']);x,y=proj.transform(lon,lat)
        det=a*d-b*c;px=(d*(x-e)-c*(y-f))/det;py=(-b*(x-e)+a*(y-f))/det
        points.append(dict(id=row['id'],nad27_lon=lon,nad27_lat=lat,projected_x=x,projected_y=y,page_x_pt=px,page_y_pt=py))
    residuals=[]
    for tie in g['/Registration']:
        px,py,x,y=map(float,tie)
        residuals.append(math.hypot(a*px+c*py+e-x,b*px+d*py+f-y))
    # Internal map-corner check: geographic frame southwest/northwest/northeast/southeast.
    # Registration points are stored data; agreement is internal, not a survey check.
    corners=[]
    for lon,lat in [(-120,47.125),(-120,47.25),(-119.875,47.25),(-119.875,47.125)]:
        x,y=proj.transform(lon,lat);px=(d*(x-e)-c*(y-f))/det;py=(-b*(x-e)+a*(y-f))/det
        corners.append(dict(longitude_nad27=lon,latitude_nad27=lat,page_x_pt=px,page_y_pt=py))
    assert residuals and max(residuals)<0.000001
    neatline=list(map(float,g['/Neatline']))
    frame=list(zip(neatline[::2],neatline[1::2]))
    for corner in corners:
        assert min(math.hypot(corner['page_x_pt']-x,corner['page_y_pt']-y) for x,y in frame)<0.00001
    records.append(dict(identifier=identifier,page_width_pt=float(p.mediabox.width),page_height_pt=float(p.mediabox.height),ctm=[a,b,c,d,e,f],registration_residuals_m=residuals,points=points,corners=corners,neatline=list(map(float,g['/Neatline']))))
result=dict(transform_description=geo.description,transform_definition=geo.definition,reported_operation_accuracy_m=geo.accuracy,best_available_in_declared_area=True,pyproj_version=__import__('pyproj').__version__,proj_version=__import__('pyproj').proj_version_str,projection_interpretation='Polyconic, longitude origin -119.938 degrees, NAD27; declared from embedded projection and printed NAD27 legend. No vertical transformation.',sheets=records)
(root/'analysis/babcock-page-locations-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('Located two controls on both sheets; reported horizontal operation accuracy',geo.accuracy,'m; no vertical transformation or flood stage computed.')
