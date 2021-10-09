# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.answer = None
        def dfs(node):
            if node is None:
                return 
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                self.answer = node
            if (node == p or node == q) and (left or right):
                self.answer = node
            if node == p or node == q:
                return True
            if left or right:
                return True 
        
        dfs(root)
        return self.answer
    
    # O(N) time
    # O(h) space
