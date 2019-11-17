# 213. 打家劫舍 II
class Solution:
    def rob(self, nums: List[int]) -> int:
        # state transfer paradigm
        # dp[n+1] = max(dp[n],dp[n-1] + num)
        def myrob(nums):
            pre, cur = 0, 0
            for num in nums:
                pre, cur = cur, max(pre + num,cur)

            return cur

        return max(myrob(nums[1:]), myrob(nums[:-1])) if len(nums) != 1 else nums[0]
