# 49. 字母异位词分组
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            d["".join(sorted(i))].append(i)
        return [*d.values()]
