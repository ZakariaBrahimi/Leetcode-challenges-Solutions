# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))
        
        
        """
       if not root: return True
        if root and not root.left and not root.right: return True
        change = [root.val]
        freeze(change)
        def validSubTree(root):
            if root and not root.left and root.right:
                right = root.right
                if change[0] < right.val and root.val < right.val:
                    return True
                else:
                    return False
                
            if root and root.left and not root.right:
                left = root.left
                if change[0] > left.val and root.val > left.val:
                    return True
                else:
                    return False
                
            left = root.left
            right = root.right
            if change[0] < right.val and change[0] > left.val and root.val < right.val and root.val > left.val:
                return True
            else:
                return False

        
        if validSubTree(root):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False        """