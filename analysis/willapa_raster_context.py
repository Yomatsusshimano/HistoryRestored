"""Audit stored raster placement, not shoreline change or survey accuracy."""
from pathlib import Path
import hashlib,json,re,math
from PIL import Image

base=Path('sources/originals/cascadia/T-03921')
image=base/'t03921_dd.jpg'
world=base/'t03921_dd.jgw'
meta=base/'t03921.met'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
with Image.open(image) as im: width,height=im.size
a,d,b,e,c,f=[float(x) for x in world.read_text().split()]
def xy(col,row): return [a*col+b*row+c,d*col+e*row+f]
corners=[xy(col,row) for col,row in [(-.5,-.5),(width-.5,-.5),(width-.5,height-.5),(-.5,height-.5)]]
bounds=[min(p[0] for p in corners),min(p[1] for p in corners),max(p[0] for p in corners),max(p[1] for p in corners)]
s=meta.read_text()
expected=[float(re.search(k+r':\s*([-\d.]+)',s).group(1)) for k in ['West_Bounding_Coordinate','South_Bounding_Coordinate','East_Bounding_Coordinate','North_Bounding_Coordinate']]
assert a>0 and e<0 and d==b==0
assert xy(0,0)==[c,f]
assert all(abs(x-y)<=.001 for x,y in zip(bounds,expected)),(bounds,expected)
out={
 'source_ids':['S251','S252'],'method':'Six-value world-file affine transform using pixel centers; outer edges at half-pixel offset. No CRS conversion or shoreline extraction.',
 'files':[{'path':p.as_posix(),'sha256':digest(p),'bytes':p.stat().st_size} for p in [image,world,meta]],
 'raster_dimensions_pixels':[width,height],
 'world_file_order':['A','D','B','E','C','F'],'world_file_values':[a,d,b,e,c,f],
 'declared_crs':'Geographic NAD83; decimal degrees per source metadata',
 'corner_edges_lon_lat':corners,'calculated_bounds_wsen':bounds,'metadata_bounds_wsen':expected,
 'checks':'Positive horizontal/negative vertical spacing, no stored rotation, pixel0 center equals stored origin; calculated bounds within0.001degree of rounded metadata.',
 'reported_rectification_rms_m':{'x':.391,'y':.628},
 'metadata_dates':{'citation_publication':'192201','source_publication':'192206','source_content_range':['192201','192206'],'content_range_labeled_ground_condition':['20060123','20060123'],'georeferencing_process':'20060123','metadata':'20060125'},
 'limits':'RMS values are source-reported fitting residuals, not independently validated full positional uncertainty. World file supplies placement, not original survey accuracy, elevation, tide correction or historical change. Mixed metadata date roles retained.'
}
Path('data/willapa-raster-context.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'dimensions':[width,height],'bounds':bounds,'reported_rms_m':out['reported_rectification_rms_m']}))
