# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def valid(root, min_val, max_val):
            if not root:
                return True
            if not (root.val < max_val and root.val > min_val):
                return False

            return valid(root.left, min_val, root.val) and valid(
                root.right, root.val, max_val
            )

        return valid(root, float("-inf"), float("inf"))       