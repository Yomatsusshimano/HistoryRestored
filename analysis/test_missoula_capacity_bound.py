import unittest
from missoula_capacity_bound import capacity_bound

class CapacityTests(unittest.TestCase):
    def test_units_and_volume_deficit(self):
        r=capacity_bound(100000,1000000,100)
        self.assertAlmostEqual(r['maximum_volume_through_section_km3'],8640)
        self.assertAlmostEqual(r['minimum_fraction_not_through_section_during_window'],.9136)
    def test_sufficient_capacity_is_not_negative_deficit(self):
        r=capacity_bound(1,1000000,1)
        self.assertEqual(r['minimum_volume_not_through_section_during_window_km3'],0)
        self.assertEqual(r['maximum_fraction_through_section'],1)
    def test_nonpositive_inputs_rejected(self):
        for values in [(0,1,1),(1,-1,1),(1,1,0)]:
            with self.assertRaises(ValueError): capacity_bound(*values)

if __name__ == '__main__': unittest.main()
