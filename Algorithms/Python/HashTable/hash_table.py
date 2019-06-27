from collections import defaultdict
from time import time

UPPER_TOL = 10
LOWER_TOL = 2
INIT_CAPACITY = 7


class HashTable:
    def __init__(self, M=INIT_CAPACITY):
        self._M = M
        self._size = 0
        self._hashtable = [defaultdict() for _ in range(M)]

    def _hash(self, key):
        return (hash(key) & 0x7fffffff) % self._M

    def get_size(self):
        return self._size

    def add(self, key, value):
        map = self._hashtable[self._hash(key)]
        # print(map)  不太理解这个map 
        if key in map:
            map[key] = value
        else:
            map[key] = value
            self._size += 1
            if self._size >= UPPER_TOL * self._M:
                self._resize(2 * self._M)

    def remove(self, key):

        map = self._hashtable[self._hash(key)]
        if key in map:
            ret = map.pop(key)
            self._size -= 1
            if self._size < LOWER_TOL * self._M and self._M // 2 >= INIT_CAPACITY:
                self._resize(self._M // 2)

        return ret

    def get(self, key):
        return self._hashtable[self._hash(key)][key]

    def set(self, key, value):
        map = self._hashtable[self._hash(key)]

        if key not in map:
            raise ValueError('{} doesn\'t exist!'.format(key))
        map[key] = value

    def contains(self, key):
        return key in self._hashtable[self._hash(key)]

    def _resize(self, new_M):
        new_hashtable = [defaultdict() for _ in range(new_M)]
        old_M = self._M
        self._M = new_M
        for i in range(old_M):
            map = self._hashtable[i]
            for key, value in map.items():
                new_hashtable[self._hash(key)][key] = value
        self._hashtable = new_hashtable


if __name__ == '__main__':
    words = ''
    with open('../Set_Map/ZenofPython', 'r') as f:
        words = f.read()
    words = words.split()

    start_time = time()
    hashtable = HashTable(M=100)
    for word in words:
        if hashtable.contains(word):
            hashtable.set(word, hashtable.get(word) + 1)
        else:
            hashtable.add(word, 1)

    print('Total words: ', len(words))
    print('Unique words: ', hashtable.get_size())
    print('Contains word "they": ', hashtable.contains('better'))
    print('HashTable Total time: {} seconds'.format(time() - start_time))
