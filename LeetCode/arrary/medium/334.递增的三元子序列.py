# 334.递增的三元子序列
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3:
            return False
        min_num, max_num = float("inf"), float("inf")

        for n in nums:
            if n < min_num:
                min_num = n
            elif min_num < n < max_num:
                max_num = n
            elif n > max_num:
                return True

        return False
