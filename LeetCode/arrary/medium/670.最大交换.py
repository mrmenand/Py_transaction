# 670.最大交换
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [_ for _ in str(num)]
        for index, elem in enumerate(nums):
            max_num = max(nums[index:])
            if elem != max_num:
                j = "".join(nums[index:]).rfind(max_num) + index
                nums[index], nums[j] = nums[j], nums[index]
                break

        return int("".join(nums))

