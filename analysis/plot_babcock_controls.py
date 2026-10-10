"""Create a source-attributed analytical figure after rendering the pinned maps.

Requires matplotlib, Pillow and Poppler's pdftoppm on PATH (or PDFTOPPM env var).
The crop PNGs are derived previews; original GeoPDF bytes remain unchanged.
"""
import json,os,subprocess
from pathlib import Path
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'analysis/babcock-page-locations-result.json').read_text(encoding='utf-8'))
cfg={'239888':dict(x=1130,y=1220,imprint=1992),'239889':dict(x=1130,y=1195,imprint=1968)}
fig,axes=plt.subplots(1,2,figsize=(12,6.7))
for ax,sheet in zip(axes,data['sheets']):
    identifier=sheet['identifier']; crop=cfg[identifier]
    preview=ROOT/f'tmp/research/babcock-{identifier}-controls'
    preview.parent.mkdir(parents=True,exist_ok=True)
    subprocess.run([os.environ.get('PDFTOPPM','pdftoppm'),'-r','180','-x',str(crop['x']),'-y',str(crop['y']),'-W','700','-H','650','-png','-singlefile',str(ROOT/f'sources/originals/missoula/babcock-quads/{identifier}.pdf'),str(preview)],check=True)
    image=Image.open(ROOT/f'tmp/research/babcock-{identifier}-controls.png')
    ax.imshow(image)
    for point in sheet['points']:
        x=point['page_x_pt']*180/72-crop['x']
        y=(sheet['page_height_pt']-point['page_y_pt'])*180/72-crop['y']
        assert 0<=x<image.width and 0<=y<image.height
        label='A' if point['id']=='S27-T1-12' else 'B'
        colour='#0b5bb5' if label=='A' else '#a10f2b'
        ax.plot(x,y,'o',markersize=7,color=colour,markeredgecolor='white',markeredgewidth=1)
        offset=(36,-43) if label=='A' else (-43,-30)
        ax.annotate(label,(x,y),xytext=offset,textcoords='offset points',fontsize=12,color=colour,
                    fontweight='bold',bbox=dict(facecolor='white',edgecolor=colour,boxstyle='round,pad=0.22'),
                    arrowprops=dict(arrowstyle='-',color=colour,linewidth=1.2))
    ax.set_title(f"USGS copy {identifier} | {crop['imprint']} imprint",fontsize=11)
    ax.set_axis_off()
fig.suptitle('Published control locations on historical map copies',fontsize=15,y=.98)
fig.text(.5,.065,'A: S27 crossing control     B: S27 noncrossing control     Separation approximately 99 m',ha='center',fontsize=10)
fig.text(.5,.035,'Both sheets: 1964 aerial photography, 1966 field check; 10 ft main contours. Marker placement is a registration diagnostic.',ha='center',fontsize=9)
fig.text(.5,.01,'Data available from U.S. Geological Survey, National Geospatial Program. No water level or event date derived.',ha='center',fontsize=8)
fig.tight_layout(rect=[0,.09,1,.94])
out=ROOT/'research/figures/babcock-historical-controls.png';out.parent.mkdir(exist_ok=True)
fig.savefig(out,dpi=160)
print(out.name)
