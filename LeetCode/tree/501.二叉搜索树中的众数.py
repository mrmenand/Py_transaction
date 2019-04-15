# 501. 二叉搜索树中的众数
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter


class Solution:
    def findMode(self, root):
            # root: TreeNode) -> List[int]:
            if not root:
                return []
            stack = [root]
            dic = {}
            while stack:
                node = stack.pop()
                if node.val not in dict:
                    dict[node.val] = 1
                dict[node.val] +=1
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            max_counter = max(dic.values())
            res = []
            for key,value in dic.items():
                if value == max_counter:
                    res.append(key)
            return res


