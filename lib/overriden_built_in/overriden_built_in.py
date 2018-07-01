import inspect
from lib.stack import stack, reversed_stack
from lib.queue import queue, reversed_queue
from lib.deque import deque, reversed_deque


def reversed(obj):
    if isinstance(obj, stack):
        return reversed_stack(obj)
    elif isinstance(obj, queue):
        return reversed_queue(obj)
    elif isinstance(obj, deque):
        return reversed_deque(obj)
    else:
        func_self = globals()[
            inspect.getframeinfo(inspect.currentframe()).function]
        del globals()['reversed']
        res = reversed(obj)
        globals()['reversed'] = func_self
        return res
