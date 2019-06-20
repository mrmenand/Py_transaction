from time import time
from Set_Map.set_map import Map

# QAQ 继承BSTMap怎么写


class LinkedListMap(Map):

    class _Node:
        def __init__(self, key=None, value=None, next=None):
            self.key = key
            self.value = value
            self.next = next

        def __str__(self):
            return f"Key :{str(self.key)} , Value : {str(self.value)} "

    def __init__(self):
        # super(BSTMap,self).__init__()
        self._dummy_head = self._Node()
        self._size = 0

    def getSize(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def _getnode(self, key):
        cur = self._dummy_head.next
        while cur:
            if cur.key == key:
                return cur
            cur = cur.next
        return

    def contains(self, key):
        return self._getnode(key) is not None

    def get(self, key):
        node = self._getnode(key)
        return node.value if node else None

    def set(self, key, newvalue):
        node = self._getnode(key)
        if not node:
            raise ValueError(key + "doesn't exist")
        else:
            node.value = newvalue

    def add(self, key, value):
        node = self._getnode(key)
        if not node:
            self._dummy_head.next = self._Node(
                key, value, self._dummy_head.next)
            self._size += 1
        else:
            node.value = value

    def remove(self, key):
        prev = self._dummy_head
        while prev.next:
            if prev.next.key == key:
                break
            prev = prev.next

        # if prev.next :
        del_node = prev.next
        prev.next = del_node.next
        del_node.next = None
        return del_node.value


if __name__ == '__main__':
    words = ""
    with open("./ZenofPython", "r") as f:
        words = f.read()
    words = words.split()

    start_time = time()

    list = LinkedListMap()
    for word in words:
        if list.contains(word):
            list.set(word, list.get(word) + 1)
        else:
            list.add(word, 1)

    print('Total words: ', len(words))
    print('Unique words: ', list.getSize())
    print('Contains word "better": ', list.contains('better'))
    print(f'Total time: {time() - start_time} seconds')

    list.remove("should")
    print(list.contains("should"))

    list.set("better", 100)
    print(list.get("better"))
