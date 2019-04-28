# 925. 长按键入
class Solution:
    def isLongPressedName(self,name, typed):
            # name: str, typed: str) -> bool:
            i, j = 0, 0
            n, m = len(name), len(typed)
            last = None
            while i < n and j < m:
                if name[i] == typed[j]:
                     last = name[i]
                     print(last)
                     i += 1
                     j += 1
                elif last == typed[j]:
                     j += 1
                else:
                    return False

            while j < m and typed[j] == last:
                j += 1
            return  i==n and j==m

# class Solution:
#     def isLongPressedName(self, name, typed):
#         i = j = 0
#         while i<len(name) and j<len(typed):
#             if name[i]==typed[j]:
#                 i+=1
#             j+=1
#         return i==len(name)