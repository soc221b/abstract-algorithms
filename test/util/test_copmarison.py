import unittest

from lib.util.comparison import Comparison


class TestComparison(unittest.TestCase):

    def test_comparison(self):
        comparison = Comparison()
        self.assertEqual(comparison.less_closure(1, 2), 1 < 2)
        self.assertEqual(comparison.less_closure(1, 1), 1 < 1)

        self.assertEqual(comparison.greater_closure(1, 0), 1 > 0)
        self.assertEqual(comparison.greater_closure(1, 1), 1 > 1)

        self.assertEqual(comparison.less_equal_closure(1, 2), 1 <= 2)
        self.assertEqual(comparison.less_equal_closure(1, 1), 1 <= 1)

        self.assertEqual(comparison.greater_equal_closure(1, 0), 1 >= 0)
        self.assertEqual(comparison.greater_equal_closure(1, 1), 1 >= 1)

        self.assertEqual(comparison.equal_closure(1, 1), 1 == 1)
        self.assertEqual(comparison.equal_closure(1, 0), 1 == 0)

        self.assertEqual(comparison.not_equal_closure(1, 2), 1 != 2)
        self.assertEqual(comparison.not_equal_closure(1, 1), 1 != 1)

        self.assertEqual(comparison.compare_closure(1, 2), -1)
        self.assertEqual(comparison.compare_closure(2, 1), 1)
        self.assertEqual(comparison.compare_closure(1, 1), 0)
