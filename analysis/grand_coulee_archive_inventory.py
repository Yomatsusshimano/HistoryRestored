"""Inventory nested source archives without extracting or executing their contents."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def inventory(path):
    expected=json.loads((ROOT/'data/grand-coulee-acquisition.json').read_text(encoding='utf-8'))['sha256']
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected:
        raise ValueError('Source archive differs from pinned acquisition')
    result={'source_id':'S126','outer_sha256':expected,'nested_archives':[],
            'limit':'Directory and projection text inspection only; geometry, workbook values and hydraulic model not validated.'}
    with zipfile.ZipFile(io.BytesIO(raw)) as outer:
        for name in outer.namelist():
            if not name.endswith('.zip') or name.startswith('__MACOSX/'):
                continue
            nested=outer.read(name)
            with zipfile.ZipFile(io.BytesIO(nested)) as inner:
                entries=[]
                for info in inner.infolist():
                    content=inner.read(info)
                    entry={'path':info.filename,'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest()}
                    if info.filename.endswith('.prj'):
                        entry['projection_text']=content.decode('utf-8')
                    entries.append(entry)
                result['nested_archives'].append({'path':name,'sha256':hashlib.sha256(nested).hexdigest(),'entries':entries})
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('archive',type=Path)
    args=parser.parse_args()
    result=inventory(args.archive)
    (ROOT/'data/grand-coulee-nested-inventory.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Nested archive inventory saved; no source code executed.')
