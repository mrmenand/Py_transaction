# 67. 二进制求和
class Solution:
    def addBinary(self,a,b):
            # a: str, b: str) -> str:
            return bin(int(a,2)+int(b,2))[2:]