class Heap():

    # O(n)
    def __init__(self, _list=[]):
        assert type(_list), list
        self._list = _list
        self.__init__heapify()

    def __init__heapify(self):
        for index in range(len(self._list) // 2, -1, -1):
            self.__heapify(index)

    def __heapify(self, index):
        left = index * 2
        right = left + 1
        upper_than_index = index
        if (self.__verify_range(left) and
           self._upper_than(left, upper_than_index)):
            upper_than_index = left
        if (self.__verify_range(right) and
           self._upper_than(right, upper_than_index)):
            upper_than_index = right

        if upper_than_index != index:
            self.__swap(index, upper_than_index)
            self.__heapify(upper_than_index)

    def __verify_range(self, index):
        return index < len(self._list)

    def _upper_than(self, index_a, index_b):
        raise NotImplementedError

    def __swap(self, a, b):
        self._list[a], self._list[b] = self._list[b], self._list[a]

    # O(log n)
    def insert(self, x):
        self._list.append(x)
        index = len(self._list) - 1
        while index > 0:
            parent = index // 2
            if self._upper_than(index, parent):
                self.__swap(index, parent)
                index = parent
            else:
                break

    # O(1)
    def peek(self):
        return self._list[0]

    # O(log n)
    def delete(self):
        peek = self.peek()

        self._list[0] = self._list[len(self._list) - 1]
        del self._list[len(self._list) - 1]

        self.__heapify(0)

        return peek

    def __str__(self):
        s = ""
        for elem in self._list:
            s += str(elem) + ', '
        return s
