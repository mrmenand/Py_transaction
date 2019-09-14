# 565. 数组嵌套
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ret = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if not visited[i]:
                S = nums[::]
                cnt = 0
                while S[i] != -1:
                    visited[i] = True
                    S[i], i = -1, S[i]
                    cnt += 1
                ret = max(ret, cnt)

        return ret
