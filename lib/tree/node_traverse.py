from lib.queue.queue import Queue
from lib.tree.node_common_closure import (
    left_closure,
    right_closure,
)
from lib.util.common_closure import (
    self_closure,
)


class NodeTraverseAdapter():

    def __init__(self, root, **kwargs):
        """
        root: Node-liked type
        value_closure: function, optional
                       pass only one parameter node and
                       return what you want it is extracted.
        left_closure: function
                      given one parameter which is a node,
                      return left node of it.
        right_closure: function
                       given one parameter which is a node,
                       return right node of it.
        """
        self.__root = root
        self.__value_closure = kwargs.get('value_closure', self_closure)
        self.__left_closure = kwargs.get('left_closure', left_closure)
        self.__right_closure = kwargs.get('right_closure', right_closure)

    def __getattr__(self, name):
        return getattr(self.__tree, name)

    def level_traversal(self):
        """
        return: list
                list of what returned by the value_closure
        """
        nodes = []
        que1 = Queue()
        que2 = Queue()

        if self.__root is not None:
            que1.push(self.__root)
            while not que1.is_empty():
                while not que1.is_empty():
                    peek = que1.peek()
                    if (peek is not None and
                        (self.__left_closure(peek) is not None or
                         self.__right_closure(peek) is not None)):
                        que2.push(self.__left_closure(peek))
                        que2.push(self.__right_closure(peek))
                    nodes.append(self.__value_closure(peek))
                    que1.pop()
                que1 = que2
                que2 = Queue()
        return nodes

    def pre_order_traversal(self):
        """
        return: list
                list of what returned by the value_closure
        """
        nodes = []
        if self.__root is not None:
            return self.__pre_order_traversal(self.__root, nodes)
        else:
            return nodes

    def __pre_order_traversal(self, root, nodes):
        root_is_not_none_and_has_child = root is not None and (
            self.__left_closure(root) is not None or
            self.__right_closure(root) is not None)

        nodes.append(self.__value_closure(root))
        if root_is_not_none_and_has_child:
            nodes = self.__pre_order_traversal(
                self.__left_closure(root), nodes)
        if root_is_not_none_and_has_child:
            nodes = self.__pre_order_traversal(
                self.__right_closure(root), nodes)

        return nodes

    def in_order_traversal(self):
        """
        return: list
                list of what returned by the value_closure
        """
        nodes = []
        if self.__root is not None:
            return self.__in_order_traversal(self.__root, nodes)
        else:
            return nodes

    def __in_order_traversal(self, root, nodes):
        root_is_not_none_and_has_child = root is not None and (
            self.__left_closure(root) is not None or
            self.__right_closure(root) is not None)

        if root_is_not_none_and_has_child:
            nodes = self.__in_order_traversal(
                self.__left_closure(root), nodes)
        nodes.append(self.__value_closure(root))
        if root_is_not_none_and_has_child:
            nodes = self.__in_order_traversal(
                self.__right_closure(root), nodes)

        return nodes

    def post_order_traversal(self):
        """
        return: list
                list of what returned by the value_closure
        """
        nodes = []
        if self.__root is not None:
            return self.__post_order_traversal(self.__root, nodes)
        else:
            return nodes

    def __post_order_traversal(self, root, nodes):
        root_is_not_none_and_has_child = root is not None and (
            self.__left_closure(root) is not None or
            self.__right_closure(root) is not None)

        if root_is_not_none_and_has_child:
            nodes = self.__post_order_traversal(
                self.__left_closure(root), nodes)
        if root_is_not_none_and_has_child:
            nodes = self.__post_order_traversal(
                self.__right_closure(root), nodes)
        nodes.append(self.__value_closure(root))

        return nodes

    def __repr__(self):
        nodes = self.level_traversal()
        for index, node in enumerate(nodes):
            if node is None and index * 2 + 1 < len(nodes):
                nodes.insert(index * 2 + 1, None)
                nodes.insert(index * 2 + 2, None)
        p = 0
        while 2**p < len(nodes):
            p += 1
        while len(nodes) < 2**p:
            nodes.append(None)

        res = ""
        if len(nodes):
            res += "{0}\n".format(self.__value_closure(nodes[0]))
            nodes = nodes[1:]
        index = 0
        p = 1
        while index < len(nodes):
            if nodes[index] is None:
                res += "None "
            else:
                res += "{0} ".format(self.__value_closure(nodes[index]))
            if index + 1 == pow(2, p):
                res += "\n"
                p += 1
            index += 1
        res += "\n"
        return res
