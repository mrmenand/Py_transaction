# 268. 缺失数字

class Solution:
    def missingNumber(self, nums):
        miss = len(nums)
        for i, num in enumerate(nums):
            miss ^= (i ^ num)
        return miss

# class Solution:
#     def missingNumber(self,nums):
#         for i in range(len(nums)+1):
#             if i not in nums:
#                return i

# tip 不要一直有for的思想

# class Solution:
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         s = sum(list(range(n+1)))
#         return s - sum(nums)
