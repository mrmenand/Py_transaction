# 219. 存在重复元素 II
class Solution:
    def containsNearbyDuplicate(self,nums,k):
             # nums: List[int], k: int) -> bool:
             dict = {}
             for i,nums in enumerate(nums):
                 if nums in dict and i - dict[nums] <= k:
                     return True
                 dict[nums] = i


             return False