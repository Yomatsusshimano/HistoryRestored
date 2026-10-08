"""Check sums of reported scenario components, not the historical flood model."""
import json
from decimal import Decimal
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'data/tanabe-height-scenarios.json').read_text(encoding='utf-8'))
for row in data['scenarios']:
    total = sum(Decimal(str(v)) for v in row['additive_components_m'].values())
    assert total == Decimal(str(row['component_sum_m'])), row['id']
    print(f"{row['id']}: component sum {total} m; printed total {row['printed_total_m']} m")
print('Arithmetic only; inputs, historical location, tides and land movement not validated.')
