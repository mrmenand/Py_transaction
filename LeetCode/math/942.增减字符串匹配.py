# 942. 增减字符串匹配
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        s,l = 0, len(S)
        res = []
        for i in S:
            if i == "I":
                res.append(s)
                s += 1
            else:
                res.append(l)
                l -= 1

        res.append(l)

        return res



