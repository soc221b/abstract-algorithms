import unittest
from random import random
from lib.tree import Node
from lib.tree import BinaryTree


class TestNode(unittest.TestCase):

    def test_init(self):
        node = Node()
        self.assertEqual(node.value, None)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)
        r = random()
        node = Node(r)
        self.assertEqual(node.value, r)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)

    def test_value_property(self):
        r = random()
        node = Node()
        node.value = r
        self.assertEqual(node.value, r)

    def test_left_property(self):
        r = random()
        node = Node()
        left_node = Node(r)
        node.left = left_node
        self.assertEqual(node.left, left_node)

    def test_right_property(self):
        r = random()
        node = Node()
        right_node = Node(r)
        node.right = right_node
        self.assertEqual(node.right, right_node)


class TestBinaryTree(unittest.TestCase):

    def test_insert(self):
        bt = BinaryTree()
        bt.insert(Node(3))
        bt.insert(Node(1))
        bt.insert(Node(5))
        self.assertLess(bt.root.value, bt.root.right.value)
        self.assertLess(bt.root.left.value, bt.root.value)
