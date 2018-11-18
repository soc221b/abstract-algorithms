from math import log, ceil


class MinMaxHeap():
    """
    operations and time complexity:
        min: O(1)
        max: O(1)
        insert: O(log n)
        delete_min: O(log n)
        delete_max: O(log n)
        is_empty: O(1)
    """

    def __init__(self, _list=[]):
        # no test
        # raise NotImplementedError
        self._list = []
        for elem in _list:
            self.insert(elem)

    def min(self):
        if not self.is_empty():
            return self._list[0]
        else:
            return None

    def max(self):
        if not self.is_empty():
            return self._list[self.__max_at()]
        else:
            return None

    def is_empty(self):
        return len(self._list) == 0

# insert begin
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
        parent = self.__get_parent_index(index)
        grand_parent = self.__get_grand_parent_index(index)
        if self.__is_greater_than(index, parent):
            self.__swap(index, parent)
            self.__update_max_bottom_up(parent)
        elif (self.__is_in_valid_range(grand_parent) and
              self.__is_smaller_than(index, grand_parent)):
            self.__swap(index, grand_parent)
            self.__update_min_bottom_up(grand_parent)

    def __update_max_bottom_up(self, index):
        if index <= 0:
            return
        parent = self.__get_parent_index(index)
        grand_parent = self.__get_grand_parent_index(index)
        if self.__is_smaller_than(index, parent):
            self.__swap(index, parent)
            self.__update_min_bottom_up(parent)
        elif (self.__is_in_valid_range(grand_parent) and
              self.__is_greater_than(index, grand_parent)):
            self.__swap(index, grand_parent)
            self.__update_max_bottom_up(grand_parent)
# insert end

# delete min begin
    def delete_min(self):
        if self.is_empty():
            return None

        _min = self.min()

        # maintain
        latest_index = len(self._list) - 1
        self._list[0] = self._list[latest_index]
        del self._list[latest_index]
        if self.__is_in_valid_range(0):
            self.__update_min_top_down(0)

        return _min

    def __update_min_top_down(self, index):
        grand_child = self.__get_leftest_grand_child(index)

        min_index = self.__find_smallest(index)

        if min_index != index:
            self.__swap(min_index, index)
            if min_index >= grand_child:
                parent = self.__get_parent_index(min_index)
                if self.__is_greater_than(min_index, parent):
                    self.__swap(min_index, parent)
                self.__update_min_top_down(min_index)

    def __find_smallest(self, index):
        min_index_for_grand_childs = \
            self.__find_smallest_for_grand_childs(index)
        # the min-max-tree is complete B.T.,
        # hence level for left tree may larger than right tree.
        min_index_for_childs = self.__find_smallest_for_childs(index)

        if self.__is_smaller_than(
           min_index_for_childs, min_index_for_grand_childs):
            return min_index_for_childs
        else:
            return min_index_for_grand_childs

    def __find_smallest_for_grand_childs(self, index):
        min_index = index
        ll = self.__get_leftest_grand_child(index)
        lr = ll + 1
        rl = ll + 2
        rr = ll + 3

        if (self.__is_in_valid_range(ll) and
           self.__is_greater_than(min_index, ll)):
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
        left = self.__get_leftest_child(index)
        right = left + 1

        if (self.__is_in_valid_range(left) and
           self.__is_greater_than(min_index, left)):
            min_index = left
        if (self.__is_in_valid_range(right) and
           self.__is_greater_than(min_index, right)):
            min_index = right

        return min_index
# delete min end

# delete max begin
    def delete_max(self):
        if self.is_empty():
            return None

        max_at = self.__max_at()
        _max = self._list[max_at]

        # maintain
        latest_index = len(self._list) - 1
        self._list[max_at] = self._list[latest_index]
        del self._list[latest_index]
        if self.__is_in_valid_range(max_at):
            self.__update_max_top_down(max_at)

        return _max

    def __update_max_top_down(self, index):
        grand_child = self.__get_leftest_grand_child(index)
        max_index = self.__find_greatest(index)

        if max_index != index:
            self.__swap(max_index, index)
            if max_index >= grand_child:
                parent = self.__get_parent_index(max_index)
                if self.__is_smaller_than(max_index, parent):
                    self.__swap(max_index, parent)
                self.__update_max_top_down(max_index)

    def __find_greatest(self, index):
        max_index_for_grand_childs = \
            self.__find_greatest_for_grand_childs(index)
        # the min-max-tree is complete B.T.,
        # hence level for left tree may larger than right tree.
        max_index_for_childs = self.__find_greatest_for_childs(index)

        if self.__is_greater_than(
           max_index_for_childs, max_index_for_grand_childs):
            return max_index_for_childs
        else:
            return max_index_for_grand_childs

    def __find_greatest_for_grand_childs(self, index):
        max_index = index
        ll = self.__get_leftest_grand_child(index)
        lr = ll + 1
        rl = ll + 2
        rr = ll + 3

        if (self.__is_in_valid_range(ll) and
           self.__is_smaller_than(max_index, ll)):
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
        left= self.__get_leftest_child(index)
        right = left + 1

        if (self.__is_in_valid_range(left) and
           self.__is_smaller_than(max_index, left)):
            max_index = left
        if (self.__is_in_valid_range(right) and
           self.__is_smaller_than(max_index, right)):
            max_index = right

        return max_index
# delete max end

    def __get_parent_index(self, index):
        return ((index + 1) // 2) - 1

    def __get_grand_parent_index(self, index):
        return ((index + 1) // 2 // 2) - 1

    def __get_leftest_child(self, index):
        return ((index + 1) * 2) - 1

    def __get_leftest_grand_child(self, index):
        return ((index + 1) * 2 * 2) - 1

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
        return 0 <= index < len(self._list)

    def __is_at_min_level(self, index):
        return ceil(log(index + 2, 2)) % 2 == 1

    def __is_at_max_level(self, index):
        return not self.__is_at_min_level(index)

    def __is_smaller_than(self, index_a, index_b):
        return self._list[index_a] < self._list[index_b]

    def __is_greater_than(self, index_a, index_b):
        return self._list[index_a] > self._list[index_b]
