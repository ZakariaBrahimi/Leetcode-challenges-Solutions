# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True, 0]
        
            left_height  = dfs(root.left)
            right_height = dfs(root.right)
            is_balanced   = (left_height[0] and right_height[0] and
                             abs(left_height[1] - right_height[1]) <= 1)
        
            return [is_balanced, max(left_height[1], right_height[1]) + 1]
        
        return dfs(root)[0]
    
    
            
           