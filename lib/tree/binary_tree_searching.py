from lib.tree.tree_common_closure import (
    smaller_side_closure,
    larger_side_closure,
)
from lib.util.common_closure import is_none_closure


class BinaryTreeSearchingDecorator():

    def __init__(self, binary_tree, *,
                 smaller_side_closure=smaller_side_closure,
                 larger_side_closure=larger_side_closure,
                 is_none_closure=is_none_closure):
        self.__binary_tree = binary_tree
        self.__root = binary_tree.root
        self.__smaller_side_closure = smaller_side_closure
        self.__larger_side_closure = larger_side_closure
        self.__is_none_closure = is_none_closure

    def __getattr__(self, name):
        return getattr(self.__binary_tree, name)

    def minimum(self):
        curr = self.__root
        while (not self.__is_none_closure(curr) and
               not self.__is_none_closure(self.__smaller_side_closure(curr))):
            curr = self.__smaller_side_closure(curr)
        return curr

    def maximum(self):
        curr = self.__root
        while (not self.__is_none_closure(curr) and
               not self.__is_none_closure(self.__larger_side_closure(curr))):
            curr = self.__larger_side_closure(curr)
        return curr
