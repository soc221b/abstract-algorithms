import unittest
from random import random

from lib.tree import Node


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
