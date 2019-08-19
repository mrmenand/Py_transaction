# 34. 在排序数组中查找元素的第一个和最后一个位置
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

            else:
                left, right = mid, mid
                while left - 1 >= 0 and nums[left - 1] == target:
                    left -= 1
                while right + 1 < len(nums) and nums[right+1] == target:
                    right += 1
                return [left, right]

        return [-1, -1]
