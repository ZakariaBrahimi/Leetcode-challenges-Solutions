"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        isCloned = {}
        
        def dfs(node):
            if node.val in isCloned:
                return isCloned[node.val]
            
            copy = Node(node.val)
            isCloned[node.val] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None
        