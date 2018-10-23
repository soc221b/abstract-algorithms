class SinglyListNode():

    def __init__(self, var, *, next=None):
        self.__var = var
        self.__next = next

    @property
    def var(self):
        return self.__var

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class DoublyListNode():

    def __init__(self, var, *, prev=None, next=None):
        self.__var = var
        self.__prev = prev
        self.__next = next

    @property
    def var(self):
        return self.__var

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next
