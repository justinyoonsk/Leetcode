class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0 
        
        for i in range(len(dp)):
            if i > 0:
                if i in coins:
                    dp[i] = 1 
                else:
                    for j in coins:
                        if i - j >= 0:
                            dp[i] = min(dp[i], 1 + dp[i - j])
        
        return dp[amount] if dp[amount] != float("inf") else -1
    
    # O(N) time
    # O(N) space
