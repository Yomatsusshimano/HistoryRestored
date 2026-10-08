import math
import unittest
from campo_fraction_check import conventional_age, required_fraction

class FractionChecks(unittest.TestCase):
    def test_age_reference_and_roundtrip(self):
        self.assertEqual(conventional_age(1), 0)
        self.assertAlmostEqual(conventional_age(math.exp(-10000/8033)), 10000)

    def test_mixture_endpoints_and_known_interior(self):
        self.assertEqual(required_fraction(.2,.2,.6),0)
        self.assertEqual(required_fraction(.6,.2,.6),1)
        self.assertAlmostEqual(required_fraction(.3,.2,.6),.25)

    def test_unidentifiable_and_outside_mixture(self):
        with self.assertRaises(ValueError): required_fraction(.3,.2,.2)
        self.assertGreater(required_fraction(.8,.2,.6),1)

if __name__ == '__main__': unittest.main()
