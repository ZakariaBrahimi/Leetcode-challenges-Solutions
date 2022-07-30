# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        # Iterative Approach
        if not root:
            return False
        
        current = root
        result = 0
        stack = []
        
        while stack or current:
            while current:
                result += current.val
                stack.append(current)
                current = current.left
            temp = stack[-1]
            if temp.right:
                current = temp.right
            else:
                if (not temp.left) and (not temp.right) and (result == targetSum):
                    return True
                temp = stack.pop()
                result -= temp.val
                while stack and stack[-1].right == temp:
                    temp = stack.pop()
                    result -= temp.val
        
        return False

        
        # Recursive Approach
        """
        current_sum = 0
        def dfs(root, current_sum):
            current = root
            if not current: 
                return False
            current_sum += current.val
            if not current.left and not current.right:
                return targetSum == current_sum
            
            return (dfs(current.left, current_sum) or
            dfs(current.right, current_sum)
            )
        return dfs(root, current_sum)
        """
        
      
         
        