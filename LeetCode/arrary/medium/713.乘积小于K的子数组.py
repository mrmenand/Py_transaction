# 713. 乘积小于K的子数组
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        mul = 1
        ret, left = 0, 0
        for right, val in enumerate(nums):
            mul *= val
            while mul >= k:
                mul /= nums[left]
                left += 1

            ret += right - left + 1

        return ret
