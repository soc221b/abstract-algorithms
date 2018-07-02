import unittest

from lib.design_pattern.decorator import Node, BalanceNode, ParentNode


class TestNode(unittest.TestCase):

    def test_node(self):
        node = Node(123)
        print(node._value)
        print(node._left)
        print(node._right)
        with self.assertRaises(AttributeError):
            print(node._balance)
        with self.assertRaises(AttributeError):
            print(node._height)
        with self.assertRaises(AttributeError):
            print(node._parent)

    def test_balance_node(self):
        node = BalanceNode(Node(123))
        print(node._value)
        print(node._left)
        print(node._right)
        print(node._balance)
        print(node._height)
        with self.assertRaises(AttributeError):
            print(node._parent)

    def test_parent_node(self):
        node = ParentNode(Node(123))
        print(node._value)
        print(node._left)
        print(node._right)
        print(node._parent)
        with self.assertRaises(AttributeError):
            print(node._balance)
        with self.assertRaises(AttributeError):
            print(node._height)

    def test_parent_balance_node(self):
        node = ParentNode(BalanceNode(Node(123)))
        print(node._value)
        print(node._left)
        print(node._right)
        print(node._parent)
        print(node._balance)
        print(node._height)
