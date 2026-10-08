"""Conditional map overlay, not confirmed specimen positions. Python + pyshp/shapely/pyproj."""
import argparse, hashlib, io, json, zipfile
from pathlib import Path
import shapefile, shapely, pyproj
from shapely.geometry import shape, Point, box
from pyproj import Transformer

p=argparse.ArgumentParser()
p.add_argument('archive',type=Path)
p.add_argument('grid',type=Path)
a=p.parse_args()
assert hashlib.sha256(a.archive.read_bytes()).hexdigest()=='bfcc8dfe52b701879e2e0a431ad1e6707f42bb25cf449ce5cae14592c1b6ae87'
assert hashlib.sha256(a.grid.read_bytes()).hexdigest()=='c7d587e0d0b39b9f46c7de850b9a6a468c17b7139f82a313aa43aa4a64d94fa8'
z=zipfile.ZipFile(a.archive); base='topock_shape/shapefiles/topockglg_poly'
r=shapefile.Reader(**{k:io.BytesIO(z.read(base+'.'+k)) for k in ['shp','shx','dbf']})
projection=z.read(base+'.prj').decode()
polys=[(i,rec.record['PTYPE'],shape(rec.shape.__geo_interface__)) for i,rec in enumerate(r.iterShapeRecords())]
invalid=[(i,u,g) for i,u,g in polys if not g.is_valid]
polys=[(i,u,g) for i,u,g in polys if g.is_valid]
project=Transformer.from_crs('EPSG:4267',projection,always_xy=True)
inverse=Transformer.from_pipeline(f'proj=pipeline step proj=unitconvert xy_in=deg xy_out=rad step inv proj=gridshift grids={a.grid.resolve().as_posix()} step proj=unitconvert xy_in=rad xy_out=deg')
sites=json.loads(Path('data/colorado-burial-context.json').read_text())['sites']
out=[]
for site in sites:
    if site['site']=='Palo Verde':continue
    lon=-site['longitude_value_as_printed'];lat=site['latitude_north_degrees_as_printed']
    for scenario in ['NAD27','NAD83_1986']:
        ll=(lon,lat) if scenario=='NAD27' else inverse.transform(lon,lat,errcheck=True)
        x,y=project.transform(*ll,errcheck=True);pt=Point(x,y)
        # Invalid source geometry is excluded only when its entire bounding box
        # is well outside the local query; otherwise fail rather than repair it.
        assert all(pt.distance(box(*g.bounds))>1000 for i,u,g in invalid)
        hits=[{'polygon_index':i,'unit':u,'distance_to_polygon_edge_m':pt.distance(g.boundary)} for i,u,g in polys if g.covers(pt)]
        near=sorted([(pt.distance(g),i,u) for i,u,g in polys])[:3]
        target='Trbfm' if site['site']=='Santa Fe Railway' else 'Trbb'
        target_distance=min(pt.distance(g) for i,u,g in polys if u==target)
        out.append({'site':site['site'],'assumed_input_datum':scenario,'map_easting_m':x,'map_northing_m':y,'containing_polygons':hits,
                    'nearest_polygons':[{'distance_m':d,'polygon_index':i,'unit':u} for d,i,u in near],
                    'target_unit':target,'distance_to_nearest_target_polygon_m':target_distance,
                    'units_intersecting_50m_radius':sorted({u for i,u,g in polys if pt.distance(g)<=50})})
result={'source_ids':['S216','S219'],'map_zip_sha256':hashlib.sha256(a.archive.read_bytes()).hexdigest(),'projection_WKT':projection,
        'invalid_polygons_excluded':[{'polygon_index':i,'unit':u,'bounds':g.bounds} for i,u,g in invalid],
        'geometry_check':'Excluded invalid polygons only after checking their bounding boxes are over1000m from every query point. No geometry repaired.',
        'versions':{'pyshp':shapefile.__version__,'shapely':shapely.__version__,'pyproj':pyproj.__version__},
        'assumptions':'Printed positive longitudes interpreted as west conditionally. Input datum unknown: separate NAD27 and NAD83(1986) scenarios, latter inverted through explicit NADCON5 grid. Neither scenario is established as original GPS datum.',
        'limits':'50m radius is an illustrative sensitivity radius, not a confidence region. Distances are computational diagnostics, not field accuracy. Map nominal scale1:24000; map coverage and unit assignment are not specimen custody, contact identification or chronology.',
        'results':out}
Path('data/topock-sample-overlay.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
for s in out:print(s['site'],s['assumed_input_datum'],s['containing_polygons'],s['nearest_polygons'][:1],s['units_intersecting_50m_radius'])
