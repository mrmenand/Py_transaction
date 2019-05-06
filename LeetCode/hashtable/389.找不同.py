# 389. 找不同
class Solution(object):
    def findTheDifference(self, s, t):
       res = 0
       for i in s+t:
           res = res ^ ord(i)
       return chr(res)
