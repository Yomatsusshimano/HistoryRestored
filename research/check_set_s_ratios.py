"""Compare ratios of published means; no uncertainty or tephra-classification test."""
import json
from pathlib import Path
r=Path(__file__).resolve().parents[1]
d=json.loads((r/'data/set-s-tephra-check.json').read_text(encoding='utf-8'))
for g in d['groups']:
    for oxide in ['Fe2O3','CaO']:
        so=g['So'][oxide]/g['So']['K2O'];sg=g['Sg'][oxide]/g['Sg']['K2O']
        print(f"{g['group']}: {oxide}/K2O So={so:.4f}; Sg={sg:.4f}; Sg>So={sg>so}")
