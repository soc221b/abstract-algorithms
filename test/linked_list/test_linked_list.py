import unittest
from random import random, randint, shuffle

from lib.linked_list import (
    SinglyLinkedList,
    SortedSinglyLinkedList,
    DoublyLinkedList,
    SortedDoublyLinkedList
)

sorted_linked_lists = [
    SortedSinglyLinkedList,
    SortedDoublyLinkedList
]

unsorted_linked_lists = [
    SinglyLinkedList,
    DoublyLinkedList
]

linked_lists = sorted_linked_lists + unsorted_linked_lists


class TestLinkedList(unittest.TestCase):

    def test_insert(self):
        for linked_list in linked_lists:
            ll = linked_list()
            i = 0
            for r in range(0, 1000):
                i += 1
                r = randint(0, 300)
                node = ll.insert(r)
                self.assertEqual(node.var, r)
                self.assertEqual(len(ll), i)

    def test_delete(self):
        for linked_list in linked_lists:
            ll = linked_list()
            for r in range(0, 1000):
                r = randint(0, 300)
                node = ll.insert(r)
                try:
                    ll.delete(node)
                except Exception:
                    self.fail()

    def test_predecessor_for_unsorted(self):
        for linked_list in linked_lists:
            ll = linked_list()
            random_ns = [random() for _ in range(0, 300)]
            for n in random_ns:
                ll.insert(n)

            prev = ll.search(random_ns[0])
            self.assertEqual(ll.predecessor(prev), None)
            for n in random_ns[1:]:
                curr = ll.search(n)
                self.assertEqual(ll.predecessor(curr), prev)
                prev = curr

    def test_predecessor_for_sorted(self):
        for linked_list in linked_lists:
            ll = linked_list()
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

    def test_successor_for_unsorted(self):
        for linked_list in unsorted_linked_lists:
            ll = linked_list()
            random_ns = [random() for _ in range(0, 300)]
            for n in random_ns:
                ll.insert(n)

            next = ll.search(random_ns[-1])
            self.assertEqual(ll.successor(next), None)
            for n in random_ns[::-1][1:]:
                curr = ll.search(n)
                self.assertEqual(ll.successor(curr), next)
                next = curr

    def test_successor_for_sorted(self):
        for linked_list in sorted_linked_lists:
            ll = linked_list()
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

    def test_is_empty(self):
        for linked_list in linked_lists:
            ll = linked_list()
            ns = []
            for _ in range(0, 100):
                self.assertEqual(len(ns) == 0, ll.is_empty())
                if random > 0.6:
                    r = random()
                    ll.insert(r)
                    ns.append(r)
                if random > 0.4 and len(ns) != 0:
                    ll.delete(ll.search(ns[0]))
                    del ns[0]

    def test_minimumn(self):
        for linked_list in linked_lists:
            ll = linked_list()
            for _ in range(0, 100):
                random_ns = [random() for _ in range(0, 20)]
                sorted_ns = sorted(random_ns)
                for n in random_ns:
                    ll.insert(n)
                self.assertEqual(ll.minimum(), sorted_ns[0])

    def test_maximum(self):
        for linked_list in linked_lists:
            ll = linked_list()
            for _ in range(0, 100):
                random_ns = [random() for _ in range(0, 20)]
                sorted_ns = sorted(random_ns)
                for n in random_ns:
                    ll.insert(n)
                self.assertEqual(ll.maximum(), sorted_ns[-1])
