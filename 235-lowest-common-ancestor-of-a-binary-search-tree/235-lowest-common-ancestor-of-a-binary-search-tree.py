# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        current = root
        while current:
            if current.val < p.val and current.val < q.val:
                current = current.right
            if current.val > p.val and current.val > q.val:
                current = current.left
            if (current.val >= p.val and current.val <= q.val) or (current.val >= q.val and current.val <= p.val):
                return current