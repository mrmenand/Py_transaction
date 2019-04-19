# 941. 有效的山脉数组
class Solution:
    def validMountainArray(self,A):
            # A: List[int]) -> bool:
            if len(A) < 3 :
                return False
            i,j = 0, len(A)-1
            while i < j:
                if A[i] >= A[i+1]:
                    break
                i += 1
            while i < j:
                if A[j] >= A[j-1]:
                    break

                j -= 1

            return i ==j and i != 0 and j != len(A)-1




