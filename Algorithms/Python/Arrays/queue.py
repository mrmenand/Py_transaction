import abc
from random import randint
from time import time
from Arrays.array import Array


class Queue:
    @abc.abstractmethod
    def enqueue(self, e):
        pass

    @abc.abstractmethod
    def dequeue(self):
        pass

    @abc.abstractmethod
    def get_font(self):
        pass

    @abc.abstractmethod
    def get_size(self):
        pass

    @abc.abstractmethod
    def is_empty(self):
        pass


# 内置List实现Queue
class ListQueue(object):
    """队列"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """入队"""
        self.__list.append(item)
        # self.__list.insert(0,item)

    def dequeue(self):
        """出队"""
        return self.__list.pop(0)
        # return self.__list.pop()

    def is_empty(self):
        """"判空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


# 自定义Array实现队列
class ArrayQueue(Queue):
    def __init__(self, capacity=0):
        self._array = Array(capacity)

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def get_capacity(self):
        return self.get_capacity()

    def get_font(self):
        return self._array.get_first()

    def enqueue(self, e):
        self._array.append(e)

    def dequeue(self):
        return self._array.remove_first()

    def __str__(self):
        return str(f"ArrayQueue : {self._array}")


# 内置List实现循环队列
class CircuQueue(Queue):

    def __init__(self, capacity=10):
        self._data = [None] * (capacity + 1)
        self._tail = 0
        self._front = 0
        self._size = 0

    def get_capacity(self):
        return len(self._data) - 1

    def is_empty(self):
        return self._front == self._tail

    def get_size(self):
        return self._size

    def get_font(self):
        if self.is_empty():
            raise ValueError("Can not get_front from an empty queue")
        return self._data[self._front]

    def enqueue(self, e):
        if (self._tail + 1) % len(self._data) == self._front:
            self._resize(self.get_capacity() * 2)
        self._data[self._tail] = e
        self._tail = (self._tail + 1) % len(self._data)
        self._size += 1

    def dequeue(self):
        if (self.is_empty()):
            raise ValueError("Can not dequeue from an empty queue.")

        ret = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size == self.get_capacity() // 4 and self.get_capacity() // 2 != 0:
            self._resize(self.get_capacity() // 2)
        return ret

    def _resize(self, new_capacity):
        new_data = [None] * (new_capacity + 1)
        for i in range(self._size):
            new_data[i] = self._data[(i + self._front) % len(self._data)]

        self._data = new_data
        self._front = 0
        self._tail = self._size

    def __str__(self):
        if self._tail >= self._front:
            return str(
                f"<CircuQueue> : front {self._data[self._front : self._tail ]}  tail, "
                f"capacity :{self.get_capacity()}")
        else:
            return str(
                f"<CircuQueue> : front {self._data[self._front: ]+self._data[:self._tail]}  tail, "
                f"capacity :{self.get_capacity()}")

# 内置List实现双端队列


class Dequeue(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """头部入"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """尾部入"""
        self.__list.append(item)

    def pop_front(self):
        """头部取"""
        return self.__list.pop(0)

    def pop_rear(self):
        """尾部取"""
        return self.__list.pop()

    def is_empty(self):
        """"判空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':

    def test_queue(queue, op_count):
        start_time = time()
        for _ in range(op_count):
            queue.enqueue(randint(10, 6666))
        for _ in range(op_count):
            queue.dequeue()

        return time() - start_time

    op_count = 10000
    array_queue = ArrayQueue()
    circu_queue = CircuQueue()

    print("ArrayQueue:", test_queue(array_queue, op_count), "S")
    print("CircuQueue:", test_queue(circu_queue, op_count), "S")
