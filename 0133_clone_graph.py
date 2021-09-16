"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            
            copy = Node(node.val)
            hashmap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy
            
            
        return dfs(node) if node else None
            
    # O(N+M) time N number of nodes, M number of edges 
    # O(N) hashmap and the recursion stack
