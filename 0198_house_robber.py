class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums
        if len(nums) == 1:
            return dp[0]
        if len(nums) == 2:
            return max(dp)
        if len(nums) == 3:
            return max(dp[0] + dp[2], dp[1])
        
        dp[2] = dp[0] + dp[2]
        for i in range(len(nums)):
            if i >= 3:
                dp[i] = dp[i] + max(dp[i-2], dp[i-3])
        
        return max(dp)
    
    # O(N) time
    # O(N) space
