# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        # Iterative Solution
        
        stack = [root]
        
        while len(stack)>0:
            node = stack.pop()
            if node != None:
                hold = node.left
                node.left = node.right
                node.right = hold
            
                stack += node.left, node.right
 
        return root
        
        # Recursive Solution
        """
        if not root: return 
        
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        """
        