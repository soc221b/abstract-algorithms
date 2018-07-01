import unittest
from random import random, randint
from lib.queue import queue
from lib.overriden_built_in import reversed


def get_random_values(n=randint(10, 20)):
    res = []
    for _ in range(n):
        res.append(random())
    return res


class TestQueue(unittest.TestCase):

    def test_queue_init(self):
        que = queue()
        self.assertEqual(que.size(), 0)
        self.assertEqual(que.is_empty(), True)
        with self.assertRaises(IndexError):
            que.pop()
        with self.assertRaises(IndexError):
            que.peek()

    def test_queue_push(self):
        que = queue()
        random_values = get_random_values()
        for v in random_values:
            que.push(v)
            self.assertEqual(que.is_empty(), False)
            self.assertEqual(que.peek(), v)
            self.assertEqual(que.pop(), v)

    def test_queue_pop(self):
        que = queue()
        random_values = get_random_values()
        for v in random_values:
            que.push(v)
        for v in random_values:
            que.pop()
        self.assertEqual(que.is_empty(), True)
        with self.assertRaises(IndexError):
            que.pop()
        with self.assertRaises(IndexError):
            que.peek()

    def test_queue_peek(self):
        que = queue()
        random_values = get_random_values()
        for v in random_values:
            que.push(v)
        for v in random_values:
            self.assertEqual(que.peek(), v)
            que.pop()

    def test_queue_is_empty(self):
        que = queue()
        random_values = get_random_values()
        self.assertEqual(que.is_empty(), True)
        for v in random_values:
            que.push(v)
            self.assertEqual(que.is_empty(), False)
        for v in random_values:
            self.assertEqual(que.is_empty(), False)
            que.pop()
        self.assertEqual(que.is_empty(), True)

    def test_queue_reverse(self):
        que = queue()
        random_values = get_random_values()
        for v in random_values:
            que.push(v)
        que.reverse()
        for v in random_values[::-1]:
            self.assertEqual(que.peek(), v)
            que.pop()

    def test_queue_size(self):
        que = queue()
        random_values = get_random_values()
        for i, v in enumerate(random_values):
            que.push(v)
            self.assertEqual(que.size(), i + 1)
        for i in range(len(random_values)):
            que.pop()
            self.assertEqual(que.size(), len(random_values) - i - 1)

    def test_queue_copy(self):
        que = queue()
        random_values = get_random_values()
        for v in random_values:
            que.push(v)
        copied_que = que.copy()
        for v in random_values:
            self.assertEqual(copied_que.peek(), v)
            copied_que.pop()
        self.assertEqual(que.size(), len(random_values))


class TestQueueHelper(unittest.TestCase):

    def test_queue_reversed(self):
        que = queue()
        random_values = get_random_values()
        for v in random_values:
            que.push(v)
        reversed_queue = reversed(que)
        for v in random_values[::-1]:
            self.assertEqual(reversed_queue.peek(), v)
            reversed_queue.pop()
        self.assertEqual(que.size(), len(random_values))

    def test_queue_reversed_with_override(self):
        self.assertEqual(list(reversed([123, 456])), [456, 123])

        que = queue()
        random_values = get_random_values()
        for v in random_values:
            que.push(v)
        reversed_queue = reversed(que)
        for v in random_values[::-1]:
            self.assertEqual(reversed_queue.peek(), v)
            reversed_queue.pop()
        self.assertEqual(que.size(), len(random_values))

        self.assertEqual(list(reversed([123, 456])), [456, 123])
