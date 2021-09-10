# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = float("-inf")
        def dfs(node):
            if node is None:
                return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            
            max_curr = node.val + left + right
            self.maximum = max(self.maximum, max_curr)
            
            return node.val + max(left,right)
        
        dfs(root)
        return self.maximum
    
    # O(N) time
    # O(h) space
