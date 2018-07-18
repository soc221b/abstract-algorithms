from lib.sort.sort_common_closure.sort_common_closure import (
    sort_by_algo_and_parse_kwargs,
    swap_closure,
)


def selection_sort(iterative, *,
                   swap_closure=swap_closure,
                   reverse=False,
                   less_closure=None):
    """
    less_closure: function optional
    reverse: optional
    swap_closure: function optional
    """
    sort_by_algo_and_parse_kwargs(iterative, __selection_sort,
                                  swap_closure=swap_closure,
                                  reverse=reverse,
                                  less_closure=less_closure)


def __selection_sort(iterative, swap, comparison):
    for (index_a, elem_a) in enumerate(iterative):
        index_min = index_a
        for index_b, elem_b in enumerate(iterative[index_a + 1:]):
            if comparison.less_closure(elem_b, iterative[index_min]):
                index_min = index_a + index_b + 1
        swap(iterative, index_a, index_min)
