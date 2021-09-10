# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return root.val
        
        self.answer = float("-inf")
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.answer = max(self.answer, left + right + node.val, node.val, node.val + left, node.val + right)
            
            return max(left + node.val, right + node.val, node.val)
            
        dfs(root)
        return self.answer
    
    # O(N) time
    # O(h) space
