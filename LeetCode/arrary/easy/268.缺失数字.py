# 268. 缺失数字
class Solution:
    def missingNumber(self,nums):
                      # nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
               return i
#tip 不要一直有for的思想

# class Solution:
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         s = sum(list(range(n+1)))
#         return s - sum(nums)