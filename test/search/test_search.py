import unittest
from lib.search.binary_search import binary_search
from lib.search.linear_search import linear_search
from util.helper import (
    get_random_list,
)


class TestBinarySearch(unittest.TestCase):

    def test_linear_search(self):
        self.__test_n_complexity(linear_search)

    def test_binary_search(self):
        self.__test_log_n_complexity(binary_search)

    def __test_n_complexity(self, search):
        self.__test_boundary(search)
        self.__test_medium_size(search)

    def __test_log_n_complexity(self, search):
        self.__test_n_complexity(search)
        self.__test_large_size(search)

    def __test_boundary(self, search):
        self.__test_search_by_range(search, range(0, 2**2))

    def __test_medium_size(self, search):
        self.__test_search_by_range(search, range(2**2, 2**8))

    def __test_large_size(self, search):
        self.__test_search_by_range(search, range(2**10, 2**16))

    def __test_search_by_count(self, search, size):
        self.__test_search_by_range(search, range(size, size + 1))

    def __test_search_by_range(self, search, range_):
        for i in range_:
            items = sorted(get_random_list(i))
            for expect_index, item in enumerate(items):
                actual_index = search(items, item)
                self.assertEqual(items[expect_index], items[actual_index])
            for item in range_:
                if item not in items:
                    self.assertEqual(None, search(items, item))
