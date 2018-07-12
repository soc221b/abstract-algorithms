def less_closure(a, b):
    return a < b


class Comparison():

    def __init__(self, less_closure=less_closure):
        self.__less_closure = less_closure

    def less_closure(self, a, b):
        return self.__less_closure(a, b)

    def greater_closure(self, a, b):
        return self.__less_closure(b, a)

    def less_equal_closure(self, a, b):
        return not self.greater_closure(a, b)

    def greater_equal_closure(self, a, b):
        return not self.__less_closure(a, b)

    def equal_closure(self, a, b):
        return (self.less_equal_closure(a, b) and
                self.greater_equal_closure(a, b))

    def not_equal_closure(self, a, b):
        return not self.equal_closure(a, b)

    def compare_closure(self, a, b):
        if self.__less_closure(a, b):
            return -1
        elif self.greater_closure(a, b):
            return 1
        else:
            return 0
