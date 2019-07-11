# 950 按递增顺序显示
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ret = []
        for i in deck:
            if ret:
                ret.insert(0,i)
            ret.append(i)
        return ret


        # deck.sort()
        # n = len(deck)
        # if len(deck) <= 2:
        #     return deck
        # for i in range(2, n):
        #     deck.insert(n - i, deck[-1])
        #     print(deck)
        #     deck.pop()
        #     print(deck)
        # return deck