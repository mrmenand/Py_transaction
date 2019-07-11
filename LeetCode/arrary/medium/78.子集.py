# 78.子集
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ret = []
        # for i in range(len(nums)+1):
        #     for tmp in itertools.combinations(nums,i):
        #         ret.append(tmp)
        # return ret
        return [list(tmp)  for i in range(len(nums)+1) for tmp in itertools.combinations(nums,i)]






