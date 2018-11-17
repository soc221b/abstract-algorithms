from lib.heap import Heap


class MaxHeap(Heap):

    def _upper_than(self, index_a, index_b):
        return self._list[index_a] > self._list[index_b]
