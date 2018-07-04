class Node():
    def __init__(self, v=None):
        self.__left = None
        self.__right = None
        self.__value = v

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, x):
        self.__left = x

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, x):
        self.__right = x

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, x):
        self.__value = x

    def copy(self):
        copied_node = Node(self.__value)
        copied_node.left = self.__left
        copied_node.right = self.__right
        return copied_node
