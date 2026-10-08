"""Extract a declared candidate set from Schwing Table2; not the author's input file."""
import argparse,re,json,math,hashlib
from pathlib import Path
from collections import Counter
from pypdf import PdfReader
p=argparse.ArgumentParser();p.add_argument('pdf',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
r=PdfReader(a.pdf)
num=r'(-?\d+(?:\.\d+)?)'
pat=re.compile(r'^(.*?)\s+(AF(?:/LTD)?|TH(?:/LTD)?|LTD/AF|Thermal)\s+(N|R)\s+'+num+r'\s+'+num+r'\s+'+num+r'\s+([ABCD])\b')
start=re.compile(r'^(?:LCW\s+\d|HWW\s+\d|WC\s+\d|GS\s+\d|T-\d|SW-\d|BC\s+\d)')
rows=[];other=[]
for page in range(48,58):
 for line in r.pages[page-1].extract_text().splitlines():
  line=line.strip();m=pat.match(line)
  if m:
   name,demag,pol,dec,inc,mad,rank=m.groups()
   rows.append(dict(pdf_page=page,printed_page=page-8,sample=name,demagnetization=demag,polarity=pol,declination=float(dec),inclination=float(inc),MAD=float(mad),rank=rank,source_line=line))
  elif start.match(line):other.append(dict(pdf_page=page,source_line=line))
def mean(group):
 v=[]
 for x in group:
  dec,inc=map(math.radians,(x['declination'],x['inclination']))
  v.append((math.cos(inc)*math.cos(dec),math.cos(inc)*math.sin(dec),math.sin(inc)))
 x,y,z=[sum(q[i] for q in v) for i in range(3)];R=math.sqrt(x*x+y*y+z*z);n=len(v)
 return dict(N=n,declination=math.degrees(math.atan2(y,x))%360,inclination=math.degrees(math.atan2(z,math.hypot(x,y))),R=R,k=(n-1)/(n-R))
result=dict(source_id='S211',sha256=hashlib.sha256(a.pdf.read_bytes()).hexdigest(),selection='Every text-extracted Table2 specimen row on PDF48-57 labeled N/R with numeric DEC/INC/MAD and rank A/B/C. Thermal spelling retained. Equal specimen weights; no geographic, method or outlier exclusion. Not asserted to be original author selection.',inspection='Text extraction; previously visually checked HWW pages54-55. Remaining table scans require full transcription review.',rows=rows,unparsed_or_ineligible_specimen_lines=other,computed={pol:mean([x for x in rows if x['polarity']==pol and x['rank'] in 'ABC']) for pol in ('N','R')})
assert len({x['sample'] for x in rows})==len(rows)
a.output.write_text(json.dumps(result,indent=2)+'\n')
print('Extracted',len(rows),'numeric N/R rows;',len(other),'other specimen lines');print(result['computed'])
