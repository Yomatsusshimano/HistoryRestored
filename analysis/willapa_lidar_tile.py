"""Read actual NOAA tile and render a declared native-coordinate window; no registration fit."""
import hashlib,json
from pathlib import Path
import laspy,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
file=ROOT/'sources/originals/cascadia/willapa-lidar-2002/20020326_17_ld_p3.copc.laz'
expected='6ce2dfff5ff066eded358ead7977d26c66ff1b79de2c2d6656d3b0e650bc34f5'
assert hashlib.sha256(file.read_bytes()).hexdigest()==expected
p=laspy.read(file);h=p.header
x,y,z=np.asarray(p.x),np.asarray(p.y),np.asarray(p.z)
bounds=dict(xmin=419600.,xmax=421400.,ymin=5164000.,ymax=5165180.)
dx=dy=5.;nx=int((bounds['xmax']-bounds['xmin'])/dx);ny=int((bounds['ymax']-bounds['ymin'])/dy)
selected=(x>=bounds['xmin'])&(x<bounds['xmax'])&(y>=bounds['ymin'])&(y<bounds['ymax'])
xx,yy,zz=x[selected],y[selected],z[selected]
ix=((xx-bounds['xmin'])/dx).astype(int);iy=((yy-bounds['ymin'])/dy).astype(int)
key=iy*nx+ix;order=np.argsort(key);keys=key[order];zs=zz[order]
unique,starts,counts=np.unique(keys,return_index=True,return_counts=True)
medians=np.full(nx*ny,np.nan)
for k,s,n in zip(unique,starts,counts):medians[k]=np.median(zs[s:s+n])
grid=medians.reshape(ny,nx);countgrid=np.bincount(key,minlength=nx*ny).reshape(ny,nx)
classes,cn=np.unique(p.classification,return_counts=True)
out=dict(source_id='S278',file=str(file.relative_to(ROOT)).replace('\\','/'),sha256=expected,
    tile_point_n=int(h.point_count),observed_point_n=len(p.points),header_min_xyz=h.mins.tolist(),header_max_xyz=h.maxs.tolist(),
    decoded_min_xyz=[float(v.min()) for v in [x,y,z]],decoded_max_xyz=[float(v.max()) for v in [x,y,z]],
    header_bound_residual_m=[max(abs(float(v.min())-lo),abs(float(v.max())-hi)) for v,lo,hi in zip([x,y,z],h.mins,h.maxs)],
    header_bounds_agree_within_half_coordinate_quantization=[bool(max(abs(float(v.min())-lo),abs(float(v.max())-hi))<=scale/2+1e-8) for v,lo,hi,scale in zip([x,y,z],h.mins,h.maxs,h.scales)],
    coordinate_quantization_m=h.scales.tolist(),crs_wkt=h.parse_crs().to_wkt(),
    class_counts={str(k):int(v) for k,v in zip(classes,cn)},
    gps_time_min=float(np.min(p.gps_time)),gps_time_max=float(np.max(p.gps_time)),creation_date=None if h.creation_date is None else h.creation_date.isoformat(),
    diagnostic_window_native_UTM=bounds,cell_size_m=5,window_point_n=int(selected.sum()),
    grid_cell_n=nx*ny,occupied_cell_n=len(unique),empty_cell_n=nx*ny-len(unique),
    window_point_z_quantiles_NAVD88_m={str(q):float(np.quantile(zz,q)) for q in [0,.05,.5,.95,1]},
    limitations='Current processed tile, not original flight file. Class2 is producer classification, not proof of every ground return. ZeroGPS times are not exposure times. Native crop has no datum transformation, core join, historical shoreline overlay or event interpretation. Empty cells remain empty; median is not a terrain interpolation or measured accretion rate.')
(ROOT/'data/willapa-lidar-tile.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
fig,axes=plt.subplots(1,2,figsize=(12,5))
extent=[bounds['xmin']/1000,bounds['xmax']/1000,bounds['ymin']/1000,bounds['ymax']/1000]
im=axes[0].imshow(grid,origin='lower',extent=extent,cmap='terrain',vmin=-1.5,vmax=5)
fig.colorbar(im,ax=axes[0],label='Median reported elevation (m NAVD88)',shrink=.8)
im=axes[1].imshow(np.where(countgrid>0,countgrid,np.nan),origin='lower',extent=extent,cmap='viridis',vmin=0,vmax=20)
fig.colorbar(im,ax=axes[1],label='Points per 5m cell',shrink=.8)
for ax,title in zip(axes,['Native elevation diagnostic','Sampling coverage; white cells empty']):
    ax.set(xlabel='NAD83(HARN) UTM10N easting (km)',ylabel='Northing (km)',title=title)
fig.suptitle('2002 Willapa lidar: actual tile17, current GEOID18 processing',fontsize=12)
fig.text(.04,.02,'No shoreline/core registration. 5m cell medians; no filling of missing cells. Zero point timestamps; acquisition day unverified.',fontsize=9)
fig.tight_layout(rect=[0,.06,1,.94]);fig.savefig(ROOT/'research/figures/willapa-lidar-native.png',dpi=150);plt.close(fig)
print(json.dumps({k:v for k,v in out.items() if k!='crs_wkt'},indent=2))
