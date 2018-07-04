from lib.sort.sort_common_closure.sort_common_closure import (
    sort_by_algo_and_parse_kwargs,
)


def bubble_sort(iterative, **kwargs):
    """
    less_closure: function optional
    reversed: bool optional
    swap_closure: function optional
    """
    sort_by_algo_and_parse_kwargs(iterative, __bubble_sort, **kwargs)


def __bubble_sort(iterative, swap, comparison):
    for index_a in range(len(iterative)):
        for index_b in range(len(iterative)):
            if comparison.less_closure(iterative[index_a], iterative[index_b]):
                swap(iterative, index_a, index_b)
