# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        # POST-Order traversing 
        # ===>> Go left - Than right - And finally visit the node
        
        # Iterative Approach
        # POST-Order Traversing: left -> right -> Node
        # Keep go to the left until reach the limit of the tree 
        # + at the same time we visited the node add it to the stack
        # Than check if this last node have a right node or not !
        # if yes, go for it, than go left again and again
        # otherwise, append it to the result, and pop it from the stack
        # + And check if the last poped item from the stack actually the right node for the last item in the stack
        # if it is, pop(cur we have finishied the right subtree), otherwise, go right
        
        result = []
        stack = []
        current = root
        
        while(current or stack):
            while current != None:
                stack.append(current)
                current = current.left
            temp = stack[-1]
            if temp.right != None:
                current = temp.right
            else:
                result.append(temp.val)
                temp = stack.pop()
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    result.append(temp.val)
                    
        return result 