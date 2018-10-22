class ListNode():

    def __init__(self, var, next=None):
        self.__var = var
        self.__next = next

    @property
    def var(self):
        return self.__var

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class Stack():

    def __init__(self):
        self.__peek = None
        self.__len = 0

    # O(1)
    def push(self, x):
        elem = ListNode(x)
        self.__len += 1
        if self.is_empty:
            self.__peek = elem
        else:
            elem.next = self.__peek
            self.__peek = elem

    # O(1)
    def pop(self):
        peek = self.peek()
        self.__len -= 1
        self.__peek = self.__peek.next
        return peek

    # O(1)
    def peek(self):
        return self.__peek

    # O(1)
    def is_empty(self):
        return self.__len == 0

    # O(n)
    def reverse(self):
        if not self.is_empty():
            peek = self.__peek
            next = self.__peek.next
            peek.next = None  # peek is last elem
            while next is not None:
                temp = next.next
                next.next = peek
                peek = next
                next = temp

            self.__peek = peek

    # O(1)
    def size(self):
        return self.__len

    # O(n)
    def copy(self):
        copied = Stack()
        peek = self.__peek
        while peek is not None:
            next = peek.next
            copied.push(ListNode(peek.var))
            peek = next

        copied.reverse()

        return copied

# O(n)
def reversed_stack(stk):
    copied_stack = stk.copy()
    copied_stack.reverse()
    return copied_stack
