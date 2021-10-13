class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0]* (len(text1)+1) for _ in range(len(text2)+1)  ]
        
        for j in range(len(text2)-1,-1,-1):
            for i in range(len(text1)-1,-1,-1):
                if text2[j] == text1[i]:
                    grid[j][i] = 1 + grid[j+1][i+1]
                else:
                    grid[j][i] = max(grid[j][i+1], grid[j+1][i])
                 
        return grid[0][0]
                    
    # O(N*M) time
    # O(N*M) space
