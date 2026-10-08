"""Planar geometry audit, not a hydraulic fit. Requires pyshp 2.3.1, shapely 2.1.2."""
import argparse,hashlib,io,json,zipfile
from pathlib import Path
import shapefile
import shapely
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely.validation import explain_validity

ROOT=Path(__file__).resolve().parents[1]

def audit(path):
    raw=path.read_bytes()
    expected=json.loads((ROOT/'data/grand-coulee-acquisition.json').read_text(encoding='utf-8'))['sha256']
    if hashlib.sha256(raw).hexdigest()!=expected:
        raise ValueError('Source hash mismatch')
    result={'source_id':'S126','outer_sha256':expected,'libraries':{'pyshp':shapefile.__version__,'shapely':shapely.__version__},'area_basis':'Planar native projected square metres; no reprojection or geodesic correction.','polygons':[],'pairs':[],'hydraulic_validation':False}
    geoms={}
    with zipfile.ZipFile(io.BytesIO(raw)) as outer:
        nested=outer.read('area_error_column_counts/area_error_polygons-20210201T193946Z-001.zip')
        with zipfile.ZipFile(io.BytesIO(nested)) as z:
            for name in sorted(n for n in z.namelist() if n.endswith('.shp')):
                base=name[:-4]
                reader=shapefile.Reader(shp=io.BytesIO(z.read(name)),shx=io.BytesIO(z.read(base+'.shx')),dbf=io.BytesIO(z.read(base+'.dbf')))
                geometries=[shape(s.__geo_interface__) for s in reader.shapes()]
                valid=all(g.is_valid for g in geometries)
                rec={'name':Path(base).name,'records':len(geometries),'valid':valid,'validity':[explain_validity(g) for g in geometries],'attributes':[r.as_dict() for r in reader.records()],'projection':z.read(base+'.prj').decode(),'area_m2':None}
                if valid:
                    g=unary_union(geometries);geoms[Path(base).name]=g
                    rec['area_m2']=g.area;rec['bounds']=list(g.bounds)
                    rec['stored_area_sum_m2']=sum(a['area'] for a in rec['attributes'])
                    rec['computed_minus_stored_area_m2']=g.area-rec['stored_area_sum_m2']
                result['polygons'].append(rec)
    for name,inner in geoms.items():
        if not name.endswith('_inner'): continue
        outer=geoms[name[:-6]+'_outer']
        result['pairs'].append({'name':name[:-6],'inner_area_m2':inner.area,'outer_area_m2':outer.area,'outer_covers_inner':outer.covers(inner),'intersection_area_m2':inner.intersection(outer).area,'boundary_distance_m':inner.distance(outer),'inner_outside_outer_m2':inner.difference(outer).area,'outer_minus_inner_m2':outer.difference(inner).area})
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('archive',type=Path)
    result=audit(p.parse_args().archive)
    (ROOT/'analysis/grand-coulee-polygon-audit-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'polygons':len(result['polygons']),'pairs':result['pairs']},indent=2))
