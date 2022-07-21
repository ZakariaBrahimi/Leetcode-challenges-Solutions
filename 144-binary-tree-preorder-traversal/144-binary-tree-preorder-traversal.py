# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
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