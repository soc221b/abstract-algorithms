from lib.util import Comparison


def parse_reversed(iterative, swap, *, reverse=False):
    if reverse is True:
        for i in range(len(iterative) // 2):
            swap(iterative, i, len(iterative) - i - 1)


def swap_closure(iterative, index_a, index_b):
    iterative[index_a], iterative[index_b] = (
        iterative[index_b], iterative[index_a])


def sort_by_algo_and_parse_kwargs(iterative, sort_algo, *,
                                  swap_closure=swap_closure,
                                  reverse=False,
                                  less_closure=None):
    comparison = Comparison(less_closure=less_closure)

    sort_algo(iterative, swap_closure, comparison)

    parse_reversed(iterative, swap_closure, reverse=reverse)
