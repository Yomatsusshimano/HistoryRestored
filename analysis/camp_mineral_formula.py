"""Audit published formula labels; no replacement geological interpretation."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/camp-century-mineral-formulas.json').read_text(encoding='utf-8'))
results=[]
for row in d['rows']:
    m={k:v['value'] for k,v in row['minerals'].items()}
    actual=m['Albite']+m['Pyrite']+m['Calcite (low Mg)']
    assert math.isclose(actual,row['combined_cached'],abs_tol=1e-12)
    labelled=m['Amphibole']+m['CaFe-amphibole']+m['Pyroxene']
    results.append({'segment':row['segment'],'grain_size_um':row['grain_size_um'],
        'source_formula_sum_percent_area':actual,
        'label_based_sum_percent_area':labelled,
        'garnet_over_source_formula_sum':m['Garnet']/actual,
        'garnet_over_label_based_sum':m['Garnet']/labelled})
out={'scope':'Source formulas reproduce cached values. Alternative sums use workbook mineral labels only; not validated replacement mineralogy. No pooling across size fractions without weights.','results':results}
(ROOT/'analysis/camp-mineral-formula-result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
