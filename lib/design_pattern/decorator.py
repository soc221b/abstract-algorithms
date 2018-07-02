class Node():

    def __init__(self, x=None):
        self._value = x
        self._left = None
        self._right = None


class BalanceNode():

    def __init__(self, node):
        self._node = node
        self._balance = 0
        self._height = 1

    def __getattr__(self, name):
        return getattr(self._node, name)


class ParentNode():

    def __init__(self, node):
        self._node = node
        self._parent = None

    def __getattr__(self, name):
        return getattr(self._node, name)
