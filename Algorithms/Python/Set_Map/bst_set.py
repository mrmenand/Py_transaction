from time import time

from BST.bst import BST
from Set_Map.set_map import Set


class BSTSet(Set):

    def __init__(self):
        self._bst = BST()

    def getSize(self):
        return self._bst.size()

    def isEmpty(self):
        return self._bst.size() == 0

    def contains(self, e):
        return self._bst.contains(e)

    def remove(self, e):
        self._bst.remove(e)

    def add(self, e):
        self._bst.add(e)




if __name__ == '__main__':
    words = ""
    with open("./ZenofPython","r") as f:
        words = f.read()
    words = words.split()

    start_time = time()
    bst_set = BSTSet()
    for word in words:
        bst_set.add(word)

    print('Total words: ', len(words))
    print('Unique words: ', bst_set.getSize())
    print('Contains word "better": ', bst_set.contains('better'))
    print(f'Total time: {time() - start_time} seconds')




