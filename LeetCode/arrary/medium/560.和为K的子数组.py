# 560. 和为K的子数组
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        ret, sumN = 0, 0
        for num in nums:
            sumN += num
            ret += dic.get(sumN - k, 0)
            dic[sumN] = dic.get(sumN, 0) + 1

        return ret
