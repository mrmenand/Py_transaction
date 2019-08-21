# 381. O(1) 时间插入、删除和获取随机元素 - 允许重复
import random
from collections import defaultdict

class RandomizedSet:

    def __init__(self):
        self.set_d = defaultdict(int)
        self.set_l = []

    def insert(self, val: int) -> bool:
        if self.set_d[val] == 0:
            self.set_l.append(val)  # O(1)
            self.set_d[val] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if self.set_d.get(val) == 1:
            self.set_l.remove(val)  # O(n)
            self.set_d[val] = 0
            return True
        else:
            return False


    def getRandom(self) -> int:
        if self.set_l:
            return random.choice(self.set_l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()