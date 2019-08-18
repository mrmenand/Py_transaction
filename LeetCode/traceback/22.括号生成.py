# 22. 括号生成
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def traceback(left, right, tmp):
            if left == right == n:
                ret.append(tmp)
            if left < n:
                traceback(left + 1, right, tmp + "(")
            if right < left:
                traceback(left, right + 1, tmp + ")")

        traceback(0, 0, "")
        return ret
