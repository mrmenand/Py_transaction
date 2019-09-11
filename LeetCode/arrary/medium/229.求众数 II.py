# 229 求众数
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        return [x for x in dic.keys() if dic[x] > n / 3]
