# 442. 数组中重复的数据
class Solution(object):
    # 对应位置的数字取负数 如果发现已经是负数 说明这个下标是重复的。
    def findDuplicates(self, nums):
        ret = []
        for i in nums:
            if nums[abs(i)-1] < 0 :
                ret.append(abs(i))
            nums[abs(i)-1] *= -1

        return  ret




