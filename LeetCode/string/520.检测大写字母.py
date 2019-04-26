# 520. 检测大写字母
class Solution:
    def detectCapitalUse(self,word):
           # word: str) -> bool:
           # return word == word.upper() or  word == word.lower() or word == word.title()
           return word.istitle() or word.isupper()  or word.islower()