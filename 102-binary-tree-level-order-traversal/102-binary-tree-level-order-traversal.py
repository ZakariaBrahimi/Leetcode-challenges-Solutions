# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        queue = [root]
        result = []
        level = []
        
        while queue:
            level = []
            
            for i in range(len(queue)):
                current = queue.pop()
                if current:
                    level.append(current.val)
                    if current.left:
                        queue.insert(0, current.left)
                    if current.right:
                        queue.insert(0, current.right)
            result.append(level)
        
        return result
                
                
        