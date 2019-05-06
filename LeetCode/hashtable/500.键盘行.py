# 500. 键盘行
class Solution(object):
    def findWords(self, words):
       set1 = set("QWERTYUIOPqwertyuiop")
       set2 = set("asdfghjklASDFGHJKL")
       set3 = set("ZXCVBNMzxcvbnm")

       return [x for x in words if set(x) <= set1 or set(x) <= set2 or set(x) <= set3]