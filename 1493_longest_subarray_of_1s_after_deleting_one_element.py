class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        so_far = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                dp[i] = dp[i-1] + 1
            elif nums[i] == 0:
                dp[i] = dp[i-1] - so_far
                so_far = dp[i-1] - so_far
                
        return max(dp) if max(dp) != len(dp) else max(dp)-1
    
    # O(N) time
    # O(N) space
                
