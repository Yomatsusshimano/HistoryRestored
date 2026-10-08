"""Analytical controls for weighted pooling, not scientific validation."""
import math
import unittest
from coyote_camel_pooling import combine
class PoolingTests(unittest.TestCase):
    def test_equal_errors_known_solution(self):
        m,s,q=combine([0,2],[1,1])
        self.assertEqual(m,1)
        self.assertAlmostEqual(s,1/math.sqrt(2))
        self.assertEqual(q,2)
    def test_translation_and_permutation(self):
        x=[20720,21010,21100];e=[75,70,270]
        a=combine(x,e);b=combine([v+1000 for v in reversed(x)],list(reversed(e)))
        self.assertAlmostEqual(b[0]-a[0],1000)
        self.assertAlmostEqual(b[1],a[1]);self.assertAlmostEqual(b[2],a[2])
    def test_error_scaling(self):
        a=combine([0,2,5],[1,2,3]);b=combine([0,2,5],[2,4,6])
        self.assertAlmostEqual(a[0],b[0]);self.assertAlmostEqual(b[1],2*a[1]);self.assertAlmostEqual(b[2],a[2]/4)
    def test_invalid_input(self):
        for x,e in [([1],[1]),([1,2],[1]),([1,2],[1,0])]:
            with self.assertRaises(ValueError):combine(x,e)
if __name__=='__main__':unittest.main()
