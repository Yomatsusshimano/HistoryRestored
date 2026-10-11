"""Reproduce limited source-summary arithmetic; no transaction authentication."""
import json
from decimal import Decimal as D
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/eiffel-operating-receipts.json').read_text(encoding='utf-8'))
checks=[]
def check(name,actual,expected):
    checks.append({'name':name,'calculated_francs':str(actual),'reported_francs':str(D(expected)),'matches':actual==D(expected)})
check('receipt_summary',sum(D(row['francs']) for row in data['receipt_summary']),data['reported_receipt_total'])
check('ticket_after_exhibition_share',D(data['ticket_gross'])-D(data['exhibition_share']),data['ticket_net'])
check('souvenir_margin',D(data['souvenir_sales'])-D(data['souvenir_purchase_cost']),data['souvenir_margin'])
check('board_scope_bridge',D(data['reported_receipt_total'])+D(data['cash_share_payments'])+D(data['exhibition_share']),data['reported_board_total'])
check('expense_deductions',sum(D(x) for x in data['expense_deductions']),data['reported_expense_deductions'])
check('expense_after_deductions',D(data['expense_subtotal'])-D(data['reported_expense_deductions']),data['expense_net'])
assert all(c['matches'] for c in checks),checks
result={'source_id':'S17','checks':checks,'receipt_minus_listed_expenses_francs':str(D(data['reported_receipt_total'])-D(data['expense_net'])),'status':'SOURCE_SUMMARY_ARITHMETIC_ONLY','not_validated':['Original transactions','Net profit','All constituent expense rows','Capital repayment','Construction financing','Scientific hypothesis']}
(root/'analysis/eiffel-operating-receipts-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
