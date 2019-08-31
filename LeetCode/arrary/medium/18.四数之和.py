    # 18. 四数之和
    class Solution:
        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            n = len(nums)
            ret = []
            nums.sort()

            for i in range(n - 3):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if nums[i] + sum(nums[i + 1:i + 4]) > target:
                    break

                if nums[i] + sum(nums[-1:-4:-1]) < target:
                    continue

                for j in range(i + 1, n - 2):
                    if j - i > 1 and nums[j] == nums[j - 1]:
                        continue
                    if nums[i] + nums[j] + sum(nums[j + 1:j + 3]) > target:
                        break

                    if nums[i] + nums[j] + sum(nums[-1:-3:-1]) < target:
                        continue

                    left, right = j + 1, n - 1

                    while left < right:
                        tmp_sum = nums[i] + nums[j] + nums[left] + nums[right]
                        if tmp_sum < target:
                            left += 1
                        elif tmp_sum > target:
                            right -= 1
                        else:
                            ret.append([nums[i], nums[j], nums[left], nums[right]])

                            while left < right and nums[left] == nums[left + 1]:
                                left += 1
                            while left < right and nums[right] == nums[right - 1]:
                                right -= 1
                            left += 1
                            right -= 1

            return ret
