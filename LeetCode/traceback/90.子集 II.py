# 90. 子集 II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ret = []
        n = len(nums)
        nums.sort()

        def traceback(i, tmp):
            ret.append(tmp)
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                traceback(j + 1, tmp + [nums[j]])

        traceback(0, [])

        return ret
