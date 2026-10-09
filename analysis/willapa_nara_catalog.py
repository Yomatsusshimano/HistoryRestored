"""Audit NARA's RG23 open-export files using the published acquisition manifest.

Run: python analysis/willapa_nara_catalog.py tmp/research/nara-rg23
The directory must contain the400unchanged JSONLfiles listed in the ledger.
Fetch URLs are base_url + object key. This script makes no API/contact requests.
"""
from pathlib import Path
import argparse
import hashlib
import json


def matches(record):
    result=[]
    if record.get('naId')==305404:result.append('target_series')
    if any(a.get('naId')==305404 for a in record.get('ancestors',[])):
        result.append('target_series_ancestor')
    if any(t in (record.get('title') or '').lower() for t in ('willapa','willpa')):
        result.append('target_place_title')
    return result


def audit(directory):
    ledger=json.loads(Path('data/willapa-nara-catalog-acquisition.json').read_text(encoding='utf-8'))
    selected=[];count=0
    for item in ledger['objects']:
        path=directory/Path(item['key']).name
        payload=path.read_bytes()
        assert len(payload)==item['size']
        assert hashlib.sha256(payload).hexdigest()==item['sha256'], path.name
        rows=0
        for i,line in enumerate(payload.splitlines(),1):
            if not line:continue
            record=json.loads(line)['record'];rows+=1
            why=matches(record)
            if why:selected.append({'file':path.name,'line':i,'reasons':why,'raw_json_line':line.decode('utf-8')})
        assert rows==item['record_count']
        count+=rows
    selected.sort(key=lambda x:(x['file'],x['line']))
    assert count==11823 and len(selected)==2
    assert not any('target_series_ancestor' in m['reasons'] for m in selected)
    excerpt=Path('sources/originals/cascadia/nara-rg23-selected.jsonl').read_bytes()
    expected=('\n'.join(m['raw_json_line'] for m in selected)+'\n').encode('utf-8')
    assert excerpt==expected, 'Record excerpts differ from source lines'
    result={'source_id':'S270','files_checked':len(ledger['objects']),'records_checked':count,
            'target_series_descendant_matches':0,
            'selected':[{'file':m['file'],'line':m['line'],'reasons':m['reasons'],
                         'naId':json.loads(m['raw_json_line'])['record']['naId'],
                         'title':json.loads(m['raw_json_line'])['record']['title']} for m in selected],
            'scope':'Titles and exact series/ancestor identifiers in this hash-recorded RG23 export only; not an OCR search or physical holdings audit.'}
    Path('data/willapa-nara-catalog-audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Audited400files/11823descriptions; series and chart matched, no target-series descendants in this export.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory',type=Path)
    audit(parser.parse_args().directory)
