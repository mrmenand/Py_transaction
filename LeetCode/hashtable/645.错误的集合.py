# 645. 错误的集合
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # err = sum(nums) - sum(set(nums))
        # loss = set(i for i in range(1,len(nums)+1))-set(nums)
        return [sum(nums) - sum(set(nums)),sum(set(range(1, len(nums)+1)) - set(nums))]
