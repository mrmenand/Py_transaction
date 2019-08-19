# 75. 颜色分类
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        cur = 0
        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
