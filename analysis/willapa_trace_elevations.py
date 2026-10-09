"""Documented datum conversion and nearest measured lidar points; no registration fit."""
import base64,hashlib,json,struct
from pathlib import Path
import laspy,numpy as np,pyproj
from pyproj.aoi import AreaOfInterest
from pyproj.transformer import TransformerGroup
from scipy.spatial import cKDTree
from shapely.geometry import LineString
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
GRID_DIR=ROOT/'sources/originals/cascadia/proj-harn'
GRIDS={'us_noaa_nadcon5_nad83_1986_nad83_harn_conus.tif':'e12ac2e886edafe616e0994c610ad3daa01db17c00d0e9938145d956f249fc2f',
       'us_noaa_WO.tif':'e6380daed501df8cfbb38149accb8b731e7b00e21368b2a8f6f696ac4eeb5f06'}
for name,sha in GRIDS.items():assert hashlib.sha256((GRID_DIR/name).read_bytes()).hexdigest()==sha
pyproj.network.set_network_enabled(False);pyproj.datadir.append_data_dir(str(GRID_DIR))
tile=ROOT/'sources/originals/cascadia/willapa-lidar-2002/20020326_17_ld_p3.copc.laz'
assert hashlib.sha256(tile.read_bytes()).hexdigest()=='6ce2dfff5ff066eded358ead7977d26c66ff1b79de2c2d6656d3b0e650bc34f5'
p=laspy.read(tile);h=p.header;target=h.parse_crs().sub_crs_list[0]
group=TransformerGroup(4269,target,always_xy=True,allow_ballpark=False,area_of_interest=AreaOfInterest(-124.3,46.3,-123.6,46.8))
assert group.best_available and len(group.transformers)==2
rowsfile=ROOT/'data/willapa-geodatabase-rows.json'
rows=json.loads(rowsfile.read_text(encoding='utf-8-sig'))['tables']['wc46c03lines_83']
rows={r['OBJECTID']:r for r in rows if r['OBJECTID'] in [49,50,51,52]};assert len(rows)==4
x,y,z=np.asarray(p.x),np.asarray(p.y),np.asarray(p.z)
tree=cKDTree(np.column_stack([x,y]));results=[];plotrows={}
for ident,row in sorted(rows.items()):
    raw=base64.b64decode(row['Shape']['base64']);parts,n=struct.unpack_from('<2I',raw,36)
    starts=list(struct.unpack_from('<'+'I'*parts,raw,44))
    coords=np.array(struct.unpack_from('<'+'d'*(2*n),raw,44+4*parts)).reshape(-1,2)
    paths=[];checks=[]
    for transform in group.transformers:
        tx,ty=transform.transform(coords[:,0],coords[:,1],errcheck=True)
        backlon,backlat=transform.transform(tx,ty,direction='INVERSE',errcheck=True)
        _,_,backdist=pyproj.Geod(ellps='GRS80').inv(coords[:,0],coords[:,1],backlon,backlat)
        paths.append(np.column_stack([tx,ty]));checks.append(float(np.max(np.abs(backdist))))
    inter=np.linalg.norm(paths[0]-paths[1],axis=1)
    sampling=[];details=[];sensitivity=[];offset=0
    for part,(a,b) in enumerate(zip(starts,starts[1:]+[n])):
        line=LineString(paths[0][a:b]);d=np.arange(0,line.length,10.)
        if len(d)==0 or d[-1]!=line.length:d=np.append(d,line.length)
        points=np.array([line.interpolate(v).coords[0] for v in d]);dist,index=tree.query(points,k=1)
        lon,lat=group.transformers[0].transform(points[:,0],points[:,1],direction='INVERSE',errcheck=True)
        altx,alty=group.transformers[1].transform(lon,lat,errcheck=True)
        alternate=np.column_stack([altx,alty]);altdist,altindex=tree.query(alternate,k=1)
        sensitivity.append(dict(part=part,query_n=len(d),changed_nearest_point_n=int(np.sum(index!=altindex)),
            max_query_shift_m=float(np.max(np.linalg.norm(points-alternate,axis=1))),
            radius_variants=[dict(radius_m=radius,alternate_matched_n=int(np.sum(altdist<=radius)),
                changed_inclusion_n=int(np.sum((dist<=radius)!=(altdist<=radius))),
                alternate_median_z_NAVD88_m=float(np.median(z[altindex[altdist<=radius]])) if np.any(altdist<=radius) else None)
                for radius in [5.,10.]]))
        # Same source samples retained under both5m and10m declared radius variants.
        for radius in [5.,10.]:
            valid=dist<=radius;vals=z[index[valid]]
            details.append(dict(part=part,radius_m=radius,query_n=len(d),matched_n=int(valid.sum()),unique_nearest_point_n=len(np.unique(index[valid])),
                nearest_z_quantiles_m={str(q):float(np.quantile(vals,q)) for q in [0,.05,.5,.95,1]} if len(vals) else None))
        sampling.extend(dict(part=part,distance_along_part_m=float(v),distance_along_feature_m=float(v+offset),
            query_x_HARN_m=float(pt[0]),query_y_HARN_m=float(pt[1]),nearest_distance_m=float(dd),
            nearest_point_index=int(j),nearest_z_NAVD88_m=float(z[j]) if dd<=10 else None,
            passes5m=bool(dd<=5),passes10m=bool(dd<=10)) for v,pt,dd,j in zip(d,points,dist,index))
        offset+=line.length
    matched=[r['nearest_z_NAVD88_m'] for r in sampling if r['passes5m']]
    result=dict(id=ident,feature_code=row['Feature'],source_id=row['Source_ID'],source_date=row['SRC_Date'],
        digitization_date=row['GIS_Date'],vertices=n,part_n=parts,length_transformed_m=offset,
        max_method_difference_at_vertices_m=float(np.max(inter)),max_inverse_roundtrip_m_by_method=checks,
        sample_n=len(sampling),matched5m_n=len(matched),matched10m_n=sum(r['passes10m'] for r in sampling),
        median_z_NAVD88_m_5m=float(np.median(matched)) if matched else None,
        part_radius_summaries=details,alternate_operation_sensitivity=sensitivity,samples=sampling)
    results.append(result);plotrows[ident]=paths[0]
