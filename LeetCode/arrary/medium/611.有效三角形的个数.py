# 611. 有效三角形的个数
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        for i in range(len(nums) - 1, 1, -1):
            left, right = 0, i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ret += (right - 1) - left + 1
                    right -= 1
                else:
                    left += 1

        return ret
