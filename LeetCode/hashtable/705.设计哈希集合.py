# 705. 设计哈希集合
class MyHashSet(object):

    def __init__(self):
        self.hs = set()

    def add(self, key):
        self.hs.add(key)

    def remove(self, key):
        if key in self.hs:
            self.hs.remove(key)


    def contains(self, key):
        return True if key in self.hs else False

