# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def valid(node, min_val, max_val):
            if not node:
                return True
            if not (node.val < max_val and node.val > min_val):
                return False

            return valid(node.left, min_val, node.val) and valid(
                node.right, node.val, max_val
            )

        return valid(root, float("-inf"), float("inf"))       