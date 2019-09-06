# 81. 搜索旋转排序数组 II

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left,right = 0, len(nums) -1

        while left < right :
            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                if nums[mid+1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            elif nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1

            else:
                if nums[right] == target:
                    return True
                right -= 1

        return nums[right] == target

