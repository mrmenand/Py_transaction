# 771. 宝石与石头
class Solution(object):
    def numJewelsInStones(self, J, S):
        cnt = 0
        for i in S:
            if i in J:
               cnt += 1

        return cnt
