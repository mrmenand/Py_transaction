# 599. 两个列表的最小索引总和
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        hashmap = {}
        for i in common:
            hashmap[i] = list1.index(i) + list2.index(i)
        minidx = min(hashmap.values())
        return [i for i in hashmap if hashmap[i] == minidx]


