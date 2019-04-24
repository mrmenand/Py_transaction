# 521. 最长特殊序列 Ⅰ
class Solution:
    def findLUSlength(self,a,b):
            # a: str, b: str) -> int:
            if a == b:
                return -1
            return max(len(a),len(b))