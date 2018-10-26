import unittest
from random import random, shuffle

from lib.linked_list import (
    SinglyLinkedList,
    SortedSinglyLinkedList,
    DoublyLinkedList,
    SortedDoublyLinkedList
)


class TestLinkedList(unittest.TestCase):

    def test_signly_linked_list(self):
        self.__test_insert(SinglyLinkedList)
        self.__test_search(SinglyLinkedList)
        self.__test_delete_for_one_node(SinglyLinkedList)
        self.__test_delete_for_last_node_for_unsorted(SinglyLinkedList)
        self.__test_delete_general(SinglyLinkedList)
        self.__test_minimum_and_maximum(SinglyLinkedList)
        self.__test_predecessor_for_unsorted(SinglyLinkedList)
        self.__test_successor_for_unsorted(SinglyLinkedList)
        self.__test_is_empty(SinglyLinkedList)

    def test_sorted_signly_linked_list(self):
        self.__test_insert(SortedSinglyLinkedList)
        self.__test_search(SortedSinglyLinkedList)
        self.__test_delete_for_one_node(SortedSinglyLinkedList)
        self.__test_delete_for_last_node_for_sorted(SortedSinglyLinkedList)
        self.__test_delete_general(SortedSinglyLinkedList)
        self.__test_minimum_and_maximum(SortedSinglyLinkedList)
        self.__test_predecessor_for_sorted(SortedSinglyLinkedList)
        self.__test_successor_for_sorted(SortedSinglyLinkedList)
        self.__test_is_empty(SortedSinglyLinkedList)

    def test_doubly_linked_list(self):
        self.__test_insert(DoublyLinkedList)
        self.__test_search(DoublyLinkedList)
        self.__test_delete_for_one_node(DoublyLinkedList)
        self.__test_delete_for_last_node_for_unsorted(DoublyLinkedList)
        self.__test_delete_general(DoublyLinkedList)
        self.__test_minimum_and_maximum(DoublyLinkedList)
        self.__test_predecessor_for_unsorted(DoublyLinkedList)
        self.__test_successor_for_unsorted(DoublyLinkedList)
        self.__test_is_empty(DoublyLinkedList)

    def test_sorted_doubly_linked_list(self):
        self.__test_insert(SortedDoublyLinkedList)
        self.__test_search(SortedDoublyLinkedList)
        self.__test_delete_for_one_node(SortedDoublyLinkedList)
        self.__test_delete_for_last_node_for_sorted(SortedDoublyLinkedList)
        self.__test_delete_general(SortedDoublyLinkedList)
        self.__test_minimum_and_maximum(SortedDoublyLinkedList)
        self.__test_predecessor_for_sorted(SortedDoublyLinkedList)
        self.__test_successor_for_sorted(SortedDoublyLinkedList)
        self.__test_is_empty(SortedDoublyLinkedList)

    def __test_insert(self, linked_list):
        for _ in range(0, 100):
            ll = linked_list()
            count = 0
            for _ in range(0, 100):
                count += 1
                r = random()
                node = ll.insert(r)
                self.assertEqual(node.var, r)
                self.assertEqual(len(ll), count)

    def __test_search(self, linked_list):
        # dependent methods: insert
        ll = linked_list()
        for _ in range(0, 100):
            r = random()
            ll.insert(r)
            self.assertIsNot(ll.search(r), None)

    def __test_delete_for_one_node(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        for _ in range(0, 100):
            node = ll.search(self.__insert(ll))
            try:
                ll.delete(node)
            except Exception:
                self.fail()

    def __test_delete_for_last_node_for_unsorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        rs = []
        rs.append(self.__insert(ll))
        for _ in range(0, 1000):
            rs = self.__delete_multiple_times_for_last(ll, rs)
            rs.extend(self.__insert_multiple_times(ll))

    def __test_delete_for_last_node_for_sorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        rs = []
        rs.append(self.__insert(ll))
        for _ in range(0, 1000):
            rs = self.__delete_multiple_times_for_last(ll, rs)
            rs.extend(self.__insert_multiple_times(ll))
            rs.sort()

    def __test_delete_general(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        rs = []
        for _ in range(0, 1000):
            rs.extend(self.__insert_multiple_times(ll))
            shuffle(rs)
            rs = self.__delete_multiple_times_for_last(ll, rs)

    def __test_minimum_and_maximum(self, linked_list):
        # dependent methods: insert
        for _ in range(0, 100):
            ll = linked_list()
            sorted_rs = []
            r = random()
            for _ in range(0, 100):
                sorted_rs.append(r)
                r += random()
            random_rs = sorted_rs[:]
            shuffle(random_rs)
            for n in random_rs:
                ll.insert(n)
            self.assertEqual(ll.minimum().var, sorted_rs[0])
            self.assertEqual(ll.maximum().var, sorted_rs[-1])

    def __test_predecessor_for_unsorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        random_rs = [random() for _ in range(0, 300)]
        for n in random_rs:
            ll.insert(n)

        prev = ll.search(random_rs[0])
        self.assertIs(ll.predecessor(prev), None)
        for n in random_rs[1:]:
            curr = ll.search(n)
            self.assertEqual(ll.predecessor(curr), prev)
            prev = curr

    def __test_predecessor_for_sorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        sorted_rs = [n for n in range(0, 300)]
        random_rs = sorted_rs[:]
        shuffle(random_rs)
        for n in random_rs:
            ll.insert(n)

        self.assertIs(ll.predecessor(ll.search(sorted_rs[0])), None)
        for index in range(0, len(sorted_rs) - 1):
            prev = ll.search(sorted_rs[index])
            curr = ll.search(sorted_rs[index + 1])
            self.assertEqual(ll.predecessor(curr), prev)

    def __test_successor_for_unsorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        random_rs = [random() for _ in range(0, 300)]
        for n in random_rs:
            ll.insert(n)

        next = ll.search(random_rs[-1])
        self.assertIs(ll.successor(next), None)
        for n in random_rs[::-1][1:]:
            curr = ll.search(n)
            self.assertEqual(ll.successor(curr), next)
            next = curr

    def __test_successor_for_sorted(self, linked_list):
        # dependent methods: insert, search
        ll = linked_list()
        sorted_rs = [n for n in range(0, 300)]
        random_rs = sorted_rs[:]
        shuffle(random_rs)
        for n in random_rs:
            ll.insert(n)

        self.assertIs(ll.successor(ll.search(sorted_rs[-1])), None)
        for index in range(0, len(sorted_rs) - 1):
            curr = ll.search(sorted_rs[index])
            next = ll.search(sorted_rs[index + 1])
            self.assertEqual(ll.successor(curr), next)

    def __test_is_empty(self, linked_list):
        # dependent methods: insert, search, delete
        ll = linked_list()
        rs = []
        for _ in range(0, 100):
            self.assertEqual(len(rs) == 0, ll.is_empty())
            rs.extend(self.__insert_multiple_times(ll))
            rs = self.__delete_multiple_times_for_last(ll, rs)

    def __insert(self, ll):
        r = random()
        ll.insert(r)
        self.assertIsNot(ll.search(r), None)
        return r

    def __insert_multiple_times(self, ll):
        rs = []
        while True:
            rs.append(self.__insert(ll))
            if random() > 0.7:
                break
        return rs

    def __delete_for_last(self, ll, rs):
        if len(rs) > 0:
            node = ll.search(rs[-1])
            ll.delete(node)
            del rs[-1]
        return rs

    def __delete_multiple_times_for_last(self, ll, rs):
        while len(rs) > 0:
            rs = self.__delete_for_last(ll, rs)
            if random() > 0.7:
                break
        return rs
