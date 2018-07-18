from lib.sort.sort_common_closure.sort_common_closure import (
    sort_by_algo_and_parse_kwargs,
    swap_closure,
)


def bubble_sort(iterative, *,
                swap_closure=swap_closure,
                reverse=False,
                less_closure=None):
    """
    less_closure: function optional
    reverse: bool optional
    swap_closure: function optional
    """
    sort_by_algo_and_parse_kwargs(iterative, __bubble_sort,
                                  swap_closure=swap_closure,
                                  reverse=reverse,
                                  less_closure=less_closure)


def __bubble_sort(iterative, swap, comparison):
    for index_a in range(len(iterative)):
        for index_b in range(len(iterative)):
            if comparison.less_closure(iterative[index_a], iterative[index_b]):
                swap(iterative, index_a, index_b)
