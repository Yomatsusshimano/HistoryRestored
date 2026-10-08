"""Known geometry checks, not validation of geological evidence."""
import math
import unittest
from missoula_controls import spherical_distance


class GeometryTests(unittest.TestCase):
    def test_coincident(self):
        a = {'latitude':47.4, 'longitude':-120.2}
        self.assertEqual(spherical_distance(a,a),0)

    def test_quarter_equator(self):
        a = {'latitude':0, 'longitude':0}
        b = {'latitude':0, 'longitude':90}
        self.assertAlmostEqual(spherical_distance(a,b,1),math.pi/2)

    def test_dateline(self):
        a = {'latitude':0, 'longitude':179}
        b = {'latitude':0, 'longitude':-179}
        self.assertAlmostEqual(spherical_distance(a,b,1),math.radians(2))


if __name__ == '__main__':
    unittest.main()
