# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def compare(node, mini, maxi):
            if node is None:
                return True
            if node.val <= mini.val or node.val >= maxi.val:
                return False
            
            left = compare(node.left, mini, node)
            right = compare(node.right, node, maxi)
            
            return left and right
            
            
        return compare(root, TreeNode(float("-inf")), TreeNode(float("inf")))
    
    # O(N) time
    # O(N) space
