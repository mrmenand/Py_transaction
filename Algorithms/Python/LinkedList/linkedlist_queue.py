import abc
from random import randint

from  LinkedList.linkedlist import LinkedList

class Queue:
    @abc.abstractmethod
    def enqueue(self, e):
        pass

    @abc.abstractmethod
    def dequeue(self):
        pass

    @abc.abstractmethod
    def get_front(self):
        pass

    @abc.abstractmethod
    def get_size(self):
        pass

    @abc.abstractmethod
    def is_empty(self):
        pass

class LinkedListQueue(Queue):
    class _Node :
        def __init__(self,e =None,next = None):
            self.e = e
            self.next = next

        def __str__(self):
            return str(self.e)

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        if not self._tail:
            self._tail = self._Node(e)
            self._head = self._tail
        else:
            self._tail.next = self._Node(e)
            self._tail = self._tail.next
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Empty queue")

        ret = self._head
        self._head = self._head.next
        ret.next = None

        if not self._head:
            self._tail = None
        self._size -= 1

        return ret.e

    def get_front(self):
        if self.is_empty():
            raise ValueError("Empty Queue")
        return self._head.e

    def __str__(self):
        cur = self._head
        res = []
        while cur:
            res.append(str(cur.e))
            cur = cur.next
        return "LinkedListQueue : " + "->".join(res) + "  NULL"

if __name__ == '__main__':
    queue = LinkedListQueue()
    for _ in range(10):
        queue.enqueue(randint(60, 100))
    print(queue)
    queue.dequeue()
    print(queue)
    print(queue.get_front())