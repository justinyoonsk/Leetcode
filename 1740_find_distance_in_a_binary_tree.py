# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0 
        def dfs(node, depth):
            if node is None:
                return 
            
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            
            if left and right:
                return left - depth + right - depth
            
            if (node.val == p or node.val == q) and (left or right):
                if left:
                    return left - depth 
                elif right:
                    return right - depth 
                
            if node.val == p or node.val == q:
                return depth 
            
            return left or right
        
        return dfs(root, 0)
    
    # O(N) time
    # O(h) space 
