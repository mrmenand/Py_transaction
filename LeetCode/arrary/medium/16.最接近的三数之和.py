# 16. 最接近的三数之和
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ret = float("inf")

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]

                if cur == target:
                    return cur
                if abs(cur - target) < abs(ret - target):
                    ret = cur

                if cur > target:
                    right -= 1
                elif cur < target:
                    left += 1

        return ret
