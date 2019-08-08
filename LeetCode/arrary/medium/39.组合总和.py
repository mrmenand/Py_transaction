# 39. 组合总和
class Solution:
    def combinationSum(self, candidates: list, target: int):
        candidates.sort()
        n = len(candidates)
        ret = []

        def backtrace(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                ret.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrace(j, tmp_sum + candidates[j], tmp + [candidates[j]])


        backtrace(0, 0, [])
        return ret


# a = Solution()
# b= a.combinationSum(candidates = [2,3,6,7], target = 7)
# print(b)