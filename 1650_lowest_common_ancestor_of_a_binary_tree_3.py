"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path = []
        q_path = [] 
        def dfs(node, path):
            if node is None:
                return 
            path.append(node)
            if node.parent:
                dfs(node.parent, path)
        dfs(p, p_path)
        dfs(q, q_path)
        
        
        for i in p_path:
            if i in q_path:
                return i 
        
        for i in q_path:
            if i in p_path:
                return i 
            
    # O(N + M) time 
    # O(N + M) space
