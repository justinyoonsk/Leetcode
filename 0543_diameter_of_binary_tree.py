# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 0
        
        distance = 0 
        self.max_len = float("-inf")
        
        def dfs(node, distance):
            if node is None:
                return 0 
            if node.left is None and node.right is None:
                return distance
            left = dfs(node.left, distance + 1)
            right = dfs(node.right, distance + 1)
            self.max_len = max(self.max_len, left - distance + right - distance)
            
            return max(left,right)
            
        dfs(root, distance)
        return self.max_len
    
    # O(N) time
    # O(H) space
