# 447. 回旋镖的数量
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in points:
            dic = {}
            for j in points:
                dis = (i[0]-j[0])**2 + (i[1]-j[1])**2
                if dis not in dic:
                    dic[dis] = 0
                dic[dis] += 1

            for value in dic.values():
                if value >= 2:
                    res += value * (value - 1)


        return res

