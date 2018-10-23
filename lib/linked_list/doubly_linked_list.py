from lib.linked_list import DoublyListNode as ListNode
from lib.linked_list import SinglyLinkedList


class DoublyLinkedList(SinglyLinkedList):

    def __init__(self):
        self.__head = ListNode(0)
        self.__tail = self.__head
        self.__len = 0
        raise NotImplementedError  # no tested

    # O(1)
    def insert(self, x):
        new_node = ListNode(x, prev=self.__tail)
        self.__tail.next = new_node
        self.__tail = new_node
        self.__len += 1
        return new_node

    # O(1)
    def delete(self, node):
        predecessor = self.predecessor(node)
        successor = self.successor(node)
        if self.size() == 1:
            self.__head.next = None
            self.__tail = self.__head
        elif predecessor is None:  # the node is first node
            self.__head = successor
            successor.prev = None
        elif successor is None:  # the node is last node
            self.__tail = predecessor
            predecessor.next = None
        else:
            predecessor.next = successor
            successor.prev = predecessor
        self.__len -= 1

    # O(1)
    def predecessor(self, node):
        return node.prev
