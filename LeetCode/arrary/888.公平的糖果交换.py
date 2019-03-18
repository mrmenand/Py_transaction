# 888. 公平的糖果交换
class Solution:
    def fairCandySwap(self, A,B): #Tip 测试不要在循环里面调用方法，不然时间很多
                      # A: List[int], B: List[int]) -> List[int]:
              sb =sum(B)
              sa =sum(A)
              cnt = int((sb-sa)/2)
              B = set(B)
              for x in A:
                   if x+cnt in B:
                       break

              return [x, x+cnt]


