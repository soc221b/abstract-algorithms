class queue():

    def __init__(self):
        self.__array = []

    def push(self, x):
        self.__array.append(x)

    def pop(self):
        peek = self.peek()
        del self.__array[0]
        return peek

    def peek(self):
        return self.__array[0]

    def is_empty(self):
        return len(self.__array) == 0

    def reverse(self):
        self.__array = self.__array[::-1]

    def size(self):
        return len(self.__array)

    def copy(self):
        copied_queue = queue()
        for v in self.__array:
            copied_queue.push(v)
        return copied_queue


def reversed_queue(que):
    copied_queue = que.copy()
    copied_queue.reverse()
    return copied_queue
