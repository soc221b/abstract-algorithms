import unittest

from lib.tree import Node, BinaryTree


class TestBinaryTree(unittest.TestCase):

    def test_insert(self):
        bt = BinaryTree()
        bt.insert(Node(3))
        bt.insert(Node(1))
        bt.insert(Node(5))
        self.assertLess(bt.root.value, bt.root.right.value)
        self.assertLess(bt.root.left.value, bt.root.value)
