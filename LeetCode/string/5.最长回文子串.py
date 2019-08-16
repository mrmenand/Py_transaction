# 5. 最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        ret = ""
        for r in range(n):
            for l in range(r, -1, -1):
                if s[l] == s[r] and (r - l < 2 or dp[r - 1][l + 1]):
                    dp[r][l] = 1
                if dp[r][l] and r - l + 1 > max_len:
                    max_len = r - l + 1
                    ret = s[l:r + 1]

        return ret
