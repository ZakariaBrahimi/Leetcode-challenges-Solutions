# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]
        def dfs(root):
            if not root:
                return -1
        
            left             = dfs(root.left)
            right            = dfs(root.right)
            res[0] = max(res[0], left + right + 2)
        
            return 1 + max(left, right)
        dfs(root)
        return res[0]
        
        
        """def dfs(root):
            if not root:
                return [0, 0] # [hight, diameter]
        
            left             = dfs(root.left)
            right            = dfs(root.right)
            longest_diameter = max(left[1], right[1], left[0] + right[0])
        
            return [1 + max(left[0], right[0]), longest_diameter]
        
        return dfs(root)[1]"""