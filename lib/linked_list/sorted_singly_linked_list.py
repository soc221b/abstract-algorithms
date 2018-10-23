from lib.linked_list import SinglyListNode as ListNode


class SortedSinglyLinkedList():

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

    def __init__(self):
        self.__head = ListNode(0)
        self.__tail = self.__head
        self.__len = 0

    # O(n)
    def search(self, x):
        curr = self.__head.next
        while curr is not None and curr.var != x:
            curr = self.successor(curr)
        return curr

    # O(n)
    def delete(self, node):
        prev = self.__prev(node)
        prev.next = node.next
        self.__len -= 1

    # O(1)
    def successor(self, node):
        # no verification for node whether it in this list or not.
        return node.next

    # O(n)
    def predecessor(self, node):
        prev = self.__prev(node)
        if prev is self.__head:
            return None
        else:
            return prev

    # O(n)
    def __prev(self, node):
        prev = self.__head
        while prev.next is not None and prev.next != node:
            prev = prev.next
        if prev.next is None:
            raise IndexError
        else:
            return prev

    # O(1)
    def __len__(self):
        return self.__len

    # O(1)
    def is_empty(self):
        return self.__len == 0
