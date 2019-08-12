# 136 只出现一次的数字

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1

        for k,v in dic.items():
            if v == 1:
                return k

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         a = 0
#         for i in nums:
#             a = a ^ i
#
#         return a
