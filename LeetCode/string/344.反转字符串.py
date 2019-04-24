# 344. 反转字符串
class Solution:
    def reverseString(self, s):
        # s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

