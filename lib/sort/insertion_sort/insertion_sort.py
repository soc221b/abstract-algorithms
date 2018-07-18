from lib.sort.sort_common_closure.sort_common_closure import (
    sort_by_algo_and_parse_kwargs,
    swap_closure,
)


def insertion_sort(iterative, *,
                   swap_closure=swap_closure,
                   reverse=False,
                   less_closure=None):
    """
    less_closure: function optional
    reverse: optional
    swap_closure: function optional
    """
    sort_by_algo_and_parse_kwargs(iterative, __insertion_sort,
                                  swap_closure=swap_closure,
                                  reverse=reverse,
                                  less_closure=less_closure)


def __insertion_sort(iterative, swap, comparison):
    for index in range(len(iterative)):
        unsort_start_index = index
        sorted_end_index = unsort_start_index - 1
        while (0 <= sorted_end_index and
               comparison.less_closure(iterative[unsort_start_index],
                                       iterative[sorted_end_index])):
            swap(iterative, sorted_end_index, sorted_end_index + 1)
            sorted_end_index -= 1
            unsort_start_index -= 1
