# 970.强整数
import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):

        res = set()
        max_x = 1 if x == 1 else int(math.log(bound,x))+1
        max_y = 1 if y == 1 else int(math.log(bound,y))+1
        for i in range(max_x):
            for j in range(max_y):
                tmp = x ** i + y ** j
                if tmp > bound:
                    break
                res.add(tmp)

        return list(res)

