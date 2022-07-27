# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root: return 
        if not root.left and not root.right:
            return root
        
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        
        """stack = []
        current = root
        
        if not root: return None
        
        k = root.left
        root.left = root.right
        root.right = k
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            temp = stack[-1]
            if temp.right:
                current = temp.right
            else:
                stack.pop()
                temp = stack[-1]
                ch = temp.left
                temp.left = temp.right
                temp.right = ch
                temp = temp.right
                while stack and stack[-1].right == temp:
                    temp = stack.pop()
        
        return root"""