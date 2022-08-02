# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        
        
        
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right
        
        
        """if not subRoot and root:
            return False"""
        
        
        
        
    def isSame(self, root, subRoot):
        if not root and not subRoot:
            return True
            
        if root and subRoot and root.val == subRoot.val:
            left = self.isSame(root.left, subRoot.left)
            right = self.isSame(root.right, subRoot.right)
            return left and right
        else:
            return False