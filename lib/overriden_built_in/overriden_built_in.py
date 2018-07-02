import inspect

from lib.stack.stack import Stack, reversed_stack
from lib.queue.queue import Queue, reversed_queue
from lib.deque.deque import Deque, reversed_deque


def reversed(obj):
    if isinstance(obj, Stack):
        return reversed_stack(obj)
    elif isinstance(obj, Queue):
        return reversed_queue(obj)
    elif isinstance(obj, Deque):
        return reversed_deque(obj)
    else:
        func_self = globals()[
            inspect.getframeinfo(inspect.currentframe()).function]
        del globals()['reversed']
        res = reversed(obj)
        globals()['reversed'] = func_self
        return res
