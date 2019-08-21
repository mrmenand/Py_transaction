# 55. 跳跃游戏
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dis = 0
        for idx, num in enumerate(nums):
            if max_dis < idx:
                return False
            max_dis = max(max_dis, idx + num)
        return True


a = Solution()
print(a.canJump([2, 3, 1, 1, 4]))
