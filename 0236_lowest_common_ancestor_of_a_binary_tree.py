# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_checker = False
        q_checker = False
        self.answer = None
        def dfs(node, p_checker, q_checker):
            if node is None:
                return 
            
            left = dfs(node.left, p_checker, q_checker)
            right = dfs(node.right, p_checker, q_checker)
            
            if node == p:
                p_checker = True
                
            if node == q:
                q_checker = True
            
            if left and right:
                self.answer = node 
            
            if node == p and (right or left):
                self.answer = node
            
            if node == q and (left or right):
                self.answer = node
                
            return p_checker or q_checker or left or right
            
            
        dfs(root, p_checker, q_checker)
        return self.answer
    
    # O(N) time
    # O(h) space
