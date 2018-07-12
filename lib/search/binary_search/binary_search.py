from lib.util import Comparison


def binary_search(iterative, target, **kwargs):
    comparison = Comparison(less_closure=kwargs.get("less_closure", None))
    left = 0
    right = len(iterative) - 1

    while left <= right:
        mid = left + (right - left) // 2
        flag = comparison.compare_closure(target, iterative[mid])
        if flag == -1:
            right = mid - 1
        elif flag == 1:
            left = mid + 1
        else:
            return mid
    return None
