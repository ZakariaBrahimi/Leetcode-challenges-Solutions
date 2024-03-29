# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        
        result = []
        current = root
        if not current:
            return []
        
        result.append(current.val)
        result += self.preorderTraversal(current.left)
        result += self.preorderTraversal(current.right)
        return result
        """  result = []
        current = root
        stack = []
        
        while stack or current:
            if current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return result
        """
        
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            current = stack.pop()
            current = current.right
            
        return result
        """