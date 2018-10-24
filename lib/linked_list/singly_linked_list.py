from lib.linked_list import SinglyListNode as ListNode


class SinglyLinkedList():

    def __init__(self):
        self.__head = ListNode(0)
        self.__tail = self.__head
        self.__len = 0

    # O(n)
    def search(self, x):
        curr = self.__head.next
        while curr is not None and curr.var != x:
            curr = curr.next
        return curr

    # O(1)
    def insert(self, x):
        new_node = ListNode(x)
        self.__tail.next = new_node
        self.__tail = new_node
        self.__len += 1
        return new_node

    # O(n)
    def delete(self, node):
        prev = self.__prev(node)
        prev.next = node.next
        self.__len -= 1

    # O(n)
    def minimumn(self):
        return self.__minmax(is_min=True)

    # O(n)
    def maximum(self):
        return self.__minmax(is_max=True)

    # O(n)
    def __minmax(self, *, is_min=False, is_max=False):
        if self.is_empty():
            raise KeyError
        else:
            curr = self.__head.next
            minmax = curr
            while curr.next is not None:
                curr = curr.next
                if is_min:
                    minmax = minmax if minmax.var < curr.var else curr
                elif is_max:
                    minmax = minmax if minmax.var > curr.var else curr
                else:
                    raise RuntimeError
            return minmax

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
    def successor(self, node):
        # no verification for node whether it in this list or not.
        return node.next

    # O(1)
    def __len__(self):
        return self.__len

    # O(1)
    def is_empty(self):
        return self.__len == 0
