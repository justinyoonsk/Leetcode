# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1]) #[15,20,7] [9,15,7,20]. [7] [9,15,7]
        root.left = self.buildTree(inorder[:mid], postorder[:mid]) # [9] [9,15,7,20], [15] [9,15,7]
        
        return root

    # O(N) time
    # O(N) space
