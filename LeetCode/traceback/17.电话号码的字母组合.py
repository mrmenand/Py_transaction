# 17. 电话号码的字母组合

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []

        ret = [""]
        for i in digits:
            ret = [x+y for x in ret for y in dic[i]]

        return ret
