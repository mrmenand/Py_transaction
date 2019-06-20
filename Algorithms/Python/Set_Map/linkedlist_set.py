from time import time

from LinkedList.linkedlist import LinkedList
from Set_Map.set_map import Set

class LinkedListSet(Set):

    def __init__(self):
        self._list = LinkedList()

    def getSize(self):
        return self._list.get_size()

    def isEmpty(self):
        return self.isEmpty()

    def contains(self, e):
        return self._list.contains(e)

    def add(self, e):
        if self.contains(e):
            return
        self._list.add_first(e)

    def remove(self, e):
        self._list.remove(e)


if __name__ == '__main__':
    words = ""
    with open("./ZenofPython","r") as f:
        words = f.read()
    ##QAQ : 怎么同时以空格和.切割
    words = words.split()

    start_time = time()
    list = LinkedListSet()
    for word in words:
        list.add(word)

    print('Total words: ', len(words))
    print('Unique words: ', list.getSize())
    print('Contains word "better": ', list.contains('better'))
    print(f'Total time: {time() - start_time} seconds')
