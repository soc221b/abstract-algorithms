import unittest

from lib.sort import (
    insertion_sort,
    selection_sort,
    bubble_sort,
)
from test.helper import (
    assertListEqualByKey,
    get_random_list,
    get_random_embedded_list,
    get_random_embedded_node,
)


class TestSort(unittest.TestCase):

    def test_bubble_sort(self):
        self.__test_n_square_complexity_sort(bubble_sort)

    def test_selection_sort(self):
        self.__test_n_square_complexity_sort(selection_sort)

    def test_insertion_sort(self):
        self.__test_n_square_complexity_sort(insertion_sort)

    def __test_n_square_complexity_sort(self, sort):
        self.__test_sort_boundary(sort)
        self.__test_sort_in_median_size(sort)
        self.__test_sort_reversed(sort)

    def __test_n_log_n_complexity_sort(self, sort):
        self.__test_n_square_complexity_sort(sort)
        self.__test_sort_in_large_size(sort)

    def __test_sort_reversed(self, sort):
        self.__test_sort_boundary(sort)
        self.__test_sort_boundary(sort, reversed=True)
        self.__test_sort_boundary(sort, reversed=False)

    def __test_sort_boundary(self, sort, **kwargs):
        self.__test_sort_in_range(sort, range(0, 10**1), **kwargs)

    def __test_sort_in_median_size(self, sort, **kwargs):
        self.__test_sort_in_range(sort, range(10**1, 10**2), **kwargs)

    def __test_sort_in_large_size(self, sort, **kwargs):
        self.__test_sort_in_range(sort, range(10**3, 10**10), **kwargs)

    def __test_sort_in_range(self, sort, range_, **kwargs):
        self.__test_sort_in_range_default(sort, range_, **kwargs)
        self.__test_sort_in_range_with_custom_less(sort, range_, **kwargs)
        self.__test_sort_in_range_with_custom_swap_only_property(
            sort, range_, **kwargs)

    def __test_sort_in_range_default(self, sort, range_, **kwargs):
        for size in range_:
            shuffle_list = get_random_list(size)
            sort_list = sorted(shuffle_list)
            actual = shuffle_list
            sort(actual, **kwargs)
            if kwargs.get('reversed', False) is True:
                self.assertEqual(sort_list[::-1], actual)
            else:
                self.assertEqual(sort_list, actual)

    def __test_sort_in_range_with_custom_less(self, sort, range_, **kwargs):
        for size in range_:
            shuffle_list = get_random_embedded_list(size)
            sort_list = sorted(shuffle_list, key=lambda x: x[1])
            actual = shuffle_list
            kwargs['less_closure'] = lambda a, b: a[1] < b[1]
            sort(actual, **kwargs)
            if kwargs.get('reversed', False) is True:
                assertListEqualByKey(
                    self, sort_list[::-1], actual, lambda x: x[1])
            else:
                assertListEqualByKey(self, sort_list, actual, lambda x: x[1])

    def __test_sort_in_range_with_custom_swap_only_property(
            self, sort, range_, **kwargs):
        for size in range_:
            shuffle_list = get_random_embedded_node(size)
            sort_list = sorted(shuffle_list, key=lambda x: x.value)
            actual = []
            for node in shuffle_list:
                actual.append(node.copy())
            # test no-effect step1: append id to each node as its index of list
            for index in range(len(actual)):
                actual[index].id = index
            kwargs['swap_closure'] = swap_node_value
            kwargs['less_closure'] = lambda a, b: a.value < b.value
            sort(actual, **kwargs)
            if kwargs.get('reversed', False) is True:
                assertListEqualByKey(
                    self, sort_list[::-1], actual, lambda x: x.value)
            else:
                assertListEqualByKey(
                    self, sort_list, actual, lambda x: x.value)
            # test no-effect step2: test node is not exchanged
            for index, node in enumerate(actual):
                self.assertEqual(index, node.id)


def swap_node_value(iterative, index_a, index_b):
    iterative[index_a].value, iterative[index_b].value = (
        iterative[index_b].value, iterative[index_a].value)
