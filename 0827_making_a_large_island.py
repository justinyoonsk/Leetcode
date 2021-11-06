class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        areas = {}
        seen = set()
            
        def area(r, c, index):
            queue = deque()
            queue.append((r, c))
            seen.add((r, c))
            grid[r][c] = index
            if index not in areas:
                areas[index] = 1
            while queue:
                row, col = queue.pop()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    if row + dr in range(rows) and col + dc in range(columns) and grid[row+dr][col+dc] == 1 and (row+dr, col+dc) not in seen:
                        queue.append((row+dr, col+dc))
                        seen.add((row+dr, col+dc))
                        grid[row+dr][col+dc] = index
                        areas[index] += 1 
                
        index = 1 
        for r in range(rows):
            for c in range(columns):
                if (r, c) not in seen and grid[r][c] == 1:
                    index = index + 1
                    area(r, c, index)
        has_zero = False
        max_area = 1 
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    has_zero = True
                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    a = 0 
                    saw = set()
                    for dr, dc in directions:
                        if r + dr in range(rows) and c + dc in range(columns) and grid[r+dr][c+dc] >= 2 and grid[r+dr][c+dc] not in saw:
                            a += areas[grid[r+dr][c+dc]]
                            saw.add(grid[r+dr][c+dc])
                            
                    max_area = max(max_area, a+1)
                    
        return max_area if has_zero else rows * columns
                            
    # O(N^2) time N is the length and width of the grid
    # O(N^2) space addition space used for dfs by area
