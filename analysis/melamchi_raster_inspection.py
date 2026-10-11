"""Inspect acquired DSMs and an exploratory window; no sediment-volume inference."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import rasterio
from rasterio.windows import Window, from_bounds
from rasterio.warp import transform

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            h.update(chunk)
    return h.hexdigest()

def metadata(ds):
    return dict(width=ds.width, height=ds.height, count=ds.count,
                dtypes=list(ds.dtypes), crs=ds.crs.to_string() if ds.crs else None,
                crs_wkt=ds.crs.to_wkt() if ds.crs else None,
                transform=list(ds.transform)[:6], bounds=list(ds.bounds),
                nodata=ds.nodata, units=list(ds.units), scales=list(ds.scales),
                offsets=list(ds.offsets), tags=ds.tags())

def inspect(before, after, figure=None):
    result = dict(status='EXPLORATORY_SURFACE_CHANGE_NOT_VALIDATED_EVENT_DEPOSITION',
                  software=dict(rasterio=rasterio.__version__, gdal=rasterio.__gdal_version__, numpy=np.__version__),
                  source_ids=['S447', 'S444'], before_sha256=digest(before), after_sha256=digest(after),
                  uncertainty_m=None, deposit_volume_m3=None,
                  selection='1 km square centered on S444 Figure2 caption coordinates; retrospective exploratory selection',
                  center_wgs84=dict(longitude=85.575513, latitude=27.830680),
                  scientific_limits=['No independently validated stable control or river/deposit mask',
                                     'Surface changes include buildings/vegetation and other interval processes',
                                     'No uncertainty threshold; change signs are not significant deposition/erosion',
                                     'Registration removes overall translation/rotation components'])
    with rasterio.open(before) as b, rasterio.open(after) as a:
        result['before'] = metadata(b)
        result['after'] = metadata(a)
        assert b.crs == a.crs and b.crs is not None, 'CRS mismatch or missing'
        assert b.count == a.count == 1, 'Unexpected band count'
        assert b.scales == a.scales == (1.0,) and b.offsets == a.offsets == (0.0,), 'Unmodeled scaling'
        assert b.transform.a == a.transform.a == 1 and b.transform.e == a.transform.e == -1
        assert b.transform.b == a.transform.b == b.transform.d == a.transform.d == 0
        dx = (a.transform.c - b.transform.c) / b.transform.a
        dy = (a.transform.f - b.transform.f) / b.transform.e
        assert abs(dx-round(dx)) < 1e-8 and abs(dy-round(dy)) < 1e-8, 'Fractional grid offset; no comparison performed'
        result['grid_offset_pixels'] = [dx, dy]
        x, y = transform('EPSG:4326', b.crs, [85.575513], [27.830680])
        row, col = b.index(x[0], y[0])
        bw = Window(col-500, row-500, 1000, 1000)
        bounds = rasterio.windows.bounds(bw, b.transform)
        aw0 = from_bounds(*bounds, transform=a.transform)
        assert all(abs(v-round(v)) < 1e-8 for v in [aw0.col_off, aw0.row_off, aw0.width, aw0.height])
        aw = Window(round(aw0.col_off), round(aw0.row_off), round(aw0.width), round(aw0.height))
        for w, ds in [(bw,b),(aw,a)]:
            assert w.col_off >= 0 and w.row_off >= 0 and w.col_off+w.width <= ds.width and w.row_off+w.height <= ds.height, 'Window outside raster'
        assert b.window_transform(bw).almost_equals(a.window_transform(aw), precision=1e-8)
        bv = b.read(1, window=bw, masked=True).astype('float64')
        av = a.read(1, window=aw, masked=True).astype('float64')
        valid = ~(np.ma.getmaskarray(bv) | np.ma.getmaskarray(av)) & np.isfinite(bv.data) & np.isfinite(av.data)
        d = (av.data-bv.data)[valid]
        assert d.size > 0, 'No paired valid pixels'
        result['window'] = dict(bounds_projected=list(bounds), shape=[1000,1000], paired_valid_pixels=int(d.size),
                                total_pixels=1000000, resampling=False,
                                change_definition='after minus before surface elevation; coordinate units from source, no independent vertical datum confirmation',
                                change_quantiles=dict(zip(['p05','p25','p50','p75','p95'], [float(v) for v in np.quantile(d,[.05,.25,.5,.75,.95])])),
                                minimum=float(d.min()), maximum=float(d.max()),
                                before_valid_range=[float(bv.data[valid].min()),float(bv.data[valid].max())],
                                after_valid_range=[float(av.data[valid].min()),float(av.data[valid].max())])
        if figure is not None:
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            fig, axes = plt.subplots(1, 3, figsize=(15, 5), layout='constrained')
            for ax, value, title in zip(axes[:2], [bv, av], ['January 2021 surface', 'October 2021 surface']):
                im = ax.imshow(value, cmap='terrain', vmin=740, vmax=960)
                ax.set_title(title)
                ax.set_xlabel('Column (1 m spacing)')
                ax.set_ylabel('Row (north at top)')
            fig.colorbar(im, ax=axes[:2], label='Stored surface height (vertical reference unverified)')
            delta = np.ma.array(av.data-bv.data, mask=~valid)
            cm = plt.colormaps['RdBu_r'].copy()
            cm.set_bad('lightgray')
            imd = axes[2].imshow(delta, cmap=cm, vmin=-10, vmax=10)
            axes[2].set_title('October minus January')
            axes[2].set_xlabel('Column (1 m spacing)')
            axes[2].set_ylabel('Row (north at top)')
            fig.colorbar(imd, ax=axes[2], extend='both', label='Raw difference; color clipped at +/-10')
            fig.suptitle('Melamchi: exploratory 1 km window. No deposit mask or error threshold; not a sediment-thickness map.', fontsize=12)
            fig.savefig(figure, dpi=150)
            plt.close(fig)
    return result

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--before', required=True, type=Path)
    parser.add_argument('--after', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--figure', type=Path)
    args=parser.parse_args()
    result=inspect(args.before,args.after,args.figure)
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(result['window'],indent=2))
