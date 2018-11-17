from random import randint, random
from math import log, ceil


class MinMaxHeap():

    def __init__(self, _list=[]):
        # no test
        raise NotImplementedError
        self._list = []
        for elem in _list:
            self.insert(elem)

    def insert(self, x):
        self._list.append(x)
        latest_index = len(self._list) - 1
        if self.__is_at_min_level(latest_index):
            self.__update_min_bottom_up(latest_index)
        else:
            self.__update_max_bottom_up(latest_index)

    def __update_min_bottom_up(self, index):
        if index <= 0:
            return
        parent = self.__get_parent(index)
        grand_parent = self.__get_grand_parent(index)
        if self.__is_greater_than(index, parent):
            self.__swap(index, parent)
            self.__update_max_bottom_up(parent)
        elif (grand_parent >= 0 and
              self.__is_smaller_than(index, grand_parent)):
            self.__swap(index, grand_parent)
            self.__update_min_bottom_up(grand_parent)

    def __update_max_bottom_up(self, index):
        if index <= 0:
            return
        parent = self.__get_parent(index)
        grand_parent = self.__get_grand_parent(index)
        if self.__is_smaller_than(index, parent):
            self.__swap(index, parent)
            self.__update_min_bottom_up(parent)
        elif (grand_parent >= 0 and
              self.__is_greater_than(index, grand_parent)):
            self.__swap(index, grand_parent)
            self.__update_max_bottom_up(grand_parent)

    def delete_min(self):
        _min = self.min()
        latest_index = len(self._list) - 1
        self._list[0] = self._list[latest_index]
        del self._list[latest_index]

        self.__update_min_top_down(0)

        return _min

    def __update_min_top_down(self, index):
        child = self.__get_leftest_child(index)
        grand_child = self.__get_leftest_grand_child(index)
        if self.__is_in_valid_range(grand_child):
            min_index = self.__find_smallest_for_grand_childs(index)
            if min_index != index:
                self.__swap(min_index, index)
                self.__update_min_top_down(min_index)

        elif self.__is_in_valid_range(child):
            min_index = self.__find_smallest_for_childs(index)
            if min_index != index:
                self.__swap(min_index, index)

    def delete_max(self):
        max_at = self.__max_at()
        _max = self._list[max_at]
        latest_index = len(self._list) - 1
        self._list[max_at] = self._list[latest_index]
        del self._list[latest_index]

        self.__update_max_top_down(max_at)

        return _max

    def __update_max_top_down(self, index):
        child = self.__get_leftest_child(index)
        grand_child = self.__get_leftest_grand_child(index)
        if self.__is_in_valid_range(grand_child):
            max_index = self.__find_greatest_for_grand_childs(index)
            if max_index != index:
                self.__swap(max_index, index)
                self.__update_max_top_down(max_index)

        elif self.__is_in_valid_range(child):
            max_index = self.__find_greatest_for_childs(index)
            if max_index != index:
                self.__swap(max_index, index)

    def __find_smallest_for_grand_childs(self, index):
        min_index = index
        ll = self.__get_leftest_grand_child(index)
        lr = ll + 1
        rl = ll + 2
        rr = ll + 3
        if self.__is_greater_than(min_index, ll):
            min_index = ll
        if (self.__is_in_valid_range(lr) and
           self.__is_greater_than(min_index, lr)):
            min_index = lr
            if (self.__is_in_valid_range(rl) and
               self.__is_greater_than(min_index, rl)):
                min_index = rl
                if (self.__is_in_valid_range(rr) and
                   self.__is_greater_than(min_index, rr)):
                    min_index = rr
        return min_index

    def __find_smallest_for_childs(self, index):
        min_index = index
        l = self.__get_leftest_child(index)
        r = l + 1
        if self.__is_greater_than(min_index, l):
            min_index = l
        if (self.__is_in_valid_range(r) and
           self.__is_greater_than(min_index, r)):
            min_index = r
        return min_index

    def __find_greatest_for_grand_childs(self, index):
        max_index = index
        ll = self.__get_leftest_grand_child(index)
        lr = ll + 1
        rl = ll + 2
        rr = ll + 3
        if self.__is_smaller_than(max_index, ll):
            max_index = ll
        if (self.__is_in_valid_range(lr) and
           self.__is_smaller_than(max_index, lr)):
            max_index = lr
            if (self.__is_in_valid_range(rl) and
               self.__is_smaller_than(max_index, rl)):
                max_index = rl
                if (self.__is_in_valid_range(rr) and
                   self.__is_smaller_than(max_index, rr)):
                    max_index = rr
        return max_index

    def __find_greatest_for_childs(self, index):
        max_index = index
        l = self.__get_leftest_child(index)
        r = l + 1
        if self.__is_smaller_than(max_index, l):
            max_index = l
        if (self.__is_in_valid_range(r) and
           self.__is_smaller_than(max_index, r)):
            max_index = r
        return max_index

    def __get_parent(self, index):
        return ((index + 1) // 2) - 1

    def __get_grand_parent(self, index):
        return ((index + 1) // 2 // 2) - 1

    def __get_leftest_child(self, index):
        return ((index + 1) * 2) - 1

    def __get_leftest_grand_child(self, index):
        return ((index + 1) * 2 * 2) - 1

    def min(self):
        return self._list[0]

    def max(self):
        return self._list[self.__max_at()]

    def __max_at(self):
        _max = 0
        left = 1
        right = 2
        if (self.__is_in_valid_range(left) and
           self.__is_greater_than(left, _max)):
            _max = left
            if (self.__is_in_valid_range(right) and
               self.__is_greater_than(right, _max)):
                _max = right
        return _max

    def __swap(self, a, b):
        self._list[a], self._list[b] = self._list[b], self._list[a]

    def __is_in_valid_range(self, index):
        return index < len(self._list)

    def __is_at_min_level(self, index):
        return ceil(log(index + 2, 2)) % 2 == 1

    def __is_at_max_level(self, index):
        return not self.__is_at_min_level(index)

    def __is_smaller_than(self, index_a, index_b):
        return self._list[index_a] < self._list[index_b]

    def __is_greater_than(self, index_a, index_b):
        return self._list[index_a] > self._list[index_b]


for _ in range(0, 1000):
    for i in range(49, 50):
        t = []
        h = MinMaxHeap()
        a = []
        for j in range(0, i):
            x = random()
            t.append(x)
            h.insert(x)
        t.sort()
    
        for _ in range(0, len(t)):
            a.insert(0, h.delete_max())
        print(a)
        print()
        print(t)
        assert a == t
        # if h.min() != t[0]:
        #     print(h.min())
        #     print(t[0])
        #     print()
        # if h.max() != t[-1]:
        #     print(h.max())
        #     print(t[-1])
    #     print()
