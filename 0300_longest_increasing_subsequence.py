class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        
        for i in range(len(dp)):
            if i > 0:
                for j in range(i-1,-1,-1):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[i], 1 + dp[j])
                        
        return max(dp)
    
    # O(N^2) time
    # O(N) space
