# 383. 赎金信
class Solution:
    def canConstruct(self,ransomNote, magazine):
            # ransomNote: str, magazine: str) -> bool:
            for i in set(ransomNote):
                if ransomNote.count(i) > magazine.count(i):
                    return False
            return True