# 40. 组合总和 II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        ret, n = [], len(candidates)

        def backtrace(i, tmp_sum, tmp):
            if tmp_sum == target:
                ret.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                backtrace(j + 1, tmp_sum + candidates[j], tmp + [candidates[j]])

        backtrace(0, 0, [])

        return ret
