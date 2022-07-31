# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        left = 0
        right = 0
        def dfs(root, left, right):
            if not root: return 0
            left = dfs(root.left, left, right)
            right = dfs(root.right, left, right)
            """if left == 0 and right!= 0:
                return 1 + max(left, right)
            if right == 0 and left!= 0:
                return 1 + max(left, right)"""
            return 1 + min(left, right) if (left and right) else 1 + max(left, right)
        return dfs(root, left, right)