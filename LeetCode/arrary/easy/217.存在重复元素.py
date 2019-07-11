# 217. 存在重复元素
from collections import Counter


# class Solution: #忽然想到有统计的用法
#     def containsDuplicate(self,nums):
#                           # nums: List[int]) -> bool:
#         if nums ==[]:
#             return False
#         if Counter(nums).most_common(1)[0][1] >1:
#             return True
#         else:
#             return False
class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums)) ==len(nums):
            return False
        else:
            return True