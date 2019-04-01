# 844. 比较含退格的字符串
class Solution:
    def backspaceCompare(self, S, T):
             # S: str, T: str) -> bool:
             s = []
             t = []
             for i in S:
                 if i=="#":
                     if s == []:
                         s = []
                     else:
                         s.pop()

                 else:
                     s.append(i)

             for j in T:
                if j == "#":
                    if t == []:
                        t = []
                    else:
                        t.pop()

                else:
                    t.append(j)

             if s == t:
                 return True
             else:
                 return False

# 从判断相等到
# class Solution:
#     def backspaceCompare(self, S, T):
#         """
#         :type S: str
#         :type T: str
#         :rtype: bool
#         """
#
#         def delspace(string):
#             stack = []
#             for i in string:
#                 if i != '#':
#                     stack.append(i)
#                 elif stack:
#                     stack.pop()
#
#             return stack
#
#         if not S and not T:
#             return True
#         elif not S or not T:
#             return False
#         return delspace(S) == delspace(T)

