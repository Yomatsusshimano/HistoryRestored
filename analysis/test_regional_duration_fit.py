import unittest
from regional_duration_fit import constrained_fit
class DurationTests(unittest.TestCase):
    def test_known_gaussians(self):
        years=list(range(0,41));a=[-.5*((t-10)/5)**2 for t in years];b=[-.5*((t-30)/5)**2 for t in years]
        same=constrained_fit(years,a,b,0)
        self.assertEqual(same['best_Bonneville_CE'],20)
        self.assertAlmostEqual(same['log_likelihood_loss'],4)
        self.assertAlmostEqual(constrained_fit(years,a,b,10)['log_likelihood_loss'],1)
        self.assertEqual(constrained_fit(years,a,b,20)['log_likelihood_loss'],0)
    def test_reverse_order_and_edges(self):
        r=constrained_fit([0,1,2],[-2,-1,0],[0,-1,-2],2)
        self.assertEqual(r['log_likelihood_loss'],0)
        self.assertEqual(r['best_Bonneville_CE'],2)
        self.assertEqual(r['best_Electron_CE'],0)
if __name__=='__main__':unittest.main()
