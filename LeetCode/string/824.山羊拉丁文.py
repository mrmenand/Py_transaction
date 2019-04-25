# 824. 山羊拉丁文
class Solution:
    def toGoatLatin(self,S):
         # S: str) -> str:
         words = S.split()
         for i in range(len(words)):
             if words[i][0] in "aeiouAEIOU":
                 words[i] = words[i] + "ma" + (i+1)*"a"
             else:
                 words[i] = words[i][1:] + words[i][0] +"ma"+(i+1)*"a"

         return " ".join(words)



