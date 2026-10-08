"""Checks interval geometry, not source dates or event attribution."""
import unittest
from regional_event_windows import minimum_span


class WindowTests(unittest.TestCase):
    def test_overlap_and_touch(self):
        self.assertEqual(minimum_span([[1, 4], [2, 3]]), 0)
        self.assertEqual(minimum_span([[1, 2], [2, 5]]), 0)

    def test_gap_and_translation(self):
        self.assertEqual(minimum_span([[1, 2], [5, 8]]), 3)
        self.assertEqual(minimum_span([[105, 108], [101, 102]]), 3)

    def test_multiple_intervals(self):
        self.assertEqual(minimum_span([[1, 2], [3, 9], [7, 10]]), 5)

    def test_invalid(self):
        for value in [[], [[3, 2]], [[1]]]:
            with self.assertRaises(ValueError):
                minimum_span(value)


if __name__ == "__main__":
    unittest.main()
