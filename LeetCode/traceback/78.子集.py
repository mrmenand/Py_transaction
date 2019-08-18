# 78.子集
# import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def traceback(i, tmp):
            ret.append(tmp)
            for j in range(i, len(nums)):
                traceback(j + 1, tmp + [nums[j]])

        traceback(0, [])
        return ret

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         return [list(tmp) for i in range(len(nums)+1) for tmp in itertools.combinations(nums,i)]
