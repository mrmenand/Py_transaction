# 198.打家劫舍
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for i in nums:
            pre, cur = cur, max(pre + i, cur)

        return cur

    # class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # st  dp(i) =  max(dp(i-2)+i,dp(k-1))
#         nums = [0,0] + nums
#         for i in range(2,len(nums)):
#             nums[i] = max(nums[i] + nums[i-2],nums[i-1])
#         return max(nums[-1],nums[-2])


if __name__ == '__main__':
    a = Solution().rob(nums=[2,7,9,3,1])
    print(a)
