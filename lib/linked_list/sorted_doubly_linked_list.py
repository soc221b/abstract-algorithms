from lib.linked_list import DoublyListNode as ListNode
from lib.linked_list import DoublyLinkedList


class SortedDoublyLinkedList(DoublyLinkedList):

    def __init__(self):
        self.__head = ListNode(0)
        self.__tail = self.__head
        self.__len = 0

    # O(n)
    def insert(self, x):
        new_node = ListNode(x)
        prev = self.find_smaller_than(x)
        if self.is_empty() or prev == self.__tail:
            prev.next = new_node
            new_node.prev = prev
            self.__tail = new_node
        else:
            new_node.prev = prev
            new_node.next = next
            prev.next = new_node
            next.prev = new_node
        self.__len += 1
        return new_node

    # O(n)
    def find_smaller_than(self, x):
        prev = self.__head
        while prev.next is not None and prev.next.var < x:
            prev = self.successor(prev)
        return prev

    # O(1)
    def minimumn(self):
        if self.is_empty():
            raise KeyError
        else:
            return self.__head.next

    # O(1)
    def maximum(self):
        if self.is_empty():
            raise KeyError
        else:
            return self.__tail

    # O(1)
    def delete(self, node):
        predecessor = self.predecessor(node)
        successor = self.successor(node)
        if self.size() == 1:
            self.__head.next = None
            self.__tail = self.__head
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

    # O(n)
    def search(self, x):
        curr = self.__head.next
        while curr is not None and curr.var != x:
            curr = self.successor(curr)
        return curr

    # O(1)
    def successor(self, node):
        # no verification for node whether it in this list or not.
        return node.next

    # O(1)
    def __len__(self):
        return self.__len

    # O(1)
    def is_empty(self):
        return self.__len == 0
