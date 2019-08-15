# 671. 二叉树中第二小的节点
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
            # root: TreeNode) -> int:
            if not root:
                return -1

            smallest = root.val
            stack = [root]
            tmp = []
            while stack:
                node = stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            tmp = list(set(tmp))
            tmp.sort()  ### tmp = sorted(list(set(tmp)))
            if len(tmp) == 1:
                return -1
            else:
                return tmp[1]

# class Solution:
#     def __init__(self):
#         self.l=[]
#     def findSecondMinimumValue(self, root: TreeNode) -> int:
#         if not root:
#             return -1
#         self.l.append(root.val)
#         self.findSecondMinimumValue(root.left)
#         self.findSecondMinimumValue(root.right)
#         self.l.sort&search()
#         base=self.l[0]
#         for i in self.l[1:]:
#             if i!=base:
#                 return i
#         return -1