# 290. 单词模式
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        hashmap = {}
        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                if words[i] not in hashmap.values():
                    hashmap[pattern[i]] = words[i]
                else:
                    return False
            elif hashmap[pattern[i]] != words[i]:
                return False

        return True





