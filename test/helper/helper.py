from random import random, randint
from lib.tree import Node
from lib.design_pattern import Decorator


def assertListEqualByKey(self, list1, list2, key_closure):
    self.assertEqual(len(list1), len(list2))
    for i in range(len(list1)):
        self.assertEqual(key_closure(list1[i]), key_closure(list2[i]))


def get_random_list(size):
    """
    size: int
    return: list[int]
    """
    list_ = []
    while len(list_) < size:
        # continuous
        if random() < 0.5:
            # duplicate
            while True and len(list_) < size:
                list_.append(randint(0, size))
                if random() < 0.5:
                    break
    return list_


def get_random_embedded_list(size):
    """
    size: int
    return: list[list[int]]
    """
    list_ = []
    while len(list_) < size:
        # continuous
        if random() < 0.5:
            # duplicate
            while True and len(list_) < size:
                list_.append([randint(0, size), randint(0, size)])
                if random() < 0.5:
                    break
    return list_


def get_random_embedded_node(size):
    """
    size: int
    return: list[Node]
    """
    list_ = []
    while len(list_) < size:
        # continuous
        if random() < 0.5:
            # duplicate
            while True and len(list_) < size:
                list_.append(InfoNodeDecorator(Node(randint(0, size))))
                if random() < 0.5:
                    break
    return list_


class InfoNodeDecorator(Decorator):

    def __init__(self, base):
        super().__init__(base)
        self.__id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = id_

    def copy(self):
        copied_node = self.decorated_class.copy()
        copied_node = InfoNodeDecorator(copied_node)
        copied_node.id = self.__id
        return copied_node
