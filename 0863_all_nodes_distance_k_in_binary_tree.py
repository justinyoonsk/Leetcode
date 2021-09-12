# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root or not target:
            return [] 
        elif k == 0:
            return [target.val]
        
        queue = deque()
        queue.append(root)
        adjList = {} 
        
        while queue:
            curr = queue.popleft()
            if curr not in adjList:
                adjList[curr] = []
            
            if curr.left:
                adjList[curr].append(curr.left)
                if curr.left not in adjList:
                    adjList[curr.left] = [] 
                adjList[curr.left].append(curr)
                queue.append(curr.left)
            if curr.right:
                adjList[curr].append(curr.right)
                if curr.right not in adjList:
                    adjList[curr.right] = [] 
                adjList[curr.right].append(curr)
                queue.append(curr.right)
        
        queue = deque()
        queue.append(target)
        visited = set()
        depth = 0 
        result = [] 
        
        while queue and depth <= k:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr not in visited:
                    for child in adjList[curr]:
                        queue.append(child)
                    if depth == k:
                        result.append(curr.val)
                visited.add(curr)
            depth += 1
                        
        return result
                        
    # O(N) time
    # O(N) space
