"""Reproduce printed arithmetic comparisons; no transaction validation."""
import json
from decimal import Decimal as D
from pathlib import Path

root = Path(__file__).resolve().parents[1]
ledger = json.loads((root / 'data/eiffel-1890-statistical-report.json').read_text(encoding='utf-8'))
p = ledger['reported']
total = sum(D(row['francs']) for row in ledger['cost_rows'])
increase = total - D(p['initial_estimate_francs'])
capital = p['capital_shares'] * D(p['share_face_francs'])
quote = D(p['approximate_market_quote_francs'])
combined = p['combined_titles'] * quote
founder = p['founder_titles'] * quote
out = {
    'cost_row_sum': str(total),
    'cost_row_sum_matches_print': total == D(p['cost_francs']),
    'estimate_increase_calculated': str(increase),
    'printed_increase_excess': str(D(p['increase_francs']) - increase),
    'capital_calculated': int(capital),
    'printed_capital_excess': int(D(p['nominal_capital_francs']) - capital),
    'combined_market_value_at_400': int(combined),
    'printed_combined_value_excess': int(D(p['combined_market_value_francs']) - combined),
    'founder_value_at_400': int(founder),
    'printed_founder_value_excess': int(D(p['founder_value_francs']) - founder),
}
for key, value in out.items():
    if ledger['calculations'][key] != value:
        raise ValueError(f'Ledger calculation differs: {key}')
print(json.dumps(out, indent=2))
print('Printed arithmetic reproduced. Accounting scope and transactions unvalidated.')
