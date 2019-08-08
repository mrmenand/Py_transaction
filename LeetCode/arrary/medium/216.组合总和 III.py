# 216. 组合总和 III
from itertools import combinations


class Solution:
    def combinationSum3(self, k: int, n: int):
        def traceback(k: int, n: int, start: int):
            if k == 1:
                if n < 10:
                    return [[n]]
                return []

            ret = []
            for i in range(start + 1, min((n + 1) // 2, 10)):
                for j in traceback(k - 1, n - i, i):
                    ret.append([i] + j)
            return ret

        return traceback(k, n, 0)


# class Solution:
#     def combinationSum3(self, k: int, n: int):
#         nums = [i for i in range(1,10)]
#         return [i for i in combinations(nums,k) if sum(i) == n]

a = Solution()
b = a.combinationSum3(3,7)
print(b)
