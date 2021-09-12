# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        res = [] 
        
        while queue:
            len_queue = len(queue) - 1 
            for i in range(len(queue)):
                curr = queue.popleft()
                if i == len_queue:
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return res
    
    # O(N) time
    # O(D) space for diameter
