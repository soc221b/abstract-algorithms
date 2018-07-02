import unittest

from lib.tree.node import Node
from lib.tree.node_common_closure import (
    self_closure,
    left_setter_closure,
    left_closure,
    right_setter_closure,
    right_closure,
    less_closure,
)


class TestCommonClosure(unittest.TestCase):

    def test_common_closure(self):
        root = Node(1)
        left = Node(0)
        right = Node(2)

        self.assertEqual(self_closure(root), root)

        left_setter_closure(root, left)
        left_1 = root.left
        root.left = left
        left_2 = root.left
        self.assertEqual(left_1, left_2)
        self.assertEqual(left_closure(root), left_1)

        right_setter_closure(root, right)
        right_1 = root.right
        root.right = right
        right_2 = root.right
        self.assertEqual(right_1, right_2)
        self.assertEqual(right_closure(root), right_1)

        self.assertTrue(less_closure(root, right))
        self.assertFalse(less_closure(root, root))
        self.assertFalse(less_closure(root, left))
