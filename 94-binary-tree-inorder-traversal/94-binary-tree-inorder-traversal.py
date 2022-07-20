# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        # IN-Order traversing
        # lnr ===>> Left - Node - Right
        
        result = []
        current = root
        if not current:
            return []
        result += self.inorderTraversal(current.left)
        result.append(current.val)
        result += self.inorderTraversal(current.right)
        return result
            