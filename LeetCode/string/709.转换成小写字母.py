# 709. 转换成小写字母
class Solution:
    def toLowerCase(self, str):
            # str: str) -> str:
            return "".join([chr(ord(s)+32) if 65 <= ord(s) <= 90 else s for s in str])
