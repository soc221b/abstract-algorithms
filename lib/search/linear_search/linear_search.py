from lib.util import Comparison


def linear_search(iterative, target, **kwargs):
    comparison = Comparison(less_closure=kwargs.get("less_closure", None))
    for index, item in enumerate(iterative):
        flag = comparison.compare_closure(target, item)
        if flag == -1:
            break
        elif flag == 0:
            return index
    return None
