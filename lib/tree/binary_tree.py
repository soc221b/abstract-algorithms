def left_setter_closure(n, x):
    n.left = x


def left_closure(n):
    return n.left


def right_setter_closure(n, x):
    n.right = x


def right_closure(n):
    return n.right


def less_closure(a, b):
    return a.value < b.value


class BinaryTree():

    def __init__(self, **kwargs):
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
        self.__less_closure = kwargs.get('less_closure', less_closure)
        self.__left_closure = kwargs.get('left_closure', left_closure)
        self.__right_closure = kwargs.get('right_closure', right_closure)

        self.__root = None

    @property
    def root(self):
        return self.__root

    def insert(self, node):
        self.__root = self.__insert_to_root(node, self.__root)
        return self.__root

    def __insert_to_root(self, node, root):
        if root is None:
            root = node
        else:
            if self.__less_closure(node, root):
                new_left = self.__insert_to_root(node, left_closure(root))
                left_setter_closure(root, new_left)
            else:
                new_right = self.__insert_to_root(node, right_closure(root))
                right_setter_closure(root, new_right)

        return root
