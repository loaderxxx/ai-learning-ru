"""Offline teaching example: inspect synthetic rows, never call a model or service."""
import argparse
from collections import defaultdict
from decimal import Decimal
import json
from pathlib import Path
import re
import sys

FIELDS = {'row', 'order_id', 'status', 'amount', 'currency'}
MONEY = re.compile(r'(?:0|[1-9][0-9]{0,11}|[1-9][0-9]{0,2}(?:[ \u00a0][0-9]{3}){1,3})(?:[.,][0-9]{1,2})?')
IDENTIFIER = re.compile(r'[A-Za-z0-9_-]{1,30}')


def parse_amount(value):
    if value is None:
        return None
    if not isinstance(value, str) or not MONEY.fullmatch(value):
        raise ValueError('amount must be a nonnegative decimal string or null')
    return Decimal(value.replace(' ', '').replace('\u00a0', '').replace(',', '.'))


def analyze_orders(rows):
    if not isinstance(rows, list) or len(rows) > 10000:
        raise ValueError('input must be a list of at most 10000 rows')
    groups = defaultdict(list)
    row_ids = set()
    amounts = {}
    for item in rows:
        if not isinstance(item, dict) or set(item) != FIELDS:
            raise ValueError('unexpected row fields')
        for field in ('row', 'order_id'):
            if not isinstance(item[field], str) or not IDENTIFIER.fullmatch(item[field]):
                raise ValueError('invalid identifier')
        if item['row'] in row_ids:
            raise ValueError('row identifiers must be unique')
        row_ids.add(item['row'])
        if item['status'] not in ('paid', 'refunded', 'cancelled'):
            raise ValueError('unsupported status')
        if item['currency'] not in ('RUB', 'USD'):
            raise ValueError('unsupported currency')
        amounts[item['row']] = parse_amount(item['amount'])
        groups[item['order_id']].append(item)
    conflicts = set()
    for order_id, members in groups.items():
        signatures = {(m['status'], m['currency'], amounts[m['row']]) for m in members}
        if len(signatures) > 1:
            conflicts.add(order_id)
    totals = defaultdict(lambda: Decimal('0'))
    included, excluded, seen = [], [], set()
    for item in rows:
        row_id, order_id = item['row'], item['order_id']
        if order_id in conflicts:
            reason = 'conflicting_order'
        elif order_id in seen:
            reason = 'duplicate'
        else:
            seen.add(order_id)
            if item['status'] != 'paid':
                reason = 'status:' + item['status']
            elif amounts[row_id] is None:
                reason = 'missing_amount'
            else:
                totals[item['currency']] += amounts[row_id]
                included.append(row_id)
                continue
        excluded.append({'row': row_id, 'reason': reason})
    return {'input_rows': len(rows), 'included_rows': included, 'excluded_rows': excluded,
            'totals_by_currency': {k: format(v, '.2f') for k, v in sorted(totals.items())},
            'scope': 'known paid nonconflicting orders only; no currency conversion'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    args = parser.parse_args()
    try:
        rows = json.loads(args.input.read_text(encoding='utf-8'))
        report = analyze_orders(rows)
    except (OSError, UnicodeError, ValueError) as exc:
        print('Invalid input: ' + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