out=dict(source_ids=['S253','S278','S279'],row_export_sha256=hashlib.sha256(rowsfile.read_bytes()).hexdigest(),
    pyproj_version=pyproj.__version__,proj_version=pyproj.proj_version_str,network_enabled=False,ballpark_allowed=False,
    target_crs=target.to_wkt(),grids=[dict(name=n,sha256=s,url='https://cdn.proj.org/'+n) for n,s in GRIDS.items()],
    operations=[dict(description=t.description,pipeline=t.definition,accuracy_m=t.accuracy) for t in group.transformers],
    selected_operation_index=0,sampling_spacing_m=10,results=results,
    limitations='Retrospective source-location diagnostic. NAD83stored datum interpreted per declared CRS; original epoch/accuracy not independently established. No registration fit or tidal conversion. Nearest point elevations are2002source observations at nearby positions, not1922elevations, habitat classifications, event dates or deformation. Radii/spacing are diagnostics, not validated error tolerances. Reused nearest points are dependent.')
(ROOT/'data/willapa-trace-elevations.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')

# Render native5m median surface plus4fixed, transformed traces; empty cells remain blank.
extent=[419600.,421400.,5164000.,5165180.];nx,ny=360,236
mask=(x>=extent[0])&(x<extent[1])&(y>=extent[2])&(y<extent[3])
ix=((x[mask]-extent[0])/5).astype(int);iy=((y[mask]-extent[2])/5).astype(int);key=iy*nx+ix
order=np.argsort(key);keys=key[order];zs=z[mask][order];u,sizes0,counts=np.unique(keys,return_index=True,return_counts=True)
grid=np.full(nx*ny,np.nan)
for k,a,n in zip(u,sizes0,counts):grid[k]=np.median(zs[a:a+n])
fig,(ax,bx)=plt.subplots(1,2,figsize=(13,5.5));colors={49:'#b02a9b',50:'#ff7f0e',51:'#2b2b2b',52:'#d62728'}
im=ax.imshow(grid.reshape(ny,nx),origin='lower',extent=np.array(extent)/1000,cmap='terrain',vmin=-1.5,vmax=5)
fig.colorbar(im,ax=ax,shrink=.75,label='5m cell median (m NAVD88)')
for result in results:
    ident=result['id'];points=plotrows[ident];kind='marsh' if result['feature_code']==15 else 'MHW'
    for a,b in zip(list(struct.unpack_from('<'+'I'*result['part_n'],base64.b64decode(rows[ident]['Shape']['base64']),44)),
                   list(struct.unpack_from('<'+'I'*result['part_n'],base64.b64decode(rows[ident]['Shape']['base64']),44))[1:]+[len(points)]):
        ax.plot(points[a:b,0]/1000,points[a:b,1]/1000,color=colors[ident],lw=1.3)
    samples=result['samples'];d=[r['distance_along_feature_m'] for r in samples if r['passes5m']]
    vals=[r['nearest_z_NAVD88_m'] for r in samples if r['passes5m']]
    bx.scatter(d,vals,s=8,color=colors[ident],label=f'{ident}: historical {kind}')
ax.set(xlim=np.array(extent[:2])/1000,ylim=np.array(extent[2:])/1000,xlabel='HARN UTM10N easting (km)',ylabel='Northing (km)',title='Fixed historical traces on 2002 lidar')
bx.set(xlabel='Distance along transformed feature (m)',ylabel='Nearest reported elevation (m NAVD88)',title='Nearest points within 5 m; gaps retained')
bx.legend(fontsize=8);bx.grid(alpha=.2)
fig.suptitle('Historical trace locations versus measured lidar surface',fontsize=13)
fig.text(.04,.025,'Documented datum conversion; no alignment fit. 1922 labels are not 2002 shoreline or habitat observations. Exact tide and historical elevation unknown.',fontsize=9)
fig.tight_layout(rect=[0,.07,1,.93]);fig.savefig(ROOT/'research/figures/willapa-trace-elevations.png',dpi=150);plt.close(fig)
print(json.dumps([{k:v for k,v in r.items() if k not in ['samples','part_radius_summaries']} for r in results],indent=2))
