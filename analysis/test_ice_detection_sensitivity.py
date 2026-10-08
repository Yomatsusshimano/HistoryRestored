import unittest
from ice_detection_sensitivity import ordinal,backgrounds,classify,match_state

class DetectionTests(unittest.TestCase):
    def test_calendar(self):
        self.assertEqual(ordinal(1.5)-ordinal(-.5),1)
        with self.assertRaises(ValueError):ordinal(.5)
    def test_constant_and_spike(self):
        s={y:10.0 for y in range(100)};s[50]=20
        b=backgrounds(s)
        for scope in ['local_window','global_residual']:
            f,_=classify(s,b,scope,1)
            self.assertTrue(f[50]);self.assertFalse(f[49]);self.assertIsNone(f[0])
    def test_gap_is_not_compressed(self):
        s={y:1 for y in range(100)};s[50]=None
        b=backgrounds(s)
        self.assertIsNone(b[35]);self.assertIsNone(b[65]);self.assertEqual(b[34],1)
    def test_unknown_matches(self):
        self.assertEqual(match_state({1:False,2:None},[1,2]),'UNRESOLVED')
        self.assertEqual(match_state({1:True,2:None},[1,2]),'MATCH')
        self.assertEqual(match_state({1:False,2:False},[1,2]),'NO_MATCH')

if __name__=='__main__':unittest.main()
