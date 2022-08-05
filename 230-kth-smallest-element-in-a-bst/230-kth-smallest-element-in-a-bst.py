class Solution(object):
    def kthSmallest(self, root, k):
        def inorder(root):
            output = list()
            if not root: return []
            output += inorder(root.left) 
            output.append(root.val)
            output += inorder(root.right) 
            
          
            return output
        return inorder(root)[k-1]

    """
class Solution(object):
    def kthSmallest(self, root, k):
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return inorder(root)[k-1]
    """