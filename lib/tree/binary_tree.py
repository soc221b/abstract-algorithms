from lib.tree.node_common_closure import (
    left_setter_closure,
    left_closure,
    right_setter_closure,
    right_closure,
    less_closure
)
from lib.util.comparison_closure import Comparison
from lib.util.common_closure import is_none_closure


class BinaryTree():

    def __init__(self, *,
                 less_closure=Comparison(less_closure=less_closure).less_closure,
                 left_closure=left_closure,
                 ight_closure=right_closure,
                 is_none_closure=is_none_closure):
        """
        less_closure: function
                      given two parameters which type is node's type,
                      return bool which determine first is less than second
        left_closure: function
                      given one parameter which is a node,
                      return left node of it.
        right_closure: function
                       given one parameter which is a node,
                       return right node of it.
        """
        self.__less_closure = less_closure
        self.__left_closure = left_closure
        self.__right_closure = right_closure
        self.__is_none_closure = is_none_closure

        self.__root = None

    @property
    def root(self):
        return self.__root

    def insert(self, node):
        self.__root = self.__insert_to_root(node, self.__root)
        return self.__root

    def __insert_to_root(self, node, root):
        if self.__is_none_closure(root):
            root = node
        else:
            if self.__less_closure(node, root):
                new_left = self.__insert_to_root(node, left_closure(root))
                left_setter_closure(root, new_left)
            else:
                new_right = self.__insert_to_root(node, right_closure(root))
                right_setter_closure(root, new_right)

        return root
