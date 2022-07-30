# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """if not root:
            return False
        
        current = root
        result = 0
        stack = [1,]
        
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
                while temp or stack or stack[-1].right == temp:
                    temp = stack.pop()
                    result -= temp.val
        
        return False"""
        
        
        
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
        def hasPathSum(self, node, s):
        if not node: return False
        ans = 0
        subSum = s - node.val
 
        # If we reach a leaf node and sum becomes 0, then
        # return True
        if(subSum == 0 and node.left == None and node.right == None):
            return True
 
        # Otherwise check both subtrees
        if node.left is not None:
            ans = ans or self.hasPathSum(node.left, subSum)
        if node.right is not None:
            ans = ans or self.hasPathSum(node.right, subSum)
 
        return ans
        """
        
        
        
        
        """current = root
        result = 0
        
        if not current: return 0
        if result == targetSum:
            return True
        else:
            result += current.val
            self.hasPathSum(current.left, targetSum)
            self.hasPathSum(current.right, targetSum)
        
        return result"""
        