import math,unittest
from camp_exposure_limit import crossing,weighted_normal
class LimitsTests(unittest.TestCase):
    def test_accumulation_inverse(self):
        p,l,t=30,.000001,16000
        self.assertAlmostEqual(crossing(p/l*(-math.expm1(-l*t)),p,l),t)
    def test_boundaries(self):
        self.assertEqual(crossing(0,30,.001),0)
        self.assertTrue(math.isinf(crossing(30000,30,.001)))
        self.assertIsNone(crossing(-1,30,.001))
    def test_gaussian_weighted_mean(self):
        m,s=weighted_normal([2,4],[1,1])
        self.assertEqual(m,3); self.assertAlmostEqual(s,math.sqrt(.5))
if __name__=='__main__': unittest.main()
