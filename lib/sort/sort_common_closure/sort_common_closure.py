from lib.util import Comparison


def sort_by_algo_and_parse_kwargs(iterative, sort_algo, **kwargs):
    comparison = Comparison(less_closure=kwargs.get('less_closure', None))
    swap = kwargs.get('swap_closure', swap_closure)

    sort_algo(iterative, swap, comparison)

    parse_reversed(iterative, swap, **kwargs)


def parse_reversed(iterative, swap, **kwargs):
    if kwargs.get('reversed', False) is True:
        for i in range(len(iterative) // 2):
            swap(iterative, i, len(iterative) - i - 1)


def swap_closure(iterative, index_a, index_b):
    iterative[index_a], iterative[index_b] = (
        iterative[index_b], iterative[index_a])
