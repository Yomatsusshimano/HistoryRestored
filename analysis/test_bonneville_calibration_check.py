import unittest
from bonneville_calibration_check import interpolate,summarize
class CalibrationChecks(unittest.TestCase):
    def test_interpolation_nodes_and_midpoint(self):
        self.assertEqual(interpolate([0,10],[100,200],0),100)
        self.assertEqual(interpolate([0,10],[100,200],5),150)
        self.assertEqual(interpolate([0,10],[100,200],10),200)
        with self.assertRaises(ValueError):interpolate([0,10],[100,200],11)
    def test_symmetric_likelihood(self):
        years=list(range(900,1101)); logs=[-.5*((y-1000)/10)**2 for y in years]
        r=summarize(years,logs)
        self.assertEqual(r['mode_CE'],1000)
        self.assertEqual(r['equal_tail_95_4_CE'],[980,1020])
if __name__=='__main__':unittest.main()
