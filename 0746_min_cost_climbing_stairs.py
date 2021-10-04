class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(dp)-1):
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])
        
        dp[len(cost)] = min(dp[len(cost)-1], dp[len(cost)-2])
        
        return dp[len(cost)]
    
    # O(N) time
    # O(N) space
