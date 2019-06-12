from random import randint

class Array:
    def __init__(self, arr=None, capacity=10):
        if isinstance(arr, list):
            self._data = arr[:]
            self._size = len(arr)
            return

        self._data = [None] * capacity
        self._size = 0

    def get_size(self):
        return self._size

    def get_capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def add(self, index, e):
        if not (0 <= index <= self._size):
            raise ValueError(
                "add failed. Require index >= 0 and index <= array sise")
        if self._size == len(self._data):
            if self._size == 0:
                self._resize(1)
            else:
                self._resize(2 * len(self._data))

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = e
        self._size += 1

    def append(self, e):
        self.add(self._size, e)

    def add_first(self, e):
        self.add(0, e)

    def get(self, index):
        if not (0 <= index <= self._size):
            raise ValueError("get failed. Index is illegal")
        return self._data[index]

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self._size - 1)

    def set(self, index, e):
        if not (0 <= index <= self._size):
            raise ValueError("set failed. Index is illegal")
        self._data[index] = e

    def contains(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return True

        return -1

    def find(self, e):
        for i, v in enumerate(self._data):
            if v == e:
                return i
        return -1

    def remove(self, index):
        if not (0 <= index <= self._size):
            raise ValueError("remove failed. Index is illegal")

        ret = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._size -= 1
        # len(self._data)如果为1，len(self._data) // 2就会为0，不合理。
        if (self._size == len(self._data) // 4 and len(self._data) // 2 != 0):
            self._resize(len(self._data) // 2)

        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_elment(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data

    def swap(self, i, j):
        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            raise ValueError('Index is illegal.')
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __str__(self):
        return str(
            f"Array : {self._data[:self._size]}  ,capacity:{self.get_capacity()}")



if __name__ == '__main__':
    arr = Array()
    for _ in range(10):
        arr.append(randint(66, 100))
    print(arr)

    arr.append(2)
    print(arr)

    arr.remove_last()
    arr.remove_last()
    print(arr)

    arr.add_first(100)
    print(arr)

    arr.add(6, "mr_menand")
    print(arr)
