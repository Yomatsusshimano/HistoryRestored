"""Audit recovered attribute and geometry consistency, not coastline change."""
from pathlib import Path
import base64,collections,hashlib,json,math,struct

source=Path('data/willapa-geodatabase-rows.json')
tables=json.loads(source.read_text(encoding='utf-8-sig'))['tables']
domains={}
for row in tables['GDB_CodedDomains']:
 b=base64.b64decode(row['CodedValues']['base64']);count,kind=struct.unpack_from('<IH',b);p=6;pairs={}
 for _ in range(count):
  if kind==2:code=struct.unpack_from('<H',b,p)[0];p+=2
  elif kind==8:end=b.index(0,p);code=b[p:end].decode('ascii');p=end+1
  else:raise ValueError(kind)
  end=b.index(0,p);label=b[p:end].decode('ascii');p=end+1;pairs[str(code)]=label
 assert p==len(b)
 domains[str(row['DomainID'])]=pairs
def shape(row):
 b=base64.b64decode(row['Shape']['base64']);typ=struct.unpack_from('<I',b)[0]
 assert typ in (3,5),typ
 bounds=struct.unpack_from('<4d',b,4);parts,n=struct.unpack_from('<2I',b,36)
 starts=list(struct.unpack_from('<'+'I'*parts,b,44));offset=44+4*parts
 assert len(b)==offset+16*n
 points=[struct.unpack_from('<2d',b,offset+16*i) for i in range(n)]
 assert starts[0]==0 and all(x<y for x,y in zip(starts,starts[1:]))
 rings=[points[s:e] for s,e in zip(starts,starts[1:]+[n])]
 computed=(min(x for x,y in points),min(y for x,y in points),max(x for x,y in points),max(y for x,y in points))
 assert all(abs(a-b)<1e-8 for a,b in zip(computed,bounds))
 length=sum(math.hypot(x2-x1,y2-y1) for r in rings for (x1,y1),(x2,y2) in zip(r,r[1:]))
 area=None
 if typ==5:
  assert all(r[0]==r[-1] for r in rings)
  area=abs(sum(sum((x1-r[0][0])*(y2-r[0][1])-(x2-r[0][0])*(y1-r[0][1]) for (x1,y1),(x2,y2) in zip(r,r[1:]))/2 for r in rings))
 return {'shape_type':typ,'parts':parts,'points':n,'bounds':list(bounds),'computed_length':length,'computed_area':area}
summaries={};features={}
for name in ['wc46c03lines','wc46c03lines_83','wc46c03polys','wc46c03polys_83']:
 rows=tables[name];decoded=[]
 for row in rows:
  result=shape(row);result['id']=row.get('OBJECTID',row.get('OID'))
  result['length_difference']=result['computed_length']-row['Shape_Length']
  assert math.isclose(result['computed_length'],row['Shape_Length'],rel_tol=1e-9,abs_tol=1e-8)
  if result['computed_area'] is not None:
   result['area_difference']=result['computed_area']-row['Shape_Area']
   assert math.isclose(result['computed_area'],row['Shape_Area'],rel_tol=1e-6,abs_tol=1e-4)
  decoded.append(result)
 geom=next(x for x in tables['GDB_GeomColumns'] if x['TableName']==name)
 sr=next(x for x in tables['GDB_SpatialRefs'] if x['SRID']==geom['SRID'])
 summaries[name]={'count':len(rows),'srid':geom['SRID'],'stored_crs':sr['SRTEXT'],'max_length_difference':max(abs(x['length_difference']) for x in decoded),'max_area_difference':max([abs(x.get('area_difference',0)) for x in decoded]),'geometry_records':decoded}
 for key in ['Feature','SRC_Date','GIS_Date','Data_Sourc','Extract_Te','Ext_Meth','Scale','Source_ID','f_name']:
  if key in rows[0]:summaries[name][key+'_counts']=dict(collections.Counter(str(x[key]) for x in rows))
for left,right,idkey in [('wc46c03lines','wc46c03lines_83','OBJECTID'),('wc46c03polys','wc46c03polys_83','OID')]:
 a={x[idkey]:x for x in tables[left]};b={x[idkey]:x for x in tables[right]};assert a.keys()==b.keys()
 for i in a:
  for key in a[i]:
   if key not in ['Shape','Shape_Length','Shape_Area']:assert a[i][key]==b[i][key]
out={'source_id':'S253','row_export_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'domains':domains,'tables':summaries,'checks':'All shape byte counts, part boundaries, bounding boxes and stored lengths/areas compared; paired IDs/nongeometry attributes match. Source counts129lines/54polygons each. No datum transformation, topology validation, raster-line authentication or historical displacement test.','limits':'Projected tables are declared NAD27 UTM10N; _83tables NAD83 geographic. Geometry agreement checks software consistency only. CCoast stored-domain labels do not validate original ecological assignments. Dates/template descriptions retained separately.'}
Path('data/willapa-vector-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'line_counts':summaries['wc46c03lines']['Feature_counts'],'polygon_counts':summaries['wc46c03polys']['f_name_counts'],'checks':out['checks']}))
