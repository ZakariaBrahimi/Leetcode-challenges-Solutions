# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return 1 + min(left, right) if (left and right) else 1 + max(left, right)
        
        """def dfs(root, left, right):
            if not root: return 0
            left = dfs(root.left, left, right)
            right = dfs(root.right, left, right)
            return 1 + min(left, right) if (left and right) else 1 + max(left, right)
        return dfs(root, left, right)"""