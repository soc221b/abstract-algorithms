import unittest

from lib.design_pattern.decorator import Decorator


class Node():

    def __init__(self, x=None):
        self._value = x
        self._left = None
        self._right = None


class BalanceNodeDecorator(Decorator):

    def __init__(self, base):
        super().__init__(base)
        self._balance = 0
        self._height = 1


class ParentNodeDecorator(Decorator):

    def __init__(self, base):
        super().__init__(base)
        self._parent = None


class TestNode(unittest.TestCase):

    def test_node(self):
        node = Node(123)
        node._value
        node._left
        node._right
        with self.assertRaises(AttributeError):
            node._balance
        with self.assertRaises(AttributeError):
            node._height
        with self.assertRaises(AttributeError):
            node._parent

    def test_balance_node(self):
        node = BalanceNodeDecorator(Node(123))
        node._value
        node._left
        node._right
        node._balance
        node._height
        with self.assertRaises(AttributeError):
            node._parent

    def test_parent_node(self):
        node = ParentNodeDecorator(Node(123))
        node._value
        node._left
        node._right
        node._parent
        with self.assertRaises(AttributeError):
            node._balance
        with self.assertRaises(AttributeError):
            node._height

    def test_parent_balance_node(self):
        node = ParentNodeDecorator(BalanceNodeDecorator(Node(123)))
        node._value
        node._left
        node._right
        node._parent
        node._balance
        node._height
