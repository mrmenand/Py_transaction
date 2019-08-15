# 461.汉明距离
class Solution(object):
    def hammingDistance(self, x, y):
        y = x ^ y
        cnt = 0
        while y:
            y &= y - 1
            cnt += 1

        return cnt

        # return bin(x ^ y).count('1')
