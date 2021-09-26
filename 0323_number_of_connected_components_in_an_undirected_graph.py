class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        for u, v in edges:
            if u not in adj_list:
                adj_list[u] = [] 
            if v not in adj_list:
                adj_list[v] = [] 
            adj_list[u].append(v) 
            adj_list[v].append(u)
        print(adj_list)
        
        output = 0 
        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            if node in adj_list:
                for nei in adj_list[node]:
                    dfs(nei)
            
            
        for i in range(n):
            if i not in visited:
                output += 1 
                dfs(i)
        
        return output
    
    # O(E + V) time 
    # O(E + V) space
