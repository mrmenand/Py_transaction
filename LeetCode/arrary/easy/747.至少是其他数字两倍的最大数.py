# 747. 至少是其他数字两倍的最大数
class Solution:
    def dominantIndex(self,nums):
            # nums: List[int]) -> int:
            if not nums :
                return -1
            if len(nums)==1:
                return 0
            sorted_nums = sorted(nums)
            if sorted_nums[-1] < 2*sorted_nums[-2]:
                return -1
            else:
                return nums.index(sorted_nums[-1])
