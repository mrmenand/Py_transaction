# 973. 最接近原点的 K 个点
class Solution:
    def kClosest(self,points,K):
         # points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points,key = lambda x: x[0] ** 2+ x[1] ** 2 )[:K]