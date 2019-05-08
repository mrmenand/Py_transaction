# 438. 找到字符串中所有字母异位词
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hp,hs, res = {}, {}, []
        for i in p:
            hp[i] = hp.get(i,0) + 1
        n = len(p)

        for i , v in enumerate(s):
            hs[v] = hs.get(v,0) + 1
            if hs == hp:
                res.append(i-n+1)

            if i-n+1 >= 0 :
                hs[s[i-n+1]] = hs.get(s[i-n+1])-1
                if hs[s[i-n+1]] == 0:
                    del hs[s[i-n+1]]

        return res




