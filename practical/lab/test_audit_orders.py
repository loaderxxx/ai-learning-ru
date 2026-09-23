import copy
from decimal import Decimal
import json
from pathlib import Path
import unittest
from audit_orders import analyze_orders, parse_amount


def row(**changes):
    value = {'row': 'r1', 'order_id': 'A-1', 'status': 'paid', 'amount': '10.00', 'currency': 'RUB'}
    value.update(changes)
    return value


class AuditTests(unittest.TestCase):
    def test_fixture_arithmetic_and_lineage(self):
        root = Path(__file__).resolve().parents[1]
        report = analyze_orders(json.loads((root / 'fixtures/orders.json').read_text()))
        self.assertEqual(report['totals_by_currency'], {'RUB': '3500.00', 'USD': '25.00'})
        self.assertEqual(report['included_rows'], ['r01', 'r02', 'r06', 'r08'])
        self.assertEqual(len(report['excluded_rows']), 6)
        self.assertEqual(report['input_rows'], 10)

    def test_semantically_equal_duplicate(self):
        report = analyze_orders([row(amount='1 200,00'), row(row='r2', amount='1200.00')])
        self.assertEqual(report['totals_by_currency'], {'RUB': '1200.00'})
        self.assertEqual(report['excluded_rows'], [{'row': 'r2', 'reason': 'duplicate'}])

    def test_conflict_excludes_whole_group(self):
        report = analyze_orders([row(), row(row='r2', amount='11.00')])
        self.assertEqual(report['totals_by_currency'], {})
        self.assertEqual([x['reason'] for x in report['excluded_rows']], ['conflicting_order'] * 2)

    def test_currencies_never_added_together(self):
        report = analyze_orders([row(), row(row='r2', order_id='A-2', currency='USD')])
        self.assertEqual(report['totals_by_currency'], {'RUB': '10.00', 'USD': '10.00'})

    def test_missing_not_zero(self):
        report = analyze_orders([row(amount=None)])
        self.assertEqual(report['totals_by_currency'], {})
        self.assertEqual(report['excluded_rows'][0]['reason'], 'missing_amount')

    def test_nonpaid_excluded(self):
        for status in ('cancelled', 'refunded'):
            with self.subTest(status=status):
                report = analyze_orders([row(status=status)])
                self.assertEqual(report['totals_by_currency'], {})
                self.assertEqual(report['excluded_rows'][0]['reason'], 'status:' + status)

    def test_bad_amounts_rejected(self):
        for amount in ('NaN', '-1', '1,234', '1 2', '1e4', '', True, 1.2):
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                analyze_orders([row(amount=amount)])

    def test_schema_rejected(self):
        for value in ({}, [None], [dict(row(), extra=1)], [row(order_id=[])], [row(status={})]):
            with self.subTest(value=value), self.assertRaises(ValueError):
                analyze_orders(value)

    def test_empty(self):
        report = analyze_orders([])
        self.assertEqual(report['input_rows'], 0)
        self.assertEqual(report['totals_by_currency'], {})

    def test_input_unchanged(self):
        data = [row(), row(row='r2')]
        old = copy.deepcopy(data)
        analyze_orders(data)
        self.assertEqual(data, old)

    def test_size_limit(self):
        with self.assertRaises(ValueError):
            analyze_orders([row()] * 10001)

    def test_unknown_enums(self):
        for value in (row(status='pending'), row(currency='EUR')):
            with self.subTest(value=value), self.assertRaises(ValueError):
                analyze_orders([value])

    def test_duplicate_row_id(self):
        with self.assertRaises(ValueError):
            analyze_orders([row(), row()])

    def test_zero_and_decimal_conversion(self):
        self.assertEqual(parse_amount('1\u00a0500,25'), Decimal('1500.25'))
        self.assertEqual(analyze_orders([row(amount='0')])['totals_by_currency'], {'RUB': '0.00'})


if __name__ == '__main__':
    unittest.main()
