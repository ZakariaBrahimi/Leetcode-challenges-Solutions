# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        count = 0
        def dfs(root, maxVal):
            if not root: return 0
            
            if root.val >= maxVal:
                count = 1
            else:
                count = 0
            maxVal = max(maxVal, root.val)
            count += dfs(root.left, maxVal)
            count += dfs(root.right, maxVal)
            
            return count
    
        return dfs(root, root.val)
        