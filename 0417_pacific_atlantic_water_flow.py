class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        atl = set()
        pac = set()
        
        def dfs(r, c, visited, prevHeight):
            if r >= rows or c >= columns or (r, c) in visited or r < 0 or c < 0 or heights[r][c] < prevHeight:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, columns - 1, atl, heights[r][columns - 1])
            
        for c in range(columns):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
            
        res = [] 
        for r in range(rows):
            for c in range(columns):
                if (r , c) in atl and (r, c) in pac:
                    res.append((r, c))
        
        return res
            
    # O(n*m) time n number of rows, m number of columns
    # O(n*m) space n number of rows, m number of columns for recursion stack 
