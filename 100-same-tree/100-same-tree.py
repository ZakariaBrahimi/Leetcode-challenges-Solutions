# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # PRE-Order Traversing and than comparing
        # Visit Node - Go Left - Go Right
        current_p = p
        current_q = q
        if not current_q and not current_p:
            return True
        if (current_q == None or current_p == None) or (current_q.val != current_p.val):
            return False
        
        return self.isSameTree(current_p.left, current_q.left) and self.isSameTree(current_p.right, current_q.right)
        
        #return True
        """
        current_p = p
        current_q = q
        stack_p = []
        stack_q = []
        
        while (stack_q and stack_p) or (current_p and current_q):
            while current_p and current_q:
                if current_p.val != current_q.val:
                    return False
                stack_p.append(current_p)
                stack_q.append(current_q)
                current_q = current_q.left
                current_p = current_p.left
                
            current_p = stack_p.pop()
            current_q = stack_q.pop()
            
            current_q = current_q.right
            current_p = current_p.right
        
        return True"""
            
            
        