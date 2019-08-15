# 278. 第一个错误的版本
class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        return l
