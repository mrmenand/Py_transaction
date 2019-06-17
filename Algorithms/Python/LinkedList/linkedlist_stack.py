import abc
from random import randint

from LinkedList.linkedlist import LinkedList


class Stack:
    @abc.abstractmethod
    def push(self):
        pass

    @abc.abstractmethod
    def pop(self):
        pass

    @abc.abstractmethod
    def peek(self):
        pass

    @abc.abstractmethod
    def get_size(self):
        pass

    @abc.abstractmethod
    def is_empty(self):
        pass


class LinkedListStack(Stack):

    def __init__(self):
        self._list = LinkedList()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()

    def push(self, e):
        self._list.add_first(e)

    def pop(self):
        return self._list.remove_first()

    def peek(self):
        return self._list.get_first()

    def __str__(self):
        cur = self._list._dummyhead.next
        res = []
        while cur:
            res.append(str(cur.e))
            cur = cur.next
        return "LinkedListStack : (Top) " + "->".join(res)


if __name__ == '__main__':
    stack = LinkedListStack()
    for _ in range(10):
        stack.push(randint(60, 100))
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())
