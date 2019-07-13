# 950 按递增顺序显示
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ret = []
        for i in deck:
            if ret:
                ret.insert(0,ret.pop())
            ret.insert(0,i)

        return ret



