# 189. 旋转数组
class Solution:
    def rotate(self,nums,k):
        # nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]
