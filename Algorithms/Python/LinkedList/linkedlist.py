class LinkedList:
    class _Node:
        def __init__(self, e=None, next=None):
            self.e = e
            self.next = next

        def __str__(self):
            return str(self.e)

    def __init__(self):
        self._dummyhead = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, index, e):
        if index < 0 or index > self._size:
            raise ValueError("Illegal index")

        prev = self._dummyhead
        for _ in range(index):
            prev = prev.next

        node = self._Node(e)
        node.next = prev.next
        prev.next = node
        self._size += 1

    def add_first(self, e):
        self.add(0, e)

    def add_last(self, e):
        self.add(self._size, e)

    def get(self, index):
        if index < 0 or index > self._size:
            raise ValueError("Illegal index")
        cur = self._dummyhead.next
        for _ in range(index):
            cur = cur.next

        return cur.e

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self._size - 1)

    def set(self, index, e):
        if index < 0 or index > self._size:
            raise ValueError("Illegal index")
        cur = self._dummyhead.next
        for _ in range(index):
            cur = cur.next

        cur.e = e

    def contains(self, e):
        cur = self._dummyhead.next
        while cur:
            if cur.e == e:
                return True
            cur = cur.next

        return False

    def remove(self, index):
        if index < 0 or index > self._size:
            raise ValueError("Illegal index")

        prev = self._dummyhead
        for _ in range(index):
            prev = prev.next

        ret = prev.next
        prev.next = ret.next
        ret.next = None
        self._size -= 1

        return ret.e

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def __str__(self):
        cur = self._dummyhead.next
        res = []
        while cur:
            res.append(str(cur.e))
            cur = cur.next
        return "LinkedList : " + "->".join(res) + "  NULL"


if __name__ == '__main__':
    linklist = LinkedList()
    for i in range(6):
        linklist.add_first(i)
    print(linklist)

    linklist.add(3, 666)
    print(linklist)

    linklist.remove_last()
    print(linklist)
