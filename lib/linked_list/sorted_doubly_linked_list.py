from lib.linked_list import DoublyListNode as ListNode
from lib.linked_list import DoublyLinkedList


class SortedDoublyLinkedList(DoublyLinkedList):

    # O(n)
    def insert(self, x):
        new_node = ListNode(x)
        prev = self.find_small_than(x)
        if (self.is_empty()
            or prev == self.__tail):
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
    def find_small_than(self, x):
        prev = self.__head
        while (prev.next is not None
               and prev.next.var < x):
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
