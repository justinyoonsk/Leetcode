class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0 
        for i in range(0,len(nums)):
            for j in range(1,nums[i]+1):
                if i+j < len(dp):
                    dp[i + j] = min(dp[i + j], (dp[i] + 1))
        
        return dp[-1]
                    
    # O(N^2) time
    # O(N) space
