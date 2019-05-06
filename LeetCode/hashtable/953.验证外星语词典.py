# 953. 验证外星语词典
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
            return words == sorted(words, key = lambda x: [order.index(i)  for i in x])
