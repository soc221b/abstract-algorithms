import unittest
from random import random

from lib.heap import MinMaxHeap


class TestDoubledEndedHeap(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.Heap = None

    def test_min_max_heap(self):
        self.Heap = MinMaxHeap
        self._test_doubled_ended_heap()

    def _test_doubled_ended_heap(self):
        self._test_insert()
        self._test_delete_min()
        self._test_delete_max()
        self._test_min()
        self._test_max()
        self._test_is_empty()
        self._test_mixed()

    def _test_insert(self):
        heap = self.Heap()
        for i in range(0, 100):
            heap.insert(i)

    def _test_delete_min(self):
        # dependence: insert
        heap = self.Heap()
        t = []
        for _ in range(0, 100):
            r = random()
            t.append(r)
            heap.insert(r)

        t.sort()
        for i in range(0, 100):
            self.assertEqual(t[i], heap.delete_min())

    def _test_delete_max(self):
        # dependence: insert
        heap = self.Heap()
        t = []
        for _ in range(0, 100):
            r = random()
            t.append(r)
            heap.insert(r)

        t.sort()
        for i in reversed(range(0, 100)):
            self.assertEqual(t[i], heap.delete_max())

    def _test_max(self):
        # dependence: insert
        heap = self.Heap()
        for i in range(0, 100):
            heap.insert(i)
            self.assertEqual(heap.max(), i)

    def _test_min(self):
        # dependence: insert
        heap = self.Heap()
        for i in range(100, 0, -1):
            heap.insert(i)
            self.assertEqual(heap.min(), i)

    def _test_is_empty(self):
        # dependence: insert, delete_min, delete_max
        heap = self.Heap()
        self.assertTrue(heap.is_empty())

        t = []
        for _ in range(1, 100):
            while random() > 0.5:
                t.append(0)
                heap.insert(random())
                self.assertEqual(heap.is_empty(), len(t) == 0)
            while len(t) > 0 and random() > 0.5:
                heap.delete_min()
                del t[0]
                self.assertEqual(heap.is_empty(), len(t) == 0)
            while len(t) > 0 and random() > 0.5:
                heap.delete_max()
                del t[0]
                self.assertEqual(heap.is_empty(), len(t) == 0)

    def _test_mixed(self):
        for i in range(0, 100):
            heap = self.Heap()
            expect = []
            for j in range(0, 100):
                x = random()
                expect.append(x)
                heap.insert(x)
                expect.sort()
                while len(expect) > 0 and random() > 0.8:
                    if random() > 0.5:
                        del expect[0]
                        heap.delete_min()
                    else:
                        del expect[-1]
                        heap.delete_max()
                if len(expect) == 0:
                    assert heap.min() is None
                    assert heap.max() is None
                else:
                    assert heap.min() == expect[0]
                    assert heap.max() == expect[-1]
            if random() > 0.5:
                actual = []
                for _ in range(0, len(expect)):
                    actual.append(heap.delete_min())
                assert actual == expect
            else:
                actual = []
                for _ in range(0, len(expect)):
                    actual.append(heap.delete_max())
                actual = list(reversed(actual))
                assert actual == expect
