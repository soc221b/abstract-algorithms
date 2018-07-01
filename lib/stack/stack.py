class stack():

    def __init__(self):
        self.__array = []

    def push(self, x):
        self.__array.append(x)

    def pop(self):
        peek = self.peek()
        del self.__array[-1]
        return peek

    def peek(self):
        return self.__array[-1]

    def is_empty(self):
        return len(self.__array) == 0

    def reverse(self):
        self.__array = self.__array[::-1]

    def size(self):
        return len(self.__array)

    def copy(self):
        copied_stack = stack()
        for v in self.__array:
            copied_stack.push(v)
        return copied_stack


def reversed_stack(stk):
    copied_stack = stk.copy()
    copied_stack.reverse()
    return copied_stack
