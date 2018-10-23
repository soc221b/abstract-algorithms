from lib.linked_list import SinglyListNode as ListNode


class SinglyLinkedList():

    def __init__(self):
        self.__head = ListNode(0)
        self.__tail = self.__head
        self.__len = 0
        raise NotImplementedError  # no tested

    # O(1)
    def insert(self, x):
        new_node = ListNode(x)
        self.__tail.next = new_elem
        self.__tail = new_elem
        self.__len += 1
        return new_node

    # O(n)
    def delete(self, node):
        predecessor = self.predecessor(node)
        if predecessor is None:  # the node is first node
            self.__head = node.next
        else:
            predecessor.next = node.next
        self.__len -= 1

    # O(1)
    def successor(self, node):
        return node.next

    # O(n)
    def predecessor(self, node):
        curr = self.__head
        while curr is not None and curr.next != node:
            curr = curr.next
        if curr is not None:
            if curr is self.__head:
                return None  # if the node is first node
            else:
                return curr
        else:
            raise KeyError

    # O(1)
    def size(self):
        return self.__len

    # O(1)
    def is_empty(self):
        return self.__len == 0

    # O(n)
    def minimumn(self):
        return self.__minmax()

    # O(n)
    def maximum(self):
        return self.__minmax(False)

    # O(n)
    def __minmax(self, is_min=True):
        if self.is_empty():
            raise KeyError
        else:
            curr = self.__head.next
            maximum = curr
            while curr.next is not None:
                curr = curr.next
                if is_min:
                    minimum = minimum if minimum.var < curr.var else curr
                else:
                    maximum = maximum if maximum.var > curr.var else curr
            return maximum
