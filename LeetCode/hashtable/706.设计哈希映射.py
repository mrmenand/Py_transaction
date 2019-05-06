# 706. 设计哈希映射
class MyHashMap(object):

    def __init__(self):
        self.hb = dict()

    def put(self, key, value):
       self.hb[key] = value

    def get(self, key):
      return self.hb[key] if key in self.hb else -1

    def remove(self, key):
      return self.hb.pop(key) if key in self.hb else -1

