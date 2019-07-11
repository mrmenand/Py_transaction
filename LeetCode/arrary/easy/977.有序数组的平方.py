##977.有序数组的平方
class Solution:
    def sortedSquares(self, A):
        return sorted([i**2 for i in A])