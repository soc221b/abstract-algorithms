from lib.linked_list import SinglyListNode as ListNode
from lib.linked_list import SinglyLinkedList


class SortedSinglyLinkedList(SinglyLinkedList):

    # O(n)
    def insert(self, x):
        new_node = ListNode(x)
        prev = self.find_smaller_than(x)
        if prev == self.__tail:
            prev.next = new_node
            self.__tail = new_node
        else:
            new_node.next = prev.next
            prev.next = new_node
        self.__len += 1
        return new_node

    # O(n)
    def find_smaller_than(self, x):
        prev = self._SinglyLinkedList__head
        while prev.next is not None and prev.next.var < x:
            prev = self.successor(prev)
        return prev

    # O(1)
    def minimumn(self):
        if self.is_empty():
            raise KeyError
        else:
            return self._SinglyLinkedList__head.next

    # O(1)
    def maximum(self):
        if self.is_empty():
            raise KeyError
        else:
            return self.__tail
