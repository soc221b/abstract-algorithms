import unittest

from lib.tree import Node, BinaryTree, BinaryTreeSearchingDecorator


"""
                  10
          /                \
         5                  15
     /       \            /     \
    2         8         13       17
   / \       / \       /  \     /  \
  N   4     6   N    12    N   N    18
     / \   / \      /  \           /  \
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


class TestTreeSearchingDecorator(unittest.TestCase):

    def test_decorator(self):
        # visit to BinaryTree's property
        BinaryTreeSearchingDecorator(empty_binary_tree).root

    def test_minimum(self):
        self.assertEqual(
            BinaryTreeSearchingDecorator(empty_binary_tree).minimum(),
            None)
        self.assertEqual(
            BinaryTreeSearchingDecorator(binary_tree).minimum(),
            n2)

    def test_maximum(self):
        self.assertEqual(
            BinaryTreeSearchingDecorator(empty_binary_tree).maximum(),
            None)
        self.assertEqual(
            BinaryTreeSearchingDecorator(binary_tree).maximum(),
            n19)
