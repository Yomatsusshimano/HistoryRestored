"""Compare raw DSM changes by author-mapped channel masks; no error correction."""
import argparse
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

import numpy as np
import rasterio
from rasterio.features import rasterize
from rasterio.warp import transform_geom
from rasterio.windows import from_bounds

NS={'k':'http://www.opengis.net/kml/2.2'}
FILES={'before_channel':'Melamchi_Khola_River_Channel_Nov2020.kml',
       'after_channel':'Melamchi_Khola_River_Channel_Oct2021.kml',
       'after_cloud':'Obscured_Areas_Cloud_Oct2021.kml',
       'after_shadow':'Obscured_Areas_Shadow_Oct2021.kml'}

def ring(element):
    assert element is not None and element.text, 'Missing KML ring'
    coords=[]
    for token in element.text.split():
        values=token.split(',')
        x,y=map(float,values[:2])
        assert np.isfinite(x) and np.isfinite(y) and -180<=x<=180 and -90<=y<=90
        coords.append([x,y])
    assert len(coords)>=4 and coords[0]==coords[-1], 'Invalid/unclosed ring'
    return coords

def polygons(path):
    tree=ET.parse(path)
    result=[]
    for poly in tree.findall('.//k:Polygon',NS):
        outer=ring(poly.find('k:outerBoundaryIs/k:LinearRing/k:coordinates',NS))
        inner=[ring(p) for p in poly.findall('k:innerBoundaryIs/k:LinearRing/k:coordinates',NS)]
        result.append(dict(type='Polygon',coordinates=[outer]+inner))
    assert result, 'No polygon geometries'
    return result

def summary(delta, select):
    v=delta[select]
    return dict(pixels=int(v.size),median=float(np.median(v)) if v.size else None,
                p05=float(np.quantile(v,.05)) if v.size else None,
                p95=float(np.quantile(v,.95)) if v.size else None)

def run(before,after,masks,prior,output,figure):
    with rasterio.open(before) as b, rasterio.open(after) as a:
        assert b.crs==a.crs
        bounds=prior['window']['bounds_projected']
        bw=from_bounds(*bounds,transform=b.transform)
        aw=from_bounds(*bounds,transform=a.transform)
        assert b.window_transform(bw).almost_equals(a.window_transform(aw),precision=1e-8)
        bv=b.read(1,window=bw,masked=True).astype('float64')
        av=a.read(1,window=aw,masked=True).astype('float64')
        assert bv.shape==av.shape==tuple(prior['window']['shape'])
        valid=~(np.ma.getmaskarray(bv)|np.ma.getmaskarray(av)) & np.isfinite(bv.data)&np.isfinite(av.data)
        delta=av.data-bv.data
        assert int(valid.sum())==prior['window']['paired_valid_pixels']
        masks_by_name={}; geometry_records={}
        for key,name in FILES.items():
            p=masks/name
            geoms=polygons(p)
            projected=[transform_geom('EPSG:4326',b.crs,g) for g in geoms]
            mask=rasterize([(g,1) for g in projected],out_shape=bv.shape,transform=b.window_transform(bw),all_touched=False,dtype='uint8').astype(bool)
            masks_by_name[key]=mask
            geometry_records[key]=dict(filename=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),polygon_count=len(geoms),window_pixels=int(mask.sum()))
        bc=masks_by_name['before_channel']; ac=masks_by_name['after_channel']
        obscured=masks_by_name['after_cloud']|masks_by_name['after_shadow']
        usable=valid&~obscured
        groups={'before_channel':usable&bc,'after_channel':usable&ac,
                'both_channel_epochs':usable&bc&ac,'after_channel_only':usable&ac&~bc,
                'before_channel_only':usable&bc&~ac,'outside_both_channels':usable&~bc&~ac}
        stats={k:summary(delta,v) for k,v in groups.items()}
        partition=['both_channel_epochs','after_channel_only','before_channel_only','outside_both_channels']
        assert sum(stats[k]['pixels'] for k in partition)==int(usable.sum())
        result=dict(status='AUTHOR_MASKED_RAW_SURFACE_COMPARISON_NOT_VALIDATED_SEDIMENT',source_ids=['S447','S448'],
                    window_bounds=bounds,shape=list(bv.shape),paired_valid_pixels=int(valid.sum()),
                    excluded_valid_pixels=int((valid&obscured).sum()),usable_pixels=int(usable.sum()),
                    rasterization='Polygon interiors/holes respected; pixel-center rule, all_touched=False; KML altitude ignored',
                    masks=geometry_records,groups=stats,uncertainty_m=None,deposit_volume_m3=None,
                    scientific_limits=['November2020 channel map does not exactly match January2021 DSM epoch',
                                       'October2021 masks only; January2021 cloud/shadow mask not acquired',
                                       'Outside-channel category is not independently verified stable ground',
                                       'Mapped channel extent is not a deposit classification',
                                       'Same-author maps/DSMs are dependent, not independent corroboration',
                                       'No estimated or corrected vertical error; raw signs lack significance test'])
        output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
        if figure:
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            fig,ax=plt.subplots(figsize=(8,7),layout='constrained')
            cmap=plt.colormaps['RdBu_r'].copy(); cmap.set_bad('lightgray')
            im=ax.imshow(np.ma.array(delta,mask=~usable),cmap=cmap,vmin=-10,vmax=10)
            ax.contour(bc.astype(float),levels=[.5],colors=['yellow'],linewidths=1)
            ax.contour(ac.astype(float),levels=[.5],colors=['black'],linewidths=1)
            ax.set_title('Melamchi raw surface difference, October minus January\nYellow: November 2020 channel; black: October 2021 channel')
            ax.set_xlabel('Column (1 m spacing)'); ax.set_ylabel('Row (north at top)')
            fig.colorbar(im,ax=ax,extend='both',label='Stored-height difference; no error threshold; clipped +/-10')
            fig.savefig(figure,dpi=150); plt.close(fig)
        print(json.dumps(stats,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    for name in ['before','after','masks','prior','output']: parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--figure',type=Path)
    args=parser.parse_args()
    run(args.before,args.after,args.masks,json.loads(args.prior.read_text(encoding='utf-8')),args.output,args.figure)
