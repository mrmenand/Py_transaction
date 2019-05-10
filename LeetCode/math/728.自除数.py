# 728.自除数
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left,right+1):
            i = str(i)
            if i.find("0") == -1 and all(int(i)%int(j) == 0 for j in i):
                res.append(int(i))
        return res

