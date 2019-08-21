# 673. 最长递增子序列的个数
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        lengths = [0] * n
        counts = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] <= nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        longst = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longst)


print(Solution().lengthOfLIS(nums=[10,9,2,5,3,7,101,18]))