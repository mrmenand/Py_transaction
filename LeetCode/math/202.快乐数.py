# 202. 快乐数
class Solution:
    def isHappy(self, n: int) -> bool:
        happy_num = set()
        while n not in happy_num:
            happy_num.add(n)
            n = sum([int(i) ** 2 for i in str(n)])

        return n == 1

# class Solution:
#     def isHappy(self, n: int) -> bool:
#
#         while n != 1 and n != 4:
#             n = sum([int(i)**2 for i in str(n)])
#
#         return n == 1
