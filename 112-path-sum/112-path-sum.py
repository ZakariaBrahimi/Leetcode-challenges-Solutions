# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
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
        