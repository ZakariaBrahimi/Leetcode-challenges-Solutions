# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        right_side_view = [root.val]
        queue = [root]
        
        while queue:
            for i in range(len(queue)):
                current = queue.pop()
                if current.left:
                    queue.insert(0, current.left)
                if current.right:
                    queue.insert(0, current.right)
            if queue:
                right_side_view.append(queue[0].val)
                
        return right_side_view