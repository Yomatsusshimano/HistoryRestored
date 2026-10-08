"""Checks interval geometry, including gaps and boundary-only overlap."""
import unittest
from sloth_intervals import common_set, minimum_cover


class IntervalTests(unittest.TestCase):
    def test_gap_is_not_filled(self):
        sets=[[[0,2],[8,10]], [[4,6]]]
        self.assertEqual(common_set(sets), [])
        self.assertEqual(minimum_cover(sets), {'minimum_span_calendar_years':2,'optimal_endpoint_witness_windows_cal_BP_young_old':[[2,4],[6,8]]})

    def test_touching_closed_endpoints(self):
        self.assertEqual(common_set([[[0,2]],[[2,5]]]), [[2,2]])
        self.assertEqual(minimum_cover([[[0,2]],[[2,5]]])['minimum_span_calendar_years'],0)

    def test_nested_ranges(self):
        self.assertEqual(common_set([[[0,10]],[[3,7]],[[4,6]]]),[[4,6]])

    def test_no_data_is_not_negative_result(self):
        with self.assertRaises(ValueError):
            common_set([])
        with self.assertRaises(ValueError):
            minimum_cover([[]])


if __name__=='__main__':
    unittest.main()
