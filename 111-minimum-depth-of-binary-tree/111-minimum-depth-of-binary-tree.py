# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        # Breadth-First Search Algorithm
        if not root: return 0
        queue = [root]
        min_depth = 1
        
        while queue:
            for i in range(len(queue)):
                current = queue.pop()
                if not current.left and not current.right:
                    return min_depth
                if current:
                    if current.left:
                        queue.insert(0, current.left)
                    if current.right:
                        queue.insert(0, current.right)
            min_depth += 1
        
        
        # Depth-First Search
        # it's a worked solution but it's not efficient
        # because we are searching for a leaf node that is nearest to the root, 
        # this is why we have used Breadth-First Search rather than Depth-First Search Algorithm
        """  
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return 1 + min(left, right) if (left and right) else 1 + max(left, right)
        """