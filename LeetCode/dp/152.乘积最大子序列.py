# 152. 乘积最大子序列
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret, up, down = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            if n >= 0:
                up, down = max(up * n, n), min(down * n, n)
            else:
                up, down = max(down * n, n), min(up * n, n)
            ret = max(ret, up)

        return ret
