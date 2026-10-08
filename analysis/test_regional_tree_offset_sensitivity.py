import math,unittest
from regional_tree_offset_sensitivity import group_loglik
class CovarianceTests(unittest.TestCase):
    def test_single_observation_adds_variance(self):
        self.assertAlmostEqual(group_loglik([3],[4],2),-.5*(9/8+math.log(8)))
    def test_zero_tau_independent(self):
        self.assertAlmostEqual(group_loglik([2,3],[4,9],0),-.5*(2+math.log(36)))
    def test_two_observation_matrix_inverse(self):
        # Covariance [[5,1],[1,10]], determinant 49; inverse [[10,-1],[-1,5]]/49.
        expected=-.5*((10*4-2*2*3+5*9)/49+math.log(49))
        self.assertAlmostEqual(group_loglik([2,3],[4,9],1),expected)
if __name__=='__main__':unittest.main()
