#922.按奇偶排序数组 II
class Solution:
    def sortArrayByParity(self, A):
        #List[int]) -> List[int]:
        odd = []
        even = []
        B = []
        for i  in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

        for i in range(len(A)):
            if i%2==0:
                B.append(even[int(i/2)])
            else:
                B.append(odd[int(i//2)])

        return B
A= [4,2,5,7,6,9]
test = Solution()
print(test.sortArrayByParity(A))



