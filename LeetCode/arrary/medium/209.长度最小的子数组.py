# 209. 长度最小的子数组
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, cur, ret = 0, 0, float("inf")
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                ret = min(ret, right - left + 1)
                cur -= nums[left]
                left += 1

        return ret if ret != float("inf") else 0
