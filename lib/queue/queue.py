from lib.linked_list import SinglyListNode as ListNode


class Queue():

    def __init__(self):
        self.__head_node = ListNode(0)
        self.__tail_node = self.__head_node
        self.__len = 0

    def push(self, x):
        new_node = ListNode(x)
        self.__tail_node.next = new_node
        self.__tail_node = new_node
        self.__len += 1

    def pop(self):
        if self.is_empty():
            raise IndexError
        else:
            peek_node = self.__head_node.next
            self.__head_node.next = peek_node.next
            self.__len -= 1
            return peek_node.var

    def peek(self):
        if self.is_empty():
            raise IndexError
        else:
            return self.__head_node.next.var

    def is_empty(self):
        return len(self) == 0

    def reverse(self):
        if not self.is_empty():
            head_node = self.__head_node
            new_second_node = None
            while head_node.next.next is not None:
                old_peek_node = head_node.next
                old_second_node = head_node.next.next
                old_peek_node.next = new_second_node
                head_node.next = old_second_node
                new_second_node = old_peek_node
            head_node.next.next = new_second_node

    def __len__(self):
        return self.__len

    def copy(self):
        copied_queue = Queue()
        peek_node = self.__head_node.next
        while peek_node is not None:
            copied_queue.push(peek_node.var)
            peek_node = peek_node.next
        return copied_queue


def reversed_queue(que):
    copied_queue = que.copy()
    copied_queue.reverse()
    return copied_queue
