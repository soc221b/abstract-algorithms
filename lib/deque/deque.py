class Deque():

    def __init__(self):
        self.__array = []

    def push_front(self, x):
        self.__array.insert(0, x)

    def push_back(self, x):
        self.__array.append(x)

    def pop_front(self):
        front = self.front()
        del self.__array[0]
        return front

    def pop_back(self):
        back = self.back()
        del self.__array[-1]
        return back

    def front(self):
        return self.__array[0]

    def back(self):
        return self.__array[-1]

    def is_empty(self):
        return len(self.__array) == 0

    def reverse(self):
        self.__array = self.__array[::-1]

    def size(self):
        return len(self.__array)

    def copy(self):
        copied_deque = Deque()
        for v in self.__array:
            copied_deque.push_back(v)
        return copied_deque


def reversed_deque(deq):
    copied_deque = deq.copy()
    copied_deque.reverse()
    return copied_deque
