import unittest
from random import random, randint

from lib.deque import Deque
from lib.overriden_built_in import reversed


def get_random_values(n=randint(10, 20)):
    res = []
    for _ in range(n):
        res.append(random())
    return res


class TestDeque(unittest.TestCase):

    def test_deque_init(self):
        deq = Deque()
        self.assertEqual(deq.size(), 0)
        self.assertEqual(deq.is_empty(), True)
        with self.assertRaises(IndexError):
            deq.pop_front()
        with self.assertRaises(IndexError):
            deq.pop_back()
        with self.assertRaises(IndexError):
            deq.front()
        with self.assertRaises(IndexError):
            deq.back()

    def test_deque_push_front(self):
        deq = Deque()
        random_values = get_random_values()
        for v in random_values:
            deq.push_front(v)
            self.assertEqual(deq.is_empty(), False)
            self.assertEqual(deq.front(), v)
            self.assertEqual(deq.pop_front(), v)

    def test_deque_push_back(self):
        deq = Deque()
        random_values = get_random_values()
        for v in random_values:
            deq.push_back(v)
            self.assertEqual(deq.is_empty(), False)
            self.assertEqual(deq.back(), v)
            self.assertEqual(deq.pop_back(), v)

    def test_deque_pop_front(self):
        deq = Deque()
        random_values = get_random_values()
        for v in random_values:
            deq.push_front(v)
        for v in random_values:
            deq.pop_front()
        self.assertEqual(deq.is_empty(), True)
        with self.assertRaises(IndexError):
            deq.pop_front()
        with self.assertRaises(IndexError):
            deq.front()

    def test_deque_pop_back(self):
        deq = Deque()
        random_values = get_random_values()
        for v in random_values:
            deq.push_back(v)
        for v in random_values:
            deq.pop_back()
        self.assertEqual(deq.is_empty(), True)
        with self.assertRaises(IndexError):
            deq.pop_back()
        with self.assertRaises(IndexError):
            deq.back()

    def test_deque_front(self):
        deq = Deque()
        random_values = get_random_values()
        for v in random_values:
            deq.push_back(v)
        for v in random_values:
            self.assertEqual(deq.front(), v)
            deq.pop_front()

    def test_deque_back(self):
        deq = Deque()
        random_values = get_random_values()
        for v in random_values:
            deq.push_front(v)
        for v in random_values:
            self.assertEqual(deq.back(), v)
            deq.pop_back()

    def test_deque_is_empty(self):
        deq = Deque()
        random_values = get_random_values()
        self.assertEqual(deq.is_empty(), True)
        for v in random_values:
            deq.push_back(v)
            self.assertEqual(deq.is_empty(), False)
        for v in random_values:
            self.assertEqual(deq.is_empty(), False)
            deq.pop_back()
        self.assertEqual(deq.is_empty(), True)

    def test_deque_reverse(self):
        deq = Deque()
        # [1, 2, 3]
        random_values = get_random_values()
        # [1, 2, 3]
        for v in random_values:
            deq.push_back(v)
        deq.reverse()
        # [3, 2, 1]
        for v in random_values:
            self.assertEqual(deq.back(), v)
            deq.pop_back()

    def test_deque_size(self):
        deq = Deque()
        random_values = get_random_values()
        for i, v in enumerate(random_values):
            deq.push_back(v)
            self.assertEqual(deq.size(), i + 1)
        for i in range(len(random_values)):
            deq.pop_back()
            self.assertEqual(deq.size(), len(random_values) - i - 1)

    def test_deque_copy(self):
        deq = Deque()
        # [1, 2, 3]
        random_values = get_random_values()
        # [1, 2, 3]
        for v in random_values:
            deq.push_back(v)
        copied_deq = deq.copy()
        # [1, 2, 3]
        for v in random_values:
            self.assertEqual(copied_deq.front(), v)
            copied_deq.pop_front()
        self.assertEqual(deq.size(), len(random_values))


class TestDequeHelper(unittest.TestCase):

    def test_deque_reversed(self):
        deq = Deque()
        # [1, 2, 3]
        random_values = get_random_values()
        # [1, 2, 3]
        for v in random_values:
            deq.push_back(v)
        reversed_deque = reversed(deq)
        # [3, 2, 1]
        for v in random_values:
            self.assertEqual(reversed_deque.back(), v)
            reversed_deque.pop_back()
        self.assertEqual(deq.size(), len(random_values))

    def test_deque_reversed_with_override(self):
        self.assertEqual(list(reversed([123, 456])), [456, 123])

        deq = Deque()
        # [1, 2, 3]
        random_values = get_random_values()
        # [1, 2, 3]
        for v in random_values:
            deq.push_back(v)
        reversed_deque = reversed(deq)
        # [3, 2, 1]
        for v in random_values:
            self.assertEqual(reversed_deque.back(), v)
            reversed_deque.pop_back()
        self.assertEqual(deq.size(), len(random_values))

        self.assertEqual(list(reversed([123, 456])), [456, 123])
