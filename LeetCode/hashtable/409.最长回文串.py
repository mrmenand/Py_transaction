# 409. 最长回文串
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:


        cnt, one = 0 , 0
        # hashmap = {}
        # for i in s:
        #     if i not in hashmap:
        #         hashmap[i] = 0
        #     hashmap[i] += 1
        hashmap = Counter(s)

        for v in hashmap.values():
            if v % 2 == 0:
                cnt += v
            else:
                cnt += v-1
                one = 1

        return cnt + one



