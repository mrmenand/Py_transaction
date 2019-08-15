# 384. 打乱数组
import random
from copy import deepcopy


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.orignal = deepcopy(nums)


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.orignal

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        # random.shuffle(self.nums)
        # returm random.sample(self.num,len(self.num))
        for i in range(len(self.nums)):
            index = random.randrange(i,len(self.nums))
            self.nums[i],self.nums[index] = self.nums[index],self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()