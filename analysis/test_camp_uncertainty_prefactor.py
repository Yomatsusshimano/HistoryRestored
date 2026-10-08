import unittest
from camp_uncertainty_prefactor import summary

class WeightedSummaryTests(unittest.TestCase):
    def test_equal_weights(self):
        self.assertEqual(summary([1,3],[1,1]),(2,1))
    def test_inverse_square_root_weights(self):
        mean,_=summary([0,3],[1,4])
        self.assertEqual(mean,1)
    def test_uniform_measurements_have_zero_spread(self):
        self.assertEqual(summary([4,4,4],[1,4,9]),(4,0))

if __name__=='__main__': unittest.main()
