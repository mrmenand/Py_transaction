# 228. 汇总区间
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        if not nums:
            return ret

        left, right = 0, len(nums)
        while left < right:
            start = left
            while left < right - 1 and nums[left] + 1 == nums[left + 1]:
                left += 1

            if left == start:
                ret.append(str(nums[left]))
            else:
                ret.append((str(nums[start]) + "->" + str(nums[left])))

            left += 1

        return ret
