# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        def check(node, level):
            if len(self.res) == level:
                self.res.append([])
            val = node.val
            self.res[level].append(val)
            if node.left:
                check(node.left, level + 1)
            if node.right:
                check(node.right, level + 1)

        check(root, 0)
        return self.res
