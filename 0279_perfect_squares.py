class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0 
        perfect = []
        p = 1
        while p * p <= n:
            perfect.append(p * p)
            p += 1 
        
        for i in range(1,len(dp)):
            for c in perfect:
                if i - c < 0:
                    break 
                if i - c > 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
                if i - c == 0:
                    dp[i] = 1
        
        return dp[-1]
                
    # O(N * sqrt(N)) time
    # O(N) space
