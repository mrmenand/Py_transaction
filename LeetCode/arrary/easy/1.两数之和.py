# 1.两数之和
class Solution:
    def twoSum(self, nums,target):
               # nums: List[int], target: int) -> List[int]:
               for i in range(len(nums)):
                   if target - nums[i] in nums[i + 1:]:
                       sec_ind = nums[i + 1:].index(target - nums[i]) + i + 1
                       return [i , sec_ind]
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         mirror = {}
# #         for idx, num in enumerate(nums):
# #             if num in mirror:
# #                 return [mirror[num], idx]
# #             mirror[target - num] = idx