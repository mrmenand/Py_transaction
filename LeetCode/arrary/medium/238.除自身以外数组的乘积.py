# 238. 除自身以外数组的乘积
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ret, l, r = [1] * n, 1, 1
        for i in range(n):
            ret[i], l = ret[i] * l, l * nums[i]
            ret[n - i - 1],r = ret[n - i - 1] * r, r * nums[n - i - 1]

        return ret
