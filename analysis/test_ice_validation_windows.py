import unittest
from ice_validation_windows import window

class WindowTests(unittest.TestCase):
    def test_bce_ce_boundary(self):
        self.assertEqual(window({'era':'BCE','years_as_printed':[1,1]},1),{-1,0,1})
        self.assertEqual(window({'era':'CE','years_as_printed':[1,1]},1),{0,1,2})
    def test_inclusive_range(self):
        self.assertEqual(len(window({'era':'BCE','years_as_printed':[44,42]},3)),9)
    def test_overlap(self):
        a=window({'era':'CE','years_as_printed':[10,10]},1)
        b=window({'era':'CE','years_as_printed':[11,11]},1)
        self.assertEqual(len(a)+len(b),6)
        self.assertEqual(len(a|b),4)

if __name__=='__main__':unittest.main()
