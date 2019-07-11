# 1002. 查找常用字符
class Solution:
    def commonChars(self, A):
            # A: List[str]) -> List[str]:
         res = []
         for i in A[0]:
             judge = True
             for j in range(1,len(A)):
                 if i not in A[j]:
                      judge =False
                      break

             if judge:
                 res.append(i)
                 for j in range(1,len(A)):
                     index = A[j].find(i)
                     A[j] = A[j][:index] + A[j][index + 1:]
                     # A[j]=A[j].remove(A[j].find(i)) 'str' object has no attribute 'remove'


         return res
A =["bella","label","roller"]
test = Solution()
print(test.commonChars(A))






