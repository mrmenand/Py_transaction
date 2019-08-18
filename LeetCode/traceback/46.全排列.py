# 46. 全排列
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def traceback(nums,tmp):
            if not nums:
                ret.append(tmp)
                return
            for i in range(len(nums)):
                traceback(nums[:i]+nums[i+1:],tmp+[nums[i]])

        traceback(nums,[])
        return ret
        # return list(itertools.permution(nums))





