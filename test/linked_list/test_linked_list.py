import unittest
from random import random, randint, shuffle

from lib.linked_list import (
    SinglyLinkedList,
    SortedSinglyLinkedList,
    DoublyLinkedList,
    SortedDoublyLinkedList
)


class TestLinkedList(unittest.TestCase):

    def test_signly_linked_list(self):
        self.__test_unsorted(SinglyLinkedList)
        self.__test_general(SinglyLinkedList)

    def test_sorted_signly_linked_list(self):
        self.__test_sorted(SortedSinglyLinkedList)
        self.__test_general(SortedSinglyLinkedList)

    def test_doubly_linked_list(self):
        self.__test_unsorted(DoublyLinkedList)
        self.__test_general(DoublyLinkedList)

    def test_sorted_doubly_linked_list(self):
        self.__test_sorted(SortedDoublyLinkedList)
        self.__test_general(SortedDoublyLinkedList)

    def __test_unsorted(self, linked_list):
        self.__test_predecessor_for_unsorted(linked_list())
        self.__test_successor_for_unsorted(linked_list())

    def __test_sorted(self, linked_list):
        self.__test_predecessor_for_sorted(linked_list())
        self.__test_successor_for_sorted(linked_list())

    def __test_general(self, linked_list):
        self.__test_insert(linked_list())
        self.__test_delete(linked_list())
        self.__test_is_empty(linked_list())
        self.__test_minimum(linked_list())
        self.__test_maximum(linked_list())

    def __test_insert(self, ll):
        count = 0
        for _ in range(0, 1000):
            count += 1
            r = random()
            node = ll.insert(r)
            self.assertEqual(node.var, r)
            self.assertEqual(len(ll), count)

    def __test_delete(self, ll):
        for _ in range(0, 1000):
            node = ll.insert(random())
            try:
                ll.delete(node)
            except Exception:
                self.fail()

    def __test_predecessor_for_unsorted(self, ll):
        random_ns = [random() for _ in range(0, 300)]
        for n in random_ns:
            ll.insert(n)

        prev = ll.search(random_ns[0])
        self.assertEqual(ll.predecessor(prev), None)
        for n in random_ns[1:]:
            curr = ll.search(n)
            self.assertEqual(ll.predecessor(curr), prev)
            prev = curr

    def __test_predecessor_for_sorted(self, ll):
        ns = [n for n in range(0, 300)]
        random_ns = ns[:]
        shuffle(random_ns)
        for n in random_ns:
            ll.insert(n)

        self.assertEqual(ll.predecessor(ll.search(ns[0])), None)
        for index in range(0, len(ns) - 1):
            prev = ll.search(ns[index])
            curr = ll.search(ns[index + 1])
            self.assertEqual(ll.predecessor(curr), prev)

    def __test_successor_for_unsorted(self, ll):
        random_ns = [random() for _ in range(0, 300)]
        for n in random_ns:
            ll.insert(n)

        next = ll.search(random_ns[-1])
        self.assertEqual(ll.successor(next), None)
        for n in random_ns[::-1][1:]:
            curr = ll.search(n)
            self.assertEqual(ll.successor(curr), next)
            next = curr

    def __test_successor_for_sorted(self, ll):
        ns = [n for n in range(0, 300)]
        random_ns = ns[:]
        shuffle(random_ns)
        for n in random_ns:
            ll.insert(n)

        self.assertEqual(ll.successor(ll.search(ns[-1])), None)
        for index in range(0, len(ns) - 1):
            curr = ll.search(ns[index])
            next = ll.search(ns[index + 1])
            self.assertEqual(ll.successor(curr), next)

    def __test_is_empty(self, ll):
        ns = []
        for _ in range(0, 100):
            self.assertEqual(len(ns) == 0, ll.is_empty())
            if random() > 0.6:
                r = random()
                ll.insert(r)
                ns.append(r)
            if random() > 0.4 and len(ns) != 0:
                ll.delete(ll.search(ns[0]))
                del ns[0]

    def __test_minimum(self, ll):
        for _ in range(0, 100):
            sorted_ns = [n for n in range(0, 300)]
            random_ns = sorted_ns[:]
            shuffle(random_ns)
            for n in random_ns:
                ll.insert(n)
            self.assertEqual(ll.minimum().var, sorted_ns[0])

    def __test_maximum(self, ll):
        for _ in range(0, 100):
            sorted_ns = [n for n in range(0, 300)]
            random_ns = sorted_ns[:]
            shuffle(random_ns)
            for n in random_ns:
                ll.insert(n)
            self.assertEqual(ll.maximum().var, sorted_ns[-1])
