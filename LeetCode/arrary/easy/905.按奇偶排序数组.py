#905.按奇偶排序数组
class Solution:
    def sortArrayByParity(self, A):
        #List[int]) -> List[int]:
        odd = []
        even = []
        for i  in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

        return even+odd




