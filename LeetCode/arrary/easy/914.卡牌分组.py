# 914. 卡牌分组
class Solution:
    def hasGroupsSizeX(self, deck):
        # deck: List[int]) -> bool:
        tmp = {}
        for i in deck:
            if i in tmp.keys():
                tmp[i] += 1
            else:
                tmp[i] = 1
        print(tmp.values())
        min_value = min(tmp.values())
        for x in range(2,min_value+1):
            if all(v%x ==0 for v in tmp.values()):
                return True
        return False

