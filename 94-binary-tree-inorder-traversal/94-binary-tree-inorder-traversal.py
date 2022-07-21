# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        # IN-Order traversing
        # lnr ===>> go left - than return the node - go right
        
        # Iterative Approach
        # Time Complexity is: O(n)
        # Space Complexity is: O(n), where n is the stack data sctructure used to store nodes
        # the worst case of space complexity is when we dealing with a tree conceptually like a linked list
        # Where we should go left and append all left nodes to the stack one by one
        
        
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
            
        return result
        
        
        
        # Recursive Solution
        # Time Complexity is: O(n), where n is the number of all Tree Nodes
        # Space Complexity is: O(n), where n is the call stack used in recursive manner
        
        """
        result = []
        current = root
        if not current:
            return []
        result += self.inorderTraversal(current.left)
        result.append(current.val)
        result += self.inorderTraversal(current.right)
        return result
        """
            