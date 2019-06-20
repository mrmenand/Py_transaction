from random import randint
from time import time

from Arrays.array import Array


class MaxHeap:

    def __init__(self, arr=None, capacity=None):
        if isinstance(arr, Array):
            self._data = arr
            for i in range(self._parent(arr.get_size() - 1), -1, -1):
                self._sift_down(i)
                return

        if not capacity:
            self._data = Array()
        else:
            self._data = Array(capacity=capacity)

    def size(self):
        return self._data.get_size()

    def is_empty(self):
        return self._data.is_empty()

    def _parent(self, index):
        if index <= 0 or index > self.size():
            raise ValueError("Illegal index")
        return (index - 1) // 2

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def add(self, e):
        self._data.append(e)
        self._sift_up(self.size() - 1)

    def _sift_up(self, k):
        while k > 0 and self._data.get(k) > self._data.get(self._parent(k)):
            self._data.swap(k, self._parent(k))
            k = self._parent(k)

    def find_max(self):
        if self.size() == 0:
            raise ValueError("Empty heap")
        return self._data.get(0)

    def extract_max(self):
        ret = self.find_max()
        self._data.swap(0, self._data.get_size() - 1)
        self._data.remove_last()
        self._sift_down(0)
        return ret

    def _sift_down(self, k):

        while self._left_child(k) < self.size():
            j = self._left_child(k)
            if j + 1 < self.size() and self._data.get(j + 1) > self._data.get(j):
                j = self._right_child(k)

            if self._data.get(k) > self._data.get(k):
                break

            self._data.swap(k, j)
            k = j

    def replace(self, e):
        ret = self.find_max()
        self._data.set(0, e)
        self._sift_down(0)
        return ret


if __name__ == '__main__':

    n = 1000000
    start_time1 = time()
    max_heap = MaxHeap()
    for _ in range(n):
        max_heap.add(randint(0, 6666))

    print(f"without heapify :{time() - start_time1}" + " seconds")

    start_time2 = time()
    arr = Array()
    for _ in range(n):
        arr.append(randint(0, 6666))

    max_heap = MaxHeap(arr)
    print(f"heapify : {time() - start_time2}" + " seconds")
