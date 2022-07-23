# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        # POST-Order traversing 
        # ===>> Go left - Than right - And finally visit the node
        
        # Recursive Approach
        
        result = list()
        # Base Case
        if not root:
            return []
        
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)
        return result
        