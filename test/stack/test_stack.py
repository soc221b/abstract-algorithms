import unittest
from random import random, randint
from lib.stack import stack
from lib.overriden_built_in import reversed


def get_random_values(n=randint(10, 20)):
    res = []
    for _ in range(n):
        res.append(random())
    return res


class TestStack(unittest.TestCase):

    def test_stack_init(self):
        stk = stack()
        self.assertEqual(stk.size(), 0)
        self.assertEqual(stk.is_empty(), True)
        with self.assertRaises(IndexError):
            stk.pop()
        with self.assertRaises(IndexError):
            stk.peek()

    def test_stack_push(self):
        stk = stack()
        random_values = get_random_values()
        for v in random_values:
            stk.push(v)
            self.assertEqual(stk.is_empty(), False)
            self.assertEqual(stk.peek(), v)
            self.assertEqual(stk.pop(), v)

    def test_stack_pop(self):
        stk = stack()
        random_values = get_random_values()
        for v in random_values:
            stk.push(v)
        for v in random_values[::-1]:
            stk.pop()
        self.assertEqual(stk.is_empty(), True)
        with self.assertRaises(IndexError):
            stk.pop()
        with self.assertRaises(IndexError):
            stk.peek()

    def test_stack_peek(self):
        stk = stack()
        random_values = get_random_values()
        for v in random_values:
            stk.push(v)
        for v in random_values[::-1]:
            self.assertEqual(stk.peek(), v)
            stk.pop()

    def test_stack_is_empty(self):
        stk = stack()
        random_values = get_random_values()
        self.assertEqual(stk.is_empty(), True)
        for v in random_values:
            stk.push(v)
            self.assertEqual(stk.is_empty(), False)
        for v in random_values[::-1]:
            self.assertEqual(stk.is_empty(), False)
            stk.pop()
        self.assertEqual(stk.is_empty(), True)

    def test_stack_reverse(self):
        stk = stack()
        random_values = get_random_values()
        for v in random_values:
            stk.push(v)
        stk.reverse()
        for v in random_values:
            self.assertEqual(stk.peek(), v)
            stk.pop()

    def test_stack_size(self):
        stk = stack()
        random_values = get_random_values()
        for i, v in enumerate(random_values):
            stk.push(v)
            self.assertEqual(stk.size(), i + 1)
        for i in range(len(random_values)):
            stk.pop()
            self.assertEqual(stk.size(), len(random_values) - i - 1)

    def test_stack_copy(self):
        stk = stack()
        random_values = get_random_values()
        for v in random_values:
            stk.push(v)
        copied_stk = stk.copy()
        for v in random_values[::-1]:
            self.assertEqual(copied_stk.peek(), v)
            copied_stk.pop()
        self.assertEqual(stk.size(), len(random_values))


class TestStackHelper(unittest.TestCase):

    def test_stack_reversed(self):
        stk = stack()
        random_values = get_random_values()
        for v in random_values:
            stk.push(v)
        reversed_stk = reversed(stk)
        for v in random_values:
            self.assertEqual(reversed_stk.peek(), v)
            reversed_stk.pop()
        self.assertEqual(stk.size(), len(random_values))

    def test_stack_reversed_with_override(self):
        self.assertEqual(list(reversed([123, 456])), [456, 123])

        stk = stack()
        random_values = get_random_values()
        for v in random_values:
            stk.push(v)
        reversed_stk = reversed(stk)
        for v in random_values:
            self.assertEqual(reversed_stk.peek(), v)
            reversed_stk.pop()
        self.assertEqual(stk.size(), len(random_values))

        self.assertEqual(list(reversed([123, 456])), [456, 123])
