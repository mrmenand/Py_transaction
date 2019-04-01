# 155. 最小栈
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min = None
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.stack.append(x)
#         if self.min == None or self.min > x:
#             self.min = x
#
#     def pop(self):
#         """
#         :rtype: void
#         """
#         popItem = self.stack.pop()
#         if len(self.stack) == 0:
#             self.min = None
#             return popItem
#
#         if popItem == self.min:
#             self.min = self.stack[0]
#             for i in self.stack:
#                 if i < self.min:
#                     self.min = i
#         return popItem
#
#        def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.min

