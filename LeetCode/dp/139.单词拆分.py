# 139. 单词拆分
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        breakup = [0]

        for i in range(len(s) + 1):
            for j in breakup:
                if s[j:i] in wordDict:
                    breakup.append(i)
                    break
        return breakup[-1] == len(s)
