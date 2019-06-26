from time import time

from Set_Map.set_map import Map


class BSTMap(Map):

    class _Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return f"Key :{str(self.key)} , Value : {str(self.value)} "

    def __init__(self):
        self._root = None
        self._size = 0

    def getSize(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self, key, value):
        self._root = self._add(self._root, key, value)

    def _add(self, node, key, value):

        if not node:
            self._size += 1
            return self._Node(key, value)

        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        else:
            node.value = value

        return node

    def _getNode(self, node, key):

        if not node:
            return
        if key < node.key:
            return self._getNode(node.left, key)
        elif key > node.key:
            return self._getNode(node.right, key)
        else:
            return node

    def get(self, key):
        node = self._getNode(self._root, key)
        return node.value if node else None

    def set(self, key, newvalue):
        node = self._getNode(self._root, key)
        if not node:
            raise ValueError(key + " doesn't exist ")
        node.value = newvalue

    def contains(self, key):
        return self._getNode(self._root, key) is not None

    def remove(self, key):

        node = self._getNode(self._root, key)
        if node:
            self._root = self._remove(self._root, key)
            return node.value
        return None

    def _remove(self, node, key):

        if not node:
            return
        if key < node.key:
            node.left = self._remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self._remove(node.right, key)
            return node
        else:
            if not node.left:
                rightNode = node.right
                node.right = None
                self._size -= 1
                return rightNode
            if not node.right:
                leftNode = node.left
                node.left = None
                self._size -= 1
                return leftNode

            successor = self._mininum(node.right)
            successor.right = self._removeMin(node.right)
            successor.left = node.left
            node.left = node.right = None
            return successor

    def _mininum(self, node):
        if not node.left:
            return node
        return self._mininum(node.left)

    def mininum(self):
        if self.isEmpty():
            raise ValueError("Empty is empty")
        self._mininum(self._root)

    def _removeMin(self, node):

        if not node.left:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node

        node.left = self._removeMin(node.left)
        return node


if __name__ == '__main__':
    words = ""
    with open("./ZenofPython", "r") as f:
        words = f.read()
    words = words.split()

    start_time = time()

    bst_map = BSTMap()
    for word in words:
        if bst_map.contains(word):
            bst_map.set(word, bst_map.get(word) + 1)
        else:
            bst_map.add(word, 1)

    print('Total words: ', len(words))
    print('Unique words: ', bst_map.getSize())
    print('Contains word "better": ', bst_map.contains('better'))
    print(f'Total time: {time() - start_time} seconds')

    # bst_map.remove("better")
    print(bst_map.contains("better"))

    bst_map.set("better", 100)
    print(bst_map.get("better"))
