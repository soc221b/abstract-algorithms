import unittest

from lib.tree.node import Node
from lib.tree.tree_common_closure import (
    smaller_side_closure,
    larger_side_closure
)


class TestNodeCommonClosure(unittest.TestCase):

    def test_node_common_closure(self):
        root = Node(1)
        left = Node(0)
        right = Node(2)

        root.left = left
        self.assertEqual(smaller_side_closure(root), left)

        root.right = right
        self.assertEqual(larger_side_closure(root), right)
