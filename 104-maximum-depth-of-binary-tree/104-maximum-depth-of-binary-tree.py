# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # Iterative Approach
        # Using PRE-Order Tree Traversing
        # Time Copmlexity: O(n), where n is the height of the tree
        # Space Com:plexity: O(n), the worst case is storing all tree nodes on the stack
        
        if root == None:
            return 0
        result = -1
        stack = []
        current = root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            temp = stack[-1]
            if temp.right:
                current = temp.right
            else:
                result = max(result, len(stack))
                temp = stack.pop()
                while stack and stack[-1].right == temp and not current:
                    temp = stack.pop()
        
        return result
    
        # Recursive Approach
        # Time Copmlexity: O(n), where n is the height of the tree
        # Space Com:plexity: O(n), we need extra space for the call stack
        """
        if not root:
            return 0
        
        return 1 + min(self.maxDepth(root.left), self.maxDepth(root.right)) 
        """