class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        preRow1 = grid[0].copy()
        preRow2 = grid[1].copy()
        
        for i in range(1, N):
            preRow1[i] += preRow1[i - 1]
            preRow2[i] += preRow2[i - 1]
        
        print(preRow1, preRow2)
        res = float("inf")
        
        for i in range(N):
            top = preRow1[-1] - preRow1[i]
            bottom = preRow2[i - 1] if i > 0 else 0
            secondRobot = max(top, bottom)
            res = min(res, secondRobot)
            
            print(top)
            print(bottom)
            
        return res
        
    # O(N) time
    # O(N) space
