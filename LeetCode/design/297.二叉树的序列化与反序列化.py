# 297. 二叉树的序列化与反序列化
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):

        def _serialize(node, string):
            if not node:
                string += "null,"
            else:
                string += str(node.val) + ","
                string = _serialize(node.left, string)
                string = _serialize(node.right, string)

            return string

        return _serialize(root, "")

    def deserialize(self, data):

        def _deserialize(node_list):
            if node_list[0] == "null":
                node_list.pop(0)
                return None

            root = TreeNode(node_list[0])
            node_list.pop(0)
            root.left = _deserialize(node_list)
            root.right = _deserialize(node_list)

            return root

        return _deserialize(data.split(","))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
