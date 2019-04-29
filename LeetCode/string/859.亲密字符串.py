# 859. 亲密字符串
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
              if len(A) != len(B) or len(A) <2 or len(B) <2 :
                  return False
              if A == B:
                  if len(A) - len(set(A)) > 0:
                      return True
                  return False

              a,b = [],[]
              for i in range(len(A)):
                  if A[i] != B[i]:
                      a.append(A[i])
                      b.append(B[i])

              if len(a) != 2 and len(b) != 2:
                  return False

              return a == b[::-1]
