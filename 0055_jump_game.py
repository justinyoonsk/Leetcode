class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
            
        dp = [False] * len(nums)
        dp[0] = True
        
        for i in range(len(nums)):
            if dp[i] == True:
                for j in range(1, min(nums[i]+1,len(nums))):
                    dp[i+j] = True
                    if dp[len(nums)-1] == True:
                        return True
        
        return False
    
    # O(N^2) time
    # O(N) space
