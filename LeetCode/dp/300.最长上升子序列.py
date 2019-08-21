# 300. 最长上升子序列
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        tail = [nums[0]]
        for i in range(1, n):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue

            left, right = 0, len(tail) - 1
            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid

            tail[left] = nums[i]

        return len(tail)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n <= 1:
#             return n
#         dp = [1] * n
#         for i in range(1,n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i],dp[j]+1)
#
#         return max(dp)
