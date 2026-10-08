"""Compare published coordinates with explicit NADCON5 grid; no field validation."""
import argparse,json,hashlib
from pathlib import Path
import pyproj
from pyproj import Transformer,Geod
p=argparse.ArgumentParser();p.add_argument('grid',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
assert hashlib.sha256(a.grid.read_bytes()).hexdigest()=='c7d587e0d0b39b9f46c7de850b9a6a468c17b7139f82a313aa43aa4a64d94fa8'
# Explicit pipeline avoids silently accepting a ballpark/no-shift transformation.
pipeline=f'proj=pipeline step proj=unitconvert xy_in=deg xy_out=rad step proj=gridshift grids={a.grid.resolve().as_posix()} step proj=unitconvert xy_in=rad xy_out=deg'
t=Transformer.from_pipeline(pipeline)
lon,lat=t.transform(-116.1185556,32.9894722,errcheck=True)
d=Geod(ellps='GRS80').inv(lon,lat,-116.119412,32.989544)[2]
r={'source_ids':['S210','S215'],'source_transcription':{'S215':{'locator':'TableDR1 PDF pages1-2, visually checked','site':'04Pw30','latitude_NAD27':32.9894722,'longitude_NAD27':-116.1185556,'unit':'Wind Caves mbr','height_above_previous_site_m':20,'height_above_section_base_m':829.0,'samples_analyzed':6,'polarity':'N','grade':'b','top_upper_megabreccia_section_height_m':681.5,'overlying_contact_section_height_m':848.0,'fault_interval_note':'COMPLEX FAULTED INTERVAL in upper Pw, between04Pw28 and04Pw29'},'S210':{'locator':'Table4 Sheet1 row6','sample':'04PW30','latitude_NAD83':32.989544,'longitude_NAD83':-116.119412}},'transformation':{'pyproj_version':pyproj.__version__,'PROJ_version':pyproj.proj_version_str,'operation':'NAD27 to NAD83 (7), normalized longitude/latitude','operation_catalog_accuracy_m':0.15,'accuracy_limit':'Operation metadata, not GPS collection accuracy or a total error bar.','grid_url':'https://cdn.proj.org/us_noaa_nadcon5_nad27_nad83_1986_conus.tif','grid_sha256':hashlib.sha256(a.grid.read_bytes()).hexdigest(),'longitude_NAD83':lon,'latitude_NAD83':lat,'separation_from_S210_m':d},'height_comparison':{'table_relative_height_m':829.0-681.5,'S201_figure_graphical_height_m_approx':151,'difference_m_approx':151-(829.0-681.5),'interpretation':'Different table/figure representations; reason unresolved, not independent measurement uncertainty.'},'limits':'Proximity supports locality correspondence but does not prove specimen identity, custody, primary deposition, fault duplication or event age.'}
a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print('Separation metres:',d)
