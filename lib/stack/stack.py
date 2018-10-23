from lib.linked_list import SinglyListNode as ListNode


class Stack():

    def __init__(self):
        self.__peek_node = None
        self.__len = 0

    # O(1)
    def push(self, x):
        new_peek_node = ListNode(x)
        new_peek_node.next = self.__peek_node
        self.__peek_node = new_peek_node
        self.__len += 1

    # O(1)
    def pop(self):
        peek_var = self.peek()
        self.__peek_node = self.__peek_node.next
        self.__len -= 1
        return peek_var

    # O(1)
    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.__peek_node.var

    # O(1)
    def is_empty(self):
        return self.__len == 0

    # O(n)
    def reverse(self):
        if not self.is_empty():
            peek_node = self.__peek_node
            next_node = self.__peek_node.next
            peek_node.next = None  # peek is last elem
            while next_node is not None:
                temp = next_node.next
                next_node.next = peek_node
                peek_node = next_node
                next_node = temp

            self.__peek_node = peek_node

    # O(1)
    def size(self):
        return self.__len

    # O(n)
    def copy(self):
        copied = Stack()
        peek_node = self.__peek_node
        while peek_node is not None:
            copied_var = peek_node.var
            peek_node = peek_node.next
            copied.push(copied_var)

        copied.reverse()

        return copied


# O(n)
def reversed_stack(stk):
    copied_stack = stk.copy()
    copied_stack.reverse()
    return copied_stack
