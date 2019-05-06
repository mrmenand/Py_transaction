# 961. 重复 N 次的元素
class Solution(object):
    def repeatedNTimes(self, A):
        cnt = len(A)//2
        for i in A:
            if A.count(i) == cnt:
                return i