# 20. 有效的括号
class Solution:
    def isValid(self, s):
        # s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in d:
                stack.append(c)
            elif not stack or d[c] != stack.pop():
                return False

        return not stack

# class Solution(object):
# #     def isValid(self, s):
# #         """
# #         :type s: str
# #         :rtype: bool
# #         """
# #         if len(s) % 2 != 0:
# #             return False
# #         lb = {'(': ')', '[': ']', '{': '}'}
# #         stack = []
# #
# #         for x in s:
# #             if x in lb:
# #                 stack.append(x)
# #             else:
# #                 if len(stack) == 0:
# #                     return False
# #                 top = stack.pop()
# #                 if lb[top] != x:
# #                     return False
# #         return len(stack) == 0
