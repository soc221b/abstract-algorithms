from lib.linked_list import SinglyListNode as ListNode
from lib.linked_list import SinglyLinkedList

class SortedSinglyLinkedList(SinglyLinkedList):

    def __init__(self):
        super().__init__()
        raise NotImplementedError  # no tested

    # O(n)
    def insert(self, x):
        new_node = ListNode(x)
        if self.is_empty():
            self.__head.next = new_node
            self.__tail = new_node
        else:
            curr = self.__head
            while curr is not None and curr.next.var < x:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        self.__len += 1
        return new_node

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
