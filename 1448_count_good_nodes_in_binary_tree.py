# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0 
        def dfs(prev, node):
            if node is None:
                return 
            if node.val >= prev:
                self.goodNodes += 1 
                
            prev = max(prev, node.val)
            
            dfs(prev, node.left)
            dfs(prev, node.right)
            
        dfs(float("-inf"), root)
        return self.goodNodes
    
    # O(N) time
    # O(H) space
