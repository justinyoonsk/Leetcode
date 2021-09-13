# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:      
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        def match(node, subnode):
            if node is None and subnode is None:
                return True
            if node is None or subnode is None:
                return False
            if node.val != subnode.val:
                return False
            return match(node.left, subnode.left) and match(node.right, subnode.right)
        
        if match(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    # O(N) time
    # O(N) space
