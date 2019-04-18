# 830. 较大分组的位置
class Solution:
    def largeGroupPositions(self,S):
                # S: str) -> List[List[int]]:
                res,i,n = [],0,len(S)
                while i < n:
                    j = i+1
                    while j < n and S[j] == S[i]:
                        j += 1

                    if j-i >2:
                        res.append([i,j-1])

                    i = j
                return res





