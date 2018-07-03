from lib.tree.tree_common_closure import (
    smaller_side_closure,
    larger_side_closure,
)


class BinaryTreeSearchingAdapter():

    def __init__(self, binary_tree, **kwargs):
        self.__binary_tree = binary_tree
        self.__root = binary_tree.root
        self.__smaller_side_closure = kwargs.get(
            'smaller_side_closure', smaller_side_closure)
        self.__larger_side_closure = kwargs.get(
            'larger_side_closure', larger_side_closure)

    def __getattr__(self, name):
        return getattr(self.__binary_tree, name)

    def minimum(self):
        curr = self.__root
        while (curr is not None and
               self.__smaller_side_closure(curr) is not None):
            curr = self.__smaller_side_closure(curr)
        return curr

    def maximum(self):
        curr = self.__root
        while (curr is not None and
               self.__larger_side_closure(curr) is not None):
            curr = self.__larger_side_closure(curr)
        return curr
