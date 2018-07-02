import unittest

from lib.util.common_closure import self_closure


class TestCommonClosure(unittest.TestCase):

    def test_comparison(self):
        self.assertEqual(self, self_closure(self))
