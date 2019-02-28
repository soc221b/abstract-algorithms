import unittest

from lib.tree import Node, BinaryTree, BinaryTreeTraverseDecorator


"""
                  10
             /
         5                  15
     /                    /
    2         8         13       17
   /         /         /        /
  N   4     6   N    12    N   N    18
     /     /        /              /
    3   N N   7    11   N         N    19
"""
empty_binary_tree = BinaryTree()
binary_tree = BinaryTree()
n10 = Node(10)
n5 = Node(5)
n2 = Node(2)
n4 = Node(4)
n3 = Node(3)
n8 = Node(8)
n6 = Node(6)
n7 = Node(7)
n15 = Node(15)
n13 = Node(13)
n12 = Node(12)
n11 = Node(11)
n17 = Node(17)
n18 = Node(18)
n19 = Node(19)
binary_tree.insert(n10)
binary_tree.insert(n5)
binary_tree.insert(n2)
binary_tree.insert(n4)
binary_tree.insert(n3)
binary_tree.insert(n8)
binary_tree.insert(n6)
binary_tree.insert(n7)
binary_tree.insert(n15)
binary_tree.insert(n13)
binary_tree.insert(n12)
binary_tree.insert(n11)
binary_tree.insert(n17)
binary_tree.insert(n18)
binary_tree.insert(n19)


class TestTreeTraverseDecorator(unittest.TestCase):

    def test_decorator(self):
        # visit to BinaryTree's property
        BinaryTreeTraverseDecorator(empty_binary_tree).root

    def test_level_traversal(self):
        self.assertEqual(
            BinaryTreeTraverseDecorator(empty_binary_tree).level_traversal(),
            [])
        self.assertEqual(
            BinaryTreeTraverseDecorator(binary_tree).level_traversal(),
            [n10, n5, n15, n2, n8, n13, n17, None, n4, n6, None,
             n12, None, None, n18, n3, None, None, n7, n11,
             None, None, n19])

    def test_pre_order_traversal(self):
        self.assertEqual(
            BinaryTreeTraverseDecorator(
                empty_binary_tree).pre_order_traversal(),
            [])
        self.assertEqual(
            BinaryTreeTraverseDecorator(binary_tree).pre_order_traversal(),
            [n10, n5, n2, None, n4, n3, None, n8, n6, None,
             n7, None, n15, n13, n12, n11, None, None, n17,
             None, n18, None, n19])

    def test_in_order_traversal(self):
        self.assertEqual(
            BinaryTreeTraverseDecorator(
                empty_binary_tree).in_order_traversal(),
            [])
        self.assertEqual(
            BinaryTreeTraverseDecorator(binary_tree).in_order_traversal(),
            [None, n2, n3, n4, None, n5, None, n6, n7, n8, None,
             n10, n11, n12, None, n13, None, n15, None, n17, None,
             n18, n19])

    def test_post_order_traversal(self):
        self.assertEqual(
            BinaryTreeTraverseDecorator(
                empty_binary_tree).post_order_traversal(),
            [])
        self.assertEqual(
            BinaryTreeTraverseDecorator(binary_tree).post_order_traversal(),
            [None, n3, None, n4, n2, None, n7, n6, None, n8, n5,
             n11, None, n12, None, n13, None, None, n19, n18, n17,
             n15, n10])
