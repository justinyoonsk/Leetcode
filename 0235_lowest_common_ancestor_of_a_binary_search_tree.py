# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(node, p_checker, q_checker):
            if node is None:
                return
            
            left = dfs(node.left, p_checker, q_checker)
            right = dfs(node.right, p_checker, q_checker)
            
            if node == p:
                p_checker = True 
            if node == q:
                q_checker = True
                
            if (node == p and (left or right)) or (node == q and (left or right)) or (left and right):
                self.ans = node
                
            return p_checker or q_checker or left or right
            
            
        dfs(root, p_checker = False, q_checker = False)
        return self.ans
    
    # O(N) time
    # O(N) space
