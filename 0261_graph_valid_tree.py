class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if edges == [] and n == 1:
            return True
        if edges == [] and n > 1:
            return False
        visited = set()
        adjList = {}
        
        for n1, n2 in edges:
            if n1 not in adjList:
                adjList[n1] = [] 
            if n2 not in adjList:
                adjList[n2] = []
            adjList[n1].append(n2)
            adjList[n2].append(n1)
            
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            
            for j in adjList[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
            
        return dfs(edges[0][0], -1) and len(visited) == n
    
    # O(E + V) time
    # O(E + V) space
